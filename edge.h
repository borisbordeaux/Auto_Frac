#ifndef EDGE_H
#define EDGE_H

enum class EdgeType
{
	CANTOR, BEZIER
};

class Edge
{
	public:
		Edge(EdgeType edgeType, int nbSubdivisions, unsigned int delay = 0);
        bool isDelay() const;


	private:
        EdgeType m_edgeType;
        int m_nbSubdivisions;
        unsigned int m_delay;
};

#endif // EDGE_H
