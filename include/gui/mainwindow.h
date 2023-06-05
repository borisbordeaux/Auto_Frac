#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

#include "fractal/edge.h"
#include "fractal/face.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow {
Q_OBJECT

public:
    explicit MainWindow(QWidget* parent = nullptr);
    ~MainWindow() override;

public slots:
    [[maybe_unused]] void slot1();
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

    void updateEnablement();
    void setError(std::string const& textError);
    void setInfo(std::string const& textInfo);
    Ui::MainWindow* ui;
};

#endif