#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "structure.h"
#include "structureprinter.h"
#include "fileprinter.h"

#include <QtWidgets>
#include <iostream>

MainWindow::MainWindow(QWidget* parent) :
        QMainWindow(parent),
        ui(new Ui::MainWindow) {
    ui->setupUi(this);
    this->ui->listWidget_Faces->setCurrentRow(0);
}

MainWindow::~MainWindow() {
    delete ui;
}

void MainWindow::slot1() {
    frac::Face::reset();
    frac::FilePrinter::reset();

    std::vector<frac::Face> faces;
    for (int i = 0; i < this->ui->listWidget_Faces->count(); ++i) {
        faces.push_back(toFace(this->ui->listWidget_Faces->item(i)->text()));
    }

    frac::Structure s { faces };

    std::cout << s;

    frac::StructurePrinter::exportStruct(s, false, "../result.py");

    std::cout.flush();
}

frac::Edge MainWindow::toEdge(QString const& edgeName) {
    QChar sepEdgesParam = '_';
    QStringList splitEdgeName = edgeName.split(sepEdgesParam);
    frac::EdgeType type = splitEdgeName[0] == "C" ? frac::EdgeType::CANTOR : frac::EdgeType::BEZIER;
    unsigned int nbSubs = splitEdgeName[1].toUInt();
    unsigned int delayEdge = splitEdgeName[2].toUInt();
    return { type, nbSubs, delayEdge };
}

frac::Face MainWindow::toFace(QString const& cellName) {
    QString sepCellInfo = " / ";
    QString sepEdges = " - ";

    QStringList splitCellName = cellName.split(sepCellInfo);
    QString edgesNames = splitCellName[0];
    QString paramsNames = splitCellName[1];
    unsigned int delay = splitCellName[2].toUInt();

    std::vector<frac::Edge> edges;
    for (QString const& edgeName: edgesNames.split(sepEdges)) {
        edges.emplace_back(MainWindow::toEdge(edgeName));
    }
    QStringList splitParamsNames = paramsNames.split(sepEdges);

    frac::Edge adjEdge = MainWindow::toEdge(splitParamsNames[0]);
    frac::Edge gapEdge = MainWindow::toEdge(splitParamsNames[1]);
    frac::Edge reqEdge = MainWindow::toEdge(splitParamsNames[2]);

    return frac::Face(edges, delay, adjEdge, gapEdge, reqEdge);
}

void MainWindow::slotAddFace() {
    this->ui->listWidget_Faces->addItem("C_2_0 - B_2_0 - C_2_0 - B_2_0 - C_2_0 - B_2_0 / C_2_0 - B_2_0 - B_2_0 / 0");
    this->ui->listWidget_Faces->setCurrentRow(this->ui->listWidget_Faces->count() - 1);
}

void MainWindow::slotRemoveFace() {
    if (this->ui->listWidget_Faces->count() > 1) {
        this->ui->listWidget_Faces->takeItem(this->ui->listWidget_Faces->currentRow());
    }
}

void MainWindow::slotOnFaceSelected(int row) {
    if (row == -1) return;

    QString cellName = this->ui->listWidget_Faces->item(row)->text();
    frac::Face f = MainWindow::toFace(cellName);
    //adjEdge
    this->ui->comboBox_adjEdgeTopology->setCurrentIndex(f.adjEdge().edgeType() == frac::EdgeType::CANTOR ? 0 : 1);
    this->ui->spinBox_adjEdgeNbSubdivisions->setValue(static_cast<int>(f.adjEdge().nbSubdivisions()));
    this->ui->spinBox_adjEdgeDelay->setValue(static_cast<int>(f.adjEdge().delay()));
    //gapEdge
    this->ui->comboBox_gapEdgeTopology->setCurrentIndex(f.gapEdge().edgeType() == frac::EdgeType::CANTOR ? 0 : 1);
    this->ui->spinBox_gapEdgeNbSubdivisions->setValue(static_cast<int>(f.gapEdge().nbSubdivisions()));
    this->ui->spinBox_gapEdgeDelay->setValue(static_cast<int>(f.gapEdge().delay()));
    //reqEdge
    this->ui->comboBox_reqEdgeTopology->setCurrentIndex(f.reqEdge().edgeType() == frac::EdgeType::CANTOR ? 0 : 1);
    this->ui->spinBox_reqEdgeNbSubdivisions->setValue(static_cast<int>(f.reqEdge().nbSubdivisions()));
    this->ui->spinBox_reqEdgeDelay->setValue(static_cast<int>(f.reqEdge().delay()));
    //list edges
    this->ui->listWidget_Edges->clear();
    for (frac::Edge const& e: f.data()) {
        this->ui->listWidget_Edges->addItem(e.toString().c_str());
    }
    this->ui->listWidget_Edges->setCurrentRow(0);
}

void MainWindow::slotOnEdgeSelected(int row) {
    if (row == -1) return;

    frac::Edge e = toEdge(this->ui->listWidget_Edges->item(row)->text());
    this->ui->comboBox_currentEdgeTopology->setCurrentIndex(e.edgeType() == frac::EdgeType::CANTOR ? 0 : 1);
    this->ui->spinBox_currentEdgeNbSubdivisions->setValue(static_cast<int>(e.nbSubdivisions()));
    this->ui->spinBox_currentEdgeDelay->setValue(static_cast<int>(e.delay()));
}
