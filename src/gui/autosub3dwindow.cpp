#include <QFileDialog>
#include "gui/autosub3dwindow.h"
#include "ui_autosub3dwindow.h"
#include "halfedge/objreader.h"
#include "halfedge/graphisomorphism.h"
#include "halfedge/halfedge.h"


AutoSub3DWindow::AutoSub3DWindow(QWidget* parent) :
        QWidget(parent), ui(new Ui::AutoSub3DWindow) {
    ui->setupUi(this);
}

AutoSub3DWindow::~AutoSub3DWindow() {
    delete ui;
}

[[maybe_unused]] void AutoSub3DWindow::slotOpenMesh1() {
    QString file = QFileDialog::getOpenFileName(this, "Open an OBJ File...", "../obj", "OBJ Files (*.obj)");

    if (file != "") {
        m_mesh1.reset();
        he::reader::readOBJ(file, m_mesh1);
    }
}

[[maybe_unused]] void AutoSub3DWindow::slotOpenMesh2() {
    QString file = QFileDialog::getOpenFileName(this, "Open an OBJ File...", "../obj", "OBJ Files (*.obj)");

    if (file != "") {
        m_mesh2.reset();
        he::reader::readOBJ(file, m_mesh2);
    }
}

[[maybe_unused]] void AutoSub3DWindow::slotCompare() {
    if (m_mesh1.halfEdges().empty() || m_mesh2.halfEdges().empty()) {
        qDebug() << "meshes are empty";
        return;
    }

    bool res = he::GraphComparator::areIsomorph(m_mesh1, m_mesh2);
    bool res2 = he::GraphComparator::areIsomorph(m_mesh1, m_mesh2, true);
    qDebug() << "topology isomorphism:" << res << "--- edge type isomorphism:" << res2;
}
