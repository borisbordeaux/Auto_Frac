#include <map>
#include "halfedge/algorithm.h"

#include "halfedge/mesh.h"
#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

void he::algo::barycentricSubdivision(he::Mesh& mesh) {
    std::map<he::HalfEdge*, he::Vertex*> middleVertexOfHalfEdge;
    std::vector<he::HalfEdge*> halfEdgesNeedDefineTwin;
    std::vector<he::Face*> faces = mesh.faces();

    for (he::Face* f: faces) {
        //create a new vertex at the center of the face
        he::Vertex* v = new he::Vertex(f->barycenter(), QString::number(mesh.vertices().size() + 1));
        mesh.append(v);

        std::vector<he::HalfEdge*> halfedges = f->allHalfEdges();
        bool firstHe = true;
        for (he::HalfEdge* he: halfedges) {
            he::Vertex* middle;
            //create a new middle vertex for the halfedge if it does not exist, or take the existent one
            if (middleVertexOfHalfEdge.find(he) == middleVertexOfHalfEdge.end()) {
                middle = new he::Vertex((he->origin()->pos() + he->next()->origin()->pos()) / 2.0f, QString::number(mesh.vertices().size() + 1));
                mesh.append(middle);
                middleVertexOfHalfEdge[he->twin()] = middle;
            } else {
                middle = middleVertexOfHalfEdge[he];
            }
            //create new halfedge before the current (CCW)
            he::HalfEdge* newHe = new he::HalfEdge(he->origin(), he->origin()->name() + " " + middle->name());
            mesh.append(newHe);

            //create new faces
            he::Face* subface1 = new he::Face(QString::number(mesh.faces().size()), newHe);
            mesh.append(subface1);

            he::Face* subface2;

            if (firstHe) {
                //reuse the current face
                subface2 = f;
            } else {
                //create new face
                subface2 = new he::Face(QString::number(mesh.faces().size()), he);
                mesh.append(subface2);
            }

            he::HalfEdge* rd = new he::HalfEdge(middle, middle->name() + " " + v->name());
            he::HalfEdge* ru = new he::HalfEdge(v, v->name() + " " + he->origin()->name());
            he::HalfEdge* ld = new he::HalfEdge(he->next()->origin(), he->next()->origin()->name() + " " + v->name());
            he::HalfEdge* lu = new he::HalfEdge(v, v->name() + " " + middle->name());
            mesh.append(rd);
            mesh.append(ru);
            mesh.append(ld);
            mesh.append(lu);

            //at this point, all elements have been added to the mesh
            //now we need to update the structures

            //vertices (need to set the halfedge)
            he->origin()->setHalfEdge(newHe);
            middle->setHalfEdge(he);
            he->next()->origin()->setHalfEdge(he->next());
            v->setHalfEdge(lu);

            //halfedges (need to set face, twin, prev and next)
            newHe->setFace(subface1);
            //twin will be done later since twin halfedge might not be created yet
            halfEdgesNeedDefineTwin.push_back(newHe);
            newHe->setPrev(ru);
            newHe->setNext(rd);
            rd->setFace(subface1);
            rd->setTwin(lu);
            rd->setPrev(newHe);
            rd->setNext(ru);
            ru->setFace(subface1);
            //twin will be done later since twin halfedge might not be created yet
            halfEdgesNeedDefineTwin.push_back(ru);
            ru->setPrev(rd);
            ru->setNext(newHe);
            lu->setFace(subface2);
            lu->setTwin(rd);
            lu->setPrev(ld);
            lu->setNext(he);
            ld->setFace(subface2);
            //twin will be done later since twin halfedge might not be created yet
            halfEdgesNeedDefineTwin.push_back(ld);
            ld->setPrev(he);
            ld->setNext(lu);

            if (firstHe) {
                he->prev()->setNext(newHe);
            }

            QString name = middle->name() + " " + ld->origin()->name();
            he->setName(name);
            he->setOrigin(middle);
            he->setFace(subface2);
            //twin will be done later since twin halfedge might not be created yet
            halfEdgesNeedDefineTwin.push_back(he);
            he->setPrev(lu);
            he->setNext(ld);

            firstHe = false;
        }
    }

    //correct twin for all halfedges
    for (he::HalfEdge* he: halfEdgesNeedDefineTwin) {
        QString name = he->next()->origin()->name() + " " + he->origin()->name();
        he::HalfEdge* twin = mesh.findByName(name, false);
        he->setTwin(twin);
    }

    mesh.updateHalfEdgeNotTwin();
}

namespace {
inline QVector3D coordOfPointOnLineAt(float t, QVector3D p0, QVector3D p1) {
    return { p0 * (1 - t) + p1 * t };
}
}

void he::algo::generalizedBarycentricSubdivision(he::Mesh& mesh) {
    std::map<he::HalfEdge*, std::vector<he::Vertex*>> middleVerticesOfHalfEdge;
    std::vector<he::HalfEdge*> halfEdgesNeedDefineTwin;
    std::vector<he::Face*> faces = mesh.faces();

    for (he::Face* f: faces) {
        //create a new vertex at the center of the face
        he::Vertex* v = new he::Vertex(f->barycenter(), QString::number(mesh.vertices().size() + 1));
        mesh.append(v);

        std::vector<he::HalfEdge*> halfedges = f->allHalfEdges();
        //useful to reuse the current face as a subface
        bool firstHe = true;

        for (he::HalfEdge* he: halfedges) {
            //for each halfedge, get its number of subdivision, 2 by default
            std::size_t nbSubs = he->userData().isEmpty() ? 2 : he->userData().toULong();

            std::vector<he::Face*> createdFaces;
            std::vector<he::HalfEdge*> createdHalfEdges;
            std::vector<he::Vertex*> createdVertices;

            bool verticesExists = middleVerticesOfHalfEdge.find(he) != middleVerticesOfHalfEdge.end();

            if (verticesExists) {
                for (he::Vertex* vertex: middleVerticesOfHalfEdge[he]) {
                    createdVertices.push_back(vertex); //ordered from begining to end of halfedge
                }
            } else {
                //create vertices between each subedge
                for (std::size_t i = 0; i < nbSubs - 1; i++) {
                    he::Vertex* vertex;
                    vertex = new he::Vertex(coordOfPointOnLineAt(static_cast<float>(i + 1) / static_cast<float>(nbSubs), he->origin()->pos(), he->next()->origin()->pos()), QString::number(mesh.vertices().size() + 1));
                    mesh.append(vertex);
                    createdVertices.push_back(vertex);
                }
                //add reverse ordered vertices to twin halfedge
                for (int j = static_cast<int>(createdVertices.size()) - 1; j >= 0; j--) {
                    middleVerticesOfHalfEdge[he->twin()].push_back(createdVertices[j]);
                }
            }

            //for each subdivision, create a halfedge
            //but reuse the current halfedge for last one
            for (std::size_t i = 0; i < nbSubs; i++) {
                if (i == nbSubs - 1) {
                    createdHalfEdges.push_back(he);
                } else {
                    he::Vertex* begin = i == 0 ? he->origin() : createdVertices[i - 1];
                    he::Vertex* end = createdVertices[i];
                    he::HalfEdge* halfEdge = new he::HalfEdge(begin, begin->name() + " " + end->name());
                    halfEdge->setUserData(he->userData());
                    createdHalfEdges.push_back(halfEdge);
                    mesh.append(halfEdge);
                }

                //for each subdivision, create a subface
                //reuse the current face if first subface and last halfedge
                if (firstHe && i == nbSubs - 1) {
                    createdFaces.push_back(f);
                } else {
                    he::Face* newFace = new Face(QString::number(mesh.faces().size()), createdHalfEdges[i]);
                    createdFaces.push_back(newFace);
                    mesh.append(newFace);
                }
            }

            //to facilitate update of the mesh, store for each created face the left and right halfedge
            std::map<he::Face*, std::pair<he::HalfEdge* /*left*/, he::HalfEdge* /*right*/>> heLAndROfFace;

            for (std::size_t i = 0; i < createdFaces.size(); i++) {
                //for each new face, create halfedges left and right
                he::Vertex* beginLeft = i == createdFaces.size() - 1 ? he->next()->origin() : createdVertices[i];
                he::Vertex* endRight = i == 0 ? he->origin() : createdVertices[i - 1];
                he::HalfEdge* left = new he::HalfEdge(beginLeft, beginLeft->name() + " " + v->name());
                he::HalfEdge* right = new he::HalfEdge(v, v->name() + " " + endRight->name());

                mesh.append(left);
                mesh.append(right);

                heLAndROfFace[createdFaces[i]] = { left, right };
            }

            //at this point, all elements have been added to the mesh
            //now we need to update the structures

            //vertices (need to set the halfedge)
            he->origin()->setHalfEdge(createdHalfEdges[0]);
            for (std::size_t i = 0; i < createdVertices.size(); i++) {
                he::HalfEdge* halfEdge = createdHalfEdges[i + 1];
                createdVertices[i]->setHalfEdge(halfEdge);
            }
            he->next()->origin()->setHalfEdge(he->twin());
            v->setHalfEdge(heLAndROfFace[createdFaces[0]].second);

            //halfedges (need to set face, twin, prev and next)
            //at first for created halfedges but not for the current halfedge (not the last created halfedge)
            for (std::size_t i = 0; i < createdHalfEdges.size() - 1; i++) {
                createdHalfEdges[i]->setFace(createdFaces[i]);
                //twin will be done later since twin halfedge might not be created yet
                halfEdgesNeedDefineTwin.push_back(createdHalfEdges[i]);
                createdHalfEdges[i]->setPrev(heLAndROfFace[createdFaces[i]].second);
                createdHalfEdges[i]->setNext(heLAndROfFace[createdFaces[i]].first);
            }
            //then for L and R halfedges of each face
            for (std::size_t i = 0; i < createdFaces.size(); i++) {
                //for L halfedges
                heLAndROfFace[createdFaces[i]].first->setFace(createdFaces[i]);
                if (i == nbSubs - 1) {
                    halfEdgesNeedDefineTwin.push_back(heLAndROfFace[createdFaces[i]].first);
                } else {
                    heLAndROfFace[createdFaces[i]].first->setTwin(heLAndROfFace[createdFaces[i + 1]].second);
                }
                heLAndROfFace[createdFaces[i]].first->setPrev(createdHalfEdges[i]);
                heLAndROfFace[createdFaces[i]].first->setNext(heLAndROfFace[createdFaces[i]].second);

                //for R halfedges
                heLAndROfFace[createdFaces[i]].second->setFace(createdFaces[i]);
                if (i == 0) {
                    halfEdgesNeedDefineTwin.push_back(heLAndROfFace[createdFaces[i]].second);
                } else {
                    heLAndROfFace[createdFaces[i]].second->setTwin(heLAndROfFace[createdFaces[i - 1]].first);
                }
                heLAndROfFace[createdFaces[i]].second->setPrev(heLAndROfFace[createdFaces[i]].first);
                heLAndROfFace[createdFaces[i]].second->setNext(createdHalfEdges[i]);
            }

            if (firstHe) {
                he->prev()->setNext(createdHalfEdges[0]);
            }

            //only prev and next of current halfedge are changed when there is 1 subdivision
            if (nbSubs != 1) {
                QString name = createdVertices[nbSubs - 2]->name() + " " + he->next()->origin()->name();
                he->setName(name);
                he->setOrigin(createdVertices[nbSubs - 2]);
                he->setFace(createdFaces[nbSubs - 1]);
                //twin will be done later since twin halfedge might not be created yet
                halfEdgesNeedDefineTwin.push_back(he);
            }
            he->setPrev(heLAndROfFace[createdFaces[nbSubs - 1]].second);
            he->setNext(heLAndROfFace[createdFaces[nbSubs - 1]].first);

            firstHe = false;
        }
    }

    //correct twin for all halfedges
    for (he::HalfEdge* he: halfEdgesNeedDefineTwin) {
        QString name = he->next()->origin()->name() + " " + he->origin()->name();
        he::HalfEdge* twin = mesh.findByName(name, false);
        he->setTwin(twin);
    }

    mesh.updateHalfEdgeNotTwin();
}
