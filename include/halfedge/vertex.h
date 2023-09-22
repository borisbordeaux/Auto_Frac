#ifndef AUTOFRAC_HE_VERTEX_H
#define AUTOFRAC_HE_VERTEX_H

#include <QString>
#include <QVector>

namespace he {

class HalfEdge;

class Face;

class Vertex {
public:
    /**
	 * @brief Construct a Vertex with its 3 params
	 * @param x the x value of the vertex
	 * @param y the y value of the vertex
	 * @param z the z value of the vertex
	 */
    Vertex(float x, float y, float z, QString name = "");

    /**
     * @brief getter
     * @return the x value of the vertex
     */
    [[nodiscard]] float x() const;

    /**
     * @brief setter
     * @param x the x value of the vertex
     */
    [[maybe_unused]] void setX(float x);

    /**
     * @brief getter
     * @return the y value of the vertex
     */
    [[nodiscard]] float y() const;

    /**
     * @brief setter
     * @param y the y value of the vertex
     */
    [[maybe_unused]] void setY(float y);

    /**
     * @brief getter
     * @return the z value of the vertex
     */
    [[nodiscard]] float z() const;

    /**
     * @brief setter
     * @param z the z value of the vertex
     */
    [[maybe_unused]] void setZ(float z);

    /**
     * @brief getter
     * @return a half-edge from which this point is its origin
     */
    [[maybe_unused]] he::HalfEdge* halfEdge();

    /**
     * @brief setter
     * @param halfEdge a half-edge that have this point as origin
     */
    void setHalfEdge(he::HalfEdge* halfEdge);

    /**
     * @brief getter
     * @return the name of this vertex
     */
    [[nodiscard]] QString name() const;

    [[nodiscard]] std::size_t degree() const;

    [[nodiscard]] std::vector<he::Face*> getAllFacesAroundVertex(he::Face* f) const;

    void addHalfEdge(he::HalfEdge* halfEdge);
    QVector<he::HalfEdge*>& otherHalfEdges();


private:
    //coordinates of this vertex
    float m_x, m_y, m_z;
    //a half-edge from which this point is the origin
    he::HalfEdge* m_halfEdge;
    //all other half-edges from which this point is the origin
    QVector<he::HalfEdge*> m_otherHalfEdges;
    //name of the vertex
    QString m_name;
};

} // poly

#endif //AUTOFRAC_HE_VERTEX_H
