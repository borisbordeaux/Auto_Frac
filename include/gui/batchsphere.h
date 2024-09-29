#ifndef AUTOFRAC_BATCHSPHERE_H
#define AUTOFRAC_BATCHSPHERE_H

#include "gui/batchgraphicsitem.h"
#include <QOpenGLVertexArrayObject>
#include <QOpenGLBuffer>
#include <QOpenGLShaderProgram>
#include <QList>

namespace he {
class Face;

class Mesh;
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

    void setSphereMesh(he::Mesh* mesh);

private:
    void addFaceSphere(he::Face* f);
    void addVertexSphere(QVector3D const& v);
    void triangleSphere(const QVector3D& pos1, const QVector3D& pos2, const QVector3D& pos3);
    static qsizetype findNbOfTriangle(he::Mesh* mesh);

private:
    int m_projMatrixLoc = 0;
    int m_viewMatrixLoc = 0;
    int m_lightPosLoc = 0;
    int m_cameraPosLoc = 0;

    he::Mesh* m_sphereMesh = nullptr;

    QList<float> m_data;
    int m_count;
    int m_floatsPerVertex = 3;

    QOpenGLVertexArrayObject m_vao;
    QOpenGLBuffer m_vbo;
    QOpenGLShaderProgram m_program;
};


#endif //AUTOFRAC_BATCHSPHERE_H
