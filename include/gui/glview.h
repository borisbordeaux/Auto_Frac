#ifndef GLVIEW_H
#define GLVIEW_H

#include <QMatrix4x4>
#include <QOpenGLFunctions>
#include <QtOpenGLWidgets/QOpenGLWidget>
#include <QTimer>
#include <QLabel>
#include <QDateTime>
#include "gui/camera.h"
#include "gui/pickingtype.h"

class Polytopal2DWindow;

class BatchGraphicsItem;

class GLView : public QOpenGLWidget, protected QOpenGLFunctions {
Q_OBJECT

public:
    /**
     * @brief Construct an OpenGL widget that will draw a Model
     * @param model the model that has to be drawn
     * @param parent the parent of this widget
     */
    explicit GLView(Polytopal2DWindow* parent = nullptr);

    void setPickingType(PickingType type);

    void setBackGroundColor(float r, float g, float b);
    PickingType pickingType() const;

    QColor const& meshColor() const;
    void initOldMeshColor();

    void enableCullFace(bool enable);

public slots:
    void animationCameraStep();
    void changeMeshColor(QColor const& color);
    void restoreMeshColor();

    void computeFrameRate();

protected:
    // QOpenGLWidget interface
    void initializeGL() override;
    void paintGL() override;
    void resizeGL(int w, int h) override;

    // QWidget interface
    void mousePressEvent(QMouseEvent* event) override;
    void mouseMoveEvent(QMouseEvent* event) override;
    void wheelEvent(QWheelEvent* event) override;
    void mouseReleaseEvent(QMouseEvent* event) override;

    void dragEnterEvent(QDragEnterEvent* event) override;
    void dropEvent(QDropEvent* event) override;

    void keyPressEvent(QKeyEvent* event) override;
    void keyReleaseEvent(QKeyEvent* event) override;

private:
    void pickingManagement(PickingType type);

    //manage mesh editing
    void handleMoveXVertex(float dx);
    void handleMoveYVertex(float dy);
    void handleMoveZVertex(float dz);

    void handleMoveXEdge(float dx);
    void handleMoveYEdge(float dy);
    void handleMoveZEdge(float dz);

    void handleMoveXFace(float dx);
    void handleMoveYFace(float dy);
    void handleMoveZFace(float dz);

    void cutFaceOnSelectedVertices();
    void cutSelectedHalfEdge();

    void removeSelectedFace();
    void removeSelectedHalfEdge();
    void removeSelectedVertex();

private:
    //camera of the scene
    Camera m_camera;

    //the last position of the mouse
    QPointF m_lastPos;

    //OpenGL stuff for rendering
    QVector3D m_clearColor = { 1.0f, 1.0f, 1.0f };

    //flag to update uniforms if needed
    bool m_uniformsDirty = true;

    //flag to update clear color
    bool m_clearColorDirty = true;
    bool m_itemsAddedInList = false;

    //matrices for rendering
    QMatrix4x4 m_proj;
    QMatrix4x4 m_world;

    //useful for item picking
    bool m_clicked = false;
    QPoint m_clickPos;
    PickingType m_pickingType = PickingType::PickingFace;
    float m_viewportWidth = 0.0f;
    float m_viewportHeight = 0.0f;

    //for animation
    QTimer m_timerAnimCamera;
    Camera m_cameraBeforeAnim;
    float m_tAnimCamera = 0.0f;

    bool m_isKeyXPressed = false;
    bool m_isKeyYPressed = false;
    bool m_isKeyZPressed = false;
    bool m_isKeyRPressed = false;
    bool m_isShiftPressed = false;

    QColor m_meshColor { 92, 163, 227, 182 };
    QColor m_oldMeshColor { m_meshColor };

    bool m_flagCullFaceChanged = false;
    bool m_cullFace = true;

    QLabel m_label;
    QDateTime m_prevTime;
    QDateTime m_currentTime;
    float timeDiffMs = 0.0f;
    float m_counter = 0.0f;

public:
    void removeItem(BatchGraphicsItem* item);
    void addItem(BatchGraphicsItem* item);
    bool containsItem(BatchGraphicsItem* item);

private:
    std::vector<BatchGraphicsItem*> m_items;

private:
    Polytopal2DWindow* m_mainWindow;
};

#endif // GLVIEW_H
