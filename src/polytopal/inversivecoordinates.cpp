#include "polytopal/inversivecoordinates.h"

#include "polytopal/circle.h"

poly::InversiveCoordinates::InversiveCoordinates(const poly::Circle& c) {
    //no lines for now
    float K = 1.0f / c.radius();
    m_e1 = K * c.center().x();
    m_e2 = K * c.center().y();
    m_e3 = K * c.center().z();
    m_e4 = 0.5f * (K * c.center().lengthSquared() - c.radius() - K);
    m_e5 = 0.5f * (K * c.center().lengthSquared() - c.radius() + K);
}

poly::InversiveCoordinates::InversiveCoordinates(float e1, float e2, float e3, float e4, float e5) : m_e1(e1), m_e2(e2), m_e3(e3), m_e4(e4), m_e5(e5) {}

poly::Circle poly::InversiveCoordinates::toCircle() const {
    float K = m_e5 - m_e4;
    return {{ m_e1 / K, m_e2 / K, m_e3 / K }, qAbs(1.0f / K) };
}

float poly::InversiveCoordinates::scalarProduct(poly::InversiveCoordinates const& first, poly::InversiveCoordinates const& second) {
    return first.m_e1 * second.m_e1 + first.m_e2 * second.m_e2 + first.m_e3 * second.m_e3 + first.m_e4 * second.m_e4 - first.m_e5 * second.m_e5;
}

bool poly::InversiveCoordinates::areOrthogonal(poly::InversiveCoordinates const& first, poly::InversiveCoordinates const& second) {
    return qAbs(scalarProduct(first, second)) < 0.01f;
}

poly::InversiveCoordinates poly::InversiveCoordinates::inverse(poly::InversiveCoordinates const& first, poly::InversiveCoordinates const& second) {
    return first - second * (2.0f * poly::InversiveCoordinates::scalarProduct(first, second));
    //float p = poly::InversiveCoordinates::scalarProduct(first, second);
    //return { first.m_e1 - 2.0f * p * second.m_e1, first.m_e2 - 2.0f * p * second.m_e2, first.m_e3 - 2.0f * p * second.m_e3, first.m_e4 - 2.0f * p * second.m_e4, first.m_e5 - 2.0f * p * second.m_e5 };
}

poly::InversiveCoordinates poly::InversiveCoordinates::operator*(float rhs) const {
    return { m_e1 * rhs, m_e2 * rhs, m_e3 * rhs, m_e4 * rhs, m_e5 * rhs };
}

poly::InversiveCoordinates poly::InversiveCoordinates::operator-(poly::InversiveCoordinates const& rhs) const {
    return { m_e1 - rhs.m_e1, m_e2 - rhs.m_e2, m_e3 - rhs.m_e3, m_e4 - rhs.m_e4, m_e5 - rhs.m_e5 };
}
