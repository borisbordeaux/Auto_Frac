#ifndef AUTOFRAC_FRAC_STRUCTURE_H
#define AUTOFRAC_FRAC_STRUCTURE_H

#include <ostream>
#include <string>
#include <vector>

#include "fractal/face.h"
#include "utils/uniquevector.h"

namespace frac {

struct Adjacency {
    std::size_t Face1;
    std::size_t Edge1;
    std::size_t Face2;
    std::size_t Edge2;

    Adjacency(std::size_t face1, std::size_t edge1, std::size_t face2, std::size_t edge2) :
            Face1(face1), Edge1(edge1), Face2(face2), Edge2(edge2) {}

    bool equals(Adjacency const& other) const {
        return Face1 == other.Face1 && Edge1 == other.Edge1 && Face2 == other.Face2 && Edge2 == other.Edge2;
    }
};

class Structure {
public:
    explicit Structure(std::vector<frac::Face> const& faces);

    void addAdjacency(std::size_t indexFace1, std::size_t indexEdgeFace1, std::size_t indexFace2, std::size_t indexEdgeFace2);
    std::string strAdjacencies() const;
    std::vector<Adjacency> const& adjacencies() const;
    frac::UniqueVector<frac::Edge> allEdges() const;
    frac::UniqueVector<frac::Face> allFaces() const;

    std::vector<frac::Face> const& faces() const;

    std::size_t nbControlPointsOfFace(std::size_t indexFace) const;
    std::vector<std::size_t> controlPointIndices(std::size_t indexEdge, std::size_t indexFace, bool reverse = false) const;

    bool isInternControlPoint(std::size_t indexControlPoint, std::size_t indexFace) const;

    friend std::ostream& operator<<(std::ostream& os, const frac::Structure& structure);
    frac::Face const& operator[](std::size_t index) const;

private:
    std::vector<frac::Face> m_faces;
    std::string m_strAdjacency;
    std::vector<Adjacency> m_adjacencies;
};

} // frac

#endif //AUTOFRAC_FRAC_STRUCTURE_H
