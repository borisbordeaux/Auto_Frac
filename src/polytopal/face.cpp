#include "polytopal/face.h"

#include "polytopal/edge.h"
#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/mesh.h"
#include "utils/utils.h"

frac::Set<poly::Face> poly::Face::s_existingFaces;
he::Mesh const* poly::Face::s_mesh = nullptr;
std::map<std::string, std::string> poly::Face::s_incidenceConstraints;
std::map<std::string, std::string> poly::Face::s_adjacencyConstraints;

void poly::Face::init() {
    for (poly::Face const& face: s_existingFaces.data()) {
        if (*this == face) {
            this->m_name = face.m_name;
        }
    }
    //if face doesn't exist
    if (this->m_name.empty()) {
        this->m_name = "Cell_" + std::to_string(s_existingFaces.size());
        s_existingFaces.add(*this);
    }
}

poly::Face::Face(he::Face* f) : m_face(f) {
    he::HalfEdge* he = f->halfEdge();
    he::HalfEdge* heNxt = he;
    do {
        this->m_edges.emplace_back(heNxt->origin(), frac::Edge(frac::EdgeType::BEZIER, heNxt->origin()->degree() - 1, 0));
        this->m_halfEdges.push_back(heNxt);
        heNxt = heNxt->next();
    } while (heNxt != he);
    this->init();
}

std::string poly::Face::name() const {
    return this->m_name;
}

std::size_t poly::Face::len() const {
    return this->m_face->nbEdges();
}

std::vector<poly::Face> poly::Face::subdivisions() const {
    std::vector<poly::Face> res;
    bool writeConstraints = poly::Face::s_incidenceConstraints.find(this->name()) == s_incidenceConstraints.end();
    for (he::Face* f: Face::s_mesh->faces()) {
        if (this->m_face != f) {
            res.emplace_back(f);
        }
    }

    if (writeConstraints) {
        // adjacency constraints
        for (std::size_t i = 0; i < res.size() - 1; ++i) { //for each fractal face
            for (std::size_t j = 0; j < res[i].constData().size(); ++j) { //for each edge
                for (std::size_t k = i + 1; k < res.size(); ++k) { //for each other face
                    for (std::size_t l = 0; l < res[k].constData().size(); ++l) { //for each edge
                        // if polytopal faces are adjacent, fractal faces will be adjacent
                        if (res[i].halfEdges()[j]->twin() == res[k].halfEdges()[l]) {
                            addAdjacencyConstraint(*this, i, j, k, l);
                        }
                    }
                }
            }
        }

        // incidence constraints
        for (std::size_t i = 0; i < m_edges.size(); i++) {
            poly::Edge e1 = m_edges[i];
            he::Vertex* polyV1 = e1.HEVertex();
            for (std::size_t j = 0; j < res.size(); j++) {
                Face const& f1 = res[j];
                he::Face* polyF1 = f1.m_face;
                for (std::size_t k = 0; k < f1.m_edges.size(); k++) {
                    poly::Edge const& e2 = f1.m_edges[k];
                    he::Vertex* polyV2 = e2.HEVertex();
                    if (polyV1 == polyV2) {
                        std::vector<he::Face*> list = polyV1->getAllFacesAroundVertex(m_face);
                        for (std::size_t l = 0; l < list.size() - 1; l++) {
                            if (polyF1 == list[l]) {
                                addIncidenceConstraint(*this, i, l, j, k);
                            }
                        }
                    }
                }
            }
        }
    }
    return res;
}

std::vector<poly::Edge> const& poly::Face::constData() const {
    return this->m_edges;
}

std::string poly::Face::toString() const {
    std::string res = this->name();
    for (poly::Edge const& e: this->m_edges) {
        res += " -- " + e.toString();
    }
    return res;
}

namespace poly {
std::ostream& operator<<(std::ostream& os, poly::Face const& face) {
    os << face.name() << " (associated half-edge face : " + face.m_face->name().toStdString() + ") ";
    for (poly::Edge const& edge: face.m_edges) {
        os << " -- " << edge.toString();
    }
    return os;
}
}

bool poly::Face::operator==(const poly::Face& other) const {
    if (this->len() != other.len()) {
        return false;
    }
    return this->m_face == other.m_face;
}

poly::Edge const& poly::Face::operator[](std::size_t index) const {
    return this->m_edges[index];
}

void poly::Face::reset() {
    poly::Face::s_incidenceConstraints.clear();
    poly::Face::s_adjacencyConstraints.clear();
    poly::Face::s_existingFaces.clear();
    poly::Face::s_mesh = nullptr;
}

std::vector<he::HalfEdge*> poly::Face::halfEdges() const {
    return this->m_halfEdges;
}

void poly::Face::addAdjacencyConstraint(const poly::Face& face, unsigned int indexSubFace1, unsigned int indexBordFace1, unsigned int indexSubFace2, unsigned int indexBordFace2) {
    if (s_adjacencyConstraints.find(face.name()) == std::end(Face::s_adjacencyConstraints)) {
        s_adjacencyConstraints[face.name()] = "";
    }
    int s1 = static_cast<int>(indexSubFace1);
    int b1 = static_cast<int>(indexBordFace1);
    int s2 = static_cast<int>(indexSubFace2);
    int b2 = static_cast<int>(indexBordFace2);
    s_adjacencyConstraints[face.name()] += "    " + face.name() + "(Sub('" + std::to_string(s1) + "') + Bord('" + std::to_string(b1) + "') + Bord('1'), Sub('" + std::to_string(s2) + "') + Bord('" + std::to_string(b2) + "') + Bord('1'))\n";
}

void poly::Face::addIncidenceConstraint(const poly::Face& face, unsigned int indexParentEdge, unsigned int indexSubEdge, unsigned int indexSubFace, unsigned int indexSubFaceEdge) {
    if (s_incidenceConstraints.find(face.name()) == std::end(Face::s_incidenceConstraints)) {
        s_incidenceConstraints[face.name()] = "";
    }
    int b1 = static_cast<int>(indexParentEdge);
    int s1 = static_cast<int>(indexSubEdge);
    int s2 = static_cast<int>(indexSubFace);
    int b2 = static_cast<int>(indexSubFaceEdge);
    s_incidenceConstraints[face.name()] += "    " + face.name() + "(Bord('" + std::to_string(b1) + "') + Sub('" + std::to_string(s1) + "') + Permut('0'), Sub('" + std::to_string(s2) + "') + Bord('" + std::to_string(b2) + "'))\n";
}

he::Face* poly::Face::face() const {
    return this->m_face;
}
