#ifndef AUTOFRAC_POINT3D_H
#define AUTOFRAC_POINT3D_H

#include <QVector3D>

namespace he {

class Point3D {
public:
    Point3D() = default;
    Point3D(double x, double y, double z);
    double x() const;
    void setX(double x);
    double y() const;
    void setY(double y);
    double z() const;
    void setZ(double z);

    QVector3D toQVector3D() const;

    void operator+=(Point3D const& other);
    void operator/=(double value);
    Point3D operator-(Point3D const& other) const;
    Point3D operator+(Point3D const& other) const;
    Point3D operator-() const;
    Point3D operator*(double value) const;

    static Point3D crossProduct(Point3D p1, Point3D p2);
    static double dotProduct(Point3D p1, Point3D p2);
    double lengthSquared() const;
    double length() const;
    void normalize();

private:
    double m_x;
    double m_y;
    double m_z;
};

} // he

#endif //AUTOFRAC_POINT3D_H
