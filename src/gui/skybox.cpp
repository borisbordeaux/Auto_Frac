#include <QImage>
#include <QtOpenGL/QOpenGLShaderProgram>
#include <iostream>
#include "gui/skybox.h"

void SkyBox::init() {
    this->initializeOpenGLFunctions();
    m_vao.create();
    m_vbo.create();

    //init shader for sky box
    m_program.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/skybox/vs.glsl");
    m_program.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/skybox/fs.glsl");
    m_program.bindAttributeLocation("aPos", 0);
    m_program.link();

    //get location of uniforms
    m_program.bind();
    m_projMatrixLocSkyBox = m_program.uniformLocation("projection");
    m_viewMatrixLocSkyBox = m_program.uniformLocation("view");

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

    m_vao.bind();
    m_vbo.bind();
    //allocate necessary memory
    m_vbo.allocate(&skyboxVertices, sizeof(skyboxVertices));

    //enable enough attrib array for all the data of the sky box vertices
    glEnableVertexAttribArray(0); //coordinates
    //3 coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), nullptr);
    m_vbo.release();
    m_vao.release();

    setSkyBox(SkyBoxType::SkyBox2);
}

void SkyBox::render() {
    glDepthMask(GL_FALSE);
    m_program.bind();
    m_vao.bind();
    glActiveTexture(GL_TEXTURE0);
    glBindTexture(GL_TEXTURE_CUBE_MAP, m_textureID);
    glDrawArrays(GL_TRIANGLES, 0, 36);
    m_program.release();
    glDepthMask(GL_TRUE);
}

void SkyBox::setProjection(QMatrix4x4 matrix) {
    m_program.bind();
    m_program.setUniformValue(m_projMatrixLocSkyBox, matrix);
    m_program.release();
}

void SkyBox::setCamera(Camera camera) {
    QMatrix4x4 view = camera.getViewMatrix();
    //remove translation part, set only rotation part of the camera
    view.setColumn(3, { 0, 0, 0, 1 });
    m_program.bind();
    m_program.setUniformValue(m_viewMatrixLocSkyBox, view);
    m_program.release();
}

void SkyBox::setSkyBox(SkyBoxType type) {
    glDeleteTextures(1, &m_textureID);
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
