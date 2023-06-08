#include "halfedge/mesh.h"

#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

he::Mesh::Mesh() {
}

he::Mesh::~Mesh() {
    reset();
}

QVector<he::Vertex*> he::Mesh::vertices() const {
    return m_vertices;
}

QVector<he::HalfEdge*> he::Mesh::halfEdges() const {
    return m_halfEdges;
}

QVector<he::Face*> he::Mesh::faces() const {
    return m_faces;
}

void he::Mesh::append(he::Vertex* v) {
    m_vertices.append(v);
}

void he::Mesh::append(he::HalfEdge* he) {
    //append a half-edge to the mesh
    m_halfEdges.append(he);
    //and to the map to enhance the finding
    m_map[he->name()] = m_halfEdges.size() - 1;
}

void he::Mesh::append(Face* f) {
    m_faces.append(f);
}

[[maybe_unused]] void he::Mesh::remove(he::Vertex* v) {
    qsizetype index = m_vertices.indexOf(v);

    if (index >= 0) {
        m_vertices.remove(index);
    }
}

[[maybe_unused]] void he::Mesh::remove(he::HalfEdge* he) {
    qsizetype index = m_halfEdges.indexOf(he);

    if (index >= 0) {
        m_halfEdges.remove(index);
        m_map.remove(he->name());
    }
}

[[maybe_unused]] void he::Mesh::remove(he::Face* f) {
    qsizetype index = m_faces.indexOf(f);

    if (index >= 0) {
        m_faces.remove(index);
    }
}

he::HalfEdge* he::Mesh::findByName(const QString& name) {
    he::HalfEdge* res = nullptr;

    if (m_map.contains(name)) {
        res = m_halfEdges.at(m_map[name]);
    }

    return res;
}

void he::Mesh::reset() {
    //free each face
    for (he::Face* f: qAsConst(m_faces)) {
        if (f != nullptr) {
            delete f;
            f = nullptr;
        }
    }

    //clear the vector
    m_faces.clear();

    //free each vertex
    for (he::Vertex* v: qAsConst(m_vertices)) {
        if (v != nullptr) {
            delete v;
            v = nullptr;
        }
    }

    //clear the vector
    m_vertices.clear();

    //free each half-edge
    for (he::HalfEdge* he: qAsConst(m_halfEdges)) {
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

QString he::Mesh::toString() const {
    QString res = "Faces :\n";
    for (he::Face const* f: this->m_faces) {
        res += f->name() + ", ";
    }
    res += "\nHalfEdges :\n";
    for (he::HalfEdge const* h: this->m_halfEdges) {
        res += h->name() + ", ";
    }
    res += "\nVertices :\n";
    for (he::Vertex const* v: this->m_vertices) {
        res += v->name() + ", ";
    }
    return res;
}

QVector<he::Face*> he::Mesh::adjacenciesOf(he::Face* f) const {
    QVector<he::Face*> res;
    he::HalfEdge* he = f->halfEdge();
    he::HalfEdge* nxt = he;
    do {
        if (nxt->twin() != nullptr) {
            if (nxt->twin()->face() != nullptr) {
                res.append(nxt->twin()->face());
            }
        }
        nxt = nxt->next();
    } while (nxt != he);

    return res;
}

std::size_t he::Mesh::degreeOf(he::Vertex* v) const {
    std::size_t res { 1 };
    he::HalfEdge* he = v->halfEdge();
    he::HalfEdge* twin_next = he->twin()->next();
    do {
        res++;
        twin_next = twin_next->twin()->next();
    } while (he != twin_next);
    return res;
}
