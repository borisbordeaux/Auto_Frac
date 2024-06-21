#ifndef AUTOFRAC_VOLUME_H
#define AUTOFRAC_VOLUME_H

#include "halfedge/mesh.h"
#include "edge.h"
#include "fractal/algorithms/algorithmsubdivision.h"
#include "utils/set.h"

namespace frac {

class Volume {
public:
    Volume() : Volume(std::vector<std::vector<frac::Edge>> {}) {}

    explicit Volume(std::vector<std::vector<frac::Edge>> edges, unsigned int delay = 0, const frac::Edge& adjEdge = { frac::EdgeType::CANTOR, 2 }, const frac::Edge& gapEdge = { frac::EdgeType::BEZIER, 2 }, const frac::Edge& reqEdge = { frac::EdgeType::BEZIER, 2 }, AlgorithmSubdivision algo = AlgorithmSubdivision::LinksSurroundDelayAndBezier);

    [[nodiscard]] frac::Edge adjEdge() const;
    [[nodiscard]] frac::Edge gapEdge() const;
    [[nodiscard]] frac::Edge reqEdge() const;
    [[nodiscard]] unsigned int delay() const;
    [[nodiscard]] frac::AlgorithmSubdivision algo() const;

    [[nodiscard]] std::vector<frac::Volume> subdivisions() const;
    [[nodiscard]] frac::Set<frac::Volume> allSubdivisions() const;

    bool operator==(frac::Volume const& other) const;

private:
    std::vector<std::vector<frac::Edge>> m_edges;
    unsigned int m_delay;
    frac::Edge m_adjEdge;
    frac::Edge m_gapEdge;
    frac::Edge m_reqEdge;
    frac::AlgorithmSubdivision m_algo;
};

} // frac

#endif //AUTOFRAC_VOLUME_H
