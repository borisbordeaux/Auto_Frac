#ifndef AUTOFRAC_CIRCLE_H
#define AUTOFRAC_CIRCLE_H

#include <QVector3D>

namespace poly {

class Circle {
public:
    Circle(QVector3D const& center, QVector3D const& axisX, QVector3D const& axisY, float radius);
    Circle(QVector3D const& A, QVector3D const& B, QVector3D const& C);
    const QVector3D& center() const;
    const QVector3D& axisX() const;
    const QVector3D& axisY() const;
    float radius() const;
private:
    QVector3D m_center;
    QVector3D m_axisX;
    QVector3D m_axisY;
    float m_radius;
};

} // poly

#endif //AUTOFRAC_CIRCLE_H
