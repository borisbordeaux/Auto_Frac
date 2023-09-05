#include "utils/measures.h"
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <QVector3D>
#include <thread>

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

void normalizeMat(cv::Mat& img) {
    uchar max = *std::max_element(img.begin<uchar>(), img.end<uchar>());
    if (max < 255) {
        std::for_each(img.begin<uchar>(), img.end<uchar>(), [&](uchar& val) {
            val = (val * 255) / max;
        });
    }
}

void computeDensity(cv::Mat const& img, int size, bool showAllImages) {
    cv::Mat res;
    img.copyTo(res); //copy in order to have same size and type

    // use multithreading for this computation since it can take time
    // and can be done independently for each pixel
    unsigned int nb_thread = std::thread::hardware_concurrency();

    auto f = [&](unsigned int idxThread) {
        // each thread handles the image cut in vertical parts
        // hence the width is determined by the number of thread
        int width = img.cols / static_cast<int>(nb_thread);
        // the last thread can handle a larger width than the others
        // but always strictly shorter than twice the width
        int realWidth = idxThread < nb_thread - 1 ? width : img.cols - static_cast<int>(idxThread) * width;
        // the beginning depends on the thread ID
        int begin = width * static_cast<int>(idxThread);
        int end = begin + realWidth;

        //for each pixel
        for (int i = begin; i < end; i++) { // columns
            for (int j = 0; j < img.rows; j++) { // lines
                // if the pixel is inside the structure
                if (img.at<uchar>(j, i) == 255) {
                    // counts the number of neighbor pixels within the given
                    // window size that are part of the structure also
                    int count = 0;
                    for (int k = -(size - 1) / 2; k <= (size - 1) / 2; k++) {
                        for (int l = -(size - 1) / 2; l <= (size - 1) / 2; l++) {
                            if ((i + k) >= 0 && (i + k) < img.cols && (j + l) >= 0 && (j + l) < img.rows && img.at<uchar>(j + l, i + k) == 255) {
                                count++;
                            }
                        }
                    }
                    // then create a ratio between the neighbor pixels and total size of the window
                    float coef = static_cast<float>(count) / static_cast<float>(size * size);
                    // finally fill the resulting Mat with a color as white as the ratio is near to 1
                    res.at<uchar>(j, i) = static_cast<uchar>(coef * 255.0f);
                }
            }
        }
    };

    std::vector<std::thread> ThreadVector;

    // for each thread, emplace in the vector their job
    for (unsigned int i = 0; i < nb_thread; i++) {
        ThreadVector.emplace_back(f, i);
    }

    // then wait them to finish
    for (auto& t: ThreadVector) {
        t.join();
    }

    cv::Mat resNoEqualization;
    if (showAllImages) {
        res.copyTo(resNoEqualization);
        cv::imshow("Grayscale not normalized", resNoEqualization);
        cv::applyColorMap(resNoEqualization, resNoEqualization, cv::COLORMAP_JET);
    }

    normalizeMat(res);

    if (showAllImages) {
        cv::imshow("Grayscale normalized", res);
    }

    // set colormap jet to have an image in red when the pixel is white and in blue when it is black
    cv::applyColorMap(res, res, cv::COLORMAP_JET);

    // the colormap set black value (background) to a darkblue RGB(0, 0, 128)
    // we need to restore the black value to have a better view of the colors
    // since it is stored in bgr format, we change the blue background by
    // affecting the first value (blue) to the new value
    cv::Mat mask;
    cv::inRange(res, cv::Scalar(128, 0, 0), cv::Scalar(128, 0, 0), mask);
    res.setTo(cv::Scalar(0, 0, 0), mask);
    if (showAllImages) {
        resNoEqualization.setTo(cv::Scalar(0, 0, 0), mask);
        cv::imshow("Colored not normalized, W=" + std::to_string(size), resNoEqualization);
    }

    cv::imshow("Colored normalized, W=" + std::to_string(size), res);
}

}

