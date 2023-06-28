#include "graph/vertex.h"

#include <utility>

graph::Vertex::Vertex(std::string name) : m_name(std::move(name)), m_centerX(0.0), m_centerY(0.0) {}

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
    return os << vertex.m_name;
}
}

void graph::Vertex::setCenter(double centerX, double centerY) {
    this->m_centerX = centerX;
    this->m_centerY = centerY;
}

double graph::Vertex::getX() const {
    return this->m_centerX;
}

double graph::Vertex::getY() const {
    return this->m_centerY;
}