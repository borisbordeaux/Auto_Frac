#include "halfedge/face.h"

#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

poly::Face::Face(QString name, HalfEdge* halfEdge) : m_name(std::move(name)), m_halfEdge(halfEdge) {}

poly::HalfEdge* poly::Face::halfEdge() {
    return m_halfEdge;
}

void poly::Face::setHalfEdge(poly::HalfEdge* halfEdge) {
    m_halfEdge = halfEdge;
}

QString poly::Face::name() const {
    return m_name;
}

void poly::Face::setName(const QString& name) {
    m_name = name;
}