#ifndef AUTOFRAC_SKYBOX_H
#define AUTOFRAC_SKYBOX_H

#include "gui/batchgraphicsitem.h"
#include <QOpenGLVertexArrayObject>
#include <QOpenGLBuffer>
#include <QOpenGLShaderProgram>

enum class SkyBoxType {
    SkyBox1,
    SkyBox2
};

class SkyBox : public BatchGraphicsItem {
public:
    void init() override;
    void render() override;

    void setProjection(QMatrix4x4 projection) override;
    void setCamera(Camera camera) override;

    void setSkyBox(SkyBoxType type);

private:
    unsigned int m_textureID = 0;

    int m_projMatrixLocSkyBox = 0;
    int m_viewMatrixLocSkyBox = 0;

    QOpenGLVertexArrayObject m_vao;
    QOpenGLBuffer m_vbo;
    QOpenGLShaderProgram m_program;
};


#endif //AUTOFRAC_SKYBOX_H
