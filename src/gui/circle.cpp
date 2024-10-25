#include <QMatrix4x4>
#include "gui/circle.h"
#include "polytopal/inversivecoordinates.h"

Circle::Circle(QVector3D const& center, float radius, QVector3D const& axisX, QVector3D const& axisY) :
        m_center(center), m_radius(radius), m_axisX(axisX), m_axisY(axisY) {}

Circle::Circle(QVector3D const& P1, QVector3D const& P2, QVector3D const& P3) {
    //find new base
    m_axisX = (P2 - P1).normalized();
    QVector3D vecP1P3 = P3 - P1;
    QVector3D axisZ = QVector3D::crossProduct(m_axisX, vecP1P3).normalized();
    m_axisY = QVector3D::crossProduct(axisZ, m_axisX);
    //canonic base B = { (1,0,0),  (0,1,0),  (0,0,1) }    and     B' = { axisX, axisY, axisZ }
    QMatrix4x4 P { m_axisX.x(), m_axisY.x(), axisZ.x(), 0,
                   m_axisX.y(), m_axisY.y(), axisZ.y(), 0,
                   m_axisX.z(), m_axisY.z(), axisZ.z(), 0,
                   0, 0, 0, 1 };

    QMatrix4x4 P_inv = P.inverted();

    QVector4D A = P_inv * QVector4D(P1, 1.0f);
    QVector4D B = P_inv * QVector4D(P2, 1.0f);
    QVector4D C = P_inv * QVector4D(P3, 1.0f);

    //after change of basis
    float denom = 2.0f * (C.x() * (A.y() - B.y()) + A.x() * (B.y() - C.y()) + B.x() * (C.y() - A.y()));
    m_center.setX((C.x() * C.x() * (A.y() - B.y()) + (B.y() - C.y()) * (A.x() * A.x() + (A.y() - B.y()) * (A.y() - C.y())) + B.x() * B.x() * (C.y() - A.y())) / denom);
    m_center.setY((-B.x() * B.x() * C.x() + A.x() * A.x() * (C.x() - B.x()) + C.x() * (A.y() * A.y() - B.y() * B.y()) + A.x() * (B.x() * B.x() - C.x() * C.x() + B.y() * B.y() - C.y() * C.y()) + B.x() * (C.x() * C.x() - A.y() * A.y() + C.y() * C.y())) / denom);
    m_center.setZ(A.z());

    //works because both basis are orthonormal
    m_radius = (m_center - A.toVector3D()).length();

    //change of basis to be in 3D
    m_center = (P * QVector4D(m_center, 1.0f)).toVector3D();
}

Circle::Circle(poly::InversiveCoordinates const& invCoord) :
        Circle({ static_cast<float>(invCoord.e1() / (invCoord.e4() - invCoord.e3())),
                 static_cast<float>(invCoord.e2() / (invCoord.e4() - invCoord.e3())),
                 0.0f },
               static_cast<float>(qAbs(1.0 / (invCoord.e4() - invCoord.e3())))) {}

poly::InversiveCoordinates Circle::getInversiveCoordinates() const {
    double K = 1.0 / m_radius;
    double e1 = K * m_center.x();
    double e2 = K * m_center.y();
    double e3 = 0.5 * (K * m_center.lengthSquared() - m_radius - K);
    double e4 = 0.5 * (K * m_center.lengthSquared() - m_radius + K);
    return { e1, e2, e3, e4 };
}

void Circle::setColor(const QVector3D& color) {
    m_color = color;
}

QVector3D const& Circle::color() const {
    return m_color;
}
