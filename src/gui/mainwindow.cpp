#include "gui/mainwindow.h"
#include "ui_mainwindow.h"
#include "fractal/structure.h"
#include "fractal/structureprinter.h"
#include "utils/fileprinter.h"
#include "utils/objreader.h"
#include "halfedge/mesh.h"

#include <QtWidgets>
#include <iostream>

MainWindow::MainWindow(QWidget* parent) : QMainWindow(parent), ui(new Ui::MainWindow) {
    ui->setupUi(this);
    this->updateEnablement();
    this->ui->label_log->setVisible(false);
}

MainWindow::~MainWindow() {
    delete ui;
}

[[maybe_unused]] void MainWindow::slot1() {
    frac::Face::reset();
    frac::FilePrinter::reset();

    std::vector<frac::Face> faces;
    for (int i = 0; i < this->ui->listWidget_faces->count(); ++i) {
        faces.push_back(toFace(this->ui->listWidget_faces->item(i)->text()));
    }

    frac::Structure s { faces };

    for (int i = 0; i < this->ui->listWidget_constraints->count(); ++i) {
        Constraint c = toConstraint(this->ui->listWidget_constraints->item(i)->text());
        //checks if constraint valid
        try {
            bool res = faces.at(c.Face1)[c.Edge1] == faces.at(c.Face2)[c.Edge2];
            if (!res) {
                this->setError("Error on constraint " + std::to_string(i) + " : edges are different!");
                return;
            } else {
                s.addAdjacency(c.Face1, c.Edge1, c.Face2, c.Edge2);
            }
        } catch (std::out_of_range const& error) {
            this->setError("Error on constraint " + std::to_string(i) + " : faces or edges indices are not valid!");
            return;
        }
    }

    std::ostringstream info;

    info << s;

    try {
        frac::StructurePrinter::exportStruct(s, false, "../result.py");
    } catch (std::runtime_error const& error) {
        info << error.what();
    }
    info << "Finished, result in ../result.py";

    this->setInfo(info.str());
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
    this->ui->listWidget_faces->addItem("C_2_0 - B_2_0 - C_2_0 - B_2_0 - C_2_0 - B_2_0 / C_2_0 - B_2_0 - B_2_0 / 0");
    this->ui->listWidget_faces->setCurrentRow(this->ui->listWidget_faces->count() - 1);
    this->updateEnablement();
}

[[maybe_unused]] void MainWindow::slotRemoveFace() {
    this->ui->listWidget_faces->takeItem(this->ui->listWidget_faces->currentRow());
    this->updateEnablement();
}

[[maybe_unused]] void MainWindow::slotOnFaceSelected(int row) {
    if (row == -1) { return; }

    QString cellName = this->ui->listWidget_faces->item(row)->text();
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
    this->ui->listWidget_edges->clear();
    for (frac::Edge const& e: f.constData()) {
        this->ui->listWidget_edges->addItem(e.toString().c_str());
    }
    this->ui->listWidget_edges->setCurrentRow(0);
}

[[maybe_unused]] void MainWindow::slotOnEdgeSelected(int row) {
    if (row == -1) { return; }

    frac::Edge e = toEdge(this->ui->listWidget_edges->item(row)->text());
    this->ui->comboBox_currentEdgeTopology->setCurrentIndex(e.edgeType() == frac::EdgeType::CANTOR ? 0 : 1);
    this->ui->spinBox_currentEdgeNbSubdivisions->setValue(static_cast<int>(e.nbSubdivisions()));
    this->ui->spinBox_currentEdgeDelay->setValue(static_cast<int>(e.delay()));
}

[[maybe_unused]] void MainWindow::slotOnFaceAdjTopologyChanged(int row) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    frac::Edge e { row == 0 ? frac::EdgeType::CANTOR : frac::EdgeType::BEZIER, f.adjEdge().nbSubdivisions(), f.adjEdge().delay() };
    f.setAdjEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceAdjNbSubdivisionsChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    frac::Edge e { f.adjEdge().edgeType(), static_cast<unsigned int>(value), f.adjEdge().delay() };
    f.setAdjEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceAdjDelayChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    frac::Edge e { f.adjEdge().edgeType(), f.adjEdge().nbSubdivisions(), static_cast<unsigned int>(value) };
    f.setAdjEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceGapTopologyChanged(int row) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    frac::Edge e { row == 0 ? frac::EdgeType::CANTOR : frac::EdgeType::BEZIER, f.gapEdge().nbSubdivisions(), f.gapEdge().delay() };
    f.setGapEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceGapNbSubdivisionsChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    frac::Edge e { f.gapEdge().edgeType(), static_cast<unsigned int>(value), f.gapEdge().delay() };
    f.setGapEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceGapDelayChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    frac::Edge e { f.gapEdge().edgeType(), f.gapEdge().nbSubdivisions(), static_cast<unsigned int>(value) };
    f.setGapEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceReqTopologyChanged(int row) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    frac::Edge e { row == 0 ? frac::EdgeType::CANTOR : frac::EdgeType::BEZIER, f.reqEdge().nbSubdivisions(), f.reqEdge().delay() };
    f.setReqEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceReqNbSubdivisionsChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    frac::Edge e { f.reqEdge().edgeType(), static_cast<unsigned int>(value), f.reqEdge().delay() };
    f.setReqEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceReqDelayChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    frac::Edge e { f.reqEdge().edgeType(), f.reqEdge().nbSubdivisions(), static_cast<unsigned int>(value) };
    f.setReqEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnFaceDelayChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    f.setDelay(value);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void MainWindow::slotAddEdge() {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    frac::Edge e { frac::EdgeType::CANTOR, 2, 0 };
    auto it = f.data().begin();
    it += this->ui->listWidget_edges->currentRow() + 1;
    f.data().emplace(it, e);
    int oldRow = this->ui->listWidget_edges->currentRow();
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
    MainWindow::slotOnFaceSelected(this->ui->listWidget_faces->currentRow());
    this->ui->listWidget_edges->setCurrentRow(oldRow + 1);
    this->updateEnablement();
}

[[maybe_unused]] void MainWindow::slotRemoveEdge() {
    if (this->ui->listWidget_edges->count() == 3) { return; }
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    long int indexToRemove = this->ui->listWidget_edges->currentRow();
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
    int oldRow = this->ui->listWidget_edges->currentRow();
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
    MainWindow::slotOnFaceSelected(this->ui->listWidget_faces->currentRow());
    this->ui->listWidget_edges->setCurrentRow(std::min(this->ui->listWidget_edges->count() - 1, oldRow));
    this->updateEnablement();
}

[[maybe_unused]] void MainWindow::slotOnSelectedEdgeTopologyChanged(int row) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    f.data().at(this->ui->listWidget_edges->currentRow()).setEdgeType(row == 0 ? frac::EdgeType::CANTOR : frac::EdgeType::BEZIER);

    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
    this->ui->listWidget_edges->currentItem()->setText(f.data().at(this->ui->listWidget_edges->currentRow()).toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnSelectedEdgeNbSubdivisionsChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    f.data().at(this->ui->listWidget_edges->currentRow()).setNbSubdivisions(static_cast<unsigned int>(value));

    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
    this->ui->listWidget_edges->currentItem()->setText(f.data().at(this->ui->listWidget_edges->currentRow()).toString().c_str());
}

[[maybe_unused]] void MainWindow::slotOnSelectedEdgeDelayChanged(int value) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    f.data().at(this->ui->listWidget_edges->currentRow()).setDelay(static_cast<unsigned int>(value));

    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
    this->ui->listWidget_edges->currentItem()->setText(f.data().at(this->ui->listWidget_edges->currentRow()).toString().c_str());
}

void MainWindow::updateEnablement() {
    //button remove face
    this->ui->pushButton_removeFace->setEnabled(this->ui->listWidget_faces->count() > 1);
    //adj edge face
    this->ui->comboBox_adjEdgeTopology->setEnabled(this->ui->listWidget_faces->currentRow() > -1);
    this->ui->spinBox_adjEdgeNbSubdivisions->setEnabled(this->ui->listWidget_faces->currentRow() > -1);
    this->ui->spinBox_adjEdgeDelay->setEnabled(this->ui->listWidget_faces->currentRow() > -1);
    //gap edge face
    this->ui->comboBox_gapEdgeTopology->setEnabled(this->ui->listWidget_faces->currentRow() > -1);
    this->ui->spinBox_gapEdgeNbSubdivisions->setEnabled(this->ui->listWidget_faces->currentRow() > -1);
    this->ui->spinBox_gapEdgeDelay->setEnabled(this->ui->listWidget_faces->currentRow() > -1);
    //req edge face
    this->ui->comboBox_reqEdgeTopology->setEnabled(this->ui->listWidget_faces->currentRow() > -1);
    this->ui->spinBox_reqEdgeNbSubdivisions->setEnabled(this->ui->listWidget_faces->currentRow() > -1);
    this->ui->spinBox_reqEdgeDelay->setEnabled(this->ui->listWidget_faces->currentRow() > -1);
    //delay face
    this->ui->spinBox_faceDelay->setEnabled(this->ui->listWidget_faces->currentRow() > -1);
    //button add and remove edges
    this->ui->pushButton_addEdge->setEnabled(this->ui->listWidget_faces->currentRow() > -1);
    this->ui->pushButton_removeEdge->setEnabled(this->ui->listWidget_edges->count() > 3);
    //edge info
    this->ui->comboBox_currentEdgeTopology->setEnabled(this->ui->listWidget_edges->currentRow() > -1);
    this->ui->spinBox_currentEdgeNbSubdivisions->setEnabled(this->ui->listWidget_edges->currentRow() > -1);
    this->ui->spinBox_currentEdgeDelay->setEnabled(this->ui->listWidget_edges->currentRow() > -1);
    //constraints
    this->ui->pushButton_addConstraint->setEnabled(this->ui->listWidget_faces->count() > 1);
    this->ui->pushButton_removeConstraint->setEnabled(this->ui->listWidget_constraints->count() > 0);
    this->ui->spinBox_constraintFace1->setEnabled(this->ui->listWidget_constraints->count() > 0);
    this->ui->spinBox_constraintFace2->setEnabled(this->ui->listWidget_constraints->count() > 0);
    this->ui->spinBox_constraintEdge1->setEnabled(this->ui->listWidget_constraints->count() > 0);
    this->ui->spinBox_constraintEdge2->setEnabled(this->ui->listWidget_constraints->count() > 0);
    //button generation
    this->ui->pushButton_generateScript->setEnabled(this->ui->listWidget_faces->currentRow() > -1);
}

[[maybe_unused]] void MainWindow::slotAddConstraint() {
    this->ui->listWidget_constraints->addItem("0.0 / 1.0");
    this->ui->listWidget_constraints->setCurrentRow(this->ui->listWidget_constraints->count() - 1);
    this->updateEnablement();
}

[[maybe_unused]] void MainWindow::slotRemoveConstraint() {
    this->ui->listWidget_constraints->takeItem(this->ui->listWidget_constraints->currentRow());
    this->updateEnablement();
}

[[maybe_unused]] void MainWindow::slotOnConstraintSelected(int row) {
    if (row == -1) { return; }
    Constraint c = MainWindow::toConstraint(this->ui->listWidget_constraints->item(row)->text());
    this->ui->spinBox_constraintFace1->setValue(static_cast<int>(c.Face1));
    this->ui->spinBox_constraintEdge1->setValue(static_cast<int>(c.Edge1));
    this->ui->spinBox_constraintFace2->setValue(static_cast<int>(c.Face2));
    this->ui->spinBox_constraintEdge2->setValue(static_cast<int>(c.Edge2));
}

MainWindow::Constraint MainWindow::toConstraint(QString const& constraintText) {
    QString sepFaces = " / ";
    QString sepFaceInfo = ".";

    QStringList splitFaces = constraintText.split(sepFaces);
    QString face1Info = splitFaces[0];
    QString face2Info = splitFaces[1];

    QStringList splitFace1 = face1Info.split(sepFaceInfo);
    QStringList splitFace2 = face2Info.split(sepFaceInfo);

    std::size_t face1 = splitFace1[0].toULong();
    std::size_t edge1 = splitFace1[1].toULong();
    std::size_t face2 = splitFace2[0].toULong();
    std::size_t edge2 = splitFace2[1].toULong();
    return { face1, edge1, face2, edge2 };
}

QString MainWindow::fromConstraint(const MainWindow::Constraint& constraint) {
    return QString::number(constraint.Face1) + "." + QString::number(constraint.Edge1) + " / " + QString::number(constraint.Face2) + "." + QString::number(constraint.Edge2);
}

[[maybe_unused]] void MainWindow::slotOnConstraintFace1Changed(int value) {
    Constraint c = toConstraint(this->ui->listWidget_constraints->currentItem()->text());
    c.Face1 = static_cast<std::size_t>(value);
    this->ui->listWidget_constraints->currentItem()->setText(MainWindow::fromConstraint(c));
}

[[maybe_unused]] void MainWindow::slotOnConstraintEdge1Changed(int value) {
    Constraint c = toConstraint(this->ui->listWidget_constraints->currentItem()->text());
    c.Edge1 = static_cast<std::size_t>(value);
    this->ui->listWidget_constraints->currentItem()->setText(MainWindow::fromConstraint(c));
}

[[maybe_unused]] void MainWindow::slotOnConstraintFace2Changed(int value) {
    Constraint c = toConstraint(this->ui->listWidget_constraints->currentItem()->text());
    c.Face2 = static_cast<std::size_t>(value);
    this->ui->listWidget_constraints->currentItem()->setText(MainWindow::fromConstraint(c));
}

[[maybe_unused]] void MainWindow::slotOnConstraintEdge2Changed(int value) {
    Constraint c = toConstraint(this->ui->listWidget_constraints->currentItem()->text());
    c.Edge2 = static_cast<std::size_t>(value);
    this->ui->listWidget_constraints->currentItem()->setText(MainWindow::fromConstraint(c));
}

void MainWindow::setError(std::string const& textError) {
    this->ui->label_log->setStyleSheet("QLabel{background-color: #ff0000; color: #fff;}");
    this->ui->label_log->setVisible(true);
    this->ui->label_log->setText(textError.c_str());
}

void MainWindow::setInfo(std::string const& textInfo) {
    this->ui->label_log->setStyleSheet("QLabel{background-color: #35a753; color: #fff;}");
    this->ui->label_log->setVisible(true);
    this->ui->label_log->setText(textInfo.c_str());
}

[[maybe_unused]] void MainWindow::slotOpenOBJFile() {
    QString file = QFileDialog::getOpenFileName(this, "Open OBJ", "", "OBJ Files (*.obj)");

    if (file != "") {
        std::cout << "[opening the file...] " << file.toStdString() << std::endl;
        poly::Mesh m {};
        poly::reader::readOBJ(file, m);
        std::cout << "[finished]" << std::endl;
        std::cout << m.toString().toStdString() << std::endl;
        std::cout.flush();
    }
}
