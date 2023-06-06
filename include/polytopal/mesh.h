#ifndef AUTOFRAC_MESH_H
#define AUTOFRAC_MESH_H

#include <QMap>
#include <QString>
#include <QVector>

namespace poly {

class Vertex;

class HalfEdge;

class Face;

class Mesh {
public:
    Mesh();
    ~Mesh();

    QVector<Vertex*> vertices() const;
    QVector<HalfEdge*> halfEdges() const;
    QVector<Face*> faces() const;

    void append(Vertex* v);
    void append(HalfEdge* he);
    void append(Face* f);
    [[maybe_unused]] void remove(Vertex* v);
    [[maybe_unused]] void remove(HalfEdge* he);
    [[maybe_unused]] void remove(Face* f);
    HalfEdge* findByName(const QString& name);

    void reset();

    QString toString() const;

private:
    QVector<Vertex*> m_vertices;
    QVector<HalfEdge*> m_halfEdges;
    QVector<Face*> m_faces;

    //to enhance the finding of one half-edge by its name
    //we store each half-edge using their unique name
    QMap<QString, int> m_map;
};

} // poly

#endif //AUTOFRAC_MESH_H
