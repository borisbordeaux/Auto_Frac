#include <iostream>
#include <QValueAxis>
#include <QScatterSeries>
#include <QFileDialog>
#include <opencv2/highgui.hpp>
#include "gui/areaperimeterwindow.h"
#include "ui_areaperimeterwindow.h"
#include "utils/measures.h"


AreaPerimeterWindow::AreaPerimeterWindow(QWidget* parent) :
        QWidget(parent), ui(new Ui::AreaPerimeterWindow), m_chartAreaPerimeter(new QChart()) {
    ui->setupUi(this);

    this->ui->graphicsView_stats->setScene(&m_sceneAreaPerimeter);
    m_chartAreaPerimeter->setTheme(QChart::ChartTheme::ChartThemeDark);
    m_chartAreaPerimeter->setTitle("Area and Perimeter");
    m_chartAreaPerimeter->setPreferredSize(845, 845);
    m_chartAreaPerimeter->setAnimationOptions(QChart::AnimationOption::AllAnimations);
    m_chartAreaPerimeter->setAnimationDuration(1000);
    m_sceneAreaPerimeter.addItem(m_chartAreaPerimeter);
}

AreaPerimeterWindow::~AreaPerimeterWindow() {
    delete ui;
}

[[maybe_unused]] void AreaPerimeterWindow::slotComputeAreaPerimeterPNG() {
    QStringList files = QFileDialog::getOpenFileNames(this, "Open PNG Files...", "../img", "PNG Files (*.png)", nullptr, QFileDialog::DontUseNativeDialog);
    if (!files.isEmpty()) {
        cv::destroyAllWindows();
        this->computeAreaPerimeter(files);
    }
}

[[maybe_unused]] void AreaPerimeterWindow::slotComputeAreaPerimeterOBJ() {
    QStringList files = QFileDialog::getOpenFileNames(this, "Open OBJ Files...", "../obj", "OBJ Files (*.obj)", nullptr, QFileDialog::DontUseNativeDialog);
    if (!files.isEmpty()) {
        this->computeAreaPerimeter(files);
    }
}

void AreaPerimeterWindow::computeAreaPerimeter(const QStringList& files) {
    int currentFile = 0;
    m_chartAreaPerimeter->removeAllSeries();
    QScatterSeries* seriesArea = new QScatterSeries();
    QScatterSeries* seriesPerimeter = new QScatterSeries();
    seriesArea->setName("Area");
    seriesPerimeter->setName("Perimeter");

    seriesArea->setColor(Qt::blue);
    seriesPerimeter->setColor(Qt::darkGreen);

    std::vector<float> vectorArea;
    std::vector<float> vectorPerimeter;

    float firstArea = -1;
    float firstPerimeter = -1;
    for (QString const& file: files) {
        float area = frac::utils::computeArea(file);
        float perimeter = frac::utils::computePerimeter(file);
        if (firstArea < 0.0f) {
            firstArea = area;
        }
        if (firstPerimeter < 0.0f) {
            firstPerimeter = perimeter;
        }

        this->ui->label_perimeter->setText(std::to_string(perimeter).c_str());
        this->ui->label_area->setText(std::to_string(area).c_str());

        float y1 = area / firstArea;
        float y2 = perimeter / firstPerimeter;

        vectorArea.push_back(area);
        vectorPerimeter.push_back(perimeter);

        seriesArea->append(static_cast<float>(currentFile), std::log(y1));
        seriesPerimeter->append(static_cast<float>(currentFile), std::log((y2)));

        this->ui->label_porosity->setText(QString::number(1.0f - y1));
        currentFile++;
    }

    bool okArea;
    bool okPerimeter;
    QPair<qreal, qreal> areaReg = seriesArea->bestFitLineEquation(okArea);
    QPair<qreal, qreal> perimeterReg = seriesPerimeter->bestFitLineEquation(okPerimeter);
    if (okArea && okPerimeter) {
        seriesArea->setBestFitLineColor(Qt::blue);
        seriesArea->setBestFitLineVisible(true);
        this->ui->label_coefArea->setText(std::to_string(std::exp(areaReg.first)).c_str());

        seriesPerimeter->setBestFitLineColor(Qt::darkGreen);
        seriesPerimeter->setBestFitLineVisible(true);
        this->ui->label_coefPerimeter->setText(std::to_string(std::exp(perimeterReg.first)).c_str());
    } else {
        this->ui->label_coefArea->setText("");
        this->ui->label_coefPerimeter->setText("");
    }

    m_chartAreaPerimeter->addSeries(seriesArea);
    m_chartAreaPerimeter->addSeries(seriesPerimeter);
    m_chartAreaPerimeter->createDefaultAxes();
    QValueAxis* xAxis = dynamic_cast<QValueAxis*>(m_chartAreaPerimeter->axes(Qt::Horizontal).first());
    QValueAxis* yAxis = dynamic_cast<QValueAxis*>(m_chartAreaPerimeter->axes(Qt::Vertical).first());
    int maxX = qRound(xAxis->max()) + 1;
    int maxY = qCeil(yAxis->max());
    int minY = qFloor(yAxis->min());
    xAxis->setRange(-1, maxX);
    xAxis->setTickInterval(1.0);
    xAxis->setTickCount(maxX + 2);
    xAxis->setTitleText("Iteration level");

    yAxis->setRange(minY, maxY);
    yAxis->setTickInterval(1.0);
    yAxis->setTickCount(maxY - minY + 1);
    yAxis->setTitleText("log(A_i/A_0) or log(P_i/P_0)");

    // add events on click
    connect(seriesArea, &QScatterSeries::clicked, this, [&, vectorArea, vectorPerimeter, firstArea](QPointF point) {
        int iter = qRound(point.x());
        this->ui->label_area->setText(std::to_string(vectorArea[iter]).c_str());
        this->ui->label_perimeter->setText(std::to_string(vectorPerimeter[iter]).c_str());
        this->ui->label_porosity->setText(QString::number(1.0f - (vectorArea[iter] / firstArea)));
    });
    connect(seriesPerimeter, &QScatterSeries::clicked, this, [&, vectorPerimeter, vectorArea, firstArea](QPointF point) {
        int iter = qRound(point.x());
        this->ui->label_perimeter->setText(std::to_string(vectorPerimeter[iter]).c_str());
        this->ui->label_area->setText(std::to_string(vectorArea[iter]).c_str());
        this->ui->label_porosity->setText(QString::number(1.0f - (vectorArea[iter] / firstArea)));
    });

    // temp cout for python script
    std::cout << "area log [";
    for (float v: vectorArea) {
        std::cout << std::log(v / firstArea) << ", ";
    }
    std::cout << "]" << std::endl;

    std::cout << "area not log [";
    for (float v: vectorArea) {
        std::cout << v / firstArea << ", ";
    }
    std::cout << "]" << std::endl;

    std::cout << areaReg.first << "x + " << areaReg.second << std::endl;

    std::cout << "perimeter log [";
    for (float v: vectorPerimeter) {
        std::cout << std::log(v / firstPerimeter) << ", ";
    }
    std::cout << "]" << std::endl;

    std::cout << "perimeter not log [";
    for (float v: vectorPerimeter) {
        std::cout << v / firstPerimeter << ", ";
    }
    std::cout << "]" << std::endl;

    std::cout << perimeterReg.first << "x + " << perimeterReg.second << std::endl;
}
