#include <QMatrix4x4>
#include "polytopal/circle.h"

namespace poly {

Circle::Circle(QVector3D const& center, QVector3D const& axisX, QVector3D const& axisY, float radius) : m_center(center), m_axisX(axisX), m_axisY(axisY), m_radius(radius) {}

Circle::Circle(QVector3D const& P1, QVector3D const& P2, QVector3D const& P3) {
    //change of basis to be in 2D
    m_axisX = (P2 - P1).normalized();
    QVector3D P1P3 = P3 - P1;
    QVector3D axisZ = QVector3D::crossProduct(m_axisX, P1P3).normalized();
    m_axisY = QVector3D::crossProduct(axisZ, m_axisX).normalized();
    //B = base canonique ((1,0,0),  (0,1,0),  (0,0,1))    et     B' = (axisX, axisY, axisZ)
    QMatrix4x4 P { m_axisX.x(), m_axisY.x(), axisZ.x(), 0.0f,
                   m_axisX.y(), m_axisY.y(), axisZ.y(), 0.0f,
                   m_axisX.z(), m_axisY.z(), axisZ.z(), 0.0f,
                   0.0f, 0.0f, 0.0f, 1.0f };

    QMatrix4x4 P_inv = P.inverted();

    QVector3D A = (QVector4D(P1,1) * P_inv).toVector3D();
    QVector3D B = (QVector4D(P2,1) * P_inv).toVector3D();
    QVector3D C = (QVector4D(P3,1) * P_inv).toVector3D();
    qDebug() << "A = " << A;
    qDebug() << "B = " << B;
    qDebug() << "C = " << C;

    //after change of basis
    float denom = 2.0f * (C.x() * (A.y() - B.y()) + A.x() * (B.y() - C.y()) + B.x() * (C.y() - A.y()));
    m_center.setX((C.x() * C.x() * (A.y() - B.y()) + (B.y() - C.y()) * (A.x() * A.x() + (A.y() - B.y()) * (A.y() - C.y())) + B.x() * B.x() * (C.y() - A.y())) / denom);
    m_center.setY((-B.x() * B.x() * C.x() + A.x() * A.x() * (C.x() - B.x()) + C.x() * (A.y() * A.y() - B.y() * B.y()) + A.x() * (B.x() * B.x() - C.x() * C.x() + B.y() * B.y() - C.y() * C.y()) + B.x() * (C.x() * C.x() - A.y() * A.y() + C.y() * C.y())) / denom);
    m_center.setZ(0.0f);
    m_radius = (m_center - A).length();

    //change of basis to be in 3D
    m_center = (QVector4D(m_center,1) * P).toVector3D();
    qDebug() << "center is " << m_center;
}

const QVector3D& Circle::center() const {
    return m_center;
}

const QVector3D& Circle::axisX() const {
    return m_axisX;
}

const QVector3D& Circle::axisY() const {
    return m_axisY;
}

float Circle::radius() const {
    return m_radius;
}

} // poly