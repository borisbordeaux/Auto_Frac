#include "graph/vertex.h"
#include "gui/vertexgraphicsitem.h"

#include <ostream>

graph::Vertex::Vertex(std::string name) : m_name(std::move(name)) {
    this->m_item = new VertexGraphicsItem();
    this->m_item->setVertex(this);
}

std::string const& graph::Vertex::getName() const {
    return this->m_name;
}

const std::vector<graph::Vertex*>& graph::Vertex::getParents() const {
    return this->m_parents;
}

const std::vector<graph::Vertex*>& graph::Vertex::getChildren() const {
    return this->m_children;
}

std::size_t graph::Vertex::getParentsSize() const {
    return this->m_parents.size();
}

std::size_t graph::Vertex::getChildrenSize() const {
    return this->m_children.size();
}

graph::Vertex* graph::Vertex::getParent(std::size_t index) const {
    return this->m_parents.at(index);
}

graph::Vertex* graph::Vertex::getChild(std::size_t index) const {
    return this->m_children.at(index);
}

void graph::Vertex::addParent(graph::Vertex* v) {
    this->m_parents.push_back(v);
}

void graph::Vertex::addChild(graph::Vertex* v) {
    this->m_children.push_back(v);
}

namespace graph {
std::ostream& operator<<(std::ostream& os, const graph::Vertex& vertex) {
    os << vertex.m_name << " - Parents : ";
    for (auto const& p: vertex.getParents()) {
        os << p->getName() << " - ";
    }
    os << "Children : ";
    for (auto const& p: vertex.getChildren()) {
        os << p->getName() << " - ";
    }
    return os;
}
}

void graph::Vertex::setCenter(int centerX, int centerY) {
    this->m_item->setCenter(centerX, centerY);
}

int graph::Vertex::getX() const {
    return this->m_item->getX();
}

int graph::Vertex::getY() const {
    return this->m_item->getY();
}

VertexGraphicsItem* graph::Vertex::graphicsItem() const {
    return this->m_item;
}