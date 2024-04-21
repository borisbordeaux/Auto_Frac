#include "fractaldimension/fractaldimension.h"

#include <opencv2/core/core.hpp>
#include <iostream>

std::vector<int> frac::computeFractalDimension(cv::Mat const& img) {
    int iter = 1;
    std::vector<int> result;
    //define max size
    int maxSize = img.size().width;
    while (maxSize > 1) {
        maxSize /= 2;
        iter *= 2;

        std::cout << "sub image size is " << maxSize << std::endl;

        //compute number of squares overlapping the fractal
        int nbOverlappingSquares = 0;
        for (int i = 0; i < iter; i++) {
            for (int j = 0; j < iter; j++) {
                cv::Range rangeX { i * maxSize, (i + 1) * maxSize };
                cv::Range rangeY { j * maxSize, (j + 1) * maxSize };

                cv::Mat sub = img(rangeY, rangeX);

                bool coverForm = cv::countNonZero(sub) != 0;

                if (coverForm) {
                    nbOverlappingSquares++;
                }
            }
        }
        //save each number into a vector
        result.emplace_back(nbOverlappingSquares);
    }

    return result;
}