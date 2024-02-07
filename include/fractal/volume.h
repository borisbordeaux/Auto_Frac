#ifndef AUTOFRAC_VOLUME_H
#define AUTOFRAC_VOLUME_H

#include <vector>
#include "fractal/face.h"

namespace frac {

class Volume {
public:
    explicit Volume(std::vector<frac::Face> faces);

private:
    std::vector<frac::Face> m_faces; //sorted in a specific order
};

} // frac

#endif //AUTOFRAC_VOLUME_H
