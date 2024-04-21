#ifndef AUTOFRAC_POLYTOPAL_H
#define AUTOFRAC_POLYTOPAL_H

#include "polytopal/circle.h"

namespace he {
class Mesh;
}

namespace poly {
/**
 * Canonizes a mesh by checking all the following conditions<br>
 * - All edges of the mesh are tangent to the unit sphere.<br>
 * - The barycenter of the tangent points is at the origin of the unit sphere.<br>
 * - All faces are planar
 * @param m the mesh to canonize
 */
void canonicalizeMesh(he::Mesh& m);

/**
 * Centers the mesh around the origin
 * @param m the mesh to recenter
 */
void setMeshToOrigin(he::Mesh& m);

std::vector<poly::Circle> computeIlluminatedCircles(he::Mesh const& m);
std::vector<poly::Circle> computeIlluminatedCirclesDual(he::Mesh const& m);
std::size_t computeInversions(std::vector<poly::Circle>& circlesToInverse, std::vector<poly::Circle>& circlesInvertive, std::size_t index);

} // poly

#endif //AUTOFRAC_POLYTOPAL_H
