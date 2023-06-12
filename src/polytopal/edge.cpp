#include "polytopal/edge.h"

poly::Edge::Edge(he::Vertex* vertex, frac::Edge const& mEdge) : m_edge(mEdge), m_vertex(vertex) {}

std::string poly::Edge::name() const {
    return this->m_edge.name();
}

std::size_t poly::Edge::nbSubs() const {
    return this->m_vertex->degree()-1;
}
