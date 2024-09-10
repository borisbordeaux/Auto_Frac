#ifndef AUTOFRAC_HE_VERTEX_H
#define AUTOFRAC_HE_VERTEX_H

#include <QString>
#include <QVector>
#include <QVector3D>
#include "point3d.h"

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

    explicit Vertex(QVector3D const& pos, QString name = "");

    /**
     * @brief getter
     * @return the position of this vertex
     */
    [[nodiscard]] QVector3D pos() const;

    /**
     * setter
     * @param pos the new position of the vertex
     */
    void setPos(QVector3D const& pos);

    /**
     * @brief getter
     * @return the precise position of this vertex
     */
    [[nodiscard]] Point3D posD() const;

    /**
     * setter
     * @param posD the new precise position of the vertex
     */
    void setPosD(Point3D const& posD);

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

    /**
     * @param f if given, the face to be in last
     * @return all faces around the vertex (ordered to have the given face in last if applicable)
     */
    [[nodiscard]] std::vector<he::Face*> getAllFacesAroundVertex(he::Face* f = nullptr) const;

    void addHalfEdge(he::HalfEdge* halfEdge);
    QVector<he::HalfEdge*>& otherHalfEdges();

    QString toString() const;

    QString userData() const;
    void setUserData(QString const& data);

private:
    //coordinates of this vertex
    QVector3D m_pos;
    //more precise coordinates of the vertex
    he::Point3D m_posD;
    //a half-edge from which this point is the origin
    he::HalfEdge* m_halfEdge;
    //all other half-edges from which this point is the origin
    QVector<he::HalfEdge*> m_otherHalfEdges;
    //name of the vertex
    QString m_name;
    //user data of the vertex
    QString m_userData;
};

} // poly

#endif //AUTOFRAC_HE_VERTEX_H
