#include "gui/model.h"

#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/mesh.h"
#include "halfedge/vertex.h"
#include "polytopal/circle.h"
#include <QMatrix4x4>

void Model::updateData() {
    this->updateDataEdges();
    this->updateDataCircles();
    this->updateDataCirclesDual();
    this->updateDataVertices();
}

void Model::updateDataEdges() {
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

    int ID = 1;

    QVector3D first;
    for (poly::Circle const& c: m_circles) {
        float isSelected = (ID == m_selectedCircle && m_selectedCircle != 0) ? 1.0f : -1.0f;

        for (int i = 0; i < 360; i += 4) {
            float alpha = qDegreesToRadians(static_cast<float>(i));
            float x = c.center().x() + c.radius() * std::cos(alpha) * c.axisX().x() + c.radius() * std::sin(alpha) * c.axisY().x();
            float y = c.center().y() + c.radius() * std::cos(alpha) * c.axisX().y() + c.radius() * std::sin(alpha) * c.axisY().y();
            float z = c.center().z() + c.radius() * std::cos(alpha) * c.axisX().z() + c.radius() * std::sin(alpha) * c.axisY().z();
            if (i == 0) {
                first = { x, y, z };
            } else {
                this->addVertexCircle({ x, y, z }, c.color(), static_cast<float>(ID), isSelected);
            }
            this->addVertexCircle({ x, y, z }, c.color(), static_cast<float>(ID), isSelected);
            if (i == 356) {
                this->addVertexCircle(first, c.color(), static_cast<float>(ID), isSelected);
            }
        }
        ID++;
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
                this->addVertexCircleDual({ x, y, z }, c.color());
            }
            this->addVertexCircleDual({ x, y, z }, c.color());
            if (i == 356) {
                this->addVertexCircleDual(first, c.color());
            }
        }
    }
}

void Model::updateDataVertices() {
    m_countVertices = 0;
    m_dataVertices.clear();

    //the number of vertices plus the projection point of the sphere mesh
    //qsizetype nbOfVertices = (m_mesh != nullptr ? static_cast<qsizetype>(m_mesh->vertices().size()) : 0) + (m_sphereMesh == nullptr ? 0 : 1);
    qsizetype nbOfVertices = (m_mesh != nullptr ? static_cast<qsizetype>(m_mesh->vertices().size()) : 0);

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
            float isSelected = ((ID == m_selectedVertex && m_selectedVertex != 0) || (ID == m_selectedVertex2 && m_selectedVertex2 != 0)) ? 1.0f : -1.0f;
            this->addVertex(v->pos(), { 0.0f, 0.0f, 0.0f }, static_cast<float>(ID), isSelected);
            ID++;
        }
    }

//    if (m_sphereMesh != nullptr) {
//        //display projection point
//        this->addVertex({ 0.0f, 0.0f, 1.0f }, { 1.0f, 0.0f, 0.0f }, 0.0f, -1.0f);
//    }
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
    //the ID of the edge
    *p++ = ID;
    //whether the edge is selected or not
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
    //the ID of the face
    *p++ = ID;
    //whether the face is selected or not
    *p = isSelected;
    //we update the amount of data
    m_countCircle += 8;
}

void Model::addVertexCircleDual(QVector3D const& v, QVector3D const& color) {
    //add to the end of the data already added
    float* p = m_dataCirclesDual.data() + m_countCircleDual;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p++ = v.z();
    *p++ = color.x();
    *p++ = color.y();
    *p = color.z();
    //we update the amount of data
    m_countCircleDual += 6;
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

void Model::setMesh(he::Mesh* mesh) {
    m_mesh = mesh;
    //reset the selected elements
    this->setSelectedEdge(0);
    this->setSelectedVertex(0);
    this->setSelectedCircle(0);
    //update buffers
    this->updateData();
}

void Model::setSelectedEdge(int edgeIndex) {
    m_selectedEdge = edgeIndex;
}

void Model::setSelectedVertex(int vertexIndex) {
    m_selectedVertex = vertexIndex;
}

void Model::setSelectedVertex2(int vertexIndex) {
    m_selectedVertex2 = vertexIndex;
}

void Model::setSelectedCircle(int circleIndex) {
    m_selectedCircle = circleIndex;
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

he::Vertex* Model::selectedVertex2() {
    he::Vertex* res = nullptr;

    if (m_selectedVertex2 - 1 >= 0 && m_selectedVertex2 - 1 < static_cast<qsizetype>(m_mesh->vertices().size())) {
        res = m_mesh->vertices().at(m_selectedVertex2 - 1);
    }

    return res;
}

poly::Circle* Model::selectedCircle() {
    poly::Circle* res = nullptr;

    if (m_selectedCircle - 1 >= 0 && m_selectedCircle - 1 < m_circles.size()) {
        res = &m_circles[m_selectedCircle - 1];
    }

    return res;
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

void Model::transformMesh(QMatrix4x4 const& transform) {
    if (m_mesh == nullptr) { return; }
    for (he::Vertex* v: m_mesh->vertices()) {
        v->setPos((transform * v->pos().toVector4D()).toVector3D());
    }
    m_mesh->updateDoublePosFromFloatPos();
    this->updateDataEdges();
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

void Model::scaleCircles(float by) {
    if (this->selectedCircle() != nullptr) {
        this->selectedCircle()->setRadius(this->selectedCircle()->radius() + by);
        this->selectedCircle()->initInversiveCoordinates();
    } else {
        for (poly::Circle& c: m_circles) {
            c.setRadius(c.radius() + by);
            c.initInversiveCoordinates();
        }
    }
}

QVector<poly::Circle> const& Model::circles() const {
    return m_circles;
}

he::Mesh* Model::mesh() {
    return m_mesh;
}
