#include <set>
#include "halfedge/mesh.h"

#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

he::Mesh::~Mesh() {
    reset();
}

std::vector<he::Vertex*> const& he::Mesh::vertices() const {
    return m_vertices;
}

std::vector<he::HalfEdge*> const& he::Mesh::halfEdges() const {
    return m_halfEdges;
}

std::vector<he::HalfEdge*> const& he::Mesh::halfEdgesNoTwin() const {
    return m_halfEdgesNotTwin;
}

std::vector<he::Face*> const& he::Mesh::faces() const {
    return m_faces;
}

void he::Mesh::append(he::Vertex* v) {
    m_vertices.push_back(v);
}

void he::Mesh::append(he::HalfEdge* he, bool completeNotTwin) {
    //append a half-edge to the mesh
    m_halfEdges.push_back(he);
    if (completeNotTwin) {
        m_halfEdgesNotTwin.push_back(he);
    }
}

void he::Mesh::append(Face* f) {
    m_faces.push_back(f);
}

he::HalfEdge* he::Mesh::findByName(QString const& name, bool useOtherHalfEdgesOfVertices) {
    he::HalfEdge* res = nullptr;
    if (useOtherHalfEdgesOfVertices) {
        int i = name.split(" ")[0].toInt() - 1;
        he::Vertex* v = m_vertices[i];
        if (v->halfEdge() != nullptr && v->halfEdge()->name() == name) {
            res = v->halfEdge();
        } else {
            for (he::HalfEdge* he: v->otherHalfEdges()) {
                if (he->name() == name) {
                    res = he;
                }
            }
        }
    } else {
        auto it = std::find_if(m_halfEdges.begin(), m_halfEdges.end(), [name](he::HalfEdge* he) { return he->name() == name; });
        if (it != m_halfEdges.end()) {
            return *it;
        }
    }
    return res;
}

void he::Mesh::reset() {
    //free each face
    for (he::Face* f: m_faces) {
        if (f != nullptr) {
            delete f;
            f = nullptr;
        }
    }

    //clear the vector
    m_faces.clear();

    //free each vertex
    for (he::Vertex* v: m_vertices) {
        if (v != nullptr) {
            delete v;
            v = nullptr;
        }
    }

    //clear the vector
    m_vertices.clear();

    //free each half-edge
    for (he::HalfEdge* he: m_halfEdges) {
        if (he != nullptr) {
            delete he;
            he = nullptr;
        }
    }

    //clear the vector
    m_halfEdges.clear();

    m_halfEdgesNotTwin.clear();
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

    res += "\n---------------------------------------------\nFaces :\n";
    for (he::Face const* f: this->m_faces) {
        res += f->toString() + "\n";
    }
    res += "\n---------------------------------------------\nHalfEdges :\n";
    for (he::HalfEdge const* h: this->m_halfEdges) {
        res += h->toString() + "\n";
    }
    res += "\n---------------------------------------------\nVertices :\n";
    for (he::Vertex const* v: this->m_vertices) {
        res += v->toString() + "\n";
    }
    return res;
}

std::optional<std::size_t> he::Mesh::indexOf(he::Vertex* v) const {
    for (std::size_t i = 0; i < m_vertices.size(); i++) {
        if (m_vertices[i] == v) {
            return i;
        }
    }
    return {};
}

void he::Mesh::updateFloatPosFromDoublePos() {
    for (he::Vertex* v: m_vertices) {
        v->setPos(v->posD().toQVector3D());
    }
}

void he::Mesh::updateDoublePosFromFloatPos() {
    for (he::Vertex* v: m_vertices) {
        v->setPosD({ static_cast<double>(v->pos().x()), static_cast<double>(v->pos().y()), static_cast<double>(v->pos().z()) });
    }
}

void he::Mesh::updateHalfEdgeNotTwin() {
    std::set<he::HalfEdge*> addedHalfEdge;
    m_halfEdgesNotTwin.clear();
    for (he::HalfEdge* he: m_halfEdges) {
        if (addedHalfEdge.find(he) == addedHalfEdge.end()) {
            m_halfEdgesNotTwin.push_back(he);
            addedHalfEdge.insert(he->twin());
        }
    }
}
