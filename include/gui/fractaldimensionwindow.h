#ifndef AUTOFRAC_FRACTALDIMENSIONWINDOW_H
#define AUTOFRAC_FRACTALDIMENSIONWINDOW_H

#include <QWidget>
#include <QGraphicsScene>
#include <QChart>


QT_BEGIN_NAMESPACE
namespace Ui { class FractalDimensionWindow; }
QT_END_NAMESPACE

class FractalDimensionWindow : public QWidget {
Q_OBJECT

public:
    explicit FractalDimensionWindow(QWidget* parent = nullptr);
    ~FractalDimensionWindow() override;

protected:
    void hideEvent(QHideEvent* event) override;
public slots:
    [[maybe_unused]] void slotComputeFractalDimension();

private:
    Ui::FractalDimensionWindow* ui;

    QGraphicsScene m_sceneFractalDim;
    QChart* m_chartFractalDim;
};


#endif //AUTOFRAC_FRACTALDIMENSIONWINDOW_H
