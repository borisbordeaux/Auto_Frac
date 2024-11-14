#ifndef AUTOFRAC_BATCHSKYBOX_H
#define AUTOFRAC_BATCHSKYBOX_H

#include "gui/batchgraphicsitem.h"
#include <QOpenGLVertexArrayObject>
#include <QOpenGLBuffer>
#include <QOpenGLShaderProgram>

enum class SkyBoxType {
    SkyBox1,
    SkyBox2
};

class BatchSkyBox : public BatchGraphicsItem {
public:
    void init() override;
    void render(PickingType type) override;

    void setProjection(QMatrix4x4 projection) override;
    void setCamera(Camera camera) override;

    void setSkyBox(SkyBoxType type);

    int renderOrder() override;
    int pickingOrder() override;

private:
    unsigned int m_textureID = 0;

    int m_projMatrixLoc = 0;
    int m_viewMatrixLoc = 0;

    QOpenGLVertexArrayObject m_vao;
    QOpenGLBuffer m_vbo;
    QOpenGLShaderProgram m_program;
};


#endif //AUTOFRAC_BATCHSKYBOX_H
