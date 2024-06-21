#ifndef AUTOFRAC_VOLUME_H
#define AUTOFRAC_VOLUME_H

#include "halfedge/mesh.h"
#include "edge.h"
#include "fractal/algorithms/algorithmsubdivision.h"
#include "utils/set.h"
#include "face.h"

namespace frac {

class Volume {
public:
    Volume() : Volume(std::vector<frac::Face> {}) {}
    explicit Volume(std::vector<frac::Face> faces, unsigned int delay = 0, const frac::Edge& adjEdge = { frac::EdgeType::CANTOR, 2 }, const frac::Edge& gapEdge = { frac::EdgeType::BEZIER, 2 }, const frac::Edge& reqEdge = { frac::EdgeType::BEZIER, 2 }, AlgorithmSubdivision algo = AlgorithmSubdivision::LinksSurroundDelayAndBezier);
    explicit Volume(he::Mesh const& mesh, unsigned int delay = 0, const frac::Edge& adjEdge = { frac::EdgeType::CANTOR, 2 }, const frac::Edge& gapEdge = { frac::EdgeType::BEZIER, 2 }, const frac::Edge& reqEdge = { frac::EdgeType::BEZIER, 2 }, AlgorithmSubdivision algo = AlgorithmSubdivision::LinksSurroundDelayAndBezier);

    std::vector<frac::Face> faces() const;

    frac::Edge adjEdge() const;
    frac::Edge gapEdge() const;
    frac::Edge reqEdge() const;
    unsigned int delay() const;
    frac::AlgorithmSubdivision algo() const;
    std::size_t offset() const;
    std::string name() const;
    std::size_t len() const;

    std::string toString() const;

    std::vector<frac::Volume> subdivisions() const;
    frac::Set<frac::Volume> allSubdivisions() const;

    he::Mesh toMesh() const;
    bool operator==(frac::Volume const& other) const;
    frac::Face const& operator[](std::size_t index) const;

    static std::map<std::string, std::string> s_incidenceConstraints;
    static std::map<std::string, std::string> s_adjacencyConstraints;
    static void reset();

private:
    std::vector<frac::Face> m_faces;
    unsigned int m_delay;
    frac::Edge m_adjEdge;
    frac::Edge m_gapEdge;
    frac::Edge m_reqEdge;
    frac::AlgorithmSubdivision m_algo;
    std::string m_name;

private:
    static frac::Set<frac::Volume> s_existingVolumes;
};

} // frac

#endif //AUTOFRAC_VOLUME_H
