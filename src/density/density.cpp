#include "density/density.h"
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <QString>
#include <thread>

void frac::computeDensity(QString const& file, int value, bool showAllImages) {
    cv::destroyAllWindows();
    cv::Mat img = cv::imread(file.toStdString(), cv::IMREAD_GRAYSCALE);
    cv::threshold(img, img, 1, 255, cv::THRESH_BINARY);
    cv::imshow(std::string("Image"), img);

    computeDensity(img, value, showAllImages);
}

void normalizeMat(cv::Mat& img) {
    uchar max = *std::max_element(img.begin<uchar>(), img.end<uchar>());
    if (max < 255) {
        std::for_each(img.begin<uchar>(), img.end<uchar>(), [&](uchar& val) {
            val = (val * 255) / max;
        });
    }
}

void frac::computeDensity(cv::Mat const& img, int size, bool showAllImages) {
    cv::Mat res;
    img.copyTo(res); //copy in order to have same size and type

    // use multithreading for this computation since it can take time
    // and can be done independently for each pixel
    unsigned int nb_thread = std::thread::hardware_concurrency();

    std::function<void(unsigned int)> f = [&](unsigned int idxThread) {
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
    cv::applyColorMap(res, res, cv::COLORMAP_TURBO);

    // the colormap set black value (background) to a darkblue RGB(0, 0, 128)
    // we need to restore the black value to have a better view of the colors
    // since it is stored in bgr format, we change the blue background by
    // affecting the first value (blue) to the new value
    cv::Mat mask;
    cv::threshold(img,mask, 1, 255, cv::THRESH_BINARY_INV);
    cv::Scalar backgroundColor(128,128,128);
    cv::imshow("mask", mask);
    res.setTo(backgroundColor, mask);
    if (showAllImages) {
        resNoEqualization.setTo(backgroundColor, mask);
        cv::imshow("Colored not normalized, W=" + std::to_string(size), resNoEqualization);
    }

    cv::imshow("Colored normalized, W=" + std::to_string(size), res);
}
