#include "gui/model.h"

#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/mesh.h"
#include "halfedge/vertex.h"
#include "polytopal/circle.h"

void Model::updateData() {
    //the amount of data of the polyhedron
    m_count = 0;
    m_data.clear();
    //the amount of data of the edges
    m_countEdge = 0;
    m_dataEdge.clear();

    updateDataFaces();

    updateDataSphere();

    updateDataEdge();

    updateDataCircles();
}

void Model::updateDataFaces() {
    if (m_mesh == nullptr) { return; }
    //we add data using triangles
    int nbTriangle = findNbOfTriangle(m_mesh);

    //for each triangle, there are 3 vertices
    int nbOfAdd = 3 * nbTriangle;

    //we resize the data for rapidity
    m_data.resize(nbOfAdd * 8);

    //set the ID to 1 for the mesh faces and it will be incremented for each face
    int ID = 1;

    //for each face
    for (he::Face* f: m_mesh->faces()) {
        addFace(f, ID);
        //going to the next face
        //we increment the ID
        ID++;
    }
}

void Model::updateDataEdge() {
    if (m_mesh == nullptr) { return; }
    //the number of edges
    int nbOfEdges = findNbOfEdges();
    //for each edge, there are 2 vertices
    int nbOfAdd = 2 * nbOfEdges;
    //we resize the data for rapidity
    m_dataEdge.resize(nbOfAdd * 6);

    //for each halfedge
    for (he::HalfEdge* he: m_mesh->halfEdges()) {
        //we will display a line
        add(he->origin()->pos());
        add(he->next()->origin()->pos());
    }
}

void Model::updateDataSphere() {
    if (m_sphereMesh == nullptr) { return; }
    //we add data using triangles
    int nbTriangle = findNbOfTriangle(m_sphereMesh);

    //for each triangle, there are 3 vertices
    int nbOfAdd = 3 * nbTriangle;
    //the amount of data of the polyhedron
    //m_count = 0;
    //m_data.clear();
    //we resize the data for rapidity
    m_data.resize(m_data.size() + nbOfAdd * 8);

    //set the ID to -2 to prevent selection of the sphere
    int ID = -2;

    //add each face
    for (he::Face* f: m_sphereMesh->faces()) {
        addFace(f, ID);
    }
}

void Model::updateDataCircles() {
    //the number of edges
    int nbOfEdges = 360 * static_cast<int>(m_circles.size()) + 360 * static_cast<int>(m_circlesDual.size());
    //for each edge, there are 2 vertices
    int nbOfAdd = 2 * nbOfEdges;
    m_dataEdge.resize(m_dataEdge.size() + nbOfAdd * 6);
    QVector3D c1 { 0.0f, 1.0f, 0.0f };
    QVector3D c2 { 0.0f, 0.0f, 0.0f };
    QVector3D first;
    for (poly::Circle const& c: m_circles) {
        for (int i = 0; i < 360; i++) {
            float alpha = qDegreesToRadians(static_cast<float>(i));
            float x = c.center().x() + c.radius() * std::cos(alpha) * c.axisX().x() + c.radius() * std::sin(alpha) * c.axisY().x();
            float y = c.center().y() + c.radius() * std::cos(alpha) * c.axisX().y() + c.radius() * std::sin(alpha) * c.axisY().y();
            float z = c.center().z() + c.radius() * std::cos(alpha) * c.axisX().z() + c.radius() * std::sin(alpha) * c.axisY().z();
            if (i == 0) {
                first = { x, y, z };
            } else {
                add({ x, y, z }, c1);
            }
            add({ x, y, z }, c1);
            if (i == 359) {
                add(first, c1);
            }
        }
    }

    for (poly::Circle const& c: m_circlesDual) {
        for (int i = 0; i < 360; i++) {
            float alpha = qDegreesToRadians(static_cast<float>(i));
            float x = c.center().x() + c.radius() * std::cos(alpha) * c.axisX().x() + c.radius() * std::sin(alpha) * c.axisY().x();
            float y = c.center().y() + c.radius() * std::cos(alpha) * c.axisX().y() + c.radius() * std::sin(alpha) * c.axisY().y();
            float z = c.center().z() + c.radius() * std::cos(alpha) * c.axisX().z() + c.radius() * std::sin(alpha) * c.axisY().z();
            if (i == 0) {
                first = { x, y, z };
            } else {
                add({ x, y, z }, c2);
            }
            add({ x, y, z }, c2);
            if (i == 359) {
                add(first, c2);
            }
        }
    }
}

void Model::add(const QVector3D& v, const QVector3D& n, float ID, float isSelected) {
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
    m_count += 8;
}

void Model::add(const QVector3D& v, const QVector3D& color) {
    //add to the end of the data already added
    float* p = m_dataEdge.data() + m_countEdge;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p++ = v.z();
    *p++ = color.x();
    *p++ = color.y();
    *p++ = color.z();
    //we update the amount of data
    m_countEdge += 6;
}

void Model::triangle(QVector3D const& pos1, QVector3D const& pos2, QVector3D const& pos3, float ID, float isSelected) {
    //compute the normal of the triangle
    QVector3D n = QVector3D::normal(pos2 - pos1, pos3 - pos2);

    //add the vertices to the data
    add(pos1, n, ID, isSelected);
    add(pos2, n, ID, isSelected);
    add(pos3, n, ID, isSelected);
}

int Model::findNbOfTriangle(he::Mesh* mesh) {
    int nb = 0;

    //for each face
    for (he::Face* f: mesh->faces()) {
        //we find the number of vertices of the face
        int nbVertices = 1;
        he::HalfEdge* he = f->halfEdge();
        he::HalfEdge* heNext = he->next();

        while (he != heNext) {
            heNext = heNext->next();
            nbVertices++;
        }

        //the number of triangle of a face
        //is the number of vertices - 2
        nb += nbVertices - 2;
    }

    return nb;
}

int Model::findNbOfEdges() const {
    return static_cast<int>(m_mesh->halfEdges().size());
}

void Model::setMesh(he::Mesh* mesh) {
    m_mesh = mesh;
    //reset the selected face
    setSelected(-1);
}

void Model::setSelected(int faceIndex) {
    m_selectedFace = faceIndex;
}

[[maybe_unused]] int Model::indexSelectedFace() const {
    return m_selectedFace;
}

[[maybe_unused]] he::Face* Model::selectedFace() {
    he::Face* res = nullptr;

    if (m_selectedFace >= 0 && m_selectedFace < static_cast<int>(m_mesh->faces().size())) {
        res = m_mesh->faces().at(m_selectedFace);
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
        float isSelected = ID == m_selectedFace ? 1.0f : -1.0f;

        triangle(pos1, pos2, pos3, static_cast<float>(ID), isSelected);

        he = he->next();
    }
}

void Model::setSphereMesh(he::Mesh* mesh) {
    m_sphereMesh = mesh;
    updateData();
}

void Model::addCircle(poly::Circle const& circle) {
    m_circles.push_back(circle);
}

void Model::addCircleDual(poly::Circle const& circle) {
    m_circlesDual.push_back(circle);
}

void Model::resetCircles() {
    m_circles.clear();
    m_circlesDual.clear();
}
