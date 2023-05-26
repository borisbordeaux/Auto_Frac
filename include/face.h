#ifndef AUTOFRAC_FACE_H
#define AUTOFRAC_FACE_H

#include <vector>
#include <map>
#include <set>
#include "edge.h"


namespace frac {

class Face {
public:
    explicit Face(std::set<Edge> edges, unsigned int delay = 0, Edge adjEdge = {EdgeType::CANTOR, 2}, Edge gapEdge = {EdgeType::BEZIER, 2}, Edge reqEdge = {EdgeType::BEZIER, 2});

    std::size_t len() const;

    void setFirstInterior(int index);
    int firstInterior() const;
    int lastInterior() const;

    Edge const& operator[](int index) const;
    bool operator==(Face const& other) const;

private:
    std::set<Edge> m_data;
    int m_firstInterior;
    std::string m_name;
    unsigned int m_nbSubdivisions;
    int m_offset;
    unsigned int m_delay;
    Edge m_adjEdge;
    Edge m_gapEdge;
    Edge m_reqEdge;

    static std::set<Face> existingFaces;
    static std::map<std::string, std::string> incidenceConstraints;
    static std::map<std::string, std::string> adjacencyConstraints;
};

} // frac

#endif //AUTOFRAC_FACE_H
