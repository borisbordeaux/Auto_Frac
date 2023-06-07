#ifndef AUTOFRAC_POLY_STRUCTURE_H
#define AUTOFRAC_POLY_STRUCTURE_H

#include "halfedge/mesh.h"

namespace poly {

class Structure {
public:
    explicit Structure(he::Mesh const& mesh);
    std::string toString() const;

private:
    he::Mesh m_mesh;
};

} // poly

#endif //AUTOFRAC_POLY_STRUCTURE_H
