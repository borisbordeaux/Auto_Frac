#include "halfedge/vertex.h"
#include "halfedge/halfedge.h"
#include "halfedge/face.h"
#include "utils/utils.h"
#include "graph/vertex.h"


he::Vertex::Vertex(float x, float y, float z, QString name) :
        m_x(x), m_y(y), m_z(z), m_halfEdge(nullptr), m_name(std::move(name)) {

}

float he::Vertex::x() const {
    return m_x;
}

[[maybe_unused]] void he::Vertex::setX(float x) {
    m_x = x;
}

float he::Vertex::y() const {
    return m_y;
}

void he::Vertex::setY(float y) {
    m_y = y;
}

float he::Vertex::z() const {
    return m_z;
}

void he::Vertex::setZ(float z) {
    m_z = z;
}

he::HalfEdge* he::Vertex::halfEdge() {
    return m_halfEdge;
}

void he::Vertex::setHalfEdge(he::HalfEdge* halfEdge) {
    if (m_halfEdge == nullptr) {
        m_halfEdge = halfEdge;
    } else {
        this->addHalfEdge(m_halfEdge);
        m_halfEdge = halfEdge;
    }
}

QString he::Vertex::name() const {
    return m_name;
}

std::size_t he::Vertex::degree() const {
    return m_otherHalfEdges.size() + 1;
}

std::vector<he::Face*> he::Vertex::getAllFacesAroundVertex(he::Face* f) const {
    std::vector<he::Face*> facesAroundVertex;

    //fill all faces around vertex
    he::HalfEdge* h = this->m_halfEdge;
    he::HalfEdge* nxt = h;
    do {
        facesAroundVertex.push_back(nxt->face());
        nxt = nxt->twin()->next();
    } while (nxt != h);

    //order faces around vertex to have the given face in last
    std::vector<he::Face*> orderedFacesAroundVertex = facesAroundVertex;

    //if given face is in the list of all faces around this vertex
    if (std::find(facesAroundVertex.begin(), facesAroundVertex.end(), f) != facesAroundVertex.end()) {
        while (orderedFacesAroundVertex[orderedFacesAroundVertex.size() - 1] != f) {
            orderedFacesAroundVertex = frac::utils::shiftVector(orderedFacesAroundVertex);
        }
    }

    return orderedFacesAroundVertex;
}

void he::Vertex::addHalfEdge(he::HalfEdge* halfEdge) {
    m_otherHalfEdges.append(halfEdge);
}

QVector<he::HalfEdge*>& he::Vertex::otherHalfEdges() {
    return m_otherHalfEdges;
}
