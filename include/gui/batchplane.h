#ifndef AUTOFRAC_BATCHPLANE_H
#define AUTOFRAC_BATCHPLANE_H


#include "gui/batchgraphicsitem.h"
#include <QOpenGLVertexArrayObject>
#include <QOpenGLBuffer>
#include <QOpenGLShaderProgram>
#include <QList>

namespace poly {
class InversiveCoordinates;
}

class BatchPlane : public BatchGraphicsItem {
public:
    void init() override;
    void render(PickingType type) override;

    void setProjection(QMatrix4x4 projection) override;
    void setCamera(Camera camera) override;

    void updateMeshData(std::vector<poly::InversiveCoordinates> const& circles);

    int renderOrder() override;
    int pickingOrder() override;

private:
    int m_projMatrixLoc = 0;
    int m_viewMatrixLoc = 0;

    int m_nbVerticesLoc = 0;

    QOpenGLVertexArrayObject m_vao;
    QOpenGLBuffer m_vbo;
    unsigned int m_ssbo = 0;
    QOpenGLShaderProgram m_program;
};


#endif //AUTOFRAC_BATCHPLANE_H
