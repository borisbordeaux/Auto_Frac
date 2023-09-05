#ifndef AUTOFRAC_MEASURES_H
#define AUTOFRAC_MEASURES_H

#include <vector>
#include <string>

namespace cv {
class Mat;
}

namespace frac::utils {

std::vector<std::pair<int, int>> computeFractalDimension(cv::Mat const& img);

int computeArea(cv::Mat const& img);

int computePerimeter(cv::Mat const& img, std::string const& displayContoursWinName);

/**
 * Compute linear regression (term A in equation y = Ax + B) <br/>
 * A = sum((xi - mean(x)) * (yi - mean(y))   /   sum((xi - mean(x))^2)) <br/>
 * B = mean(y) - A * mean(x)
 * @param values each x and y coordinates
 * @return the values A and B of the line equation
 */
std::pair<float, float> computeLinearRegression(std::vector<std::pair<float, float>> const& values);

void computeDensity(cv::Mat const& img, int size, bool showAllImages);
}

#endif //AUTOFRAC_MEASURES_H
