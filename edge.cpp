#include "edge.h"

Edge::Edge(EdgeType edgeType, int nbSubdivisions, unsigned int delay):
    m_edgeType(edgeType), m_nbSubdivisions(nbSubdivisions), m_delay(delay)
{

}

bool Edge::isDelay() const
{
    return this->m_delay > 0;
}
