#include "face.h"

frac::Face::Face(std::set<Edge> edges, unsigned int delay, frac::Edge adjEdge, frac::Edge gapEdge, frac::Edge reqEdge) :
        m_data(edges), m_firstInterior(-1), m_name(""), m_nbSubdivisions(0), m_offset(0), m_delay(delay),
        m_adjEdge(adjEdge), m_gapEdge(gapEdge), m_reqEdge(reqEdge) {
    for (Face f: existingFaces) {
        if (*this == f) {
            this->m_name = f.m_name;
            this->m_nbSubdivisions = f.m_nbSubdivisions;
            this->m_offset = f.m_offset;
        }
    }
    //if face doesn't exist
    if (this->m_name.empty()) {
        this->m_name = "Cell_" + std::to_string(existingFaces.size());
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
        Face::existingFaces.append(*this);
    }
}

std::size_t frac::Face::len() const {
    return this->m_data.size();
}

void frac::Face::setFirstInterior(int index) {
    this->m_firstInterior = index;
}

int frac::Face::firstInterior() const {
    return this->m_firstInterior;
}

int frac::Face::lastInterior() const {
    return this->m_firstInterior + 2;
}

const frac::Edge& frac::Face::operator[](int index) const {
    return this->m_data[index];
}

bool frac::Face::operator==(const frac::Face& other) const {
    if (this->m_delay != other.m_delay || this->m_adjEdge != other.m_adjEdge || this->m_gapEdge != other.m_gapEdge || this->m_reqEdge != other.m_reqEdge || this->len() != other.len())
        return false;

    for (int i = 0; i < this->len(); ++i) {
        for (int j = 0; j < other.len(); ++j) {
            for (int k = 0; k < other.len(); ++k) {

            }
        }
    }

    return false;
}
