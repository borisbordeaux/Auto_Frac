#include "polytopal/structure.h"
#include <iostream>

poly::Structure::Structure(he::Mesh const& mesh) : m_mesh(mesh) {}

std::string poly::Structure::toString() const {
    return this->m_mesh.toString().toStdString();
}

std::string poly::Structure::adjacencies() const {
    return this->m_adj;
}

frac::UniqueVector<poly::Edge> poly::Structure::allEdges() const {
    return frac::UniqueVector<poly::Edge>();
}

frac::UniqueVector<poly::Face> poly::Structure::allFaces() const {
    return frac::UniqueVector<poly::Face>();
}

std::vector<poly::Face> const& poly::Structure::faces() const {
    return this->m_faces;
}

std::size_t poly::Structure::nbControlPointsOfFace(std::size_t indexFace) const {
    return this->m_faces[indexFace].len();
}

namespace poly {
std::ostream& operator<<(std::ostream& os, poly::Structure const& structure) {
    for (poly::Face const& f: structure.m_faces) {
        os << f << std::endl;
    }
    os << structure.m_adj;
    return os;
}
}

poly::Face const& poly::Structure::operator[](std::size_t index) const {
    return m_faces[index];
}