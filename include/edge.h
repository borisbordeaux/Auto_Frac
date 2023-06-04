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
    Edge& operator=(const Edge& other) = default;

    void decreaseDelay();
    [[nodiscard]] EdgeType edgeType() const;
    [[nodiscard]] unsigned int nbSubdivisions() const;
    [[nodiscard]] unsigned int nbActualSubdivisions() const;
    [[nodiscard]] unsigned int delay() const;
    [[nodiscard]] std::vector<Edge> subdivisions(Edge const& reqEdge) const;
    [[nodiscard]] bool isDelay() const;
    [[nodiscard]] std::string name() const;
    void setEdgeType(EdgeType edgeType);
    void setNbSubdivisions(unsigned int nbSubdivisions);
    void setDelay(unsigned int delay);

    friend std::ostream& operator<<(std::ostream& os, Edge const& edge);
    bool operator==(Edge const& other) const;
    bool operator!=(Edge const& other) const;

    [[nodiscard]] std::string toString() const;

private:
    EdgeType m_edgeType;
    unsigned int m_nbSubdivisions;
    unsigned int m_delay;
};

} // frac

#endif // EDGE_H


