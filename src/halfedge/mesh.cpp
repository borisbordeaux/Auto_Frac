#include "halfedge/mesh.h"

#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

poly::Mesh::Mesh() {
}

poly::Mesh::~Mesh() {
    reset();
}

QVector<poly::Vertex*> poly::Mesh::vertices() const {
    return m_vertices;
}

QVector<poly::HalfEdge*> poly::Mesh::halfEdges() const {
    return m_halfEdges;
}

QVector<poly::Face*> poly::Mesh::faces() const {
    return m_faces;
}

void poly::Mesh::append(Vertex* v) {
    m_vertices.append(v);
}

void poly::Mesh::append(HalfEdge* he) {
    //append a half-edge to the mesh
    m_halfEdges.append(he);
    //and to the map to enhance the finding
    m_map[he->name()] = m_halfEdges.size() - 1;
}

void poly::Mesh::append(Face* f) {
    m_faces.append(f);
}

[[maybe_unused]] void poly::Mesh::remove(Vertex* v) {
    qsizetype index = m_vertices.indexOf(v);

    if (index >= 0) {
        m_vertices.remove(index);
    }
}

[[maybe_unused]] void poly::Mesh::remove(HalfEdge* he) {
    qsizetype index = m_halfEdges.indexOf(he);

    if (index >= 0) {
        m_halfEdges.remove(index);
        m_map.remove(he->name());
    }
}

[[maybe_unused]] void poly::Mesh::remove(Face* f) {
    qsizetype index = m_faces.indexOf(f);

    if (index >= 0) {
        m_faces.remove(index);
    }
}

poly::HalfEdge* poly::Mesh::findByName(const QString& name) {
    HalfEdge* res = nullptr;

    if (m_map.contains(name)) {
        res = m_halfEdges.at(m_map[name]);
    }

    return res;
}

void poly::Mesh::reset() {
    //free each face
    for (Face* f: qAsConst(m_faces)) {
        if (f != nullptr) {
            delete f;
            f = nullptr;
        }
    }

    //clear the vector
    m_faces.clear();

    //free each vertex
    for (Vertex* v: qAsConst(m_vertices)) {
        if (v != nullptr) {
            delete v;
            v = nullptr;
        }
    }

    //clear the vector
    m_vertices.clear();

    //free each half-edge
    for (HalfEdge* he: qAsConst(m_halfEdges)) {
        if (he != nullptr) {
            delete he;
            he = nullptr;
        }
    }

    //clear the vector
    m_halfEdges.clear();
    //clear the map
    m_map.clear();
}

QString poly::Mesh::toString() const {
    QString res = "Faces :\n";
    for (poly::Face const* f: this->m_faces) {
        res += f->name() + ", ";
    }
    res += "\nHalfEdges :\n";
    for (poly::HalfEdge const* h: this->m_halfEdges) {
        res += h->name() + ", ";
    }
    res += "\nVertices :\n";
    for (poly::Vertex const* v: this->m_vertices) {
        res += v->name() + ", ";
    }
    return res;
}
