#ifndef AUTOFRAC_BATCHDEBUGLINE_H
#define AUTOFRAC_BATCHDEBUGLINE_H

#include <QOpenGLShaderProgram>
#include <QOpenGLBuffer>
#include <QOpenGLVertexArrayObject>
#include "batchgraphicsitem.h"

class BatchDebugLine : public BatchGraphicsItem {
public:
    void init() override;
    void update() override;
    void render(PickingType type) override;

    void setProjection(QMatrix4x4 projection) override;
    void setCamera(Camera camera) override;

    void addDebugLine(QVector3D const& v1, QVector3D const& v2);
    void clearDebugLine();

    int renderOrder() override;
    int pickingOrder() override;

    bool containsData() const { return m_count != 0; }

private:
    QVector<float> m_data;
    int m_count = 0;
    int m_floatsPerVertex = 3;

    QOpenGLVertexArrayObject m_vao;
    QOpenGLBuffer m_vbo;
    QOpenGLShaderProgram m_program;
    int m_projMatrixLoc = 0;
    int m_viewMatrixLoc = 0;
};


#endif //AUTOFRAC_BATCHDEBUGLINE_H
