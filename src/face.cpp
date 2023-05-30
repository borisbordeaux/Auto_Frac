#include "face.h"

frac::Face::Face(std::vector<Edge> edges, unsigned int delay, frac::Edge const& adjEdge, frac::Edge const& gapEdge, frac::Edge const& reqEdge) :
        m_data(std::move(edges)), m_delay(delay), m_adjEdge(adjEdge), m_gapEdge(gapEdge), m_reqEdge(reqEdge), m_nbSubdivisions(0), m_offset(0), m_firstInterior(-1) {
    for (Face const& f: s_existingFaces.data()) {
        if (*this == f) {
            this->m_name = f.m_name;
            this->m_nbSubdivisions = f.m_nbSubdivisions;
            this->m_offset = computeOffset(f, *this);
        }
    }
    //if face doesn't exist
    if (this->m_name.empty()) {
        this->m_name = "Cell_" + std::to_string(s_existingFaces.len());
        if (this->m_delay == 0) {
            for (Edge const& e: this->m_data) {
                this->m_nbSubdivisions += e.nbSubdivisions();
            }
            this->m_nbSubdivisions -= this->len();
        } else {
            // one face if delayed, with subdivided boundaries
            // add delay info to name
            this->m_name += "_" + std::to_string(delay);
            this->m_nbSubdivisions = 1;
        }
        s_existingFaces.add(*this);
    }
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
    bool writeConstraints = s_incidenceConstraints.find(name()) == s_incidenceConstraints.end();
    if (m_delay == 0) {
        for (int i = 0; i < len(); ++i) {
            // foreach edge
            frac::Edge current = (*this)[i];
            if (current.isDelay()) {
                // current edge has a delay so creation of one face
                frac::Edge subFirst { current };
                subFirst.decreaseDelay();
                std::vector<frac::Edge> boundaries = { subFirst };
                std::vector<frac::Edge> interiorEdges = interior(this->m_adjEdge, this->m_gapEdge);
                boundaries.insert(boundaries.end(), interiorEdges.begin(), interiorEdges.end());
                frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                c.setFirstInterior(1);
                if (writeConstraints) {
                    addIncidenceConstraint(*this, c, i, 0, 0, res.size());
                }
                res.push_back(c);
            } else {
                // current edge has not a delay, so we look at the edge before
                if ((*this)[static_cast<int>((i - 1) % this->len())].isDelay()) {
                    // the state before has a delay
                    std::vector<frac::Edge> boundaries = { current };
                    std::vector<frac::Edge> requiredEdge = edgeIfRequired(current, this->m_reqEdge);
                    boundaries.insert(boundaries.end(), requiredEdge.begin(), requiredEdge.end());
                    std::vector<frac::Edge> interiorEdges = interior(this->m_adjEdge, this->m_gapEdge);
                    boundaries.insert(boundaries.end(), interiorEdges.begin(), interiorEdges.end());
                    frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                    c.setFirstInterior(static_cast<int>(boundaries.size() - 3));
                    if (writeConstraints) {
                        addIncidenceConstraint(*this, c, i, 0, 0, res.size());
                    }
                    res.push_back(c);
                }

                //creation of intermediate states
                int nbIntermediateStates { static_cast<int>(current.nbSubdivisions()) - 2 };
                if (nbIntermediateStates > 0) {
                    for (int j = 0; j < nbIntermediateStates; j++) {
                        std::vector<frac::Edge> boundaries = { current };
                        std::vector<frac::Edge> requiredEdge = edgeIfRequired(current, this->m_reqEdge);
                        boundaries.insert(boundaries.end(), requiredEdge.begin(), requiredEdge.end());
                        int indexFirstInterior { static_cast<int>(boundaries.size()) };
                        std::vector<frac::Edge> interiorEdges = interior(this->m_adjEdge, this->m_gapEdge);
                        boundaries.insert(boundaries.end(), interiorEdges.begin(), interiorEdges.end());
                        boundaries.insert(boundaries.end(), requiredEdge.begin(), requiredEdge.end());
                        frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                        c.setFirstInterior(indexFirstInterior);
                        if (writeConstraints) {
                            addIncidenceConstraint(*this, c, i, j + 1, 0, res.size());
                        }
                        res.push_back(c);
                    }
                }

                // creation of last state of the edge
                frac::Edge next = (*this)[static_cast<int>((i + 1) % this->len())];
                if (next.isDelay()) {
                    // if next edge has delay
                    std::vector<frac::Edge> boundaries = { current };
                    std::vector<frac::Edge> interiorEdges = interior(this->m_adjEdge, this->m_gapEdge);
                    boundaries.insert(boundaries.end(), interiorEdges.begin(), interiorEdges.end());
                    std::vector<frac::Edge> requiredEdge = edgeIfRequired(current, this->m_reqEdge);
                    boundaries.insert(boundaries.end(), requiredEdge.begin(), requiredEdge.end());
                    frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                    c.setFirstInterior(1);
                    if (writeConstraints) {
                        addIncidenceConstraint(*this, c, i, nbIntermediateStates + 1, 0, res.size());
                    }
                    res.push_back(c);
                } else {
                    // if next edge has no delay
                    std::vector<frac::Edge> boundaries = { current, next };
                    std::vector<frac::Edge> requiredEdge = edgeIfRequired(next, this->m_reqEdge);
                    boundaries.insert(boundaries.end(), requiredEdge.begin(), requiredEdge.end());
                    int indexFirstInterior { static_cast<int>(boundaries.size()) };
                    std::vector<frac::Edge> interiorEdges = interior(this->m_adjEdge, this->m_gapEdge);
                    boundaries.insert(boundaries.end(), interiorEdges.begin(), interiorEdges.end());
                    std::vector<frac::Edge> secondRequiredEdge = edgeIfRequired(current, this->m_reqEdge);
                    boundaries.insert(boundaries.end(), secondRequiredEdge.begin(), secondRequiredEdge.end());
                    frac::Face c = Face(boundaries, 0, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
                    c.setFirstInterior(indexFirstInterior);
                    if (writeConstraints) {
                        addIncidenceConstraint(*this, c, i, nbIntermediateStates + 1, 0, res.size());
                        addIncidenceConstraint(*this, c, (i + 1) % this->len(), 0, 1, res.size());
                    }
                    res.push_back(c);
                }
            }
        }
        for (int i = 0; i < this->len(); ++i) {
            frac::Face current = res[i];
            frac::Face next = res[(i + 1) % res.size()];
            if (writeConstraints) {
                addAdjacencyConstraint(*this, current, next, i, current.firstInterior(), (i + 1) % res.size(), next.lastInterior());
            }
        }
    } else {
        // current face has delay
        std::vector<frac::Edge> boundaries = {};
        for (int i = 0; i < this->len(); ++i) {
            // for each edge, we subdivide it and add it to the result face
            frac::Edge edge = (*this)[i];
            std::vector<Edge> subdivisionsEdge = edge.subdivisions();
            boundaries.insert(boundaries.end(), subdivisionsEdge.begin(), subdivisionsEdge.end());
        }
        frac::Face c = Face(boundaries, this->m_delay - 1, this->m_adjEdge, this->m_gapEdge, this->m_reqEdge);
        // no adjacency constraints
        if (writeConstraints) {
            int k = 0;
            for (int i = 0; i < this->len(); ++i) {
                frac::Edge edge = (*this)[i];
                unsigned int nbSubdivisionsEdge = edge.nbSubdivisions();
                for (unsigned int j = 0; j < nbSubdivisionsEdge; ++j) {
                    addIncidenceConstraint(*this, c, i, j, k, 0);
                    if (edge.edgeType() == EdgeType::BEZIER) {
                        k++;
                    }
                    if (edge.edgeType() == EdgeType::CANTOR) {
                        if (edge.isDelay()) {
                            k++;
                        } else {
                            k += (j != nbSubdivisionsEdge - 1) ? 3 : 1;
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

    std::vector<frac::Edge> shifted;
    shifted.reserve(other.m_data.size());
    for (frac::Edge const& e: other.m_data) {
        shifted.emplace_back(e);
    }
    for (int i = 0; i < other.len(); ++i) {
        if (this->m_data == shifted) {
            return true;
        }
        frac::Edge first { shifted[0] };
        shifted.erase(std::begin(shifted));
        shifted.emplace_back(first);
    }
    return false;
}

namespace frac {
std::ostream& operator<<(std::ostream& os, frac::Face const& edge) {
    os << edge.m_name << " : [" << edge[0];
    for (int i = 1; i < edge.len(); ++i) {
        os << ", " << edge[i];
    }
    os << "], " << edge.m_nbSubdivisions << " subdivisions, interior is ";

    for (const Edge& e: Face::interior(edge.m_adjEdge, edge.m_gapEdge)) {
        os << e << " ";
    }

    return os;
}
}

void frac::Face::addAdjacencyConstraint(frac::Face const& face, frac::Face const& faceSub1, frac::Face const& faceSub2, unsigned int indexSubFace1, unsigned int indexBordFace1, unsigned int indexSubFace2, unsigned int indexBordFace2) {
    if (s_adjacencyConstraints.find(face.name()) != std::end(Face::s_adjacencyConstraints)) {
        s_adjacencyConstraints[face.name()] = "";
    }
    s_adjacencyConstraints[face.name()] += "    " + face.name() + "(Sub('" + std::to_string(indexSubFace1) + "') + Bord('" + std::to_string((indexBordFace1 - faceSub1.offset()) % faceSub1.len()) + "') + Permut('0'), Sub('" + std::to_string(indexSubFace2) + "') + Bord('" + std::to_string((indexBordFace2 - faceSub2.offset()) % faceSub2.len()) + "'))\n";
}

void frac::Face::addIncidenceConstraint(frac::Face const& face, frac::Face const& faceSub, unsigned int indexParentEdge, unsigned int indexSubEdge, unsigned int indexSubFaceEdge, unsigned int indexSubFace) {
    if (s_incidenceConstraints.find(face.name()) != std::end(Face::s_incidenceConstraints)) {
        s_incidenceConstraints[face.name()] = "";
    }
    s_incidenceConstraints[face.name()] += "    " + face.name() + "(Bord('" + std::to_string((indexParentEdge - face.offset()) % face.len()) + "') + Sub('" + std::to_string(indexSubEdge) + "'), Sub('" + std::to_string(indexSubFace) + "') + Bord('" + std::to_string((indexSubFaceEdge - faceSub.offset()) % faceSub.len()) + "'))\n";
}

int frac::Face::computeOffset(frac::Face const& face, frac::Face const& other) {
    if (face.m_delay != other.m_delay || face.len() != other.len() || face.m_adjEdge != other.m_adjEdge || face.m_gapEdge != other.m_gapEdge || face.m_reqEdge != other.m_reqEdge)
        return -1;
    std::vector<Edge> shifted;
    shifted.reserve(face.m_data.size());
    for (Edge const& e: face.m_data) {
        shifted.emplace_back(e);
    }
    for (int i = 0; i < other.len(); ++i) {
        if (face.m_data == shifted) {
            return i;
        }
        Edge first { shifted[0] };
        shifted.erase(std::begin(shifted));
        shifted.emplace_back(first);
    }
    return -1;
}

std::vector<frac::Edge> frac::Face::edgeIfRequired(frac::Edge const& edge, frac::Edge const& reqEdge) {
    return edge.edgeType() == EdgeType::CANTOR ? std::vector<Edge> { reqEdge } : std::vector<Edge>();
}

std::vector<frac::Edge> frac::Face::interior(frac::Edge const& adjacencyEdge, frac::Edge const& gapEdge) {
    return { adjacencyEdge, gapEdge, adjacencyEdge };
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
                res.add(f);
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
