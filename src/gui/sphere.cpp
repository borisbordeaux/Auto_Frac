#include "gui/sphere.h"
#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/mesh.h"
#include "halfedge/vertex.h"

void Sphere::init() {
    this->initializeOpenGLFunctions();

    m_vao.create();
    m_vbo.create();

    m_vao.bind();
    m_vbo.bind();

    //enable enough attrib array for all the data of the mesh's vertices
    glEnableVertexAttribArray(0); //coordinates
    //3 coordinates of the vertex
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), nullptr);
    m_vbo.release();
    m_vao.release();

    m_program.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/sphere/vs.glsl");
    m_program.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/sphere/fs.glsl");
    m_program.bindAttributeLocation("vertex", 0);
    m_program.link();

    //get locations of uniforms
    m_program.bind();
    m_projMatrixLocSphere = m_program.uniformLocation("projMatrix");
    m_mvMatrixLocSphere = m_program.uniformLocation("mvMatrix");
    m_lightPosLocSphere = m_program.uniformLocation("lightPos");
    m_cameraPosLocSphere = m_program.uniformLocation("cameraPosition");
}

void Sphere::update() {
    m_count = 0;
    m_data.clear();

    if (m_sphereMesh == nullptr) { return; }
    //we add data using triangles
    qsizetype nbTriangle = Sphere::findNbOfTriangle(m_sphereMesh);

    //for each triangleSphere, there are 3 vertices
    qsizetype nbOfAdd = 3 * nbTriangle;

    //we resize the data for rapidity
    m_data.resize(nbOfAdd * 6);

    //add each face
    for (he::Face* f: m_sphereMesh->faces()) {
        this->addFaceSphere(f);
    }

    //send data to GPU
    m_vbo.bind();
    m_vbo.allocate(m_data.constData(), m_count * static_cast<int>(sizeof(GLfloat)));
    m_vbo.release();
}

void Sphere::render(PickingType type) {
    if (type != PickingType::PickingNone) { glColorMask(false, false, false, false); }
    m_program.bind();
    m_vao.bind();
    glDrawArrays(GL_TRIANGLES, 0, m_count / m_floatsPerVertex);
    m_program.release();
    if (type != PickingType::PickingNone) { glColorMask(true, true, true, true); }
}

void Sphere::setProjection(QMatrix4x4 matrix) {
    m_program.bind();
    m_program.setUniformValue(m_projMatrixLocSphere, matrix);
    m_program.release();
}

void Sphere::setCamera(Camera camera) {
    m_program.bind();
    m_program.setUniformValue(m_mvMatrixLocSphere, camera.getViewMatrix());
    m_program.setUniformValue(m_cameraPosLocSphere, camera.getEye());
    m_program.release();
}

void Sphere::setLight(QVector3D lightPos) {
    m_program.bind();
    m_program.setUniformValue(m_lightPosLocSphere, lightPos);
    m_program.release();
}

void Sphere::setSphereMesh(he::Mesh* mesh) {
    m_sphereMesh = mesh;
}

he::Mesh* Sphere::sphereMesh() const {
    return m_sphereMesh;
}

void Sphere::addFaceSphere(he::Face* f) {
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

void Sphere::addVertexSphere(const QVector3D& v) {
    //add to the end of the data already added
    float* p = m_data.data() + m_count;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p = v.z();
    //we update the amount of data
    m_count += 3;
}

void Sphere::triangleSphere(const QVector3D& pos1, const QVector3D& pos2, const QVector3D& pos3) {
    this->addVertexSphere(pos1);
    this->addVertexSphere(pos2);
    this->addVertexSphere(pos3);
}

qsizetype Sphere::findNbOfTriangle(he::Mesh* mesh) {
    qsizetype nb = 0;

    //for each face
    for (he::Face* f: mesh->faces()) {
        //the number of triangle of a face
        //is the number of edges - 2
        nb += static_cast<qsizetype>(f->nbEdges() - 2);
    }

    return nb;
}
