#ifndef AUTOFRAC_COMPUTATION_H
#define AUTOFRAC_COMPUTATION_H

#include "polytopal/circle.h"

namespace he {
class Mesh;
}

class QString;

namespace frac {

namespace DensityComputation {
void computeDensity(QString const& file, int value, bool showAllImages);
};

namespace Canonizer {
/**
 * Canonizes a mesh by checking all the following conditions<br>
 * - All edges of the mesh are tangent to the unit sphere.<br>
 * - The barycenter of the tangent points is at the origin of the unit sphere.<br>
 * - All faces are planar
 * @param m the mesh to canonize
 */
void canonicalizeMesh(he::Mesh& m);

/**
 * Recenters the mesh around the origin
 * @param m the mesh to recenter
 */
void setMeshToOrigin(he::Mesh& m);
}

namespace PolyCircle {
std::vector<poly::Circle> computeIlluminatedCircles(he::Mesh const& m);
std::vector<poly::Circle> computeIlluminatedCirclesDual(he::Mesh const& m);
std::size_t computeInversions(std::vector<poly::Circle>& circlesToInverse, std::vector<poly::Circle>& circlesInvertive, std::size_t index);
}

} // frac

#endif //AUTOFRAC_COMPUTATION_H
