#ifndef AUTOFRAC_STRUCTURE_H
#define AUTOFRAC_STRUCTURE_H

#include "uniquevector.h"
#include "face.h"

namespace frac {

class Structure {
public:
    explicit Structure(std::vector<Face> const& faces);

    void addAdjacency(std::size_t indexFace1, std::size_t indexEdgeFace1, std::size_t indexFace2, std::size_t indexEdgeFace2);
    [[nodiscard]] std::string adjacencies() const;
    [[nodiscard]] UniqueVector<Edge> allEdges() const;
    [[nodiscard]] UniqueVector<Face> allFaces() const;

    const std::vector<Face>& faces() const;

    [[nodiscard]] std::size_t nbControlPointsOfFace(std::size_t indexFace) const;

    friend std::ostream& operator<<(std::ostream& os, const Structure& structure);
    Face const& operator[](std::size_t index) const;

private:
    std::vector<Face> m_faces;
    std::string m_adj;
};

} // frac

#endif //AUTOFRAC_STRUCTURE_H
