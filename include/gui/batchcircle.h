#ifndef AUTOFRAC_BATCHCIRCLE_H
#define AUTOFRAC_BATCHCIRCLE_H

#include <QOpenGLShaderProgram>
#include <QOpenGLBuffer>
#include <QOpenGLVertexArrayObject>
#include "batchgraphicsitem.h"
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

    void updateDataCircles();
    void updateDataCirclesDual();

    void scaleCircles(float by);
    void addCircle(gui::Circle const& circle);
    void addCircleDual(gui::Circle const& circle);
    void resetCircles();
    void resetCirclesDual();
    void setSelectedCircle(int circleIndex);
    gui::Circle* selectedCircle();
    void updateColorOfCircles(QVector3D const& color);
    void updateColorOfCirclesDual(QVector3D const& color);
    QVector<gui::Circle> const& circles() const;

    int renderOrder() override;
    int pickingOrder() override;

private:
    void addVertexCircle(QVector3D const& v, QVector3D const& color, float ID, float isSelected);
    void addVertexCircleDual(QVector3D const& v, QVector3D const& color);
    qsizetype findNbOfSegmentsCircles() const;
    qsizetype findNbOfSegmentsCirclesDual() const;

private:
    QVector<float> m_data;
    QVector<float> m_dataDual;
    int m_count = 0;
    int m_countDual = 0;
    int m_floatsPerVertex = 8;
    int m_floatsPerVertexDual = 6;

    QOpenGLVertexArrayObject m_vao;
    QOpenGLBuffer m_vbo;
    QOpenGLShaderProgram m_program;
    QOpenGLShaderProgram m_programPicking;
    QOpenGLVertexArrayObject m_vaoDual;
    QOpenGLBuffer m_vboDual;
    QOpenGLShaderProgram m_programDual;

    int m_projMatrixLoc = 0;
    int m_viewMatrixLoc = 0;
    int m_projMatrixPickingLoc = 0;
    int m_viewMatrixPickingLoc = 0;
    int m_invViewportPickingLoc = 0;
    int m_projMatrixLocDual = 0;
    int m_viewMatrixLocDual = 0;

    QVector<gui::Circle> m_circles;
    QVector<gui::Circle> m_circlesDual;

    int m_selectedCircle = 0;
};


#endif //AUTOFRAC_BATCHCIRCLE_H
