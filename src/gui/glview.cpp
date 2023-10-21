#include "gui/glview.h"

#include "gui/model.h"
#include "gui/shaders.h"
#include "halfedge/face.h"

#include <QKeyEvent>
#include <QtOpenGL/QOpenGLShaderProgram>


#ifndef GL_MULTISAMPLE
#ifdef Q_OS_ANDROID
#define GL_MULTISAMPLE 0x809D
#endif
#endif

GLView::GLView(Model* model, QWidget* parent) :
        QOpenGLWidget(parent), m_model(model) {
}

GLView::~GLView() {
    //destroy the programs
    if (m_program != nullptr) {
        makeCurrent();
        m_vbo.destroy();
        delete m_program;
        m_program = nullptr;
        doneCurrent();
    }

    if (m_programEdge != nullptr) {
        makeCurrent();
        m_vboEdge.destroy();
        delete m_programEdge;
        m_programEdge = nullptr;
        doneCurrent();
    }
}

static void qNormalizeAngle(int& angle) {
    //normalize the angle
    while (angle < 0) {
        angle += 360 * 2;
    }

    while (angle > 360 * 2) {
        angle -= 360 * 2;
    }
}

void GLView::setXRotation(int angle) {
    //normalize the angle and set it to the x rotation
    qNormalizeAngle(angle);
    m_xRot = angle;
}

void GLView::setYRotation(int angle) {
    //normalize the angle and set it to the y rotation
    qNormalizeAngle(angle);
    m_yRot = angle;
}

void GLView::meshChanged() {
    //------for the faces------//
    m_vao.bind();
    m_vbo.bind();
    //allocate necessary memory
    m_vbo.allocate(nullptr, m_model->count() * sizeof(GLfloat));

    //enable enough attrib array for all the data of the mesh's vertices
    glEnableVertexAttribArray(0);
    glEnableVertexAttribArray(1);
    glEnableVertexAttribArray(2);
    glEnableVertexAttribArray(3);
    //3 coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), nullptr);
    //3 coordinates of the vertex's normal
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //the ID
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    //whether it's selected or not, to simplify the code, a negative value means not selected
    //while a positive value means selected
    glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(7 * sizeof(GLfloat)));
    m_vbo.release();
    m_vao.release();

    //------for the edges------//
    m_vaoEdge.bind();
    m_vboEdge.bind();
    //allocate necessary memory
    m_vboEdge.allocate(nullptr, m_model->countEdge() * sizeof(GLfloat));

    //enable enough attrib array for all the data of the edge's vertex
    glEnableVertexAttribArray(0);
    //coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), nullptr);
    m_vboEdge.release();

    //update the view
    update();
}

void GLView::initializeGL() {
    //init OpenGL
    initializeOpenGLFunctions();

    //to hide faces that are behind others
    glEnable(GL_DEPTH_TEST);

    //print information
    QString val = QString::fromLatin1((char*) glGetString(GL_VERSION));
    qDebug() << "OpenGL version : " << val;
    val = QString::fromLatin1((char*) glGetString(GL_SHADING_LANGUAGE_VERSION));
    qDebug() << "GLSL version : " << val;

    //for compatibility
    m_vao.create();
    m_vaoEdge.create();

    m_vbo.create();
    m_vboEdge.create();

    //background
    glClearColor(0.3f, 0.3f, 0.3f, 1.0f);

    //init shader for mesh
    m_program = new QOpenGLShaderProgram();
    m_program->addShaderFromSourceCode(QOpenGLShader::Vertex, vertexShaderSource);
    m_program->addShaderFromSourceCode(QOpenGLShader::Fragment, fragmentShaderSource);
    m_program->bindAttributeLocation("vertex", 0);
    m_program->bindAttributeLocation("normal", 1);
    m_program->bindAttributeLocation("ID", 2);
    m_program->bindAttributeLocation("isSelected", 3);
    m_program->link();

    //get locations of uniforms
    m_program->bind();
    m_projMatrixLoc = m_program->uniformLocation("projMatrix");
    m_mvMatrixLoc = m_program->uniformLocation("mvMatrix");
    m_normalMatrixLoc = m_program->uniformLocation("normalMatrix");
    m_lightPosLoc = m_program->uniformLocation("lightPos");
    m_cameraPosLoc = m_program->uniformLocation("cameraPosition");
    m_modelMatrixLoc = m_program->uniformLocation("model");
    m_isPickingLoc = m_program->uniformLocation("isPicking");

    //init shader for edges
    m_programEdge = new QOpenGLShaderProgram();
    m_programEdge->addShaderFromSourceCode(QOpenGLShader::Vertex, vertexShaderSourceEdge);
    m_programEdge->addShaderFromSourceCode(QOpenGLShader::Fragment, fragmentShaderSourceEdge);
    m_programEdge->bindAttributeLocation("vertex", 0);
    m_programEdge->link();

    //get location of uniforms
    m_programEdge->bind();
    m_projMatrixLocEdge = m_programEdge->uniformLocation("projMatrix");
    m_mvMatrixLocEdge = m_programEdge->uniformLocation("mvMatrix");

    //memory allocation
    meshChanged();

    //set light position
    m_program->bind();
    m_program->setUniformValue(m_lightPosLoc, QVector3D(0.0f, 0.0f, 100.0f));
    m_program->release();
}

void GLView::paintGL() {
    //write mesh data
    m_vbo.bind();
    m_vbo.write(0, m_model->constData(), m_model->count() * sizeof(GLfloat));
    m_vbo.release();

    //write edge data
    m_vboEdge.bind();
    m_vboEdge.write(0, m_model->constDataEdge(), m_model->countEdge() * sizeof(GLfloat));
    m_vboEdge.release();

    //compute camera and world matrices
    computeMVMatrices();

    //get normal matrix of the world
    QMatrix3x3 normalMatrix = m_world.normalMatrix();

    //set values for uniforms
    m_program->bind();
    m_program->setUniformValue(m_projMatrixLoc, m_proj);
    m_program->setUniformValue(m_mvMatrixLoc, m_camera * m_world);
    m_program->setUniformValue(m_normalMatrixLoc, normalMatrix);
    m_program->setUniformValue(m_cameraPosLoc, m_cameraPos);
    m_program->setUniformValue(m_modelMatrixLoc, m_world);

    //click management
    if (m_clicked) {
        clickFaceManagement();
        m_clicked = false;
    }

    //clear buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    //draw faces
    //for compatibility
    m_vao.bind();
    //m_vbo.bind();
    m_program->bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCount());
    m_program->release();

    //bind edge shader
    m_programEdge->bind();

    //camera translate to set lines
    //in front of the polyhedron
    float transCam = qMax(m_cameraDistance / 1000.0f, 0.001f);

    //the translation is done in the direction of the camera position and where it looks
    m_camera.translate(transCam * (m_cameraPos - m_cameraLookAt).normalized());

    //set uniforms
    m_programEdge->setUniformValue(m_projMatrixLocEdge, m_proj);
    m_programEdge->setUniformValue(m_mvMatrixLocEdge, m_camera * m_world);
    m_camera.translate(-transCam * (m_cameraPos - m_cameraLookAt).normalized());

    //draw edges
    //for compatibility
    m_vaoEdge.bind();
    m_vboEdge.bind();
    glDrawArrays(GL_LINES, 0, m_model->vertexCountEdge());
    m_programEdge->release();
}


void GLView::resizeGL(int w, int h) {
    //reset the projection with the new window size
    m_proj.setToIdentity();
    m_proj.perspective(45.0f, GLfloat(w) / h, 0.01f, 100.0f);
    m_screenSize = QSize(w, h);
}


void GLView::mousePressEvent(QMouseEvent* event) {
    //update the mouse positions
    m_lastPos = event->pos();
    m_clickPos = event->pos();
}

void GLView::mouseMoveEvent(QMouseEvent* event) {
    //compute rotations
    int dx = event->position().toPoint().x() - m_lastPos.x();
    int dy = event->position().toPoint().y() - m_lastPos.y();

    if (event->buttons() & Qt::LeftButton) {
        setXRotation(m_xRot + dy);
        setYRotation(m_yRot + dx);
    }

    if (event->buttons() & Qt::RightButton) {
        m_translateX += dx;
        m_translateY += dy;
    }

    m_lastPos = event->pos();

    //update after rotations
    update();
}

void GLView::wheelEvent(QWheelEvent* event) {
    //compute new distance of camera from object
    float val = (float) event->angleDelta().y() / 500.0f;

    if (m_cameraDistance - val > 0.0f) {
        m_cameraDistance -= val;
        m_camera.translate(0.0f, 0.0f, (float) event->angleDelta().y() / 500.0f);

        //update if the distance changed
        update();
    }
}

void GLView::mouseReleaseEvent(QMouseEvent* event) {
    QVector2D v(event->pos() - m_clickPos);

    //if there was a click
    if (v.length() < 5.0f) {
        //then will do the edge or face selection
        m_clicked = true;
        update();
    }
}

void GLView::computeMVMatrices() {
    m_world.setToIdentity();
    m_camera.setToIdentity();

    //otherwise the camera will be at its default state
    m_cameraPos = QVector3D(0.0f, 0.0f, m_cameraDistance);
    m_cameraLookAt = QVector3D(0.0f, 0.0f, 0.0f);
    m_camera.lookAt(m_cameraPos, m_cameraLookAt, QVector3D(0.0f, 1.0f, 0.0f));

    //and we set the right orientation of the world
    m_world.rotate(m_xRot / 2.0f, 1, 0, 0);
    m_world.rotate(m_yRot / 2.0f, 0, 1, 0);
    m_world.translate(m_translateX / 10.0f, m_translateY / 10.0f);
}

void GLView::clickFaceManagement() {
    //white background
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);

    //no multisample
    glDisable(GL_MULTISAMPLE);
    //clear buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    //indicates to the shader that we're doing a selection
    m_program->bind();
    m_program->setUniformValue(m_isPickingLoc, true);

    //draw faces
    m_vao.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCount());

    //render the scene
    QImage image = grabFramebuffer();

    //compute real click position on image based on screen size
    //because on android, screen size is not pixel size
    QSize imageSize = image.size();
    QPoint clickPos((float) m_clickPos.x() / (float) m_screenSize.width() * imageSize.width(),
                    (float) m_clickPos.y() / (float) m_screenSize.height() * imageSize.height());

    //read the pixel under the mouse
    QColor color = image.pixelColor(clickPos.x(), clickPos.y());

    //set the selected face using the red color
    m_model->setSelected(color.red());

    //update the data for drawing
    m_model->updateData();

    //write data to the GPU
    m_vbo.bind();
    m_vbo.write(0, m_model->constData(), m_model->count() * sizeof(GLfloat));
    m_vbo.release();

    //indicates that we're not picking
    m_program->setUniformValue(m_isPickingLoc, false);

    //reset color
    glClearColor(0.3f, 0.3f, 0.3f, 1.0f);

    //enable multisample
    glEnable(GL_MULTISAMPLE);
}