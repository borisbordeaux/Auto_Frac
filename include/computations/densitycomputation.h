#ifndef AUTOFRAC_DENSITYCOMPUTATION_H
#define AUTOFRAC_DENSITYCOMPUTATION_H

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
    void canonizeMesh(he::Mesh &m);
}

} // frac

#endif //AUTOFRAC_DENSITYCOMPUTATION_H
