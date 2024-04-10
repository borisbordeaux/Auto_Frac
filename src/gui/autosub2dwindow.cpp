#include <sstream>
#include <iostream>
#include "gui/autosub2dwindow.h"
#include "ui_autosub2dwindow.h"
#include "fractal/structureprinter.h"
#include "utils/fileprinter.h"

#include <QStatusBar>


AutoSub2DWindow::AutoSub2DWindow(QWidget* parent) :
        QWidget(parent), ui(new Ui::AutoSub2DWindow), m_statusBar(new QStatusBar(this)) {
    ui->setupUi(this);

    //    //to draw frac signal
//    this->ui->listWidget_faces->addItem("C_2_1 - B_2_1 - C_2_1 - B_2_1 - C_2_1 - B_2_1 / C_2_0 - B_2_0 - B_2_0 / 1 / 1");
//    this->ui->listWidget_faces->addItem("C_2_1 - B_2_0 - C_2_1 - B_2_0 - C_2_1 - B_2_0 - C_2_0 - B_2_0 / C_2_0 - B_2_0 - B_2_0 / 0 / 1");
//    this->ui->listWidget_faces->addItem("C_2_0 - B_2_0 - C_2_0 - B_2_0 - C_2_0 - B_2_0 / C_2_0 - B_2_0 - B_2_0 / 0 / 1");
//    this->ui->listWidget_faces->setCurrentRow(this->ui->listWidget_faces->count() - 1);
//    this->ui->listWidget_constraints->addItem("1.2 / 0.0");
//    this->ui->listWidget_constraints->addItem("1.6 / 2.0");
//    this->ui->listWidget_constraints->setCurrentRow(this->ui->listWidget_constraints->count() - 1);

    // classic algo
    this->ui->listWidget_faces->addItem("C_2_0 - B_2_0 - C_2_0 - B_2_0 - C_2_0 - B_2_0 / C_2_0 - B_2_0 - B_2_0 / 0 / 1");
    this->ui->listWidget_faces->addItem("C_2_0 - C_2_0 - C_2_0 - C_2_0 - C_2_0 - C_2_0 - C_2_0 / C_2_0 - C_2_0 - C_2_0 / 0 / 1");
    this->ui->listWidget_faces->addItem("B_2_0 - B_2_0 - B_2_0 - B_2_0 - B_2_0 / B_2_0 - B_2_0 - B_2_0 / 0 / 1");
    // corner algo
    this->ui->listWidget_faces->addItem("C_2_0 - C_2_0 - C_2_0 - C_2_0 - C_2_0 / C_2_0 - C_2_0 - C_2_0 / 0 / 2");
    this->ui->listWidget_faces->addItem("B_2_0 - B_2_0 - B_2_0 - B_2_0 / B_2_0 - B_2_0 - B_2_0 / 0 / 2");
    //this->ui->listWidget_faces->addItem("B_3_0 - B_3_0 - B_3_0 - B_3_0 / B_3_0 - B_3_0 - B_3_0 / 0 / 2");
    this->ui->listWidget_faces->setCurrentRow(this->ui->listWidget_faces->count() - 1);
    // constraints to draw cells connected
    this->ui->listWidget_constraints->addItem("0.0 / 1.0");
    this->ui->listWidget_constraints->addItem("0.3 / 2.0");
    this->ui->listWidget_constraints->addItem("2.2 / 4.0");
    this->ui->listWidget_constraints->addItem("1.4 / 3.0");
    this->ui->listWidget_constraints->setCurrentRow(this->ui->listWidget_constraints->count() - 1);

    this->updateEnablement();

    connect(this->ui->spinBox_nbIterations, &QSpinBox::valueChanged, this, [&](int) { this->updateEnablement(); });
    m_CPEditor = new frac::ControlPointEditor();

    this->ui->gridLayout->addWidget(m_statusBar);

    this->setInfo("ceci est un test");
}

AutoSub2DWindow::~AutoSub2DWindow() {
    delete ui;
    delete m_CPEditor;
}

[[maybe_unused]] void AutoSub2DWindow::slotGenerateScript() {
    frac::Face::reset();
    frac::FilePrinter::reset();

    std::vector<frac::Face> faces;
    for (int i = 0; i < this->ui->listWidget_faces->count(); ++i) {
        faces.push_back(frac::Face::fromStr(this->ui->listWidget_faces->item(i)->text().toStdString()));
    }

    frac::Structure s { faces };

    for (int i = 0; i < this->ui->listWidget_constraints->count(); ++i) {
        frac::Adjacency c = toConstraint(this->ui->listWidget_constraints->item(i)->text());
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
        if (m_CPEditor->isValidForStructure(&s)) {
            frac::StructurePrinter::exportStruct(s, this->ui->checkBox_planarControlPoints->isChecked(), "../output/result.py", m_CPEditor->coordinates());
        } else {
            frac::StructurePrinter::exportStruct(s, this->ui->checkBox_planarControlPoints->isChecked(), "../output/result.py");
        }
    } catch (std::runtime_error const& error) {
        info << error.what();
    }
    info << "[Finished] Result in ../output/result.py";

    this->setInfo(info.str());
}

[[maybe_unused]] void AutoSub2DWindow::slotAddFace() {
    this->ui->listWidget_faces->addItem("C_2_0 - B_2_0 - C_2_0 - B_2_0 - C_2_0 - B_2_0 / C_2_0 - B_2_0 - B_2_0 / 0 / 1");
    this->ui->listWidget_faces->setCurrentRow(this->ui->listWidget_faces->count() - 1);
    this->updateEnablement();
}

[[maybe_unused]] void AutoSub2DWindow::slotDuplicateFace() {
    this->ui->listWidget_faces->addItem(this->ui->listWidget_faces->currentItem()->text());
    this->ui->listWidget_faces->setCurrentRow(this->ui->listWidget_faces->count() - 1);
    this->updateEnablement();
}

[[maybe_unused]] void AutoSub2DWindow::slotRemoveFace() {
    this->ui->listWidget_faces->takeItem(this->ui->listWidget_faces->currentRow());
    this->updateEnablement();
}

[[maybe_unused]] void AutoSub2DWindow::slotOnFaceSelected(int row) {
    if (row == -1) { return; }

    std::string cellName = this->ui->listWidget_faces->item(row)->text().toStdString();
    frac::Face f = frac::Face::fromStr(cellName);
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

[[maybe_unused]] void AutoSub2DWindow::slotOnEdgeSelected(int row) {
    if (row == -1) { return; }

    frac::Edge e = frac::Edge::fromStr(this->ui->listWidget_edges->item(row)->text().toStdString());
    this->ui->comboBox_currentEdgeTopology->setCurrentIndex(e.edgeType() == frac::EdgeType::CANTOR ? 0 : 1);
    this->ui->spinBox_currentEdgeNbSubdivisions->setValue(static_cast<int>(e.nbSubdivisions()));
    this->ui->spinBox_currentEdgeDelay->setValue(static_cast<int>(e.delay()));
}

[[maybe_unused]] void AutoSub2DWindow::slotOnFaceAdjTopologyChanged(int row) {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    frac::Edge e { row == 0 ? frac::EdgeType::CANTOR : frac::EdgeType::BEZIER, f.adjEdge().nbSubdivisions(), f.adjEdge().delay() };
    f.setAdjEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotOnFaceAdjNbSubdivisionsChanged(int value) {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    frac::Edge e { f.adjEdge().edgeType(), static_cast<unsigned int>(value), f.adjEdge().delay() };
    f.setAdjEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotOnFaceAdjDelayChanged(int value) {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    frac::Edge e { f.adjEdge().edgeType(), f.adjEdge().nbSubdivisions(), static_cast<unsigned int>(value) };
    f.setAdjEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotOnFaceGapTopologyChanged(int row) {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    frac::Edge e { row == 0 ? frac::EdgeType::CANTOR : frac::EdgeType::BEZIER, f.gapEdge().nbSubdivisions(), f.gapEdge().delay() };
    f.setGapEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotOnFaceGapNbSubdivisionsChanged(int value) {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    frac::Edge e { f.gapEdge().edgeType(), static_cast<unsigned int>(value), f.gapEdge().delay() };
    f.setGapEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotOnFaceGapDelayChanged(int value) {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    frac::Edge e { f.gapEdge().edgeType(), f.gapEdge().nbSubdivisions(), static_cast<unsigned int>(value) };
    f.setGapEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotOnFaceReqTopologyChanged(int row) {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    frac::Edge e { row == 0 ? frac::EdgeType::CANTOR : frac::EdgeType::BEZIER, f.reqEdge().nbSubdivisions(), f.reqEdge().delay() };
    f.setReqEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotOnFaceReqNbSubdivisionsChanged(int value) {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    frac::Edge e { f.reqEdge().edgeType(), static_cast<unsigned int>(value), f.reqEdge().delay() };
    f.setReqEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotOnFaceReqDelayChanged(int value) {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    frac::Edge e { f.reqEdge().edgeType(), f.reqEdge().nbSubdivisions(), static_cast<unsigned int>(value) };
    f.setReqEdge(e);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotOnFaceDelayChanged(int value) {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    f.setDelay(value);
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotOnFaceAlgoChanged(int row) {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    f.setAlgo(static_cast<frac::AlgorithmSubdivision>(row));
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotAddEdge() {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    frac::Edge e { frac::EdgeType::CANTOR, 2, 0 };
    auto it = f.data().begin();
    it += this->ui->listWidget_edges->currentRow() + 1;
    f.data().emplace(it, e);
    int oldRow = this->ui->listWidget_edges->currentRow();
    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
    this->slotOnFaceSelected(this->ui->listWidget_faces->currentRow());
    this->ui->listWidget_edges->setCurrentRow(oldRow + 1);
    this->updateEnablement();
}

[[maybe_unused]] void AutoSub2DWindow::slotRemoveEdge() {
    if (this->ui->listWidget_edges->count() == 3) return;
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
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
    this->slotOnFaceSelected(this->ui->listWidget_faces->currentRow());
    this->ui->listWidget_edges->setCurrentRow(std::min(this->ui->listWidget_edges->count() - 1, oldRow));
    this->updateEnablement();
}

[[maybe_unused]] void AutoSub2DWindow::slotOnSelectedEdgeTopologyChanged(int row) {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    f.data().at(this->ui->listWidget_edges->currentRow()).setEdgeType(row == 0 ? frac::EdgeType::CANTOR : frac::EdgeType::BEZIER);

    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
    this->ui->listWidget_edges->currentItem()->setText(f.data().at(this->ui->listWidget_edges->currentRow()).toString().c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotOnSelectedEdgeNbSubdivisionsChanged(int value) {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    f.data().at(this->ui->listWidget_edges->currentRow()).setNbSubdivisions(static_cast<unsigned int>(value));

    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
    this->ui->listWidget_edges->currentItem()->setText(f.data().at(this->ui->listWidget_edges->currentRow()).toString().c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotOnSelectedEdgeDelayChanged(int value) {
    if (this->ui->listWidget_faces->currentItem() == nullptr) return;
    frac::Face f = frac::Face::fromStr(this->ui->listWidget_faces->currentItem()->text().toStdString());
    f.data().at(this->ui->listWidget_edges->currentRow()).setDelay(static_cast<unsigned int>(value));

    this->ui->listWidget_faces->currentItem()->setText(f.toString().c_str());
    this->ui->listWidget_edges->currentItem()->setText(f.data().at(this->ui->listWidget_edges->currentRow()).toString().c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotAddConstraint() {
    this->ui->listWidget_constraints->addItem("0.0 / 1.0");
    this->ui->listWidget_constraints->setCurrentRow(this->ui->listWidget_constraints->count() - 1);
    this->updateEnablement();
}

[[maybe_unused]] void AutoSub2DWindow::slotRemoveConstraint() {
    this->ui->listWidget_constraints->takeItem(this->ui->listWidget_constraints->currentRow());
    this->updateEnablement();
}

[[maybe_unused]] void AutoSub2DWindow::slotOnConstraintSelected(int row) {
    if (row == -1) { return; }
    frac::Adjacency c = AutoSub2DWindow::toConstraint(this->ui->listWidget_constraints->item(row)->text());
    this->ui->spinBox_constraintFace1->setValue(static_cast<int>(c.Face1));
    this->ui->spinBox_constraintEdge1->setValue(static_cast<int>(c.Edge1));
    this->ui->spinBox_constraintFace2->setValue(static_cast<int>(c.Face2));
    this->ui->spinBox_constraintEdge2->setValue(static_cast<int>(c.Edge2));
}

[[maybe_unused]] void AutoSub2DWindow::slotOnConstraintFace1Changed(int value) {
    frac::Adjacency c = AutoSub2DWindow::toConstraint(this->ui->listWidget_constraints->currentItem()->text());
    c.Face1 = static_cast<std::size_t>(value);
    this->ui->listWidget_constraints->currentItem()->setText(AutoSub2DWindow::fromConstraint(c));
}

[[maybe_unused]] void AutoSub2DWindow::slotOnConstraintEdge1Changed(int value) {
    frac::Adjacency c = AutoSub2DWindow::toConstraint(this->ui->listWidget_constraints->currentItem()->text());
    c.Edge1 = static_cast<std::size_t>(value);
    this->ui->listWidget_constraints->currentItem()->setText(AutoSub2DWindow::fromConstraint(c));
}

[[maybe_unused]] void AutoSub2DWindow::slotOnConstraintFace2Changed(int value) {
    frac::Adjacency c = AutoSub2DWindow::toConstraint(this->ui->listWidget_constraints->currentItem()->text());
    c.Face2 = static_cast<std::size_t>(value);
    this->ui->listWidget_constraints->currentItem()->setText(AutoSub2DWindow::fromConstraint(c));
}

[[maybe_unused]] void AutoSub2DWindow::slotOnConstraintEdge2Changed(int value) {
    frac::Adjacency c = AutoSub2DWindow::toConstraint(this->ui->listWidget_constraints->currentItem()->text());
    c.Edge2 = static_cast<std::size_t>(value);
    this->ui->listWidget_constraints->currentItem()->setText(AutoSub2DWindow::fromConstraint(c));
}

[[maybe_unused]] void AutoSub2DWindow::slotEditCP() {
    frac::Face::reset();
    frac::FilePrinter::reset();

    std::vector<frac::Face> faces;
    for (int i = 0; i < this->ui->listWidget_faces->count(); ++i) {
        faces.push_back(frac::Face::fromStr(this->ui->listWidget_faces->item(i)->text().toStdString()));
    }

    frac::Structure* newStruct = new frac::Structure(faces);

    for (int i = 0; i < this->ui->listWidget_constraints->count(); ++i) {
        frac::Adjacency c = toConstraint(this->ui->listWidget_constraints->item(i)->text());
        //checks if constraint valid
        try {
            bool res = faces.at(c.Face1)[c.Edge1] == faces.at(c.Face2)[c.Edge2];
            if (!res) {
                this->setInfo("[Error] Constraint " + std::to_string(i) + " : edges are different!");
                return;
            } else {
                newStruct->addAdjacency(c.Face1, c.Edge1, c.Face2, c.Edge2);
            }
        } catch (std::out_of_range const& error) {
            this->setInfo("[Error] Constraint " + std::to_string(i) + " : faces or edges indices are not valid!");
            return;
        }
    }

    if (m_CPEditor->isValidForStructure(newStruct)) {
        delete newStruct;
    } else {
        delete m_currentStructureForCP;
        m_currentStructureForCP = newStruct;
        m_CPEditor->setStructure(m_currentStructureForCP);
    }
    m_CPEditor->show();
}

[[maybe_unused]] void AutoSub2DWindow::slotPlanarControlPointsChanged() {
    this->updateEnablement();
}

[[maybe_unused]] void AutoSub2DWindow::slotComputeNbCells() {
    // create the structure
    frac::Face::reset();
    frac::FilePrinter::reset();

    std::vector<frac::Face> faces;
    for (int i = 0; i < this->ui->listWidget_faces->count(); ++i) {
        faces.push_back(frac::Face::fromStr(this->ui->listWidget_faces->item(i)->text().toStdString()));
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
        nbCells += AutoSub2DWindow::getNbCellsOfCell(f.name(), static_cast<std::size_t>(this->ui->spinBox_nbIterations->value()), cache);
    }

    this->ui->label_nbCells->setText(std::to_string(nbCells).c_str());
}

[[maybe_unused]] void AutoSub2DWindow::slotComputeNbLacunas() {
    // create the structure
    frac::Face::reset();
    frac::FilePrinter::reset();

    std::vector<frac::Face> faces;
    for (int i = 0; i < this->ui->listWidget_faces->count(); ++i) {
        faces.push_back(frac::Face::fromStr(this->ui->listWidget_faces->item(i)->text().toStdString()));
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
        nbLacuna += AutoSub2DWindow::getNbLacunaOfCell(f.name(), static_cast<std::size_t>(this->ui->spinBox_nbIterations->value()), cacheSubdivisions, cacheLacunas);
    }
    this->ui->label_nbLacunas->setText(QString::number(nbLacuna, 'f', 1));
}

[[maybe_unused]] void AutoSub2DWindow::slotComputePorosityMetrics() {
    // create the structure
    frac::Face::reset();
    frac::FilePrinter::reset();

    std::vector<frac::Face> faces;
    for (int i = 0; i < this->ui->listWidget_faces->count(); ++i) {
        faces.push_back(frac::Face::fromStr(this->ui->listWidget_faces->item(i)->text().toStdString()));
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
            nbLacuna += AutoSub2DWindow::getNbLacunaOfCell(f.name(), static_cast<std::size_t>(i), cacheSubdivisions, cacheLacunas);
            nbCells += AutoSub2DWindow::getNbCellsOfCell(f.name(), static_cast<std::size_t>(i), cacheSubdivisions);
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

frac::Adjacency AutoSub2DWindow::toConstraint(QString const& constraintText) {
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

QString AutoSub2DWindow::fromConstraint(frac::Adjacency const& constraint) {
    return QString::number(constraint.Face1) + "." + QString::number(constraint.Edge1) + " / " + QString::number(constraint.Face2) + "." + QString::number(constraint.Edge2);
}

std::size_t AutoSub2DWindow::getNbCellsOfCell(std::string const& faceName, std::size_t level, std::unordered_map<std::string, std::unordered_map<std::string, std::size_t>>& cacheSubdivisions) {
    if (level == 0) {
        return 1;
    } else {
        // level more than 0, so we need to iterate through cacheSubdivisions
        std::size_t sum = 0;
        for (auto const& val: cacheSubdivisions[faceName]) {
            sum += val.second * AutoSub2DWindow::getNbCellsOfCell(val.first, level - 1, cacheSubdivisions);
        }
        return sum;
    }
}

double AutoSub2DWindow::getNbLacunaOfCell(std::string const& faceName, std::size_t level, std::unordered_map<std::string, std::unordered_map<std::string, std::size_t>>& cacheSubdivisions, std::unordered_map<std::string, double>& cacheLacunas) {
    if (level == 0) {
        return 0.0;
    } else {
        // level more than 0, so we need to iterate through cacheSubdivisions
        double sum = cacheLacunas[faceName];
        for (auto const& val: cacheSubdivisions[faceName]) {
            sum += static_cast<double>(val.second) * AutoSub2DWindow::getNbLacunaOfCell(val.first, level - 1, cacheSubdivisions, cacheLacunas);
        }
        return sum;
    }
}

void AutoSub2DWindow::updateEnablement() {
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
    this->ui->pushButton_EditCP->setEnabled(this->ui->checkBox_planarControlPoints->isChecked());
}

void AutoSub2DWindow::setInfo(std::string const& textInfo, int timeoutMs) {
    m_statusBar->showMessage(textInfo.c_str(), timeoutMs);
}
