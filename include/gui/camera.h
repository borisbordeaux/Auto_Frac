#ifndef AUTOFRAC_CAMERA_H
#define AUTOFRAC_CAMERA_H

#include <QVector3D>
#include <QMatrix4x4>

class Camera {
public:
    Camera(QVector3D const& center, QVector3D const& upVector, float radius, float minRadius, float maxRadius, float azimuthAngle, float polarAngle);

    void rotateAzimuth(float radians);
    void rotatePolar(float radians);
    void zoom(float by);
    void zoom();
    void dezoom();

    void moveHorizontal(float distance);
    void moveVertical(float distance);

    QMatrix4x4 getViewMatrix() const;
    QVector3D getEye() const;
    QVector3D getNormalizedViewVector() const;

    void reset(QVector3D const& center, float radius, float azimuthAngle, float polarAngle);

private:
    QVector3D m_center; // Center of the orbit camera sphere (the point upon which the camera looks)
    QVector3D m_upVector; // Up vector of the camera
    float m_radius; // Radius of the orbit camera sphere
    float m_minRadius; // Minimal radius of the orbit camera sphere (cannot fall below this value)
    float m_maxRadius; // Maximal radius of the orbit camera sphere (cannot go beyond this value)
    float m_azimuthAngle; // Azimuth angle on the orbit camera sphere
    float m_polarAngle; // Polar angle on the orbit camera sphere
};

#endif //AUTOFRAC_CAMERA_H
