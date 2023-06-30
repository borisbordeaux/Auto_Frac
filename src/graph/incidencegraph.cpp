#include "graph/incidencegraph.h"
#include "graph/vertex.h"
#include "utils/utils.h"
#include <ostream>

graph::IncidenceGraph::~IncidenceGraph() {
    reset();
}

void graph::IncidenceGraph::addVertex(graph::Vertex* v) {
    this->m_vertices.push_back(v);
}

void graph::IncidenceGraph::addEdge(graph::Vertex* v) {
    this->m_edges.push_back(v);
}

void graph::IncidenceGraph::addFace(graph::Vertex* v) {
    this->m_faces.push_back(v);
}

void graph::IncidenceGraph::addVolume(graph::Vertex* v) {
    this->m_volumes.push_back(v);
}

std::size_t graph::IncidenceGraph::getVerticesSize() const {
    return this->m_vertices.size();
}

std::size_t graph::IncidenceGraph::getEdgesSize() const {
    return this->m_edges.size();
}

std::size_t graph::IncidenceGraph::getFacesSize() const {
    return this->m_faces.size();
}

std::size_t graph::IncidenceGraph::getVolumesSize() const {
    return this->m_volumes.size();
}

std::vector<graph::Vertex*> const& graph::IncidenceGraph::getVertices() const {
    return this->m_vertices;
}

std::vector<graph::Vertex*> const& graph::IncidenceGraph::getEdges() const {
    return this->m_edges;
}

std::vector<graph::Vertex*> const& graph::IncidenceGraph::getFaces() const {
    return this->m_faces;
}

std::vector<graph::Vertex*> const& graph::IncidenceGraph::getVolumes() const {
    return this->m_volumes;
}

graph::Vertex* graph::IncidenceGraph::findVertexByName(std::string const& name) const {
    for (auto* v: this->m_vertices) {
        if (v->getName() == name) {
            return v;
        }
    }
    return nullptr;
}

graph::Vertex* graph::IncidenceGraph::findEdgeByName(std::string const& name) const {
    for (auto* v: this->m_edges) {
        if (v->getName() == name) {
            return v;
        }
        //compare also with reverse name
        std::string first = frac::utils::split(name, ' ')[0];
        std::string last = frac::utils::split(name, ' ')[1];

        std::string mfirst = frac::utils::split(v->getName(), ' ')[0];
        std::string mlast = frac::utils::split(v->getName(), ' ')[1];

        if (first == mlast && last == mfirst) {
            return v;
        }
    }
    return nullptr;
}

void graph::IncidenceGraph::reset() {
    for (auto* v: this->m_vertices) {
        delete v;
    }
    for (auto* e: this->m_edges) {
        delete e;
    }
    for (auto* f: this->m_faces) {
        delete f;
    }
    for (auto* v: this->m_volumes) {
        delete v;
    }
    this->m_vertices.clear();
    this->m_edges.clear();
    this->m_faces.clear();
    this->m_volumes.clear();
}

namespace graph {
std::ostream& operator<<(std::ostream& os, const graph::IncidenceGraph& g) {
    os << "Vertices :" << std::endl;
    for (auto* v: g.getVertices()) {
        os << *v << std::endl;
    }
    os << std::endl << "Edges :" << std::endl;
    for (auto* e: g.getEdges()) {
        os << *e << std::endl;
    }
    os << std::endl << "Faces :" << std::endl;
    for (auto* f: g.getFaces()) {
        os << *f << std::endl;
    }
    os << std::endl << "Volumes :" << std::endl;
    for (auto* v: g.getVolumes()) {
        os << *v << std::endl;
    }
    return os;
}
}

void graph::IncidenceGraph::updateVerticesPositions(int availableWidth) {
    for (std::size_t i = 0; i < this->m_vertices.size(); ++i) {
        int s = availableWidth / (static_cast<int>(this->m_vertices.size()) + 1);
        int x = (static_cast<int>(i) + 1) * s;
        int y = 800.;
        this->m_vertices[i]->setCenter(x, y);
    }
    for (std::size_t i = 0; i < this->m_edges.size(); ++i) {
        int s = availableWidth / (static_cast<int>(this->m_edges.size()) + 1);
        int x = (static_cast<int>(i) + 1) * s;
        int y = 550.;
        this->m_edges[i]->setCenter(x, y);
    }
    for (std::size_t i = 0; i < this->m_faces.size(); ++i) {
        int s = availableWidth / (static_cast<int>(this->m_faces.size()) + 1);
        int x = (static_cast<int>(i) + 1) * s;
        int y = 300.;
        this->m_faces[i]->setCenter(x, y);
    }
    for (std::size_t i = 0; i < this->m_volumes.size(); ++i) {
        int s = availableWidth / (static_cast<int>(this->m_volumes.size()) + 1);
        int x = (static_cast<int>(i) + 1) * s;
        int y = 50.;
        this->m_volumes[i]->setCenter(x, y);
    }
}

void graph::IncidenceGraph::sortVertices() {
    //sort vertices of graph (by construction, only graph vertices that represents an edge need to be sorted
    IncidenceGraph::sortByName(this->m_edges);

    //sort parents of vertices
    for(graph::Vertex *v : this->m_vertices){
        IncidenceGraph::sortByName(v->getParents());
    }

    //sort parent and children of edges
    for(graph::Vertex *v : this->m_edges){
        IncidenceGraph::sortByName(v->getParents());
        IncidenceGraph::sortByName(v->getChildren());
    }

    //sort parent and children of faces
    for(graph::Vertex *v : this->m_faces){
        IncidenceGraph::sortByName(v->getParents());
        IncidenceGraph::sortByName(v->getChildren());
    }

    //sort children of volumes
    for(graph::Vertex *v : this->m_volumes){
        IncidenceGraph::sortByName(v->getParents());
        IncidenceGraph::sortByName(v->getChildren());
    }
}

void graph::IncidenceGraph::sortByName(std::vector<graph::Vertex*>& v) {
    std::sort(v.begin(), v.end(), [&](graph::Vertex* v1, graph::Vertex* v2) -> bool {
        return v1->getName().compare(v2->getName()) < 0;
    });
}