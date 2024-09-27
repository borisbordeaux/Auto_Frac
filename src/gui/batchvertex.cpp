#include "gui/batchvertex.h"
#include "halfedge/mesh.h"
#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

void BatchVertex::init() {
    this->initializeOpenGLFunctions();

    m_vaoVertices.create();
    m_vboVertices.create();
    m_vaoVertices.bind();
    m_vboVertices.bind();

    //enable enough attrib array for all the data of the edge's vertex
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //color
    glEnableVertexAttribArray(2); //ID for picking
    glEnableVertexAttribArray(3); //is selected
    //coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), nullptr);
    //color of the vertex
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //the ID
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    //whether it's selected or not, to simplify the code, a negative value means not selected while a positive value means selected
    glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(7 * sizeof(GLfloat)));
    m_vboVertices.release();
    m_vaoVertices.release();

    m_programVertices = new QOpenGLShaderProgram();
    m_programVertices->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/vertices/vs.glsl");
    m_programVertices->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/vertices/fs.glsl");
    m_programVertices->bindAttributeLocation("vertex", 0);
    m_programVertices->bindAttributeLocation("color", 1);
    m_programVertices->bindAttributeLocation("ID", 2);
    m_programVertices->bindAttributeLocation("isSelected", 3);
    m_programVertices->link();

    //get location of uniforms
    m_programVertices->bind();
    m_projMatrixLocVertices = m_programVertices->uniformLocation("projMatrix");
    m_mvMatrixLocVertices = m_programVertices->uniformLocation("mvMatrix");

    m_programVerticesPicking = new QOpenGLShaderProgram();
    m_programVerticesPicking->addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/vertices/picking/vs.glsl");
    m_programVerticesPicking->addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/vertices/picking/fs.glsl");
    m_programVerticesPicking->bindAttributeLocation("vertex", 0);
    m_programVerticesPicking->bindAttributeLocation("color", 1);
    m_programVerticesPicking->bindAttributeLocation("ID", 2);
    m_programVerticesPicking->bindAttributeLocation("isSelected", 3);
    m_programVerticesPicking->link();

    //get location of uniforms
    m_programVerticesPicking->bind();
    m_projMatrixPickingLocVertices = m_programVerticesPicking->uniformLocation("projMatrix");
    m_mvMatrixPickingLocVertices = m_programVerticesPicking->uniformLocation("mvMatrix");

    this->updateData();
}

void BatchVertex::update() {
    m_vboVertices.bind();
    m_vboVertices.allocate(m_dataVertices.constData(), m_countVertices * static_cast<int>(sizeof(GLfloat)));
    m_vboVertices.release();
}

void BatchVertex::updateData() {
    m_countVertices = 0;
    m_dataVertices.clear();

    //the number of vertices of the mesh plus the projection point on sphere
    qsizetype nbOfVertices = (m_mesh != nullptr ? static_cast<qsizetype>(m_mesh->vertices().size()) : 0) + 1;

    //for each vertex, there is 1 add
    qsizetype nbOfAdd = 1 * nbOfVertices;

    //we resize the data for rapidity
    m_dataVertices.resize(nbOfAdd * 8);

    this->addVertex({ 0.0f, 0.0f, 1.0f }, { 1.0f, 0.0f, 0.0f }, 0.0f, -1.0f);

    int ID = 1;

    if (m_mesh != nullptr) {
        //for each vertex
        for (he::Vertex* v: m_mesh->vertices()) {
            //will display a point
            float isSelected = ((ID == m_selectedVertex && m_selectedVertex != 0) || (ID == m_selectedVertex2 && m_selectedVertex2 != 0)) ? 1.0f : -1.0f;
            this->addVertex(v->pos(), { 0.0f, 0.0f, 0.0f }, static_cast<float>(ID), isSelected);
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
            m_programVerticesPicking->bind();
            m_vaoVertices.bind();
            glDrawArrays(GL_POINTS, 1, m_countVertices / m_floatsPerVertex - 1);
            m_programVerticesPicking->release();
            break;
        case PickingType::PickingNone:
            m_programVertices->bind();
            m_vaoVertices.bind();
            if (m_displayMesh && !m_displayProjectionPoint) {
                glDrawArrays(GL_POINTS, 1, m_countVertices / m_floatsPerVertex - 1);
            }
            if (!m_displayMesh && m_displayProjectionPoint) {
                glDrawArrays(GL_POINTS, 0, 1);
            }
            if (m_displayMesh && m_displayProjectionPoint) {
                glDrawArrays(GL_POINTS, 0, m_countVertices / m_floatsPerVertex);
            }
            m_programVertices->release();
            break;
        case PickingType::PickingFace:
        case PickingType::PickingEdge:
        case PickingType::PickingCircle:
            break;
    }
}

void BatchVertex::setProjection(QMatrix4x4 matrix) {
    m_programVertices->bind();
    m_programVertices->setUniformValue(m_projMatrixLocVertices, matrix);
    m_programVertices->release();

    m_programVerticesPicking->bind();
    m_programVerticesPicking->setUniformValue(m_projMatrixPickingLocVertices, matrix);
    m_programVerticesPicking->release();
}

void BatchVertex::setCamera(Camera camera) {
    camera.zoom(0.001f);
    camera.zoom(0.001f);

    m_programVertices->bind();
    m_programVertices->setUniformValue(m_mvMatrixLocVertices, camera.getViewMatrix());
    m_programVertices->release();

    m_programVerticesPicking->bind();
    m_programVerticesPicking->setUniformValue(m_mvMatrixPickingLocVertices, camera.getViewMatrix());
    m_programVerticesPicking->release();
}

void BatchVertex::setMesh(he::Mesh* mesh) {
    m_mesh = mesh;
    m_displayMesh = true;
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

void BatchVertex::addVertex(const QVector3D& v, const QVector3D& color, float ID, float isSelected) {
    //add to the end of the data already added
    float* p = m_dataVertices.data() + m_countVertices;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p++ = v.z();
    *p++ = color.x();
    *p++ = color.y();
    *p++ = color.z();
    //the ID of the vertex
    *p++ = ID;
    //whether the vertex is selected or not
    *p = isSelected;
    //we update the amount of data
    m_countVertices += 8;
}
