#include "fractal/volume.h"

#include <utility>
#include "fractal/algorithms/algorithmsurrounddelay.h"
#include "fractal/algorithms/algorithmsurrounddelayandbezier.h"
#include "fractal/algorithms/algorithmoncorners.h"

#include "halfedge/mesh.h"
#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/graphisomorphism.h"

namespace frac {

frac::Set<frac::Volume> frac::Volume::s_existingVolumes;
std::map<std::string, std::string> frac::Volume::s_incidenceConstraints;
std::map<std::string, std::string> frac::Volume::s_adjacencyConstraints;

Volume::Volume(std::vector<frac::Face> faces, unsigned int delay, Edge const& adjEdge, Edge const& gapEdge, Edge const& reqEdge, AlgorithmSubdivision algo) :
        m_faces(std::move(faces)), m_delay(delay), m_adjEdge(adjEdge), m_gapEdge(gapEdge), m_reqEdge(reqEdge), m_algo(algo) {
    for (Volume const& v: s_existingVolumes.data()) {
        if (*this == v) {
            m_name = v.m_name;
        }
    }
    //if volume doesn't exist
    if (m_name.empty()) {
        m_name = "Vol_" + std::to_string(s_existingVolumes.size());
        if (m_delay != 0) {
            // one face if delayed, with subdivided boundaries
            // add delay info to name
            m_name += "_" + std::to_string(delay);
        }
        s_existingVolumes.add(*this);
    }
}

Volume::Volume(he::Mesh const& mesh, unsigned int delay, const Edge& adjEdge, const Edge& gapEdge, const Edge& reqEdge, AlgorithmSubdivision algo) :
        m_faces({}), m_delay(delay), m_adjEdge(adjEdge), m_gapEdge(gapEdge), m_reqEdge(reqEdge), m_algo(algo) {

    //build faces from mesh
    for (he::Face* f: mesh.faces()) {
        std::vector<frac::Edge> edges;
        for (he::HalfEdge* he: f->allHalfEdges()) {
            edges.emplace_back(Edge::fromStr(he->name().toStdString()));
        }
        m_faces.emplace_back(edges, delay, adjEdge, gapEdge, reqEdge, algo);
    }

    for (Volume const& v: s_existingVolumes.data()) {
        if (*this == v) {
            m_name = v.m_name;
        }
    }
    //if volume doesn't exist
    if (m_name.empty()) {
        m_name = "Vol_" + std::to_string(s_existingVolumes.size());
        if (m_delay != 0) {
            // one face if delayed, with subdivided boundaries
            // add delay info to name
            m_name += "_" + std::to_string(delay);
        }
        s_existingVolumes.add(*this);
    }
}

frac::Edge Volume::adjEdge() const {
    return m_adjEdge;
}

frac::Edge Volume::gapEdge() const {
    return m_gapEdge;
}

frac::Edge Volume::reqEdge() const {
    return m_reqEdge;
}

unsigned int Volume::delay() const {
    return m_delay;
}

frac::AlgorithmSubdivision Volume::algo() const {
    return m_algo;
}

std::vector<frac::Volume> Volume::subdivisions() const {
    switch (m_algo) {
        case frac::AlgorithmSubdivision::LinksSurroundDelay:
            return frac::LinksSurroundDelay::subdivide(*this);
        case frac::AlgorithmSubdivision::LinksSurroundDelayAndBezier:
            return frac::LinksSurroundDelayAndBezier::subdivide(*this);
        case frac::AlgorithmSubdivision::LinksOnCorners:
            return frac::LinksOnCorners::subdivide(*this);
        default:
            return {};
    }
}

frac::Set<frac::Volume> Volume::allSubdivisions() const {
    frac::Set<frac::Volume> res;
    res.add(*this);
    std::size_t i = 0;
    bool changed = true;
    while (changed) {
        frac::Set<frac::Volume> added;
        for (std::size_t j = i; j < res.size(); ++j) {
            std::vector<frac::Volume> subs = res[j].subdivisions();
            for (frac::Volume const& v: subs) {
                added.add(v);
            }
        }
        std::size_t lastSize = res.size();
        for (frac::Volume const& v: added.data()) {
            res.add(v);
        }
        changed = res.size() != lastSize;
        i = lastSize;
    }
    return res;
}

bool Volume::operator==(Volume const& other) const {
    return he::GraphComparator::areIsomorph(this->toMesh(), other.toMesh(), true);
}

std::size_t Volume::offset() const {
    return 0;
}

std::vector<frac::Face> Volume::faces() const {
    return m_faces;
}

std::string Volume::name() const {
    return m_name;
}

std::string Volume::toString() const {
    //TODO: return representation of this volume
    return m_name;
}

void Volume::reset() {
    Volume::s_incidenceConstraints.clear();
    Volume::s_adjacencyConstraints.clear();
    Volume::s_existingVolumes.clear();
}

std::size_t Volume::len() const {
    return m_faces.size();
}

frac::Face const& Volume::operator[](std::size_t index) const {
    return m_faces[index];
}

he::Mesh Volume::toMesh() const {
    he::Mesh mesh;
    //TODO: create mesh from the faces, need adjacency or order in faces
    return mesh;
}
} // frac