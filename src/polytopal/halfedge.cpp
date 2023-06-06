#include "polytopal/halfedge.h"

#include <utility>

#include "polytopal/face.h"
#include "polytopal/vertex.h"

poly::HalfEdge::HalfEdge(poly::Vertex* origin, QString name) :
        m_origin(origin), m_face(nullptr),
        m_twin(nullptr), m_prev(nullptr),
        m_next(nullptr), m_name(std::move(name)) {

}

poly::Vertex* poly::HalfEdge::origin() {
    return m_origin;
}

void poly::HalfEdge::setOrigin(poly::Vertex* origin) {
    m_origin = origin;
}

poly::Face* poly::HalfEdge::face() {
    return m_face;
}

void poly::HalfEdge::setFace(Face* face) {
    m_face = face;
}

poly::HalfEdge* poly::HalfEdge::twin() {
    return m_twin;
}

void poly::HalfEdge::setTwin(poly::HalfEdge* twin) {
    m_twin = twin;
}

poly::HalfEdge* poly::HalfEdge::prev() {
    return m_prev;
}

void poly::HalfEdge::setPrev(HalfEdge* prev) {
    m_prev = prev;
}

poly::HalfEdge* poly::HalfEdge::next() {
    return m_next;
}

void poly::HalfEdge::setNext(poly::HalfEdge* next) {
    m_next = next;
}

QString poly::HalfEdge::name() const {
    return m_name;
}

void poly::HalfEdge::setName(QString const& name) {
    m_name = name;
}
