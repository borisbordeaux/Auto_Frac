#include "halfedge/face.h"

#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

he::Face::Face(QString name, he::HalfEdge* halfEdge) : m_name(std::move(name)), m_halfEdge(halfEdge) {}

he::HalfEdge* he::Face::halfEdge() {
    return m_halfEdge;
}

void he::Face::setHalfEdge(he::HalfEdge* halfEdge) {
    m_halfEdge = halfEdge;
}

QString he::Face::name() const {
    return m_name;
}

void he::Face::setName(const QString& name) {
    m_name = name;
}