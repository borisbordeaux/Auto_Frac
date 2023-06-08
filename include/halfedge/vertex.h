#ifndef AUTOFRAC_HE_VERTEX_H
#define AUTOFRAC_HE_VERTEX_H

#include <QString>

namespace he {

class HalfEdge;

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
    float x() const;

    /**
     * @brief setter
     * @param x the x value of the vertex
     */
    void setX(float x);

    /**
     * @brief getter
     * @return the y value of the vertex
     */
    float y() const;

    /**
     * @brief setter
     * @param y the y value of the vertex
     */
    void setY(float y);

    /**
     * @brief getter
     * @return the z value of the vertex
     */
    float z() const;

    /**
     * @brief setter
     * @param z the z value of the vertex
     */
    void setZ(float z);

    /**
     * @brief getter
     * @return a half-edge from which this point is its origin
     */
    he::HalfEdge* halfEdge();

    /**
     * @brief setter
     * @param halfEdge a half-edge that have this point as origin
     */
    void setHalfEdge(he::HalfEdge* halfEdge);

    /**
     * @brief getter
     * @return the name of this vertex
     */
    QString name() const;

    /**
     * @brief setter
     * @param name the name to set to this vertex
     */
    void setName(const QString& name);

    /**
     * @brief tests if the vertices are at the same position
     * @param other the vertex that has to be tested
     * @return true if the vertices has the same position, false otherwise
     */
    bool equals(Vertex* other) const;

private:
    //coordinates of this vertex
    float m_x, m_y, m_z;
    //a half-edge from which this point is its origin
    he::HalfEdge* m_halfEdge;
    //name of the vertex
    QString m_name;
};

} // poly

#endif //AUTOFRAC_HE_VERTEX_H
