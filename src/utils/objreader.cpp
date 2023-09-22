#include "utils/objreader.h"

#include "halfedge/mesh.h"
#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

#include "graph/incidencegraph.h"
#include "graph/vertex.h"

#include <QString>
#include <QFile>
#include <QTextStream>

void he::reader::readOBJ(QString const& filename, he::Mesh& mesh) {
    QFile file(filename);

    //open the file
    if (file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        //we read the file line by line
        QTextStream stream(&file);
        QString line;

        //until the end of the file
        while (!stream.atEnd()) {
            //read the line
            line = stream.readLine();
            //split with a space
            QStringList list = line.split(" ");

            //if it is a vertex (with 3 coordinates)
            if (list.size() == 4 && !list[0].compare("v")) {
                //create the vertex
                auto* v = new he::Vertex(list[1].toFloat(), list[2].toFloat(), list[3].toFloat(), QString::number(mesh.vertices().size() + 1));
                //and append it to the mesh
                mesh.append(v);
            } else {
                //if it is a face, it contains at least 3 vertices
                if (list.size() > 3 && !list[0].compare("f")) {
                    //we create the face
                    auto* f = new he::Face(QString::number(mesh.faces().size()));

                    //for each vertex of the face
                    for (int i = 1; i < list.size(); i++) {
                        //get the unique name of the half-edge
                        //for instance a half-edge between vertex 0 and 3 will be named "0 3"
                        int next = (i == list.size() - 1 ? 1 : i + 1);
                        QString name = list[i] + " " + list[next];

                        //we find the half-edge using its unique name
                        he::HalfEdge* he = mesh.findByName(name);

                        //if the half-edge doesn't exist
                        if (he == nullptr) {
                            //we create it
                            he = new he::HalfEdge(mesh.vertices()[list[i].toInt() - 1], name);
                            //we update the vertex
                            mesh.vertices()[list[i].toInt() - 1]->setHalfEdge(he);
                            //we append the half-edge
                            mesh.append(he);

                            //twin of the half-edge
                            //get its name
                            name = list[next] + " " + list[i];
                            //create it
                            auto* twinHe = new he::HalfEdge(mesh.vertices()[list[next].toInt() - 1], name);
                            //update the vertex
                            mesh.vertices()[list[next].toInt() - 1]->setHalfEdge(twinHe);
                            //append the half-edge
                            mesh.append(twinHe);
                            //set the twin for both half-edges
                            twinHe->setTwin(he);
                            he->setTwin(twinHe);
                        }

                        f->setHalfEdge(he);
                        he->setFace(f);
                    }

                    mesh.append(f);
                }
            }
        }

        file.close();

        //half-edge data completion
        for (he::HalfEdge* he: mesh.halfEdges()) {
            //find for next half-edge
            QString name = he->name();
            QString nextBeginName = name.split(" ")[1];

            if (mesh.vertices()[nextBeginName.toInt() - 1]->halfEdge()->face() == he->face()) {
                he->setNext(mesh.vertices()[nextBeginName.toInt() - 1]->halfEdge());
                mesh.vertices()[nextBeginName.toInt() - 1]->halfEdge()->setPrev(he);
            }

            for (he::HalfEdge* otherHalfEdge: mesh.vertices()[nextBeginName.toInt() - 1]->otherHalfEdges()) {
                if (otherHalfEdge->face() == he->face()) {
                    he->setNext(otherHalfEdge);
                    otherHalfEdge->setPrev(he);
                }
            }
        }
    }
}

void graph::reader::readOBJ4(const QString& filename, graph::IncidenceGraph& g) {
    QFile file(filename);

    //open the file
    if (file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        //we read the file line by line
        QTextStream stream(&file);
        QString line;

        //until the end of the file
        while (!stream.atEnd()) {
            //read the line
            line = stream.readLine();
            //split with a space
            QStringList list = line.split(" ");

            //if it is a face, it contains at least 3 vertices
            if (!list[0].compare("f")) {
                //we create the face
                auto* f = new graph::Vertex(std::to_string(g.getFacesSize() + 1));
                g.addFace(f);

                //for each vertex of the face
                for (int i = 1; i < list.size(); i++) {
                    //create vertices
                    graph::Vertex* v1 = g.findVertexByName(list[i].toStdString());
                    if (v1 == nullptr) {
                        v1 = new graph::Vertex(list[i].toStdString());
                        g.addVertex(v1);
                    }

                    int next = (i == list.size() - 1 ? 1 : i + 1);

                    graph::Vertex* v2 = g.findVertexByName(list[next].toStdString());
                    if (v2 == nullptr) {
                        v2 = new graph::Vertex(std::to_string(g.getVerticesSize() + 1));
                        g.addVertex(v2);
                    }

                    //get the name of the edge
                    //an edge between vertex 0 and 3 will be named "0 3"
                    QString name = list[i].toInt() < list[next].toInt() ? list[i] + " " + list[next] : list[next] + " " + list[i];

                    //create edge
                    graph::Vertex* edge = g.findEdgeByName(name.toStdString());
                    if (edge == nullptr) {
                        edge = new graph::Vertex(name.toStdString());
                        g.addEdge(edge);
                        v1->addParent(edge);
                        v2->addParent(edge);
                        if (list[i].toInt() < list[next].toInt()) {
                            edge->addChild(v1);
                            edge->addChild(v2);
                        } else {
                            edge->addChild(v2);
                            edge->addChild(v1);
                        }
                    }

                    edge->addParent(f);
                    f->addChild(edge);
                }
            }
            // if it  is a volume
            if (!list[0].compare("v")) {
                auto* vol = new graph::Vertex(std::to_string(g.getVolumesSize() + 1));
                g.addVolume(vol);

                //for each face of the volume
                for (int i = 1; i < list.size(); i++) {
                    graph::Vertex* face = g.getFaces()[list[i].toULong() - 1];
                    vol->addChild(face);
                    face->addParent(vol);
                }
            }
        }
        file.close();
        g.sortVertices();
    }
}
