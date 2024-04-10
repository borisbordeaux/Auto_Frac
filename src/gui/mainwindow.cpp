#include "gui/mainwindow.h"
#include "ui_mainwindow.h"

#include "halfedge/face.h"
#include "halfedge/mesh.h"
#include "polytopal/structure.h"
#include "polytopal/structureprinter.h"
#include "utils/fileprinter.h"
#include "utils/objreader.h"
#include "utils/measures.h"
#include "computations/computation.h"
#include "utils/utils.h"

#include <QtWidgets>
#include <iostream>

#include <string>

#include "NazaraUtils/Algorithm.hpp"

#include "utils/objwriter.h"
#include "gui/persistenthomologywindow.h"
#include "gui/densitywindow.h"
#include "gui/areaperimeterwindow.h"
#include "gui/fractaldimensionwindow.h"
#include "gui/autosub2dwindow.h"

MainWindow::MainWindow(QWidget* parent) : QMainWindow(parent), ui(new Ui::MainWindow), m_openedMesh(false),
                                          m_inversionLevel(0) {
    ui->setupUi(this);


    this->updateEnablementPoly();

    m_view = new GLView(&m_modelMesh, this);
    this->ui->verticalLayout_poly2D->addWidget(m_view);


    connect(&m_timerCanonicalize, &QTimer::timeout, this, &MainWindow::canonicalizeStep);
    connect(&m_timerAnimProject, &QTimer::timeout, this, &MainWindow::animProjectStep);
    connect(&m_timerAnimInversion, &QTimer::timeout, this, &MainWindow::animInversionStep);

    m_circlesIndex = 0;

}

MainWindow::~MainWindow() {
    delete ui;
}

void MainWindow::updateEnablementPoly() {
    this->ui->pushButton_ExportAll->setEnabled(m_openedMesh);
    this->ui->pushButton_ExportSelectedFace->setEnabled(m_openedMesh);
}


void MainWindow::setInfo(std::string const& textInfo, int timeoutMs) {
    this->ui->statusBar->showMessage(textInfo.c_str(), timeoutMs);
}

[[maybe_unused]] void MainWindow::slotOpenOBJFile() {
    m_view->stopAnimation();
    QString file = QFileDialog::getOpenFileName(this, "Open an OBJ File...", "../obj", "OBJ Files (*.obj)");

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
        m_modelMesh.setMesh(&m_mesh);
        m_view->updateData();
        m_view->update();
        m_openedMesh = true;
        this->updateEnablementPoly();
    }
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

[[maybe_unused]] void MainWindow::slotDisplayUnitSphereChanged() {
    if (m_modelMesh.sphereMesh() == nullptr) {
        if (m_sphereMesh.vertices().empty()) {
            he::reader::readOBJ("../obj/unit_sphere.obj", m_sphereMesh);
        }
        m_modelMesh.setSphereMesh(&m_sphereMesh);
    } else {
        m_modelMesh.setSphereMesh(nullptr);
    }
    m_view->updateDataSphere();
    m_view->updateDataVertices(); //for projection point
    m_view->update();
}

[[maybe_unused]] void MainWindow::slotCanonizeMesh() {
    if (!m_mesh.vertices().empty()) {
        frac::Canonizer::setMeshToOrigin(m_mesh);
        m_timerCanonicalize.start(0);
    }
}

void MainWindow::canonicalizeStep() {
    std::vector<QVector3D> oldPos;
    for (auto const& v: m_mesh.vertices()) {
        oldPos.push_back(v->pos());
    }

    frac::Canonizer::canonicalizeMesh(m_mesh);
    m_modelMesh.updateDataFaces();
    m_modelMesh.updateDataEdge();
    m_modelMesh.updateDataVertices();
    m_view->updateDataFaces();
    m_view->updateDataEdge();
    m_view->updateDataVertices();
    m_view->update();

    float maxError = -1.0f;
    for (size_t i = 0; i < m_mesh.vertices().size(); i++) {
        float error = (m_mesh.vertices()[i]->pos() - oldPos[i]).length();
        if (error > maxError) {
            maxError = error;
        }
    }
    if (maxError < 0.000001f) {
        this->setInfo("stopped at error of " + std::to_string(maxError));
        m_timerCanonicalize.stop();
    }
}

[[maybe_unused]] void MainWindow::slotDisplayAreaCircles() {
    if (!m_mesh.vertices().empty()) {
        m_inversionLevel = 0;
        m_circlesIndex = 0;
        m_modelMesh.resetCircles();

        if (m_circles.empty()) {
            m_circles = frac::PolyCircle::computeIlluminatedCircles(m_mesh);
            m_circlesDual = frac::PolyCircle::computeIlluminatedCirclesDual(m_mesh);

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
        } else {
            m_circles.clear();
            m_circlesDual.clear();
        }

        m_modelMesh.updateDataCircles();
        m_view->updateDataCircles();
        m_view->update();
    }
}

[[maybe_unused]] void MainWindow::slotDisplayMeshClicked() {
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

[[maybe_unused]] void MainWindow::slotIncreaseInversion() {
    if (this->ui->checkBox_animations->isChecked()) {
        if (!m_timerAnimInversion.isActive()) {
            std::size_t index = m_circlesIndex;
            m_circlesIndex = m_circles.size();
            m_nbInversions = frac::PolyCircle::computeInversions(m_circles, m_circlesDual, index);
            m_timerAnimInversion.start();
        }
    } else {
        this->increaseInversion();
    }
}

[[maybe_unused]] void MainWindow::slotDecreaseInversion() {
    if (m_circles.empty()) { return; }
    int inversionLevel = std::max(m_inversionLevel - 1, 0);

    m_inversionLevel = 0;
    m_circlesIndex = 0;

    m_modelMesh.resetCircles();

    m_circles = frac::PolyCircle::computeIlluminatedCircles(m_mesh);
    m_circlesDual = frac::PolyCircle::computeIlluminatedCirclesDual(m_mesh);

    for (int i = 0; i < inversionLevel; i++) {
        std::size_t index = m_circlesIndex;
        m_circlesIndex = m_circles.size();
        m_nbInversions = frac::PolyCircle::computeInversions(m_circles, m_circlesDual, index);

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

    for (poly::Circle const& c: m_circlesDual) {
        if (this->ui->checkBox_projectCircles->isChecked()) {
            m_modelMesh.addCircleDual(c);
        } else {
            m_modelMesh.addCircleDual(c.inverseStereographicProject());
        }
    }

    this->setInfo("Iteration level : " + std::to_string(m_inversionLevel) + ", " + std::to_string(m_circles.size()) + " circles in total", 4000);

    m_modelMesh.updateDataCircles();
    m_view->updateDataCircles();
    m_view->update();
}

[[maybe_unused]] void MainWindow::slotProjectCirclesClicked() {
    if (this->ui->checkBox_animations->isChecked()) {
        m_circlesAnimProject = m_circles;
        m_circlesDualAnimProject = m_circlesDual;
        m_timerAnimProject.start();
    } else {
        m_modelMesh.resetCircles();

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
        m_view->updateDataCircles();
        m_view->update();
    }
}

void MainWindow::animProjectStep() {
    if (m_circles.empty()) {
        m_timerAnimProject.stop();
        return;
    }

    m_modelMesh.resetCircles();
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
    m_view->updateDataCircles();
    m_view->update();
}

void MainWindow::animInversionStep() {
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

void MainWindow::projectCirclesToPlan() {
    this->ui->checkBox_projectCircles->setChecked(!this->ui->checkBox_projectCircles->isChecked());
    m_circlesAnimProject = m_circles;
    m_circlesDualAnimProject = m_circlesDual;
    m_timerAnimProject.start();
}

void MainWindow::updateCircles() {
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
            m_nbInversions = frac::PolyCircle::computeInversions(m_circles, m_circlesDual, index);

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

            for (poly::Circle const& c: m_circlesDual) {
                if (this->ui->checkBox_projectCircles->isChecked()) {
                    m_modelMesh.addCircleDual(c);
                } else {
                    m_modelMesh.addCircleDual(c.inverseStereographicProject());
                }
            }
        }
        m_modelMesh.updateDataCircles();
    }
}

void MainWindow::increaseInversion() {
    if (m_circles.empty()) { return; }

    std::size_t index = m_circlesIndex;
    m_circlesIndex = m_circles.size();
    m_nbInversions = frac::PolyCircle::computeInversions(m_circles, m_circlesDual, index);

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

    for (poly::Circle const& c: m_circlesDual) {
        if (this->ui->checkBox_projectCircles->isChecked()) {
            m_modelMesh.addCircleDual(c);
        } else {
            m_modelMesh.addCircleDual(c.inverseStereographicProject());
        }
    }

    this->setInfo("Iteration level : " + std::to_string(m_inversionLevel) + ", " + std::to_string(m_circles.size()) + " circles in total", 4000);

    m_modelMesh.updateDataCircles();
    m_view->updateDataCircles();
    m_view->update();
}


[[maybe_unused]] void MainWindow::slotExportOBJ() {
    if (!m_mesh.vertices().empty()) {
        this->grabKeyboard();
        this->releaseKeyboard();
        QString file = QFileDialog::getSaveFileName(this, "Choose an OBJ File...", "../obj", "OBJ Files (*.obj)");
        if (file != "") {
            he::writer::writeOBJ(file, m_mesh);
        }
    }
}

[[maybe_unused]] void MainWindow::slotOpenPersistentHomologyWindow() {
    if (m_persistentHomologyWindow == nullptr || m_persistentHomologyWindow->isHidden()) {
        m_persistentHomologyWindow = std::make_unique<PersistentHomologyWindow>();
    }
    m_persistentHomologyWindow->show();
}

[[maybe_unused]] void MainWindow::slotOpenDensityWindow() {
    if (m_densityWindow == nullptr || m_densityWindow->isHidden()) {
        m_densityWindow = std::make_unique<DensityWindow>();
    }
    m_densityWindow->show();
}

[[maybe_unused]] void MainWindow::slotOpenAreaPerimeterWindow() {
    if (m_areaPerimeterWindow == nullptr || m_areaPerimeterWindow->isHidden()) {
        m_areaPerimeterWindow = std::make_unique<AreaPerimeterWindow>();
    }
    m_areaPerimeterWindow->show();
}

[[maybe_unused]] void MainWindow::slotOpenFractalDimensionWindow() {
    if (m_fractalDimensionWindow == nullptr || m_fractalDimensionWindow->isHidden()) {
        m_fractalDimensionWindow = std::make_unique<FractalDimensionWindow>();
    }
    m_fractalDimensionWindow->show();
}

[[maybe_unused]] void MainWindow::slotOpenAutoSub2DWindow() {
    if (m_autoSub2DWindow == nullptr || m_autoSub2DWindow->isHidden()) {
        m_autoSub2DWindow = std::make_unique<AutoSub2DWindow>();
    }
    m_autoSub2DWindow->show();
}
