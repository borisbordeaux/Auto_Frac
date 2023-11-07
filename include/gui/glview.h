#ifndef GLVIEW_H
#define GLVIEW_H

#include <QMatrix4x4>
#include <QOpenGLFunctions>
#include <QtOpenGL/QOpenGLBuffer>
#include <QtOpenGL/QOpenGLVertexArrayObject>
#include <QtOpenGLWidgets/QOpenGLWidget>
#include <QTimer>
#include "gui/camera.h"

class QOpenGLShaderProgram;

class Model;

class GLView : public QOpenGLWidget, protected QOpenGLFunctions {
Q_OBJECT

public:
    /**
     * @brief Construct an OpenGL widget that will draw a Model
     * @param model the model that has to be drawn
     * @param parent the parent of this widget
     */
    explicit GLView(Model* model, QWidget* parent = nullptr);
    ~GLView() override;

    /**
     * @brief indicates that the mesh changed, so we have
     * to reallocate memory and resend data to the GPU
     */
    void meshChanged();

    void stopAnimation();

public slots:
    void animationStep();

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
    void keyPressEvent(QKeyEvent* event) override;

    void hideEvent(QHideEvent* event) override;

private:
    //manage face selection
    void clickFaceManagement();

    //camera of the scene
    Camera m_camera;
    QTimer m_timerAnimation;

    //the last position of the mouse
    //used for rotation
    QPointF m_lastPos;

    //OpenGL stuff for rendering
    QOpenGLVertexArrayObject m_vao;
    QOpenGLVertexArrayObject m_vaoEdge;
    QOpenGLVertexArrayObject m_vaoVertices;
    QOpenGLBuffer m_vbo;
    QOpenGLBuffer m_vboEdge;
    QOpenGLBuffer m_vboVertices;
    QOpenGLShaderProgram* m_program = nullptr;
    QOpenGLShaderProgram* m_programEdge = nullptr;
    QOpenGLShaderProgram* m_programVertices = nullptr;

    //location of the different variables in the GPU
    int m_projMatrixLoc = 0;
    int m_mvMatrixLoc = 0;
    int m_normalMatrixLoc = 0;
    int m_lightPosLoc = 0;
    int m_cameraPosLoc = 0;
    int m_modelMatrixLoc = 0;
    int m_isPickingLoc = 0;

    //for edges
    int m_projMatrixLocEdge = 0;
    int m_mvMatrixLocEdge = 0;
    int m_isPickingLocEdge = 0;

    //for vertices
    int m_projMatrixLocVertices = 0;
    int m_mvMatrixLocVertices = 0;
    int m_isPickingLocVertices = 0;

    //to prevent sending uniform already sent
    bool m_uniformsDirty = true;

    //matrices for rendering
    QMatrix4x4 m_proj;
    QMatrix4x4 m_world;

    //the model that will be displayed
    Model* m_model;

    //useful for item selection
    bool m_clicked = false;
    QPoint m_clickPos;
};

#endif // GLVIEW_H
