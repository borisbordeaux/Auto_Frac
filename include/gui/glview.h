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
    PickingVertex,
    PickingCircle
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
    void updateDataEdges();
    void updateDataCircles();
    void updateDataCirclesDual();
    void updateDataVertices();
    void updateDataDebugLine();

    void setPickingType(PickingType type);

    void setBackGroundColor(float r, float g, float b);
    PickingType pickingType() const;

public slots:
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

    void dragEnterEvent(QDragEnterEvent* event) override;
    void dropEvent(QDropEvent* event) override;

    void keyPressEvent(QKeyEvent* event) override;
    void keyReleaseEvent(QKeyEvent* event) override;

private:
    void initShaders();
    void initShadersView();
    void initShadersPicking();

    //manage face picking
    void clickFaceManagement();
    void clickEdgeManagement();
    void clickVertexManagement();
    void clickCircleManagement();

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

    void collapseSelectedHalfEdge();

private:
    //camera of the scene
    Camera m_camera;

    //the last position of the mouse
    QPointF m_lastPos;

    //OpenGL stuff for rendering
    QVector3D m_clearColor = { 0.3f, 0.3f, 0.3f };
    QOpenGLVertexArrayObject m_vaoFaces;
    QOpenGLVertexArrayObject m_vaoSphere;
    QOpenGLVertexArrayObject m_vaoEdges;
    QOpenGLVertexArrayObject m_vaoCircles;
    QOpenGLVertexArrayObject m_vaoCirclesDual;
    QOpenGLVertexArrayObject m_vaoVertices;
    QOpenGLVertexArrayObject m_vaoDebugLine;
    QOpenGLBuffer m_vboFaces;
    QOpenGLBuffer m_vboSphere;
    QOpenGLBuffer m_vboEdges;
    QOpenGLBuffer m_vboCircles;
    QOpenGLBuffer m_vboCirclesDual;
    QOpenGLBuffer m_vboVertices;
    QOpenGLBuffer m_vboDebugLine;
    QOpenGLShaderProgram* m_programSphere = nullptr;
    QOpenGLShaderProgram* m_programFaces = nullptr;
    QOpenGLShaderProgram* m_programFacesPicking = nullptr;
    QOpenGLShaderProgram* m_programEdges = nullptr;
    QOpenGLShaderProgram* m_programEdgesPicking = nullptr;
    QOpenGLShaderProgram* m_programVertices = nullptr;
    QOpenGLShaderProgram* m_programVerticesPicking = nullptr;
    QOpenGLShaderProgram* m_programCircles = nullptr;
    QOpenGLShaderProgram* m_programCirclesPicking = nullptr;
    QOpenGLShaderProgram* m_programCirclesDual = nullptr;
    QOpenGLShaderProgram* m_programDebugLine = nullptr;

    //location of the different variables in the GPU
    //Sphere viewing
    int m_projMatrixLocSphere = 0;
    int m_mvMatrixLocSphere = 0;
    int m_lightPosLocSphere = 0;
    int m_cameraPosLocSphere = 0;

    //Faces viewing
    int m_projMatrixLoc = 0;
    int m_mvMatrixLoc = 0;
    int m_lightPosLoc = 0;
    int m_cameraPosLoc = 0;
    //Faces picking
    int m_projMatrixPickingLoc = 0;
    int m_mvMatrixPickingLoc = 0;

    //Edges viewing
    int m_projMatrixLocEdge = 0;
    int m_mvMatrixLocEdge = 0;
    //Edges picking
    int m_projMatrixPickingLocEdge = 0;
    int m_mvMatrixPickingLocEdge = 0;
    int m_invViewportPickingLocEdge = 0;

    //Vertices viewing
    int m_projMatrixLocVertices = 0;
    int m_mvMatrixLocVertices = 0;
    //Vertices picking
    int m_projMatrixPickingLocVertices = 0;
    int m_mvMatrixPickingLocVertices = 0;

    //Circles viewing
    int m_projMatrixLocCircle = 0;
    int m_mvMatrixLocCircle = 0;
    //Circles picking
    int m_projMatrixPickingLocCircle = 0;
    int m_mvMatrixPickingLocCircle = 0;
    int m_invViewportPickingLocCircle = 0;

    //Circles dual viewing
    int m_projMatrixLocCircleDual = 0;
    int m_mvMatrixLocCircleDual = 0;

    //debug line viewing
    int m_projMatrixLocDebugLine = 0;
    int m_mvMatrixLocDebugLine = 0;

    //flag to update uniforms if needed
    bool m_uniformsDirty = true;

    //flag to update clear color
    bool m_clearColorDirty = false;

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
    QTimer m_timerAnimCamera;
    Camera m_cameraBeforeAnim;
    float m_tAnimCamera = 0.0f;

    bool m_isKeyXPressed = false;
    bool m_isKeyYPressed = false;
    bool m_isKeyZPressed = false;
    bool m_isKeyRPressed = false;
    bool m_isShiftPressed = false;

private:
    Polytopal2DWindow* m_mainWindow;
};

#endif // GLVIEW_H
