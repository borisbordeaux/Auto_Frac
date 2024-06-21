#include "fractal/structure3d.h"

namespace frac {
Structure3D::Structure3D(const std::vector<frac::Volume>& volumes, bool bezierCubic) : m_volumes(volumes), m_bezierCubic(bezierCubic) {}

frac::Set<frac::Edge> Structure3D::allEdges() const {
    frac::Set<frac::Edge> res;
    frac::Set<frac::Face> faces = this->allFaces();
    for (frac::Face const& f: faces.data()) {
        for (frac::Edge const& e: f.constData()) {
            res.add(e);
        }
    }
    return res;
}

frac::Set<frac::Face> Structure3D::allFaces() const {
    frac::Set<frac::Face> res;
    frac::Set<frac::Volume> volumes = this->allVolumes();
    for (frac::Volume const& v: volumes) {
        for (frac::Face const& f: v.faces()) {
            res.add(f);
        }
    }
    return res;
}

frac::Set<frac::Volume> Structure3D::allVolumes() const {
    frac::Set<frac::Volume> res;
    for (frac::Volume const& v: this->m_volumes) {
        res.add(v);
    }
    for (frac::Volume const& v: this->m_volumes) {
        frac::Set<frac::Volume> subdivisions = v.allSubdivisions();
        for (frac::Volume const& sub: subdivisions.data()) {
            res.add(sub);
        }
    }
    return res;
}

std::vector<frac::Volume> const& Structure3D::volumes() const {
    return m_volumes;
}

frac::Volume const& Structure3D::operator[](std::size_t index) const {
    return m_volumes[index];
}

bool Structure3D::isBezierCubic() const {
    return m_bezierCubic;
}
} // frac