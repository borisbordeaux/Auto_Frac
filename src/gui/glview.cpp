#include "gui/glview.h"
#include "gui/model.h"
#include "gui/polytopal2dwindow.h"
#include <QMouseEvent>
#include <QtOpenGL/QOpenGLShaderProgram>

GLView::GLView(Model* model, Polytopal2DWindow* parent) :
        QOpenGLWidget(parent),
        m_camera(QVector3D(0.0f, 0.0f, 0.0f), QVector3D(0.0f, 1.0f, 0.0f), 8.0f, 0.01f, 49.0f, qDegreesToRadians(90.0f), qDegreesToRadians(0.0f)),
        m_rotationType(RotationType::CameraRotation),
        m_model(model),
        m_cameraBeforeAnim(QVector3D(0.0f, 0.0f, 0.0f), QVector3D(0.0f, 1.0f, 0.0f), 8.0f, 0.01f, 49.0f, qDegreesToRadians(90.0f), qDegreesToRadians(0.0f)),
        m_mainWindow(parent) {
    connect(&m_timerAnimation, &QTimer::timeout, this, &GLView::animationStep);
    connect(&m_timerAnimCamera, &QTimer::timeout, this, &GLView::animationCameraStep);
    this->connectTimers();
}

GLView::~GLView() {
    //destroy the programs
    if (m_programFaces != nullptr) {
        makeCurrent();
        m_vboFaces.destroy();
        delete m_programFaces;
        m_programFaces = nullptr;
        doneCurrent();
    }

    if (m_programLinesPicking != nullptr) {
        makeCurrent();
        m_vboEdges.destroy();
        delete m_programLinesPicking;
        m_programLinesPicking = nullptr;
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

void GLView::initBuffers() {
    //------for the faces------//
    m_vaoFaces.bind();
    m_vboFaces.bind();
    //allocate necessary memory
    m_vboFaces.allocate(m_model->constDataFace(), m_model->countFace() * static_cast<int>(sizeof(GLfloat)));

    //enable enough attrib array for all the data of the mesh's vertices
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //normal
    glEnableVertexAttribArray(2); //ID for picking
    glEnableVertexAttribArray(3); //is selected
    //3 coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), nullptr);
    //3 coordinates of the vertex's normal
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //the ID
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    //whether it's selected or not, to simplify the code, a negative value means not selected while a positive value means selected
    glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(7 * sizeof(GLfloat)));
    m_vboFaces.release();
    m_vaoFaces.release();

    //------for the sphere------//
    m_vaoSphere.bind();
    m_vboSphere.bind();
    //allocate necessary memory
    m_vboSphere.allocate(m_model->constDataSphere(), m_model->countSphere() * static_cast<int>(sizeof(GLfloat)));

    //enable enough attrib array for all the data of the mesh's vertices
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //normal
    glEnableVertexAttribArray(2); //ID for picking
    glEnableVertexAttribArray(3); //is selected
    //3 coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), nullptr);
    //3 coordinates of the vertex's normal
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //the ID
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    //whether it's selected or not, to simplify the code, a negative value means not selected while a positive value means selected
    glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(7 * sizeof(GLfloat)));
    m_vboSphere.release();
    m_vaoSphere.release();

    //------for the edges------//
    m_vaoEdges.bind();
    m_vboEdges.bind();
    //allocate necessary memory
    m_vboEdges.allocate(m_model->constDataEdge(), m_model->countEdge() * static_cast<int>(sizeof(GLfloat)));

    //enable enough attrib array for all the data of the edge's vertex
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //color
    glEnableVertexAttribArray(2); //ID for picking
    glEnableVertexAttribArray(3); //is selected
    //coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), nullptr);
    //color of the edge
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //the ID
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    //whether it's selected or not, to simplify the code, a negative value means not selected while a positive value means selected
    glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(7 * sizeof(GLfloat)));
    m_vboEdges.release();
    m_vaoEdges.release();

    //------for the circles------//
    m_vaoCircles.bind();
    m_vboCircles.bind();
    //allocate necessary memory
    m_vboCircles.allocate(m_model->constDataCircles(), m_model->countCircles() * static_cast<int>(sizeof(GLfloat)));

    //enable enough attrib array for all the data of the edge's vertex
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //color
    glEnableVertexAttribArray(2); //ID for picking
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

    //------for the circles dual ------//
    m_vaoCirclesDual.bind();
    m_vboCirclesDual.bind();
    //allocate necessary memory
    m_vboCirclesDual.allocate(m_model->constDataCirclesDual(), m_model->countCirclesDual() * static_cast<int>(sizeof(GLfloat)));

    //enable enough attrib array for all the data of the edge's vertex
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //color
    glEnableVertexAttribArray(2); //ID for picking
    glEnableVertexAttribArray(3); //is selected
    //coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), nullptr);
    //color of the edge
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //the ID
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    //whether it's selected or not, to simplify the code, a negative value means not selected while a positive value means selected
    glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(7 * sizeof(GLfloat)));
    m_vboCirclesDual.release();
    m_vaoCirclesDual.release();

    //------for the vertices------//
    m_vaoVertices.bind();
    m_vboVertices.bind();
    //allocate necessary memory
    m_vboVertices.allocate(m_model->constDataVertices(), m_model->countVertices() * static_cast<int>(sizeof(GLfloat)));

    //enable enough attrib array for all the data of the edge's vertex
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //color
    glEnableVertexAttribArray(2); //ID for picking
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
    this->update();
}

void GLView::initShaders() {
    this->initShadersView();
    this->initShadersPicking();
}

void GLView::initShadersView() {
    //init shader for faces
    m_programFaces = new QOpenGLShaderProgram();
    m_programFaces->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/faces/vs.glsl");
    m_programFaces->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/faces/fs.glsl");
    m_programFaces->bindAttributeLocation("vertex", 0);
    m_programFaces->bindAttributeLocation("normal", 1);
    m_programFaces->bindAttributeLocation("ID", 2);
    m_programFaces->bindAttributeLocation("isSelected", 3);
    m_programFaces->link();

    //get locations of uniforms
    m_programFaces->bind();
    m_projMatrixLoc = m_programFaces->uniformLocation("projMatrix");
    m_mvMatrixLoc = m_programFaces->uniformLocation("mvMatrix");
    m_lightPosLoc = m_programFaces->uniformLocation("lightPos");
    m_cameraPosLoc = m_programFaces->uniformLocation("cameraPosition");

    //init shader for lines
    m_programLines = new QOpenGLShaderProgram();
    m_programLines->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/lines/vs.glsl");
    m_programLines->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/lines/fs.glsl");
    m_programLines->bindAttributeLocation("vertex", 0);
    m_programLines->bindAttributeLocation("color", 1);
    m_programLines->bindAttributeLocation("ID", 2);
    m_programLines->bindAttributeLocation("isSelected", 3);
    m_programLines->link();

    //get location of uniforms
    m_programLines->bind();
    m_projMatrixLocEdge = m_programLines->uniformLocation("projMatrix");
    m_mvMatrixLocEdge = m_programLines->uniformLocation("mvMatrix");

    //init shader for vertices
    m_programVertices = new QOpenGLShaderProgram();
    m_programVertices->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/vertices/vs.glsl");
    m_programVertices->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/vertices/fs.glsl");
    m_programVertices->bindAttributeLocation("vertex", 0);
    m_programVertices->bindAttributeLocation("color", 1);
    m_programVertices->bindAttributeLocation("ID", 2);
    m_programVertices->bindAttributeLocation("isSelected", 3);
    m_programVertices->link();

    //get location of uniforms
    m_programVertices->bind();
    m_projMatrixLocVertices = m_programVertices->uniformLocation("projMatrix");
    m_mvMatrixLocVertices = m_programVertices->uniformLocation("mvMatrix");
}

void GLView::initShadersPicking() {
    //init shader for faces
    m_programFacesPicking = new QOpenGLShaderProgram();
    m_programFacesPicking->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/faces/picking/vs.glsl");
    m_programFacesPicking->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/faces/picking/fs.glsl");
    m_programFacesPicking->bindAttributeLocation("vertex", 0);
    m_programFacesPicking->bindAttributeLocation("normal", 1);
    m_programFacesPicking->bindAttributeLocation("ID", 2);
    m_programFacesPicking->bindAttributeLocation("isSelected", 3);
    m_programFacesPicking->link();

    //get locations of uniforms
    m_programFacesPicking->bind();
    m_projMatrixPickingLoc = m_programFacesPicking->uniformLocation("projMatrix");
    m_mvMatrixPickingLoc = m_programFacesPicking->uniformLocation("mvMatrix");

    //init shader for lines picking
    m_programLinesPicking = new QOpenGLShaderProgram();
    m_programLinesPicking->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/lines/picking/vs.glsl");
    m_programLinesPicking->addShaderFromSourceFile(QOpenGLShader::Geometry, "../shaders/lines/picking/gs.glsl");
    m_programLinesPicking->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/lines/picking/fs.glsl");
    m_programLinesPicking->bindAttributeLocation("vertex", 0);
    m_programLinesPicking->bindAttributeLocation("color", 1);
    m_programLinesPicking->bindAttributeLocation("ID", 2);
    m_programLinesPicking->bindAttributeLocation("isSelected", 3);
    m_programLinesPicking->link();

    //get location of uniforms
    m_programLinesPicking->bind();
    m_projMatrixPickingLocEdge = m_programLinesPicking->uniformLocation("projMatrix");
    m_mvMatrixPickingLocEdge = m_programLinesPicking->uniformLocation("mvMatrix");
    m_invViewportPickingLocEdge = m_programLinesPicking->uniformLocation("invViewport");

    //init shader for vertices
    m_programVerticesPicking = new QOpenGLShaderProgram();
    m_programVerticesPicking->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/vertices/picking/vs.glsl");
    m_programVerticesPicking->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/vertices/picking/fs.glsl");
    m_programVerticesPicking->bindAttributeLocation("vertex", 0);
    m_programVerticesPicking->bindAttributeLocation("color", 1);
    m_programVerticesPicking->bindAttributeLocation("ID", 2);
    m_programVerticesPicking->bindAttributeLocation("isSelected", 3);
    m_programVerticesPicking->link();

    //get location of uniforms
    m_programVerticesPicking->bind();
    m_projMatrixPickingLocVertices = m_programVerticesPicking->uniformLocation("projMatrix");
    m_mvMatrixPickingLocVertices = m_programVerticesPicking->uniformLocation("mvMatrix");
}

void GLView::initializeGL() {
    //init OpenGL
    this->initializeOpenGLFunctions();

    //to hide faces that are behind others
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_PROGRAM_POINT_SIZE);

    //print information
    QString val = QString::fromLatin1((char*) glGetString(GL_VERSION));
    qDebug() << "OpenGL version : " << val;
    val = QString::fromLatin1((char*) glGetString(GL_SHADING_LANGUAGE_VERSION));
    qDebug() << "GLSL version : " << val;

    //for compatibility
    m_vaoFaces.create();
    m_vaoSphere.create();
    m_vaoEdges.create();
    m_vaoCircles.create();
    m_vaoCirclesDual.create();
    m_vaoVertices.create();

    m_vboFaces.create();
    m_vboSphere.create();
    m_vboEdges.create();
    m_vboCircles.create();
    m_vboCirclesDual.create();
    m_vboVertices.create();

    //background
    glClearColor(m_clearColor.x(), m_clearColor.y(), m_clearColor.z(), 1.0f);

    this->initShaders();

    //memory allocation
    this->initBuffers();
}

void GLView::paintGL() {
    if (m_uniformsDirty) {
        //set values for uniforms
        m_programFaces->bind();
        m_programFaces->setUniformValue(m_projMatrixLoc, m_proj);
        m_programFaces->setUniformValue(m_mvMatrixLoc, m_camera.getViewMatrix());
        m_programFaces->setUniformValue(m_cameraPosLoc, m_camera.getEye());
        m_programFaces->setUniformValue(m_lightPosLoc, m_camera.getEye());
        m_programFaces->release();

        m_programFacesPicking->bind();
        m_programFacesPicking->setUniformValue(m_projMatrixPickingLoc, m_proj);
        m_programFacesPicking->setUniformValue(m_mvMatrixPickingLoc, m_camera.getViewMatrix());
        m_programFacesPicking->release();

        m_camera.zoom(0.001);

        m_programLines->bind();
        m_programLines->setUniformValue(m_projMatrixLocEdge, m_proj);
        m_programLines->setUniformValue(m_mvMatrixLocEdge, m_camera.getViewMatrix());
        m_programLines->release();

        m_programLinesPicking->bind();
        m_programLinesPicking->setUniformValue(m_projMatrixPickingLocEdge, m_proj);
        m_programLinesPicking->setUniformValue(m_mvMatrixPickingLocEdge, m_camera.getViewMatrix());
        m_programLinesPicking->setUniformValue(m_invViewportPickingLocEdge, 1.0f / m_viewportWidth, 1.0f / m_viewportHeight);
        m_programLinesPicking->release();

        m_camera.zoom(0.001);

        m_programVertices->bind();
        m_programVertices->setUniformValue(m_projMatrixLocVertices, m_proj);
        m_programVertices->setUniformValue(m_mvMatrixLocVertices, m_camera.getViewMatrix());
        m_programVertices->release();

        m_programVerticesPicking->bind();
        m_programVerticesPicking->setUniformValue(m_projMatrixPickingLocVertices, m_proj);
        m_programVerticesPicking->setUniformValue(m_mvMatrixPickingLocVertices, m_camera.getViewMatrix());
        m_programVerticesPicking->release();

        m_camera.dezoom(0.001);
        m_camera.dezoom(0.001);

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
    m_programFaces->bind();
    m_vaoFaces.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCountFace());

    m_vaoSphere.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCountSphere());
    m_programFaces->release();

    //draw circles
    m_programLines->bind();
    m_vaoCircles.bind();
    glDrawArrays(GL_LINES, 0, m_model->vertexCountCircles());

    //draw circles dual
    m_vaoCirclesDual.bind();
    glDrawArrays(GL_LINES, 0, m_model->vertexCountCirclesDual());

    //draw edges
    m_vaoEdges.bind();
    glDrawArrays(GL_LINES, 0, m_model->vertexCountEdge());
    m_programLines->release();

    //draw vertices
    m_programVertices->bind();
    m_vaoVertices.bind();
    glDrawArrays(GL_POINTS, 0, m_model->vertexCountVertices());
    m_programVertices->release();
}

void GLView::resizeGL(int w, int h) {
    m_viewportWidth = static_cast<float>(w);
    m_viewportHeight = static_cast<float>(h);
    //reset the projection with the new window size
    m_proj.setToIdentity();
    m_proj.perspective(45.0f, m_viewportWidth / m_viewportHeight, 0.005f, 50.0f);
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
    qreal dy = event->position().y() - m_lastPos.y();

    if (event->buttons() & Qt::LeftButton) {
        if (m_rotationType == RotationType::CameraRotation) {
            m_camera.rotateAzimuth(static_cast<float>(dx / this->size().toSizeF().width() * 4.0));
            m_camera.rotatePolar(static_cast<float>(dy / this->size().toSizeF().height() * 2.0));
            m_uniformsDirty = true;
        } else {
            m_world.setToIdentity();
            m_world.rotate(static_cast<float>(dy) / 4.0f, 1, 0, 0);
            m_world.rotate(static_cast<float>(dx) / 4.0f, 0, 1, 0);
            m_model->transformMesh(m_world);
            m_mainWindow->updateCirclesDual();
            m_mainWindow->updateCircles();
            this->updateData();
        }
        update();
    }

    if (event->buttons() & Qt::RightButton) {
        if (m_rotationType == RotationType::CameraRotation) {
            m_camera.moveHorizontal(static_cast<float>(-dx) / 100.0f);
            m_camera.moveVertical(static_cast<float>(dy) / 100.0f);
            m_uniformsDirty = true;
        } else {
            m_world.setToIdentity();
            m_world.rotate(static_cast<float>(-dx) / 4.0f, 0, 0, 1);
            m_world.rotate(static_cast<float>(dy) / 4.0f, 0, 1, 0);
            m_model->transformMesh(m_world);
            m_mainWindow->updateCirclesDual();
            m_mainWindow->updateCircles();
            this->updateData();
        }
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
            //then will do the face picking
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

    //using the picking shader
    m_programFacesPicking->bind();

    //draw faces
    m_vaoFaces.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCountFace());
    m_vaoSphere.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCountSphere());
    m_programFaces->release();

    //get the rendered image of the scene
    QImage image = grabFramebuffer();
    image.save("picking.png");

    //read the pixel under the mouse
    QColor color = image.pixelColor(m_clickPos);

    //set the selected face using the red color
    m_model->setSelectedFace(color.red() * 65536 + color.green() * 256 + color.blue());

    //update the data for drawing the selected object in the right color
    m_model->updateDataFaces();

    //write data to the GPU
    m_vboFaces.bind();
    m_vboFaces.write(0, m_model->constDataFace(), m_model->countFace() * static_cast<int>(sizeof(GLfloat)));
    m_vboFaces.release();

    //reset color
    glClearColor(m_clearColor.x(), m_clearColor.y(), m_clearColor.z(), 1.0f);

    //re enable multisample
    glEnable(GL_MULTISAMPLE);
}

void GLView::clickEdgeManagement() {
    //black background
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);

    //no multisample
    glDisable(GL_MULTISAMPLE);

    //clear buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    //draw faces only in depth buffer
    m_programFaces->bind();
    glColorMask(false, false, false, false);
    m_vaoFaces.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCountFace());
    m_vaoSphere.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCountSphere());
    glColorMask(true, true, true, true);
    m_programFaces->release();

    //draw edges
    m_programLinesPicking->bind();
    m_vaoEdges.bind();
    glDrawArrays(GL_LINES, 0, m_model->vertexCountEdge());
    m_programLinesPicking->release();

    //render the scene
    QImage image = grabFramebuffer();

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
                image.setPixelColor(m_clickPos.x() + i, m_clickPos.y() + j, Qt::blue);
            }
        }
    }
    image.save("picking.png");

    //set the selected face using the red color
    m_model->setSelectedEdge(max);

    //update the data for drawing the selected object in the right color
    m_model->updateDataEdge();

    //write data to the GPU
    m_vboEdges.bind();
    m_vboEdges.write(0, m_model->constDataEdge(), m_model->countEdge() * static_cast<int>(sizeof(GLfloat)));
    m_vboEdges.release();

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

    //draw faces only in depth buffer
    m_programFaces->bind();
    glColorMask(false, false, false, false);
    m_vaoFaces.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCountFace());
    m_vaoSphere.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCountSphere());
    glColorMask(true, true, true, true);
    m_programFaces->release();

    //draw vertices
    m_programVerticesPicking->bind();
    m_vaoVertices.bind();
    glDrawArrays(GL_POINTS, 0, m_model->vertexCountVertices());
    m_programVerticesPicking->release();

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

void GLView::connectTimers() {
    connect(&m_timerDisplaySphere, &QTimer::timeout, this, [&]() {
        m_mainWindow->slotDisplayUnitSphereChanged();
        m_timerCanonic.start(1000);
        m_timerDisplaySphere.stop();
    });
    connect(&m_timerCanonic, &QTimer::timeout, this, [&]() {
        m_mainWindow->slotCanonizeMesh();
        m_timerDisplayCircle.start(6000);
        m_timerCanonic.stop();
    });
    connect(&m_timerDisplayCircle, &QTimer::timeout, this, [&]() {
        m_mainWindow->slotDisplayAreaCircles();
        m_timerDisplayCircleDual.start(2000);
        m_timerDisplayCircle.stop();
    });
    connect(&m_timerDisplayCircleDual, &QTimer::timeout, this, [&]() {
        m_mainWindow->slotDisplayDualAreaCircles();
        m_model->updateDataCirclesDual();
        m_timerResetCamera.start(9000);
        m_timerDisplayCircleDual.stop();
    });
    connect(&m_timerResetCamera, &QTimer::timeout, this, [&]() {
        m_timerAnimation.stop();
        m_cameraBeforeAnim = m_camera;
        m_timerAnimCamera.start();
        m_timerProjection.start(1000);
        m_timerResetCamera.stop();
    });
    connect(&m_timerProjection, &QTimer::timeout, this, [&]() {
        m_mainWindow->projectCirclesToPlan();
        m_timerHideMeshes.start(1000);
        m_timerProjection.stop();
    });
    connect(&m_timerHideMeshes, &QTimer::timeout, this, [&]() {
        m_model->setMesh(nullptr);
        m_model->setSphereMesh(nullptr);
        this->updateData();
        m_timerInversion.start(1000);
        m_timerHideMeshes.stop();
    });
    connect(&m_timerInversion, &QTimer::timeout, this, [&]() {
        m_mainWindow->slotIncreaseInversion();
        if (m_mainWindow->inversionLevel() == 10) {
            m_timerInversion.stop();
            m_timerHideCircleDual.start();
        } else {
            m_timerInversion.start(1000);
        }
    });
    connect(&m_timerHideCircleDual, &QTimer::timeout, this, [&]() {
        m_mainWindow->slotDisplayDualAreaCircles();
        m_model->updateDataCirclesDual();
        m_timerHideCircleDual.stop();
        m_timerZoom.start();
    });
    connect(&m_timerZoom, &QTimer::timeout, this, [&]() {
        this->m_camera.zoom(0.01f);
        if (m_camera.radius() < 5.0f) {
            m_timerZoom.stop();
        }
        m_uniformsDirty = true;
        update();
    });
}

void GLView::updateData() {
    this->updateDataFaces();
    this->updateDataSphere();
    this->updateDataEdge();
    this->updateDataCircles();
    this->updateDataCirclesDual();
    this->updateDataVertices();
}

void GLView::updateDataFaces() {
    m_vboFaces.bind();
    m_vboFaces.allocate(m_model->constDataFace(), m_model->countFace() * static_cast<int>(sizeof(GLfloat)));
    m_vboFaces.release();
}

void GLView::updateDataSphere() {
    m_vboSphere.bind();
    m_vboSphere.allocate(m_model->constDataSphere(), m_model->countSphere() * static_cast<int>(sizeof(GLfloat)));
    m_vboSphere.release();
}

void GLView::updateDataEdge() {
    m_vboEdges.bind();
    m_vboEdges.allocate(m_model->constDataEdge(), m_model->countEdge() * static_cast<int>(sizeof(GLfloat)));
    m_vboEdges.release();
}

void GLView::updateDataCircles() {
    m_vboCircles.bind();
    m_vboCircles.allocate(m_model->constDataCircles(), m_model->countCircles() * static_cast<int>(sizeof(GLfloat)));
    m_vboCircles.release();
}

void GLView::updateDataCirclesDual() {
    m_vboCirclesDual.bind();
    m_vboCirclesDual.allocate(m_model->constDataCirclesDual(), m_model->countCirclesDual() * static_cast<int>(sizeof(GLfloat)));
    m_vboCirclesDual.release();
}

void GLView::updateDataVertices() {
    m_vboVertices.bind();
    m_vboVertices.allocate(m_model->constDataVertices(), m_model->countVertices() * static_cast<int>(sizeof(GLfloat)));
    m_vboVertices.release();
}

void GLView::rotationAnimation() {
    if (m_timerAnimation.isActive()) {
        m_timerAnimation.stop();
    } else {
        m_timerAnimation.start(0);
    }
}

void GLView::setPickingType(PickingType type) {
    m_pickingType = type;
    m_model->setSelectedFace(0);
    m_model->setSelectedEdge(0);
    m_model->setSelectedVertex(0);
    m_model->updateDataFaces();
    m_model->updateDataEdge();
    m_model->updateDataVertices();
    this->updateDataFaces();
    this->updateDataEdge();
    this->updateDataVertices();
    this->update();
}

void GLView::setRotationType(RotationType type) {
    m_rotationType = type;
}

void GLView::startVideoAnimation() {
    m_timerDisplaySphere.start();
}

