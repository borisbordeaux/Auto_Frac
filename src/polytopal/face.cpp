#include "polytopal/face.h"

#include <utility>
#include "halfedge/face.h"

std::map<std::string, std::string> poly::Face::s_incidenceConstraints;
std::map<std::string, std::string> poly::Face::s_adjacencyConstraints;

poly::Face::Face(he::Face* f, std::string name) : m_face(f), m_name(std::move(name)) {}

std::string poly::Face::name() const {
    return this->m_name;
}

std::size_t poly::Face::len() const {
    return this->m_face->nbEdges();
}

std::vector<poly::Face> poly::Face::subdivisions() const {
    return std::vector<poly::Face>();
}

std::vector<poly::Edge> const& poly::Face::constData() const {
    return this->m_edges;
}

std::string poly::Face::toString() const {
    return this->name();
}

namespace poly {
std::ostream& operator<<(std::ostream& os, poly::Face const& face) {
    return os << face.toString();
}
}