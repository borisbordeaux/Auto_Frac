#include "mainwindow.h"
#include "ui_mainwindow.h"

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
    std::cout << "button clicked" << std::endl;
    std::cout.flush();
}
