#include "halfedge/vertex.h"

#include <utility>

#include "halfedge/halfedge.h"

poly::Vertex::Vertex(float x, float y, float z, QString name) :
        m_x(x), m_y(y), m_z(z), m_halfEdge(nullptr), m_name(std::move(name)) {

}

float poly::Vertex::x() const {
    return m_x;
}

void poly::Vertex::setX(float x) {
    m_x = x;
}

float poly::Vertex::y() const {
    return m_y;
}

void poly::Vertex::setY(float y) {
    m_y = y;
}

float poly::Vertex::z() const {
    return m_z;
}

void poly::Vertex::setZ(float z) {
    m_z = z;
}

poly::HalfEdge* poly::Vertex::halfEdge() {
    return m_halfEdge;
}

void poly::Vertex::setHalfEdge(poly::HalfEdge* halfEdge) {
    m_halfEdge = halfEdge;
}

QString poly::Vertex::name() const {
    return m_name;
}

void poly::Vertex::setName(QString const& name) {
    m_name = name;
}

bool poly::Vertex::equals(poly::Vertex* other) const {
    //compare each coordinate
    return abs(m_x - other->m_x) < 0.001 && abs(m_y - other->m_y) < 0.001 && abs(m_z - other->m_z) < 0.001;
}
