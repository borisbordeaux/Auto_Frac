#include "polytopal/structure.h"
#include <halfedge/face.h>
#include <halfedge/halfedge.h>
#include <polytopal/face.h>
#include <iostream>

poly::Structure::Structure(he::Mesh const& mesh, he::Face* face) : m_mesh(mesh), m_selectedFace(face) {
    poly::Face::s_mesh = &this->m_mesh;
    for (he::Face* f: m_mesh.faces()) {
        //for each selected polytopal face, build its fractal face
        this->m_faces.emplace_back(f);
    }
    //init adj constraints
    if (m_selectedFace == nullptr) {
        for (std::size_t i = 0; i < m_faces.size() - 1; ++i) { //for each fractal face
            for (std::size_t j = 0; j < m_faces[i].constData().size(); ++j) { //for each edge
                for (std::size_t k = i + 1; k < m_faces.size(); ++k) { //for each other face
                    if (i != k) {
                        for (std::size_t l = 0; l < m_faces[k].constData().size(); ++l) { //for each edge
                            if (m_faces[i].halfEdges()[j]->twin() == m_faces[k].halfEdges()[l]) {
                                addAdjacency(i, j, k, l);
                            }
                        }
                    }
                }
            }
        }
    }
}

std::string poly::Structure::adjacencies() const {
    return this->m_adj;
}

frac::UniqueVector<poly::Edge> poly::Structure::allEdges() const {
    frac::UniqueVector<poly::Edge> res;
    for (poly::Face const& f: this->m_faces) {
        for (poly::Edge const& e: f.constData()) {
            res.add(e);
        }
    }
    return res;
}

frac::UniqueVector<poly::Face> poly::Structure::allFaces() const {
    frac::UniqueVector<poly::Face> res;
    for (poly::Face const& f: this->m_faces) {
        res.add(f);
    }
    return res;
}

std::vector<poly::Face> poly::Structure::faces() const {
    if (m_selectedFace != nullptr) {
        for (poly::Face const& f: m_faces) {
            if (f.face() == m_selectedFace) {
                return { f };
            }
        }
    }
    return this->m_faces;
}

std::size_t poly::Structure::nbControlPointsOfFace(std::size_t indexFace) const {
    return 2 * this->m_faces[indexFace].len();
}

namespace poly {
std::ostream& operator<<(std::ostream& os, poly::Structure const& structure) {
    for (poly::Face const& f: structure.m_faces) {
        os << f << "\n";
    }
    os << structure.m_adj;
    return os;
}
}

poly::Face const& poly::Structure::operator[](std::size_t index) const {
    return m_faces[index];
}

void poly::Structure::addAdjacency(std::size_t indexFace1, std::size_t indexEdgeFace1, std::size_t indexFace2, std::size_t indexEdgeFace2) {
    this->m_adj += "    init(Sub('" + std::to_string(indexFace1) + "') + Bord('" + std::to_string(indexEdgeFace1) + "') + Bord('1'), Sub('" + std::to_string(indexFace2) + "') + Bord('" + std::to_string(indexEdgeFace2) + "') + Bord('1'))\n";
}