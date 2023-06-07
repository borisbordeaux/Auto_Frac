#ifndef AUTOFRAC_HALFEDGE_H
#define AUTOFRAC_HALFEDGE_H

#include <QString>

namespace poly {

class Vertex;

class Face;

class HalfEdge {
public:
    /**
     * @brief Construct a half-edge with its origin
     * @param origin the origin of the half-edge
     */
    explicit HalfEdge(Vertex* origin, QString name = "");

    /**
     * @brief getter
     * @return the origin of the half-edge
     */
    Vertex* origin();

    /**
     * @brief setter
     * @param origin the origin to set for this half-edge
     */
    void setOrigin(Vertex* origin);

    /**
     * @brief getter
     * @return the face of this half-edge
     */
    Face* face();

    /**
     * @brief setter
     * @param face the face to set for this half-edge
     */
    void setFace(Face* face);

    /**
     * @brief getter
     * @return the twin half-edge of this half-edge
     */
    HalfEdge* twin();

    /**
     * @brief setter
     * @param twin the twin half-edge to be set for this half-edge
     */
    void setTwin(HalfEdge* twin);

    /**
     * @brief getter
     * @return the previous half-edge of this half-edge
     */
    HalfEdge* prev();

    /**
     * @brief setter
     * @param prev the previous half-edge to be set for this half-edge
     */
    void setPrev(HalfEdge* prev);

    /**
     * @brief getter
     * @return the next half-edge of this half-edge
     */
    HalfEdge* next();

    /**
     * @brief setter
     * @param next the next half-edge to be set for this half-edge
     */
    void setNext(HalfEdge* next);

    /**
     * @brief getter
     * @return the name of this half-edge, represented by the vertices
     * it bind, in the order origin -> next.origin
     */
    QString name() const;

    /**
     * @brief setter
     * @param name the name to be set for this half-edge
     */
    void setName(const QString& name);

private:
    Vertex* m_origin;
    Face* m_face;
    HalfEdge* m_twin;
    HalfEdge* m_prev;
    HalfEdge* m_next;
    QString m_name;
};

} // poly

#endif //AUTOFRAC_HALFEDGE_H
