#ifndef AUTOFRAC_BATCHCIRCLEDUAL_H
#define AUTOFRAC_BATCHCIRCLEDUAL_H

#include <QOpenGLShaderProgram>
#include <QOpenGLBuffer>
#include <QOpenGLVertexArrayObject>
#include "gui/batchgraphicsitem.h"
#include "gui/circle.h"

class BatchCircleDual : public BatchGraphicsItem {
public:
    void init() override;
    void update() override;
    void updateData() override;
    void render(PickingType type) override;
    void setProjection(QMatrix4x4 matrix) override;
    void setCamera(Camera camera) override;
    void setInvViewport(float x, float y) override;

    void addCircle(gui::Circle const& circle);
    void resetCircles();

    int renderOrder() override;
    int pickingOrder() override;

    void setSelectedCircle(int circleIndex);
    gui::Circle* selectedCircle();
    void removeSelectedCircle();
    int selectedCircleIndex() const;

private:
    void addVertexCircle(QVector3D const& v, QVector3D const& color, float dist, float ID);

private:
    QVector<float> m_data;
    QVector<unsigned int> m_indices;
    int m_count = 0;
    int m_countIndices = 0;
    int m_floatsPerVertex = 7;

    int m_selectedCircle = 0;

    QOpenGLVertexArrayObject m_vao;
    QOpenGLBuffer m_vbo;
    QOpenGLBuffer m_ibo { QOpenGLBuffer::IndexBuffer };
    QOpenGLShaderProgram m_program;
    QOpenGLShaderProgram m_programPicking;

    int m_projMatrixLoc = 0;
    int m_viewMatrixLoc = 0;
    int m_invViewportLoc = 0;

    int m_projMatrixLocPicking = 0;
    int m_viewMatrixLocPicking = 0;
    int m_invViewportLocPicking = 0;

    QVector<gui::Circle> m_circles;

    QMatrix4x4 m_view;
    QMatrix4x4 m_proj;
    float m_w = 0.0f;
    float m_h = 0.0f;
};


#endif //AUTOFRAC_BATCHCIRCLEDUAL_H
