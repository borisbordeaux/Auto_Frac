#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

class PersistentHomologyWindow;
class DensityWindow;
class AreaPerimeterWindow;
class FractalDimensionWindow;
class AutoSub2DWindow;
class Polytopal2DWindow;

namespace Ui {
class MainWindow;
}

namespace frac {
class SchemeEditor;
}

class MainWindow : public QMainWindow {
Q_OBJECT

public:
    explicit MainWindow(QWidget* parent = nullptr);
    ~MainWindow() override;

public slots:
    [[maybe_unused]] void slotOpenAutoSub2DWindow();
    [[maybe_unused]] void slotOpenPolytopal2DWindow();
    [[maybe_unused]] void slotOpenFractalDimensionWindow();
    [[maybe_unused]] void slotOpenAreaPerimeterWindow();
    [[maybe_unused]] void slotOpenDensityWindow();
    [[maybe_unused]] void slotOpenPersistentHomologyWindow();

protected:
    void closeEvent(QCloseEvent* event) override;

private:
    Ui::MainWindow* ui;

    std::unique_ptr<AutoSub2DWindow> m_autoSub2DWindow;
    std::unique_ptr<Polytopal2DWindow> m_polytopal2DWindow;
    std::unique_ptr<FractalDimensionWindow> m_fractalDimensionWindow;
    std::unique_ptr<AreaPerimeterWindow> m_areaPerimeterWindow;
    std::unique_ptr<DensityWindow> m_densityWindow;
    std::unique_ptr<PersistentHomologyWindow> m_persistentHomologyWindow;
};

#endif