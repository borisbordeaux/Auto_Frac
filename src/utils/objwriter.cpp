#include "utils/objwriter.h"
#include <QFile>
#include <QTextStream>
#include "halfedge/mesh.h"
#include "halfedge/vertex.h"
#include "halfedge/face.h"
#include "halfedge/halfedge.h"

void he::writer::writeOBJ(QString const& filename, he::Mesh const& mesh) {
    QFile file(filename);

    //open the file
    if (file.open(QIODevice::WriteOnly | QIODevice::Text)) {
        //write the file using a stream
        QTextStream stream(&file);

        for (he::Vertex* v: mesh.vertices()) {
            QVector3D pos = v->pos();
            stream << "v " << pos.x() << " " << pos.y() << " " << pos.z() << Qt::endl;
        }

        for (he::Face* f: mesh.faces()) {
            stream << "f";
            for (he::HalfEdge* he: f->allHalfEdges()) {
                stream << " " << mesh.indexOf(he->origin()).value_or(-1) + 1;
            }
            stream << Qt::endl;
        }

        file.close();
    }
}
