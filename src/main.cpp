#include <QApplication>
#include <QSurfaceFormat>

#include "gui/mainwindow.h"

int main(int argc, char* argv[]) {
    QApplication a(argc, argv);

    QSurfaceFormat fmt;
    fmt.setDepthBufferSize(24);
    //smoother display
    fmt.setSamples(16);
    fmt.setVersion(4,6);
    fmt.setProfile(QSurfaceFormat::CoreProfile);
    fmt.setSwapInterval(0);
    QSurfaceFormat::setDefaultFormat(fmt);

    MainWindow w;
    w.show();
    return QApplication::exec();
}
