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
#include "graph/incidencegraph.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow {
Q_OBJECT

public:
    explicit MainWindow(QWidget* parent = nullptr);
    ~MainWindow() override;

public slots:
    [[maybe_unused]] void slotGenerateScript();
    [[maybe_unused]] void slotAddFace();
    [[maybe_unused]] void slotRemoveFace();
    [[maybe_unused]] void slotOnFaceSelected(int row);
    [[maybe_unused]] void slotOnEdgeSelected(int row);
    [[maybe_unused]] void slotOnFaceAdjTopologyChanged(int row);
    [[maybe_unused]] void slotOnFaceAdjNbSubdivisionsChanged(int value);
    [[maybe_unused]] void slotOnFaceAdjDelayChanged(int value);
    [[maybe_unused]] void slotOnFaceGapTopologyChanged(int row);
    [[maybe_unused]] void slotOnFaceGapNbSubdivisionsChanged(int value);
    [[maybe_unused]] void slotOnFaceGapDelayChanged(int value);
    [[maybe_unused]] void slotOnFaceReqTopologyChanged(int row);
    [[maybe_unused]] void slotOnFaceReqNbSubdivisionsChanged(int value);
    [[maybe_unused]] void slotOnFaceReqDelayChanged(int value);
    [[maybe_unused]] void slotOnFaceDelayChanged(int value);
    [[maybe_unused]] void slotOnFaceAlgoChanged(int row);
    [[maybe_unused]] void slotAddEdge();
    [[maybe_unused]] void slotRemoveEdge();
    [[maybe_unused]] void slotOnSelectedEdgeTopologyChanged(int row);
    [[maybe_unused]] void slotOnSelectedEdgeNbSubdivisionsChanged(int value);
    [[maybe_unused]] void slotOnSelectedEdgeDelayChanged(int value);
    [[maybe_unused]] void slotAddConstraint();
    [[maybe_unused]] void slotRemoveConstraint();
    [[maybe_unused]] void slotOnConstraintSelected(int row);
    [[maybe_unused]] void slotOnConstraintFace1Changed(int value);
    [[maybe_unused]] void slotOnConstraintEdge1Changed(int value);
    [[maybe_unused]] void slotOnConstraintFace2Changed(int value);
    [[maybe_unused]] void slotOnConstraintEdge2Changed(int value);
    [[maybe_unused]] void slotOpenOBJFile();
    [[maybe_unused]] void slotExportAllFaces();
    [[maybe_unused]] void slotExportSelectedFace();
    [[maybe_unused]] void slotOpenOBJ4File();
    [[maybe_unused]] void slotComputeFractalDimension();
    [[maybe_unused]] void slotComputeAreaPerimeterPNG();
    [[maybe_unused]] void slotComputeAreaPerimeterOBJ();
    [[maybe_unused]] void slotComputeImageDensity();
    [[maybe_unused]] void slotComputeNbCells();
    [[maybe_unused]] void slotComputeNbLacunas();
    [[maybe_unused]] void slotComputePorosityMetrics();
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

private:
    struct Constraint {
        std::size_t Face1;
        std::size_t Edge1;
        std::size_t Face2;
        std::size_t Edge2;
    };
private:
    static frac::Face toFace(QString const& cellName);
    static frac::Edge toEdge(QString const& edgeName);
    static Constraint toConstraint(QString const& constraintText);
    static QString fromConstraint(Constraint const& constraint);
    static std::size_t getNbCellsOfCell(std::string const& faceName, std::size_t level, std::unordered_map<std::string, std::unordered_map<std::string, std::size_t>>& cacheSubdivisions);
    static double getNbLacunaOfCell(std::string const& faceName, std::size_t level, std::unordered_map<std::string, std::unordered_map<std::string, std::size_t>>& cacheSubdivisions, std::unordered_map<std::string, double>& cacheLacunas);
    void computeAreaPerimeter(QStringList const& files);
    void updateEnablement();
    void updateEnablementPoly();
    void setInfo(std::string const& textInfo, int timeoutMs = 2000);
    void displayGraph();

private:
    std::map<frac::Face, std::map<frac::Face, int>> m_mapSubFaces;

    Ui::MainWindow* ui;
    he::Mesh m_mesh;
    he::Mesh m_sphereMesh;
    Model m_modelMesh;
    GLView* m_view;
    bool m_openedMesh;

    graph::IncidenceGraph m_graph;
    QGraphicsScene m_scene;

    QGraphicsScene m_sceneFractalDim;
    QChart* m_chartFractalDim;

    QGraphicsScene m_sceneAreaPerimeter;
    QChart* m_chartAreaPerimeter;

    QTimer m_timerCanonicalize;

    std::vector<poly::Circle> m_circles;
    std::vector<poly::Circle> m_circlesDual;

    int m_inversionLevel;
    std::size_t m_circlesIndex;

    QTimer m_timerAnimProject;
    std::vector<poly::Circle> m_circlesAnimProjectStart;
    std::vector<poly::Circle> m_circlesDualAnimProjectStart;
    std::vector<poly::Circle> m_circlesAnimProjectEnd;
    std::vector<poly::Circle> m_circlesDualAnimProjectEnd;
    float m_tAnimProject = 0.0f;

    QTimer m_timerAnimInversion;
    float m_tAnimInversion = 0.0f;
    std::size_t m_nbInversions = 0;
};

#endif