#ifndef AUTOFRAC_STRUCTURE_H
#define AUTOFRAC_STRUCTURE_H

#include <ostream>
#include <string>
#include <vector>

#include "fractal/face.h"
#include "utils/uniquevector.h"

namespace frac {

class Structure {
public:
    explicit Structure(std::vector<frac::Face> const& faces);

    void addAdjacency(std::size_t indexFace1, std::size_t indexEdgeFace1, std::size_t indexFace2, std::size_t indexEdgeFace2);
    [[nodiscard]] std::string adjacencies() const;
    [[nodiscard]] frac::UniqueVector<frac::Edge> allEdges() const;
    [[nodiscard]] frac::UniqueVector<frac::Face> allFaces() const;

    [[nodiscard]] std::vector<frac::Face> const& faces() const;

    [[nodiscard]] std::size_t nbControlPointsOfFace(std::size_t indexFace) const;

    friend std::ostream& operator<<(std::ostream& os, const frac::Structure& structure);
    frac::Face const& operator[](std::size_t index) const;

private:
    std::vector<frac::Face> m_faces;
    std::string m_adj;
};

} // frac

#endif //AUTOFRAC_STRUCTURE_H
