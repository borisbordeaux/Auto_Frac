#include "edge.h"

frac::Edge::Edge(EdgeType edgeType, unsigned int nbSubdivisions, unsigned int delay) :
        m_edgeType(edgeType), m_nbSubdivisions(nbSubdivisions), m_delay(delay) {
}

frac::Edge::Edge(Edge const& other) :
        m_edgeType(other.m_edgeType), m_nbSubdivisions(other.m_nbSubdivisions), m_delay(other.m_delay) {
}

void frac::Edge::decreaseDelay() {
    if (this->isDelay())
        this->m_delay--;
}

frac::EdgeType frac::Edge::edgeType() const {
    return this->m_edgeType;
}

unsigned int frac::Edge::nbSubdivisions() const {
    return this->m_nbSubdivisions;
}

unsigned int frac::Edge::delay() const {
    return this->m_delay;
}

std::vector<frac::Edge> frac::Edge::subdivisions() const {
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

bool frac::Edge::isDelay() const {
    return this->m_delay > 0;
}

namespace frac {
std::ostream& operator<<(std::ostream& os, const frac::Edge& edge) {
    std::string edgeType = edge.edgeType() == frac::EdgeType::BEZIER ? "B" : "C";
    std::string nbSub = std::to_string(edge.nbSubdivisions());
    std::string delay = edge.isDelay() ? "_" + std::to_string(edge.delay()) : "";

    return os << edgeType << nbSub << delay;
}
}

bool frac::Edge::operator==(const Edge& other) const {
    return this->m_edgeType == other.m_edgeType && this->m_delay == other.m_delay && this->m_nbSubdivisions == other.m_nbSubdivisions;
}

bool frac::Edge::operator!=(const Edge& other) const {
    return !(*this == other);
}
