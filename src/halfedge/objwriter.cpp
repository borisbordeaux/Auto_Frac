#include "halfedge/objwriter.h"
#include <QFile>
#include <QTextStream>
#include "halfedge/mesh.h"
#include "halfedge/vertex.h"
#include "halfedge/face.h"
#include "halfedge/halfedge.h"

void he::writer::writeOBJ(QString const& filename, he::Mesh const& mesh, bool usePreciseCoords) {
    QFile file(filename);

    //open the file
    if (file.open(QIODevice::WriteOnly | QIODevice::Text)) {
        //write the file using a stream
        QTextStream stream(&file);

        for (he::Vertex* v: mesh.vertices()) {
            if (usePreciseCoords) {
                he::Point3D pos = v->posD();
                stream << "v " << QString::number(pos.x(), 'g', 16) << " " << QString::number(pos.y(), 'g', 16) << " " << QString::number(pos.z(), 'g', 16) << Qt::endl;
            } else {
                QVector3D pos = v->pos();
                stream << "v " << QString::number(pos.x()) << " " << QString::number(pos.y()) << " " << QString::number(pos.z()) << Qt::endl;
            }
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
