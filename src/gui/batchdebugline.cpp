#include "gui/batchdebugline.h"

void BatchDebugLine::init() {
    this->initializeOpenGLFunctions();

    m_vao.create();
    m_vbo.create();
    m_vao.bind();
    m_vbo.bind();

    //enable enough attrib array for all the data of the debug lines vertices
    glEnableVertexAttribArray(0); //coordinates
    //3 coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), nullptr);
    m_vbo.release();
    m_vao.release();

    m_program = new QOpenGLShaderProgram();
    m_program->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/debugline/vs.glsl");
    m_program->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/debugline/fs.glsl");
    m_program->bindAttributeLocation("vertex", 0);
    m_program->link();
    m_program->bind();
    m_projMatrixLoc = m_program->uniformLocation("projMatrix");
    m_viewMatrixLoc = m_program->uniformLocation("mvMatrix");
}

void BatchDebugLine::update() {
    m_vbo.bind();
    m_vbo.allocate(m_data.constData(), m_count * static_cast<int>(sizeof(GLfloat)));
    m_vbo.release();
}

void BatchDebugLine::render(PickingType type) {
    if (type != PickingType::PickingNone) { return; }
    m_program->bind();
    m_vao.bind();
    glDrawArrays(GL_LINES, 0, m_count / m_floatsPerVertex);
    m_program->release();
}

void BatchDebugLine::setProjection(QMatrix4x4 projection) {
    m_program->bind();
    m_program->setUniformValue(m_projMatrixLoc, projection);
    m_program->release();
}

void BatchDebugLine::setCamera(Camera camera) {
    //to be sure to draw in front of sphere and faces
    camera.zoom(0.001f);
    m_program->bind();
    m_program->setUniformValue(m_viewMatrixLoc, camera.getViewMatrix());
    m_program->release();
}

void BatchDebugLine::addDebugLine(QVector3D const& v1, QVector3D const& v2) {
    //the coordinates of the vertex
    m_data.append(v1.x());
    m_data.append(v1.y());
    m_data.append(v1.z());
    m_data.append(v2.x());
    m_data.append(v2.y());
    m_data.append(v2.z());
    //we update the amount of data
    m_count += 6;
}

void BatchDebugLine::clearDebugLine() {
    m_count = 0;
    m_data.clear();
}
