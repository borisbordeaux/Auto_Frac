#include "gui/batchface.h"
#include "halfedge/mesh.h"
#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

void BatchFace::init() {
    this->initializeOpenGLFunctions();

    m_vao.create();
    m_vbo.create();

    m_vao.bind();
    m_vbo.bind();

    //enable enough attrib array for all the data of the mesh's vertices
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //normal
    glEnableVertexAttribArray(2); //ID for picking
    glEnableVertexAttribArray(3); //is selected
    //3 coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), nullptr);
    //3 coordinates of the vertex's normal
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //the ID
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    //whether it's selected or not, to simplify the code, a negative value means not selected while a positive value means selected
    glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 8 * sizeof(GLfloat), reinterpret_cast<void*>(7 * sizeof(GLfloat)));
    m_vbo.release();
    m_vao.release();

    m_program.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/faces/vs.glsl");
    m_program.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/faces/fs.glsl");
    m_program.bindAttributeLocation("vertex", 0);
    m_program.bindAttributeLocation("normal", 1);
    m_program.bindAttributeLocation("ID", 2);
    m_program.bindAttributeLocation("isSelected", 3);
    m_program.link();

    //get locations of uniforms
    m_program.bind();
    m_projMatrixLoc = m_program.uniformLocation("projMatrix");
    m_viewMatrixLoc = m_program.uniformLocation("mvMatrix");
    m_lightPosLoc = m_program.uniformLocation("lightPos");
    m_cameraPosLoc = m_program.uniformLocation("cameraPosition");

    m_programPicking.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/faces/picking/vs.glsl");
    m_programPicking.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/faces/picking/fs.glsl");
    m_programPicking.bindAttributeLocation("vertex", 0);
    m_programPicking.bindAttributeLocation("normal", 1);
    m_programPicking.bindAttributeLocation("ID", 2);
    m_programPicking.bindAttributeLocation("isSelected", 3);
    m_programPicking.link();

    //get locations of uniforms
    m_programPicking.bind();
    m_projMatrixPickingLoc = m_programPicking.uniformLocation("projMatrix");
    m_viewMatrixPickingLoc = m_programPicking.uniformLocation("mvMatrix");
}

void BatchFace::update() {
    m_vbo.bind();
    m_vbo.allocate(m_data.constData(), m_count * static_cast<int>(sizeof(GLfloat)));
    m_vbo.release();
}

void BatchFace::updateData() {
    m_count = 0;
    m_data.clear();

    if (m_mesh == nullptr) { return; }
    //we add data using triangles
    qsizetype nbTriangle = BatchFace::findNbOfTriangle(m_mesh);

    //for each triangle, there are 3 vertices
    qsizetype nbOfAdd = 3 * nbTriangle;

    //we resize the data for rapidity
    m_data.resize(nbOfAdd * 8);

    // set the ID to 1 for the mesh faces
    // it will be incremented for each face
    int ID = 1;

    //for each face
    for (he::Face* f: m_mesh->faces()) {
        this->addFace(f, ID);
        //going to the next face
        //we increment the ID
        ID++;
    }

    this->update();
}

void BatchFace::render(PickingType type) {
    switch (type) {
        case PickingType::PickingFace:
            m_programPicking.bind();
            m_vao.bind();
            glDrawArrays(GL_TRIANGLES, 0, m_count / m_floatsPerVertex);
            m_programPicking.release();
            break;
        case PickingType::PickingEdge:
        case PickingType::PickingVertex:
        case PickingType::PickingCircle:
            //draw only in depth buffer
            glColorMask(false, false, false, false);
            m_program.bind();
            m_vao.bind();
            glDrawArrays(GL_TRIANGLES, 0, m_count / m_floatsPerVertex);
            m_program.release();
            glColorMask(true, true, true, true);
            break;
        case PickingType::PickingNone:
            m_program.bind();
            m_vao.bind();
            glDrawArrays(GL_TRIANGLES, 0, m_count / m_floatsPerVertex);
            m_program.release();
            break;
    }
}

void BatchFace::setProjection(QMatrix4x4 projection) {
    m_program.bind();
    m_program.setUniformValue(m_projMatrixLoc, projection);
    m_program.release();

    m_programPicking.bind();
    m_programPicking.setUniformValue(m_projMatrixPickingLoc, projection);
    m_programPicking.release();
}

void BatchFace::setCamera(Camera camera) {
    m_program.bind();
    m_program.setUniformValue(m_viewMatrixLoc, camera.getViewMatrix());
    m_program.setUniformValue(m_cameraPosLoc, camera.getEye());
    m_program.release();

    m_programPicking.bind();
    m_programPicking.setUniformValue(m_viewMatrixPickingLoc, camera.getViewMatrix());
    m_programPicking.release();
}

void BatchFace::setLight(QVector3D lightPos) {
    m_program.bind();
    m_program.setUniformValue(m_lightPosLoc, lightPos);
    m_program.release();
}

void BatchFace::setMesh(he::Mesh* mesh) {
    m_mesh = mesh;
    m_selectedFace = 0;
    this->updateData();
}

void BatchFace::setSelectedFace(int faceIndex) {
    m_selectedFace = faceIndex;
}

he::Face* BatchFace::selectedFace() {
    he::Face* res = nullptr;

    if (m_selectedFace - 1 >= 0 && m_selectedFace - 1 < static_cast<qsizetype>(m_mesh->faces().size())) {
        res = m_mesh->faces().at(m_selectedFace - 1);
    }

    return res;
}

qsizetype BatchFace::findNbOfTriangle(he::Mesh* mesh) {
    qsizetype nb = 0;

    //for each face
    for (he::Face* f: mesh->faces()) {
        //the number of triangle of a face
        //is the number of edges - 2
        nb += static_cast<qsizetype>(f->nbEdges() - 2);
    }

    return nb;
}

void BatchFace::addFace(he::Face* f, int ID) {
    //we compute the number of halfedges
    he::HalfEdge* he = f->halfEdge();
    he::HalfEdge* temp = f->halfEdge()->next();
    int nbHe = 1;

    while (temp != he) {
        temp = temp->next();
        nbHe++;
    }

    //we set the origin of the triangles
    QVector3D pos1 = he->origin()->pos();

    //then we can triangulate the face
    //using the origin and the other vertices
    for (int i = 0; i < nbHe - 2; i++) {
        QVector3D pos2 = he->next()->origin()->pos();
        QVector3D pos3 = he->next()->next()->origin()->pos();

        //if the face is selected, we will
        //throw 1.0 and -1.0 otherwise
        float isSelected = (ID == m_selectedFace && m_selectedFace != 0) ? 1.0f : -1.0f;

        triangle(pos1, pos2, pos3, static_cast<float>(ID), isSelected);

        he = he->next();
    }
}

void BatchFace::triangle(QVector3D const& pos1, QVector3D const& pos2, QVector3D const& pos3, float ID, float isSelected) {
    //compute the normal of the triangleSphere
    QVector3D n = QVector3D::normal(pos2 - pos1, pos3 - pos2);

    //add the vertices to the data
    this->addVertexFace(pos1, n, ID, isSelected);
    this->addVertexFace(pos2, n, ID, isSelected);
    this->addVertexFace(pos3, n, ID, isSelected);
}

void BatchFace::addVertexFace(QVector3D const& v, QVector3D const& n, float ID, float isSelected) {
    //add to the end of the data already added
    float* p = m_data.data() + m_count;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p++ = v.z();
    //the normal of the vertex
    *p++ = n.x();
    *p++ = n.y();
    *p++ = n.z();
    //the ID of the face
    *p++ = ID;
    //whether the face is selected or not
    *p = isSelected;
    //we update the amount of data
    m_count += m_floatsPerVertex;
}
