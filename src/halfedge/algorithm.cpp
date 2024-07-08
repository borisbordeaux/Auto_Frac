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
            //faces (need to set the halfedge)
            subface1->setHalfEdge(newHe);
            subface2->setHalfEdge(he);

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

            if(firstHe){
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

void he::algo::generalizedBarycentricSubdivision(he::Mesh& mesh) {
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
            //faces (need to set the halfedge)
            subface1->setHalfEdge(newHe);
            subface2->setHalfEdge(he);

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

            if(firstHe){
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
