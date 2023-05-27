#ifndef AUTOFRAC_FACE_H
#define AUTOFRAC_FACE_H

#include <vector>
#include <map>
#include <set>
#include <functional>
#include "edge.h"

namespace frac {

class Face {
public:
    explicit Face(std::vector<Edge> edges, unsigned int delay = 0, const Edge& adjEdge = { EdgeType::CANTOR, 2 }, const Edge& gapEdge = { EdgeType::BEZIER, 2 }, const Edge& reqEdge = { EdgeType::BEZIER, 2 });

    [[nodiscard]] int firstInterior() const;
    [[nodiscard]] int lastInterior() const;
    [[nodiscard]] std::size_t len() const;
    [[nodiscard]] std::string name() const;
    [[nodiscard]] int offset() const;
    void setFirstInterior(int index);

    Edge const& operator[](int index) const;
    bool operator==(Face const& other) const;
    friend std::ostream& operator<<(std::ostream& os, const Face& edge);

private:
    std::vector<Edge> m_data;
    unsigned int m_delay;
    Edge m_adjEdge;
    Edge m_gapEdge;
    Edge m_reqEdge;
    std::string m_name;
    unsigned int m_nbSubdivisions;
    int m_offset;
    int m_firstInterior;

    inline static std::set<Face, std::equal_to<>> s_existingFaces;
    inline static std::map<std::string, std::string> s_incidenceConstraints;
    inline static std::map<std::string, std::string> s_adjacencyConstraints;

    static void addAdjacencyConstraint(Face const& face, Face const& faceSub1, Face const& faceSub2, unsigned int indexSubFace1, unsigned int indexBordFace1, unsigned int indexSubFace2, unsigned int indexBordFace2);
    static void addIncidenceConstraint(Face const& face, Face const& faceSub, unsigned int indexParentEdge, unsigned int indexSubEdge, unsigned int indexSubFaceEdge, unsigned int indexSubFace);

    static int computeOffset(Face const& face, Face const& other);
    static std::vector<Edge> edgeIfRequired(const Edge& edge, const Edge& reqEdge);
    static std::vector<Edge> interior(Edge const& adjacencyEdge, Edge const& gapEdge);
};

} // frac

#endif //AUTOFRAC_FACE_H
