#include "structure.h"
#include <iostream>

frac::Structure::Structure(std::vector<Face> const& faces) : m_faces(faces) {}

void frac::Structure::addAdjacency(std::size_t indexFace1, std::size_t indexEdgeFace1, std::size_t indexFace2, std::size_t indexEdgeFace2) {
    if (m_faces[indexFace1][indexEdgeFace1] == m_faces[indexFace2][indexEdgeFace2]) {
        this->m_adj += "    init(Sub('" + std::to_string(indexFace1) + "') + Bord('" + std::to_string(indexEdgeFace1) + "') + Permut('0'), Sub('" + std::to_string(indexFace2) + "') + Bord('" + std::to_string(indexEdgeFace2) + "'))\n";
    } else {
        //TODO: throw exception, to be caught in window
        std::cout << "Error on adj constraint" << std::endl;
    }
}

frac::UniqueVector<frac::Edge> frac::Structure::allEdges() const {
    frac::UniqueVector<frac::Edge> res;
    frac::UniqueVector<frac::Face> faces = this->allFaces();
    for (frac::Face const& f: faces.data()) {
        for (frac::Edge const& e: f.data()) {
            res.add(e);
        }
    }
    return res;
}

frac::UniqueVector<frac::Face> frac::Structure::allFaces() const {
    frac::UniqueVector<frac::Face> res;
    for (frac::Face const& f: this->m_faces) {
        res.add(f);
    }
    for (frac::Face const& f: this->m_faces) {
        frac::UniqueVector<frac::Face> subdivisions = f.allSubdivisions();
        for (frac::Face const& sub: subdivisions.data()) {
            res.add(sub);
        }
    }
    return res;
}

std::size_t frac::Structure::nbControlPointsOfFace(std::size_t indexFace) const {
    std::size_t res { 0 };
    for (Edge const& e: this->m_faces[indexFace].data()) {
        res += e.edgeType() == EdgeType::BEZIER ? 3 : 2;
        res--;
    }
    return res;
}

namespace frac {
std::ostream& operator<<(std::ostream& os, frac::Structure const& structure) {
    for (frac::Face const& f: structure.m_faces) {
        os << f << std::endl;
    }
    os << structure.m_adj;
    return os;
}
}

frac::Face const& frac::Structure::operator[](std::size_t index) const {
    return m_faces[index];
}

std::string frac::Structure::adjacencies() const {
    return this->m_adj;
}

const std::vector<frac::Face>& frac::Structure::faces() const {
    return m_faces;
}
