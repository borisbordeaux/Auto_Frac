#ifndef AUTOFRAC_MEASURES_H
#define AUTOFRAC_MEASURES_H

#include <vector>
#include <string>

class QString;

namespace he {
class Mesh;
}

namespace cv {
class Mat;
}

namespace frac {

float computeArea(QString const& filename);
float computePerimeter(QString const& filename);

float computeArea(cv::Mat const& img);
float computeArea(he::Mesh const& mesh);

float computePerimeter(cv::Mat const& img);
float computePerimeter(he::Mesh const& mesh);

}

#endif //AUTOFRAC_MEASURES_H
