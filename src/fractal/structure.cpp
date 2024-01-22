#include "fractal/structure.h"
#include <iostream>

frac::Structure::Structure(std::vector<Face> const& faces) : m_faces(faces) {}

void frac::Structure::addAdjacency(std::size_t indexFace1, std::size_t indexEdgeFace1, std::size_t indexFace2, std::size_t indexEdgeFace2) {
    if (m_faces[indexFace1][indexEdgeFace1] == m_faces[indexFace2][indexEdgeFace2]) {
        m_strAdjacency += "    init(Sub('" + std::to_string(indexFace1) + "') + Bord('" + std::to_string(indexEdgeFace1) + "') + Permut('0'), Sub('" + std::to_string(indexFace2) + "') + Bord('" + std::to_string(indexEdgeFace2) + "'))\n";
        m_adjacencies.emplace_back(indexFace1, indexEdgeFace1, indexFace2, indexEdgeFace2);
    }
}

frac::UniqueVector<frac::Edge> frac::Structure::allEdges() const {
    frac::UniqueVector<frac::Edge> res;
    frac::UniqueVector<frac::Face> faces = this->allFaces();
    for (frac::Face const& f: faces.data()) {
        for (frac::Edge const& e: f.constData()) {
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
    return m_faces[indexFace].nbControlPoints();
}

namespace frac {
std::ostream& operator<<(std::ostream& os, frac::Structure const& structure) {
    for (frac::Face const& f: structure.m_faces) {
        os << f << std::endl;
    }
    os << structure.m_strAdjacency;
    return os;
}
}

frac::Face const& frac::Structure::operator[](std::size_t index) const {
    return m_faces[index];
}

std::string frac::Structure::strAdjacencies() const {
    return this->m_strAdjacency;
}

const std::vector<frac::Face>& frac::Structure::faces() const {
    return m_faces;
}

std::vector<frac::Adjacency> const& frac::Structure::adjacencies() const {
    return m_adjacencies;
}

std::vector<std::size_t> frac::Structure::controlPointIndices(std::size_t indexEdge, std::size_t indexFace, bool reverse) const {
    std::vector<std::size_t> res = {};
    std::size_t current = 0;
    for (std::size_t i = 0; i < indexEdge; i++) {
        current += m_faces[indexFace][i].edgeType() == EdgeType::BEZIER ? 2 : 1;
    }
    res.emplace_back(current);
    res.emplace_back((current + 1) % this->nbControlPointsOfFace(indexFace));

    if (m_faces[indexFace][indexEdge].edgeType() == EdgeType::BEZIER) {
        res.emplace_back((current + 2) % this->nbControlPointsOfFace(indexFace));
    }

    if (reverse) {
        // max 3 control points, so reverse is trivial
        std::size_t temp = res[0];
        res[0] = res[res.size() - 1];
        res[res.size() - 1] = temp;
    }

    return res;
}
