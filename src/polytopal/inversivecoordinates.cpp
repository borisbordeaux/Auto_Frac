#include "polytopal/inversivecoordinates.h"

poly::InversiveCoordinates::InversiveCoordinates(double e1, double e2, double e3, double e4) :
        m_e1(e1), m_e2(e2), m_e3(e3), m_e4(e4), m_inverter(nullptr) {}

poly::InversiveCoordinates::InversiveCoordinates(he::Point3D point) :
        m_inverter(nullptr) {
    double coef = 1.0 / qSqrt(point.lengthSquared() - 1.0);
    m_e1 = coef * point.x();
    m_e2 = coef * point.y();
    m_e3 = coef * point.z();
    m_e4 = coef;
}

double poly::InversiveCoordinates::scalarProduct(poly::InversiveCoordinates const& first, poly::InversiveCoordinates const& second) {
    return first.m_e1 * second.m_e1 + first.m_e2 * second.m_e2 + first.m_e3 * second.m_e3 - first.m_e4 * second.m_e4;
}

bool poly::InversiveCoordinates::areOrthogonal(poly::InversiveCoordinates const& first, poly::InversiveCoordinates const& second) {
    return qAbs(scalarProduct(first, second)) < 0.01;
}

poly::InversiveCoordinates poly::InversiveCoordinates::inverse(poly::InversiveCoordinates const& inverted, poly::InversiveCoordinates const& inverter) {
    return inverted - inverter * (2.0 * poly::InversiveCoordinates::scalarProduct(inverted, inverter));
}

poly::InversiveCoordinates poly::InversiveCoordinates::operator*(double rhs) const {
    return { m_e1 * rhs, m_e2 * rhs, m_e3 * rhs, m_e4 * rhs };
}

poly::InversiveCoordinates poly::InversiveCoordinates::operator-(poly::InversiveCoordinates const& rhs) const {
    return { m_e1 - rhs.m_e1, m_e2 - rhs.m_e2, m_e3 - rhs.m_e3, m_e4 - rhs.m_e4 };
}

gui::Circle poly::InversiveCoordinates::inverseStereographicProject() const {
    //plan with equation ax + by + cz + d = 0 intersecting the sphere
    double a = m_e1;
    double b = m_e2;
    double c = m_e3;
    double d = -m_e4;

    //compute orthogonal projection of the origin on the plan
    double lambda = d / (a * a + b * b + c * c);
    he::Point3D H(-lambda * a, -lambda * b, -lambda * c);

    //squared distance of origin to plan
    double D_squared = H.lengthSquared();

    //radius of the circle
    double r = qSqrt(1.0 - D_squared);

    //normal of the plan
    he::Point3D n { a, b, c };
    n.normalize();

    //get an orthogonal vector
    he::Point3D xAxis { -b, a, 0 };
    if (qFuzzyIsNull(xAxis.lengthSquared())) {
        xAxis.setX(0);
        xAxis.setY(c);
        xAxis.setZ(0);
    }
    xAxis.normalize();

    //get a second orthogonal vector to have an orthonormal basis
    he::Point3D yAxis = he::Point3D::crossProduct(n, xAxis);

    //return the circle with the new axes
    gui::Circle res { H.toQVector3D(), static_cast<float>(r), xAxis.toQVector3D(), yAxis.toQVector3D() };
    return res;
}

poly::InversiveCoordinates const* poly::InversiveCoordinates::inverter() const {
    return m_inverter;
}

void poly::InversiveCoordinates::setInverter(poly::InversiveCoordinates const* inverter) {
    m_inverter = inverter;
}

he::Point3D poly::InversiveCoordinates::lightPoint() const {
    return { m_e1 / m_e4, m_e2 / m_e4, m_e3 / m_e4 };
}

bool poly::InversiveCoordinates::areExternallyTangentCircles(poly::InversiveCoordinates const& c1, poly::InversiveCoordinates const& c2, double threshold) {
    //with inversive coordinates, scalar product gives -1 if externally tangent
    return qAbs(scalarProduct(c1, c2) + 1.0) < threshold;
}

he::Point3D poly::InversiveCoordinates::tangencyPoint(poly::InversiveCoordinates const& c1, poly::InversiveCoordinates const& c2) {
    double x = (c1.m_e1 + c2.m_e1) / ((c1.m_e4 + c2.m_e4) - (c1.m_e3 + c2.m_e3));
    double y = (c1.m_e2 + c2.m_e2) / ((c1.m_e4 + c2.m_e4) - (c1.m_e3 + c2.m_e3));
    return { x, y, 0 };
}

gui::Circle poly::InversiveCoordinates::toCircle() const {
    return {{ static_cast<float>(m_e1 / (m_e4 - m_e3)),
              static_cast<float>(m_e2 / (m_e4 - m_e3)),
              0.0f },
            static_cast<float>(qAbs(1.0 / (m_e4 - m_e3))) };
}

double poly::InversiveCoordinates::radius() const {
    return 1.0 / (m_e4 - m_e3);
}
