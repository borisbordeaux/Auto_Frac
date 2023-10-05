#include "gui/mainwindow.h"
#include "ui_mainwindow.h"

#include "fractal/structure.h"
#include "fractal/structureprinter.h"
#include "graph/vertex.h"
#include "gui/vertexgraphicsitem.h"
#include "halfedge/face.h"
#include "halfedge/mesh.h"
#include "polytopal/structure.h"
#include "polytopal/structureprinter.h"
#include "utils/fileprinter.h"
#include "utils/objreader.h"
#include "utils/measures.h"
#include "computations/densitycomputation.h"
#include "utils/utils.h"

#include <QtWidgets>
#include <QPen>
#include <iostream>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>

#include <string>
#include <QScatterSeries>
#include <QValueAxis>

#include "NazaraUtils/Algorithm.hpp"

MainWindow::MainWindow(QWidget* parent) : QMainWindow(parent), ui(new Ui::MainWindow), m_openedMesh(false), m_chartFractalDim(new QChart()), m_chartAreaPerimeter(new QChart()) {
    ui->setupUi(this);

    //this->ui->listWidget_faces->addItem("C_2_1 - B_2_0 - C_2_1 - B_2_0 - C_2_1 - B_2_0 - C_2_0 - B_2_0 / C_2_0 - B_2_0 - B_2_0 / 0 / 1");
    //this->ui->listWidget_faces->addItem("C_2_1 - B_2_1 - C_2_1 - B_2_1 - C_2_1 - B_2_1 / C_2_0 - B_2_0 - B_2_0 / 1 / 1");
    //this->ui->listWidget_faces->addItem("C_2_0 - B_2_0 - C_2_0 - B_2_0 - C_2_0 - B_2_0 / C_2_0 - B_2_0 - B_2_0 / 0 / 1");
    // classic algo
    this->ui->listWidget_faces->addItem("C_2_0 - B_2_0 - C_2_0 - B_2_0 - C_2_0 - B_2_0 / C_2_0 - B_2_0 - B_2_0 / 0 / 1");
    this->ui->listWidget_faces->addItem("C_2_0 - C_2_0 - C_2_0 - C_2_0 - C_2_0 - C_2_0 - C_2_0 / C_2_0 - C_2_0 - C_2_0 / 0 / 1");
    this->ui->listWidget_faces->addItem("B_2_0 - B_2_0 - B_2_0 - B_2_0 - B_2_0 / B_2_0 - B_2_0 - B_2_0 / 0 / 1");
    // corner algo
    this->ui->listWidget_faces->addItem("C_2_0 - C_2_0 - C_2_0 - C_2_0 - C_2_0 / C_2_0 - C_2_0 - C_2_0 / 0 / 2");
    this->ui->listWidget_faces->addItem("B_2_0 - B_2_0 - B_2_0 - B_2_0 / B_2_0 - B_2_0 - B_2_0 / 0 / 2");
    this->ui->listWidget_faces->addItem("B_3_0 - B_3_0 - B_3_0 - B_3_0 / B_3_0 - B_3_0 - B_3_0 / 0 / 2");
    this->ui->listWidget_faces->setCurrentRow(this->ui->listWidget_faces->count() - 1);

    //this->ui->listWidget_constraints->addItem("0.2 / 1.0");
    //this->ui->listWidget_constraints->addItem("0.6 / 2.0");
    //this->ui->listWidget_constraints->setCurrentRow(this->ui->listWidget_constraints->count() - 1);

    this->updateEnablement();
    this->updateEnablementPoly();

    m_view = new GLView(&m_modelMesh);
    this->ui->verticalLayout_poly2D->addWidget(m_view);
    this->ui->graphicsView->setScene(&m_scene);
    m_scene.setBackgroundBrush(Qt::white);
    m_scene.setSceneRect(10., 10., 840., 840.);

    this->ui->graphicsView_fractalDim->setScene(&m_sceneFractalDim);
    m_chartFractalDim->setTheme(QChart::ChartTheme::ChartThemeDark);
    m_chartFractalDim->legend()->hide();
    m_chartFractalDim->setTitle("Fractal Dimension");
    m_chartFractalDim->setPreferredSize(845, 845);
    m_chartFractalDim->setAnimationOptions(QChart::AnimationOption::AllAnimations);
    m_chartFractalDim->setAnimationDuration(1000);
    m_sceneFractalDim.addItem(m_chartFractalDim);

    this->ui->graphicsView_stats->setScene(&m_sceneAreaPerimeter);
    m_chartAreaPerimeter->setTheme(QChart::ChartTheme::ChartThemeDark);
    m_chartAreaPerimeter->setTitle("Area and Perimeter");
    m_chartAreaPerimeter->setPreferredSize(845, 845);
    m_chartAreaPerimeter->setAnimationOptions(QChart::AnimationOption::AllAnimations);
    m_chartAreaPerimeter->setAnimationDuration(1000);
    m_sceneAreaPerimeter.addItem(m_chartAreaPerimeter);

    connect(this->ui->horizontalSlider_windowSize, &QSlider::valueChanged, this->ui->label_windowSize, qOverload<int>(&QLabel::setNum));
    connect(this->ui->horizontalSlider_windowSize, &QSlider::sliderMoved, this, [&](int value) {
        if (value % 2 == 0) {
            this->ui->horizontalSlider_windowSize->setValue(value - 1);
        }
    });
    connect(this->ui->spinBox_nbIterations, &QSpinBox::valueChanged, this, [&](int) { updateEnablement(); });
}

MainWindow::~MainWindow() {
    delete ui;
}

[[maybe_unused]] void MainWindow::slotGenerateScript() {
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
                this->setInfo("[Error] Constraint " + std::to_string(i) + " : edges are different!");
                return;
            } else {
                s.addAdjacency(c.Face1, c.Edge1, c.Face2, c.Edge2);
            }
        } catch (std::out_of_range const& error) {
            this->setInfo("[Error] Constraint " + std::to_string(i) + " : faces or edges indices are not valid!");
            return;
        }
    }

    std::ostringstream info;

    try {
        frac::StructurePrinter::exportStruct(s, this->ui->checkBox_planarControlPoints->isChecked(), "../output/result.py");
    } catch (std::runtime_error const& error) {
        info << error.what();
    }
    info << "[Finished] Result in ../output/result.py";

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

    frac::AlgorithmSubdivision algo = static_cast<frac::AlgorithmSubdivision>(splitCellName[3].toUInt());
    return frac::Face(edges, delay, adjEdge, gapEdge, reqEdge, algo);
}

[[maybe_unused]] void MainWindow::slotAddFace() {
    this->ui->listWidget_faces->addItem("C_2_0 - B_2_0 - C_2_0 - B_2_0 - C_2_0 - B_2_0 / C_2_0 - B_2_0 - B_2_0 / 0 / 1");
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
    //algo
    this->ui->comboBox_algorithm->setCurrentIndex(static_cast<int>(f.algo()));
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

[[maybe_unused]] void MainWindow::slotOnFaceAlgoChanged(int row) {
    frac::Face f = MainWindow::toFace(this->ui->listWidget_faces->currentItem()->text());
    f.setAlgo(static_cast<frac::AlgorithmSubdivision>(row));
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
    //compute cells and lacunas
    this->ui->pushButton_computeNbCells->setEnabled(this->ui->listWidget_faces->count() > 0);
    this->ui->pushButton_computeNbLacunas->setEnabled(this->ui->listWidget_faces->count() > 0);
    this->ui->pushButton_computePorosity->setEnabled(this->ui->spinBox_nbIterations->value() > 1);
    //button generation
    this->ui->pushButton_generateScript->setEnabled(this->ui->listWidget_faces->currentRow() > -1);
}

void MainWindow::updateEnablementPoly() {
    this->ui->pushButton_changeSelectionMode->setEnabled(m_openedMesh);
    this->ui->pushButton_ExportAll->setEnabled(m_openedMesh);
    this->ui->pushButton_ExportSelectedFace->setEnabled(m_openedMesh);
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

void MainWindow::setInfo(std::string const& textInfo) {
    this->ui->statusBar->showMessage(textInfo.c_str(), 2000);
}

[[maybe_unused]] void MainWindow::slotOpenOBJFile() {
    QString file = QFileDialog::getOpenFileName(this, "Open an OBJ File...", "../obj", "OBJ Files (*.obj)");

    if (file != "") {
        poly::Face::reset();
        m_mesh.reset();
        he::reader::readOBJ(file, m_mesh);
        m_modelMesh.setMesh(&m_mesh);
        m_view->meshChanged();
        m_openedMesh = true;
        this->updateEnablementPoly();
    }
}

[[maybe_unused]] void MainWindow::slotChangeSelectionMode() {
    m_view->changeSelectionMode();
    this->ui->pushButton_changeSelectionMode->setText(m_view->selectionMode() == SelectionMode::FACES ? "Selection Mode: Faces" : "Selection Mode: Edges");
}

[[maybe_unused]] void MainWindow::slotExportAllFaces() {
    poly::Structure structure { m_mesh };
    frac::FilePrinter::reset();

    std::ostringstream info;

    try {
        poly::StructurePrinter::exportStruct(structure, this->ui->checkBox_polytopalPlanarControlPoints->isChecked(), "../output/result_poly.py");
    } catch (std::runtime_error const& error) {
        info << error.what();
    }

    info << "[Finished] Result in ../output/result_poly.py";
    this->setInfo(info.str());
}

[[maybe_unused]] void MainWindow::slotExportSelectedFace() {
    if (m_modelMesh.selectedFace() == nullptr) {
        this->setInfo("[Error] You must select one face");
        return;
    }

    poly::Structure structure { m_mesh, m_modelMesh.selectedFace() };
    frac::FilePrinter::reset();

    std::ostringstream info;

    try {
        poly::StructurePrinter::exportStruct(structure, this->ui->checkBox_polytopalPlanarControlPoints->isChecked(), "../output/result_poly.py");
    } catch (std::runtime_error const& error) {
        info << error.what();
    }

    info << "[Finished] Result in ../output/result_poly.py";
    this->setInfo(info.str());
}

[[maybe_unused]] void MainWindow::slotOpenOBJ4File() {
    QString file = QFileDialog::getOpenFileName(this, "Open an OBJ4 File...", "../obj", "OBJ4 Files (*.obj4)");

    if (file != "") {
        m_graph.reset();
        graph::reader::readOBJ4(file, m_graph);
        std::cout << m_graph << std::endl;
    }

    m_graph.updateVerticesPositions(this->ui->graphicsView->width());

    this->displayGraph();
}

void MainWindow::displayGraph() {
    m_scene.clear();

    QPen penLine;
    penLine.setWidth(1);
    penLine.setColor(Qt::black);

    //first draw lines
    for (graph::Vertex* v: m_graph.getVertices()) {
        for (graph::Vertex* p: v->getParents()) {
            m_scene.addLine(v->getX(), v->getY(), p->getX(), p->getY(), penLine);
        }
    }
    for (graph::Vertex* v: m_graph.getEdges()) {
        for (graph::Vertex* p: v->getParents()) {
            m_scene.addLine(v->getX(), v->getY(), p->getX(), p->getY(), penLine);
        }
    }
    for (graph::Vertex* v: m_graph.getFaces()) {
        for (graph::Vertex* p: v->getParents()) {
            m_scene.addLine(v->getX(), v->getY(), p->getX(), p->getY(), penLine);
        }
    }

    // then draw vertices
    for (graph::Vertex* v: m_graph.getVertices()) {
        m_scene.addItem(v->graphicsItem());
    }
    for (graph::Vertex* v: m_graph.getEdges()) {
        m_scene.addItem(v->graphicsItem());
    }
    for (graph::Vertex* v: m_graph.getFaces()) {
        m_scene.addItem(v->graphicsItem());
    }
    for (graph::Vertex* v: m_graph.getVolumes()) {
        m_scene.addItem(v->graphicsItem());
    }

    m_scene.update();
}

[[maybe_unused]] void MainWindow::slotComputeFractalDimension() {
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

        std::vector<int> res = frac::utils::computeFractalDimension(img);

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
        QValueAxis * xAxis = dynamic_cast<QValueAxis*>(m_chartFractalDim->axes(Qt::Horizontal, series).first());
        QValueAxis * yAxis = dynamic_cast<QValueAxis*>(m_chartFractalDim->axes(Qt::Vertical, series).first());
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

void MainWindow::computeAreaPerimeter(QStringList const& files) {
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
    QValueAxis * xAxis = dynamic_cast<QValueAxis*>(m_chartAreaPerimeter->axes(Qt::Horizontal).first());
    QValueAxis * yAxis = dynamic_cast<QValueAxis*>(m_chartAreaPerimeter->axes(Qt::Vertical).first());
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

[[maybe_unused]] void MainWindow::slotComputeAreaPerimeterPNG() {
    QStringList files = QFileDialog::getOpenFileNames(this, "Open PNG Files...", "../img", "PNG Files (*.png)", nullptr, QFileDialog::DontUseNativeDialog);
    if (!files.isEmpty()) {
        cv::destroyAllWindows();
        this->computeAreaPerimeter(files);
    }
}

[[maybe_unused]] void MainWindow::slotComputeAreaPerimeterOBJ() {
    QStringList files = QFileDialog::getOpenFileNames(this, "Open OBJ Files...", "../obj", "OBJ Files (*.obj)", nullptr);//, QFileDialog::DontUseNativeDialog);
    if (!files.isEmpty()) {
        this->computeAreaPerimeter(files);
    }
}

[[maybe_unused]] void MainWindow::slotComputeImageDensity() {
    QString file = QFileDialog::getOpenFileName(this, "Open a PNG File...", "../img", "PNG Files (*.png)", nullptr, QFileDialog::DontUseNativeDialog);

    if (file != "") {
        frac::DensityComputation::computeDensity(file, this->ui->horizontalSlider_windowSize->value(), this->ui->checkBox_showDensityImages->isChecked());
    }
}

[[maybe_unused]] void MainWindow::slotComputeNbCells() {
    // create the structure
    frac::Face::reset();
    frac::FilePrinter::reset();

    std::vector<frac::Face> faces;
    for (int i = 0; i < this->ui->listWidget_faces->count(); ++i) {
        faces.push_back(toFace(this->ui->listWidget_faces->item(i)->text()));
    }

    frac::Structure s { faces };

    // need to store for each face the number of subdivisions and their type (their face)
    std::unordered_map<std::string, std::unordered_map<std::string, std::size_t>> cache;

    for (frac::Face const& f: s.allFaces()) {
        std::unordered_map<std::string, std::size_t> map;
        // get the number of each kind of subdivision
        for (frac::Face const& sub: f.subdivisions()) {
            if (map.find(sub.name()) != map.end()) {
                map[sub.name()]++;
            } else {
                map[sub.name()] = 1;
            }
        }
        cache[f.name()] = map;
    }

    std::size_t nbCells = 0;
    for (auto const& f: s.faces()) {
        nbCells += MainWindow::getNbCellsOfCell(f.name(), static_cast<std::size_t>(this->ui->spinBox_nbIterations->value()), cache);
    }

    this->ui->label_nbCells->setText(std::to_string(nbCells).c_str());
}

[[maybe_unused]] void MainWindow::slotComputeNbLacunas() {
    // create the structure
    frac::Face::reset();
    frac::FilePrinter::reset();

    std::vector<frac::Face> faces;
    for (int i = 0; i < this->ui->listWidget_faces->count(); ++i) {
        faces.push_back(toFace(this->ui->listWidget_faces->item(i)->text()));
    }

    frac::Structure s { faces };

    // need to store for each face the number of subdivisions and their type (their face)
    std::unordered_map<std::string, std::unordered_map<std::string, std::size_t>> cacheSubdivisions;
    std::unordered_map<std::string, double> cacheLacunas;

    for (frac::Face const& f: s.allFaces()) {
        // fill the cache subdivision
        std::unordered_map<std::string, std::size_t> map;
        // get the number of each kind of subdivision
        for (frac::Face const& sub: f.subdivisions()) {
            if (map.find(sub.name()) != map.end()) {
                map[sub.name()]++;
            } else {
                map[sub.name()] = 1;
            }
        }
        cacheSubdivisions[f.name()] = map;

        // fill the cache lacunas
        double nbLacunas = 0.0;
        // if face have delay, it has no lacuna
        if (f.delay() == 0) {
            // if face have no delay, it has one central lacuna
            nbLacunas = 1.0;
        }
        // then +0.5 for each lacuna due to cantor edges
        for (frac::Edge const& e: f.constData()) {
            if (e.edgeType() == frac::EdgeType::CANTOR) {
                // don't check if delay on edge because actual subdivisions will do this for us
                nbLacunas += 0.5 * static_cast<double>(e.nbActualSubdivisions() - 1);
            }
        }

        cacheLacunas[f.name()] = nbLacunas;
    }

    double nbLacuna = 0.0;
    for (auto const& f: s.faces()) {
        nbLacuna += MainWindow::getNbLacunaOfCell(f.name(), static_cast<std::size_t>(this->ui->spinBox_nbIterations->value()), cacheSubdivisions, cacheLacunas);
    }
    this->ui->label_nbLacunas->setText(QString::number(nbLacuna, 'f', 1));
}

std::size_t MainWindow::getNbCellsOfCell(std::string const& faceName, std::size_t level, std::unordered_map<std::string, std::unordered_map<std::string, std::size_t>>& cacheSubdivisions) {
    if (level == 0) {
        return 1;
    } else {
        // level more than 0, so we need to iterate through cacheSubdivisions
        std::size_t sum = 0;
        for (auto const& val: cacheSubdivisions[faceName]) {
            sum += val.second * MainWindow::getNbCellsOfCell(val.first, level - 1, cacheSubdivisions);
        }
        return sum;
    }
}

double MainWindow::getNbLacunaOfCell(std::string const& faceName, std::size_t level, std::unordered_map<std::string, std::unordered_map<std::string, std::size_t>>& cacheSubdivisions, std::unordered_map<std::string, double>& cacheLacunas) {
    if (level == 0) {
        return 0.0;
    } else {
        // level more than 0, so we need to iterate through cacheSubdivisions
        double sum = cacheLacunas[faceName];
        for (auto const& val: cacheSubdivisions[faceName]) {
            sum += static_cast<double>(val.second) * MainWindow::getNbLacunaOfCell(val.first, level - 1, cacheSubdivisions, cacheLacunas);
        }
        return sum;
    }
}

[[maybe_unused]] void MainWindow::slotComputePorosityMetrics() {
    // create the structure
    frac::Face::reset();
    frac::FilePrinter::reset();

    std::vector<frac::Face> faces;
    for (int i = 0; i < this->ui->listWidget_faces->count(); ++i) {
        faces.push_back(toFace(this->ui->listWidget_faces->item(i)->text()));
    }

    frac::Structure s { faces };

    // need to store for each face the number of subdivisions and their type (their face)
    std::unordered_map<std::string, std::unordered_map<std::string, std::size_t>> cacheSubdivisions;
    std::unordered_map<std::string, double> cacheLacunas;

    for (frac::Face const& f: s.allFaces()) {
        // fill the cache subdivision
        std::unordered_map<std::string, std::size_t> map;
        // get the number of each kind of subdivision
        for (frac::Face const& sub: f.subdivisions()) {
            if (map.find(sub.name()) != map.end()) {
                map[sub.name()]++;
            } else {
                map[sub.name()] = 1;
            }
        }
        cacheSubdivisions[f.name()] = map;

        // fill the cache lacunas
        double nbLacunas = 0.0;
        // if face have delay, it has no lacuna
        if (f.delay() == 0) {
            // if face have no delay, it has one central lacuna
            nbLacunas = 1.0;
            // then +0.5 for each lacuna due to cantor edges
            for (frac::Edge const& e: f.constData()) {
                if (e.edgeType() == frac::EdgeType::CANTOR) {
                    // don't check if delay because actual subdivisions will do this for us
                    nbLacunas += 0.5 * static_cast<double>(e.nbActualSubdivisions() - 1);
                }
            }
        }
        cacheLacunas[f.name()] = nbLacunas;
    }

    this->ui->tableWidget_TopoMetrics->setRowCount(this->ui->spinBox_nbIterations->value());
    for (int i = 1; i <= this->ui->spinBox_nbIterations->value(); i++) {
        double nbLacuna = 0.0;
        std::size_t nbCells = 0;
        for (auto const& f: s.faces()) {
            nbLacuna += MainWindow::getNbLacunaOfCell(f.name(), static_cast<std::size_t>(i), cacheSubdivisions, cacheLacunas);
            nbCells += MainWindow::getNbCellsOfCell(f.name(), static_cast<std::size_t>(i), cacheSubdivisions);
        }

        QTableWidgetItem* widgetL = new QTableWidgetItem();
        QTableWidgetItem* widgetC = new QTableWidgetItem();
        QTableWidgetItem* widgetR = new QTableWidgetItem();
        widgetL->setText(QString::number(nbLacuna, 'f', 1));
        widgetC->setText(QString::number(nbCells));
        widgetR->setText(std::to_string(static_cast<double>(nbLacuna) / (static_cast<double>(nbCells) + static_cast<double>(nbLacuna))).c_str());
        this->ui->tableWidget_TopoMetrics->setItem(i - 1, 0, widgetL);
        this->ui->tableWidget_TopoMetrics->setItem(i - 1, 1, widgetC);
        this->ui->tableWidget_TopoMetrics->setItem(i - 1, 2, widgetR);
    }

}
