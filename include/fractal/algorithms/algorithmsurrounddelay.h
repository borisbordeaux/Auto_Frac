#ifndef AUTOFRAC_ALGORITHMSURROUNDDELAY_H
#define AUTOFRAC_ALGORITHMSURROUNDDELAY_H

#include <vector>
#include "fractal/face.h"
#include "fractal/volume.h"

namespace frac::LinksSurroundDelay {

std::vector<frac::Face> subdivide(frac::Face const& face);

std::vector<frac::Volume> subdivide(frac::Volume const& volume);

}

#endif //AUTOFRAC_ALGORITHMSURROUNDDELAY_H
