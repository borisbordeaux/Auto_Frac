#ifndef AUTOFRAC_STRUCTURE3D_H
#define AUTOFRAC_STRUCTURE3D_H

#include <vector>
#include "fractal/volume.h"
#include "fractal/face.h"
#include "fractal/edge.h"

namespace frac {

class Structure3D {
public:
    explicit Structure3D(std::vector<frac::Volume> const& volumes, bool bezierCubic);

    frac::Set<frac::Edge> allEdges() const;
    frac::Set<frac::Face> allFaces() const;
    frac::Set<frac::Volume> allVolumes() const;

    std::vector<frac::Volume> const& volumes() const;

    frac::Volume const& operator[](std::size_t index) const;

    bool isBezierCubic() const;

private:
    std::vector<frac::Volume> m_volumes;
    bool m_bezierCubic;
};

} // frac

#endif //AUTOFRAC_STRUCTURE3D_H
