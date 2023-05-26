#ifndef EDGE_H
#define EDGE_H

#include <string>
#include <ostream>
#include <vector>

namespace frac {

enum class EdgeType {
    CANTOR, BEZIER
};

class Edge {
public:
    Edge(Edge const &other);
    Edge(EdgeType edgeType, unsigned int nbSubdivisions, unsigned int delay = 0);

    EdgeType edgeType() const;
    unsigned int delay() const;
    unsigned int nbSubdivisions() const;

    bool isDelay() const;
    std::vector<Edge> subdivisions() const;

    friend std::ostream &operator<<(std::ostream &os, const Edge &edge);
    bool operator==(Edge const &other) const;
    bool operator!=(Edge const &other) const;

private:
    EdgeType m_edgeType;
    unsigned int m_nbSubdivisions;
    unsigned int m_delay;
};
}
#endif // EDGE_H


