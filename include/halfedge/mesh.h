#ifndef AUTOFRAC_MESH_H
#define AUTOFRAC_MESH_H

#include <QMap>
#include <QString>
#include <QVector>

namespace he {

class Vertex;

class HalfEdge;

class Face;

class Mesh {
public:
    Mesh();
    ~Mesh();

    QVector<he::Vertex*> vertices() const;
    QVector<he::HalfEdge*> halfEdges() const;
    QVector<he::Face*> faces() const;

    void append(he::Vertex* v);
    void append(he::HalfEdge* he);
    void append(he::Face* f);
    [[maybe_unused]] void remove(he::Vertex* v);
    [[maybe_unused]] void remove(he::HalfEdge* he);
    [[maybe_unused]] void remove(he::Face* f);
    he::HalfEdge* findByName(const QString& name);

    void reset();

    QString toString() const;

private:
    QVector<he::Vertex*> m_vertices;
    QVector<he::HalfEdge*> m_halfEdges;
    QVector<he::Face*> m_faces;

    //to enhance the finding of one half-edge by its name
    //we store each half-edge using their unique name
    QMap<QString, int> m_map;
};

} // poly

#endif //AUTOFRAC_MESH_H
