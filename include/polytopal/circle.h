#ifndef AUTOFRAC_CIRCLE_H
#define AUTOFRAC_CIRCLE_H

#include <QVector3D>

namespace poly {

class Circle {
public:
    Circle(QVector3D const& center, float radius, QVector3D const& axisX = { 1, 0, 0 }, QVector3D const& axisY = { 0, 1, 0 }, Circle const* inversionCircle = nullptr);
    Circle(QVector3D const& center, float radius, Circle const* inversionCircle);
    Circle(QVector3D const& P1, QVector3D const& P2, QVector3D const& P3, Circle const* inversionCircle = nullptr);
    Circle(float e1, float e2, float e4, float e5, Circle const* inversionCircle = nullptr);
    const QVector3D& center() const;
    const QVector3D& axisX() const;
    const QVector3D& axisY() const;
    float radius() const;
    void setCenter(QVector3D const& center);
    void setRadius(float radius);
    void setAxisX(QVector3D const& axisX);
    void setAxisY(QVector3D const& axisY);
    void from3Points(QVector3D const& P1, QVector3D const& P2, QVector3D const& P3);

    void setInversionCircle(Circle const* inversionCircle);
    Circle const* inversionCircle() const;

    static float scalarProduct(Circle const& c1, Circle const& c2);
    bool static areOrthogonalCircles(Circle const& c1, Circle const& c2);

    void setOldCircleBeforeInversion(Circle const& oldCircle);
    Circle oldCircleBeforeInversion() const;

    void setNewCircleAfterInversion(Circle const& newCircle);
    Circle newCircleAfterInversion() const;

    void setInvertedValues();

    void setColor(QVector3D const& color);
    QVector3D const& color() const;

    static Circle inverse(Circle const& inverted, Circle const& inverter);
    Circle inverseStereographicProject() const;
    void updateR3Coord();
    void initInversiveCoordinates();

private:
    Circle operator*(float rhs) const;
    Circle operator-(Circle const& rhs) const;

private:
    QVector3D m_center;
    float m_radius;
    QVector3D m_axisX;
    QVector3D m_axisY;

    Circle const* m_inversionCircle;

    //for animation
    QVector3D m_oldCenter;
    float m_oldRadius = 0.0f;

    QVector3D m_newCenter;
    float m_newRadius = 0.0f;

    //color of circle
    QVector3D m_color = {0,0,0};

    //inversive coordinates
    float m_e1 = 0.0f;
    float m_e2 = 0.0f;
    float m_e4 = 0.0f;
    float m_e5 = 0.0f;
};

} // poly

#endif //AUTOFRAC_CIRCLE_H
