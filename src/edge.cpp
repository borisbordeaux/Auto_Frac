#include "edge.h"

namespace frac {
Edge::Edge(EdgeType edgeType, unsigned int nbSubdivisions, unsigned int delay) :
        m_edgeType(edgeType), m_nbSubdivisions(nbSubdivisions), m_delay(delay) {
}

Edge::Edge(Edge const &other) :
        m_edgeType(other.m_edgeType), m_nbSubdivisions(other.m_nbSubdivisions), m_delay(other.m_delay) {
}

bool Edge::isDelay() const {
    return this->m_delay > 0;
}

bool Edge::operator==(const Edge &other) const {
    return this->m_edgeType == other.m_edgeType && this->m_delay == other.m_delay && this->m_nbSubdivisions == other.m_nbSubdivisions;
}

bool Edge::operator!=(const Edge &other) const {
    return !(*this == other);
}

std::ostream &operator<<(std::ostream &os, const Edge &edge) {
    std::string edgeType = edge.edgeType() == EdgeType::BEZIER ? "B" : "C";
    std::string nbSub = std::to_string(edge.nbSubdivisions());
    std::string delay = edge.isDelay() ? "_" + std::to_string(edge.delay()) : "";

    return os << edgeType << nbSub << delay;
}

unsigned int Edge::nbSubdivisions() const {
    return this->m_nbSubdivisions;
}

unsigned int Edge::delay() const {
    return this->m_delay;
}

EdgeType Edge::edgeType() const {
    return this->m_edgeType;
}

std::vector<Edge> Edge::subdivisions() const {
    std::vector<Edge> result;
    if (this->isDelay()) {
        result.emplace_back(this->edgeType(), this->nbSubdivisions(), this->delay() - 1);
    } else {
        if (this->edgeType() == EdgeType::CANTOR) {
            for (int i = 0; i < this->nbSubdivisions() - 1; ++i) {
                result.emplace_back(EdgeType::CANTOR, this->nbSubdivisions());
                result.emplace_back(EdgeType::BEZIER, 2);
                result.emplace_back(EdgeType::BEZIER, 2);
            }
            result.emplace_back(EdgeType::CANTOR, this->nbSubdivisions());
        }
        if (this->edgeType() == EdgeType::BEZIER) {
            for (int i = 0; i < this->nbSubdivisions() - 1; ++i) {
                result.emplace_back(EdgeType::BEZIER, this->nbSubdivisions());
            }
        }
    }
    return result;
}
}
