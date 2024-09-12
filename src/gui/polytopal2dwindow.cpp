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
#include "halfedge/face.h"
#include "utils/utils.h"

Polytopal2DWindow::Polytopal2DWindow(QWidget* parent) :
        QWidget(parent), ui(new Ui::Polytopal2DWindow), m_statusBar(new QStatusBar(this)), m_openedMesh(false),
        m_inversionLevel(0), m_circlesIndex(0) {
    ui->setupUi(this);

    this->updateEnablementPoly();
    m_view = new GLView(&m_modelMesh, this);
    m_view->setSizePolicy(QSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding));
    m_view->setFocusPolicy(Qt::ClickFocus);

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
        m_modelMesh.resetCircles();
        m_modelMesh.resetCirclesDual();
        m_modelMesh.setMesh(&m_mesh);
        m_modelMesh.clearDebugLine();
        m_view->updateData();
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
        m_modelMesh.clearDebugLine();
        m_modelMesh.setMesh(&m_mesh);
        m_view->updateData();
        m_view->update();
        m_openedMesh = true;
        m_canonicalized = false;
        this->updateEnablementPoly();
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
        //poly::setMeshToOrigin(m_mesh);
        m_timerCanonicalize.start(0);
    }
}

void Polytopal2DWindow::canonicalizeStep() {
    std::vector<he::Point3D> oldPos;
    oldPos.reserve(m_mesh.vertices().size());
    for (he::Vertex const* v: m_mesh.vertices()) {
        oldPos.push_back(v->posD());
    }

    poly::canonicalizeMesh(m_mesh, this->ui->spinBox_canonicalizeStep->value(), this->ui->doubleSpinBox_canonicalizeForce->value());

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

    m_modelMesh.updateDataFaces();
    m_modelMesh.updateDataEdges();
    m_modelMesh.updateDataVertices();
    m_view->updateDataFaces();
    m_view->updateDataEdges();
    m_view->updateDataVertices();
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotDisplayAreaCircles() {
    if (!m_mesh.vertices().empty()) {
        m_inversionLevel = 0;
        m_circlesIndex = 0;
        m_modelMesh.resetCircles();

        if (m_circles.empty()) {
            m_circles = poly::computeIlluminatedCircles(m_mesh, this->ui->checkBox_darkTheme->isChecked() ? m_colorDarkTheme : m_colorWhiteTheme);

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
        this->updateEnablementPoly();
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotDisplayDualAreaCircles() {
    if (!m_mesh.vertices().empty()) {
        m_modelMesh.resetCirclesDual();

        if (m_circlesDual.empty()) {
            m_circlesDual = poly::computeIlluminatedCirclesDual(m_mesh, this->ui->checkBox_darkTheme->isChecked() ? m_colorDarkThemeDual : m_colorWhiteThemeDual);

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
    m_view->updateDataEdges();
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
        this->updateEnablementPoly();
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
        this->updateEnablementPoly();
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
    if (m_circles.empty() || m_circlesDual.empty()) { return; }

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
    this->ui->pushButton_OBJFromCircles->setEnabled(!m_modelMesh.circles().empty() && this->ui->checkBox_projectCircles->isChecked());
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
    if (m_mesh.vertices().empty()) { return; }

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

[[maybe_unused]] void Polytopal2DWindow::slotLoopSubdivision() {
    if (m_mesh.vertices().empty()) { return; }

    he::algo::loopSubdivision(m_mesh);

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
    float val = this->ui->checkBox_darkTheme->isChecked() ? 0.3f : 1.0f;
    m_view->setBackGroundColor(val, val, val);

    for (poly::Circle& c: m_circles) {
        c.setColor(this->ui->checkBox_darkTheme->isChecked() ? m_colorDarkTheme : m_colorWhiteTheme);
    }
    for (poly::Circle& c: m_circlesDual) {
        c.setColor(this->ui->checkBox_darkTheme->isChecked() ? m_colorDarkThemeDual : m_colorWhiteThemeDual);
    }

    m_modelMesh.updateColorOfCircles(this->ui->checkBox_darkTheme->isChecked() ? m_colorDarkTheme : m_colorWhiteTheme);
    m_modelMesh.updateColorOfCirclesDual(this->ui->checkBox_darkTheme->isChecked() ? m_colorDarkThemeDual : m_colorWhiteThemeDual);
    m_view->updateDataCircles();
    m_view->updateDataCirclesDual();
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotChangeUserData() {
    switch (m_view->pickingType()) {
        case PickingType::PickingFace:
            if (m_modelMesh.selectedFace() != nullptr) {
                m_modelMesh.selectedFace()->setUserData(this->ui->lineEdit_userData->text());
            }
            break;
        case PickingType::PickingEdge:
            if (m_modelMesh.selectedEdge() != nullptr) {
                m_modelMesh.selectedEdge()->setUserData(this->ui->lineEdit_userData->text());
                m_modelMesh.selectedEdge()->twin()->setUserData(this->ui->lineEdit_userData->text());
            }
            break;
        case PickingType::PickingVertex:
            if (m_modelMesh.selectedVertex() != nullptr) {
                m_modelMesh.selectedVertex()->setUserData(this->ui->lineEdit_userData->text());
            }
            break;
        default:
            break;
    }
}

void Polytopal2DWindow::updateUserData() {
    switch (m_view->pickingType()) {
        case PickingType::PickingFace:
            if (m_modelMesh.selectedFace() != nullptr) {
                this->ui->lineEdit_userData->setText(m_modelMesh.selectedFace()->userData());
                qDebug() << m_modelMesh.selectedFace()->toString();
                qDebug() << "----------------";
            }
            break;
        case PickingType::PickingEdge:
            if (m_modelMesh.selectedEdge() != nullptr) {
                this->ui->lineEdit_userData->setText(m_modelMesh.selectedEdge()->userData());
                qDebug() << m_modelMesh.selectedEdge()->toString();
                if (m_modelMesh.selectedEdge()->twin() != nullptr) {
                    qDebug() << "---" << Qt::endl << m_modelMesh.selectedEdge()->twin()->toString();
                }
                qDebug() << "----------------";
            }
            break;
        case PickingType::PickingVertex:
            if (m_modelMesh.selectedVertex() != nullptr) {
                this->ui->lineEdit_userData->setText(m_modelMesh.selectedVertex()->userData());
                qDebug() << m_modelMesh.selectedVertex()->toString();
                qDebug() << "----------------";
            }
            break;
        case PickingType::PickingCircle:
            if (m_modelMesh.selectedCircle() != nullptr) {
                qDebug() << "Radius: " << m_modelMesh.selectedCircle()->radius();
                qDebug() << "----------------";
            }
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
        default:
            break;
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotScaleUpCircles() {
    m_modelMesh.scaleCircles(static_cast<float>(this->ui->doubleSpinBox_scaleForce->value()));
    m_modelMesh.updateDataCircles();

    m_view->updateDataCircles();
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotScaleDownCircles() {
    m_modelMesh.scaleCircles(-static_cast<float>(this->ui->doubleSpinBox_scaleForce->value()));
    m_modelMesh.updateDataCircles();

    m_view->updateDataCircles();
    m_view->update();
}

[[maybe_unused]] void Polytopal2DWindow::slotOBJFromCircles() {
    QVector<poly::Circle> circles = m_modelMesh.circles();
    if (circles.empty()) { return; }

    he::Mesh m;

    // for each circle, add the center as vertex to the mesh
    for (poly::Circle const& c: circles) {
        he::Vertex* v = new he::Vertex(c.center().x(), c.center().y(), c.center().z(), QString::number(m.vertices().size()));
        m.append(v);
    }

    std::vector<std::pair<std::size_t, std::size_t>> listAdj;
    for (qsizetype i = 0; i < circles.size() - 1; i++) {
        for (qsizetype j = i + 1; j < circles.size(); j++) {
            if (poly::Circle::areExternallyTangentCircles(circles[i], circles[j])) {
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
            poly::Circle const& currentCircle = circles[static_cast<qsizetype>(i)];
            poly::Circle const& circle1 = circles[he1->name().split(" ")[1].toUInt()];
            poly::Circle const& circle2 = circles[he2->name().split(" ")[1].toUInt()];
            QVector3D to1 = poly::Circle::tangencyPoint(currentCircle, circle1);
            QVector3D to2 = poly::Circle::tangencyPoint(currentCircle, circle2);
            QVector3D from1 = he1->origin()->pos();
            QVector3D from2 = he2->origin()->pos();
            float angle1 = std::atan2(to1.y() - from1.y(), to1.x() - from1.x());
            float angle2 = std::atan2(to2.y() - from2.y(), to2.x() - from2.x());
            return angle1 > angle2;
        });
        orderedHalfEdgesOfVertex.emplace_back(halfedges);
    }

    for (poly::Circle& c: circles) {
        c.initInversiveCoordinates();
    }

    std::vector<std::size_t> indicesInternallyTangent;
    for (qsizetype i = 0; i < circles.size() - 1; i++) {
        for (qsizetype j = i + 1; j < circles.size(); j++) {
            if (poly::Circle::areInternallyTangentCircles(circles[i], circles[j])) {
                indicesInternallyTangent.push_back(i);
                indicesInternallyTangent.push_back(j);
            }
        }
    }

    int indexCircle = indicesInternallyTangent.empty() ? -1 : static_cast<int>(frac::utils::findDuplicate(indicesInternallyTangent));
    std::cout << "index external circle " << indexCircle << std::endl;

    if (indexCircle != -1) {
        std::reverse(orderedHalfEdgesOfVertex[indexCircle].begin(), orderedHalfEdgesOfVertex[indexCircle].end());
    }

    // set next he on halfedges
    bool errors = false;
    m_modelMesh.clearDebugLine();
    for (auto const& halfedges: orderedHalfEdgesOfVertex) {
        if (halfedges.size() == 1) {
            errors = true;
            continue;
        }
        for (std::size_t j = 0; j < halfedges.size(); j++) {
            he::HalfEdge* he = halfedges[j];
            he::HalfEdge* heNext = halfedges[(j + 1) % halfedges.size()];
            heNext->twin()->setNext(he);
            m_modelMesh.addDebugLine(heNext->twin()->origin()->pos(), he->origin()->pos());
        }
    }
    m_view->updateDataDebugLine();
    m_view->update();
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
        m.vertices()[i]->setPos(circles[static_cast<qsizetype>(i)].vertexOfCircle());
    }

    he::writer::writeOBJ("../obj/exported.obj", m);
    this->setInfo("Mesh exported to obj/exported.obj");
}

[[maybe_unused]] void Polytopal2DWindow::slotOBJOfCircles() {
    QVector<poly::Circle> circles = m_modelMesh.circles();
    if (circles.empty()) { return; }

    he::Mesh m;

    for (poly::Circle const& c: circles) {
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
