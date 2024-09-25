#ifndef AUTOFRAC_SKYBOX_H
#define AUTOFRAC_SKYBOX_H

#include <QOpenGLFunctions>
#include <QOpenGLVertexArrayObject>
#include <QOpenGLBuffer>

enum class SkyBoxType {
    None,
    SkyBox1,
    SkyBox2
};

enum class Location {
    Projection,
    View
};

class QOpenGLShaderProgram;

class SkyBox : protected QOpenGLFunctions {
public:
    void init();
    void setSkyBox(SkyBoxType type);

    void setUniform(Location loc, QMatrix4x4 const& matrix);
    void render();

private:
    SkyBoxType m_skyBoxType = SkyBoxType::None;

    QOpenGLShaderProgram* m_programSkyBox = nullptr;
    QOpenGLBuffer m_vboSkyBox;
    QOpenGLVertexArrayObject m_vaoSkyBox;
    unsigned int m_textureID = 0;

    int m_projMatrixLocSkyBox = 0;
    int m_viewMatrixLocSkyBox = 0;
};


#endif //AUTOFRAC_SKYBOX_H
