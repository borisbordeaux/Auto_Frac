#ifndef AUTOFRAC_INVERSIVECOORDINATES_H
#define AUTOFRAC_INVERSIVECOORDINATES_H

#include "circle.h"

namespace poly {
    class InversiveCoordinates {
    public:
        explicit InversiveCoordinates(poly::Circle const& c);
        InversiveCoordinates(float e1, float e2, float e3, float e4, float e5);
        poly::Circle toCircle() const;
        static float scalarProduct(InversiveCoordinates const& first, InversiveCoordinates const& second);
        static bool areOrthogonal(InversiveCoordinates const& first, InversiveCoordinates const& second);
        static InversiveCoordinates inverse(InversiveCoordinates const& inverted, InversiveCoordinates const& inverter);
        InversiveCoordinates operator*(float rhs) const;
        InversiveCoordinates operator-(InversiveCoordinates const& rhs) const;

    private:
        float m_e1;
        float m_e2;
        float m_e3;
        float m_e4;
        float m_e5;
    };
} //namespace poly

#endif //AUTOFRAC_INVERSIVECOORDINATES_H
