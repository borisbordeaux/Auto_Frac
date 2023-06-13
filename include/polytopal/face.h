#ifndef AUTOFRAC_POLY_FACE_H
#define AUTOFRAC_POLY_FACE_H

#include <map>
#include <string>
#include <vector>
#include "edge.h"
#include "utils/uniquevector.h"

namespace he {
class Face;

class Mesh;
}

namespace poly {

class Face {
public:
    explicit Face(he::Face* f);
    std::string name() const;
    std::size_t len() const;

    [[nodiscard]] std::vector<poly::Face> subdivisions() const;
    [[nodiscard]] std::vector<poly::Edge> const& constData() const;
    [[nodiscard]] std::string toString() const;
    [[nodiscard]] he::Face* HEFace() const;
    [[nodiscard]] std::vector<he::HalfEdge*> halfEdges() const;

    poly::Edge const& operator[](std::size_t index) const;
    friend std::ostream& operator<<(std::ostream& os, const poly::Face& face);
    bool operator==(Face const& other) const;

    static std::map<std::string, std::string> s_incidenceConstraints;
    static std::map<std::string, std::string> s_adjacencyConstraints;
    static he::Mesh const* s_mesh;
    static void reset();

private:
    void init();
    static void addAdjacencyConstraint(poly::Face const& face, unsigned int indexSubFace1, unsigned int indexBordFace1, unsigned int indexSubFace2, unsigned int indexBordFace2);
    static void addIncidenceConstraint(poly::Face const& face, unsigned int indexParentEdge, unsigned int indexSubEdge, unsigned int indexSubFaceEdge, unsigned int indexSubFace);
    static frac::UniqueVector<poly::Face> s_existingFaces;

    he::Face* m_face;
    std::vector<he::HalfEdge*> m_halfEdges;
    std::vector<poly::Edge> m_edges;
    std::string m_name;
};

} // poly

#endif //AUTOFRAC_POLY_FACE_H
