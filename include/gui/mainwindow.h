#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QGraphicsScene>

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
    [[maybe_unused]] void slotChangeSelectionMode();
    [[maybe_unused]] void slotExportAllFaces();
    [[maybe_unused]] void slotExportSelectedFace();
    [[maybe_unused]] void slotOpenOBJ4File();
    [[maybe_unused]] void slotComputeFractalDimension();
    [[maybe_unused]] void slotComputeAreaPerimeter();
    [[maybe_unused]] void slotComputeImageDensity();
    void setImpairValuesSlider(int value);
    [[maybe_unused]] void slotComputeNbCells();
    [[maybe_unused]] void slotComputeNbLacunas();

private:
    struct Constraint {
        std::size_t Face1;
        std::size_t Edge1;
        std::size_t Face2;
        std::size_t Edge2;
    };

    [[nodiscard]] static frac::Face toFace(QString const& cellName);
    [[nodiscard]] static frac::Edge toEdge(QString const& edgeName);
    [[nodiscard]] static Constraint toConstraint(QString const& constraintText);
    [[nodiscard]] static QString fromConstraint(Constraint const& constraint);
    [[nodiscard]] static std::size_t getNbCellsOfCell(std::string const& faceName, std::size_t level, std::unordered_map<std::string, std::unordered_map<std::string, std::size_t>>& cacheSubdivisions);
    [[nodiscard]] static double getNbLacunaOfCell(std::string const& faceName, std::size_t level, std::unordered_map<std::string, std::unordered_map<std::string, std::size_t>>& cacheSubdivisions, std::unordered_map<std::string, double>& cacheLacunas);

    std::map<frac::Face, std::map<frac::Face, int>> m_mapSubFaces;

    void updateEnablement();
    void updateEnablementPoly();

    void setInfo(std::string const& textInfo);

    Ui::MainWindow* ui;

    he::Mesh m_mesh;
    Model m_modelMesh;
    GLView* m_view;
    bool m_openedMesh;
    graph::IncidenceGraph m_graph;

    QGraphicsScene m_scene;
    void displayGraph();

    QGraphicsScene m_sceneFractalDim;
    void displayGridFractalDim();

    QGraphicsScene m_sceneAreaPerimeter;
    void displayGridAreaPerimeter();
};

#endif