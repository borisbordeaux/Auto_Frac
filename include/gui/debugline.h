#ifndef AUTOFRAC_DEBUGLINE_H
#define AUTOFRAC_DEBUGLINE_H

#include <QOpenGLShaderProgram>
#include <QOpenGLBuffer>
#include <QOpenGLVertexArrayObject>
#include "batchgraphicsitem.h"

class DebugLine : public BatchGraphicsItem {
public:
    void init() override;
    void update() override;
    void render(PickingType type) override;

    void setProjection(QMatrix4x4 projection) override;
    void setCamera(Camera camera) override;

    void addDebugLine(QVector3D const& v1, QVector3D const& v2);
    void clearDebugLine();

private:
    QVector<float> m_data;
    int m_count = 0;
    int m_floatsPerVertex = 3;

    QOpenGLVertexArrayObject m_vao;
    QOpenGLBuffer m_vbo;
    QOpenGLShaderProgram* m_program = nullptr;
    int m_projMatrixLoc = 0;
    int m_viewMatrixLoc = 0;
};


#endif //AUTOFRAC_DEBUGLINE_H
