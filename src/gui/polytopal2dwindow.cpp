#include "gui/polytopal2dwindow.h"
#include "ui_polytopal2dwindow.h"

#include <QStatusBar>
#include <QFileDialog>
#include <QProgressBar>
#include <iostream>
#include "gui/glview.h"
#include "halfedge/objreader.h"
#include "halfedge/objwriter.h"
#include "polytopal/face.h"
#include "polytopal/structure.h"
#include "polytopal/structureprinter.h"
#include "polytopal/polytopal.h"
#include "utils/fileprinter.h"
#include "halfedge/algorithm.h"
#include "halfedge/halfedge.h"
#include "halfedge/face.h"
#include "utils/utils.h"
#include "gui/circle.h"

Polytopal2DWindow::Polytopal2DWindow(QWidget* parent) :
        QWidget(parent), ui(new Ui::Polytopal2DWindow), m_statusBar(new QStatusBar(this)),
        m_openedMesh(false), m_inversionLevel(0), m_circlesIndex(0) {
    ui->setupUi(this);

    this->updateEnablementPoly();
    m_view = new GLView(this);
    m_view->setSizePolicy(QSizePolicy(QSizePolicy::Expanding, QSizePolicy::MinimumExpanding));
    m_view->setFocusPolicy(Qt::ClickFocus);

    this->ui->verticalLayout->addWidget(m_view);

    m_statusBar->setMaximumHeight(40);
    this->ui->verticalLayout->addWidget(m_statusBar);

    connect(&m_timerCanonicalize, &QTimer::timeout, this, &Polytopal2DWindow::canonicalizeStep);

    he::Mesh sphereMesh;
    he::reader::readOBJ("../obj/unit_sphere.obj", sphereMesh);
    m_batchSphere.setSphereMesh(std::move(sphereMesh));

    m_view->addItem(&m_batchSkybox);
    m_view->addItem(&m_batchSphere);
    m_view->addItem(&m_batchDebugLine);
    m_view->addItem(&m_batchFace);
    m_view->addItem(&m_batchEdge);
    m_view->addItem(&m_batchVertex);
    m_view->addItem(&m_batchCircle);
    m_view->addItem(&m_batchCircleDual);
    m_view->addItem(&m_batchPlane);

    m_progressBar = new QProgressBar();
    m_progressBar->setRange(0, 100);
    m_statusBar->insertPermanentWidget(0, m_progressBar);

    m_colorDialog.setOptions(QColorDialog::ShowAlphaChannel | QColorDialog::DontUseNativeDialog);
    m_colorDialog.setCurrentColor(m_view->meshColor());

    connect(&m_colorDialog, &QColorDialog::currentColorChanged, m_view, &GLView::changeMeshColor);
    connect(&m_colorDialog, &QColorDialog::rejected, m_view, &GLView::restoreMeshColor);
}

Polytopal2DWindow::~Polytopal2DWindow() {
    delete ui;
}

void Polytopal2DWindow::setInfo(const std::string& textInfo, int timeoutMs) {
    m_statusBar->showMessage(textInfo.c_str(), timeoutMs);
}

void Polytopal2DWindow::setInfoAdvancement(int percent) {
    m_progressBar->setValue(percent);
}

void Polytopal2DWindow::openOBJFile(QString const& file) {
    m_timerCanonicalize.stop();
    m_progressBar->reset();
    m_step = 0;

    if (file != "") {
        this->ui->checkBox_displayMesh->setChecked(true);
        m_inversionLevel = 0;
        m_circlesIndex = 0;
        poly::Face::reset();
        m_mesh.reset();
        m_circles.clear();
        m_circlesDual.clear();
        he::reader::readOBJ(file, m_mesh);
        this->updateBatchCircles(false);
        this->updateBatchCircles(true);
        m_batchFace.setMesh(&m_mesh);
        m_batchEdge.setMesh(&m_mesh);
        m_batchVertex.setMesh(&m_mesh);
        m_batchDebugLine.clearDebugLine();
        m_view->addItem(&m_batchFace);
        m_view->addItem(&m_batchEdge);
        m_view->addItem(&m_batchVertex);
        m_view->update();
        m_openedMesh = true;
        m_canonicalized = false;
        this->updateEnablementPoly();
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotOpenOBJFile() {
    m_timerCanonicalize.stop();
    m_progressBar->reset();
    m_step = 0;

    QString file = QFileDialog::getOpenFileName(this, "Open an OBJ File...", "../obj/polyhedrons", "OBJ Files (*.obj)");

    if (file != "") {
        this->openOBJFile(file);
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotExportAllFaces() {
    poly::Structure structure { m_mesh };

    std::ostringstream info;

    try {
        poly::StructurePrinter structurePrinter(structure, this->ui->checkBox_polytopalPlanarControlPoints->isChecked(), "../output/result_poly.py");
        structurePrinter.exportStruct();
        info << "[Finished] Result in ../output/result_poly.py";
    } catch (std::runtime_error const& error) {
        info << error.what();
    }

    this->setInfo(info.str());
}

[[maybe_unused]] void Polytopal2DWindow::slotExportSelectedFace() {
    if (m_batchFace.selectedFace() == nullptr) {
        this->setInfo("[Error] You must select one face");
        return;
    }

    poly::Structure structure { m_mesh, m_batchFace.selectedFace() };

    std::ostringstream info;

    try {
        poly::StructurePrinter structurePrinter(structure, this->ui->checkBox_polytopalPlanarControlPoints->isChecked(), "../output/result_poly.py");
        structurePrinter.exportStruct();
        info << "[Finished] Result in ../output/result_poly.py";
    } catch (std::runtime_error const& error) {
        info << error.what();
    }

    this->setInfo(info.str());
}

[[maybe_unused]] void Polytopal2DWindow::slotDisplayUnitSphereChanged() {
    if (this->ui->checkBox_displayUnitSphere->isChecked()) {
        m_view->addItem(&m_batchSphere);
    } else {
        m_view->removeItem(&m_batchSphere);
    }
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotCanonizeMesh() {
    if (!m_mesh.vertices().empty() && m_step == 0) {
        m_mesh.updateDoublePosFromFloatPos();
        m_timerCanonicalize.start(0);
    }
}

void Polytopal2DWindow::canonicalizeStep() {
    std::vector<he::Point3D> oldPos;
    oldPos.reserve(m_mesh.vertices().size());
    for (he::Vertex const* v: m_mesh.vertices()) {
        oldPos.push_back(v->posD());
    }

    poly::canonicalizeMesh(m_mesh, this->ui->spinBox_canonicalizeStep->value(), this->ui->doubleSpinBox_canonicalizeForce->value(), this->ui->checkBox_canonicForm->isChecked());

    //compute the difference of positions for the point that moved the more
    double maxError = -1.0;
    for (size_t i = 0; i < m_mesh.vertices().size(); i++) {
        double error = (m_mesh.vertices()[i]->posD() - oldPos[i]).length();
        if (error > maxError) {
            maxError = error;
        }
    }
    double threshold = std::pow(10.0, -this->ui->horizontalSlider_precision->value());
    if (maxError < threshold) {
        this->setInfo("Stopped at error of " + QString::number(maxError, 'g', 3).toStdString());
        m_canonicalized = true;
        m_timerCanonicalize.stop();
        m_progressBar->reset();
        m_step = 0;
    } else {
        if (m_firstError < 0.) {
            m_firstError = maxError;
        }

        double dist = std::log(m_firstError) - std::log(threshold);
        double percent = 100.0 - 100.0 * (std::log(maxError) - std::log(threshold)) / dist;

        this->setInfoAdvancement(static_cast<int>(percent));
        this->setInfo("Step " + std::to_string(m_step) + " --- Error of " + QString::number(maxError, 'g', 3).toStdString());
        m_step++;
    }

    if (!m_circles.empty()) {
        slotDisplayAreaCircles();
        slotDisplayAreaCircles();
    }

    if (!m_circlesDual.empty()) {
        slotDisplayDualAreaCircles();
        slotDisplayDualAreaCircles();
    }

    this->updateDataMesh();
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotDisplayAreaCircles() {
    if (!m_mesh.vertices().empty()) {
        m_inversionLevel = 0;
        m_circlesIndex = 0;

        if (m_circles.empty()) {
            m_circles = poly::computeIlluminatedCircles(m_mesh);
        } else {
            m_circles.clear();
        }

        this->updateBatchCircles(false);
        m_view->update();
        this->updateEnablementPoly();
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotDisplayDualAreaCircles() {
    if (!m_mesh.vertices().empty()) {
        m_batchCircleDual.resetCircles();

        if (m_circlesDual.empty()) {
            m_circlesDual = poly::computeIlluminatedCirclesDual(m_mesh);
        } else {
            m_circlesDual.clear();
        }

        this->updateBatchCircles(true);
        m_view->update();
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotDisplayMeshClicked() {
    if (this->ui->checkBox_displayMesh->isChecked()) {
        m_view->addItem(&m_batchFace);
        m_view->addItem(&m_batchEdge);
        m_view->addItem(&m_batchVertex);
    } else {
        m_view->removeItem(&m_batchFace);
        m_view->removeItem(&m_batchEdge);
        m_view->removeItem(&m_batchVertex);
    }
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotIncreaseInversion() {
    this->increaseInversion();
}

[[maybe_unused]] void Polytopal2DWindow::slotDecreaseInversion() {
    if (m_circles.empty()) { return; }
    int inversionLevel = std::max(m_inversionLevel - 1, 0);
    m_inversionLevel = 0;
    m_circlesIndex = 0;
    m_circles = poly::computeIlluminatedCircles(m_mesh);

    for (int i = 0; i < inversionLevel; i++) {
        std::size_t index = m_circlesIndex;
        m_circlesIndex = m_circles.size();
        m_nbInversions = poly::computeInversions(m_circles, m_circlesDual, index);

        if (m_nbInversions != 0) {
            m_inversionLevel++;
        }
    }

    this->updateBatchCircles(false);
    this->setInfo("Iteration level : " + std::to_string(m_inversionLevel) + ", " + std::to_string(m_circles.size()) + " circles in total", 4000);
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotProjectCirclesClicked() {
    this->updateBatchCircles(false);
    this->updateBatchCircles(true);
    this->updateEnablementPoly();
    m_view->update();
}

void Polytopal2DWindow::updateCircles() {
    //if there were circles
    if (!m_circles.empty()) {
        int inversionLevel = m_inversionLevel;
        //clear circles
        this->slotDisplayAreaCircles();
        //set circles
        this->slotDisplayAreaCircles();

        //redo all inversions
        for (int i = 0; i < inversionLevel; i++) {
            std::size_t index = m_circlesIndex;
            m_circlesIndex = m_circles.size();
            m_nbInversions = poly::computeInversions(m_circles, m_circlesDual, index);

            if (m_nbInversions == 0) { return; }

            m_inversionLevel++;
        }

        this->updateBatchCircles(false);
    }
}

void Polytopal2DWindow::updateCirclesDual() {
    //if there were circles
    if (!m_circlesDual.empty()) {
        //clear circles
        this->slotDisplayDualAreaCircles();
        //set circles
        this->slotDisplayDualAreaCircles();

        this->updateBatchCircles(true);
    }
}

void Polytopal2DWindow::increaseInversion() {
    if (m_circles.empty() || m_circlesDual.empty()) { return; }

    std::size_t index = m_circlesIndex;
    m_circlesIndex = m_circles.size();
    m_nbInversions = poly::computeInversions(m_circles, m_circlesDual, index);

    if (m_nbInversions == 0) { return; }

    m_inversionLevel++;

    this->updateBatchCircles(false);
    this->setInfo("Iteration level : " + std::to_string(m_inversionLevel) + ", " + std::to_string(m_circles.size()) + " circles in total", 4000);
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotExportOBJ() {
    if (!m_mesh.vertices().empty()) {
        QString file = QFileDialog::getSaveFileName(this, "Choose an OBJ File...", "../obj", "OBJ Files (*.obj)");
        if (file != "") {
            he::writer::writeOBJ(file, m_mesh, m_canonicalized);
        }
    }
}

void Polytopal2DWindow::updateEnablementPoly() {
    this->ui->pushButton_ExportAll->setEnabled(m_openedMesh);
    this->ui->pushButton_ExportSelectedFace->setEnabled(m_openedMesh);
    this->ui->pushButton_canonizeMesh->setEnabled(m_openedMesh);
    this->ui->pushButton_displayCircles->setEnabled(m_openedMesh);
    this->ui->pushButton_displayCirclesDual->setEnabled(m_openedMesh);
    this->ui->pushButton_OBJFromCircles->setEnabled(!m_batchCircle.circles().empty() && this->ui->checkBox_projectCircles->isChecked());
}

[[maybe_unused]] void Polytopal2DWindow::slotUpdateLabelPrecision(int value) {
    double valD = std::pow(10.0, -value);
    this->ui->label_precision->setText(QString::number(valD, 'e', 0));
}

[[maybe_unused]] void Polytopal2DWindow::slotBarycentricSubdivision() {
    if (m_mesh.vertices().empty()) { return; }

    he::algo::barycentricSubdivision(m_mesh);

    this->ui->checkBox_displayMesh->setChecked(true);
    m_inversionLevel = 0;
    m_circlesIndex = 0;
    poly::Face::reset();
    m_circles.clear();
    m_circlesDual.clear();
    this->updateBatchCircles(false);
    this->updateBatchCircles(true);
    this->updateDataMesh();
    m_openedMesh = true;
    m_canonicalized = false;
    this->updateEnablementPoly();
    m_view->addItem(&m_batchFace);
    m_view->addItem(&m_batchEdge);
    m_view->addItem(&m_batchVertex);
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotGeneralizedBarycentricSubdivision() {
    if (m_mesh.vertices().empty()) { return; }

    he::algo::generalizedBarycentricSubdivision(m_mesh, this->ui->spinBox_cornerEdges->value(), this->ui->spinBox_edgeEdges->value());

    this->ui->checkBox_displayMesh->setChecked(true);
    m_inversionLevel = 0;
    m_circlesIndex = 0;
    poly::Face::reset();
    m_circles.clear();
    m_circlesDual.clear();
    this->updateBatchCircles(false);
    this->updateBatchCircles(true);
    this->updateDataMesh();
    m_openedMesh = true;
    m_canonicalized = false;
    this->updateEnablementPoly();
    m_view->addItem(&m_batchFace);
    m_view->addItem(&m_batchEdge);
    m_view->addItem(&m_batchVertex);
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotLoopSubdivision() {
    if (m_mesh.vertices().empty()) { return; }

    he::algo::loopSubdivision(m_mesh);

    this->ui->checkBox_displayMesh->setChecked(true);
    m_inversionLevel = 0;
    m_circlesIndex = 0;
    poly::Face::reset();
    m_circles.clear();
    m_circlesDual.clear();
    this->updateBatchCircles(false);
    this->updateBatchCircles(true);
    this->updateDataMesh();
    m_openedMesh = true;
    m_canonicalized = false;
    this->updateEnablementPoly();
    m_view->addItem(&m_batchFace);
    m_view->addItem(&m_batchEdge);
    m_view->addItem(&m_batchVertex);
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotChangeTheme() {
    float val = this->ui->checkBox_darkTheme->isChecked() ? 0.3f : 1.0f;
    m_view->setBackGroundColor(val, val, val);

    m_batchCircle.updateColorOfCircles(this->ui->checkBox_darkTheme->isChecked() ? m_colorDarkTheme : m_colorWhiteTheme);
    m_batchCircleDual.updateColorOfCircles(this->ui->checkBox_darkTheme->isChecked() ? m_colorDarkThemeDual : m_colorWhiteThemeDual);
    m_batchCircle.updateData();
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotChangeUserData() {
    switch (m_view->pickingType()) {
        case PickingType::PickingFace:
            if (m_batchFace.selectedFace() != nullptr) {
                m_batchFace.selectedFace()->setUserData(this->ui->lineEdit_userData->text());
            }
            break;
        case PickingType::PickingEdge:
            if (m_batchEdge.selectedEdge() != nullptr) {
                m_batchEdge.selectedEdge()->setUserData(this->ui->lineEdit_userData->text());
                m_batchEdge.selectedEdge()->twin()->setUserData(this->ui->lineEdit_userData->text());
            }
            break;
        case PickingType::PickingVertex:
            if (m_batchVertex.selectedVertex() != nullptr) {
                m_batchVertex.selectedVertex()->setUserData(this->ui->lineEdit_userData->text());
            }
            break;
        default:
            break;
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotChangeAllUserData() {
    switch (m_view->pickingType()) {
        case PickingType::PickingFace:
            for (he::Face* f: m_mesh.faces()) {
                f->setUserData(this->ui->lineEdit_userData->text());
            }
            break;
        case PickingType::PickingEdge:
            for (he::HalfEdge* he: m_mesh.halfEdges()) {
                he->setUserData(this->ui->lineEdit_userData->text());
            }
            break;
        case PickingType::PickingVertex:
            for (he::Vertex* v: m_mesh.vertices()) {
                v->setUserData(this->ui->lineEdit_userData->text());
            }
        default:
            break;
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotScaleUpCircles() {
    m_batchCircle.scaleCircles(static_cast<float>(this->ui->doubleSpinBox_scaleForce->value()));
    m_batchCircle.updateData();
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotScaleDownCircles() {
    m_batchCircle.scaleCircles(-static_cast<float>(this->ui->doubleSpinBox_scaleForce->value()));
    m_batchCircle.updateData();
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotOBJFromCircles() {
    if (m_circles.empty()) { return; }
    std::vector<gui::Circle> circles;
    circles.reserve(m_circles.size());
    for (poly::InversiveCoordinates const& c: m_circles) {
        circles.push_back(c.toCircle());
    }

    he::Mesh m;

    // for each circle, add its center as vertex to the mesh
    for (poly::InversiveCoordinates const& c: m_circles) {
        he::Vertex* v = new he::Vertex(c.toCircle().center(), QString::number(m.vertices().size()));
        m.append(v);
    }

    std::vector<std::pair<std::size_t, std::size_t>> listAdj;
    for (std::size_t i = 0; i < m_circles.size() - 1; i++) {
        for (std::size_t j = i + 1; j < m_circles.size(); j++) {
            if (poly::InversiveCoordinates::areExternallyTangentCircles(m_circles[i], m_circles[j], this->ui->doubleSpinBox_thresholdAdjacency->value())) {
                listAdj.emplace_back(i, j);
            }
        }
    }

    for (auto p: listAdj) {
        he::HalfEdge* he1 = new he::HalfEdge(m.vertices()[p.first], QString::number(p.first) + " " + QString::number(p.second));
        m.append(he1);
        m.vertices()[p.first]->setHalfEdge(he1);

        he::HalfEdge* he2 = new he::HalfEdge(m.vertices()[p.second], QString::number(p.second) + " " + QString::number(p.first));
        m.append(he2);
        m.vertices()[p.second]->setHalfEdge(he2);

        he1->setTwin(he2);
        he2->setTwin(he1);
    }

    // we need to set only next on all halfedges and one halfedge per face
    // if we only need to export the mesh in OBJ

    m_batchDebugLine.clearDebugLine();
    //at first, store clockwise ordered halfedges for each vertex
    //with a special case for a circle that contains all others
    std::vector<std::vector<he::HalfEdge*>> orderedHalfEdgesOfVertex;
    for (std::size_t i = 0; i < m.vertices().size(); i++) {
        he::Vertex* v = m.vertices()[i];
        std::vector<he::HalfEdge*> halfedges;
        halfedges.emplace_back(v->halfEdge());
        for (he::HalfEdge* he: v->otherHalfEdges()) {
            halfedges.emplace_back(he);
        }
        std::sort(halfedges.begin(), halfedges.end(), [&](he::HalfEdge* he1, he::HalfEdge* he2) {
            poly::InversiveCoordinates const& currentCircle = m_circles[static_cast<qsizetype>(i)];
            poly::InversiveCoordinates const& circle1 = m_circles[he1->name().split(" ")[1].toUInt()];
            poly::InversiveCoordinates const& circle2 = m_circles[he2->name().split(" ")[1].toUInt()];
            QVector3D to1 = poly::InversiveCoordinates::tangencyPoint(currentCircle, circle1).toQVector3D();
            QVector3D to2 = poly::InversiveCoordinates::tangencyPoint(currentCircle, circle2).toQVector3D();
            QVector3D from1 = he1->origin()->pos();
            QVector3D from2 = he2->origin()->pos();
            float angle1 = std::atan2(to1.y() - from1.y(), to1.x() - from1.x());
            float angle2 = std::atan2(to2.y() - from2.y(), to2.x() - from2.x());
            m_batchDebugLine.addDebugLine(from1, to1);
            m_batchDebugLine.addDebugLine(from2, to2);
            return angle1 > angle2;
        });
        orderedHalfEdgesOfVertex.emplace_back(halfedges);
    }
    m_batchDebugLine.update();
    m_view->update();

    int indexCircle = -1;
    for (std::size_t i = 0; i < m_circles.size() - 1; i++) {
        if (m_circles[i].radius() < 0) {
            indexCircle = static_cast<int>(i);
        }
    }

    std::cout << "index external circle " << indexCircle << std::endl;

    if (indexCircle != -1) {
        std::reverse(orderedHalfEdgesOfVertex[indexCircle].begin(), orderedHalfEdgesOfVertex[indexCircle].end());
    }

    // set next he on halfedges
    bool errors = false;
    for (auto const& halfedges: orderedHalfEdgesOfVertex) {
        if (halfedges.size() == 1) {
            errors = true;
            continue;
        }
        for (std::size_t j = 0; j < halfedges.size(); j++) {
            he::HalfEdge* he = halfedges[j];
            he::HalfEdge* heNext = halfedges[(j + 1) % halfedges.size()];
            heNext->twin()->setNext(he);
        }
    }
    if (errors) {
        this->setInfo("Errors on the mesh, adjacency list is not complete...");
        return;
    }

    // find faces
    std::vector<he::HalfEdge*> usedHalfEdges;
    while (usedHalfEdges.size() != m.halfEdges().size()) {
        he::HalfEdge* he = nullptr;
        for (he::HalfEdge* h: m.halfEdges()) {
            if (std::find(usedHalfEdges.begin(), usedHalfEdges.end(), h) == usedHalfEdges.end()) {
                he = h;
                break;
            }
        }
        he::HalfEdge* currentHE = he;

        he::Face* f = new he::Face(QString::number(m.faces().size()), he);
        m.append(f);

        do {
            currentHE = currentHE->next();
            usedHalfEdges.emplace_back(currentHE);
        } while (currentHE != he);
    }

    for (std::size_t i = 0; i < m.vertices().size(); i++) {
        m.vertices()[i]->setPos(m_circles[i].lightPoint().toQVector3D());
    }

    he::writer::writeOBJ("../obj/exported.obj", m);
    this->setInfo("Mesh exported to obj/exported.obj");
}

[[maybe_unused]] void Polytopal2DWindow::slotOBJOfCircles() {
    QVector<gui::Circle> circles = m_batchCircle.circles();
    if (circles.empty()) { return; }

    he::Mesh m;

    for (gui::Circle const& c: circles) {
        he::HalfEdge* firstHE = nullptr;
        he::HalfEdge* oldHE = nullptr;
        for (int i = 0; i < 360; i += 4) {
            float alpha = qDegreesToRadians(static_cast<float>(i));
            float x = c.center().x() + c.radius() * std::cos(alpha) * c.axisX().x() + c.radius() * std::sin(alpha) * c.axisY().x();
            float y = c.center().y() + c.radius() * std::cos(alpha) * c.axisX().y() + c.radius() * std::sin(alpha) * c.axisY().y();
            float z = c.center().z() + c.radius() * std::cos(alpha) * c.axisX().z() + c.radius() * std::sin(alpha) * c.axisY().z();
            he::Vertex* v = new he::Vertex(x, y, z, QString::number(m.vertices().size()));
            m.append(v);
            he::HalfEdge* he = new he::HalfEdge(v);
            m.append(he);

            if (i == 0) {
                firstHE = he;
            }
            if (i == 356) {
                he->setNext(firstHE);
            }

            if (oldHE != nullptr) {
                oldHE->setNext(he);
            }

            oldHE = he;
        }
        he::Face* f = new he::Face(QString::number(m.faces().size()), firstHE);
        m.append(f);
    }

    he::writer::writeOBJ("../obj/exported.obj", m);
    this->setInfo("Mesh exported to obj/exported.obj");
}

[[maybe_unused]] void Polytopal2DWindow::slotUpdateSkyBox(int index) {
    if (m_view == nullptr) { return; }
    switch (index) {
        case 1:
            if (!m_view->containsItem(&m_batchSkybox)) { m_view->addItem(&m_batchSkybox); }
            m_batchSkybox.setSkyBox(SkyBoxType::SkyBox1);
            break;
        case 2:
            if (!m_view->containsItem(&m_batchSkybox)) { m_view->addItem(&m_batchSkybox); }
            m_batchSkybox.setSkyBox(SkyBoxType::SkyBox2);
            break;
        default:
            if (m_view->containsItem(&m_batchSkybox)) { m_view->removeItem(&m_batchSkybox); }
            break;
    }
    m_view->update();
}

void Polytopal2DWindow::updateDataFaces() {
    m_batchFace.updateData();
}

he::Face* Polytopal2DWindow::selectedFace() {
    return m_batchFace.selectedFace();
}

void Polytopal2DWindow::setSelectedFace(int faceIndex) {
    m_batchFace.setSelectedFace(faceIndex);
    if (m_batchFace.selectedFace() != nullptr) {
        this->ui->lineEdit_userData->setText(m_batchFace.selectedFace()->userData());
        qDebug() << m_batchFace.selectedFace()->toString();
        qDebug() << "----------------";
    }
}

void Polytopal2DWindow::updateDataEdges() {
    m_batchEdge.updateData();
}

he::HalfEdge* Polytopal2DWindow::selectedEdge() {
    return m_batchEdge.selectedEdge();
}

void Polytopal2DWindow::setSelectedEdge(int edgeIndex) {
    m_batchEdge.setSelectedEdge(edgeIndex);
    if (m_batchEdge.selectedEdge() != nullptr) {
        this->ui->lineEdit_userData->setText(m_batchEdge.selectedEdge()->userData());
        qDebug() << m_batchEdge.selectedEdge()->toString();
        if (m_batchEdge.selectedEdge()->twin() != nullptr) {
            qDebug() << "---" << Qt::endl << m_batchEdge.selectedEdge()->twin()->toString();
        }
        qDebug() << "----------------";
    }
}

void Polytopal2DWindow::updateDataVertices() {
    m_batchVertex.updateData();
}

he::Vertex* Polytopal2DWindow::selectedVertex() {
    return m_batchVertex.selectedVertex();
}

he::Vertex* Polytopal2DWindow::selectedVertex2() {
    return m_batchVertex.selectedVertex2();
}

void Polytopal2DWindow::setSelectedVertex(int vertexIndex) {
    m_batchVertex.setSelectedVertex(vertexIndex);
    if (m_batchVertex.selectedVertex() != nullptr) {
        this->ui->lineEdit_userData->setText(m_batchVertex.selectedVertex()->userData());
        qDebug() << m_batchVertex.selectedVertex()->toString();
        qDebug() << "----------------";
    }
}

void Polytopal2DWindow::setSelectedVertex2(int vertexIndex) {
    m_batchVertex.setSelectedVertex2(vertexIndex);
}

void Polytopal2DWindow::setSelectedCircle(int circleIndex) {
    m_batchCircle.setSelectedCircle(circleIndex);
    if (m_batchCircle.selectedCircle() != nullptr) {
        qDebug() << "Radius:" << m_batchCircle.selectedCircle()->radius() << " real radius:" << m_circles[circleIndex - 1].radius();
        qDebug() << "----------------";
    }
}

void Polytopal2DWindow::updateDataCircles() {
    m_batchCircle.updateData();
    m_batchCircleDual.updateData();
}

he::Mesh* Polytopal2DWindow::mesh() {
    return &m_mesh;
}

void Polytopal2DWindow::updateDataMesh() {
    this->updateDataFaces();
    this->updateDataEdges();
    this->updateDataVertices();
}

void Polytopal2DWindow::updateData() {
    this->updateCirclesDual();
    this->updateCircles();
    this->updateDataMesh();
}

void Polytopal2DWindow::updateBatchCircles(bool dual) {
    if (dual) {
        m_batchCircleDual.resetCircles();
        for (poly::InversiveCoordinates const& c: m_circlesDual) {
            if (this->ui->checkBox_projectCircles->isChecked()) {
                m_batchCircleDual.addCircle(c.toCircle());
            } else {
                m_batchCircleDual.addCircle(c.inverseStereographicProject());
            }
        }
        m_batchCircleDual.updateData();
    } else {
        m_batchCircle.resetCircles();
        for (poly::InversiveCoordinates const& c: m_circles) {
            if (this->ui->checkBox_projectCircles->isChecked()) {
                m_batchCircle.addCircle(c.toCircle());
            } else {
                m_batchCircle.addCircle(c.inverseStereographicProject());
            }
        }
        m_batchCircle.updateData();
    }

    //update circles display on sphere and on plane depending on projection
    if (!this->ui->checkBox_projectCircles->isChecked() && !m_circles.empty()) {
        m_batchSphere.updateMeshData(m_circles);
        m_batchPlane.updateMeshData({});
    } else {
        m_batchSphere.updateMeshData({});
        m_batchPlane.updateMeshData(m_circles);
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotChangeMeshColor() {
    if (!m_colorDialog.isVisible()) {
        m_view->initOldMeshColor();
        m_colorDialog.setVisible(true);
    }
}

void Polytopal2DWindow::closeEvent(QCloseEvent* event) {
    if (m_colorDialog.isVisible()) {
        m_colorDialog.close();
    }
    QWidget::closeEvent(event);
}

[[maybe_unused]] void Polytopal2DWindow::slotChangeMeshTransparency(int value) {
    QColor c = m_view->meshColor();
    c.setAlpha(value);
    m_view->changeMeshColor(c);
}

[[maybe_unused]] void Polytopal2DWindow::slotScaleMesh() {
    for (he::Vertex* v: m_mesh.vertices()) {
        QVector3D pos = v->pos();
        float dist = pos.length() - 1.0f;
        pos.normalize();
        pos *= (1.0f + dist * static_cast<float>(this->ui->doubleSpinBox_scaleMesh->value()));
        v->setPos(pos, true);
    }
    this->updateData();
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotCullFaceChanged() {
    m_view->enableCullFace(this->ui->checkBox_cullFace->isChecked());
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotSphereRenderTypeChanged(int newValue) {
    m_batchSphere.setCircleRenderType(static_cast<CircleRenderType>(newValue));
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotDisplayProjectionPoint() {
    m_batchSphere.setDisplayNorth(this->ui->checkBox_displayProjectionPoint->isChecked());
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotDisplayPlane() {
    if (this->ui->checkBox_displayPlane->isChecked()) {
        m_view->addItem(&m_batchPlane);
    } else {
        m_view->removeItem(&m_batchPlane);
    }
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotDisplayPolar() {
    if (m_batchDebugLine.containsData()) {
        m_batchDebugLine.clearDebugLine();
    } else {
        std::vector<he::Point3D> vertices;
        std::vector<std::pair<std::size_t, std::size_t>> segments;
        for (he::Face const* f: m_mesh.faces()) {
            vertices.push_back(f->computePolar());
        }
        for (he::HalfEdge const* he: m_mesh.halfEdgesNoTwin()) {
            std::size_t f1 = m_mesh.indexOf(he->face()).value();
            std::size_t f2 = m_mesh.indexOf(he->twin()->face()).value();
            segments.emplace_back(f1, f2);
        }
        for (std::pair<std::size_t, std::size_t> s: segments) {
            m_batchDebugLine.addDebugLine(vertices[s.first].toQVector3D(), vertices[s.second].toQVector3D());
        }
    }
    m_batchDebugLine.update();
    m_view->update();
}
