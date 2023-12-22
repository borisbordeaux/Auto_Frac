#include <QMatrix4x4>
#include "polytopal/circle.h"

namespace poly {

Circle::Circle(QVector3D const& center, float radius, QVector3D const& axisX, QVector3D const& axisY, Circle const* inversionCircle) :
        m_center(center), m_radius(radius), m_axisX(axisX), m_axisY(axisY), m_inversionCircle(inversionCircle) {
    this->initInversiveCoordinates();
}

Circle::Circle(QVector3D const& center, float radius, Circle const* inversionCircle) :
        m_center(center), m_radius(radius), m_axisX(1, 0, 0), m_axisY(0, 1, 0), m_inversionCircle(inversionCircle) {
    this->initInversiveCoordinates();
}

Circle::Circle(QVector3D const& P1, QVector3D const& P2, QVector3D const& P3, Circle const* inversionCircle) :
        m_radius(0.0f), m_inversionCircle(inversionCircle) {
    from3Points(P1, P2, P3);
    this->initInversiveCoordinates();
}

Circle::Circle(float e1, float e2, float e4, float e5, const Circle* inversionCircle) :
        m_center(e1 / (e5 - e4), e2 / (e5 - e4), 0.0f),
        m_radius(qAbs(1.0f / (e5 - e4))),
        m_axisX(1, 0, 0), m_axisY(0, 1, 0),
        m_inversionCircle(inversionCircle),
        m_e1(e1), m_e2(e2), m_e4(e4), m_e5(e5) {}

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

bool Circle::areOrthogonalCircles(Circle const& c1, Circle const& c2) {
    //with inversive coordinates
    return qAbs(scalarProduct(c1, c2)) < 0.01f;
}

Circle const* Circle::inversionCircle() const {
    return m_inversionCircle;
}

void Circle::setInversionCircle(Circle const* inversionCircle) {
    m_inversionCircle = inversionCircle;
}

void Circle::setCenter(QVector3D const& center) {
    m_center = center;
}

void Circle::setRadius(float radius) {
    m_radius = radius;
}

void Circle::setAxisX(QVector3D const& axisX) {
    m_axisX = axisX;
}

void Circle::setAxisY(QVector3D const& axisY) {
    m_axisY = axisY;
}

void Circle::from3Points(QVector3D const& P1, QVector3D const& P2, QVector3D const& P3) {
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
    initInversiveCoordinates();
}

void Circle::setOldCircleBeforeInversion(Circle const& oldCircle) {
    m_oldCenter = oldCircle.center();
    m_oldRadius = oldCircle.radius();
}

Circle Circle::oldCircleBeforeInversion() const {
    Circle res { m_oldCenter, m_oldRadius };
    res.setColor(m_color);
    return res;
}

void Circle::setNewCircleAfterInversion(Circle const& newCircle) {
    m_newCenter = newCircle.center();
    m_newRadius = newCircle.radius();
}

Circle Circle::newCircleAfterInversion() const {
    Circle res { m_newCenter, m_newRadius };
    res.setColor(m_color);
    return res;
}

void Circle::setInvertedValues() {
    m_center = m_newCenter;
    m_radius = m_newRadius;
    this->initInversiveCoordinates();
}

void Circle::setColor(const QVector3D& color) {
    m_color = color;
}

QVector3D const& Circle::color() const {
    return m_color;
}

qsizetype Circle::numberOfSegments(float n) const {
    //n is the number of segment on the unit circle
    return qFloor(n * m_radius);
}

void Circle::initInversiveCoordinates() {
    float K = 1.0f / m_radius;
    m_e1 = K * m_center.x();
    m_e2 = K * m_center.y();
    m_e4 = 0.5f * (K * m_center.lengthSquared() - m_radius - K);
    m_e5 = 0.5f * (K * m_center.lengthSquared() - m_radius + K);
}

float Circle::scalarProduct(const Circle& c1, const Circle& c2) {
    return c1.m_e1 * c2.m_e1 + c1.m_e2 * c2.m_e2 + c1.m_e4 * c2.m_e4 - c1.m_e5 * c2.m_e5;
}

Circle Circle::operator-(const Circle& rhs) const {
    return { m_e1 - rhs.m_e1, m_e2 - rhs.m_e2, m_e4 - rhs.m_e4, m_e5 - rhs.m_e5 };
}

Circle Circle::operator*(float rhs) const {
    return { m_e1 * rhs, m_e2 * rhs, m_e4 * rhs, m_e5 * rhs };
}

Circle Circle::inverse(const Circle& inverted, const Circle& inverter) {
    return inverted - inverter * (2.0f * Circle::scalarProduct(inverted, inverter));
}

Circle Circle::inverseStereographicProject() const {
    float a = m_e1;
    float b = m_e2;
    float c = m_e4;
    float d = -m_e5;

    //compute orthogonal projection of the origin on the plan
    float lambda = d / (a * a + b * b + c * c);
    QVector3D H(-lambda * a, -lambda * b, -lambda * c);

    //squared distance of origin to plan
    float D_squared = H.lengthSquared();

    //radius of the circle
    float r = qSqrt(1.0f - D_squared);

    //normal of the plan
    QVector3D n { a, b, c };
    n.normalize();

    //get an orthogonal vector
    QVector3D xAxis { -b, a, 0 };
    if (qFuzzyIsNull(xAxis.lengthSquared())) {
        xAxis.setX(0);
        xAxis.setY(c);
        xAxis.setZ(0);
    }
    xAxis.normalize();

    //get a second orthogonal vector to have an orthonormal basis
    QVector3D yAxis = QVector3D::crossProduct(n, xAxis);

    //return the circle with the new axes
    return { H, r, xAxis, yAxis };
}

void Circle::updateR3Coord() {
    float K = m_e5 - m_e4;
    m_center = { m_e1 / K, m_e2 / K, 0.0f };
    m_radius = qAbs(1.0f / K);
    m_axisX = { 1, 0, 0 };
    m_axisY = { 0, 1, 0 };
}

} // poly