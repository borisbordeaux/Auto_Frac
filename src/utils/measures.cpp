#include "utils/measures.h"
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui.hpp>

namespace frac::utils {
std::vector<std::pair<int, int>> computeFractalDimension(cv::Mat const& img) {
    int iter = 1;
    std::vector<std::pair<int, int>> result;
    //define max size
    int maxSize = img.size().width;
    while (maxSize > 1) {
        maxSize /= 2;
        iter *= 2;
        //compute number of squares overlapping the fractal
        int nbOverlappingSquares = 0;
        for (int i = 0; i < iter; i++) {
            for (int j = 0; j < iter; j++) {
                cv::Range rangeX { i * maxSize, (i + 1) * maxSize };
                cv::Range rangeY { j * maxSize, (j + 1) * maxSize };

                cv::Mat sub = img(rangeY, rangeX);

                bool coverForm = false;
                sub.forEach<cv::Point3_<uint8_t>>([&](cv::Point3_<uint8_t>& pixel, const int* /*position*/) -> void {
                    if (pixel.x != 0 || pixel.y != 0 || pixel.z != 0) {
                        coverForm = true;
                    }
                });
                if (coverForm) {
                    nbOverlappingSquares++;
                }

                /*if (iter == 2) {
                    cv::Rect rect { i * maxSize, j * maxSize, maxSize, maxSize };
                    cv::Mat copy;
                    img.copyTo(copy);
                    cv::rectangle(copy, rect, cv::Scalar(0, 255, 0));
                    cv::imshow("img " + std::to_string(iter) + "_" + std::to_string(i) + "_" + std::to_string(j), copy);
                }*/
            }
        }
        //save each number into a vector
        result.emplace_back(nbOverlappingSquares, maxSize);
    }

    return result;
}

int computeArea(const cv::Mat& img) {
    return cv::countNonZero(img);
}

int computePerimeter(const cv::Mat& img, std::string const& displayContoursWinName) {
    cv::Mat eroded;
    cv::Mat kernel = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(3, 3), cv::Point(1, 1));
    cv::erode(img, eroded, kernel, cv::Point(1, 1), 1, cv::BORDER_CONSTANT, cv::Scalar::all(0));
    cv::subtract(img, eroded, eroded);
    if (!displayContoursWinName.empty()) {
        cv::imshow(displayContoursWinName, eroded);
    }
    return cv::countNonZero(eroded);
}

std::pair<float, float> computeLinearRegression(std::vector<std::pair<float, float>> const& values) {
    float A = 0.0f;
    float B = 0.0f;

    float meanX = 0.0f;
    float meanY = 0.0f;

    for (auto const& val: values) {
        meanX += val.first;
        meanY += val.second;
    }

    meanX /= static_cast<float>(values.size());
    meanY /= static_cast<float>(values.size());

    float numerator = 0.0f;
    float denominator = 0.0f;

    for (auto const& val: values) {
        numerator += (val.first - meanX) * (val.second - meanY);
        denominator += (val.first - meanX) * (val.first - meanX);
    }

    A = numerator / denominator;
    B = meanY - A * meanX;

    return { A, B };
}

}

