#include "polytopal/inversivecoordinates.h"

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

double poly::InversiveCoordinates::e1() const {
    return m_e1;
}

double poly::InversiveCoordinates::e2() const {
    return m_e2;
}

double poly::InversiveCoordinates::e3() const {
    return m_e3;
}

double poly::InversiveCoordinates::e4() const {
    return m_e4;
}

poly::InversiveCoordinates::InversiveCoordinates(double e1, double e2, double e3, double e4) :
        m_e1(e1), m_e2(e2), m_e3(e3), m_e4(e4) {}

