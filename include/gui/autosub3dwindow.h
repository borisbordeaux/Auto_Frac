#ifndef AUTOFRAC_AUTOSUB3DWINDOW_H
#define AUTOFRAC_AUTOSUB3DWINDOW_H

#include <QWidget>
#include "halfedge/mesh.h"


QT_BEGIN_NAMESPACE
namespace Ui { class AutoSub3DWindow; }
QT_END_NAMESPACE

class AutoSub3DWindow : public QWidget {
Q_OBJECT

public:
    explicit AutoSub3DWindow(QWidget* parent = nullptr);
    ~AutoSub3DWindow() override;

public slots:
    [[maybe_unused]] void slotOpenMesh1();
    [[maybe_unused]] void slotOpenMesh2();
    [[maybe_unused]] void slotCompare();
    [[maybe_unused]] void slotExportMesh1();

private:
    Ui::AutoSub3DWindow* ui;

    he::Mesh m_mesh1;
    he::Mesh m_mesh2;
};


#endif //AUTOFRAC_AUTOSUB3DWINDOW_H
