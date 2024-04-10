#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QGraphicsScene>
#include <QChart>
#include <QTimer>

#include "fractal/edge.h"
#include "fractal/face.h"
#include "glview.h"
#include "halfedge/mesh.h"
#include "model.h"
#include "controlpointeditor.h"
#include "fractal/structure.h"

class PersistentHomologyWindow;
class DensityWindow;
class AreaPerimeterWindow;
class FractalDimensionWindow;
class AutoSub2DWindow;

namespace Ui {
class MainWindow;
}

namespace frac {
class ControlPointEditor;
}

class MainWindow : public QMainWindow {
Q_OBJECT

public:
    explicit MainWindow(QWidget* parent = nullptr);
    ~MainWindow() override;

    int inversionLevel() const { return m_inversionLevel; }

public slots:

    [[maybe_unused]] void slotOpenOBJFile();
    [[maybe_unused]] void slotExportAllFaces();
    [[maybe_unused]] void slotExportSelectedFace();
    [[maybe_unused]] void slotDisplayUnitSphereChanged();
    [[maybe_unused]] void slotCanonizeMesh();
    void canonicalizeStep();
    [[maybe_unused]] void slotDisplayAreaCircles();
    [[maybe_unused]] void slotDisplayMeshClicked();
    [[maybe_unused]] void slotIncreaseInversion();
    [[maybe_unused]] void slotDecreaseInversion();
    [[maybe_unused]] void slotProjectCirclesClicked();
    void animProjectStep();
    void animInversionStep();
    void increaseInversion();
    [[maybe_unused]] void slotExportOBJ();

    [[maybe_unused]] void slotOpenPersistentHomologyWindow();
    [[maybe_unused]] void slotOpenDensityWindow();
    [[maybe_unused]] void slotOpenAreaPerimeterWindow();
    [[maybe_unused]] void slotOpenFractalDimensionWindow();
    [[maybe_unused]] void slotOpenAutoSub2DWindow();

public:
    void projectCirclesToPlan();
    void updateCircles();

private:
    void updateEnablementPoly();
    void setInfo(std::string const& textInfo, int timeoutMs = 2000);

private:
    std::map<frac::Face, std::map<frac::Face, int>> m_mapSubFaces;

    Ui::MainWindow* ui;
    he::Mesh m_mesh;
    he::Mesh m_sphereMesh;
    Model m_modelMesh;
    GLView* m_view;
    bool m_openedMesh;

    QTimer m_timerCanonicalize;

    std::vector<poly::Circle> m_circles;
    std::vector<poly::Circle> m_circlesDual;

    int m_inversionLevel;
    std::size_t m_circlesIndex;

    QTimer m_timerAnimProject;
    std::vector<poly::Circle> m_circlesAnimProject;
    std::vector<poly::Circle> m_circlesDualAnimProject;
    float m_tAnimProject = 0.0f;

    QTimer m_timerAnimInversion;
    float m_tAnimInversion = 0.0f;
    std::size_t m_nbInversions = 0;

    std::unique_ptr<PersistentHomologyWindow> m_persistentHomologyWindow;
    std::unique_ptr<DensityWindow> m_densityWindow;
    std::unique_ptr<AreaPerimeterWindow> m_areaPerimeterWindow;
    std::unique_ptr<FractalDimensionWindow> m_fractalDimensionWindow;
    std::unique_ptr<AutoSub2DWindow> m_autoSub2DWindow;
};

#endif