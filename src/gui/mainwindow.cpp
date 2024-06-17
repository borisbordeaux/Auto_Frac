#include "gui/mainwindow.h"
#include "ui_mainwindow.h"

#include "gui/autosub2dwindow.h"
#include "gui/autosub3dwindow.h"
#include "gui/polytopal2dwindow.h"
#include "gui/fractaldimensionwindow.h"
#include "gui/areaperimeterwindow.h"
#include "gui/densitywindow.h"
#include "gui/persistenthomologywindow.h"

MainWindow::MainWindow(QWidget* parent) : QMainWindow(parent), ui(new Ui::MainWindow) {
    ui->setupUi(this);
}

MainWindow::~MainWindow() {
    delete ui;
}

[[maybe_unused]] void MainWindow::slotOpenAutoSub2DWindow() {
    if (m_autoSub2DWindow == nullptr || m_autoSub2DWindow->isHidden()) {
        m_autoSub2DWindow = std::make_unique<AutoSub2DWindow>();
    }
    m_autoSub2DWindow->show();
}

[[maybe_unused]] void MainWindow::slotOpenAutoSub3DWindow() {
    if (m_autoSub3DWindow == nullptr || m_autoSub3DWindow->isHidden()) {
        m_autoSub3DWindow = std::make_unique<AutoSub3DWindow>();
    }
    m_autoSub3DWindow->show();
}

[[maybe_unused]] void MainWindow::slotOpenPolytopal2DWindow() {
    if (m_polytopal2DWindow == nullptr || m_polytopal2DWindow->isHidden()) {
        m_polytopal2DWindow = std::make_unique<Polytopal2DWindow>();
    }
    m_polytopal2DWindow->show();
}

[[maybe_unused]] void MainWindow::slotOpenFractalDimensionWindow() {
    if (m_fractalDimensionWindow == nullptr || m_fractalDimensionWindow->isHidden()) {
        m_fractalDimensionWindow = std::make_unique<FractalDimensionWindow>();
    }
    m_fractalDimensionWindow->show();
}

[[maybe_unused]] void MainWindow::slotOpenDensityWindow() {
    if (m_densityWindow == nullptr || m_densityWindow->isHidden()) {
        m_densityWindow = std::make_unique<DensityWindow>();
    }
    m_densityWindow->show();
}

[[maybe_unused]] void MainWindow::slotOpenAreaPerimeterWindow() {
    if (m_areaPerimeterWindow == nullptr || m_areaPerimeterWindow->isHidden()) {
        m_areaPerimeterWindow = std::make_unique<AreaPerimeterWindow>();
    }
    m_areaPerimeterWindow->show();
}

[[maybe_unused]] void MainWindow::slotOpenPersistentHomologyWindow() {
    if (m_persistentHomologyWindow == nullptr || m_persistentHomologyWindow->isHidden()) {
        m_persistentHomologyWindow = std::make_unique<PersistentHomologyWindow>();
    }
    m_persistentHomologyWindow->show();
}

void MainWindow::closeEvent(QCloseEvent* event) {
    QWidget::closeEvent(event);
    if (m_autoSub2DWindow != nullptr) {
        m_autoSub2DWindow->close();
    }
    if (m_autoSub3DWindow != nullptr) {
        m_autoSub3DWindow->close();
    }
    if (m_polytopal2DWindow != nullptr) {
        m_polytopal2DWindow->close();
    }
    if (m_fractalDimensionWindow != nullptr) {
        m_fractalDimensionWindow->close();
    }
    if (m_densityWindow != nullptr) {
        m_densityWindow->close();
    }
    if (m_areaPerimeterWindow != nullptr) {
        m_areaPerimeterWindow->close();
    }
    if (m_persistentHomologyWindow != nullptr) {
        m_persistentHomologyWindow->close();
    }
}
