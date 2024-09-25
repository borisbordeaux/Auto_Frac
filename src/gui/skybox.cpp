#include <QImage>
#include <QtOpenGL/QOpenGLShaderProgram>
#include <iostream>
#include "gui/skybox.h"

void SkyBox::init() {
    this->initializeOpenGLFunctions();
    m_vaoSkyBox.create();
    m_vboSkyBox.create();

    //init shader for sky box
    m_programSkyBox = new QOpenGLShaderProgram();
    m_programSkyBox->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/skybox/vs.glsl");
    m_programSkyBox->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/skybox/fs.glsl");
    m_programSkyBox->bindAttributeLocation("aPos", 0);
    m_programSkyBox->link();

    //get location of uniforms
    m_programSkyBox->bind();
    m_projMatrixLocSkyBox = m_programSkyBox->uniformLocation("projection");
    m_viewMatrixLocSkyBox = m_programSkyBox->uniformLocation("view");

    float skyboxVertices[] = {
            // positions
            -1.0f, 1.0f, -1.0f,
            -1.0f, -1.0f, -1.0f,
            1.0f, -1.0f, -1.0f,
            1.0f, -1.0f, -1.0f,
            1.0f, 1.0f, -1.0f,
            -1.0f, 1.0f, -1.0f,

            -1.0f, -1.0f, 1.0f,
            -1.0f, -1.0f, -1.0f,
            -1.0f, 1.0f, -1.0f,
            -1.0f, 1.0f, -1.0f,
            -1.0f, 1.0f, 1.0f,
            -1.0f, -1.0f, 1.0f,

            1.0f, -1.0f, -1.0f,
            1.0f, -1.0f, 1.0f,
            1.0f, 1.0f, 1.0f,
            1.0f, 1.0f, 1.0f,
            1.0f, 1.0f, -1.0f,
            1.0f, -1.0f, -1.0f,

            -1.0f, -1.0f, 1.0f,
            -1.0f, 1.0f, 1.0f,
            1.0f, 1.0f, 1.0f,
            1.0f, 1.0f, 1.0f,
            1.0f, -1.0f, 1.0f,
            -1.0f, -1.0f, 1.0f,

            -1.0f, 1.0f, -1.0f,
            1.0f, 1.0f, -1.0f,
            1.0f, 1.0f, 1.0f,
            1.0f, 1.0f, 1.0f,
            -1.0f, 1.0f, 1.0f,
            -1.0f, 1.0f, -1.0f,

            -1.0f, -1.0f, -1.0f,
            -1.0f, -1.0f, 1.0f,
            1.0f, -1.0f, -1.0f,
            1.0f, -1.0f, -1.0f,
            -1.0f, -1.0f, 1.0f,
            1.0f, -1.0f, 1.0f
    };

    m_vaoSkyBox.bind();
    m_vboSkyBox.bind();
    //allocate necessary memory
    m_vboSkyBox.allocate(&skyboxVertices, sizeof(skyboxVertices));

    //enable enough attrib array for all the data of the sky box vertices
    glEnableVertexAttribArray(0); //coordinates
    //3 coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), nullptr);
    m_vboSkyBox.release();
    m_vaoSkyBox.release();
}

void SkyBox::setSkyBox(SkyBoxType type) {
    m_skyBoxType = type;

    glDeleteTextures(1, &m_textureID);
    if (type == SkyBoxType::None) { return; }

    glGenTextures(1, &m_textureID);
    glBindTexture(GL_TEXTURE_CUBE_MAP, m_textureID);

    std::vector<std::string> faces = { "right.jpg", "left.jpg", "top.jpg", "bottom.jpg", "front.jpg", "back.jpg" };
    for (unsigned int i = 0; i < faces.size(); i++) {
        std::string path = "../textures/skybox";
        path += (type == SkyBoxType::SkyBox1 ? "1/" : "2/") + faces[i];
        QImage img(path.c_str());
        img.convertTo(QImage::Format_RGBA8888);
        const unsigned char* bufferImage = img.constBits();

        if (bufferImage) {
            glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X + i, 0, GL_RGBA8, img.width(), img.height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, bufferImage);
        } else {
            std::cout << "Cubemap texture failed to load at path: " << path << std::endl;
        }
    }
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE);
}

void SkyBox::setUniform(Location loc, QMatrix4x4 const& matrix) {
    m_programSkyBox->bind();
    switch (loc) {
        case Location::Projection:
            m_programSkyBox->setUniformValue(m_projMatrixLocSkyBox, matrix);
            break;
        case Location::View:
            m_programSkyBox->setUniformValue(m_viewMatrixLocSkyBox, matrix);
            break;
    }
    m_programSkyBox->release();
}

void SkyBox::render() {
    if (m_skyBoxType != SkyBoxType::None) {
        glDepthMask(GL_FALSE);
        m_programSkyBox->bind();
        m_vaoSkyBox.bind();
        glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_CUBE_MAP, m_textureID);
        glDrawArrays(GL_TRIANGLES, 0, 36);
        m_programSkyBox->release();
        glDepthMask(GL_TRUE);
    }
}
