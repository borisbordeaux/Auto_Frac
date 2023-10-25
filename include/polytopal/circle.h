#ifndef AUTOFRAC_CIRCLE_H
#define AUTOFRAC_CIRCLE_H

#include <QVector3D>

namespace poly {

class Circle {
public:
    Circle(QVector3D const& center, float radius, QVector3D const& axisX = {1,0,0}, QVector3D const& axisY = {0,1,0});
    Circle(QVector3D const& A, QVector3D const& B, QVector3D const& C);
    const QVector3D& center() const;
    const QVector3D& axisX() const;
    const QVector3D& axisY() const;
    float radius() const;
private:
    QVector3D m_center;
    float m_radius;
    QVector3D m_axisX;
    QVector3D m_axisY;
};

} // poly

#endif //AUTOFRAC_CIRCLE_H
