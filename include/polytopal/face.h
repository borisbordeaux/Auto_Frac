#ifndef AUTOFRAC_POLY_FACE_H
#define AUTOFRAC_POLY_FACE_H

#include <map>
#include <string>
#include <vector>
#include "edge.h"

namespace he {
class Face;
}

namespace poly {

class Face {
public:
    explicit Face(he::Face* f, std::string name);
    std::string name() const;
    std::size_t len() const;

    [[nodiscard]] std::vector<poly::Face> subdivisions() const;
    [[nodiscard]] std::vector<poly::Edge> const& constData() const;
    [[nodiscard]] std::string toString() const;

    friend std::ostream& operator<<(std::ostream& os, const poly::Face& face);

    static std::map<std::string, std::string> s_incidenceConstraints;
    static std::map<std::string, std::string> s_adjacencyConstraints;

private:
    he::Face* m_face;
    std::vector<poly::Edge> m_edges;
    std::string m_name;
};

} // poly

#endif //AUTOFRAC_POLY_FACE_H
