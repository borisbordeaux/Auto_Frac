#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include "computations/densitycomputation.h"
#include "utils/measures.h"
#include <QString>

void frac::DensityComputation::computeDensity(QString const& file, int value) {
    cv::destroyAllWindows();
    cv::Mat img = cv::imread(file.toStdString(), cv::IMREAD_GRAYSCALE);
    cv::threshold(img, img, 1, 255, cv::THRESH_BINARY);
    cv::imshow(std::string("Image"), img);

    frac::utils::computeDensity(img, value);
}