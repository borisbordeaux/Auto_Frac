#ifndef AUTOFRAC_PERSISTENTHOMOLOGYWINDOW_H
#define AUTOFRAC_PERSISTENTHOMOLOGYWINDOW_H

#include <QWidget>
#include <QGraphicsScene>
#include <QChart>


QT_BEGIN_NAMESPACE
namespace Ui { class PersistentHomologyWindow; }
QT_END_NAMESPACE

class PersistentHomologyWindow : public QWidget {
Q_OBJECT

public:
    explicit PersistentHomologyWindow(QWidget* parent = nullptr);
    ~PersistentHomologyWindow() override;

public slots:
    [[maybe_unused]] void slotComputePersistenceHomology();

private:
    Ui::PersistentHomologyWindow* ui;

    QGraphicsScene m_scenePersistentHomology;
    QChart* m_chartPersistentHomology;
};


#endif //AUTOFRAC_PERSISTENTHOMOLOGYWINDOW_H
