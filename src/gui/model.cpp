#include "gui/model.h"

#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/mesh.h"
#include "halfedge/vertex.h"
#include "polytopal/circle.h"
#include <QMatrix4x4>

void Model::updateData() {
    this->updateDataFaces();
    this->updateDataSphere();
    this->updateDataEdge();
    this->updateDataCircles();
    this->updateDataCirclesDual();
    this->updateDataVertices();
}

void Model::updateDataFaces() {
    m_countFace = 0;
    m_dataFace.clear();

    if (m_mesh == nullptr) { return; }
    //we add data using triangles
    qsizetype nbTriangle = Model::findNbOfTriangle(m_mesh);

    //for each triangle, there are 3 vertices
    qsizetype nbOfAdd = 3 * nbTriangle;

    //we resize the data for rapidity
    m_dataFace.resize(nbOfAdd * 8);

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
}

void Model::updateDataSphere() {
    m_countSphere = 0;
    m_dataSphere.clear();

    if (m_sphereMesh == nullptr) { return; }
    //we add data using triangles
    qsizetype nbTriangle = Model::findNbOfTriangle(m_sphereMesh);

    //for each triangleSphere, there are 3 vertices
    qsizetype nbOfAdd = 3 * nbTriangle;

    //we resize the data for rapidity
    m_dataSphere.resize(nbOfAdd * 6);

    //add each face
    for (he::Face* f: m_sphereMesh->faces()) {
        this->addFaceSphere(f);
    }
}

void Model::updateDataEdge() {
    m_countEdge = 0;
    m_dataEdge.clear();

    if (m_mesh == nullptr) { return; }

    //the number of edges
    qsizetype nbOfEdges = static_cast<qsizetype>(m_mesh->halfEdgesNoTwin().size());

    //for each edge, there are 2 vertices
    qsizetype nbOfAdd = 2 * nbOfEdges;

    //we resize the data for rapidity
    m_dataEdge.resize(nbOfAdd * 8);

    int ID = 1;

    //for each halfedge
    for (he::HalfEdge* he: m_mesh->halfEdgesNoTwin()) {
        float isSelected = (ID == m_selectedEdge && m_selectedEdge != 0) ? 1.0f : -1.0f;
        //we will display a line
        this->addVertexEdge(he->origin()->pos(), { 0, 0, 0 }, static_cast<float>(ID), isSelected);
        this->addVertexEdge(he->next()->origin()->pos(), { 0, 0, 0 }, static_cast<float>(ID), isSelected);
        ID++;
    }
}

void Model::updateDataCircles() {
    //the amount of data of the circles
    m_countCircle = 0;
    m_dataCircles.clear();

    //the number of edges
    qsizetype nbOfEdges = findNbOfSegmentsCircles();

    //for each edge, there are 2 vertices
    qsizetype nbOfAdd = 2 * nbOfEdges;

    //we resize the data for rapidity
    m_dataCircles.resize(nbOfAdd * 8);

    QVector3D first;
    for (poly::Circle const& c: m_circles) {
        for (int i = 0; i < 360; i += 4) {
            float alpha = qDegreesToRadians(static_cast<float>(i));
            float x = c.center().x() + c.radius() * std::cos(alpha) * c.axisX().x() + c.radius() * std::sin(alpha) * c.axisY().x();
            float y = c.center().y() + c.radius() * std::cos(alpha) * c.axisX().y() + c.radius() * std::sin(alpha) * c.axisY().y();
            float z = c.center().z() + c.radius() * std::cos(alpha) * c.axisX().z() + c.radius() * std::sin(alpha) * c.axisY().z();
            if (i == 0) {
                first = { x, y, z };
            } else {
                this->addVertexCircle({ x, y, z }, c.color(), -2.0f, -1.0f);
            }
            this->addVertexCircle({ x, y, z }, c.color(), -2.0f, -1.0f);
            if (i == 356) {
                this->addVertexCircle(first, c.color(), -2.0f, -1.0f);
            }
        }
    }
}

void Model::updateDataCirclesDual() {
    //the amount of data of the circles
    m_countCircleDual = 0;
    m_dataCirclesDual.clear();

    //the number of edges
    qsizetype nbOfEdges = findNbOfSegmentsCirclesDual();

    //for each edge, there are 2 vertices
    qsizetype nbOfAdd = 2 * nbOfEdges;

    //we resize the data for rapidity
    m_dataCirclesDual.resize(nbOfAdd * 8);

    QVector3D first;
    for (poly::Circle const& c: m_circlesDual) {
        for (int i = 0; i < 360; i += 4) {
            float alpha = qDegreesToRadians(static_cast<float>(i));
            float x = c.center().x() + c.radius() * std::cos(alpha) * c.axisX().x() + c.radius() * std::sin(alpha) * c.axisY().x();
            float y = c.center().y() + c.radius() * std::cos(alpha) * c.axisX().y() + c.radius() * std::sin(alpha) * c.axisY().y();
            float z = c.center().z() + c.radius() * std::cos(alpha) * c.axisX().z() + c.radius() * std::sin(alpha) * c.axisY().z();
            if (i == 0) {
                first = { x, y, z };
            } else {
                this->addVertexCircleDual({ x, y, z }, c.color(), -2.0f, -1.0f);
            }
            this->addVertexCircleDual({ x, y, z }, c.color(), -2.0f, -1.0f);
            if (i == 356) {
                this->addVertexCircleDual(first, c.color(), -2.0f, -1.0f);
            }
        }
    }
}

void Model::updateDataVertices() {
    m_countVertices = 0;
    m_dataVertices.clear();

    //the number of vertices plus the projection point of the sphere mesh
    qsizetype nbOfVertices = (m_mesh != nullptr ? static_cast<qsizetype>(m_mesh->vertices().size()) : 0) + (m_sphereMesh == nullptr ? 0 : 1);

    //if no vertices, no need to compute the rest
    if (nbOfVertices == 0) { return; }

    //for each vertex, there is 1 add
    qsizetype nbOfAdd = 1 * nbOfVertices;

    //we resize the data for rapidity
    m_dataVertices.resize(nbOfAdd * 8);

    int ID = 1;

    if (m_mesh != nullptr) {
        //for each vertex
        for (he::Vertex* v: m_mesh->vertices()) {
            //will display a point
            float isSelected = (ID == m_selectedVertex && m_selectedVertex != 0) ? 1.0f : -1.0f;
            this->addVertex(v->pos(), { 0.0f, 0.0f, 0.0f }, static_cast<float>(ID), isSelected);
            ID++;
        }
    }

    if (m_sphereMesh != nullptr) {
        //display projection point
        this->addVertex({ 0.0f, 0.0f, 1.0f }, { 1.0f, 0.0f, 0.0f }, 0.0f, -1.0f);
    }
}

void Model::addVertexFace(const QVector3D& v, const QVector3D& n, float ID, float isSelected) {
    //add to the end of the data already added
    float* p = m_dataFace.data() + m_countFace;
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
    m_countFace += 8;
}

void Model::addVertexSphere(const QVector3D& v) {
    //add to the end of the data already added
    float* p = m_dataSphere.data() + m_countSphere;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p++ = v.z();
    //the normal of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p = v.z();
    //we update the amount of data
    m_countSphere += 6;
}

void Model::addVertexEdge(QVector3D const& v, QVector3D const& color, float ID, float isSelected) {
    //add to the end of the data already added
    float* p = m_dataEdge.data() + m_countEdge;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p++ = v.z();
    *p++ = color.x();
    *p++ = color.y();
    *p++ = color.z();
    //the ID of the face
    *p++ = ID;
    //whether the face is selected or not
    *p = isSelected;
    //we update the amount of data
    m_countEdge += 8;
}

void Model::addVertexCircle(QVector3D const& v, QVector3D const& color, float ID, float isSelected) {
    //add to the end of the data already added
    float* p = m_dataCircles.data() + m_countCircle;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p++ = v.z();
    *p++ = color.x();
    *p++ = color.y();
    *p++ = color.z();
    //the ID of the circle
    *p++ = ID;
    //whether the face is selected or not
    *p = isSelected;
    //we update the amount of data
    m_countCircle += 8;
}

void Model::addVertexCircleDual(QVector3D const& v, QVector3D const& color, float ID, float isSelected) {
    //add to the end of the data already added
    float* p = m_dataCirclesDual.data() + m_countCircleDual;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p++ = v.z();
    *p++ = color.x();
    *p++ = color.y();
    *p++ = color.z();
    //the ID of the circle
    *p++ = ID;
    //whether the face is selected or not
    *p = isSelected;
    //we update the amount of data
    m_countCircleDual += 8;
}

void Model::addVertex(QVector3D const& v, QVector3D const& color, float ID, float isSelected) {
    //add to the end of the data already added
    float* p = m_dataVertices.data() + m_countVertices;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p++ = v.z();
    *p++ = color.x();
    *p++ = color.y();
    *p++ = color.z();
    //the ID of the face
    *p++ = ID;
    //whether the face is selected or not
    *p = isSelected;
    //we update the amount of data
    m_countVertices += 8;
}

void Model::triangle(QVector3D const& pos1, QVector3D const& pos2, QVector3D const& pos3, float ID, float isSelected) {
    //compute the normal of the triangleSphere
    QVector3D n = QVector3D::normal(pos2 - pos1, pos3 - pos2);

    //add the vertices to the data
    this->addVertexFace(pos1, n, ID, isSelected);
    this->addVertexFace(pos2, n, ID, isSelected);
    this->addVertexFace(pos3, n, ID, isSelected);
}

qsizetype Model::findNbOfTriangle(he::Mesh* mesh) {
    qsizetype nb = 0;

    //for each face
    for (he::Face* f: mesh->faces()) {
        //the number of triangle of a face
        //is the number of edges - 2
        nb += static_cast<qsizetype>(f->nbEdges() - 2);
    }

    return nb;
}

void Model::setMesh(he::Mesh* mesh) {
    m_mesh = mesh;
    //reset the selected elements
    this->setSelectedFace(0);
    this->setSelectedEdge(0);
    this->setSelectedVertex(0);
    //update buffers
    this->updateData();
}

void Model::setSelectedFace(int faceIndex) {
    m_selectedFace = faceIndex;
}

void Model::setSelectedEdge(int edgeIndex) {
    m_selectedEdge = edgeIndex;
}

void Model::setSelectedVertex(int vertexIndex) {
    m_selectedVertex = vertexIndex;
}

he::Face* Model::selectedFace() {
    he::Face* res = nullptr;

    if (m_selectedFace - 1 >= 0 && m_selectedFace - 1 < static_cast<qsizetype>(m_mesh->faces().size())) {
        res = m_mesh->faces().at(m_selectedFace - 1);
    }

    return res;
}

he::HalfEdge* Model::selectedEdge() {
    he::HalfEdge* res = nullptr;

    if (m_selectedEdge - 1 >= 0 && m_selectedEdge - 1 < static_cast<qsizetype>(m_mesh->halfEdgesNoTwin().size())) {
        res = m_mesh->halfEdgesNoTwin().at(m_selectedEdge - 1);
    }

    return res;
}

he::Vertex* Model::selectedVertex() {
    he::Vertex* res = nullptr;

    if (m_selectedVertex - 1 >= 0 && m_selectedVertex - 1 < static_cast<qsizetype>(m_mesh->vertices().size())) {
        res = m_mesh->vertices().at(m_selectedVertex - 1);
    }

    return res;
}

void Model::addFace(he::Face* f, int ID) {
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

void Model::setSphereMesh(he::Mesh* mesh) {
    m_sphereMesh = mesh;
    this->updateDataSphere();
    //for projection point
    this->updateDataVertices();
}

void Model::addCircle(poly::Circle const& circle) {
    m_circles.push_back(circle);
}

void Model::addCircleDual(poly::Circle const& circle) {
    m_circlesDual.push_back(circle);
}

void Model::resetCircles() {
    m_circles.clear();
}

void Model::resetCirclesDual() {
    m_circlesDual.clear();
}

qsizetype Model::findNbOfSegmentsCircles() const {
    return 90 * m_circles.size();
}

qsizetype Model::findNbOfSegmentsCirclesDual() const {
    return 90 * m_circlesDual.size();
}

he::Mesh* Model::sphereMesh() const {
    return m_sphereMesh;
}

void Model::triangleSphere(const QVector3D& pos1, const QVector3D& pos2, const QVector3D& pos3) {
    //add the vertices to the data
    this->addVertexSphere(pos1);
    this->addVertexSphere(pos2);
    this->addVertexSphere(pos3);
}

void Model::addFaceSphere(he::Face* f) {
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

void Model::transformMesh(QMatrix4x4 const& transform) {
    if (m_mesh == nullptr) { return; }
    for (he::Vertex* v: m_mesh->vertices()) {
        v->setPos((transform * v->pos().toVector4D()).toVector3D());
    }
    m_mesh->updateDoublePosFromFloatPos();
    this->updateDataFaces();
    this->updateDataEdge();
    this->updateDataVertices();
}

void Model::updateColorOfCircles(QVector3D const& color) {
    for (poly::Circle& c: m_circles) {
        c.setColor(color);
    }
    this->updateDataCircles();
}

void Model::updateColorOfCirclesDual(QVector3D const& color) {
    for (poly::Circle& c: m_circlesDual) {
        c.setColor(color);
    }
    this->updateDataCirclesDual();
}



