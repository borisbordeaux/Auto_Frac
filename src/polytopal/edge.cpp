#include "polytopal/edge.h"

poly::Edge::Edge(he::Vertex* vertex, frac::Edge const& edge) : m_edge(edge), m_vertex(vertex) {}

std::string poly::Edge::name() const {
    return this->m_edge.name();
}

std::size_t poly::Edge::nbSubs() const {
    return this->m_edge.nbSubdivisions();
}

bool poly::Edge::operator==(const poly::Edge& other) const {
    return other.m_edge == this->m_edge;
}

he::Vertex* poly::Edge::HEVertex() const {
    return this->m_vertex;
}

std::string poly::Edge::toString() const {
    return this->name() + " associated HE vertex : " + this->m_vertex->name().toStdString();
}
