#include "gui/glview.h"

#include "gui/model.h"
#include "gui/shaders.h"
#include <QKeyEvent>
#include <QtOpenGL/QOpenGLShaderProgram>

GLView::GLView(Model* model, QWidget* parent) :
        QOpenGLWidget(parent),
        m_camera(QVector3D(0.0f, 0.0f, 0.0f), QVector3D(0.0f, 1.0f, 0.0f), 8.0f, 0.01f, 49.0f, qDegreesToRadians(90.0f), qDegreesToRadians(0.0f)),
        m_model(model),
        m_cameraBeforeAnim(QVector3D(0.0f, 0.0f, 0.0f), QVector3D(0.0f, 1.0f, 0.0f), 8.0f, 0.01f, 49.0f, qDegreesToRadians(90.0f), qDegreesToRadians(0.0f)) {
    connect(&m_timerAnimation, &QTimer::timeout, this, &GLView::animationStep);
    connect(&m_timerAnimCamera, &QTimer::timeout, this, &GLView::animationCameraStep);
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

    if (m_programVertices != nullptr) {
        makeCurrent();
        m_vboVertices.destroy();
        delete m_programVertices;
        m_programVertices = nullptr;
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
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //normal
    glEnableVertexAttribArray(2); //ID for selection
    glEnableVertexAttribArray(3); //is selected
    //3 coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), nullptr);
    //3 coordinates of the vertex's normal
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //the ID
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    //whether it's selected or not, to simplify the code, a negative value means not selected while a positive value means selected
    glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(7 * sizeof(GLfloat)));
    m_vbo.release();
    m_vao.release();

    //------for the edges------//
    m_vaoEdge.bind();
    m_vboEdge.bind();
    //allocate necessary memory
    m_vboEdge.allocate(m_model->constDataEdge(), m_model->countEdge() * static_cast<int>(sizeof(GLfloat)));

    //enable enough attrib array for all the data of the edge's vertex
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //color
    glEnableVertexAttribArray(2); //ID for selection
    glEnableVertexAttribArray(3); //is selected
    //coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), nullptr);
    //color of the edge
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //the ID
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    //whether it's selected or not, to simplify the code, a negative value means not selected while a positive value means selected
    glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(7 * sizeof(GLfloat)));
    m_vboEdge.release();
    m_vaoEdge.release();

    //------for the circles------//
    m_vaoCircles.bind();
    m_vboCircles.bind();
    //allocate necessary memory
    m_vboCircles.allocate(m_model->constDataCircles(), m_model->countCircles() * static_cast<int>(sizeof(GLfloat)));

    //enable enough attrib array for all the data of the edge's vertex
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //color
    glEnableVertexAttribArray(2); //ID for selection
    glEnableVertexAttribArray(3); //is selected
    //coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), nullptr);
    //color of the edge
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //the ID
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    //whether it's selected or not, to simplify the code, a negative value means not selected while a positive value means selected
    glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(7 * sizeof(GLfloat)));
    m_vboCircles.release();
    m_vaoCircles.release();

    //------for the vertices------//
    m_vaoVertices.bind();
    m_vboVertices.bind();
    //allocate necessary memory
    m_vboVertices.allocate(m_model->constDataVertices(), m_model->countVertices() * static_cast<int>(sizeof(GLfloat)));

    //enable enough attrib array for all the data of the edge's vertex
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //color
    glEnableVertexAttribArray(2); //ID for selection
    glEnableVertexAttribArray(3); //is selected
    //coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), nullptr);
    //color of the vertex
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //the ID
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    //whether it's selected or not, to simplify the code, a negative value means not selected while a positive value means selected
    glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(7 * sizeof(GLfloat)));
    m_vboVertices.release();
    m_vaoVertices.release();

    //update the view
    update();
}

void GLView::initializeGL() {
    //init OpenGL
    initializeOpenGLFunctions();

    //to hide faces that are behind others
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_PROGRAM_POINT_SIZE);

    //print information
    QString val = QString::fromLatin1((char*) glGetString(GL_VERSION));
    qDebug() << "OpenGL version : " << val;
    val = QString::fromLatin1((char*) glGetString(GL_SHADING_LANGUAGE_VERSION));
    qDebug() << "GLSL version : " << val;

    //for compatibility
    m_vao.create();
    m_vaoEdge.create();
    m_vaoCircles.create();
    m_vaoVertices.create();

    m_vbo.create();
    m_vboEdge.create();
    m_vboCircles.create();
    m_vboVertices.create();

    //background
    glClearColor(m_clearColor.x(), m_clearColor.y(), m_clearColor.z(), 1.0f);

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
    m_programEdge->bindAttributeLocation("ID", 2);
    m_programEdge->bindAttributeLocation("isSelected", 3);
    m_programEdge->link();

    //get location of uniforms
    m_programEdge->bind();
    m_projMatrixLocEdge = m_programEdge->uniformLocation("projMatrix");
    m_mvMatrixLocEdge = m_programEdge->uniformLocation("mvMatrix");
    m_isPickingLocEdge = m_programEdge->uniformLocation("isPicking");

    //init shader for edges
    m_programCircles = new QOpenGLShaderProgram();
    m_programCircles->addShaderFromSourceCode(QOpenGLShader::Vertex, vertexShaderSourceEdge);
    m_programCircles->addShaderFromSourceCode(QOpenGLShader::Fragment, fragmentShaderSourceEdge);
    m_programCircles->bindAttributeLocation("vertex", 0);
    m_programCircles->bindAttributeLocation("color", 1);
    m_programCircles->bindAttributeLocation("ID", 2);
    m_programCircles->bindAttributeLocation("isSelected", 3);
    m_programCircles->link();

    //get location of uniforms
    m_programCircles->bind();
    m_projMatrixLocCircles = m_programCircles->uniformLocation("projMatrix");
    m_mvMatrixLocCircles = m_programCircles->uniformLocation("mvMatrix");
    m_isPickingLocCircles = m_programCircles->uniformLocation("isPicking");

    //init shader for vertices
    m_programVertices = new QOpenGLShaderProgram();
    m_programVertices->addShaderFromSourceCode(QOpenGLShader::Vertex, vertexShaderSourceVertices);
    m_programVertices->addShaderFromSourceCode(QOpenGLShader::Fragment, fragmentShaderSourceVertices);
    m_programVertices->bindAttributeLocation("vertex", 0);
    m_programVertices->bindAttributeLocation("color", 1);
    m_programVertices->bindAttributeLocation("ID", 2);
    m_programVertices->bindAttributeLocation("isSelected", 3);
    m_programVertices->link();

    //get location of uniforms
    m_programVertices->bind();
    m_projMatrixLocVertices = m_programVertices->uniformLocation("projMatrix");
    m_mvMatrixLocVertices = m_programVertices->uniformLocation("mvMatrix");
    m_isPickingLocVertices = m_programVertices->uniformLocation("isPicking");

    //memory allocation
    meshChanged();
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
        m_program->release();

        m_programEdge->bind();
        m_programEdge->setUniformValue(m_projMatrixLocEdge, m_proj);
        m_programEdge->release();

        m_programCircles->bind();
        m_programCircles->setUniformValue(m_projMatrixLocCircles, m_proj);
        m_programCircles->release();

        m_programVertices->bind();
        m_programVertices->setUniformValue(m_projMatrixLocVertices, m_proj);
        m_programVertices->release();

        m_uniformsDirty = false;
    }

    //click management
    if (m_clicked) {
        if (m_pickingType == PickingType::PickingFace) {
            clickFaceManagement();
        }
        if (m_pickingType == PickingType::PickingEdge) {
            clickEdgeManagement();
        }
        if (m_pickingType == PickingType::PickingVertex) {
            clickVertexManagement();
        }
        m_clicked = false;
    }

    //clear buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    //draw faces
    m_program->bind();
    m_vao.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCount());
    m_program->release();

    //camera translate to set lines
    //in front of the polyhedron
    m_camera.zoom(0.002f);

    //set uniforms
    m_programEdge->bind();
    m_programEdge->setUniformValue(m_mvMatrixLocEdge, m_camera.getViewMatrix() * m_world);

    //draw edges
    m_vaoEdge.bind();
    glDrawArrays(GL_LINES, 0, m_model->vertexCountEdge());
    m_programEdge->release();

    //set uniforms
    m_programCircles->bind();
    m_programCircles->setUniformValue(m_mvMatrixLocCircles, m_camera.getViewMatrix() * m_world);

    //draw circles
    m_vaoCircles.bind();
    glDrawArrays(GL_LINES, 0, m_model->vertexCountCircles());
    m_programCircles->release();

    //camera translate to set vertices
    //in front of the polyhedron
    m_camera.zoom(0.002f);

    //set uniforms
    m_programVertices->bind();
    m_programVertices->setUniformValue(m_mvMatrixLocVertices, m_camera.getViewMatrix() * m_world);

    //draw vertices
    m_vaoVertices.bind();
    glDrawArrays(GL_POINTS, 0, m_model->vertexCountVertices());
    m_programEdge->release();

    //reset camera zoom
    m_camera.zoom(-0.004f);

    //set uniforms
    m_program->bind();
    m_program->setUniformValue(m_mvMatrixLoc, m_camera.getViewMatrix() * m_world);
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
        m_cameraBeforeAnim = m_camera;
        m_timerAnimCamera.start();
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

    if (val > 0.0f) {
        this->m_camera.zoom();
    } else {
        this->m_camera.dezoom();
    }

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
    //black background
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);

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
    m_program->release();

    //render the scene
    QImage image = grabFramebuffer();
    image.save("picking.png");

    //read the pixel under the mouse
    QColor color = image.pixelColor(m_clickPos);

    //set the selected face using the red color
    m_model->setSelected(color.red() * 65536 + color.green() * 256 + color.blue());

    //update the data for drawing the selected object in the right color
    m_model->updateDataFaces();
    //update data sphere because polyhedron and sphere use the same buffer
    m_model->updateDataSphere();

    //write data to the GPU
    m_vbo.bind();
    m_vbo.write(0, m_model->constData(), m_model->count() * static_cast<int>(sizeof(GLfloat)));
    m_vbo.release();

    //indicates that we're not picking
    m_program->bind();
    m_program->setUniformValue(m_isPickingLoc, false);

    //reset color
    glClearColor(m_clearColor.x(), m_clearColor.y(), m_clearColor.z(), 1.0f);

    //enable multisample
    glEnable(GL_MULTISAMPLE);
}

void GLView::clickEdgeManagement() {
    //black background
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);

    //no multisample
    glDisable(GL_MULTISAMPLE);
    //clear buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    //draw faces
    m_program->bind();
    m_vao.bind();
    glColorMask(false, false, false, false);
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCount());
    glColorMask(true, true, true, true);
    m_program->release();

    //camera translate to set edges
    //in front of the polyhedron
    m_camera.zoom(0.002f);

    //set uniforms
    m_programEdge->bind();
    m_programEdge->setUniformValue(m_mvMatrixLocEdge, m_camera.getViewMatrix() * m_world);
    //indicates to the shader that we're doing a selection
    m_programEdge->setUniformValue(m_isPickingLocEdge, true);

    //reset camera zoom
    m_camera.zoom(-0.002f);

    //draw edges
    m_vaoEdge.bind();
    glDrawArrays(GL_LINES, 0, m_model->vertexCountEdge());

    //indicates that we're not picking
    m_programEdge->setUniformValue(m_isPickingLocVertices, false);
    m_programEdge->release();

    //render the scene
    QImage image = grabFramebuffer();
    image.save("picking.png");

    //read the pixel under the mouse
    int max = 0;
    int area = 5;

    for (int i = -area; i < area; i++) {
        for (int j = -area; j < area; j++) {
            QColor color = image.pixelColor(m_clickPos.x() + i, m_clickPos.y() + j);
            if (color.isValid()) {
                int val = color.red() * 65536 + color.green() * 256 + color.blue();
                if (val > max) {
                    max = val;
                }
            }
        }
    }

    //set the selected face using the red color
    m_model->setSelectedEdge(max);

    //update the data for drawing the selected object in the right color
    m_model->updateDataEdge();

    //write data to the GPU
    m_vboEdge.bind();
    m_vboEdge.write(0, m_model->constDataEdge(), m_model->countEdge() * static_cast<int>(sizeof(GLfloat)));
    m_vboEdge.release();

    //reset clear color
    glClearColor(m_clearColor.x(), m_clearColor.y(), m_clearColor.z(), 1.0f);

    //enable multisample
    glEnable(GL_MULTISAMPLE);
}

void GLView::clickVertexManagement() {
    //black background
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);

    //no multisample
    glDisable(GL_MULTISAMPLE);
    //clear buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    //draw faces
    m_program->bind();
    m_vao.bind();
    glColorMask(false, false, false, false);
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCount());
    glColorMask(true, true, true, true);
    m_program->release();

    //camera translate to set vertices
    //in front of the polyhedron
    m_camera.zoom(0.002f);

    //set uniforms
    m_programVertices->bind();
    m_programVertices->setUniformValue(m_mvMatrixLocVertices, m_camera.getViewMatrix() * m_world);
    //indicates to the shader that we're doing a selection
    m_programVertices->setUniformValue(m_isPickingLocVertices, true);

    //reset camera zoom
    m_camera.zoom(-0.002f);

    //draw vertices
    m_vaoVertices.bind();
    glDrawArrays(GL_POINTS, 0, m_model->vertexCountVertices());

    //indicates that we're not picking
    m_programVertices->setUniformValue(m_isPickingLocVertices, false);
    m_programVertices->release();

    //render the scene
    QImage image = grabFramebuffer();
    image.save("picking.png");

    //read the pixel under the mouse
    int max = 0;
    int area = 5;

    for (int i = -area; i < area; i++) {
        for (int j = -area; j < area; j++) {
            QColor color = image.pixelColor(m_clickPos.x() + i, m_clickPos.y() + j);
            if (color.isValid()) {
                int val = color.red() * 65536 + color.green() * 256 + color.blue();
                if (val > max) {
                    max = val;
                }
            }
        }
    }

    //set the selected face using the red color
    m_model->setSelectedVertex(max);

    //update the data for drawing the selected object in the right color
    m_model->updateDataVertices();

    //write data to the GPU
    m_vboVertices.bind();
    m_vboVertices.write(0, m_model->constDataVertices(), m_model->countVertices() * static_cast<int>(sizeof(GLfloat)));
    m_vboVertices.release();

    //reset clear color
    glClearColor(m_clearColor.x(), m_clearColor.y(), m_clearColor.z(), 1.0f);

    //enable multisample
    glEnable(GL_MULTISAMPLE);
}

void GLView::keyPressEvent(QKeyEvent* event) {
    if (event->key() == Qt::Key_A) {
        if (m_timerAnimation.isActive()) {
            m_timerAnimation.stop();
        } else {
            m_timerAnimation.start(0);
        }
    }
    if (event->key() == Qt::Key_D) {
        m_model->toggleDisplayCircleDual();
        m_model->updateDataCircles();
        this->meshChanged();
    }
    if (event->key() == Qt::Key_F) {
        m_pickingType = PickingType::PickingFace;
        m_model->setSelected(0);
        m_model->setSelectedEdge(0);
        m_model->setSelectedVertex(0);
        m_model->updateData();
        this->meshChanged();
    }
    if (event->key() == Qt::Key_E) {
        m_pickingType = PickingType::PickingEdge;
        m_model->setSelected(0);
        m_model->setSelectedEdge(0);
        m_model->setSelectedVertex(0);
        m_model->updateData();
        this->meshChanged();
    }
    if (event->key() == Qt::Key_V) {
        m_pickingType = PickingType::PickingVertex;
        m_model->setSelected(0);
        m_model->setSelectedEdge(0);
        m_model->setSelectedVertex(0);
        m_model->updateData();
        this->meshChanged();
    }
    QWidget::keyPressEvent(event);
}

void GLView::animationStep() {
    m_camera.rotateAzimuth(qDegreesToRadians(1.0f));
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

void GLView::animationCameraStep() {
    m_camera.setCenter((1.0f - m_tAnimCamera) * m_cameraBeforeAnim.center() + m_tAnimCamera * QVector3D { 0, 0, 0 });
    m_camera.setRadius((1.0f - m_tAnimCamera) * m_cameraBeforeAnim.radius() + m_tAnimCamera * 8.0f);
    m_camera.setAzimuthAngle((1.0f - m_tAnimCamera) * m_cameraBeforeAnim.azimuthAngle() + m_tAnimCamera * qDegreesToRadians(90.0f));
    m_camera.setPolarAngle((1.0f - m_tAnimCamera) * m_cameraBeforeAnim.polarAngle() + m_tAnimCamera * qDegreesToRadians(0.0f));

    m_tAnimCamera += 0.05f;
    if (m_tAnimCamera > 1.0f) {
        m_camera.reset({ 0, 0, 0 }, 8.0f, qDegreesToRadians(90.0f), qDegreesToRadians(0.0f));
        m_timerAnimCamera.stop();
        m_tAnimCamera = 0.0f;
    }
    m_uniformsDirty = true;
    update();
}
