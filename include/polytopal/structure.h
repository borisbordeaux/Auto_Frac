#ifndef AUTOFRAC_POLY_STRUCTURE_H
#define AUTOFRAC_POLY_STRUCTURE_H

#include "face.h"
#include "halfedge/mesh.h"
#include "utils/uniquevector.h"

namespace poly {

class Structure {
public:
    explicit Structure(he::Mesh const& mesh, he::Face* face = nullptr);
    [[nodiscard]] std::string toString() const;

    void addAdjacency(std::size_t indexFace1, std::size_t indexEdgeFace1, std::size_t indexFace2, std::size_t indexEdgeFace2);
    [[nodiscard]] std::string adjacencies() const;
    [[nodiscard]] frac::UniqueVector<poly::Edge> allEdges() const;
    [[nodiscard]] frac::UniqueVector<poly::Face> allFaces() const;

    [[nodiscard]] std::vector<poly::Face> faces() const;

    [[nodiscard]] std::size_t nbControlPointsOfFace(std::size_t indexFace) const;

    friend std::ostream& operator<<(std::ostream& os, const poly::Structure& structure);
    poly::Face const& operator[](std::size_t index) const;

private:
    he::Mesh const& m_mesh;
    std::vector<poly::Face> m_faces;
    std::string m_adj;
    he::Face* m_selectedFace;
};

} // poly

#endif //AUTOFRAC_POLY_STRUCTURE_H
