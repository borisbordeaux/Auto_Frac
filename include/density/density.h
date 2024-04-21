#ifndef AUTOFRAC_DENSITY_H
#define AUTOFRAC_DENSITY_H

class QString;

namespace cv {
class Mat;
}


namespace frac {
void computeDensity(QString const& file, int value, bool showAllImages);

void computeDensity(cv::Mat const& img, int size, bool showAllImages);
}

#endif //AUTOFRAC_DENSITY_H
