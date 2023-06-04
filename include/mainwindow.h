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
    void slot1();
    void slotAddFace();
    void slotRemoveFace();
    void slotOnFaceSelected(int row);
    void slotOnEdgeSelected(int row);

private:
    [[nodiscard]] static frac::Face toFace(QString const& cellName);
    [[nodiscard]] static frac::Edge toEdge(QString const& edgeName);
    Ui::MainWindow* ui;

};

#endif