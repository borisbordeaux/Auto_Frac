#include "algorithm.h"

#include "halfedge/mesh.h"
#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

void he::algo::barycentricSubdivision(he::Mesh& mesh) {
    //for each face, create a new vertex at the center
    std::unordered_map<he::Face*, he::Vertex*> vertexOfFace;
    for (he::Face* f: mesh.faces()) {
        he::Vertex* v = new he::Vertex(f->barycenter());
        //mesh.append(v);
        vertexOfFace[f] = v;
    }

    //for each halfedge, create a new vertex at the middle
    for (he::HalfEdge* he: mesh.halfEdgesNoTwin()) {
        //old halfedges
        he::HalfEdge* heNext = he->next();
        he::HalfEdge* heTwin = he->twin();
        he::HalfEdge* heTwinPrev = he->twin()->prev();

        //new vertex at the middle
        QVector3D middle = (he->origin()->pos() + he->next()->origin()->pos()) / 2.0f;
        he::Vertex* v = new he::Vertex(middle);
        mesh.append(v);

        //new halfedges
        he::HalfEdge* newHeNext = new he::HalfEdge(v);
        he::HalfEdge* newHeNextTwin = new he::HalfEdge(he->next()->origin());

        he->setNext(newHeNext);

        newHeNext->setFace(he->face());
        newHeNext->setTwin(newHeNextTwin);
        newHeNext->setPrev(he);
        newHeNext->setNext(heNext);

        heNext->setPrev(newHeNext);

        heTwin->setPrev(newHeNextTwin);
        heTwin->setOrigin(v);

        newHeNextTwin->setFace(heTwin->face());
        newHeNextTwin->setTwin(newHeNext);
        newHeNextTwin->setPrev(heTwinPrev);
        newHeNextTwin->setNext(heTwin);

        mesh.append(heNext);
        mesh.append(newHeNextTwin);
        return;
    }
    //for each created halfedge, create a new face
}
