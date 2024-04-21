#ifndef AUTOFRAC_FRACTALDIMENSION_H
#define AUTOFRAC_FRACTALDIMENSION_H

#include <vector>

namespace cv {
class Mat;
}

namespace frac {
std::vector<int> computeFractalDimension(cv::Mat const& img);
}

#endif //AUTOFRAC_FRACTALDIMENSION_H
