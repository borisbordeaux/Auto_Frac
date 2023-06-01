#ifndef EDGE_H
#define EDGE_H

#include <ostream>
#include <string>
#include <vector>

namespace frac {

enum class EdgeType {
    CANTOR, BEZIER
};

class Edge {
public:
    Edge(Edge const& other);
    Edge(EdgeType edgeType, unsigned int nbSubdivisions, unsigned int delay = 0);

    void decreaseDelay();
    [[nodiscard]] EdgeType edgeType() const;
    [[nodiscard]] unsigned int nbSubdivisions() const;
    [[nodiscard]] unsigned int delay() const;
    [[nodiscard]] std::vector<Edge> subdivisions() const;
    [[nodiscard]] bool isDelay() const;

    friend std::ostream& operator<<(std::ostream& os, const Edge& edge);
    bool operator==(Edge const& other) const;
    bool operator!=(Edge const& other) const;

    std::string toString() const;

private:
    EdgeType m_edgeType;
    unsigned int m_nbSubdivisions;
    unsigned int m_delay;
};

} // frac

#endif // EDGE_H


