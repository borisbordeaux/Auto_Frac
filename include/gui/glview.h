#ifndef GLVIEW_H
#define GLVIEW_H

#include <QMatrix4x4>
#include <QOpenGLFunctions>
#include <QtOpenGL/QOpenGLBuffer>
#include <QtOpenGL/QOpenGLVertexArrayObject>
#include <QtOpenGLWidgets/QOpenGLWidget>
#include <QTimer>
#include "gui/camera.h"

enum class PickingType {
    PickingFace,
    PickingEdge,
    PickingVertex
};

enum class RotationType {
    CameraRotation,
    PolyhedronRotation
};

class QOpenGLShaderProgram;

class Model;

class Polytopal2DWindow;

class GLView : public QOpenGLWidget, protected QOpenGLFunctions {
Q_OBJECT

public:
    /**
     * @brief Construct an OpenGL widget that will draw a Model
     * @param model the model that has to be drawn
     * @param parent the parent of this widget
     */
    explicit GLView(Model* model, Polytopal2DWindow* parent = nullptr);
    ~GLView() override;

    /**
     * @brief indicates that the mesh changed, so we have
     * to reallocate memory and resend data to the GPU
     */
    void initBuffers();

    void updateData();
    void updateDataFaces();
    void updateDataSphere();
    void updateDataEdge();
    void updateDataCircles();
    void updateDataVertices();

    void stopAnimation();

    void setPickingType(PickingType type);
    void setRotationType(RotationType type);
    void startVideoAnimation();
    void rotationAnimation();

public slots:
    void animationStep();
    void animationCameraStep();

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

    void hideEvent(QHideEvent* event) override;

private:
    void initShaders();
    void initShadersView();
    void initShadersPicking();

    //manage face picking
    void clickFaceManagement();
    void clickEdgeManagement();
    void clickVertexManagement();

    //camera of the scene
    Camera m_camera;

    //the last position of the mouse
    //used for rotation
    QPointF m_lastPos;
    RotationType m_rotationType;

    //OpenGL stuff for rendering
    QVector3D m_clearColor = { 0.7f, 0.7f, 0.7f };
    QOpenGLVertexArrayObject m_vaoFaces;
    QOpenGLVertexArrayObject m_vaoSphere;
    QOpenGLVertexArrayObject m_vaoEdges;
    QOpenGLVertexArrayObject m_vaoCircles;
    QOpenGLVertexArrayObject m_vaoVertices;
    QOpenGLBuffer m_vboFaces;
    QOpenGLBuffer m_vboSphere;
    QOpenGLBuffer m_vboEdges;
    QOpenGLBuffer m_vboCircles;
    QOpenGLBuffer m_vboVertices;
    QOpenGLShaderProgram* m_programFaces = nullptr;
    QOpenGLShaderProgram* m_programFacesPicking = nullptr;
    QOpenGLShaderProgram* m_programLines = nullptr;
    QOpenGLShaderProgram* m_programLinesPicking = nullptr;
    QOpenGLShaderProgram* m_programVertices = nullptr;
    QOpenGLShaderProgram* m_programVerticesPicking = nullptr;

    //location of the different variables in the GPU
    //Faces viewing
    int m_projMatrixLoc = 0;
    int m_mvMatrixLoc = 0;
    int m_lightPosLoc = 0;
    int m_cameraPosLoc = 0;
    //Faces picking
    int m_projMatrixPickingLoc = 0;
    int m_mvMatrixPickingLoc = 0;

    //Lines viewing
    int m_projMatrixLocEdge = 0;
    int m_mvMatrixLocEdge = 0;
    //Lines picking
    int m_projMatrixPickingLocEdge = 0;
    int m_mvMatrixPickingLocEdge = 0;
    int m_invViewportPickingLocEdge = 0;

    //Vertices viewing
    int m_projMatrixLocVertices = 0;
    int m_mvMatrixLocVertices = 0;
    //Vertices picking
    int m_projMatrixPickingLocVertices = 0;
    int m_mvMatrixPickingLocVertices = 0;

    //flag to update uniforms if needed
    bool m_uniformsDirty = true;

    //matrices for rendering
    QMatrix4x4 m_proj;
    QMatrix4x4 m_world;

    //the model that will be displayed
    Model* m_model;

    //useful for item picking
    bool m_clicked = false;
    QPoint m_clickPos;
    PickingType m_pickingType = PickingType::PickingFace;
    float m_viewportWidth = 0.0f;
    float m_viewportHeight = 0.0f;

    //for animation
    QTimer m_timerAnimation;
    QTimer m_timerAnimCamera;
    Camera m_cameraBeforeAnim;
    float m_tAnimCamera = 0.0f;

private:
    Polytopal2DWindow* m_mainWindow;
    //for video animation
    QTimer m_timerDisplaySphere;
    QTimer m_timerCanonic;
    QTimer m_timerDisplayCircle;
    QTimer m_timerDisplayCircleDual;
    QTimer m_timerResetCamera;
    QTimer m_timerProjection;
    QTimer m_timerHideMeshes;
    QTimer m_timerInversion;
    QTimer m_timerHideCircleDual;
    QTimer m_timerZoom;

    void connectTimers();
};

#endif // GLVIEW_H
