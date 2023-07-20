#include "utils/fractaldimension.h"
#include <iostream>
#include <QPaintEngine>

namespace frac::utils {

void computeFractalDimension(QImage const& img) {
    std::cout << "image size : " << img.size().width() << " x " << img.size().height() << std::endl;
    int iter = 1;
    std::vector<std::pair<int, int>> result;
    //define max size
    int maxSize = img.size().width();
    while (maxSize > 1) {
        maxSize /= 2;
        iter *= 2;
        int nbOverlappingSquares = 0;
        for (int i = 0; i < iter; i++) {
            for (int j = 0; j < iter; j++) {
                //compute number of squares overlapping the fractal
                QRect crop = { i * maxSize, j * maxSize, maxSize, maxSize };
                //std::cout << "crop rect = " << crop.x() << ", " << crop.y() << ", " << crop.width() << ", " << crop.height() << std::endl;
                QImage sub = img.copy(crop);
                /*if (iter == 8) {
                    QImage temp = img.copy();
                    std::cout << "begin paint" << std::endl;
                    QPainter painter(&temp);
                    QPen pen;
                    pen.setWidth(1);
                    pen.setColor(Qt::red);
                    painter.setPen(pen);
                    painter.fillRect(crop, Qt::blue);
                    painter.end();
                    temp.save("../img/" + QString::number(iter) + "_" + QString::number(i) + "_" + QString::number(j) + ".png");
                }*/
                if (!sub.allGray()) {
                    nbOverlappingSquares++;
                }
            }
        }
        //save each number into a vector
        result.emplace_back(nbOverlappingSquares, maxSize);
    }
    //print the vector
    int i = 1;
    for (auto x: result) {
        std::cout << x.first << " rects out of " << (2 * i) * (2 * i) << " with size of " << x.second << std::endl;
        i *= 2;
    }

}

}

