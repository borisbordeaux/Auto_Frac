#ifndef AUTOFRAC_AREAPERIMETERWINDOW_H
#define AUTOFRAC_AREAPERIMETERWINDOW_H

#include <QWidget>
#include <QGraphicsScene>
#include <QChart>


QT_BEGIN_NAMESPACE
namespace Ui { class AreaPerimeterWindow; }
QT_END_NAMESPACE

class AreaPerimeterWindow : public QWidget {
Q_OBJECT

public:
    explicit AreaPerimeterWindow(QWidget* parent = nullptr);
    ~AreaPerimeterWindow() override;

public slots:
    [[maybe_unused]] void slotComputeAreaPerimeterPNG();
    [[maybe_unused]] void slotComputeAreaPerimeterOBJ();

private:
    void computeAreaPerimeter(QStringList const& files);

private:
    Ui::AreaPerimeterWindow* ui;

    QGraphicsScene m_sceneAreaPerimeter;
    QChart* m_chartAreaPerimeter;
};


#endif //AUTOFRAC_AREAPERIMETERWINDOW_H
