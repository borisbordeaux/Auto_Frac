#include "halfedge/vertex.h"

#include <utility>

#include "halfedge/halfedge.h"

he::Vertex::Vertex(float x, float y, float z, QString name) :
        m_x(x), m_y(y), m_z(z), m_halfEdge(nullptr), m_name(std::move(name)) {

}

float he::Vertex::x() const {
    return m_x;
}

void he::Vertex::setX(float x) {
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
    m_halfEdge = halfEdge;
}

QString he::Vertex::name() const {
    return m_name;
}

void he::Vertex::setName(QString const& name) {
    m_name = name;
}

bool he::Vertex::equals(he::Vertex* other) const {
    //compare each coordinate
    return abs(m_x - other->m_x) < 0.001 && abs(m_y - other->m_y) < 0.001 && abs(m_z - other->m_z) < 0.001;
}
