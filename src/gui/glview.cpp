#include "gui/glview.h"
#include "gui/model.h"
#include "gui/polytopal2dwindow.h"
#include <QMouseEvent>
#include <QMimeData>
#include <QtOpenGL/QOpenGLShaderProgram>
#include <iostream>
#include "halfedge/vertex.h"
#include "halfedge/halfedge.h"
#include "halfedge/face.h"

GLView::GLView(Model* model, Polytopal2DWindow* parent) :
        QOpenGLWidget(parent),
        m_camera(QVector3D(0.0f, 0.0f, 0.0f), QVector3D(0.0f, 1.0f, 0.0f), 8.0f, 0.01f, 49.0f, qDegreesToRadians(90.0f), qDegreesToRadians(0.0f)),
        m_model(model),
        m_cameraBeforeAnim(QVector3D(0.0f, 0.0f, 0.0f), QVector3D(0.0f, 1.0f, 0.0f), 8.0f, 0.01f, 49.0f, qDegreesToRadians(90.0f), qDegreesToRadians(0.0f)),
        m_mainWindow(parent) {
    connect(&m_timerAnimCamera, &QTimer::timeout, this, &GLView::animationCameraStep);
    this->setAcceptDrops(true);
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

    if (m_programEdgesPicking != nullptr) {
        makeCurrent();
        m_vboEdges.destroy();
        delete m_programEdgesPicking;
        m_programEdgesPicking = nullptr;
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

    //enable enough attrib array for all the data of the circle's vertex
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
    //coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), nullptr);
    //color of the edge
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
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

    //------for debug lines------//
    m_vaoDebugLine.bind();
    m_vboDebugLine.bind();
    //allocate necessary memory
    m_vboDebugLine.allocate(m_model->constDataDebugLine(), m_model->countDebugLine() * static_cast<int>(sizeof(GLfloat)));

    //enable enough attrib array for all the data of the debug lines vertices
    glEnableVertexAttribArray(0); //coordinates
    //3 coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), nullptr);
    m_vboDebugLine.release();
    m_vaoDebugLine.release();
}

void GLView::initShaders() {
    this->initShadersView();
    this->initShadersPicking();
}

void GLView::initShadersView() {
    //init shader for circles
    m_programCircles = new QOpenGLShaderProgram();
    m_programCircles->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/circles/vs.glsl");
    m_programCircles->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/circles/fs.glsl");
    m_programCircles->bindAttributeLocation("vertex", 0);
    m_programCircles->bindAttributeLocation("color", 1);
    m_programCircles->bindAttributeLocation("ID", 2);
    m_programCircles->bindAttributeLocation("isSelected", 3);
    m_programCircles->link();

    //get locations of uniforms
    m_programCircles->bind();
    m_projMatrixLocCircle = m_programCircles->uniformLocation("projMatrix");
    m_mvMatrixLocCircle = m_programCircles->uniformLocation("mvMatrix");

    //init shader for circles dual
    m_programCirclesDual = new QOpenGLShaderProgram();
    m_programCirclesDual->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/circlesdual/vs.glsl");
    m_programCirclesDual->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/circlesdual/fs.glsl");
    m_programCirclesDual->bindAttributeLocation("vertex", 0);
    m_programCirclesDual->bindAttributeLocation("color", 1);
    m_programCirclesDual->link();

    //get locations of uniforms
    m_programCirclesDual->bind();
    m_projMatrixLocCircleDual = m_programCirclesDual->uniformLocation("projMatrix");
    m_mvMatrixLocCircleDual = m_programCirclesDual->uniformLocation("mvMatrix");

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
    m_programEdges = new QOpenGLShaderProgram();
    m_programEdges->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/edges/vs.glsl");
    m_programEdges->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/edges/fs.glsl");
    m_programEdges->bindAttributeLocation("vertex", 0);
    m_programEdges->bindAttributeLocation("color", 1);
    m_programEdges->bindAttributeLocation("ID", 2);
    m_programEdges->bindAttributeLocation("isSelected", 3);
    m_programEdges->link();

    //get location of uniforms
    m_programEdges->bind();
    m_projMatrixLocEdge = m_programEdges->uniformLocation("projMatrix");
    m_mvMatrixLocEdge = m_programEdges->uniformLocation("mvMatrix");

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

    //init shader for debug line
    m_programDebugLine = new QOpenGLShaderProgram();
    m_programDebugLine->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/debugline/vs.glsl");
    m_programDebugLine->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/debugline/fs.glsl");
    m_programDebugLine->bindAttributeLocation("vertex", 0);
    m_programDebugLine->link();

    //get location of uniforms
    m_programDebugLine->bind();
    m_projMatrixLocDebugLine = m_programDebugLine->uniformLocation("projMatrix");
    m_mvMatrixLocDebugLine = m_programDebugLine->uniformLocation("mvMatrix");
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
    m_programEdgesPicking = new QOpenGLShaderProgram();
    m_programEdgesPicking->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/edges/picking/vs.glsl");
    m_programEdgesPicking->addShaderFromSourceFile(QOpenGLShader::Geometry, "../shaders/edges/picking/gs.glsl");
    m_programEdgesPicking->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/edges/picking/fs.glsl");
    m_programEdgesPicking->bindAttributeLocation("vertex", 0);
    m_programEdgesPicking->bindAttributeLocation("color", 1);
    m_programEdgesPicking->bindAttributeLocation("ID", 2);
    m_programEdgesPicking->bindAttributeLocation("isSelected", 3);
    m_programEdgesPicking->link();

    //get location of uniforms
    m_programEdgesPicking->bind();
    m_projMatrixPickingLocEdge = m_programEdgesPicking->uniformLocation("projMatrix");
    m_mvMatrixPickingLocEdge = m_programEdgesPicking->uniformLocation("mvMatrix");
    m_invViewportPickingLocEdge = m_programEdgesPicking->uniformLocation("invViewport");

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

    //init shader for circles picking
    m_programCirclesPicking = new QOpenGLShaderProgram();
    m_programCirclesPicking->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/circles/picking/vs.glsl");
    m_programCirclesPicking->addShaderFromSourceFile(QOpenGLShader::Geometry, "../shaders/circles/picking/gs.glsl");
    m_programCirclesPicking->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/circles/picking/fs.glsl");
    m_programCirclesPicking->bindAttributeLocation("vertex", 0);
    m_programCirclesPicking->bindAttributeLocation("color", 1);
    m_programCirclesPicking->bindAttributeLocation("ID", 2);
    m_programCirclesPicking->bindAttributeLocation("isSelected", 3);
    m_programCirclesPicking->link();

    //get location of uniforms
    m_programCirclesPicking->bind();
    m_projMatrixPickingLocCircle = m_programCirclesPicking->uniformLocation("projMatrix");
    m_mvMatrixPickingLocCircle = m_programCirclesPicking->uniformLocation("mvMatrix");
    m_invViewportPickingLocCircle = m_programCirclesPicking->uniformLocation("invViewport");
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
    m_vaoEdges.create();
    m_vaoCircles.create();
    m_vaoCirclesDual.create();
    m_vaoVertices.create();
    m_vaoDebugLine.create();

    m_vboFaces.create();
    m_vboEdges.create();
    m_vboCircles.create();
    m_vboCirclesDual.create();
    m_vboVertices.create();
    m_vboDebugLine.create();

    //background
    glClearColor(m_clearColor.x(), m_clearColor.y(), m_clearColor.z(), 1.0f);

    this->initShaders();

    //memory allocation
    this->initBuffers();

    for (BatchGraphicsItem* item: m_items) {
        item->init();
    }

    for (BatchGraphicsItem* item: m_items) {
        item->update();
    }

    //update the view
    this->update();
}

void GLView::paintGL() {
    if (m_uniformsDirty) {
        for (BatchGraphicsItem* item: m_items) {
            item->setProjection(m_proj);
        }
        for (BatchGraphicsItem* item: m_items) {
            item->setCamera(m_camera);
        }
        for (BatchGraphicsItem* item: m_items) {
            item->setLight(m_camera.getEye());
        }

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

        //to be sure to draw in front of sphere and faces
        m_camera.zoom(0.001f);

        m_programCircles->bind();
        m_programCircles->setUniformValue(m_projMatrixLocCircle, m_proj);
        m_programCircles->setUniformValue(m_mvMatrixLocCircle, m_camera.getViewMatrix());
        m_programCircles->release();

        m_programCirclesPicking->bind();
        m_programCirclesPicking->setUniformValue(m_projMatrixPickingLocCircle, m_proj);
        m_programCirclesPicking->setUniformValue(m_mvMatrixPickingLocCircle, m_camera.getViewMatrix());
        m_programCirclesPicking->setUniformValue(m_invViewportPickingLocCircle, 1.0f / m_viewportWidth, 1.0f / m_viewportHeight);
        m_programCirclesPicking->release();

        m_programCirclesDual->bind();
        m_programCirclesDual->setUniformValue(m_projMatrixLocCircleDual, m_proj);
        m_programCirclesDual->setUniformValue(m_mvMatrixLocCircleDual, m_camera.getViewMatrix());
        m_programCirclesDual->release();

        m_programEdges->bind();
        m_programEdges->setUniformValue(m_projMatrixLocEdge, m_proj);
        m_programEdges->setUniformValue(m_mvMatrixLocEdge, m_camera.getViewMatrix());
        m_programEdges->release();

        m_programEdgesPicking->bind();
        m_programEdgesPicking->setUniformValue(m_projMatrixPickingLocEdge, m_proj);
        m_programEdgesPicking->setUniformValue(m_mvMatrixPickingLocEdge, m_camera.getViewMatrix());
        m_programEdgesPicking->setUniformValue(m_invViewportPickingLocEdge, 1.0f / m_viewportWidth, 1.0f / m_viewportHeight);
        m_programEdgesPicking->release();

        m_programDebugLine->bind();
        m_programDebugLine->setUniformValue(m_projMatrixLocDebugLine, m_proj);
        m_programDebugLine->setUniformValue(m_mvMatrixLocDebugLine, m_camera.getViewMatrix());
        m_programDebugLine->release();

        //to be sure to draw in front of edges and circles
        m_camera.zoom(0.001f);

        m_programVertices->bind();
        m_programVertices->setUniformValue(m_projMatrixLocVertices, m_proj);
        m_programVertices->setUniformValue(m_mvMatrixLocVertices, m_camera.getViewMatrix());
        m_programVertices->release();

        m_programVerticesPicking->bind();
        m_programVerticesPicking->setUniformValue(m_projMatrixPickingLocVertices, m_proj);
        m_programVerticesPicking->setUniformValue(m_mvMatrixPickingLocVertices, m_camera.getViewMatrix());
        m_programVerticesPicking->release();

        //dezoom to reset camera position
        m_camera.dezoom(0.001f);
        m_camera.dezoom(0.001f);

        m_uniformsDirty = false;
    }

    if (m_clearColorDirty) {
        glClearColor(m_clearColor.x(), m_clearColor.y(), m_clearColor.z(), 1.0f);
        m_clearColorDirty = false;
    }

    //click management
    if (m_clicked) {
        switch (m_pickingType) {
            case PickingType::PickingFace:
                clickFaceManagement();
                break;
            case PickingType::PickingEdge:
                clickEdgeManagement();
                break;
            case PickingType::PickingVertex:
                clickVertexManagement();
                break;
            case PickingType::PickingCircle:
                clickCircleManagement();
                break;
        }
        m_clicked = false;
    }

    //clear buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    for (BatchGraphicsItem* item: m_items) {
        item->render();
    }

    //draw faces
    m_programFaces->bind();
    m_vaoFaces.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCountFace());
    m_programFaces->release();

    //draw circles
    m_programCircles->bind();
    m_vaoCircles.bind();
    glDrawArrays(GL_LINES, 0, m_model->vertexCountCircles());
    m_programCircles->release();

    //draw circles dual
    m_programCirclesDual->bind();
    m_vaoCirclesDual.bind();
    glDrawArrays(GL_LINES, 0, m_model->vertexCountCirclesDual());
    m_programCirclesDual->release();

    //draw edges
    m_programEdges->bind();
    m_vaoEdges.bind();
    glDrawArrays(GL_LINES, 0, m_model->vertexCountEdge());
    m_programEdges->release();

    //draw vertices
    m_programVertices->bind();
    m_vaoVertices.bind();
    glDrawArrays(GL_POINTS, 0, m_model->vertexCountVertices());
    m_programVertices->release();

    //draw debug lines
    m_programDebugLine->bind();
    m_vaoDebugLine.bind();
    glDrawArrays(GL_LINES, 0, m_model->vertexCountDebugLine());
    m_programDebugLine->release();
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

    if (m_isKeyXPressed) {
        if (m_model->selectedVertex() != nullptr) {
            this->handleMoveXVertex(static_cast<float>(dx));
            m_lastPos = event->pos();
            return;
        }
        if (m_model->selectedEdge() != nullptr) {
            this->handleMoveXEdge(static_cast<float>(dx));
            m_lastPos = event->pos();
            return;
        }
        if (m_model->selectedFace() != nullptr) {
            this->handleMoveXFace(static_cast<float>(dx));
            m_lastPos = event->pos();
            return;
        }
    }
    if (m_isKeyYPressed) {
        if (m_model->selectedVertex() != nullptr) {
            this->handleMoveYVertex(static_cast<float>(-dy));
            m_lastPos = event->pos();
            return;
        }
        if (m_model->selectedEdge() != nullptr) {
            this->handleMoveYEdge(static_cast<float>(-dy));
            m_lastPos = event->pos();
            return;
        }
        if (m_model->selectedFace() != nullptr) {
            this->handleMoveYFace(static_cast<float>(-dy));
            m_lastPos = event->pos();
            return;
        }
    }
    if (m_isKeyZPressed) {
        if (m_model->selectedVertex() != nullptr) {
            this->handleMoveZVertex(static_cast<float>(dx - dy) / 2.0f);
            m_lastPos = event->pos();
            return;
        }
        if (m_model->selectedEdge() != nullptr) {
            this->handleMoveZEdge(static_cast<float>(dx - dy) / 2.0f);
            m_lastPos = event->pos();
            return;
        }
        if (m_model->selectedFace() != nullptr) {
            this->handleMoveZFace(static_cast<float>(dx - dy) / 2.0f);
            m_lastPos = event->pos();
            return;
        }
    }

    if (event->buttons() & Qt::LeftButton) {
        if (!m_isKeyRPressed) {
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
        if (!m_isKeyRPressed) {
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
            //then will do the picking
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

    //draw sphere only in depth buffer
    glColorMask(false, false, false, false);
    //m_sphere.render();
    glColorMask(true, true, true, true);

    //draw faces using the picking shader
    m_programFacesPicking->bind();
    m_vaoFaces.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCountFace());
    m_programFacesPicking->release();

    //get the rendered image of the scene
    QImage image = grabFramebuffer();
    image.save("picking.png");

    //read the pixel under the mouse
    QColor color = image.pixelColor(m_clickPos);

    //set the selected face using the red color
    m_model->setSelectedFace(color.red() * 65536 + color.green() * 256 + color.blue());
    m_mainWindow->updateUserData();

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

    //draw only in depth buffer
    glColorMask(false, false, false, false);
    //draw faces
    m_programFaces->bind();
    m_vaoFaces.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCountFace());
    m_programFaces->release();

    //draw sphere only in depth buffer
    //m_sphere.render();
    glColorMask(true, true, true, true);

    //draw edges
    m_programEdgesPicking->bind();
    m_vaoEdges.bind();
    glDrawArrays(GL_LINES, 0, m_model->vertexCountEdge());
    m_programEdgesPicking->release();

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
    m_mainWindow->updateUserData();

    //update the data for drawing the selected object in the right color
    m_model->updateDataEdges();

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

    //draw only in depth buffer
    glColorMask(false, false, false, false);
    //faces
    m_programFaces->bind();
    m_vaoFaces.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCountFace());
    m_programFaces->release();

    //m_sphere.render();
    glColorMask(true, true, true, true);

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

    //set the selected vertex or vertices
    if (m_model->selectedVertex() != nullptr && m_isShiftPressed) {
        m_model->setSelectedVertex2(max);
    } else {
        m_model->setSelectedVertex2(0);
        m_model->setSelectedVertex(max);
    }
    m_mainWindow->updateUserData();

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

void GLView::clickCircleManagement() {
    /*//black background
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);

    //no multisample
    glDisable(GL_MULTISAMPLE);

    //clear buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    //draw only in depth buffer
    glColorMask(false, false, false, false);
    //draw faces
    m_programFaces->bind();
    m_vaoFaces.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_model->vertexCountFace());
    m_programFaces->release();

    //draw sphere only in depth buffer
    m_sphere.render();
    glColorMask(true, true, true, true);

    //draw circles
    m_programCirclesPicking->bind();
    m_vaoCircles.bind();
    glDrawArrays(GL_LINES, 0, m_model->vertexCountCircles());
    m_programCirclesPicking->release();

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

    //set the selected circle using the color
    m_model->setSelectedCircle(max);
    m_mainWindow->updateUserData();

    //update the data for drawing the selected object in the right color
    m_model->updateDataCircles();

    //write data to the GPU
    m_vboCircles.bind();
    m_vboCircles.write(0, m_model->constDataCircles(), m_model->countCircles() * static_cast<int>(sizeof(GLfloat)));
    m_vboCircles.release();

    //reset clear color
    glClearColor(m_clearColor.x(), m_clearColor.y(), m_clearColor.z(), 1.0f);

    //enable multisample
    glEnable(GL_MULTISAMPLE);*/
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

void GLView::updateData() {
    this->updateDataFaces();
    this->updateDataEdges();
    this->updateDataCircles();
    this->updateDataCirclesDual();
    this->updateDataVertices();
    this->updateDataDebugLine();
}

void GLView::updateDataFaces() {
    m_vboFaces.bind();
    m_vboFaces.allocate(m_model->constDataFace(), m_model->countFace() * static_cast<int>(sizeof(GLfloat)));
    m_vboFaces.release();
}

void GLView::updateDataEdges() {
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

void GLView::updateDataDebugLine() {
    m_vboDebugLine.bind();
    m_vboDebugLine.allocate(m_model->constDataDebugLine(), m_model->countDebugLine() * static_cast<int>(sizeof(GLfloat)));
    m_vboDebugLine.release();
}

void GLView::setPickingType(PickingType type) {
    if (type == m_pickingType) { return; }
    m_pickingType = type;
    m_model->setSelectedFace(0);
    m_model->setSelectedEdge(0);
    m_model->setSelectedVertex(0);
    m_model->setSelectedVertex2(0);
    m_model->setSelectedCircle(0);
    m_model->updateDataFaces();
    m_model->updateDataEdges();
    m_model->updateDataVertices();
    m_model->updateDataCircles();
    this->updateDataFaces();
    this->updateDataEdges();
    this->updateDataVertices();
    this->updateDataCircles();
    this->update();
}

void GLView::setBackGroundColor(float r, float g, float b) {
    m_clearColor.setX(r);
    m_clearColor.setY(g);
    m_clearColor.setZ(b);
    m_clearColorDirty = true;
}

PickingType GLView::pickingType() const {
    return m_pickingType;
}

void GLView::dragEnterEvent(QDragEnterEvent* event) {
    const QMimeData* mimeData = event->mimeData();
    //drop only one OBJ file
    if (mimeData->hasUrls() && mimeData->urls().size() == 1 && mimeData->urls()[0].toLocalFile().split('.').last() == "obj") {
        event->accept();
    }
}

void GLView::dropEvent(QDropEvent* event) {
    m_mainWindow->openOBJFile(event->mimeData()->urls()[0].toLocalFile());
}

void GLView::keyPressEvent(QKeyEvent* event) {
    if (event->key() == Qt::Key_X) {
        m_isKeyXPressed = true;
    }
    if (event->key() == Qt::Key_Y) {
        m_isKeyYPressed = true;
    }
    if (event->key() == Qt::Key_Z) {
        m_isKeyZPressed = true;
    }
    if (event->key() == Qt::Key_R) {
        m_isKeyRPressed = true;
    }
    if (event->key() == Qt::Key_Shift) {
        m_isShiftPressed = true;
    }
}

void GLView::keyReleaseEvent(QKeyEvent* event) {
    if (event->key() == Qt::Key_X) {
        m_isKeyXPressed = false;
    }
    if (event->key() == Qt::Key_Y) {
        m_isKeyYPressed = false;
    }
    if (event->key() == Qt::Key_Z) {
        m_isKeyZPressed = false;
    }
    if (event->key() == Qt::Key_R) {
        m_isKeyRPressed = false;
    }
    if (event->key() == Qt::Key_V) {
        m_mainWindow->setInfo("Vertex selection");
        this->setPickingType(PickingType::PickingVertex);
    }
    if (event->key() == Qt::Key_E) {
        m_mainWindow->setInfo("Edge selection");
        this->setPickingType(PickingType::PickingEdge);
    }
    if (event->key() == Qt::Key_F) {
        m_mainWindow->setInfo("Face selection");
        this->setPickingType(PickingType::PickingFace);
    }
    if (event->key() == Qt::Key_C && !event->modifiers().testFlag(Qt::ShiftModifier)) {
        m_mainWindow->setInfo("Circle selection");
        this->setPickingType(PickingType::PickingCircle);
    }
    if (event->key() == Qt::Key_Shift) {
        m_isShiftPressed = false;
    }
    if (event->key() == Qt::Key_C && event->modifiers().testFlag(Qt::ShiftModifier)) {
        if (m_model->selectedEdge() != nullptr) {
            this->cutSelectedHalfEdge();
        }
        if (m_model->selectedVertex2() != nullptr) {
            this->cutFaceOnSelectedVertices();
        }
    }
    if (event->key() == Qt::Key_Delete) {
        if (m_model->selectedFace() != nullptr) {
            this->removeSelectedFace();
        }
        if (m_model->selectedEdge() != nullptr) {
            this->removeSelectedHalfEdge();
        }
        if (m_model->selectedVertex() != nullptr && m_model->selectedVertex2() == nullptr) {
            this->removeSelectedVertex();
        }
    }
}

void GLView::handleMoveXVertex(float dx) {
    QVector3D newPos = m_model->selectedVertex()->pos();
    newPos.setX(newPos.x() + dx / 100.0f);
    m_model->selectedVertex()->setPos(newPos);
    m_mainWindow->updateCircles();
    m_mainWindow->updateCirclesDual();
    m_model->updateData();
    this->updateData();
    update();
}

void GLView::handleMoveYVertex(float dy) {
    QVector3D newPos = m_model->selectedVertex()->pos();
    newPos.setY(newPos.y() + dy / 100.0f);
    m_model->selectedVertex()->setPos(newPos);
    m_mainWindow->updateCircles();
    m_mainWindow->updateCirclesDual();
    m_model->updateData();
    this->updateData();
    update();
}

void GLView::handleMoveZVertex(float dz) {
    QVector3D newPos = m_model->selectedVertex()->pos();
    newPos.setZ(newPos.z() + dz / 100.0f);
    m_model->selectedVertex()->setPos(newPos);
    m_mainWindow->updateCircles();
    m_mainWindow->updateCirclesDual();
    m_model->updateData();
    this->updateData();
    update();
}

void GLView::handleMoveXEdge(float dx) {
    he::Vertex* v1 = m_model->selectedEdge()->origin();
    he::Vertex* v2 = m_model->selectedEdge()->next()->origin();
    QVector3D newPos1 = v1->pos();
    QVector3D newPos2 = v2->pos();
    newPos1.setX(newPos1.x() + dx / 100.0f);
    newPos2.setX(newPos2.x() + dx / 100.0f);
    v1->setPos(newPos1);
    v2->setPos(newPos2);
    m_mainWindow->updateCircles();
    m_mainWindow->updateCirclesDual();
    m_model->updateData();
    this->updateData();
    update();
}

void GLView::handleMoveYEdge(float dy) {
    he::Vertex* v1 = m_model->selectedEdge()->origin();
    he::Vertex* v2 = m_model->selectedEdge()->next()->origin();
    QVector3D newPos1 = v1->pos();
    QVector3D newPos2 = v2->pos();
    newPos1.setY(newPos1.y() + dy / 100.0f);
    newPos2.setY(newPos2.y() + dy / 100.0f);
    v1->setPos(newPos1);
    v2->setPos(newPos2);
    m_mainWindow->updateCircles();
    m_mainWindow->updateCirclesDual();
    m_model->updateData();
    this->updateData();
    update();
}

void GLView::handleMoveZEdge(float dz) {
    he::Vertex* v1 = m_model->selectedEdge()->origin();
    he::Vertex* v2 = m_model->selectedEdge()->next()->origin();
    QVector3D newPos1 = v1->pos();
    QVector3D newPos2 = v2->pos();
    newPos1.setZ(newPos1.z() + dz / 100.0f);
    newPos2.setZ(newPos2.z() + dz / 100.0f);
    v1->setPos(newPos1);
    v2->setPos(newPos2);
    m_mainWindow->updateCircles();
    m_mainWindow->updateCirclesDual();
    m_model->updateData();
    this->updateData();
    update();
}

void GLView::handleMoveXFace(float dx) {
    for (he::Vertex* v: m_model->selectedFace()->allVertices()) {
        QVector3D newPos = v->pos();
        newPos.setX(newPos.x() + dx / 100.0f);
        v->setPos(newPos);
    }
    m_mainWindow->updateCircles();
    m_mainWindow->updateCirclesDual();
    m_model->updateData();
    this->updateData();
    update();
}

void GLView::handleMoveYFace(float dy) {
    for (he::Vertex* v: m_model->selectedFace()->allVertices()) {
        QVector3D newPos = v->pos();
        newPos.setY(newPos.y() + dy / 100.0f);
        v->setPos(newPos);
    }
    m_mainWindow->updateCircles();
    m_mainWindow->updateCirclesDual();
    m_model->updateData();
    this->updateData();
    update();
}

void GLView::handleMoveZFace(float dz) {
    for (he::Vertex* v: m_model->selectedFace()->allVertices()) {
        QVector3D newPos = v->pos();
        newPos.setZ(newPos.z() + dz / 100.0f);
        v->setPos(newPos);
    }
    m_mainWindow->updateCircles();
    m_mainWindow->updateCirclesDual();
    m_model->updateData();
    this->updateData();
    update();
}

void GLView::cutFaceOnSelectedVertices() {
    he::Vertex* v1 = m_model->selectedVertex();
    he::Vertex* v2 = m_model->selectedVertex2();
    if (v1 == nullptr || v2 == nullptr) { return; }

    //test if vertices are on a same face
    std::vector<he::Face*> faces1 = v1->getAllFacesAroundVertex();
    he::Face* face = nullptr;
    for (he::Face* f: faces1) {
        std::vector<he::Vertex*> vertices = f->allVertices();
        if (std::find(vertices.begin(), vertices.end(), v2) != vertices.end()) {
            face = f;
            break;
        }
    }

    if (face == nullptr) { return; }
    m_model->mesh()->cutFace(face, v1, v2);
    m_model->mesh()->updateHalfEdgeNotTwin();
    m_model->mesh()->updateOtherHalfEdges();
    m_model->updateDataFaces();
    m_model->updateDataEdges();
    m_model->updateDataVertices();
    this->updateDataFaces();
    this->updateDataEdges();
    this->updateDataVertices();
    this->update();
}

void GLView::cutSelectedHalfEdge() {
    he::HalfEdge* he = m_model->selectedEdge();
    if (he == nullptr) { return; }

    m_model->mesh()->cutHalfEdge(he);
    m_model->mesh()->updateHalfEdgeNotTwin();
    m_model->mesh()->updateOtherHalfEdges();
    m_model->setSelectedEdge(0);
    m_model->updateDataFaces();
    m_model->updateDataEdges();
    m_model->updateDataVertices();
    this->updateDataFaces();
    this->updateDataEdges();
    this->updateDataVertices();
    this->update();
}

void GLView::removeSelectedFace() {
    m_model->mesh()->remove(m_model->selectedFace());
    m_model->setSelectedFace(0);
    m_model->updateDataFaces();
    this->updateDataFaces();
    this->update();
}

void GLView::removeSelectedHalfEdge() {
    m_model->mesh()->remove(m_model->selectedEdge());
    m_model->setSelectedEdge(0);
    m_model->updateDataFaces();
    m_model->updateDataEdges();
    m_model->updateDataVertices();
    this->updateDataFaces();
    this->updateDataEdges();
    this->updateDataVertices();
    this->update();
}

void GLView::removeSelectedVertex() {
    m_model->mesh()->remove(m_model->selectedVertex());
    m_model->setSelectedVertex(0);
    m_model->setSelectedVertex2(0);
    m_model->updateDataFaces();
    m_model->updateDataEdges();
    m_model->updateDataVertices();
    this->updateDataFaces();
    this->updateDataEdges();
    this->updateDataVertices();
    this->update();
}

void GLView::clearScene() {
    m_items.clear();
}

void GLView::addItem(BatchGraphicsItem* item) {
    m_items.push_back(item);
    std::sort(m_items.begin(), m_items.end(), [](BatchGraphicsItem* item1, BatchGraphicsItem* item2) -> bool {
        return item1->layer() > item2->layer();
    });
}

void GLView::removeItem(BatchGraphicsItem* item) {
    auto it = std::find(m_items.begin(), m_items.end(), item);
    if (it != m_items.end()) {
        m_items.erase(it);
    }
}

bool GLView::containsItem(BatchGraphicsItem* item) {
    if(m_items.empty()) return false;
    return std::find(m_items.begin(), m_items.end(), item) != m_items.end();
}
