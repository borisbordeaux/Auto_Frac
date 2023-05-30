#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "edge.h"
#include "face.h"
#include "structure.h"

#include <QtWidgets>
#include <iostream>

MainWindow::MainWindow(QWidget* parent) :
        QMainWindow(parent),
        ui(new Ui::MainWindow) {
    ui->setupUi(this);
}

MainWindow::~MainWindow() {
    delete ui;
}

void MainWindow::slot1() {

    frac::Edge b2 { frac::EdgeType::BEZIER, 2 };
    frac::Edge b3 { frac::EdgeType::BEZIER, 3 };
    frac::Edge c2 { frac::EdgeType::CANTOR, 2 };
    frac::Face cell0 {{ b2, c2, b2, c2, b2, c2 }, 0, c2, b2, b2 };
    frac::Face cell1 {{ c2, b3, c2, b2, c2, b2 }, 0, c2, b2, b2 };

    frac::Structure s {{ cell0, cell1 }};
    s.addAdjacency(0, 0, 1, 3);

    std::cout << s;

    std::cout.flush();
}
