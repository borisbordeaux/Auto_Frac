#include "gui/densitywindow.h"
#include "ui_densitywindow.h"
#include <QFileDialog>
#include <opencv2/highgui.hpp>
#include "density/density.h"


DensityWindow::DensityWindow(QWidget* parent) :
        QWidget(parent), ui(new Ui::DensityWindow) {
    ui->setupUi(this);

    connect(this->ui->horizontalSlider_windowSize, &QSlider::valueChanged, this->ui->label_windowSize, qOverload<int>(&QLabel::setNum));
    connect(this->ui->horizontalSlider_windowSize, &QSlider::sliderMoved, this, [&](int value) {
        if (value % 2 == 0) {
            this->ui->horizontalSlider_windowSize->setValue(value - 1);
        }
    });
}

DensityWindow::~DensityWindow() {
    delete ui;
}

[[maybe_unused]] void DensityWindow::slotComputeImageDensity() {
    QString file = QFileDialog::getOpenFileName(this, "Open a PNG File...", "../img", "PNG Files (*.png)", nullptr);

    if (file != "") {
        frac::computeDensity(file, this->ui->horizontalSlider_windowSize->value(), this->ui->checkBox_showDensityImages->isChecked());
    }
}

void DensityWindow::hideEvent(QHideEvent* event) {
    cv::destroyAllWindows();
    QWidget::hideEvent(event);
}
