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
    this->updateEnablement();
}

MainWindow::~MainWindow() {
    delete ui;
}

[[maybe_unused]] void MainWindow::slot1() {
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

[[maybe_unused]] void MainWindow::slotAddFace() {
    this->ui->listWidget_Faces->addItem("C_2_0 - B_2_0 - C_2_0 - B_2_0 - C_2_0 - B_2_0 / C_2_0 - B_2_0 - B_2_0 / 0");
    this->ui->listWidget_Faces->setCurrentRow(this->ui->listWidget_Faces->count() - 1);
    this->updateEnablement();
}

[[maybe_unused]] void MainWindow::slotRemoveFace() {
    this->ui->listWidget_Faces->takeItem(this->ui->listWidget_Faces->currentRow());
    this->updateEnablement();
}

[[maybe_unused]] void MainWindow::slotOnFaceSelected(int row) {
    if (row == -1) return;

    QString cellName = this->ui->listWidget_Faces->item(row)->text();
    frac::Face f = MainWindow::toFace(cellName);
    //delay
    this->ui->spinBox_faceDelay->setValue(static_cast<int>(f.delay()));
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
    for (frac::Edge const& e: f.constData()) {
        this->ui->listWidget_Edges->addItem(e.toString().c_str());
    }
    this->ui->listWidget_Edges->setCurrentRow(0);
}

[[maybe_unused]] void MainWindow::slotOnEdgeSelected(int row) {
    if (row == -1) return;

    frac::Edge e = toEdge(this->ui->listWidget_Edges->item(row)->text());
    this->ui->comboBox_currentEdgeTopology->setCurrentIndex(e.edgeType() == frac::EdgeType::CANTOR ? 0 : 1);
    this->ui->spinBox_currentEdgeNbSubdivisions->setValue(static_cast<int>(e.nbSubdivisions()));
    this->ui->spinBox_currentEdgeDelay->setValue(static_cast<int>(e.delay()));
}

[[maybe_unused]] void MainWindow::slotOnFaceAdjTopologyChanged(int row) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    frac::Edge e { row == 0 ? frac::EdgeType::CANTOR : frac::EdgeType::BEZIER, f.adjEdge().nbSubdivisions(), f.adjEdge().delay() };
    f.setAdjEdge(e);
    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceAdjNbSubdivisionsChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    frac::Edge e { f.adjEdge().edgeType(), static_cast<unsigned int>(value), f.adjEdge().delay() };
    f.setAdjEdge(e);
    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceAdjDelayChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    frac::Edge e { f.adjEdge().edgeType(), f.adjEdge().nbSubdivisions(), static_cast<unsigned int>(value) };
    f.setAdjEdge(e);
    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceGapTopologyChanged(int row) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    frac::Edge e { row == 0 ? frac::EdgeType::CANTOR : frac::EdgeType::BEZIER, f.adjEdge().nbSubdivisions(), f.adjEdge().delay() };
    f.setGapEdge(e);
    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceGapNbSubdivisionsChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    frac::Edge e { f.adjEdge().edgeType(), static_cast<unsigned int>(value), f.adjEdge().delay() };
    f.setGapEdge(e);
    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceGapDelayChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    frac::Edge e { f.adjEdge().edgeType(), f.adjEdge().nbSubdivisions(), static_cast<unsigned int>(value) };
    f.setGapEdge(e);
    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceReqTopologyChanged(int row) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    frac::Edge e { row == 0 ? frac::EdgeType::CANTOR : frac::EdgeType::BEZIER, f.adjEdge().nbSubdivisions(), f.adjEdge().delay() };
    f.setReqEdge(e);
    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceReqNbSubdivisionsChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    frac::Edge e { f.adjEdge().edgeType(), static_cast<unsigned int>(value), f.adjEdge().delay() };
    f.setReqEdge(e);
    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceReqDelayChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    frac::Edge e { f.adjEdge().edgeType(), f.adjEdge().nbSubdivisions(), static_cast<unsigned int>(value) };
    f.setReqEdge(e);
    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceDelayChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    f.setDelay(value);
    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotAddEdge() {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    frac::Edge e { frac::EdgeType::CANTOR, 2, 0 };
    auto it = f.data().begin();
    it += this->ui->listWidget_Edges->currentRow() + 1;
    f.data().emplace(it, e);
    int oldRow = this->ui->listWidget_Edges->currentRow();
    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
    MainWindow::slotOnFaceSelected(this->ui->listWidget_Faces->currentRow());
    this->ui->listWidget_Edges->setCurrentRow(oldRow + 1);
    this->updateEnablement();
}

[[maybe_unused]] void MainWindow::slotRemoveEdge() {
    if (this->ui->listWidget_Edges->count() == 3) return;
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    long int indexToRemove = this->ui->listWidget_Edges->currentRow();
    std::vector<frac::Edge> edges;
    int i = 0;
    for (frac::Edge const& e: f.constData()) {
        if (i != indexToRemove) {
            edges.push_back(e);
        }
        i++;
    }
    f.data().clear();
    f.data().insert(f.data().begin(), edges.begin(), edges.end());
    int oldRow = this->ui->listWidget_Edges->currentRow();
    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
    MainWindow::slotOnFaceSelected(this->ui->listWidget_Faces->currentRow());
    this->ui->listWidget_Edges->setCurrentRow(std::min(this->ui->listWidget_Edges->count() - 1, oldRow));
    this->updateEnablement();
}

[[maybe_unused]] void MainWindow::slotOnSelectedEdgeTopologyChanged(int row) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    f.data().at(this->ui->listWidget_Edges->currentRow()).setEdgeType(row == 0 ? frac::EdgeType::CANTOR : frac::EdgeType::BEZIER);

    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
    this->ui->listWidget_Edges->currentItem()->setText(f.data().at(this->ui->listWidget_Edges->currentRow()).toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnSelectedEdgeNbSubdivisionsChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    f.data().at(this->ui->listWidget_Edges->currentRow()).setNbSubdivisions(static_cast<unsigned int>(value));

    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
    this->ui->listWidget_Edges->currentItem()->setText(f.data().at(this->ui->listWidget_Edges->currentRow()).toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnSelectedEdgeDelayChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_Faces->currentItem()->text());
    f.data().at(this->ui->listWidget_Edges->currentRow()).setDelay(static_cast<unsigned int>(value));

    this->ui->listWidget_Faces->currentItem()->setText(f.toString().c_str());
    this->ui->listWidget_Edges->currentItem()->setText(f.data().at(this->ui->listWidget_Edges->currentRow()).toString().c_str());
}

void MainWindow::updateEnablement() {
    //button remove face
    this->ui->pushButton_removeFace->setEnabled(this->ui->listWidget_Faces->count() > 1);
    //adj edge face
    this->ui->comboBox_adjEdgeTopology->setEnabled(this->ui->listWidget_Faces->currentRow() > -1);
    this->ui->spinBox_adjEdgeNbSubdivisions->setEnabled(this->ui->listWidget_Faces->currentRow() > -1);
    this->ui->spinBox_adjEdgeDelay->setEnabled(this->ui->listWidget_Faces->currentRow() > -1);
    //gap edge face
    this->ui->comboBox_gapEdgeTopology->setEnabled(this->ui->listWidget_Faces->currentRow() > -1);
    this->ui->spinBox_gapEdgeNbSubdivisions->setEnabled(this->ui->listWidget_Faces->currentRow() > -1);
    this->ui->spinBox_gapEdgeDelay->setEnabled(this->ui->listWidget_Faces->currentRow() > -1);
    //req edge face
    this->ui->comboBox_reqEdgeTopology->setEnabled(this->ui->listWidget_Faces->currentRow() > -1);
    this->ui->spinBox_reqEdgeNbSubdivisions->setEnabled(this->ui->listWidget_Faces->currentRow() > -1);
    this->ui->spinBox_reqEdgeDelay->setEnabled(this->ui->listWidget_Faces->currentRow() > -1);
    //delay face
    this->ui->spinBox_faceDelay->setEnabled(this->ui->listWidget_Faces->currentRow() > -1);
    //button add and remove edges
    this->ui->pushButton_addEdge->setEnabled(this->ui->listWidget_Faces->currentRow() > -1);
    this->ui->pushButton_removeEdge->setEnabled(this->ui->listWidget_Edges->count() > 3);
    //edge info
    this->ui->comboBox_currentEdgeTopology->setEnabled(this->ui->listWidget_Edges->currentRow() > -1);
    this->ui->spinBox_currentEdgeNbSubdivisions->setEnabled(this->ui->listWidget_Edges->currentRow() > -1);
    this->ui->spinBox_currentEdgeDelay->setEnabled(this->ui->listWidget_Edges->currentRow() > -1);
    //TODO: constraints
    //button generation
    this->ui->pushButton_generateScript->setEnabled(this->ui->listWidget_Faces->currentRow() > -1);
}
