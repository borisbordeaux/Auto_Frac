#ifndef AUTOFRAC_ALGORITHMSURROUNDDELAYANDBEZIER_H
#define AUTOFRAC_ALGORITHMSURROUNDDELAYANDBEZIER_H

#include <vector>
#include "fractal/face.h"
#include "fractal/volume.h"

namespace frac::LinksSurroundDelayAndBezier {

std::vector<frac::Face> subdivide(frac::Face const& face);

std::vector<frac::Volume> subdivide(frac::Volume const& volume);

}

#endif //AUTOFRAC_ALGORITHMSURROUNDDELAYANDBEZIER_H
