#include "gui/batchsphere.h"
#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/mesh.h"
#include "halfedge/vertex.h"
#include "polytopal/inversivecoordinates.h"

void BatchSphere::init() {
    this->initializeOpenGLFunctions();

    m_vao.create();
    glGenBuffers(1, &m_ssbo);
    m_vbo.create();

    m_vao.bind();

    glBindBuffer(GL_SHADER_STORAGE_BUFFER, m_ssbo);
    glBindBufferBase(GL_SHADER_STORAGE_BUFFER, 2, m_ssbo);
    glBindBuffer(GL_SHADER_STORAGE_BUFFER, 0); // unbind

    m_vbo.bind();

    //enable enough attrib array for all the data of the mesh's vertices
    glEnableVertexAttribArray(0); //coordinates
    //3 coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), nullptr);

    m_vbo.release();
    m_vao.release();

    m_program.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/sphere/vs.glsl");
    m_program.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/sphere/fs.glsl");
    m_program.link();

    //get locations of uniforms
    m_program.bind();
    m_projMatrixLoc = m_program.uniformLocation("projMatrix");
    m_viewMatrixLoc = m_program.uniformLocation("mvMatrix");
    m_lightPosLoc = m_program.uniformLocation("lightPos");
    m_cameraPosLoc = m_program.uniformLocation("cameraPosition");
    m_nbVerticesLoc = m_program.uniformLocation("nbVertices");
    m_renderTypeLoc = m_program.uniformLocation("renderType");
    m_displayNorthLoc = m_program.uniformLocation("displayNorth");

    this->updateMeshData({});
    this->setCircleRenderType(CircleRenderType::ILLUMINATED);
    this->setDisplayNorth(true);
}

void BatchSphere::update() {
    m_vbo.bind();
    m_vbo.allocate(m_data.constData(), m_count * static_cast<int>(sizeof(GLfloat)));
    m_vbo.release();
}

void BatchSphere::updateData() {
    m_count = 0;
    m_data.clear();

    if (m_sphereMesh.faces().empty()) { return; }
    //we add data using triangles
    qsizetype nbTriangle = this->findNbOfTriangle();

    //for each triangleSphere, there are 3 vertices
    qsizetype nbOfAdd = 3 * nbTriangle;

    //we resize the data for rapidity
    m_data.resize(nbOfAdd * 6);

    //add each face
    for (he::Face* f: m_sphereMesh.faces()) {
        this->addFaceSphere(f);
    }
}

void BatchSphere::render(PickingType type) {
    if (type != PickingType::PickingNone) { glColorMask(false, false, false, false); }
    m_program.bind();
    m_vao.bind();
    glBindBuffer(GL_SHADER_STORAGE_BUFFER, m_ssbo);
    glDrawArrays(GL_TRIANGLES, 0, m_count / m_floatsPerVertex);
    m_program.release();
    if (type != PickingType::PickingNone) { glColorMask(true, true, true, true); }
}

void BatchSphere::setProjection(QMatrix4x4 matrix) {
    m_program.bind();
    m_program.setUniformValue(m_projMatrixLoc, matrix);
    m_program.release();
}

void BatchSphere::setCamera(Camera camera) {
    m_program.bind();
    m_program.setUniformValue(m_viewMatrixLoc, camera.getViewMatrix());
    m_program.setUniformValue(m_cameraPosLoc, camera.getEye());
    m_program.release();
}

void BatchSphere::setLight(QVector3D lightPos) {
    m_program.bind();
    m_program.setUniformValue(m_lightPosLoc, lightPos);
    m_program.release();
}

void BatchSphere::setSphereMesh(he::Mesh&& mesh) {
    m_sphereMesh = std::move(mesh);
    this->updateData();
}

void BatchSphere::addFaceSphere(he::Face* f) {
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

        this->triangleSphere(pos1, pos2, pos3);

        he = he->next();
    }
}

void BatchSphere::addVertexSphere(const QVector3D& v) {
    //add to the end of the data already added
    float* p = m_data.data() + m_count;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p = v.z();
    //we update the amount of data
    m_count += 3;
}

void BatchSphere::triangleSphere(const QVector3D& pos1, const QVector3D& pos2, const QVector3D& pos3) {
    this->addVertexSphere(pos1);
    this->addVertexSphere(pos2);
    this->addVertexSphere(pos3);
}

qsizetype BatchSphere::findNbOfTriangle() {
    qsizetype nb = 0;

    //for each face
    for (he::Face* f: m_sphereMesh.faces()) {
        //the number of triangle of a face
        //is the number of edges - 2
        nb += static_cast<qsizetype>(f->nbEdges() - 2);
    }

    return nb;
}

void BatchSphere::updateMeshData(std::vector<poly::InversiveCoordinates> const& circles) {
    if (circles.empty()) {
        m_program.bind();
        glUniform1ui(m_nbVerticesLoc, 0);
        m_program.release();
        return;
    }

    std::vector<float> data;
    data.reserve(circles.size() * 3);
    for (poly::InversiveCoordinates const& c: circles) {
        QVector3D v = c.lightPoint().toQVector3D();
        data.push_back(v.x());
        data.push_back(v.y());
        data.push_back(v.z());
    }

    glBindBuffer(GL_SHADER_STORAGE_BUFFER, m_ssbo);
    glBufferData(GL_SHADER_STORAGE_BUFFER, static_cast<long>(data.size() * sizeof(float)), data.data(), GL_DYNAMIC_DRAW);
    glBindBuffer(GL_SHADER_STORAGE_BUFFER, 0); // unbind

    m_program.bind();
    glUniform1ui(m_nbVerticesLoc, static_cast<unsigned int>(data.size()));
    m_program.release();
}

void BatchSphere::setCircleRenderType(CircleRenderType type) {
    m_program.bind();
    switch (type) {
        case CircleRenderType::TRANSPARENT:
            glUniform1i(m_renderTypeLoc, 0);
            break;
        case CircleRenderType::ILLUMINATED:
            glUniform1i(m_renderTypeLoc, 1);
            break;
        case CircleRenderType::NONE:
            glUniform1i(m_renderTypeLoc, 2);
            break;
    }
    m_program.release();
}

void BatchSphere::setDisplayNorth(bool display) {
    m_program.bind();
    glUniform1ui(m_displayNorthLoc, display ? 1 : 0);
    m_program.release();
}

int BatchSphere::renderOrder() {
    return 3;
}

int BatchSphere::pickingOrder() {
    return 4;
}
