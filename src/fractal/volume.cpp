//
// Created by boris on 07/02/24.
//

#include "fractal/volume.h"

namespace frac {
Volume::Volume(std::vector<frac::Face> faces) :
        m_faces(std::move(faces)) {}
} // frac