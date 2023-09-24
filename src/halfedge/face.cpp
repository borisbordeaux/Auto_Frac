#include <vector>
#include <QMatrix4x4>

#include "halfedge/face.h"
#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"

he::Face::Face(QString name, he::HalfEdge* halfEdge) : m_name(std::move(name)), m_halfEdge(halfEdge) {}

he::HalfEdge* he::Face::halfEdge() {
    return m_halfEdge;
}

void he::Face::setHalfEdge(he::HalfEdge* halfEdge) {
    m_halfEdge = halfEdge;
}

QString he::Face::name() const {
    return m_name;
}

QVector3D he::Face::computeNormal() {
    //take 3 points of the face
    QVector3D p1 = this->halfEdge()->origin()->pos();
    QVector3D p2 = this->halfEdge()->next()->origin()->pos();
    QVector3D p3 = this->halfEdge()->next()->next()->origin()->pos();

    //then compute the normal of the vectors created using the taken points
    return QVector3D::normal(QVector3D(p2.x() - p1.x(), p2.y() - p1.y(), p2.z() - p1.z()),
                             QVector3D(p3.x() - p2.x(), p3.y() - p2.y(), p3.z() - p2.z()));
}

std::size_t he::Face::nbEdges() const {
    std::size_t res = 0;

    he::HalfEdge* he = this->m_halfEdge;
    he::HalfEdge* heNxt = he;
    do {
        res++;
        heNxt = heNxt->next();
    } while (heNxt != he);

    return res;
}

float he::Face::area() {
    // compute the new basis
    QVector3D axeX = (m_halfEdge->next()->origin()->pos() - m_halfEdge->origin()->pos()).normalized();
    QVector3D axeZ = this->computeNormal();
    QVector3D axeY = QVector3D::crossProduct(axeZ, axeX);

    // row major order
    QMatrix4x4 invTransMat = QMatrix4x4(axeX.x(), axeY.x(), axeZ.x(), 0,
                                        axeX.y(), axeY.y(), axeZ.y(), 0,
                                        axeX.z(), axeY.z(), axeZ.z(), 0,
                                        0, 0, 0, 1).inverted();

    float res = 0.0f;
    he::HalfEdge* he = this->m_halfEdge;
    he::HalfEdge* heNxt = he;
    do {
        QVector4D p1 = invTransMat * QVector4D(heNxt->origin()->pos(), 1.0f);
        QVector4D p2 = invTransMat * QVector4D(heNxt->next()->origin()->pos(), 1.0f);
        res += p1.x() * p2.y() - p2.x() * p1.y();
        heNxt = heNxt->next();
    } while (heNxt != he);

    return res / 2.0f;
}
