#include "gui/batchplane.h"

#include "polytopal/inversivecoordinates.h"

void BatchPlane::init() {
    this->initializeOpenGLFunctions();

    float f = 100.0f;

    float planeVertices[] = {
            // positions
            f * -1.0f, f * -1.0f, 0.0f,
            f * +1.0f, f * -1.0f, 0.0f,
            f * -1.0f, f * +1.0f, 0.0f,
            f * -1.0f, f * +1.0f, 0.0f,
            f * +1.0f, f * -1.0f, 0.0f,
            f * +1.0f, f * +1.0f, 0.0f,
    };

    m_vao.create();
    glGenBuffers(1, &m_ssbo);
    m_vbo.create();

    m_vao.bind();

    glBindBuffer(GL_SHADER_STORAGE_BUFFER, m_ssbo);
    glBindBufferBase(GL_SHADER_STORAGE_BUFFER, 3, m_ssbo);
    glBindBuffer(GL_SHADER_STORAGE_BUFFER, 0); // unbind

    m_vbo.bind();
    //allocate necessary memory
    m_vbo.allocate(&planeVertices, sizeof(planeVertices));

    //enable enough attrib array for all the data of the mesh's vertices
    glEnableVertexAttribArray(0); //coordinates
    //3 coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), nullptr);

    m_vbo.release();
    m_vao.release();

    m_program.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/plane/vs.glsl");
    m_program.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/plane/fs.glsl");
    m_program.link();

    //get locations of uniforms
    m_program.bind();
    m_projMatrixLoc = m_program.uniformLocation("projMatrix");
    m_viewMatrixLoc = m_program.uniformLocation("mvMatrix");
    m_nbVerticesLoc = m_program.uniformLocation("nbVertices");

    this->updateMeshData({});
}

void BatchPlane::render(PickingType type) {
    if (type != PickingType::PickingNone) { return; }
    bool cullFaceEnabled = glIsEnabled(GL_CULL_FACE);
    if (cullFaceEnabled) {
        glDisable(GL_CULL_FACE);
    }
    m_program.bind();
    m_vao.bind();
    glBindBuffer(GL_SHADER_STORAGE_BUFFER, m_ssbo);
    glDrawArrays(GL_TRIANGLES, 0, 6);
    m_program.release();
    if (cullFaceEnabled) {
        glEnable(GL_CULL_FACE);
    }
}

void BatchPlane::setProjection(QMatrix4x4 projection) {
    m_program.bind();
    m_program.setUniformValue(m_projMatrixLoc, projection);
    m_program.release();
}

void BatchPlane::setCamera(Camera camera) {
    m_program.bind();
    m_program.setUniformValue(m_viewMatrixLoc, camera.getViewMatrix());
    m_program.release();
}

void BatchPlane::updateMeshData(std::vector<poly::InversiveCoordinates> const& circles) {
    if (circles.empty()) {
        m_program.bind();
        glUniform1ui(m_nbVerticesLoc, 0);
        m_program.release();
        return;
    }

    std::vector<float> data;
    data.reserve(circles.size() * 3);
    for (poly::InversiveCoordinates const& c: circles) {
        gui::Circle v = c.toCircle();
        data.push_back(v.center().x());
        data.push_back(v.center().y());
        data.push_back(static_cast<float>(c.radius()));
    }

    glBindBuffer(GL_SHADER_STORAGE_BUFFER, m_ssbo);
    glBufferData(GL_SHADER_STORAGE_BUFFER, static_cast<long>(data.size() * sizeof(float)), data.data(), GL_DYNAMIC_DRAW);
    glBindBuffer(GL_SHADER_STORAGE_BUFFER, 0); // unbind

    m_program.bind();
    glUniform1ui(m_nbVerticesLoc, static_cast<unsigned int>(data.size()));
    m_program.release();
}

int BatchPlane::renderOrder() {
    return 3;
}

int BatchPlane::pickingOrder() {
    return 4;
}
