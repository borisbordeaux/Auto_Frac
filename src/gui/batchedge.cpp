#include "gui/batchedge.h"
#include "halfedge/mesh.h"
#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

void BatchEdge::init() {
    this->initializeOpenGLFunctions();

    m_vao.create();
    m_vbo.create();
    m_vao.bind();
    m_vbo.bind();

    //enable enough attrib array for all the data of the edge's vertex
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //color
    glEnableVertexAttribArray(2); //ID for picking
    glEnableVertexAttribArray(3); //is selected
    //coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), nullptr);
    //color of the edge
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //the ID
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    //whether it's selected or not, to simplify the code, a negative value means not selected while a positive value means selected
    glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(7 * sizeof(GLfloat)));
    m_vbo.release();
    m_vao.release();

    m_program = new QOpenGLShaderProgram();
    m_program->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/edges/vs.glsl");
    m_program->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/edges/fs.glsl");
    m_program->bindAttributeLocation("vertex", 0);
    m_program->bindAttributeLocation("color", 1);
    m_program->bindAttributeLocation("ID", 2);
    m_program->bindAttributeLocation("isSelected", 3);
    m_program->link();

    //get location of uniforms
    m_program->bind();
    m_projMatrixLoc = m_program->uniformLocation("projMatrix");
    m_viewMatrixLoc = m_program->uniformLocation("mvMatrix");
    //picking
    m_programPicking = new QOpenGLShaderProgram();
    m_programPicking->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/edges/picking/vs.glsl");
    m_programPicking->addShaderFromSourceFile(QOpenGLShader::Geometry, "../shaders/edges/picking/gs.glsl");
    m_programPicking->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/edges/picking/fs.glsl");
    m_programPicking->bindAttributeLocation("vertex", 0);
    m_programPicking->bindAttributeLocation("color", 1);
    m_programPicking->bindAttributeLocation("ID", 2);
    m_programPicking->bindAttributeLocation("isSelected", 3);
    m_programPicking->link();

    //get location of uniforms
    m_programPicking->bind();
    m_projMatrixPickingLoc = m_programPicking->uniformLocation("projMatrix");
    m_viewMatrixPickingLoc = m_programPicking->uniformLocation("mvMatrix");
    m_invViewportPickingLoc = m_programPicking->uniformLocation("invViewport");
}

void BatchEdge::update() {
    m_vbo.bind();
    m_vbo.allocate(m_data.constData(), m_count * static_cast<int>(sizeof(GLfloat)));
    m_vbo.release();
}

void BatchEdge::updateData() {
    m_count = 0;
    m_data.clear();

    if (m_mesh == nullptr) { return; }

    //the number of edges
    qsizetype nbOfEdges = static_cast<qsizetype>(m_mesh->halfEdgesNoTwin().size());

    //for each edge, there are 2 vertices
    qsizetype nbOfAdd = 2 * nbOfEdges;

    //we resize the data for rapidity
    m_data.resize(nbOfAdd * 8);

    int ID = 1;

    //for each halfedge
    for (he::HalfEdge* he: m_mesh->halfEdgesNoTwin()) {
        float isSelected = (ID == m_selectedEdge && m_selectedEdge != 0) ? 1.0f : -1.0f;
        //we will display a line
        this->addVertexEdge(he->origin()->pos(), { 0, 0, 0 }, static_cast<float>(ID), isSelected);
        this->addVertexEdge(he->next()->origin()->pos(), { 0, 0, 0 }, static_cast<float>(ID), isSelected);
        ID++;
    }

    this->update();
}

void BatchEdge::render(PickingType type) {
    switch (type) {
        case PickingType::PickingEdge:
            m_programPicking->bind();
            m_vao.bind();
            glDrawArrays(GL_LINES, 0, m_count / m_floatsPerVertex);
            m_programPicking->release();
            break;
        case PickingType::PickingNone:
            m_program->bind();
            m_vao.bind();
            glDrawArrays(GL_LINES, 0, m_count / m_floatsPerVertex);
            m_program->release();
            break;
        case PickingType::PickingFace:
        case PickingType::PickingVertex:
        case PickingType::PickingCircle:
            break;
    }
}

void BatchEdge::setProjection(QMatrix4x4 matrix) {
    m_program->bind();
    m_program->setUniformValue(m_projMatrixLoc, matrix);
    m_program->release();

    m_programPicking->bind();
    m_programPicking->setUniformValue(m_projMatrixPickingLoc, matrix);
    m_programPicking->release();
}

void BatchEdge::setCamera(Camera camera) {
    camera.zoom(0.001f);
    m_program->bind();
    m_program->setUniformValue(m_viewMatrixLoc, camera.getViewMatrix());
    m_program->release();

    m_programPicking->bind();
    m_programPicking->setUniformValue(m_viewMatrixPickingLoc, camera.getViewMatrix());
    m_programPicking->release();
}

void BatchEdge::setInvViewport(float x, float y) {
    m_programPicking->bind();
    m_programPicking->setUniformValue(m_invViewportPickingLoc, x, y);
    m_programPicking->release();
}

void BatchEdge::setMesh(he::Mesh* mesh) {
    m_mesh = mesh;
    this->updateData();
}

void BatchEdge::setSelectedEdge(int edgeIndex) {
    m_selectedEdge = edgeIndex;
}

he::HalfEdge* BatchEdge::selectedEdge() {
    he::HalfEdge* res = nullptr;

    if (m_selectedEdge - 1 >= 0 && m_selectedEdge - 1 < static_cast<qsizetype>(m_mesh->halfEdgesNoTwin().size())) {
        res = m_mesh->halfEdgesNoTwin().at(m_selectedEdge - 1);
    }

    return res;
}

void BatchEdge::addVertexEdge(const QVector3D& v, const QVector3D& color, float ID, float isSelected) {
    //add to the end of the data already added
    float* p = m_data.data() + m_count;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p++ = v.z();
    *p++ = color.x();
    *p++ = color.y();
    *p++ = color.z();
    //the ID of the edge
    *p++ = ID;
    //whether the edge is selected or not
    *p = isSelected;
    //we update the amount of data
    m_count += 8;
}
