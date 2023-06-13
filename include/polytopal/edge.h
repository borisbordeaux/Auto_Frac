#ifndef AUTOFRAC_POLY_EDGE_H
#define AUTOFRAC_POLY_EDGE_H

#include "fractal/edge.h"
#include "halfedge/vertex.h"
#include <string>

namespace poly {

class Edge {
public:
    explicit Edge(he::Vertex* vertex, frac::Edge const& edge);
    [[nodiscard]] std::string name() const;
    [[nodiscard]] std::size_t nbSubs() const;
    [[nodiscard]] he::Vertex* HEVertex() const;
    bool operator==(Edge const& other) const;
private:
    frac::Edge m_edge;
    he::Vertex* m_vertex;
};

} // poly

#endif //AUTOFRAC_POLY_EDGE_H
