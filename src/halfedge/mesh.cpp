#include "halfedge/mesh.h"

#include <set>
#include <iostream>
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
    for (he::Face* f: m_faces) {
        delete f;
    }
    for (he::Vertex* v: m_vertices) {
        delete v;
    }
    for (he::HalfEdge* he: m_halfEdges) {
        delete he;
    }
    m_faces.clear();
    m_vertices.clear();
    m_halfEdges.clear();
    m_halfEdgesNotTwin.clear();
}

QString he::Mesh::toString() const {
    QString res = "Faces :\n";
    for (he::Face const* f: m_faces) {
        res += f->name() + ", ";
    }
    res += "\nHalfEdges :\n";
    for (he::HalfEdge const* h: m_halfEdges) {
        res += h->name() + ", ";
    }
    res += "\nVertices :\n";
    for (he::Vertex const* v: m_vertices) {
        res += v->name() + ", ";
    }

    res += "\n---------------------------------------------\nFaces :\n";
    for (he::Face const* f: m_faces) {
        res += f->toString() + "\n";
    }
    res += "\n---------------------------------------------\nHalfEdges :\n";
    for (he::HalfEdge const* h: m_halfEdges) {
        res += h->toString() + "\n";
    }
    res += "\n---------------------------------------------\nVertices :\n";
    for (he::Vertex const* v: m_vertices) {
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

void he::Mesh::updateOtherHalfEdges() {
    for (he::Vertex* v: m_vertices) {
        v->setHalfEdge(nullptr);
        v->clearOtherHalfEdges();
    }
    for (he::HalfEdge* he: m_halfEdges) {
        he->origin()->setHalfEdge(he);
    }
}

he::Vertex* he::Mesh::cutHalfEdge(he::HalfEdge* he) {
    //current data we need
    he::HalfEdge* twin = he->twin();
    he::Vertex* vertexLeft = twin->origin();
    he::Vertex* vertexRight = he->origin();
    he::HalfEdge* nextNextTwin = twin->next();
    he::HalfEdge* prevPrevHe = he->prev();

    he::Vertex* newVertex = new he::Vertex((vertexLeft->pos() + vertexRight->pos()) / 2.0f, QString::number(m_vertices.size() + 1));
    this->append(newVertex);

    he::HalfEdge* prevHe = new he::HalfEdge(vertexRight, vertexRight->name() + " " + newVertex->name());
    he::HalfEdge* nextTwin = new he::HalfEdge(newVertex, newVertex->name() + " " + vertexRight->name());
    this->append(prevHe);
    this->append(nextTwin);

    //for vertices
    vertexRight->setHalfEdge(prevHe);
    newVertex->setHalfEdge(he);

    //for halfedges: origin, name, face, twin, prev, next
    he->setOrigin(newVertex);
    he->setName(newVertex->name() + " " + vertexLeft->name());
    twin->setName(vertexLeft->name() + " " + newVertex->name());
    prevHe->setFace(he->face());
    nextTwin->setFace(twin->face());
    prevHe->setTwin(nextTwin);
    nextTwin->setTwin(prevHe);
    he->setPrev(prevHe);
    prevHe->setPrev(prevPrevHe);
    nextTwin->setPrev(twin);
    nextNextTwin->setPrev(nextTwin);
    twin->setNext(nextTwin);
    prevHe->setNext(he);
    nextTwin->setNext(nextNextTwin);
    prevPrevHe->setNext(prevHe);

    return newVertex;
}

he::HalfEdge* he::Mesh::cutFace(he::Face* face, he::Vertex* v1, he::Vertex* v2) {
    // ensure v1 and v2 are different vertices of the face and are not consecutive
    if (v1 == v2) { return nullptr; }
    std::vector<he::HalfEdge*> halfedges = face->allHalfEdges();
    he::HalfEdge* heFromV1 = nullptr;
    he::HalfEdge* heFromV2 = nullptr;
    for (he::HalfEdge* he: halfedges) {
        if (he->origin() == v1) {
            heFromV1 = he;
        }
        if (he->origin() == v2) {
            heFromV2 = he;
        }
    }
    if (heFromV1 == nullptr || heFromV2 == nullptr) { return nullptr; }
    if (heFromV1->next()->origin() == v2) { return nullptr; }
    if (heFromV2->next()->origin() == v1) { return nullptr; }

    he::HalfEdge* he1 = new he::HalfEdge(v1, v1->name() + " " + v2->name());
    he::HalfEdge* he2 = new he::HalfEdge(v2, v2->name() + " " + v1->name());
    he::Face* newFace = new he::Face(QString::number(m_faces.size()));
    newFace->setHalfEdge(he2);
    face->setHalfEdge(he1);
    this->append(he1);
    this->append(he2);
    this->append(newFace);

    he::HalfEdge* heFromV1Prev = heFromV1->prev();
    he::HalfEdge* heFromV2Prev = heFromV2->prev();

    //for halfedges: face, twin, prev, next
    he1->setFace(face);
    he2->setFace(newFace);
    heFromV2Prev->setFace(newFace);
    heFromV1->setFace(newFace);
    he1->setTwin(he2);
    he2->setTwin(he1);
    he1->setPrev(heFromV1Prev);
    he2->setPrev(heFromV2Prev);
    heFromV1->setPrev(he2);
    heFromV2->setPrev(he1);
    he1->setNext(heFromV2);
    he2->setNext(heFromV1);
    heFromV1Prev->setNext(he1);
    heFromV2Prev->setNext(he2);

    return he1;
}

void he::Mesh::remove(he::Face* f) {
    auto it = std::find(m_faces.begin(), m_faces.end(), f);
    if (it == m_faces.end()) { return; }
    for (he::HalfEdge* he: f->allHalfEdges()) {
        he->setFace(nullptr);
    }
    m_faces.erase(it);
    delete f;
}

void he::Mesh::remove(he::HalfEdge* he) {
    auto itHe = std::find(m_halfEdges.begin(), m_halfEdges.end(), he);
    if (itHe == m_halfEdges.end()) { return; }
    m_halfEdges.erase(itHe);
    auto itTwin = std::find(m_halfEdges.begin(), m_halfEdges.end(), he->twin());
    if (itTwin == m_halfEdges.end()) { return; }
    m_halfEdges.erase(itTwin);

    he::HalfEdge* twin = he->twin();
    he::HalfEdge* twinPrev = twin->prev();
    he::HalfEdge* twinNext = twin->next();
    he::HalfEdge* hePrev = he->prev();
    he::HalfEdge* heNext = he->next();

    he::Face* f1 = he->face();
    he::Face* f2 = twin->face();

    //remove faces
    this->remove(f1);
    this->remove(f2);

    //update prev and next
    twinPrev->setNext(heNext);
    hePrev->setNext(twinNext);
    heNext->setPrev(twinPrev);
    twinNext->setPrev(hePrev);

    delete he;
    delete twin;

    this->updateHalfEdgeNotTwin();
    this->updateOtherHalfEdges();
}

void he::Mesh::remove(he::Vertex* v) {
    auto it = std::find(m_vertices.begin(), m_vertices.end(), v);
    if (it == m_vertices.end()) { return; }
    m_vertices.erase(it);
    QVector<he::HalfEdge*> halfedges = v->otherHalfEdges();
    halfedges.push_back(v->halfEdge());

    for (he::HalfEdge* he: halfedges) {
        this->remove(he);
    }

    delete v;
}
