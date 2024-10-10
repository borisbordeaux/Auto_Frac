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
 * @param steps the number of steps to do
 */
void canonicalizeMesh(he::Mesh& m, int steps, double d, bool recenterMesh);

std::vector<poly::Circle> computeIlluminatedCircles(he::Mesh const& m, QVector3D const& color);
std::vector<poly::Circle> computeIlluminatedCirclesDual(he::Mesh const& m, QVector3D const& color);
std::size_t computeInversions(std::vector<poly::Circle>& circlesToInverse, std::vector<poly::Circle>& circlesInvertive, std::size_t index);

} // poly

#endif //AUTOFRAC_POLYTOPAL_H
