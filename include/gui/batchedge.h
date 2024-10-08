#ifndef AUTOFRAC_BATCHEDGE_H
#define AUTOFRAC_BATCHEDGE_H

#include <QOpenGLShaderProgram>
#include <QOpenGLBuffer>
#include <QOpenGLVertexArrayObject>
#include "batchgraphicsitem.h"

namespace he {
class Mesh;

class HalfEdge;
}

class BatchEdge : public BatchGraphicsItem {
public:
    void init() override;
    void update() override;
    void updateData() override;
    void render(PickingType type) override;
    void setProjection(QMatrix4x4 matrix) override;
    void setCamera(Camera camera) override;
    void setInvViewport(float x, float y) override;

    void setMesh(he::Mesh* mesh);

    void setSelectedEdge(int edgeIndex);
    he::HalfEdge* selectedEdge();

private:
    void addVertexEdge(QVector3D const& v, QVector3D const& color, float ID, float isSelected);

private:
    QVector<float> m_data;
    int m_count = 0;
    int m_floatsPerVertex = 8;

    QOpenGLVertexArrayObject m_vao;
    QOpenGLBuffer m_vbo;
    QOpenGLShaderProgram m_program;
    QOpenGLShaderProgram m_programPicking;
    //Edges viewing
    int m_projMatrixLoc = 0;
    int m_viewMatrixLoc = 0;
    //Edges picking
    int m_projMatrixPickingLoc = 0;
    int m_viewMatrixPickingLoc = 0;
    int m_invViewportPickingLoc = 0;

    he::Mesh* m_mesh = nullptr;
    int m_selectedEdge = 0;
};


#endif //AUTOFRAC_BATCHEDGE_H
