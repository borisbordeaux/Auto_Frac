#include <iostream>
#include "face.h"
#include "utils.h"

frac::UniqueVector<frac::Face> frac::Face::s_existingFaces;
std::map<std::string, std::string> frac::Face::s_incidenceConstraints;
std::map<std::string, std::string> frac::Face::s_adjacencyConstraints;

std::vector<frac::Edge> shiftVector(std::vector<frac::Edge> const& edges) {
    std::vector<frac::Edge> res;
    res.reserve(edges.size());
    for (std::size_t i = 1; i < edges.size(); ++i) {
        res.emplace_back(edges[i]);
    }
    res.emplace_back(edges[0]);
    return res;
}

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
        this->m_name = "Cell_" + std::to_string(s_existingFaces.len());
        if (this->m_delay != 0) {
            // one face if delayed, with subdivided boundaries
            // add delay info to name
            this->m_name += "_" + std::to_string(delay);
        }
        s_existingFaces.add(*this);
    }
}

std::vector<frac::Edge> const& frac::Face::data() const {
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
    std::vector<frac::Face> res;
    bool writeConstraints = s_incidenceConstraints.find(this->name()) == s_incidenceConstraints.end();
    if (m_delay == 0) {
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
                std::size_t idx = static_cast<std::size_t>(Utils::mod(static_cast<int>(i) - 1, static_cast<int>(this->len())));
                if ((*this)[idx].isDelay()) {
                    // the state before has a delay
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
                frac::Edge next = (*this)[Utils::mod(i + 1, this->len())];
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
                        addIncidenceConstraint(*this, c, frac::Utils::mod(i + 1, this->len()), 0, 1, res.size());
                    }
                    res.push_back(c);
                }
            }
        }
        for (std::size_t i = 0; i < res.size(); ++i) {
            frac::Face current = res[i];
            frac::Face next = res[frac::Utils::mod(i + 1, res.size())];
            if (writeConstraints) {
                addAdjacencyConstraint(*this, current, next, i, current.firstInterior(), frac::Utils::mod(i + 1, res.size()), next.lastInterior());
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
    return res;
}

const frac::Edge& frac::Face::operator[](std::size_t index) const {
    return this->m_data[index];
}

bool frac::Face::operator==(frac::Face const& other) const {
    if (this->m_delay != other.m_delay || this->len() != other.len() || this->m_adjEdge != other.m_adjEdge || this->m_gapEdge != other.m_gapEdge || this->m_reqEdge != other.m_reqEdge)
        return false;

    std::vector<frac::Edge> shifted { other.m_data };

    for (std::size_t i = 0; i < this->len(); ++i) {
        if (this->m_data == shifted) {
            return true;
        }
        std::vector<frac::Edge> new_shifted { shiftVector(shifted) };
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
    int b1 = frac::Utils::mod(static_cast<int>(indexBordFace1) - faceSub1.offset(), static_cast<int>(faceSub1.len()));
    int s2 = static_cast<int>(indexSubFace2);
    int b2 = frac::Utils::mod(static_cast<int>(indexBordFace2) - faceSub2.offset(), static_cast<int>(faceSub2.len()));
    s_adjacencyConstraints[face.name()] += "    " + face.name() + "(Sub('" + std::to_string(s1) + "') + Bord('" + std::to_string(b1) + "') + Permut('0'), Sub('" + std::to_string(s2) + "') + Bord('" + std::to_string(b2) + "'))\n";
}

void frac::Face::addIncidenceConstraint(frac::Face const& face, frac::Face const& faceSub, unsigned int indexParentEdge, unsigned int indexSubEdge, unsigned int indexSubFaceEdge, unsigned int indexSubFace) {
    if (s_incidenceConstraints.find(face.name()) == std::end(Face::s_incidenceConstraints)) {
        s_incidenceConstraints[face.name()] = "";
    }
    int b1 = frac::Utils::mod(static_cast<int>(indexParentEdge) - face.offset(), static_cast<int>(face.len()));
    int s1 = static_cast<int>(indexSubEdge);
    int s2 = static_cast<int>(indexSubFace);
    int b2 = frac::Utils::mod(static_cast<int>(indexSubFaceEdge) - faceSub.offset(), static_cast<int>(faceSub.len()));
    s_incidenceConstraints[face.name()] += "    " + face.name() + "(Bord('" + std::to_string(b1) + "') + Sub('" + std::to_string(s1) + "'), Sub('" + std::to_string(s2) + "') + Bord('" + std::to_string(b2) + "'))\n";
}

int frac::Face::computeOffset(frac::Face const& face, frac::Face const& other) {
    if (face.m_delay != other.m_delay || face.len() != other.len() || face.m_adjEdge != other.m_adjEdge || face.m_gapEdge != other.m_gapEdge || face.m_reqEdge != other.m_reqEdge)
        return -1;
    std::vector<Edge> shifted { other.m_data };
    for (std::size_t i = 0; i < other.len(); ++i) {
        if (face.m_data == shifted) {
            return static_cast<int>(i);
        }
        std::vector<frac::Edge> new_shifted { shiftVector(shifted) };
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
        for (std::size_t j = i; j < res.len(); ++j) {
            std::vector<frac::Face> subs = res[j].subdivisions();
            for (frac::Face const& f: subs) {
                added.add(f);
            }
        }
        std::size_t lastSize = res.len();
        for (frac::Face const& f: added.data()) {
            res.add(f);
        }
        changed = res.len() != lastSize;
        i = lastSize;
    }
    return res;
}

std::string frac::Face::toString() const {
    std::string res = this->m_name + " : [" + (*this)[0].toString();
    for (std::size_t i = 1; i < this->len(); ++i) {
        res += ", " + (*this)[i].toString();
    }
    res += "], adj, gap, req edges are ";

    res += this->m_adjEdge.toString() + " ";
    res += this->m_gapEdge.toString() + " ";
    res += this->m_reqEdge.toString() + " ";
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
}
