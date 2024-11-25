#include "gui/batchvertex.h"
#include "halfedge/mesh.h"
#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

void BatchVertex::init() {
    this->initializeOpenGLFunctions();

    m_vao.create();
    m_vbo.create();
    m_vao.bind();
    m_vbo.bind();

    //enable enough attrib array for all the data of the edge's vertex
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //color
    glEnableVertexAttribArray(2); //ID for picking
    //coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, static_cast<int>(m_floatsPerVertex * sizeof(GLfloat)), nullptr);
    //color of the vertex
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, static_cast<int>(m_floatsPerVertex * sizeof(GLfloat)), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //the ID
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, static_cast<int>(m_floatsPerVertex * sizeof(GLfloat)), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    m_vbo.release();
    m_vao.release();

    m_program.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/vertices/vs.glsl");
    m_program.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/vertices/fs.glsl");
    m_program.link();

    //get location of uniforms
    m_program.bind();
    m_projMatrixLoc = m_program.uniformLocation("projMatrix");
    m_viewMatrixLoc = m_program.uniformLocation("mvMatrix");

    m_programPicking.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/vertices/picking/vs.glsl");
    m_programPicking.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/vertices/picking/fs.glsl");
    m_programPicking.link();

    //get location of uniforms
    m_programPicking.bind();
    m_projMatrixPickingLoc = m_programPicking.uniformLocation("projMatrix");
    m_viewMatrixPickingLoc = m_programPicking.uniformLocation("mvMatrix");

    this->updateData();
}

void BatchVertex::update() {
    m_vbo.bind();
    m_vbo.allocate(m_data.constData(), m_count * static_cast<int>(sizeof(GLfloat)));
    m_vbo.release();
}

void BatchVertex::updateData() {
    m_count = 0;
    m_data.clear();

    //the number of vertices of the mesh plus the projection point on sphere
    qsizetype nbOfVertices = (m_mesh != nullptr ? static_cast<qsizetype>(m_mesh->vertices().size()) : 0) + 1;

    //for each vertex, there is 1 add
    qsizetype nbOfAdd = 1 * nbOfVertices;

    //we resize the data for rapidity
    m_data.resize(nbOfAdd * m_floatsPerVertex);

    //the projection point
    this->addVertex({ 0.0f, 0.0f, 1.0f }, { 1.0f, 0.0f, 0.0f }, 0.0f);

    int ID = 1;

    if (m_mesh != nullptr) {
        //for each vertex
        for (he::Vertex* v: m_mesh->vertices()) {
            //will display a point
            bool isSelected = (ID == m_selectedVertex && m_selectedVertex != 0) || (ID == m_selectedVertex2 && m_selectedVertex2 != 0);
            QVector3D color = isSelected ? QVector3D(0.0f, 0.8f, 0.0f) : QVector3D(0.0f, 0.0f, 0.0f);
            this->addVertex(v->pos(), color, static_cast<float>(ID));
            ID++;
        }
    }

    this->update();
}

void BatchVertex::render(PickingType type) {
    if (!m_displayMesh && !m_displayProjectionPoint) { return; }
    switch (type) {
        case PickingType::PickingVertex:
            if (!m_displayMesh) { return; }
            m_programPicking.bind();
            m_vao.bind();
            glDrawArrays(GL_POINTS, 1, m_count / m_floatsPerVertex - 1);
            m_programPicking.release();
            break;
        case PickingType::PickingNone:
            m_program.bind();
            m_vao.bind();
            if (m_displayMesh && !m_displayProjectionPoint) {
                glDrawArrays(GL_POINTS, 1, m_count / m_floatsPerVertex - 1);
            }
            if (!m_displayMesh && m_displayProjectionPoint) {
                glDrawArrays(GL_POINTS, 0, 1);
            }
            if (m_displayMesh && m_displayProjectionPoint) {
                glDrawArrays(GL_POINTS, 0, m_count / m_floatsPerVertex);
            }
            m_program.release();
            break;
        case PickingType::PickingFace:
        case PickingType::PickingEdge:
        case PickingType::PickingCircle:
            break;
    }
}

void BatchVertex::setProjection(QMatrix4x4 matrix) {
    m_program.bind();
    m_program.setUniformValue(m_projMatrixLoc, matrix);
    m_program.release();

    m_programPicking.bind();
    m_programPicking.setUniformValue(m_projMatrixPickingLoc, matrix);
    m_programPicking.release();
}

void BatchVertex::setCamera(Camera camera) {
    camera.zoom(0.001f);
    camera.zoom(0.001f);

    m_program.bind();
    m_program.setUniformValue(m_viewMatrixLoc, camera.getViewMatrix());
    m_program.release();

    m_programPicking.bind();
    m_programPicking.setUniformValue(m_viewMatrixPickingLoc, camera.getViewMatrix());
    m_programPicking.release();
}

void BatchVertex::setMesh(he::Mesh* mesh) {
    m_mesh = mesh;
    m_displayMesh = true;
    m_selectedVertex = 0;
    m_selectedVertex2 = 0;
    this->updateData();
}

void BatchVertex::setProjectionPoint(bool displayed) {
    m_displayProjectionPoint = displayed;
}

void BatchVertex::setDisplayMesh(bool displayed) {
    m_displayMesh = displayed;
}

void BatchVertex::setSelectedVertex(int vertexIndex) {
    m_selectedVertex = vertexIndex;
}

void BatchVertex::setSelectedVertex2(int vertexIndex) {
    m_selectedVertex2 = vertexIndex;
}

he::Vertex* BatchVertex::selectedVertex() {
    he::Vertex* res = nullptr;

    if (m_selectedVertex - 1 >= 0 && m_selectedVertex - 1 < static_cast<qsizetype>(m_mesh->vertices().size())) {
        res = m_mesh->vertices().at(m_selectedVertex - 1);
    }

    return res;
}

he::Vertex* BatchVertex::selectedVertex2() {
    he::Vertex* res = nullptr;

    if (m_selectedVertex2 - 1 >= 0 && m_selectedVertex2 - 1 < static_cast<qsizetype>(m_mesh->vertices().size())) {
        res = m_mesh->vertices().at(m_selectedVertex2 - 1);
    }

    return res;
}

void BatchVertex::addVertex(const QVector3D& v, const QVector3D& color, float ID) {
    //add to the end of the data already added
    float* p = m_data.data() + m_count;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p++ = v.z();
    *p++ = color.x();
    *p++ = color.y();
    *p++ = color.z();
    //the ID of the vertex
    *p = ID;
    //we update the amount of data
    m_count += m_floatsPerVertex;
}

int BatchVertex::renderOrder() {
    return 1;
}

int BatchVertex::pickingOrder() {
    return 1;
}
