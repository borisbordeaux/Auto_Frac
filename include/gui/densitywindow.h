#ifndef AUTOFRAC_DENSITYWINDOW_H
#define AUTOFRAC_DENSITYWINDOW_H

#include <QWidget>


QT_BEGIN_NAMESPACE
namespace Ui { class DensityWindow; }
QT_END_NAMESPACE

class DensityWindow : public QWidget {
Q_OBJECT

public:
    explicit DensityWindow(QWidget* parent = nullptr);
    ~DensityWindow() override;

public slots:
    [[maybe_unused]] void slotComputeImageDensity();

private:
    Ui::DensityWindow* ui;
};


#endif //AUTOFRAC_DENSITYWINDOW_H
