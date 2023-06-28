#ifndef AUTOFRAC_INCIDENCEGRAPH_H
#define AUTOFRAC_INCIDENCEGRAPH_H

#include <vector>
#include <string>

namespace graph {

class Vertex;

class IncidenceGraph {
public:
    IncidenceGraph() = default;
    ~IncidenceGraph();
    void addVertex(graph::Vertex* v);
    void addEdge(graph::Vertex* v);
    void addFace(graph::Vertex* v);
    void addVolume(graph::Vertex* v);
    [[nodiscard]] std::size_t getVerticesSize() const;
    [[nodiscard]] std::size_t getEdgesSize() const;
    [[nodiscard]] std::size_t getFacesSize() const;
    [[nodiscard]] std::size_t getVolumesSize() const;

    [[nodiscard]] std::vector<graph::Vertex*> const& getVertices() const;
    [[nodiscard]] std::vector<graph::Vertex*> const& getEdges() const;
    [[nodiscard]] std::vector<graph::Vertex*> const& getFaces() const;
    [[nodiscard]] std::vector<graph::Vertex*> const& getVolumes() const;

    [[nodiscard]] graph::Vertex* findVertexByName(std::string const& name) const;
    [[nodiscard]] graph::Vertex* findEdgeByName(std::string const& name) const;
    void reset();
    friend std::ostream& operator<<(std::ostream& os, const graph::IncidenceGraph& g);

    void updateVerticesPositions(double availableWidth);
private:
    std::vector<graph::Vertex*> m_vertices;
    std::vector<graph::Vertex*> m_edges;
    std::vector<graph::Vertex*> m_faces;
    std::vector<graph::Vertex*> m_volumes;
};

} // graph

#endif //AUTOFRAC_INCIDENCEGRAPH_H
