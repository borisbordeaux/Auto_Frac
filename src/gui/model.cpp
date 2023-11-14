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
    //the amount of data of the vertices
    m_countVertices = 0;
    m_dataVertices.clear();

    updateDataFaces();

    updateDataSphere();

    updateDataEdge();

    updateDataCircles();

    updateDataVertices();
}

void Model::updateDataFaces() {
    if (m_mesh == nullptr) { return; }
    //we add data using triangles
    qsizetype nbTriangle = findNbOfTriangle(m_mesh);

    //for each triangle, there are 3 vertices
    qsizetype nbOfAdd = 3 * nbTriangle;

    //we resize the data for rapidity
    m_data.resize(nbOfAdd * 8);

    // set the ID to 1 for the mesh faces
    // it will be incremented for each face
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
    qsizetype nbOfEdges = findNbOfEdges();
    //for each edge, there are 2 vertices
    qsizetype nbOfAdd = 2 * nbOfEdges;
    //we resize the data for rapidity
    m_dataEdge.resize(nbOfAdd * 8);

    float ID = 1.0f;

    //for each halfedge
    for (he::HalfEdge* he: m_mesh->halfEdges()) {
        //we will display a line
        addVertexEdge(he->origin()->pos(), { 0, 0, 0 }, ID, -1.0f);
        addVertexEdge(he->next()->origin()->pos(), { 0, 0, 0 }, ID, -1.0f);
        ID += 1.0f;
    }
}

void Model::updateDataSphere() {
    if (m_sphereMesh == nullptr) { return; }
    //we add data using triangles
    qsizetype nbTriangle = findNbOfTriangle(m_sphereMesh);

    //for each triangle, there are 3 vertices
    qsizetype nbOfAdd = 3 * nbTriangle;
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
    qsizetype nbOfEdges = 90 * m_circles.size() + 90 * m_circlesDual.size();
    //for each edge, there are 2 vertices
    qsizetype nbOfAdd = 2 * nbOfEdges;
    m_dataEdge.resize(m_dataEdge.size() + nbOfAdd * 8);
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
                addVertexEdge({ x, y, z }, c.color(), -2.0f, -1.0f);
            }
            addVertexEdge({ x, y, z }, c.color(), -2.0f, -1.0f);
            if (i == 356) {
                addVertexEdge(first, c.color(), -2.0f, -1.0f);
            }
        }
    }

    for (poly::Circle const& c: m_circlesDual) {
        for (int i = 0; i < 360; i += 4) {
            float alpha = qDegreesToRadians(static_cast<float>(i));
            float x = c.center().x() + c.radius() * std::cos(alpha) * c.axisX().x() + c.radius() * std::sin(alpha) * c.axisY().x();
            float y = c.center().y() + c.radius() * std::cos(alpha) * c.axisX().y() + c.radius() * std::sin(alpha) * c.axisY().y();
            float z = c.center().z() + c.radius() * std::cos(alpha) * c.axisX().z() + c.radius() * std::sin(alpha) * c.axisY().z();
            if (i == 0) {
                first = { x, y, z };
            } else {
                addVertexEdge({ x, y, z }, c.color(), -2.0f, -1.0f);
            }
            addVertexEdge({ x, y, z }, c.color(), -2.0f, -1.0f);
            if (i == 356) {
                addVertexEdge(first, c.color(), -2.0f, -1.0f);
            }
        }
    }
}

void Model::updateDataVertices() {
    //the number of vertices plus the projection point of the sphere mesh
    qsizetype nbOfVertices = (m_mesh != nullptr ? static_cast<qsizetype>(m_mesh->vertices().size()) : 0) + (m_sphereMesh == nullptr ? 0 : 1);

    //if no vertices, no need to compute the rest
    if (nbOfVertices == 0) { return; }

    //for each vertex, there is 1 add
    qsizetype nbOfAdd = 1 * nbOfVertices;
    //we resize the data for rapidity
    m_dataVertices.resize(nbOfAdd * 8);

    float ID = 1.0f;

    if (m_mesh != nullptr) {
        //for each vertex
        for (he::Vertex* v: m_mesh->vertices()) {
            //will display a point
            addVertex(v->pos(), { 0.0f, 0.0f, 0.0f }, ID, -1.0f);
        }
    }

    if (m_sphereMesh != nullptr) {
        //display projection point, the color depends on if the user is selecting or not
        addVertex({ 0, 0, 1 }, { 1, 0, 0 }, -2, -1.0f);
    }
}

void Model::addVertexFace(const QVector3D& v, const QVector3D& n, float ID, float isSelected) {
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
    //compute the normal of the triangle
    QVector3D n = QVector3D::normal(pos2 - pos1, pos3 - pos2);

    //add the vertices to the data
    addVertexFace(pos1, n, ID, isSelected);
    addVertexFace(pos2, n, ID, isSelected);
    addVertexFace(pos3, n, ID, isSelected);
}

qsizetype Model::findNbOfTriangle(he::Mesh* mesh) {
    qsizetype nb = 0;

    //for each face
    for (he::Face* f: mesh->faces()) {
        //we find the number of vertices of the face
        qsizetype nbVertices = 1;
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

qsizetype Model::findNbOfEdges() const {
    return static_cast<qsizetype>(m_mesh->halfEdges().size());
}

void Model::setMesh(he::Mesh* mesh) {
    m_mesh = mesh;
    //reset the selected face
    setSelected(-1);
}

void Model::setSelected(int faceIndex) {
    m_selectedFace = faceIndex;
}

[[maybe_unused]] qsizetype Model::indexSelectedFace() const {
    return m_selectedFace;
}

[[maybe_unused]] he::Face* Model::selectedFace() {
    he::Face* res = nullptr;

    if (m_selectedFace >= 0 && m_selectedFace < static_cast<qsizetype>(m_mesh->faces().size())) {
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
