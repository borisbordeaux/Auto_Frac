#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QListWidgetItem>
#include "edge.h"
#include "face.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow {
Q_OBJECT
public:
    explicit MainWindow(QWidget* parent = nullptr);
    ~MainWindow() override;

public slots:
    [[maybe_unused]] [[maybe_unused]] void slot1();
    [[maybe_unused]] [[maybe_unused]] void slotAddFace();
    [[maybe_unused]] [[maybe_unused]] void slotRemoveFace();
    [[maybe_unused]] [[maybe_unused]] void slotOnFaceSelected(int row);
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
    [[maybe_unused]] [[maybe_unused]] void slotOnFaceDelayChanged(int value);
    [[maybe_unused]] void slotAddEdge();
    [[maybe_unused]] void slotRemoveEdge();
    [[maybe_unused]] void slotOnSelectedEdgeTopologyChanged(int row);
    [[maybe_unused]] void slotOnSelectedEdgeNbSubdivisionsChanged(int value);
    [[maybe_unused]] void slotOnSelectedEdgeDelayChanged(int value);

private:
    [[nodiscard]] static frac::Face toFace(QString const& cellName);
    [[nodiscard]] static frac::Edge toEdge(QString const& edgeName);
    void updateEnablement();
    Ui::MainWindow* ui;

};

#endif