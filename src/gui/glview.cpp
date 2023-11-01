#include "gui/glview.h"

#include "gui/model.h"
#include "gui/shaders.h"
#include "halfedge/face.h"

#include <QKeyEvent>
#include <QtOpenGL/QOpenGLShaderProgram>

GLView::GLView(Model* model, QWidget* parent) :
        QOpenGLWidget(parent),
        m_camera(QVector3D(0.0f, 0.0f, 0.0f), QVector3D(0.0f, 1.0f, 0.0f), 8.0f, 0.01f, 50.0f, qDegreesToRadians(90.0f), qDegreesToRadians(0.0f)),
        m_model(model) {
    connect(&m_timerAnimation, &QTimer::timeout, this, &GLView::animationStep);
    grabKeyboard();
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

void GLView::meshChanged() {
    //------for the faces------//
    m_vao.bind();
    m_vbo.bind();
    //allocate necessary memory
    m_vbo.allocate(m_model->constData(), m_model->count() * static_cast<int>(sizeof(GLfloat)));

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
    m_vboEdge.allocate(m_model->constDataEdge(), m_model->countEdge() * static_cast<int>(sizeof(GLfloat)));

    //enable enough attrib array for all the data of the edge's vertex
    glEnableVertexAttribArray(0);
    glEnableVertexAttribArray(1);
    //coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), nullptr);
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
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
    m_programEdge->bindAttributeLocation("color", 1);
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
    if (m_uniformsDirty) {
        //set values for uniforms
        m_program->bind();
        m_program->setUniformValue(m_projMatrixLoc, m_proj);
        m_program->setUniformValue(m_mvMatrixLoc, m_camera.getViewMatrix() * m_world);
        m_program->setUniformValue(m_normalMatrixLoc, m_world.normalMatrix());
        m_program->setUniformValue(m_cameraPosLoc, m_camera.getEye());
        m_program->setUniformValue(m_modelMatrixLoc, m_world);
        m_program->setUniformValue(m_lightPosLoc, m_camera.getEye());
        m_uniformsDirty = false;
    }

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
    m_camera.zoom(0.002f);

    //set uniforms
    m_programEdge->setUniformValue(m_projMatrixLocEdge, m_proj);
    m_programEdge->setUniformValue(m_mvMatrixLocEdge, m_camera.getViewMatrix() * m_world);
    m_camera.zoom(-0.002f);

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
    m_proj.perspective(45.0f, static_cast<float>(w) / static_cast<float>(h), 0.005f, 50.0f);
    m_uniformsDirty = true;
}

void GLView::mousePressEvent(QMouseEvent* event) {
    if (event->button() & Qt::MouseButton::LeftButton || event->button() & Qt::MouseButton::RightButton) {
        //update the mouse positions
        m_lastPos = event->pos().toPointF();
        m_clickPos = event->pos();
    } else if (event->button() & Qt::MouseButton::MiddleButton) {
        m_camera.reset({ 0, 0, 0 }, 8.0f, qDegreesToRadians(90.0f), qDegreesToRadians(0.0f));
        m_uniformsDirty = true;
        update();
    }
}

void GLView::mouseMoveEvent(QMouseEvent* event) {
    //compute rotations
    qreal dx = event->position().x() - m_lastPos.x();
    qreal dy = event->position().toPoint().y() - m_lastPos.y();

    if (event->buttons() & Qt::LeftButton) {
        m_camera.rotateAzimuth(static_cast<float>(dx / this->size().toSizeF().width() * 4.0));
        m_camera.rotatePolar(static_cast<float>(dy / this->size().toSizeF().height() * 2.0));
        m_uniformsDirty = true;
        update();
    }

    if (event->buttons() & Qt::RightButton) {
        m_camera.moveHorizontal(static_cast<float>(-dx) / 100.0f);
        m_camera.moveVertical(static_cast<float>(dy) / 100.0f);
        m_uniformsDirty = true;
        update();
    }

    m_lastPos = event->pos();
}

void GLView::wheelEvent(QWheelEvent* event) {
    //compute new distance of camera from object
    float val = (float) event->angleDelta().y() / 500.0f;

    if (val > 0.0f)
        this->m_camera.zoom();
    else
        this->m_camera.dezoom();

    m_uniformsDirty = true;
    update();
}

void GLView::mouseReleaseEvent(QMouseEvent* event) {
    if (event->button() & Qt::MouseButton::LeftButton) {
        QVector2D v(event->pos() - m_clickPos);

        //if there was a click
        if (v.length() < 5.0f) {
            //then will do the face selection
            m_clicked = true;
            update();
        }
    }
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

    //read the pixel under the mouse
    QColor color = image.pixelColor(m_clickPos);

    //set the selected face using the red color
    m_model->setSelected(color.red());

    //update the data for drawing
    m_model->updateData();

    //write data to the GPU
    m_vbo.bind();
    m_vbo.write(0, m_model->constData(), m_model->count() * static_cast<int>(sizeof(GLfloat)));
    m_vbo.release();

    //indicates that we're not picking
    m_program->setUniformValue(m_isPickingLoc, false);

    //reset color
    glClearColor(0.3f, 0.3f, 0.3f, 1.0f);

    //enable multisample
    glEnable(GL_MULTISAMPLE);
}

void GLView::keyPressEvent(QKeyEvent* event) {
    if (event->key() & Qt::Key_A) {
        if (m_timerAnimation.isActive())
            m_timerAnimation.stop();
        else
            m_timerAnimation.start(0);
    }
    QWidget::keyPressEvent(event);
}

void GLView::animationStep() {
    m_camera.rotateAzimuth(qDegreesToRadians(0.5f));
    m_uniformsDirty = true;
    update();
}

void GLView::hideEvent(QHideEvent* event) {
    this->stopAnimation();
    QWidget::hideEvent(event);
}

void GLView::stopAnimation() {
    m_timerAnimation.stop();
}
