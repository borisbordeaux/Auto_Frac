#include "gui/camera.h"

Camera::Camera(const QVector3D& center, const QVector3D& upVector, float radius, float minRadius, float maxRadius, float azimuthAngle, float polarAngle) :
        m_center(center), m_upVector(upVector), m_radius(radius), m_minRadius(minRadius), m_maxRadius(maxRadius), m_azimuthAngle(azimuthAngle), m_polarAngle(polarAngle) {}

void Camera::rotateAzimuth(const float radians) {
    m_azimuthAngle += radians;

    // Keep azimuth angle within range <0..2PI) - it's not necessary, just to have it nicely output
    const float fullCircle = 2.0f * 3.1415926f;
    m_azimuthAngle = fmodf(m_azimuthAngle, fullCircle);

    if (m_azimuthAngle < 0.0f) {
        m_azimuthAngle += fullCircle;
    }
}

void Camera::rotatePolar(const float radians) {
    m_polarAngle += radians;

    // Check if the angle hasn't exceeded quarter of a circle to prevent flip, add a bit of epsilon like 0.001 radians
    const float polarMaxCap = 3.1415926f / 2.0f - 0.001f;
    const float polarMinCap = -3.1415926f / 2.0f + 0.001f;

    if (m_polarAngle > polarMaxCap) {
        m_polarAngle = polarMaxCap;
    }

    if (m_polarAngle < polarMinCap) {
        m_polarAngle = polarMinCap;
    }
}

void Camera::zoom(const float by) {
    m_radius -= by;

    if (m_radius < m_minRadius) {
        m_radius = m_minRadius;
    }

    if (m_radius > m_maxRadius) {
        m_radius = m_maxRadius;
    }
}

void Camera::moveHorizontal(const float distance) {
    const QVector3D viewVector = getNormalizedViewVector();
    const QVector3D strafeVector = QVector3D::crossProduct(viewVector, m_upVector).normalized();
    m_center += strafeVector * distance;
}

void Camera::moveVertical(const float distance) {
    const QVector3D viewVector = getNormalizedViewVector();
    const QVector3D strafeVector = QVector3D::crossProduct(viewVector, m_upVector).normalized();
    const QVector3D upVector = QVector3D::crossProduct(strafeVector, viewVector).normalized();
    m_center += upVector * distance;
}

QMatrix4x4 Camera::getViewMatrix() const {
    QMatrix4x4 res;
    res.lookAt(getEye(), m_center, m_upVector);
    return res;
}

QVector3D Camera::getEye() const {
    // Calculate sines / cosines of angles
    const float sineAzimuth = std::sin(m_azimuthAngle);
    const float cosineAzimuth = std::cos(m_azimuthAngle);
    const float sinePolar = std::sin(m_polarAngle);
    const float cosinePolar = std::cos(m_polarAngle);

    // Calculate eye position out of them
    const float x = m_center.x() + m_radius * cosinePolar * cosineAzimuth;
    const float y = m_center.y() + m_radius * sinePolar;
    const float z = m_center.z() + m_radius * cosinePolar * sineAzimuth;

    return { x, y, z };
}

QVector3D Camera::getNormalizedViewVector() const {
    return (m_center - getEye()).normalized();
}

void Camera::reset(QVector3D const& center, float radius, float azimuthAngle, float polarAngle) {
    m_center = center;
    m_radius = radius;
    m_azimuthAngle = azimuthAngle;
    m_polarAngle = polarAngle;
}
