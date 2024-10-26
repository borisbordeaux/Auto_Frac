#ifndef AUTOFRAC_INVERSIVECOORDINATES_H
#define AUTOFRAC_INVERSIVECOORDINATES_H

#include "gui/circle.h"
#include "halfedge/point3d.h"

namespace poly {
class InversiveCoordinates {
public:
    InversiveCoordinates(double e1, double e2, double e3, double e4);
    explicit InversiveCoordinates(he::Point3D point);
    static double scalarProduct(InversiveCoordinates const& first, InversiveCoordinates const& second);
    static bool areOrthogonal(InversiveCoordinates const& first, InversiveCoordinates const& second);
    static bool areExternallyTangentCircles(InversiveCoordinates const& c1, InversiveCoordinates const& c2, double threshold);
    static he::Point3D tangencyPoint(InversiveCoordinates const& c1, InversiveCoordinates const& c2);
    static InversiveCoordinates inverse(InversiveCoordinates const& inverted, InversiveCoordinates const& inverter);
    InversiveCoordinates operator*(double rhs) const;
    InversiveCoordinates operator-(InversiveCoordinates const& rhs) const;
    gui::Circle inverseStereographicProject() const;
    gui::Circle toCircle() const;
    he::Point3D lightPoint() const;
    double radius() const;

    InversiveCoordinates const* inverter() const;
    void setInverter(InversiveCoordinates const* inverter);

private:
    double m_e1;
    double m_e2;
    double m_e3;
    double m_e4;

    InversiveCoordinates const* m_inverter;
};
} //namespace poly

#endif //AUTOFRAC_INVERSIVECOORDINATES_H
