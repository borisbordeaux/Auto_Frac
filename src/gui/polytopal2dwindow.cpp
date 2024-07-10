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
#include "polytopal/circle.h"
#include "polytopal/structure.h"
#include "polytopal/structureprinter.h"
#include "polytopal/polytopal.h"
#include "utils/fileprinter.h"
#include "halfedge/algorithm.h"
#include "halfedge/halfedge.h"

Polytopal2DWindow::Polytopal2DWindow(QWidget* parent) :
        QWidget(parent), ui(new Ui::Polytopal2DWindow), m_statusBar(new QStatusBar(this)), m_openedMesh(false),
        m_inversionLevel(0), m_circlesIndex(0) {
    ui->setupUi(this);

    this->updateEnablementPoly();
    m_view = new GLView(&m_modelMesh, this);

    this->ui->verticalLayout->addWidget(m_view);

    m_statusBar->setMaximumHeight(40);
    this->ui->verticalLayout->addWidget(m_statusBar);

    connect(&m_timerCanonicalize, &QTimer::timeout, this, &Polytopal2DWindow::canonicalizeStep);
    connect(&m_timerAnimProject, &QTimer::timeout, this, &Polytopal2DWindow::animProjectStep);
    connect(&m_timerAnimInversion, &QTimer::timeout, this, &Polytopal2DWindow::animInversionStep);

    he::reader::readOBJ("../obj/unit_sphere.obj", m_sphereMesh);
    m_modelMesh.setSphereMesh(&m_sphereMesh);
    m_view->updateDataSphere();
    m_view->updateDataVertices(); //for projection point

    m_progressBar = new QProgressBar();
    m_progressBar->setRange(0, 100);
    m_statusBar->insertPermanentWidget(0, m_progressBar);
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

[[maybe_unused]] void Polytopal2DWindow::slotOpenOBJFile() {
    m_view->stopAnimation();
    QString file = QFileDialog::getOpenFileName(this, "Open an OBJ File...", "../obj/polyhedrons", "OBJ Files (*.obj)");

    if (file != "") {
        this->ui->checkBox_displayMesh->setChecked(true);
        m_inversionLevel = 0;
        m_circlesIndex = 0;
        poly::Face::reset();
        m_mesh.reset();
        m_circles.clear();
        m_circlesDual.clear();
        he::reader::readOBJ(file, m_mesh);
        m_modelMesh.resetCircles();
        m_modelMesh.resetCirclesDual();
        m_modelMesh.setMesh(&m_mesh);
        m_view->updateData();
        m_view->update();
        m_openedMesh = true;
        m_canonicalized = false;
        this->updateEnablementPoly();

//        std::vector<he::Vertex*> vertices = m_mesh.vertices();
//        for (std::size_t i = 0; i < vertices.size(); i++) {
//            for (std::size_t j = i + 1; j < vertices.size(); j++) {
//                he::Vertex* v1 = vertices[i];
//                he::Vertex* v2 = vertices[j];
//
//                double angle = qAcos(he::Point3D::dotProduct(v1->posD(), v2->posD()) / (v1->posD().length() * v2->posD().length()));
//                std::cout << "Angle between " << v1->name().toStdString() << " and " << v2->name().toStdString() << ": " << angle << std::endl;
//            }
//        }
//        std::cout << "---------" << std::endl;
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
    if (m_modelMesh.selectedFace() == nullptr) {
        this->setInfo("[Error] You must select one face");
        return;
    }

    poly::Structure structure { m_mesh, m_modelMesh.selectedFace() };

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
    if (m_modelMesh.sphereMesh() == nullptr) {
        m_modelMesh.setSphereMesh(&m_sphereMesh);
    } else {
        m_modelMesh.setSphereMesh(nullptr);
    }
    m_view->updateDataSphere();
    m_view->updateDataVertices(); //for projection point
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotCanonizeMesh() {
    if (!m_mesh.vertices().empty() && m_step == 0) {
        m_mesh.updateDoublePosFromFloatPos();
        poly::setMeshToOrigin(m_mesh);
        m_timerCanonicalize.start(0);
    }
}

void Polytopal2DWindow::canonicalizeStep() {
    std::vector<he::Point3D> oldPos;
    for (he::Vertex const* v: m_mesh.vertices()) {
        oldPos.push_back(v->posD());
    }

    poly::canonicalizeMesh(m_mesh);

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

    m_modelMesh.updateDataFaces();
    m_modelMesh.updateDataEdge();
    m_modelMesh.updateDataVertices();
    m_view->updateDataFaces();
    m_view->updateDataEdge();
    m_view->updateDataVertices();
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotDisplayAreaCircles() {
    if (!m_mesh.vertices().empty()) {
        m_inversionLevel = 0;
        m_circlesIndex = 0;
        m_modelMesh.resetCircles();

        if (m_circles.empty()) {
            float val = this->ui->checkBox_darkTheme->isChecked() ? 1.0f : 0.0f;
            QVector3D color { val, val, val };
            m_circles = poly::computeIlluminatedCircles(m_mesh, color);

            for (poly::Circle const& c: m_circles) {
                if (this->ui->checkBox_projectCircles->isChecked()) {
                    m_modelMesh.addCircle(c);
                } else {
                    m_modelMesh.addCircle(c.inverseStereographicProject());
                }
            }
        } else {
            m_circles.clear();
        }

        m_modelMesh.updateDataCircles();
        m_view->updateDataCircles();
        m_view->update();
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotDisplayDualAreaCircles() {
    if (!m_mesh.vertices().empty()) {
        m_modelMesh.resetCirclesDual();

        if (m_circlesDual.empty()) {
            float val = this->ui->checkBox_darkTheme->isChecked() ? 1.0f : 0.0f;
            QVector3D color { val, val, val };
            m_circlesDual = poly::computeIlluminatedCirclesDual(m_mesh, color);

            for (poly::Circle const& c: m_circlesDual) {
                if (this->ui->checkBox_projectCircles->isChecked()) {
                    m_modelMesh.addCircleDual(c);
                } else {
                    m_modelMesh.addCircleDual(c.inverseStereographicProject());
                }
            }
        } else {
            m_circlesDual.clear();
        }

        m_modelMesh.updateDataCirclesDual();
        m_view->updateDataCirclesDual();
        m_view->update();
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotDisplayMeshClicked() {
    if (this->ui->checkBox_displayMesh->isChecked()) {
        m_modelMesh.setMesh(&m_mesh);
    } else {
        m_modelMesh.setMesh(nullptr);
    }
    m_view->updateDataFaces();
    m_view->updateDataEdge();
    m_view->updateDataVertices();
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotIncreaseInversion() {
    if (this->ui->checkBox_animations->isChecked()) {
        if (!m_timerAnimInversion.isActive()) {
            std::size_t index = m_circlesIndex;
            m_circlesIndex = m_circles.size();
            m_nbInversions = poly::computeInversions(m_circles, m_circlesDual, index);
            m_timerAnimInversion.start();
        }
    } else {
        this->increaseInversion();
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotDecreaseInversion() {
    if (m_circles.empty()) { return; }
    int inversionLevel = std::max(m_inversionLevel - 1, 0);

    m_inversionLevel = 0;
    m_circlesIndex = 0;

    m_modelMesh.resetCircles();

    float val = this->ui->checkBox_darkTheme->isChecked() ? 1.0f : 0.0f;
    QVector3D color { val, val, val };
    m_circles = poly::computeIlluminatedCircles(m_mesh, color);

    for (int i = 0; i < inversionLevel; i++) {
        std::size_t index = m_circlesIndex;
        m_circlesIndex = m_circles.size();
        m_nbInversions = poly::computeInversions(m_circles, m_circlesDual, index);

        if (m_nbInversions != 0) {
            m_inversionLevel++;
        }
    }

    for (poly::Circle const& c: m_circles) {
        if (this->ui->checkBox_projectCircles->isChecked()) {
            m_modelMesh.addCircle(c);
        } else {
            m_modelMesh.addCircle(c.inverseStereographicProject());
        }
    }

    this->setInfo("Iteration level : " + std::to_string(m_inversionLevel) + ", " + std::to_string(m_circles.size()) + " circles in total", 4000);

    m_modelMesh.updateDataCircles();
    m_view->updateDataCircles();
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotProjectCirclesClicked() {
    if (this->ui->checkBox_animations->isChecked()) {
        m_circlesAnimProject = m_circles;
        m_circlesDualAnimProject = m_circlesDual;
        m_timerAnimProject.start();
    } else {
        m_modelMesh.resetCircles();
        m_modelMesh.resetCirclesDual();

        for (poly::Circle const& c: m_circles) {
            if (this->ui->checkBox_projectCircles->isChecked()) {
                m_modelMesh.addCircle(c);
            } else {
                m_modelMesh.addCircle(c.inverseStereographicProject());
            }
        }

        for (poly::Circle const& c: m_circlesDual) {
            if (this->ui->checkBox_projectCircles->isChecked()) {
                m_modelMesh.addCircleDual(c);
            } else {
                m_modelMesh.addCircleDual(c.inverseStereographicProject());
            }
        }

        m_modelMesh.updateDataCircles();
        m_modelMesh.updateDataCirclesDual();
        m_view->updateDataCircles();
        m_view->updateDataCirclesDual();
        m_view->update();
    }
}

void Polytopal2DWindow::animProjectStep() {
    if (m_circles.empty()) {
        m_timerAnimProject.stop();
        return;
    }

    m_modelMesh.resetCircles();
    m_modelMesh.resetCirclesDual();
    for (size_t i = 0; i < m_circlesAnimProject.size(); i++) {
        if (!this->ui->checkBox_projectCircles->isChecked()) {
            m_circlesAnimProject[i].setRadius((1 - m_tAnimProject) * m_circles[i].radius() + m_tAnimProject * m_circles[i].inverseStereographicProject().radius());
            m_circlesAnimProject[i].setCenter((1 - m_tAnimProject) * m_circles[i].center() + m_tAnimProject * m_circles[i].inverseStereographicProject().center());
            m_circlesAnimProject[i].setAxisX((1 - m_tAnimProject) * m_circles[i].axisX() + m_tAnimProject * m_circles[i].inverseStereographicProject().axisX());
            m_circlesAnimProject[i].setAxisY((1 - m_tAnimProject) * m_circles[i].axisY() + m_tAnimProject * m_circles[i].inverseStereographicProject().axisY());
        } else {
            m_circlesAnimProject[i].setRadius((1 - m_tAnimProject) * m_circles[i].inverseStereographicProject().radius() + m_tAnimProject * m_circles[i].radius());
            m_circlesAnimProject[i].setCenter((1 - m_tAnimProject) * m_circles[i].inverseStereographicProject().center() + m_tAnimProject * m_circles[i].center());
            m_circlesAnimProject[i].setAxisX((1 - m_tAnimProject) * m_circles[i].inverseStereographicProject().axisX() + m_tAnimProject * m_circles[i].axisX());
            m_circlesAnimProject[i].setAxisY((1 - m_tAnimProject) * m_circles[i].inverseStereographicProject().axisY() + m_tAnimProject * m_circles[i].axisY());
        }
        m_modelMesh.addCircle(m_circlesAnimProject[i]);
    }

    for (size_t i = 0; i < m_circlesDual.size(); i++) {
        if (!this->ui->checkBox_projectCircles->isChecked()) {
            m_circlesDualAnimProject[i].setRadius((1 - m_tAnimProject) * m_circlesDual[i].radius() + m_tAnimProject * m_circlesDual[i].inverseStereographicProject().radius());
            m_circlesDualAnimProject[i].setCenter((1 - m_tAnimProject) * m_circlesDual[i].center() + m_tAnimProject * m_circlesDual[i].inverseStereographicProject().center());
            m_circlesDualAnimProject[i].setAxisX((1 - m_tAnimProject) * m_circlesDual[i].axisX() + m_tAnimProject * m_circlesDual[i].inverseStereographicProject().axisX());
            m_circlesDualAnimProject[i].setAxisY((1 - m_tAnimProject) * m_circlesDual[i].axisY() + m_tAnimProject * m_circlesDual[i].inverseStereographicProject().axisY());
        } else {
            m_circlesDualAnimProject[i].setRadius((1 - m_tAnimProject) * m_circlesDual[i].inverseStereographicProject().radius() + m_tAnimProject * m_circlesDual[i].radius());
            m_circlesDualAnimProject[i].setCenter((1 - m_tAnimProject) * m_circlesDual[i].inverseStereographicProject().center() + m_tAnimProject * m_circlesDual[i].center());
            m_circlesDualAnimProject[i].setAxisX((1 - m_tAnimProject) * m_circlesDual[i].inverseStereographicProject().axisX() + m_tAnimProject * m_circlesDual[i].axisX());
            m_circlesDualAnimProject[i].setAxisY((1 - m_tAnimProject) * m_circlesDual[i].inverseStereographicProject().axisY() + m_tAnimProject * m_circlesDual[i].axisY());
        }
        m_modelMesh.addCircleDual(m_circlesDualAnimProject[i]);
    }

    m_tAnimProject += 0.02f;

    if (m_tAnimProject > 1.0f) {
        m_timerAnimProject.stop();
        m_tAnimProject = 0.0f;
        m_modelMesh.resetCircles();
        m_modelMesh.resetCirclesDual();

        for (poly::Circle const& c: m_circles) {
            if (this->ui->checkBox_projectCircles->isChecked()) {
                m_modelMesh.addCircle(c);
            } else {
                m_modelMesh.addCircle(c.inverseStereographicProject());
            }
        }

        for (poly::Circle const& c: m_circlesDual) {
            if (this->ui->checkBox_projectCircles->isChecked()) {
                m_modelMesh.addCircleDual(c);
            } else {
                m_modelMesh.addCircleDual(c.inverseStereographicProject());
            }
        }
    }

    m_modelMesh.updateDataCircles();
    m_modelMesh.updateDataCirclesDual();
    m_view->updateDataCircles();
    m_view->updateDataCirclesDual();
    m_view->update();
}

void Polytopal2DWindow::animInversionStep() {
    if (m_circles.empty()) {
        m_timerAnimInversion.stop();
        return;
    }

    m_modelMesh.resetCircles();
    for (size_t i = 0; i < m_circlesIndex; i++) {
        if (this->ui->checkBox_projectCircles->isChecked()) {
            m_modelMesh.addCircle(m_circles[i]);
        } else {
            m_modelMesh.addCircle(m_circles[i].inverseStereographicProject());
        }
    }

    for (size_t i = m_circlesIndex; i < m_circles.size(); i++) {
        m_circles[i].setRadius((1 - m_tAnimInversion) * m_circles[i].oldCircleBeforeInversion().radius() + m_tAnimInversion * m_circles[i].newCircleAfterInversion().radius());
        m_circles[i].setCenter((1 - m_tAnimInversion) * m_circles[i].oldCircleBeforeInversion().center() + m_tAnimInversion * m_circles[i].newCircleAfterInversion().center());
        if (this->ui->checkBox_projectCircles->isChecked()) {
            m_modelMesh.addCircle(m_circles[i]);
        } else {
            m_circles[i].initInversiveCoordinates();
            m_modelMesh.addCircle(m_circles[i].inverseStereographicProject());
        }
    }

    for (poly::Circle const& c: m_circlesDual) {
        if (this->ui->checkBox_projectCircles->isChecked()) {
            m_modelMesh.addCircleDual(c);
        } else {
            m_modelMesh.addCircleDual(c.inverseStereographicProject());
        }
    }

    m_tAnimInversion += 0.02f;

    if (m_tAnimInversion > 1.0f) {
        m_timerAnimInversion.stop();
        m_tAnimInversion = 0.0f;
        m_modelMesh.resetCircles();

        for (size_t i = 0; i < m_circlesIndex; i++) {
            if (this->ui->checkBox_projectCircles->isChecked()) {
                m_modelMesh.addCircle(m_circles[i]);
            } else {
                m_modelMesh.addCircle(m_circles[i].inverseStereographicProject());
            }
        }

        for (size_t i = m_circlesIndex; i < m_circles.size(); i++) {
            m_circles[i].setInvertedValues();
            if (this->ui->checkBox_projectCircles->isChecked()) {
                m_modelMesh.addCircle(m_circles[i]);
            } else {
                m_modelMesh.addCircle(m_circles[i].inverseStereographicProject());
            }
        }

        for (poly::Circle const& c: m_circlesDual) {
            if (this->ui->checkBox_projectCircles->isChecked()) {
                m_modelMesh.addCircleDual(c);
            } else {
                m_modelMesh.addCircleDual(c.inverseStereographicProject());
            }
        }

        if (m_nbInversions != 0) {
            m_inversionLevel++;
        }

        this->setInfo("Iteration level : " + std::to_string(m_inversionLevel) + ", " + std::to_string(m_nbInversions) + " inversions, " + std::to_string(m_circles.size()) + " circles in total", 4000);
    }

    m_modelMesh.updateDataCircles();
    m_view->updateDataCircles();
    m_view->update();
}

void Polytopal2DWindow::projectCirclesToPlan() {
    this->ui->checkBox_projectCircles->setChecked(!this->ui->checkBox_projectCircles->isChecked());
    m_circlesAnimProject = m_circles;
    m_circlesDualAnimProject = m_circlesDual;
    m_timerAnimProject.start();
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

            m_modelMesh.resetCircles();

            for (poly::Circle const& c: m_circles) {
                if (this->ui->checkBox_projectCircles->isChecked()) {
                    m_modelMesh.addCircle(c);
                } else {
                    m_modelMesh.addCircle(c.inverseStereographicProject());
                }
            }
        }
        m_modelMesh.updateDataCircles();
    }
}

void Polytopal2DWindow::updateCirclesDual() {
    //if there were circles
    if (!m_circlesDual.empty()) {
        //clear circles
        this->slotDisplayDualAreaCircles();
        //set circles
        this->slotDisplayDualAreaCircles();

        m_modelMesh.updateDataCirclesDual();
    }
}

void Polytopal2DWindow::increaseInversion() {
    if (m_circles.empty()) { return; }

    std::size_t index = m_circlesIndex;
    m_circlesIndex = m_circles.size();
    m_nbInversions = poly::computeInversions(m_circles, m_circlesDual, index);

    if (m_nbInversions == 0) { return; }

    m_inversionLevel++;

    m_modelMesh.resetCircles();

    for (poly::Circle const& c: m_circles) {
        if (this->ui->checkBox_projectCircles->isChecked()) {
            m_modelMesh.addCircle(c);
        } else {
            m_modelMesh.addCircle(c.inverseStereographicProject());
        }
    }

    this->setInfo("Iteration level : " + std::to_string(m_inversionLevel) + ", " + std::to_string(m_circles.size()) + " circles in total", 4000);

    m_modelMesh.updateDataCircles();
    m_view->updateDataCircles();
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
}

[[maybe_unused]] void Polytopal2DWindow::slotTypeSelectionChanged(int index) {
    switch (index) {
        case 0:
            m_view->setPickingType(PickingType::PickingFace);
            break;
        case 1:
            m_view->setPickingType(PickingType::PickingEdge);
            break;
        case 2:
            m_view->setPickingType(PickingType::PickingVertex);
            break;
        default:
            break;
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotTypeRotationChanged(int index) {
    switch (index) {
        case 0:
            m_view->setRotationType(RotationType::CameraRotation);
            break;
        case 1:
            m_view->setRotationType(RotationType::PolyhedronRotation);
            break;
        default:
            break;
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotStartVideoAnimation() {
    m_view->startVideoAnimation();
}

[[maybe_unused]] void Polytopal2DWindow::slotAnimationRotation() {
    m_view->rotationAnimation();
}

[[maybe_unused]] void Polytopal2DWindow::slotUpdateLabelPrecision(int value) {
    double valD = std::pow(10.0, -value);
    this->ui->label_precision->setText(QString::number(valD, 'e', 0));
}

[[maybe_unused]] void Polytopal2DWindow::slotBarycentricSubdivision() {
    if (m_mesh.vertices().empty()) return;

    he::algo::barycentricSubdivision(m_mesh);

    this->ui->checkBox_displayMesh->setChecked(true);
    m_inversionLevel = 0;
    m_circlesIndex = 0;
    poly::Face::reset();
    m_circles.clear();
    m_circlesDual.clear();
    m_modelMesh.resetCircles();
    m_modelMesh.resetCirclesDual();
    m_modelMesh.setMesh(&m_mesh);
    m_view->updateData();
    m_view->update();
    m_openedMesh = true;
    m_canonicalized = false;
    this->updateEnablementPoly();
}

[[maybe_unused]] void Polytopal2DWindow::slotGeneralizedBarycentricSubdivision() {
    if (m_mesh.vertices().empty()) return;

    he::algo::generalizedBarycentricSubdivision(m_mesh, this->ui->spinBox_cornerEdges->value(), this->ui->spinBox_edgeEdges->value());

    this->ui->checkBox_displayMesh->setChecked(true);
    m_inversionLevel = 0;
    m_circlesIndex = 0;
    poly::Face::reset();
    m_circles.clear();
    m_circlesDual.clear();
    m_modelMesh.resetCircles();
    m_modelMesh.resetCirclesDual();
    m_modelMesh.setMesh(&m_mesh);
    m_view->updateData();
    m_view->update();
    m_openedMesh = true;
    m_canonicalized = false;
    this->updateEnablementPoly();
}

[[maybe_unused]] void Polytopal2DWindow::slotChangeTheme() {
    float val = this->ui->checkBox_darkTheme->isChecked() ? 0.0f : 1.0f;
    m_view->setBackGroundColor(val, val, val);

    val = this->ui->checkBox_darkTheme->isChecked() ? 1.0f : 0.0f;

    for (poly::Circle& c: m_circles) {
        c.setColor({ val, val, val });
    }
    for (poly::Circle& c: m_circlesDual) {
        c.setColor({ val, val, val });
    }

    m_modelMesh.updateColorOfCircles(val, val, val);
    m_view->updateDataCircles();
    m_view->updateDataCirclesDual();
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotChangeUserData() {
    if (m_modelMesh.selectedEdge() == nullptr) return;
    m_modelMesh.selectedEdge()->setUserData(this->ui->lineEdit_userData->text());
    m_modelMesh.selectedEdge()->twin()->setUserData(this->ui->lineEdit_userData->text());
}

void Polytopal2DWindow::updateUserData() {
    if (m_modelMesh.selectedEdge() == nullptr) return;
    this->ui->lineEdit_userData->setText(m_modelMesh.selectedEdge()->userData());
}

[[maybe_unused]] void Polytopal2DWindow::slotChangeAllUserData() {
    for (he::HalfEdge* he: m_mesh.halfEdges())
        he->setUserData(this->ui->lineEdit_userData->text());
}
