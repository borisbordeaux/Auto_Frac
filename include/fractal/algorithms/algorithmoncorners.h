#ifndef AUTOFRAC_ALGORITHMONCORNERS_H
#define AUTOFRAC_ALGORITHMONCORNERS_H

#include <vector>
#include "fractal/face.h"
#include "fractal/volume.h"

namespace frac::LinksOnCorners {

std::vector<frac::Face> subdivide(frac::Face const& face);

std::vector<frac::Volume> subdivide(frac::Volume const& volume);

}

#endif //AUTOFRAC_ALGORITHMONCORNERS_H
