#include <QFileDialog>
#include <QScatterSeries>
#include <QLineSeries>
#include <QValueAxis>
#include "gui/persistenthomologywindow.h"
#include "ui_persistenthomologywindow.h"
#include "persistenthomology/persistenthomology.h"


PersistentHomologyWindow::PersistentHomologyWindow(QWidget* parent) :
        QWidget(parent), ui(new Ui::PersistentHomologyWindow), m_chartPersistentHomology(new QChart()) {
    ui->setupUi(this);
    this->ui->graphicsView_PersistentHomology->setScene(&m_scenePersistentHomology);
    m_chartPersistentHomology->setTheme(QChart::ChartTheme::ChartThemeDark);
    m_chartPersistentHomology->setTitle("Persistent Homology");
    m_chartPersistentHomology->setPreferredSize(845, 845);
    m_chartPersistentHomology->setAnimationOptions(QChart::AnimationOption::AllAnimations);
    m_chartPersistentHomology->setAnimationDuration(1000);
    m_scenePersistentHomology.addItem(m_chartPersistentHomology);
}

PersistentHomologyWindow::~PersistentHomologyWindow() {
    delete ui;
}

[[maybe_unused]] void PersistentHomologyWindow::slotComputePersistenceHomology() {
    QString file = QFileDialog::getOpenFileName(this, "Open an OFF File...", "../off", "OFF Files (*.off)");
    if (file == "") { return; }

    m_chartPersistentHomology->removeAllSeries();
    std::vector<QScatterSeries*> series;
    QLineSeries* diag = new QLineSeries();
    diag->setName("Diagonal");

    // dim will never be greater than 4
    Qt::GlobalColor colors[4] = { Qt::darkGreen, Qt::blue, Qt::red, Qt::yellow };

    std::vector<frac::PersistentHomology::Cycles> cycles = frac::PersistentHomology::computePersistenceHomology(file, static_cast<float>(this->ui->spinBox_persistenceR->value()), static_cast<float>(this->ui->spinBox_persistenceLifeTime->value()), this->ui->spinBox_persistenceDim->value());
    for (frac::PersistentHomology::Cycles const& c: cycles) {
        if (c.Death < 100.0f) { //not inf
            while (series.size() < static_cast<std::size_t>(c.Dim) + 1) {
                series.push_back(new QScatterSeries());
                series[series.size() - 1]->setName("Dim " + QString::number(c.Dim));
                series[series.size() - 1]->setColor(colors[series.size() - 1]);
            }
            series[c.Dim]->append(c.Birth, c.Death);
        }
    }

    std::vector<int> addedSeries;
    int i = 0;
    for (auto* s: series) {
        m_chartPersistentHomology->addSeries(s);
        addedSeries.push_back(i);
        i++;
    }
    m_chartPersistentHomology->createDefaultAxes();
    QValueAxis* xAxis = dynamic_cast<QValueAxis*>(m_chartPersistentHomology->axes(Qt::Horizontal).first());
    QValueAxis* yAxis = dynamic_cast<QValueAxis*>(m_chartPersistentHomology->axes(Qt::Vertical).first());

    int max = qCeil(qMax(xAxis->max(), yAxis->max()));

    xAxis->setRange(-1.0, max);
    xAxis->setTickCount(2 * max + 3);
    xAxis->setTitleText("Birth");

    yAxis->setRange(-1.0, max);
    yAxis->setTickCount(2 * max + 3);
    yAxis->setTitleText("Death");

    for (frac::PersistentHomology::Cycles const& c: cycles) {
        if (c.Death > 100.0f) { //not inf
            while (series.size() < static_cast<std::size_t>(c.Dim) + 1) {
                series.push_back(new QScatterSeries());
                series[series.size() - 1]->setName("Dim " + QString::number(c.Dim));
                series[series.size() - 1]->setColor(colors[series.size() - 1]);
            }
            series[c.Dim]->append(c.Birth, max);
        }
    }

    i = 0;
    for (auto* s: series) {
        if (std::find(addedSeries.begin(), addedSeries.end(), i) == addedSeries.end()) {
            m_chartPersistentHomology->addSeries(s);
        }
        i++;
    }

    diag->append(-1.0, -1.0);
    diag->append(max, max);
    m_chartPersistentHomology->addSeries(diag);
}
