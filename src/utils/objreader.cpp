#include "utils/objreader.h"

#include "halfedge/mesh.h"
#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

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
                he::Vertex* v = new he::Vertex(list[1].toFloat(), list[2].toFloat(), list[3].toFloat(), QString::number(mesh.vertices().size() + 1));
                //and append it to the mesh
                mesh.append(v);
            } else {
                //if it is a face, it contains at least 3 vertices
                if (list.size() > 3 && !list[0].compare("f")) {
                    //we create the face
                    he::Face* f = new he::Face(QString::number(mesh.faces().size()));

                    //for each vertex of the face
                    for (int i = 1; i < list.size(); i++) {
                        //get the unique name of the half-edge
                        //a half-edge between vertex 0 and 3 will be named "0 3"
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
                            he::HalfEdge* twinHe = new he::HalfEdge(mesh.vertices()[list[next].toInt() - 1], name);
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

            for (int i = 1; i < mesh.vertices().size() + 1; i++) {
                he::HalfEdge* other = mesh.findByName(nextBeginName + " " + QString::number(i));

                if (other != nullptr && other->face() == he->face()) {
                    he->setNext(other);
                    other->setPrev(he);
                }
            }
        }
    }
}