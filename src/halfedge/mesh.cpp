#include "halfedge/mesh.h"

#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

he::Mesh::Mesh() {
}

he::Mesh::~Mesh() {
    reset();
}

std::vector<he::Vertex*> he::Mesh::vertices() const {
    return m_vertices;
}

std::vector<he::HalfEdge*> he::Mesh::halfEdges() const {
    return m_halfEdges;
}

std::vector<he::Face*> he::Mesh::faces() const {
    return m_faces;
}

void he::Mesh::append(he::Vertex* v) {
    m_vertices.push_back(v);
}

void he::Mesh::append(he::HalfEdge* he) {
    //append a half-edge to the mesh
    m_halfEdges.push_back(he);
    //and to the map to enhance the finding
    m_map[he->name()] = m_halfEdges.size() - 1;
}

void he::Mesh::append(Face* f) {
    m_faces.push_back(f);
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

std::vector<he::Face*> he::Mesh::adjacenciesOf(he::Face* f) const {
    std::vector<he::Face*> res;
    he::HalfEdge* he = f->halfEdge();
    he::HalfEdge* nxt = he;
    do {
        if (nxt->twin() != nullptr) {
            if (nxt->twin()->face() != nullptr) {
                res.push_back(nxt->twin()->face());
            }
        }
        nxt = nxt->next();
    } while (nxt != he);

    return res;
}
