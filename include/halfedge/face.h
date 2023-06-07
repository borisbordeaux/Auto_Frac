#ifndef AUTOFRAC_FACE_H
#define AUTOFRAC_FACE_H

#include <QString>

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
     * @brief setter
     * @param name the name to set to this face
     */
    void setName(const QString& name);

private:
    //the name of the face
    QString m_name;
    //the half-edge of the face
    he::HalfEdge* m_halfEdge;
};

}

#endif //AUTOFRAC_FACE_H
