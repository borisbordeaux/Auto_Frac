#ifndef AUTOFRAC_BATCHCIRCLE_H
#define AUTOFRAC_BATCHCIRCLE_H

#include <QOpenGLShaderProgram>
#include <QOpenGLBuffer>
#include <QOpenGLVertexArrayObject>
#include "gui/batchgraphicsitem.h"
#include "gui/circle.h"

class BatchCircle : public BatchGraphicsItem {
public:
    void init() override;
    void update() override;
    void updateData() override;
    void render(PickingType type) override;
    void setProjection(QMatrix4x4 matrix) override;
    void setCamera(Camera camera) override;
    void setInvViewport(float d, float d1) override;

    void scaleCircles(float by);
    void addCircle(gui::Circle const& circle);
    void resetCircles();
    void setSelectedCircle(int circleIndex);
    gui::Circle* selectedCircle();
    void updateColorOfCircles(QVector3D const& color);
    QVector<gui::Circle> const& circles() const;

    int renderOrder() override;
    int pickingOrder() override;

private:
    void addVertexCircle(QVector3D const& center, float radius, QVector3D const& xAxis, QVector3D const& yAxis, QVector3D const& color, float ID);

private:
    QVector<float> m_data;
    int m_count = 0;
    int m_floatsPerVertex = 14;

    QOpenGLVertexArrayObject m_vao;
    QOpenGLBuffer m_vbo;
    QOpenGLShaderProgram m_program;
    QOpenGLShaderProgram m_programPicking;

    int m_projMatrixLoc = 0;
    int m_viewMatrixLoc = 0;
    int m_cameraPosLoc = 0;
    int m_projMatrixPickingLoc = 0;
    int m_viewMatrixPickingLoc = 0;
    int m_invViewportPickingLoc = 0;

    QVector<gui::Circle> m_circles;

    int m_selectedCircle = 0;
};


#endif //AUTOFRAC_BATCHCIRCLE_H
