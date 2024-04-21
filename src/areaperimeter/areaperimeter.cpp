#include "areaperimeter/areaperimeter.h"
#include "halfedge/mesh.h"
#include "halfedge/objreader.h"
#include "halfedge/halfedge.h"
#include "halfedge/vertex.h"
#include "halfedge/face.h"
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <QString>

namespace frac {

float computeArea(QString const& filename) {
    if (filename.split(".")[1] == "png") {
        cv::Mat img = cv::imread(filename.toStdString(), cv::IMREAD_GRAYSCALE);
        cv::threshold(img, img, 1, 255, cv::THRESH_BINARY);
        cv::imshow(filename.toStdString(), img);
        return computeArea(img);
    }
    if (filename.split(".")[1] == "obj") {
        he::Mesh mesh;
        he::reader::readOBJ(filename, mesh);
        return computeArea(mesh);
    }
    return 0;
}

float computePerimeter(QString const& filename) {
    if (filename.split(".")[1] == "png") {
        cv::Mat img = cv::imread(filename.toStdString(), cv::IMREAD_GRAYSCALE);
        cv::threshold(img, img, 1, 255, cv::THRESH_BINARY);
        cv::imshow(filename.toStdString(), img);
        return computePerimeter(img);
    }
    if (filename.split(".")[1] == "obj") {
        he::Mesh mesh;
        he::reader::readOBJ(filename, mesh);
        return computePerimeter(mesh);
    }
    return 0;
}

float computeArea(const cv::Mat& img) {
    return static_cast<float>(cv::countNonZero(img));
}

float computeArea(he::Mesh const& mesh) {
    float res = 0.0f;
    for (he::Face* f: mesh.faces()) {
        res += f->area();
    }
    return res;
}

float computePerimeter(const cv::Mat& img) {
    cv::Mat eroded;
    cv::Mat kernel = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(3, 3), cv::Point(1, 1));
    cv::erode(img, eroded, kernel, cv::Point(1, 1), 1, cv::BORDER_CONSTANT, cv::Scalar::all(0));
    cv::subtract(img, eroded, eroded);

    return static_cast<float>(cv::countNonZero(eroded));
}

float computePerimeter(he::Mesh const& mesh) {
    float res = 0.0f;
    for (he::HalfEdge* he: mesh.halfEdges()) {
        // compute length only if half edge is on the perimeter
        if (he->face() == nullptr) {
            res += he->length();
        }
    }
    return res;
}

} //frac

