#ifndef AUTOFRAC_INVERSIVECOORDINATES_H
#define AUTOFRAC_INVERSIVECOORDINATES_H

#include "circle.h"

namespace poly {
    class InversiveCoordinates {
    public:
        InversiveCoordinates(double e1, double e2, double e3, double e4);
        static double scalarProduct(InversiveCoordinates const& first, InversiveCoordinates const& second);
        static bool areOrthogonal(InversiveCoordinates const& first, InversiveCoordinates const& second);
        static InversiveCoordinates inverse(InversiveCoordinates const& inverted, InversiveCoordinates const& inverter);
        InversiveCoordinates operator*(double rhs) const;
        InversiveCoordinates operator-(InversiveCoordinates const& rhs) const;

        double e1() const;
        double e2() const;
        double e3() const;
        double e4() const;

    private:
        double m_e1;
        double m_e2;
        double m_e3;
        double m_e4;
    };
} //namespace poly

#endif //AUTOFRAC_INVERSIVECOORDINATES_H
