#ifndef AUTOFRAC_POLY_STRUCTURE_H
#define AUTOFRAC_POLY_STRUCTURE_H

#include "halfedge/mesh.h"
#include "face.h"
#include "utils/uniquevector.h"

namespace poly {

class Structure {
public:
    explicit Structure(he::Mesh const& mesh);
    std::string toString() const;

    [[nodiscard]] std::string adjacencies() const;
    [[nodiscard]] frac::UniqueVector<poly::Edge> allEdges() const;
    [[nodiscard]] frac::UniqueVector<poly::Face> allFaces() const;

    [[nodiscard]] std::vector<poly::Face> const& faces() const;

    [[nodiscard]] std::size_t nbControlPointsOfFace(std::size_t indexFace) const;

    friend std::ostream& operator<<(std::ostream& os, const poly::Structure& structure);
    poly::Face const& operator[](std::size_t index) const;

private:
    he::Mesh const& m_mesh;
    std::vector<poly::Face> m_faces;
    std::string m_adj;
};

} // poly

#endif //AUTOFRAC_POLY_STRUCTURE_H
