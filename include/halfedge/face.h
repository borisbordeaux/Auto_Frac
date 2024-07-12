#ifndef AUTOFRAC_HE_FACE_H
#define AUTOFRAC_HE_FACE_H

#include <QString>
#include <QVector3D>

namespace he {

class HalfEdge;

class Face {
public:
    /**
     * @brief Construct a Face with one half-edge
     * @param halfEdge the half-edge the face will use
     */
    explicit Face(QString name = "", he::HalfEdge* halfEdge = nullptr);

    /**
     * @brief getter
     * @return the half-edge associated to this Face
     */
    he::HalfEdge* halfEdge();
    /**
     * @brief setter
     * @param halfEdge the half-edge that has to be
     * associated to this Face
     */
    void setHalfEdge(he::HalfEdge* halfEdge);

    /**
     * @brief getter
     * @return the name of this face
     */
    QString name() const;

    /**
	 * @brief compute the normal of the face
	 * @return the normalized normal of the face
	 */
    QVector3D computeNormal();

    std::size_t nbEdges() const;

    std::vector<he::HalfEdge*> allHalfEdges() const;

    float area();

    QVector3D barycenter() const;

    QString toString() const;

    QString userData() const;
    void setUserData(QString const& data);

private:
    QString m_name;
    he::HalfEdge* m_halfEdge;
    QString m_userData;
};

}

#endif //AUTOFRAC_HE_FACE_H
