#include "fractal/volume.h"

#include <utility>
#include "fractal/algorithms/algorithmsurrounddelay.h"
#include "fractal/algorithms/algorithmsurrounddelayandbezier.h"
#include "fractal/algorithms/algorithmoncorners.h"

namespace frac {
Volume::Volume(std::vector<std::vector<frac::Edge>> edges, unsigned int delay, Edge const& adjEdge, Edge const& gapEdge, Edge const& reqEdge, AlgorithmSubdivision algo) :
        m_edges(std::move(edges)), m_delay(delay), m_adjEdge(adjEdge), m_gapEdge(gapEdge), m_reqEdge(reqEdge), m_algo(algo) {

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
    //To avoid refind the subdivisions, but not necessary at first
    /*if (s_subdivisions.find(m_name) != s_subdivisions.end()) {
        return s_subdivisions[m_name];
    }*/
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

bool Volume::operator==(Volume const& /*other*/) const {
    //TODO: use graph isomorphism
    return false;
}
} // frac