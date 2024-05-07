#include "gui/polytopal2dwindow.h"
#include "ui_polytopal2dwindow.h"

#include <QStatusBar>
#include <QFileDialog>
#include "gui/glview.h"
#include "halfedge/objreader.h"
#include "halfedge/objwriter.h"
#include "polytopal/face.h"
#include "polytopal/circle.h"
#include "polytopal/structure.h"
#include "polytopal/structureprinter.h"
#include "polytopal/polytopal.h"
#include "utils/fileprinter.h"

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
}

Polytopal2DWindow::~Polytopal2DWindow() {
    delete ui;
}

void Polytopal2DWindow::setInfo(const std::string& textInfo, int timeoutMs) {
    m_statusBar->showMessage(textInfo.c_str(), timeoutMs);
}

[[maybe_unused]] void Polytopal2DWindow::slotOpenOBJFile() {
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
        m_modelMesh.resetCirclesDual();
        m_modelMesh.setMesh(&m_mesh);
        m_view->updateData();
        m_view->update();
        m_openedMesh = true;
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

[[maybe_unused]] void Polytopal2DWindow::slotCanonizeMesh() {
    if (!m_mesh.vertices().empty()) {
        poly::setMeshToOrigin(m_mesh);
        m_timerCanonicalize.start(0);
    }
}

void Polytopal2DWindow::canonicalizeStep() {
    std::vector<QVector3D> oldPos;
    for (auto const& v: m_mesh.vertices()) {
        oldPos.push_back(v->pos());
    }

    poly::canonicalizeMesh(m_mesh);
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
        this->setInfo("Stopped at error of " + std::to_string(maxError));
        m_timerCanonicalize.stop();
    } else {
        this->setInfo("Error of " + std::to_string(maxError));
    }
}

[[maybe_unused]] void Polytopal2DWindow::slotDisplayAreaCircles() {
    if (!m_mesh.vertices().empty()) {
        m_inversionLevel = 0;
        m_circlesIndex = 0;
        m_modelMesh.resetCircles();

        if (m_circles.empty()) {
            m_circles = poly::computeIlluminatedCircles(m_mesh);

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
            m_circlesDual = poly::computeIlluminatedCirclesDual(m_mesh);

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

    m_circles = poly::computeIlluminatedCircles(m_mesh);

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
            he::writer::writeOBJ(file, m_mesh);
        }
    }
}

void Polytopal2DWindow::updateEnablementPoly() {
    this->ui->pushButton_ExportAll->setEnabled(m_openedMesh);
    this->ui->pushButton_ExportSelectedFace->setEnabled(m_openedMesh);
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
