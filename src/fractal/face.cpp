#include "fractal/face.h"
#include "utils/utils.h"

#include <iostream>

frac::UniqueVector<frac::Face> frac::Face::s_existingFaces;
std::map<std::string, std::string> frac::Face::s_incidenceConstraints;
std::map<std::string, std::string> frac::Face::s_adjacencyConstraints;
std::unordered_map<std::string, std::vector<frac::Face>> frac::Face::s_subdivisions;

frac::AlgorithmSubdivision frac::Face::s_algorithm = frac::AlgorithmSubdivision::LinksSurroundDelayAndBezier;

frac::Face::Face(std::vector<Edge> edges, unsigned int delay, frac::Edge const& adjEdge, frac::Edge const& gapEdge, frac::Edge const& reqEdge) :
        m_data(std::move(edges)), m_delay(delay), m_adjEdge(adjEdge), m_gapEdge(gapEdge), m_reqEdge(reqEdge), m_offset(0), m_firstInterior(-1) {
    for (Face const& f: s_existingFaces.data()) {
        if (*this == f) {
            this->m_name = f.m_name;
            this->m_offset = computeOffset(f, *this);
        }
    }
    //if face doesn't exist
    if (this->m_name.empty()) {
        this->m_name = "Cell_" + std::to_string(s_existingFaces.size());
        if (this->m_delay != 0) {
            // one face if delayed, with subdivided boundaries
            // add delay info to name
            this->m_name += "_" + std::to_string(delay);
        }
        s_existingFaces.add(*this);
    }
}

std::vector<frac::Edge> const& frac::Face::constData() const {
    return this->m_data;
}

std::vector<frac::Edge>& frac::Face::data() {
    return this->m_data;
}


int frac::Face::firstInterior() const {
    return this->m_firstInterior;
}

int frac::Face::lastInterior() const {
    return this->m_firstInterior + 2;
}

std::size_t frac::Face::len() const {
    return this->m_data.size();
}

std::string frac::Face::name() const {
    return this->m_name;
}

int frac::Face::offset() const {
    return this->m_offset;
}

void frac::Face::setFirstInterior(int index) {
    this->m_firstInterior = index;
}

std::vector<frac::Face> frac::Face::subdivisions() const {
    if (s_subdivisions.find(m_name) != s_subdivisions.end()) {
        return s_subdivisions[m_name];
    }
    switch (s_algorithm) {
        case AlgorithmSubdivision::LinksSurroundDelay:
            return this->subdivisionsSurroundDelay();
        case AlgorithmSubdivision::LinksSurroundDelayAndBezier:
            return this->subdivisionsSurroundDelayAndBezier();
    }
    return {};
}

const frac::Edge& frac::Face::operator[](std::size_t index) const {
    return this->m_data.at(index);
}

bool frac::Face::operator==(frac::Face const& other) const {
    if (this->m_delay != other.m_delay || this->len() != other.len() || this->m_adjEdge != other.m_adjEdge || this->m_gapEdge != other.m_gapEdge || this->m_reqEdge != other.m_reqEdge) {
        return false;
    }

    std::vector<frac::Edge> shifted { other.m_data };

    for (std::size_t i = 0; i < this->len(); ++i) {
        if (this->m_data == shifted) {
            return true;
        }
        std::vector<frac::Edge> new_shifted { frac::utils::shiftVector(shifted) };
        shifted.clear();
        for (Edge const& e: new_shifted) {
            shifted.emplace_back(e);
        }
    }
    return false;
}

namespace frac {
std::ostream& operator<<(std::ostream& os, frac::Face const& face) {
    return os << face.toString();
}
}

void frac::Face::addAdjacencyConstraint(frac::Face const& face, frac::Face const& faceSub1, frac::Face const& faceSub2, unsigned int indexSubFace1, unsigned int indexBordFace1, unsigned int indexSubFace2, unsigned int indexBordFace2) {
    if (s_adjacencyConstraints.find(face.name()) == std::end(Face::s_adjacencyConstraints)) {
        s_adjacencyConstraints[face.name()] = "";
    }
    int s1 = static_cast<int>(indexSubFace1);
    int b1 = frac::utils::mod(static_cast<int>(indexBordFace1) - faceSub1.offset(), static_cast<int>(faceSub1.len()));
    int s2 = static_cast<int>(indexSubFace2);
    int b2 = frac::utils::mod(static_cast<int>(indexBordFace2) - faceSub2.offset(), static_cast<int>(faceSub2.len()));
    s_adjacencyConstraints[face.name()] += "    " + face.name() + "(Sub('" + std::to_string(s1) + "') + Bord('" + std::to_string(b1) + "') + Permut('0'), Sub('" + std::to_string(s2) + "') + Bord('" + std::to_string(b2) + "'))\n";
}

void frac::Face::addIncidenceConstraint(frac::Face const& face, frac::Face const& faceSub, unsigned int indexParentEdge, unsigned int indexSubEdge, unsigned int indexSubFaceEdge, unsigned int indexSubFace) {
    if (s_incidenceConstraints.find(face.name()) == std::end(Face::s_incidenceConstraints)) {
        s_incidenceConstraints[face.name()] = "";
    }
    int b1 = frac::utils::mod(static_cast<int>(indexParentEdge) - face.offset(), static_cast<int>(face.len()));
    int s1 = static_cast<int>(indexSubEdge);
    int s2 = static_cast<int>(indexSubFace);
    int b2 = frac::utils::mod(static_cast<int>(indexSubFaceEdge) - faceSub.offset(), static_cast<int>(faceSub.len()));
    s_incidenceConstraints[face.name()] += "    " + face.name() + "(Bord('" + std::to_string(b1) + "') + Sub('" + std::to_string(s1) + "'), Sub('" + std::to_string(s2) + "') + Bord('" + std::to_string(b2) + "'))\n";
}

int frac::Face::computeOffset(frac::Face const& face, frac::Face const& other) {
    if (face.m_delay != other.m_delay || face.len() != other.len() || face.m_adjEdge != other.m_adjEdge || face.m_gapEdge != other.m_gapEdge || face.m_reqEdge != other.m_reqEdge) {
        return -1;
    }
    std::vector<Edge> shifted { other.m_data };
    for (std::size_t i = 0; i < other.len(); ++i) {
        if (face.m_data == shifted) {
            return static_cast<int>(i);
        }
        std::vector<frac::Edge> new_shifted { frac::utils::shiftVector(shifted) };
        shifted.clear();
        for (Edge const& e: new_shifted) {
            shifted.emplace_back(e);
        }
    }
    return -1;
}

std::optional<frac::Edge> frac::Face::edgeIfRequired(frac::Edge const& edge, frac::Edge const& reqEdge) {
    if (edge.edgeType() == EdgeType::CANTOR) {
        return reqEdge;
    } else {
        return {};
    }
}

frac::UniqueVector<frac::Face> frac::Face::allSubdivisions() const {
    frac::UniqueVector<frac::Face> res;
    res.add(*this);
    std::size_t i = 0;
    bool changed = true;
    while (changed) {
        frac::UniqueVector<frac::Face> added;
        for (std::size_t j = i; j < res.size(); ++j) {
            std::vector<frac::Face> subs = res[j].subdivisions();
            for (frac::Face const& f: subs) {
                added.add(f);
            }
        }
        std::size_t lastSize = res.size();
        for (frac::Face const& f: added.data()) {
            res.add(f);
        }
        changed = res.size() != lastSize;
        i = lastSize;
    }
    return res;
}

std::string frac::Face::toString() const {
    std::string res = (*this)[0].toString();
    for (std::size_t i = 1; i < this->len(); ++i) {
        res += " - " + (*this)[i].toString();
    }
    res += " / ";

    res += this->m_adjEdge.toString() + " - ";
    res += this->m_gapEdge.toString() + " - ";
    res += this->m_reqEdge.toString() + " / ";
    res += std::to_string(this->m_delay);
    return res;
}


frac::Edge frac::Face::adjEdge() const {
    return this->m_adjEdge;
}

frac::Edge frac::Face::gapEdge() const {
    return this->m_gapEdge;
}

frac::Edge frac::Face::reqEdge() const {
    return this->m_reqEdge;
}

void frac::Face::reset() {
    Face::s_incidenceConstraints.clear();
    Face::s_adjacencyConstraints.clear();
    Face::s_existingFaces.clear();
    Face::s_subdivisions.clear();
}

void frac::Face::setAdjEdge(frac::Edge const& edge) {
    this->m_adjEdge = edge;
}

void frac::Face::setGapEdge(frac::Edge const& edge) {
    this->m_gapEdge = edge;
}

void frac::Face::setReqEdge(frac::Edge const& edge) {
    this->m_reqEdge = edge;
}

void frac::Face::setDelay(unsigned int delay) {
    this->m_delay = delay;
}

unsigned int frac::Face::delay() const {
    return this->m_delay;
}

std::vector<frac::Face> frac::Face::subdivisionsSurroundDelay() const {
    std::vector<frac::Face> res;
    bool writeConstraints = s_incidenceConstraints.find(this->name()) == s_incidenceConstraints.end();
    if (m_delay == 0) {
        //if face has no delay
        for (std::size_t i = 0; i < this->len(); ++i) {
            // foreach edge
            frac::Edge current = (*this)[i];
            if (current.isDelay()) {
                // current edge has a delay so creation of one face
                frac::Edge subFirst { current };
                subFirst.decreaseDelay();
                std::vector<frac::Edge> boundaries = { subFirst };
                boundaries.push_back(this->m_adjEdge);
                boundaries.push_back(this->m_gapEdge);
                boundaries.push_back(this->m_adjEdge);
                frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                c.setFirstInterior(1);
                if (writeConstraints) {
                    addIncidenceConstraint(*this, c, i, 0, 0, res.size());
                }
                res.push_back(c);
            } else {
                // current edge has not a delay, so we look at the edge before
                std::size_t idx = static_cast<std::size_t>(utils::mod(static_cast<int>(i) - 1, static_cast<int>(this->len())));
                if ((*this)[idx].isDelay()) {
                    // the edge before has a delay
                    std::vector<frac::Edge> boundaries = { current };
                    std::optional<frac::Edge> requiredEdge = edgeIfRequired(current, this->m_reqEdge);
                    if (requiredEdge.has_value()) {
                        boundaries.push_back(requiredEdge.value());
                    }
                    boundaries.push_back(this->m_adjEdge);
                    boundaries.push_back(this->m_gapEdge);
                    boundaries.push_back(this->m_adjEdge);
                    frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                    c.setFirstInterior(static_cast<int>(boundaries.size() - 3));
                    if (writeConstraints) {
                        addIncidenceConstraint(*this, c, i, 0, 0, res.size());
                    }
                    res.push_back(c);
                }

                //creation of intermediate states
                int nbIntermediateStates { static_cast<int>(current.nbSubdivisions()) - 2 };
                for (int j = 0; j < nbIntermediateStates; j++) {
                    std::vector<frac::Edge> boundaries = { current };
                    std::optional<frac::Edge> requiredEdge = edgeIfRequired(current, this->m_reqEdge);
                    if (requiredEdge.has_value()) {
                        boundaries.push_back(requiredEdge.value());
                    }
                    int indexFirstInterior { static_cast<int>(boundaries.size()) };
                    boundaries.push_back(this->m_adjEdge);
                    boundaries.push_back(this->m_gapEdge);
                    boundaries.push_back(this->m_adjEdge);
                    if (requiredEdge.has_value()) {
                        boundaries.push_back(requiredEdge.value());
                    }
                    frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                    c.setFirstInterior(indexFirstInterior);
                    if (writeConstraints) {
                        addIncidenceConstraint(*this, c, i, j + 1, 0, res.size());
                    }
                    res.push_back(c);
                }

                // creation of last state of the edge
                frac::Edge next = (*this)[utils::mod(i + 1, this->len())];
                if (next.isDelay()) {
                    // if next edge has delay
                    std::vector<frac::Edge> boundaries = { current };
                    boundaries.push_back(this->m_adjEdge);
                    boundaries.push_back(this->m_gapEdge);
                    boundaries.push_back(this->m_adjEdge);
                    std::optional<frac::Edge> requiredEdge = edgeIfRequired(current, this->m_reqEdge);
                    if (requiredEdge.has_value()) {
                        boundaries.push_back(requiredEdge.value());
                    }
                    frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                    c.setFirstInterior(1);
                    if (writeConstraints) {
                        addIncidenceConstraint(*this, c, i, nbIntermediateStates + 1, 0, res.size());
                    }
                    res.push_back(c);
                } else {
                    // if next edge has no delay
                    std::vector<frac::Edge> boundaries = { current, next };
                    std::optional<frac::Edge> requiredEdge = edgeIfRequired(next, this->m_reqEdge);
                    if (requiredEdge.has_value()) {
                        boundaries.push_back(requiredEdge.value());
                    }
                    int indexFirstInterior { static_cast<int>(boundaries.size()) };
                    boundaries.push_back(this->m_adjEdge);
                    boundaries.push_back(this->m_gapEdge);
                    boundaries.push_back(this->m_adjEdge);
                    std::optional<frac::Edge> secondRequiredEdge = edgeIfRequired(current, this->m_reqEdge);
                    if (secondRequiredEdge.has_value()) {
                        boundaries.push_back(secondRequiredEdge.value());
                    }
                    frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                    c.setFirstInterior(indexFirstInterior);
                    if (writeConstraints) {
                        addIncidenceConstraint(*this, c, i, nbIntermediateStates + 1, 0, res.size());
                        addIncidenceConstraint(*this, c, frac::utils::mod(i + 1, this->len()), 0, 1, res.size());
                    }
                    res.push_back(c);
                }
            }
        }
        for (std::size_t i = 0; i < res.size(); ++i) {
            frac::Face current = res[i];
            frac::Face next = res[frac::utils::mod(i + 1, res.size())];
            if (writeConstraints) {
                addAdjacencyConstraint(*this, current, next, i, current.firstInterior(), frac::utils::mod(i + 1, res.size()), next.lastInterior());
            }
        }
    } else {
        // current face has delay
        std::vector<frac::Edge> boundaries = {};
        for (std::size_t i = 0; i < this->len(); ++i) {
            // for each edge, we subdivide it and add it to the result face
            frac::Edge edge = (*this)[i];
            std::vector<Edge> subdivisionsEdge = edge.subdivisions(this->m_reqEdge);
            for (frac::Edge const& e: subdivisionsEdge) {
                boundaries.push_back(e);
            }
        }
        frac::Face c = Face(boundaries, this->m_delay - 1, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
        // no adjacency constraints
        // write incidence constraints
        if (writeConstraints) {
            int k = 0;
            for (std::size_t i = 0; i < this->len(); ++i) {
                frac::Edge edge { (*this)[i] };
                unsigned int nbSubdivisionsEdge = edge.nbActualSubdivisions();
                for (unsigned int j = 0; j < nbSubdivisionsEdge; ++j) {
                    addIncidenceConstraint(*this, c, i, j, k, 0);
                    if (edge.edgeType() == EdgeType::BEZIER) {
                        k++;
                    }
                    if (edge.edgeType() == EdgeType::CANTOR) {
                        if (edge.isDelay()) {
                            k++;
                        } else {
                            k += (j != (nbSubdivisionsEdge - 1)) ? 3 : 1;
                        }
                    }
                }
            }
        }
        res.push_back(c);
    }
    s_subdivisions[m_name] = res;
    return res;
}

std::vector<frac::Face> frac::Face::subdivisionsSurroundDelayAndBezier() const {
    std::vector<frac::Face> res;
    bool writeConstraints = s_incidenceConstraints.find(this->name()) == s_incidenceConstraints.end();
    if (m_delay == 0) {
        //if face has no delay
        std::vector<std::size_t> visitedDelayEdges;
        for (std::size_t i = 0; i < this->len(); ++i) {
            // foreach edge
            frac::Edge current = (*this)[i];
            if (current.isDelay()) {
                // current edge has a delay so look at edges before and after to merge also with bezier
                frac::Edge next = (*this)[utils::mod(i + 1, this->len())];
                frac::Edge prev = (*this)[static_cast<std::size_t>(utils::mod(static_cast<int>(i) - 1, static_cast<int>(this->len())))];

                if (prev.edgeType() == EdgeType::BEZIER && !prev.isDelay() && next.edgeType() == EdgeType::BEZIER && !next.isDelay()) {
                    // prev and next are bezier so merge with both of them
                    frac::Edge subCurrent { current };
                    subCurrent.decreaseDelay();
                    std::vector<frac::Edge> boundaries = { prev, subCurrent, next };
                    boundaries.push_back(this->m_adjEdge);
                    boundaries.push_back(this->m_gapEdge);
                    boundaries.push_back(this->m_adjEdge);
                    frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                    c.setFirstInterior(3);
                    if (writeConstraints) {
                        addIncidenceConstraint(*this, c, static_cast<std::size_t>(utils::mod(static_cast<int>(i) - 1, static_cast<int>(this->len()))), prev.nbSubdivisions() - 1, 0, res.size());
                        addIncidenceConstraint(*this, c, i, 0, 1, res.size());
                        addIncidenceConstraint(*this, c, frac::utils::mod(i + 1, this->len()), 0, 2, res.size());
                    }
                    res.push_back(c);
                    visitedDelayEdges.push_back(i);
                } else if (prev.edgeType() == EdgeType::BEZIER && !prev.isDelay()) {
                    // prev is bezier but not next so merge with prev only
                    frac::Edge subFirst { current };
                    subFirst.decreaseDelay();
                    std::vector<frac::Edge> boundaries = { prev, subFirst };
                    boundaries.push_back(this->m_adjEdge);
                    boundaries.push_back(this->m_gapEdge);
                    boundaries.push_back(this->m_adjEdge);
                    frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                    c.setFirstInterior(2);
                    if (writeConstraints) {
                        addIncidenceConstraint(*this, c, static_cast<std::size_t>(utils::mod(static_cast<int>(i) - 1, static_cast<int>(this->len()))), prev.nbSubdivisions() - 1, 0, res.size());
                        addIncidenceConstraint(*this, c, i, 0, 1, res.size());
                    }
                    res.push_back(c);
                    visitedDelayEdges.push_back(i);
                } else if (next.edgeType() == EdgeType::BEZIER && !next.isDelay()) {
                    // next is bezier but not prev so merge with next only
                    frac::Edge subFirst { current };
                    subFirst.decreaseDelay();
                    std::vector<frac::Edge> boundaries = { subFirst, next };
                    boundaries.push_back(this->m_adjEdge);
                    boundaries.push_back(this->m_gapEdge);
                    boundaries.push_back(this->m_adjEdge);
                    frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                    c.setFirstInterior(2);
                    if (writeConstraints) {
                        addIncidenceConstraint(*this, c, i, 0, 0, res.size());
                        addIncidenceConstraint(*this, c, frac::utils::mod(i + 1, this->len()), 0, 1, res.size());
                    }
                    res.push_back(c);
                } else if ((prev.edgeType() == EdgeType::CANTOR || prev.isDelay()) && (next.edgeType() == EdgeType::CANTOR || next.isDelay())) {
                    // next and prev are not bezier so no merge
                    frac::Edge subFirst { current };
                    subFirst.decreaseDelay();
                    std::vector<frac::Edge> boundaries = { subFirst };
                    boundaries.push_back(this->m_adjEdge);
                    boundaries.push_back(this->m_gapEdge);
                    boundaries.push_back(this->m_adjEdge);
                    frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                    c.setFirstInterior(1);
                    if (writeConstraints) {
                        addIncidenceConstraint(*this, c, i, 0, 0, res.size());
                    }
                    res.push_back(c);
                }
            } else {
                // current edge has not a delay, so we look at the edge before if current edge is Cantor
                std::size_t idx = static_cast<std::size_t>(utils::mod(static_cast<int>(i) - 1, static_cast<int>(this->len())));
                if ((*this)[idx].isDelay() && current.edgeType() == EdgeType::CANTOR) {
                    // the edge before has a delay and current edge is CANTOR, then we have not merged the edge so create a subcell for the edge's first subdivision
                    std::vector<frac::Edge> boundaries = { current };
                    std::optional<frac::Edge> requiredEdge = edgeIfRequired(current, this->m_reqEdge);
                    if (requiredEdge.has_value()) {
                        boundaries.push_back(requiredEdge.value());
                    }
                    boundaries.push_back(this->m_adjEdge);
                    boundaries.push_back(this->m_gapEdge);
                    boundaries.push_back(this->m_adjEdge);
                    frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                    c.setFirstInterior(static_cast<int>(boundaries.size() - 3));
                    if (writeConstraints) {
                        addIncidenceConstraint(*this, c, i, 0, 0, res.size());
                    }
                    res.push_back(c);
                }

                // creation of intermediate subcells
                int nbIntermediateStates { static_cast<int>(current.nbSubdivisions()) - 2 };
                for (int j = 0; j < nbIntermediateStates; j++) {
                    std::vector<frac::Edge> boundaries = { current };
                    std::optional<frac::Edge> requiredEdge = edgeIfRequired(current, this->m_reqEdge);
                    if (requiredEdge.has_value()) {
                        boundaries.push_back(requiredEdge.value());
                    }
                    int indexFirstInterior { static_cast<int>(boundaries.size()) };
                    boundaries.push_back(this->m_adjEdge);
                    boundaries.push_back(this->m_gapEdge);
                    boundaries.push_back(this->m_adjEdge);
                    if (requiredEdge.has_value()) {
                        boundaries.push_back(requiredEdge.value());
                    }
                    frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                    c.setFirstInterior(indexFirstInterior);
                    if (writeConstraints) {
                        addIncidenceConstraint(*this, c, i, j + 1, 0, res.size());
                    }
                    res.push_back(c);
                }

                // creation of last subcell of the edge, depends on the next edge
                frac::Edge next = (*this)[utils::mod(i + 1, this->len())];
                if (next.isDelay()) {
                    // if next edge has delay
                    if (current.edgeType() == EdgeType::CANTOR) {
                        // if current edge is cantor, create a subcell only with the last current edge subdivision
                        std::vector<frac::Edge> boundaries = { current };
                        boundaries.push_back(this->m_adjEdge);
                        boundaries.push_back(this->m_gapEdge);
                        boundaries.push_back(this->m_adjEdge);
                        std::optional<frac::Edge> requiredEdge = edgeIfRequired(current, this->m_reqEdge);
                        if (requiredEdge.has_value()) {
                            boundaries.push_back(requiredEdge.value());
                        }
                        frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                        c.setFirstInterior(1);
                        if (writeConstraints) {
                            addIncidenceConstraint(*this, c, i, nbIntermediateStates + 1, 0, res.size());
                        }
                        res.push_back(c);
                    } else if (std::find(visitedDelayEdges.begin(), visitedDelayEdges.end(), utils::mod(i + 1, this->len())) == visitedDelayEdges.end()) {
                        // if next edge that has a delay has not been visited, we need to merge with it

                        // current edge is Bezier, create subcell with subdivided delay edge
                        // and subdivided bezier edge but check also with the edge after the delay
                        // edge to merge also this one if it is bezier. If it is the case, increment i
                        // to skip the next delay edge since the subdivision is already created

                        // need to check the next's next edge
                        frac::Edge nextNext = (*this)[utils::mod(i + 2, this->len())];
                        if (!nextNext.isDelay() && nextNext.edgeType() == EdgeType::BEZIER) {
                            // if next's next edge is bezier without delay, merge for the subcell
                            frac::Edge subNext { next };
                            subNext.decreaseDelay();
                            std::vector<frac::Edge> boundaries = { current, subNext, nextNext };
                            boundaries.push_back(this->m_adjEdge);
                            boundaries.push_back(this->m_gapEdge);
                            boundaries.push_back(this->m_adjEdge);
                            frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                            c.setFirstInterior(3);
                            if (writeConstraints) {
                                addIncidenceConstraint(*this, c, i, nbIntermediateStates + 1, 0, res.size());
                                addIncidenceConstraint(*this, c, frac::utils::mod(i + 1, this->len()), 0, 1, res.size());
                                addIncidenceConstraint(*this, c, frac::utils::mod(i + 2, this->len()), 0, 2, res.size());
                            }
                            res.push_back(c);
                        } else {
                            // next's next edge can't be merged (not bezier or delay)
                            frac::Edge subNext { next };
                            subNext.decreaseDelay();
                            std::vector<frac::Edge> boundaries = { current, subNext };
                            boundaries.push_back(this->m_adjEdge);
                            boundaries.push_back(this->m_gapEdge);
                            boundaries.push_back(this->m_adjEdge);
                            frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                            c.setFirstInterior(2);
                            if (writeConstraints) {
                                addIncidenceConstraint(*this, c, i, nbIntermediateStates + 1, 0, res.size());
                                addIncidenceConstraint(*this, c, frac::utils::mod(i + 1, this->len()), 0, 1, res.size());
                            }
                            res.push_back(c);
                        }
                        // the next edge has been merged, so no need to create subs with it
                        i++;
                    }
                } else {
                    // if next edge has no delay, merge edges from current and next edge for the subcell
                    std::vector<frac::Edge> boundaries = { current, next };
                    std::optional<frac::Edge> requiredEdge = edgeIfRequired(next, this->m_reqEdge);
                    if (requiredEdge.has_value()) {
                        boundaries.push_back(requiredEdge.value());
                    }
                    int indexFirstInterior { static_cast<int>(boundaries.size()) };
                    boundaries.push_back(this->m_adjEdge);
                    boundaries.push_back(this->m_gapEdge);
                    boundaries.push_back(this->m_adjEdge);
                    std::optional<frac::Edge> secondRequiredEdge = edgeIfRequired(current, this->m_reqEdge);
                    if (secondRequiredEdge.has_value()) {
                        boundaries.push_back(secondRequiredEdge.value());
                    }
                    frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                    c.setFirstInterior(indexFirstInterior);
                    if (writeConstraints) {
                        addIncidenceConstraint(*this, c, i, nbIntermediateStates + 1, 0, res.size());
                        addIncidenceConstraint(*this, c, frac::utils::mod(i + 1, this->len()), 0, 1, res.size());
                    }
                    res.push_back(c);
                }
            }
        }
        for (std::size_t i = 0; i < res.size(); ++i) {
            frac::Face current = res[i];
            frac::Face next = res[frac::utils::mod(i + 1, res.size())];
            if (writeConstraints) {
                addAdjacencyConstraint(*this, current, next, i, current.firstInterior(), frac::utils::mod(i + 1, res.size()), next.lastInterior());
            }
        }
    } else {
        // current face has delay
        std::vector<frac::Edge> boundaries = {};
        for (std::size_t i = 0; i < this->len(); ++i) {
            // for each edge, we subdivide it and add it to the result face
            frac::Edge edge = (*this)[i];
            std::vector<Edge> subdivisionsEdge = edge.subdivisions(this->m_reqEdge);
            for (frac::Edge const& e: subdivisionsEdge) {
                boundaries.push_back(e);
            }
        }
        frac::Face c = Face(boundaries, this->m_delay - 1, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
        // no adjacency constraints
        // write incidence constraints
        if (writeConstraints) {
            int k = 0;
            for (std::size_t i = 0; i < this->len(); ++i) {
                frac::Edge edge { (*this)[i] };
                unsigned int nbSubdivisionsEdge = edge.nbActualSubdivisions();
                for (unsigned int j = 0; j < nbSubdivisionsEdge; ++j) {
                    addIncidenceConstraint(*this, c, i, j, k, 0);
                    if (edge.edgeType() == EdgeType::BEZIER) {
                        k++;
                    }
                    if (edge.edgeType() == EdgeType::CANTOR) {
                        if (edge.isDelay()) {
                            k++;
                        } else {
                            k += (j != (nbSubdivisionsEdge - 1)) ? 3 : 1;
                        }
                    }
                }
            }
        }
        res.push_back(c);
    }
    s_subdivisions[m_name] = res;
    return res;
}
