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
    //coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, static_cast<int>(m_floatsPerVertex * sizeof(GLfloat)), nullptr);
    //color of the edge
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, static_cast<int>(m_floatsPerVertex * sizeof(GLfloat)), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //the ID
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, static_cast<int>(m_floatsPerVertex * sizeof(GLfloat)), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    m_vbo.release();
    m_vao.release();

    m_program.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/edges/vs.glsl");
    m_program.addShaderFromSourceFile(QOpenGLShader::Geometry, "../shaders/edges/gs.glsl");
    m_program.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/edges/fs.glsl");
    m_program.link();

    //get location of uniforms
    m_program.bind();
    m_projMatrixLoc = m_program.uniformLocation("projMatrix");
    m_viewMatrixLoc = m_program.uniformLocation("mvMatrix");
    m_invViewportLoc = m_program.uniformLocation("invViewport");

    //picking
    m_programPicking.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/edges/picking/vs.glsl");
    m_programPicking.addShaderFromSourceFile(QOpenGLShader::Geometry, "../shaders/edges/picking/gs.glsl");
    m_programPicking.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/edges/picking/fs.glsl");
    m_programPicking.link();

    //get location of uniforms
    m_programPicking.bind();
    m_projMatrixPickingLoc = m_programPicking.uniformLocation("projMatrix");
    m_viewMatrixPickingLoc = m_programPicking.uniformLocation("mvMatrix");
    m_invViewportPickingLoc = m_programPicking.uniformLocation("invViewport");
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
    m_data.resize(nbOfAdd * m_floatsPerVertex);

    int ID = 1;

    //for each halfedge
    for (he::HalfEdge* he: m_mesh->halfEdgesNoTwin()) {
        bool isSelected = ID == m_selectedEdge;
        QVector3D color = isSelected ? QVector3D(0.0, 0.6, 0.0) : QVector3D(0.0, 0.0, 0.0);
        //we will display a line
        this->addVertexEdge(he->origin()->pos(), color, static_cast<float>(ID));
        this->addVertexEdge(he->next()->origin()->pos(), color, static_cast<float>(ID));
        ID++;
    }

    this->update();
}

void BatchEdge::render(PickingType type) {
    switch (type) {
        case PickingType::PickingEdge: {
            bool cullFaceEnabled = glIsEnabled(GL_CULL_FACE);
            if (cullFaceEnabled) {
                glDisable(GL_CULL_FACE);
            }
            m_programPicking.bind();
            m_vao.bind();
            glDrawArrays(GL_LINES, 0, m_count / m_floatsPerVertex);
            m_programPicking.release();
            if (cullFaceEnabled) {
                glEnable(GL_CULL_FACE);
            }
            break;
        }

        case PickingType::PickingNone: {
            bool cullFaceEnabled = glIsEnabled(GL_CULL_FACE);
            if (cullFaceEnabled) {
                glDisable(GL_CULL_FACE);
            }
            m_program.bind();
            m_vao.bind();
            glDrawArrays(GL_LINES, 0, m_count / m_floatsPerVertex);
            m_program.release();
            if (cullFaceEnabled) {
                glEnable(GL_CULL_FACE);
            }
            break;
        }
        case PickingType::PickingFace:
        case PickingType::PickingVertex:
        case PickingType::PickingCircle:
            break;
    }
}

void BatchEdge::setProjection(QMatrix4x4 matrix) {
    m_program.bind();
    m_program.setUniformValue(m_projMatrixLoc, matrix);
    m_program.release();

    m_programPicking.bind();
    m_programPicking.setUniformValue(m_projMatrixPickingLoc, matrix);
    m_programPicking.release();
}

void BatchEdge::setCamera(Camera camera) {
    camera.zoom(0.001f);
    m_program.bind();
    m_program.setUniformValue(m_viewMatrixLoc, camera.getViewMatrix());
    m_program.release();

    m_programPicking.bind();
    m_programPicking.setUniformValue(m_viewMatrixPickingLoc, camera.getViewMatrix());
    m_programPicking.release();
}

void BatchEdge::setInvViewport(float x, float y) {
    m_program.bind();
    m_program.setUniformValue(m_invViewportLoc, x, y);
    m_program.release();

    m_programPicking.bind();
    m_programPicking.setUniformValue(m_invViewportPickingLoc, x, y);
    m_programPicking.release();
}

void BatchEdge::setMesh(he::Mesh* mesh) {
    m_mesh = mesh;
    m_selectedEdge = 0;
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

void BatchEdge::addVertexEdge(QVector3D const& v, QVector3D const& color, float ID) {
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
    *p = ID;
    //we update the amount of data
    m_count += m_floatsPerVertex;
}

int BatchEdge::renderOrder() {
    return 2;
}

int BatchEdge::pickingOrder() {
    return 2;
}
