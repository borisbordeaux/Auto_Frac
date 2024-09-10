#include "halfedge/vertex.h"

#include <utility>
#include "halfedge/halfedge.h"
#include "halfedge/face.h"
#include "utils/utils.h"


he::Vertex::Vertex(float x, float y, float z, QString name) :
        m_pos(x, y, z), m_posD(static_cast<qreal>(x), static_cast<qreal>(y), static_cast<qreal>(z)), m_halfEdge(nullptr), m_name(std::move(name)) {}

he::Vertex::Vertex(QVector3D const& pos, QString name) : Vertex(pos.x(), pos.y(), pos.z(), std::move(name)) {}

QVector3D he::Vertex::pos() const {
    return m_pos;
}

void he::Vertex::setPos(QVector3D const& pos) {
    m_pos = pos;
}

he::Point3D he::Vertex::posD() const {
    return m_posD;
}

void he::Vertex::setPosD(he::Point3D const& posD) {
    m_posD = posD;
}

he::HalfEdge* he::Vertex::halfEdge() {
    return m_halfEdge;
}

void he::Vertex::setHalfEdge(he::HalfEdge* halfEdge) {
    if (m_halfEdge == nullptr) {
        m_halfEdge = halfEdge;
    } else {
        this->addHalfEdge(m_halfEdge);
        m_halfEdge = halfEdge;
    }
}

QString he::Vertex::name() const {
    return m_name;
}

std::size_t he::Vertex::degree() const {
    return m_otherHalfEdges.size() + 1;
}

std::vector<he::Face*> he::Vertex::getAllFacesAroundVertex(he::Face* f) const {
    std::vector<he::Face*> facesAroundVertex;

    //fill all faces around vertex
    he::HalfEdge* h = this->m_halfEdge;
    he::HalfEdge* nxt = h;
    do {
        facesAroundVertex.push_back(nxt->face());
        nxt = nxt->twin()->next();
    } while (nxt != h);

    if (f == nullptr) {
        return facesAroundVertex;
    }

    //order faces around vertex to have the given face in last
    std::vector<he::Face*> orderedFacesAroundVertex = facesAroundVertex;

    //if given face is in the list of all faces around this vertex
    if (std::find(facesAroundVertex.begin(), facesAroundVertex.end(), f) != facesAroundVertex.end()) {
        while (orderedFacesAroundVertex[orderedFacesAroundVertex.size() - 1] != f) {
            orderedFacesAroundVertex = frac::utils::shiftVector(orderedFacesAroundVertex);
        }
    }

    return orderedFacesAroundVertex;
}

void he::Vertex::addHalfEdge(he::HalfEdge* halfEdge) {
    m_otherHalfEdges.append(halfEdge);
}

QVector<he::HalfEdge*>& he::Vertex::otherHalfEdges() {
    return m_otherHalfEdges;
}

QString he::Vertex::toString() const {
    QString res;
    res += m_name + ": HalfEdge: " + (m_halfEdge ? m_halfEdge->name() : "nullprt");
    res += " Position: (" + QString::number(m_pos.x()) + "," + QString::number(m_pos.y()) + "," + QString::number(m_pos.z()) + ")" + " User data: " + m_userData;
    res += "other halfedges: ";
    for (he::HalfEdge* e: m_otherHalfEdges) {
        res += e->name() + ", ";
    }
    return res;
}

QString he::Vertex::userData() const {
    return m_userData;
}

void he::Vertex::setUserData(QString const& data) {
    m_userData = data;
}
