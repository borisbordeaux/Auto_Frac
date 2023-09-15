#ifndef AUTOFRAC_MEASURES_H
#define AUTOFRAC_MEASURES_H

#include <vector>
#include <string>

namespace cv {
class Mat;
}

namespace frac::utils {

std::vector<int> computeFractalDimension(cv::Mat const& img);

int computeArea(cv::Mat const& img);

int computePerimeter(cv::Mat const& img, std::string const& displayContoursWinName);

/**
 * Compute linear regression (term A in equation y = Ax + B) <br/>
 * A = sum((xi - mean(x)) * (yi - mean(y))   /   sum((xi - mean(x))^2)) <br/>
 * B = mean(y) - A * mean(x)
 * @param values each x and y coordinates
 * @return the values A and B of the line equation
 */
template<typename T>
std::pair<T, T> computeLinearRegression(std::vector<std::pair<T, T>> const& values) {
    T A = 0.0f;
    T B = 0.0f;

    T meanX = 0.0f;
    T meanY = 0.0f;

    for (auto const& val: values) {
        meanX += val.first;
        meanY += val.second;
    }

    meanX /= static_cast<T>(values.size());
    meanY /= static_cast<T>(values.size());

    T numerator = 0.0f;
    T denominator = 0.0f;

    for (auto const& val: values) {
        numerator += (val.first - meanX) * (val.second - meanY);
        denominator += (val.first - meanX) * (val.first - meanX);
    }

    A = numerator / denominator;
    B = meanY - A * meanX;

    return { A, B };
}

void computeDensity(cv::Mat const& img, int size, bool showAllImages);
}

#endif //AUTOFRAC_MEASURES_H
