#ifndef AUTOFRAC_BATCHSPHERE_H
#define AUTOFRAC_BATCHSPHERE_H

#include "gui/batchgraphicsitem.h"
#include "halfedge/mesh.h"
#include <QOpenGLVertexArrayObject>
#include <QOpenGLBuffer>
#include <QOpenGLShaderProgram>
#include <QList>

namespace he {
class Face;
}

class BatchSphere : public BatchGraphicsItem {
public:
    void init() override;
    void update() override;
    void updateData() override;
    void render(PickingType type) override;

    void setProjection(QMatrix4x4 projection) override;
    void setCamera(Camera camera) override;
    void setLight(QVector3D lightPos) override;

    void setSphereMesh(he::Mesh&& mesh);
    void updateMeshData(he::Mesh* mesh);

    int priority() override { return 2; }

private:
    void addFaceSphere(he::Face* f);
    void addVertexSphere(QVector3D const& v);
    void triangleSphere(const QVector3D& pos1, const QVector3D& pos2, const QVector3D& pos3);
    qsizetype findNbOfTriangle();

private:
    int m_projMatrixLoc = 0;
    int m_viewMatrixLoc = 0;
    int m_lightPosLoc = 0;
    int m_cameraPosLoc = 0;

    int m_nbVerticesLoc = 0;

    he::Mesh m_sphereMesh;

    QList<float> m_data;
    int m_count = 0;
    int m_floatsPerVertex = 3;

    QOpenGLVertexArrayObject m_vao;
    QOpenGLBuffer m_vbo;
    unsigned int m_ssbo = 0;
    QOpenGLShaderProgram m_program;
};


#endif //AUTOFRAC_BATCHSPHERE_H
