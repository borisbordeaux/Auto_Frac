#ifndef AUTOFRAC_CIRCLE_H
#define AUTOFRAC_CIRCLE_H

#include <QVector3D>

namespace poly {
class InversiveCoordinates;
}

namespace gui {
class Circle {
public:
    Circle(QVector3D const& center, float radius, QVector3D const& axisX = { 1, 0, 0 }, QVector3D const& axisY = { 0, 1, 0 });
    Circle(QVector3D const& P1, QVector3D const& P2, QVector3D const& P3);

    poly::InversiveCoordinates getInversiveCoordinates() const;

    void setColor(QVector3D const& color);
    QVector3D const& color() const;

    QVector3D const& center() const;
    float radius() const;
    void setRadius(float radius);
    QVector3D const& axisX() const;
    QVector3D const& axisY() const;

private:
    QVector3D m_center;
    float m_radius;
    QVector3D m_axisX;
    QVector3D m_axisY;

    QVector3D m_color = { 0, 0, 0 };
};
} //namespace gui

#endif //AUTOFRAC_CIRCLE_H
