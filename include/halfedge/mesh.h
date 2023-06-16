#ifndef AUTOFRAC_HE_MESH_H
#define AUTOFRAC_HE_MESH_H

#include <QMap>
#include <QString>
#include <vector>

namespace he {

class Vertex;

class HalfEdge;

class Face;

class Mesh {
public:
    Mesh() = default;
    ~Mesh();

    [[nodiscard]] std::vector<he::Vertex*> const& vertices() const;
    [[nodiscard]] std::vector<he::HalfEdge*> const& halfEdges() const;
    [[nodiscard]] std::vector<he::Face*> const& faces() const;

    void append(he::Vertex* v);
    void append(he::HalfEdge* he);
    void append(he::Face* f);
    he::HalfEdge* findByName(const QString& name);

    void reset();

    [[nodiscard]] QString toString() const;

private:
    std::vector<he::Vertex*> m_vertices;
    std::vector<he::HalfEdge*> m_halfEdges;
    std::vector<he::Face*> m_faces;

    //to enhance the finding of one half-edge by its name
    //we store each half-edge using their unique name
    QMap<QString, int> m_map;
};

} // poly

#endif //AUTOFRAC_HE_MESH_H
