#include "face.h"

#include <utility>

frac::Face::Face(std::vector<Edge> edges, unsigned int delay, frac::Edge const& adjEdge, frac::Edge const& gapEdge, frac::Edge const& reqEdge) :
        m_data(std::move(edges)), m_delay(delay), m_adjEdge(adjEdge), m_gapEdge(gapEdge), m_reqEdge(reqEdge), m_nbSubdivisions(0), m_offset(0), m_firstInterior(-1) {
    for (Face const& f: s_existingFaces) {
        if (*this == f) {
            this->m_name = f.m_name;
            this->m_nbSubdivisions = f.m_nbSubdivisions;
            this->m_offset = f.m_offset;
        }
    }
    //if face doesn't exist
    if (this->m_name.empty()) {
        this->m_name = "Cell_" + std::to_string(s_existingFaces.size());
        if (this->m_delay == 0) {
            for (Edge const& e: this->m_data) {
                this->m_nbSubdivisions += e.nbSubdivisions();
            }
            this->m_nbSubdivisions -= this->len();
        } else {
            // one face if delayed, with subdivided boundaries
            // add delay info to name
            this->m_name += "_" + std::to_string(delay);
            this->m_nbSubdivisions = 1;
        }
        s_existingFaces.insert(*this);
    }
}

int frac::Face::firstInterior() const {
    return this->m_firstInterior;
}

int frac::Face::lastInterior() const {
    return this->m_firstInterior + 2;
}

std::size_t frac::Face::len() const {
    return this->m_data.size();
}

std::string frac::Face::name() const {
    return this->m_name;
}

int frac::Face::offset() const {
    return this->m_offset;
}

void frac::Face::setFirstInterior(int index) {
    this->m_firstInterior = index;
}

const frac::Edge& frac::Face::operator[](int index) const {
    return this->m_data[index];
}

bool frac::Face::operator==(frac::Face const& other) const {
    if (this->m_delay != other.m_delay || this->len() != other.len() || this->m_adjEdge != other.m_adjEdge || this->m_gapEdge != other.m_gapEdge || this->m_reqEdge != other.m_reqEdge)
        return false;

    std::vector<Edge> shifted;
    shifted.reserve(other.m_data.size());
    for (Edge const& e: other.m_data) {
        shifted.emplace_back(e);
    }
    for (int i = 0; i < other.len(); ++i) {
        if (this->m_data == shifted) {
            return true;
        }
        Edge first { shifted[0] };
        shifted.erase(std::begin(shifted));
        shifted.emplace_back(first);
    }
    return false;
}

namespace frac {
std::ostream& operator<<(std::ostream& os, frac::Face const& edge) {
    os << edge.m_name << " : [" << edge[0];
    for (int i = 1; i < edge.len(); ++i) {
        os << ", " << edge[i];
    }
    os << "], " << edge.m_nbSubdivisions << " subdivisions, interior is ";

    for (const Edge& e: Face::interior(edge.m_adjEdge, edge.m_gapEdge)) {
        os << e << " ";
    }

    return os;
}
}

void frac::Face::addAdjacencyConstraint(frac::Face const& face, frac::Face const& faceSub1, frac::Face const& faceSub2, unsigned int indexSubFace1, unsigned int indexBordFace1, unsigned int indexSubFace2, unsigned int indexBordFace2) {
    if (s_adjacencyConstraints.find(face.name()) != std::end(Face::s_adjacencyConstraints)) {
        s_adjacencyConstraints[face.name()] = "";
    }
    s_adjacencyConstraints[face.name()] += "    " + face.name() + "(Sub('" + std::to_string(indexSubFace1) + "') + Bord('" + std::to_string((indexBordFace1 - faceSub1.offset()) % faceSub1.len()) + "') + Permut('0'), Sub('" + std::to_string(indexSubFace2) + "') + Bord('" + std::to_string((indexBordFace2 - faceSub2.offset()) % faceSub2.len()) + "'))\n";
}

void frac::Face::addIncidenceConstraint(frac::Face const& face, frac::Face const& faceSub, unsigned int indexParentEdge, unsigned int indexSubEdge, unsigned int indexSubFaceEdge, unsigned int indexSubFace) {
    if (s_incidenceConstraints.find(face.name()) != std::end(Face::s_incidenceConstraints)) {
        s_incidenceConstraints[face.name()] = "";
    }
    s_incidenceConstraints[face.name()] += "    " + face.name() + "(Bord('" + std::to_string((indexParentEdge - face.offset()) % face.len()) + "') + Sub('" + std::to_string(indexSubEdge) + "'), Sub('" + std::to_string(indexSubFace) + "') + Bord('" + std::to_string((indexSubFaceEdge - faceSub.offset()) % faceSub.len()) + "'))\n";
}

int frac::Face::computeOffset(frac::Face const& face, frac::Face const& other) {
    if (face.m_delay != other.m_delay || face.len() != other.len() || face.m_adjEdge != other.m_adjEdge || face.m_gapEdge != other.m_gapEdge || face.m_reqEdge != other.m_reqEdge)
        return -1;
    std::vector<Edge> shifted;
    shifted.reserve(face.m_data.size());
    for (Edge const& e: face.m_data) {
        shifted.emplace_back(e);
    }
    for (int i = 0; i < other.len(); ++i) {
        if (face.m_data == shifted) {
            return i;
        }
        Edge first { shifted[0] };
        shifted.erase(std::begin(shifted));
        shifted.emplace_back(first);
    }
    return -1;
}

std::vector<frac::Edge> frac::Face::edgeIfRequired(frac::Edge const& edge, frac::Edge const& reqEdge) {
    return edge.edgeType() == EdgeType::CANTOR ? std::vector<Edge> { reqEdge } : std::vector<Edge>();
}

std::vector<frac::Edge> frac::Face::interior(frac::Edge const& adjacencyEdge, frac::Edge const& gapEdge) {
    return { adjacencyEdge, gapEdge, adjacencyEdge };
}
