#include "halfedge/point3d.h"

namespace he {
Point3D::Point3D(double x, double y, double z) :
        m_x(x), m_y(y), m_z(z) {}

double Point3D::x() const {
    return m_x;
}

void Point3D::setX(double x) {
    m_x = x;
}

double Point3D::y() const {
    return m_y;
}

void Point3D::setY(double y) {
    m_y = y;
}

double Point3D::z() const {
    return m_z;
}

void Point3D::setZ(double z) {
    m_z = z;
}

void Point3D::operator+=(Point3D const& other) {
    m_x += other.m_x;
    m_y += other.m_y;
    m_z += other.m_z;
}

void Point3D::operator/=(double value) {
    m_x /= value;
    m_y /= value;
    m_z /= value;
}

Point3D Point3D::operator-(Point3D const& other) const {
    return { m_x - other.m_x, m_y - other.m_y, m_z - other.m_z };
}

Point3D Point3D::operator+(Point3D const& other) const {
    return { m_x + other.m_x, m_y + other.m_y, m_z + other.m_z };
}

Point3D Point3D::crossProduct(Point3D p1, Point3D p2) {
    return { p1.m_y * p2.m_z - p1.m_z * p2.m_y,
             p1.m_z * p2.m_x - p1.m_x * p2.m_z,
             p1.m_x * p2.m_y - p1.m_y * p2.m_x };
}

QVector3D Point3D::toQVector3D() const {
    return { static_cast<float>(m_x), static_cast<float>(m_y), static_cast<float>(m_z) };
}

Point3D Point3D::operator*(double value) const {
    return { m_x * value, m_y * value, m_z * value };
}

Point3D Point3D::operator-() const {
    return { -m_x, -m_y, -m_z };
}

double Point3D::lengthSquared() const {
    return m_x * m_x + m_y * m_y + m_z * m_z;
}

double Point3D::length() const {
    return qSqrt(lengthSquared());
}

void Point3D::normalize() {
    double l = this->length();
    if (l > 0.000000001) {
        (*this) /= l;
    }
}

double Point3D::dotProduct(Point3D p1, Point3D p2) {
    return p1.m_x * p2.m_x + p1.m_y * p2.m_y + p1.m_z * p2.m_z;
}



} // he