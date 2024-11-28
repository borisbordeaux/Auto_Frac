#include "gui/glview.h"
#include "gui/polytopal2dwindow.h"
#include <QMouseEvent>
#include <QMimeData>
#include <QStyle>
#include "halfedge/vertex.h"
#include "halfedge/halfedge.h"
#include "halfedge/face.h"
#include "gui/batchgraphicsitem.h"

GLView::GLView(Polytopal2DWindow* parent) :
        QOpenGLWidget(parent),
        m_camera(QVector3D(0.0f, 0.0f, 0.0f), QVector3D(0.0f, 1.0f, 0.0f), 8.0f, 0.006f, 250.0f, qDegreesToRadians(90.0f), qDegreesToRadians(0.0f)),
        m_cameraBeforeAnim(m_camera),
        m_label(this),
        m_mainWindow(parent) {
    connect(&m_timerAnimCamera, &QTimer::timeout, this, &GLView::animationCameraStep);
    this->setAcceptDrops(true);
    m_label.setText("Hello world");
    m_label.setStyleSheet("QLabel { background-color : white; color : black; }");
    m_prevTime = QDateTime::currentDateTime();
    m_currentTime = QDateTime::currentDateTime();
    connect(this, &GLView::frameSwapped, this, &GLView::computeFrameRate);
}

void GLView::initializeGL() {
    //init OpenGL
    this->initializeOpenGLFunctions();

    glEnable(GL_DEPTH_TEST);
    glEnable(GL_PROGRAM_POINT_SIZE);

    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    glEnable(GL_CULL_FACE);

    //print information
    QString val = QString::fromLatin1((char*) glGetString(GL_VERSION));
    qDebug() << "OpenGL version : " << val;
    val = QString::fromLatin1((char*) glGetString(GL_SHADING_LANGUAGE_VERSION));
    qDebug() << "GLSL version : " << val;

    //background
    glClearColor(m_clearColor.x(), m_clearColor.y(), m_clearColor.z(), 1.0f);

    for (BatchGraphicsItem* item: m_items) {
        item->init();
        item->update();
    }

    //update the view
    this->update();
}

void GLView::paintGL() {
    if (m_flagCullFaceChanged) {
        if (m_cullFace) {
            glEnable(GL_CULL_FACE);
        } else {
            glDisable(GL_CULL_FACE);
        }
        m_flagCullFaceChanged = false;
    }

    if (m_uniformsDirty || m_itemsAddedInList) {
        for (BatchGraphicsItem* item: m_items) {
            item->setProjection(m_proj);
            item->setCamera(m_camera);
            item->setLight(m_camera.getEye());
            item->setInvViewport(1.0f / m_viewportWidth, 1.0f / m_viewportHeight);
            item->setColor(m_meshColor);
        }

        m_uniformsDirty = false;
        m_itemsAddedInList = false;
    }

    if (m_clearColorDirty) {
        glClearColor(m_clearColor.x(), m_clearColor.y(), m_clearColor.z(), 1.0f);
        m_clearColorDirty = false;
    }

    if (m_clicked) {
        this->pickingManagement(m_pickingType);
        m_clicked = false;
    }

    //clear buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    for (BatchGraphicsItem* item: m_items) {
        item->render(PickingType::PickingNone);
    }

    //this->computeFrameRate();
}

void GLView::resizeGL(int w, int h) {
    m_viewportWidth = static_cast<float>(w);
    m_viewportHeight = static_cast<float>(h);
    //reset the projection with the new window size
    m_proj.setToIdentity();
    m_proj.perspective(45.0f, m_viewportWidth / m_viewportHeight, 0.005f, 250.0f);
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
    m_prevTime = QDateTime::currentDateTime();
}

void GLView::mouseMoveEvent(QMouseEvent* event) {
    //compute rotations
    qreal dx = event->position().x() - m_lastPos.x();
    qreal dy = event->position().y() - m_lastPos.y();

    if (m_isKeyXPressed) {
        if (m_mainWindow->selectedVertex() != nullptr) {
            this->handleMoveXVertex(static_cast<float>(dx));
            m_lastPos = event->pos();
            return;
        }
        if (m_mainWindow->selectedEdge() != nullptr) {
            this->handleMoveXEdge(static_cast<float>(dx));
            m_lastPos = event->pos();
            return;
        }
        if (m_mainWindow->selectedFace() != nullptr) {
            this->handleMoveXFace(static_cast<float>(dx));
            m_lastPos = event->pos();
            return;
        }
    }
    if (m_isKeyYPressed) {
        if (m_mainWindow->selectedVertex() != nullptr) {
            this->handleMoveYVertex(static_cast<float>(-dy));
            m_lastPos = event->pos();
            return;
        }
        if (m_mainWindow->selectedEdge() != nullptr) {
            this->handleMoveYEdge(static_cast<float>(-dy));
            m_lastPos = event->pos();
            return;
        }
        if (m_mainWindow->selectedFace() != nullptr) {
            this->handleMoveYFace(static_cast<float>(-dy));
            m_lastPos = event->pos();
            return;
        }
    }
    if (m_isKeyZPressed) {
        if (m_mainWindow->selectedVertex() != nullptr) {
            this->handleMoveZVertex(static_cast<float>(dx - dy) / 2.0f);
            m_lastPos = event->pos();
            return;
        }
        if (m_mainWindow->selectedEdge() != nullptr) {
            this->handleMoveZEdge(static_cast<float>(dx - dy) / 2.0f);
            m_lastPos = event->pos();
            return;
        }
        if (m_mainWindow->selectedFace() != nullptr) {
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
            m_mainWindow->mesh()->transformMesh(m_world);
            m_mainWindow->updateData();
        }
        update();
    }

    if (event->buttons() & Qt::RightButton) {
        if (!m_isKeyRPressed) {
            m_camera.moveHorizontal(static_cast<float>(-dx) / 10.0f);
            m_camera.moveVertical(static_cast<float>(dy) / 10.0f);
            m_uniformsDirty = true;
        } else {
            m_world.setToIdentity();
            m_world.rotate(static_cast<float>(-dx) / 4.0f, 0, 0, 1);
            m_world.rotate(static_cast<float>(dy) / 4.0f, 0, 1, 0);
            m_mainWindow->mesh()->transformMesh(m_world);
            m_mainWindow->updateData();
        }
        this->update();
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
    this->update();
}

void GLView::mouseReleaseEvent(QMouseEvent* event) {
    if (event->button() & Qt::MouseButton::LeftButton) {
        QVector2D v(event->pos() - m_clickPos);

        //if there was a click
        if (v.length() < 5.0f) {
            //then will do the picking
            m_clicked = true;
            this->update();
        }
    }
}

void GLView::pickingManagement(PickingType type) {
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    std::sort(m_items.begin(), m_items.end(), [](BatchGraphicsItem* item1, BatchGraphicsItem* item2) -> bool {
        return item1->pickingOrder() > item2->pickingOrder();
    });

    for (BatchGraphicsItem* item: m_items) {
        item->render(type);
    }

    std::sort(m_items.begin(), m_items.end(), [](BatchGraphicsItem* item1, BatchGraphicsItem* item2) -> bool {
        return item1->renderOrder() > item2->renderOrder();
    });

    //get the rendered image of the scene
    QImage image = grabFramebuffer();

    //read the pixel under the mouse
    QColor color = image.pixelColor(m_clickPos);
    const int index = color.red() * 65536 + color.green() * 256 + color.blue();

    image.setPixelColor(m_clickPos, Qt::white);
    image.save("picking.png");

    //set the selected item using the color and update the
    //data for drawing the selected object in the right color
    switch (type) {
        case PickingType::PickingFace:
            m_mainWindow->setSelectedFace(index);
            m_mainWindow->updateDataFaces();
            break;
        case PickingType::PickingEdge:
            m_mainWindow->setSelectedEdge(index);
            m_mainWindow->updateDataEdges();
            break;
        case PickingType::PickingVertex:
            if (m_mainWindow->selectedVertex() != nullptr && m_isShiftPressed) {
                m_mainWindow->setSelectedVertex2(index);
            } else {
                m_mainWindow->setSelectedVertex2(0);
                m_mainWindow->setSelectedVertex(index);
            }
            m_mainWindow->updateDataVertices();
            break;
        case PickingType::PickingCircle:
            m_mainWindow->setSelectedCircle(index);
            m_mainWindow->updateDataCircles();
            break;
        default:
            break;
    }

    glClearColor(m_clearColor.x(), m_clearColor.y(), m_clearColor.z(), 1.0f);
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

void GLView::setPickingType(PickingType type) {
    if (type == m_pickingType) { return; }
    m_pickingType = type;
    m_mainWindow->setSelectedFace(0);
    m_mainWindow->setSelectedEdge(0);
    m_mainWindow->setSelectedVertex(0);
    m_mainWindow->setSelectedVertex2(0);
    m_mainWindow->setSelectedCircle(0);
    m_mainWindow->updateDataMesh();
    m_mainWindow->updateDataCircles();
    this->update();
}

void GLView::setBackGroundColor(float r, float g, float b) {
    m_clearColor = QVector3D(r, g, b);
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
        if (m_mainWindow->selectedEdge() != nullptr) {
            this->cutSelectedHalfEdge();
        }
        if (m_mainWindow->selectedVertex2() != nullptr) {
            this->cutFaceOnSelectedVertices();
        }
    }
    if (event->key() == Qt::Key_Delete) {
        if (m_mainWindow->selectedFace() != nullptr) {
            this->removeSelectedFace();
        }
        if (m_mainWindow->selectedEdge() != nullptr) {
            this->removeSelectedHalfEdge();
        }
        if (m_mainWindow->selectedVertex() != nullptr && m_mainWindow->selectedVertex2() == nullptr) {
            this->removeSelectedVertex();
        }
    }
}

void GLView::handleMoveXVertex(float dx) {
    QVector3D newPos = m_mainWindow->selectedVertex()->pos();
    newPos.setX(newPos.x() + dx / 100.0f);
    m_mainWindow->selectedVertex()->setPos(newPos, true);
    m_mainWindow->updateData();
    update();
}

void GLView::handleMoveYVertex(float dy) {
    QVector3D newPos = m_mainWindow->selectedVertex()->pos();
    newPos.setY(newPos.y() + dy / 100.0f);
    m_mainWindow->selectedVertex()->setPos(newPos, true);
    m_mainWindow->updateData();
    update();
}

void GLView::handleMoveZVertex(float dz) {
    QVector3D newPos = m_mainWindow->selectedVertex()->pos();
    newPos.setZ(newPos.z() + dz / 100.0f);
    m_mainWindow->selectedVertex()->setPos(newPos, true);
    m_mainWindow->updateData();
    update();
}

void GLView::handleMoveXEdge(float dx) {
    he::Vertex* v1 = m_mainWindow->selectedEdge()->origin();
    he::Vertex* v2 = m_mainWindow->selectedEdge()->next()->origin();
    QVector3D newPos1 = v1->pos();
    QVector3D newPos2 = v2->pos();
    newPos1.setX(newPos1.x() + dx / 100.0f);
    newPos2.setX(newPos2.x() + dx / 100.0f);
    v1->setPos(newPos1, true);
    v2->setPos(newPos2, true);
    m_mainWindow->updateData();
    update();
}

void GLView::handleMoveYEdge(float dy) {
    he::Vertex* v1 = m_mainWindow->selectedEdge()->origin();
    he::Vertex* v2 = m_mainWindow->selectedEdge()->next()->origin();
    QVector3D newPos1 = v1->pos();
    QVector3D newPos2 = v2->pos();
    newPos1.setY(newPos1.y() + dy / 100.0f);
    newPos2.setY(newPos2.y() + dy / 100.0f);
    v1->setPos(newPos1, true);
    v2->setPos(newPos2, true);
    m_mainWindow->updateData();
    update();
}

void GLView::handleMoveZEdge(float dz) {
    he::Vertex* v1 = m_mainWindow->selectedEdge()->origin();
    he::Vertex* v2 = m_mainWindow->selectedEdge()->next()->origin();
    QVector3D newPos1 = v1->pos();
    QVector3D newPos2 = v2->pos();
    newPos1.setZ(newPos1.z() + dz / 100.0f);
    newPos2.setZ(newPos2.z() + dz / 100.0f);
    v1->setPos(newPos1, true);
    v2->setPos(newPos2, true);
    m_mainWindow->updateData();
    update();
}

void GLView::handleMoveXFace(float dx) {
    for (he::Vertex* v: m_mainWindow->selectedFace()->allVertices()) {
        QVector3D newPos = v->pos();
        newPos.setX(newPos.x() + dx / 100.0f);
        v->setPos(newPos, true);
    }
    m_mainWindow->updateData();
    update();
}

void GLView::handleMoveYFace(float dy) {
    for (he::Vertex* v: m_mainWindow->selectedFace()->allVertices()) {
        QVector3D newPos = v->pos();
        newPos.setY(newPos.y() + dy / 100.0f);
        v->setPos(newPos, true);
    }
    m_mainWindow->updateData();
    update();
}

void GLView::handleMoveZFace(float dz) {
    for (he::Vertex* v: m_mainWindow->selectedFace()->allVertices()) {
        QVector3D newPos = v->pos();
        newPos.setZ(newPos.z() + dz / 100.0f);
        v->setPos(newPos, true);
    }
    m_mainWindow->updateData();
    update();
}

void GLView::cutFaceOnSelectedVertices() {
    he::Vertex* v1 = m_mainWindow->selectedVertex();
    he::Vertex* v2 = m_mainWindow->selectedVertex2();
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
    m_mainWindow->mesh()->cutFace(face, v1, v2);
    m_mainWindow->mesh()->updateHalfEdgeNotTwin();
    m_mainWindow->mesh()->updateOtherHalfEdges();
    m_mainWindow->updateData();
    this->update();
}

void GLView::cutSelectedHalfEdge() {
    he::HalfEdge* he = m_mainWindow->selectedEdge();
    if (he == nullptr) { return; }

    m_mainWindow->mesh()->cutHalfEdge(he);
    m_mainWindow->mesh()->updateHalfEdgeNotTwin();
    m_mainWindow->mesh()->updateOtherHalfEdges();
    m_mainWindow->setSelectedEdge(0);
    m_mainWindow->updateData();
    this->update();
}

void GLView::removeSelectedFace() {
    m_mainWindow->mesh()->remove(m_mainWindow->selectedFace());
    m_mainWindow->setSelectedFace(0);
    m_mainWindow->updateData();
    this->update();
}

void GLView::removeSelectedHalfEdge() {
    m_mainWindow->mesh()->remove(m_mainWindow->selectedEdge());
    m_mainWindow->setSelectedEdge(0);
    m_mainWindow->updateData();
    this->update();
}

void GLView::removeSelectedVertex() {
    m_mainWindow->mesh()->remove(m_mainWindow->selectedVertex());
    m_mainWindow->setSelectedVertex(0);
    m_mainWindow->setSelectedVertex2(0);
    m_mainWindow->updateData();
    this->update();
}

void GLView::addItem(BatchGraphicsItem* item) {
    if (this->containsItem(item)) { return; }
    m_items.push_back(item);
    std::sort(m_items.begin(), m_items.end(), [](BatchGraphicsItem* item1, BatchGraphicsItem* item2) -> bool {
        return item1->renderOrder() > item2->renderOrder();
    });
    m_itemsAddedInList = true;
}

void GLView::removeItem(BatchGraphicsItem* item) {
    auto it = std::find(m_items.begin(), m_items.end(), item);
    if (it != m_items.end()) {
        m_items.erase(it);
    }
}

bool GLView::containsItem(BatchGraphicsItem* item) {
    if (m_items.empty()) { return false; }
    return std::find(m_items.begin(), m_items.end(), item) != m_items.end();
}

void GLView::changeMeshColor(QColor const& color) {
    m_meshColor = color;
    m_uniformsDirty = true;
    this->update();
}

QColor const& GLView::meshColor() const {
    return m_meshColor;
}

void GLView::initOldMeshColor() {
    m_oldMeshColor = m_meshColor;
}

void GLView::restoreMeshColor() {
    this->changeMeshColor(m_oldMeshColor);
}

void GLView::enableCullFace(bool enable) {
    m_cullFace = enable;
    m_flagCullFaceChanged = true;
}

void GLView::computeFrameRate() {
    m_currentTime = QDateTime::currentDateTime();
    m_timeDiffMs = static_cast<float>(m_prevTime.msecsTo(m_currentTime));
    m_counter += 1.0f;
    if (m_timeDiffMs >= 50.0) { //every 50ms
        QString fps = QString::number(static_cast<int>(1000.0f / m_timeDiffMs * m_counter));
        QString ms = QString::number(m_timeDiffMs / m_counter);

        m_label.setText(fps + " fps / " + ms + " ms");
        m_label.adjustSize();
        m_prevTime = m_currentTime;
        m_counter = 0.0f;
    }
}
