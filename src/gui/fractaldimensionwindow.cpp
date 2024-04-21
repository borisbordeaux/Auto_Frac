#include <QFileDialog>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>
#include <QScatterSeries>
#include <QValueAxis>
#include "gui/fractaldimensionwindow.h"
#include "ui_fractaldimensionwindow.h"
#include "NazaraUtils/Algorithm.hpp"
#include "fractaldimension/fractaldimension.h"


FractalDimensionWindow::FractalDimensionWindow(QWidget* parent) :
        QWidget(parent), ui(new Ui::FractalDimensionWindow), m_chartFractalDim(new QChart()) {
    ui->setupUi(this);

    this->ui->graphicsView_fractalDim->setScene(&m_sceneFractalDim);
    m_chartFractalDim->setTheme(QChart::ChartTheme::ChartThemeDark);
    m_chartFractalDim->legend()->hide();
    m_chartFractalDim->setTitle("Fractal Dimension");
    m_chartFractalDim->setPreferredSize(845, 845);
    m_chartFractalDim->setAnimationOptions(QChart::AnimationOption::AllAnimations);
    m_chartFractalDim->setAnimationDuration(1000);
    m_sceneFractalDim.addItem(m_chartFractalDim);
}

FractalDimensionWindow::~FractalDimensionWindow() {
    delete ui;
}

[[maybe_unused]] void FractalDimensionWindow::slotComputeFractalDimension() {
    QString file = QFileDialog::getOpenFileName(this, "Open a PNG File...", "../img", "PNG Files (*.png)", nullptr, QFileDialog::DontUseNativeDialog);

    if (file != "") {
        cv::destroyAllWindows();
        cv::Mat img = cv::imread(file.toStdString(), cv::IMREAD_GRAYSCALE);
        cv::threshold(img, img, 1, 255, cv::THRESH_BINARY);
        cv::imshow("Image", img);

        std::cout << "image size : " << img.size().width << " x " << img.size().height << std::endl;

        // resize image to make it squared
        if (img.cols != img.rows || !Nz::IsPow2(img.rows)) {
            int max = Nz::RoundToPow2(std::max(img.cols, img.rows));
            int top = (max - img.rows) / 2;
            int bottom = (max - img.rows) - top;
            int left = (max - img.cols) / 2;
            int right = (max - img.cols) - left;
            cv::copyMakeBorder(img, img, top, bottom, left, right, cv::BORDER_CONSTANT, cv::Scalar(0));
        }

        std::cout << "image size for fractal dimension : " << img.size().width << " x " << img.size().height << std::endl;

        m_chartFractalDim->removeAllSeries();
        QScatterSeries* series = new QScatterSeries();
        QScatterSeries* seriesUnused = new QScatterSeries();

        series->setColor(Qt::blue);
        seriesUnused->setColor(Qt::black);

        std::vector<int> res = frac::computeFractalDimension(img);

        std::vector<std::pair<float, float>> logRes;
        logRes.reserve(res.size());
        int i = 2;
        for (auto x: res) {
            logRes.emplace_back(std::log(static_cast<float>(i)), std::log(static_cast<float>(x)));
            i *= 2;
        }

        int maxUsefulTerm = std::min(this->ui->spinBox_maxUsefulBox->value(), static_cast<int>(res.size()));
        if (maxUsefulTerm == 0) {
            maxUsefulTerm = static_cast<int>(res.size());
        } else {
            if (maxUsefulTerm == 1) { maxUsefulTerm = 2; }
            this->ui->spinBox_maxUsefulBox->setValue(maxUsefulTerm);
        }
        int minUsefulTerm = std::min(this->ui->spinBox_minUsefulBox->value(), maxUsefulTerm - 2);
        this->ui->spinBox_minUsefulBox->setValue(minUsefulTerm);
        int current = 0;

        std::cout << "dim fractale" << std::endl;
        for (auto p: logRes) {
            if (current >= minUsefulTerm && current < maxUsefulTerm) {
                series->append(p.first, p.second);
                std::cout << p.first << " " << p.second << std::endl;
            } else {
                seriesUnused->append(p.first, p.second);
            }
            current++;
        }

        series->setBestFitLineVisible(true);
        series->setBestFitLineColor(Qt::yellow);
        m_chartFractalDim->addSeries(series);
        m_chartFractalDim->addSeries(seriesUnused);
        m_chartFractalDim->createDefaultAxes();
        QValueAxis* xAxis = dynamic_cast<QValueAxis*>(m_chartFractalDim->axes(Qt::Horizontal, series).first());
        QValueAxis* yAxis = dynamic_cast<QValueAxis*>(m_chartFractalDim->axes(Qt::Vertical, series).first());
        int max = std::max(qRound(xAxis->max() + 1.0), qRound(yAxis->max() + 1.0));
        xAxis->setRange(0, max);
        xAxis->setTickInterval(1.0);
        xAxis->setTickCount(max + 1);
        xAxis->setTitleText("log(1/e)");
        yAxis->setRange(0, max);
        yAxis->setTickInterval(1.0);
        yAxis->setTickCount(max + 1);
        yAxis->setTitleText("log(Ne)");

        bool ok;
        QPair<qreal, qreal> eq = series->bestFitLineEquation(ok);
        if (ok) {
            this->ui->label_fractalDimension->setText(QString::number(eq.first));
            std::cout << eq.first << "x + " << eq.second << std::endl;
        }
    }
}

void FractalDimensionWindow::hideEvent(QHideEvent* event) {
    cv::destroyAllWindows();
    QWidget::hideEvent(event);
}
