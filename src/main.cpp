#include <QApplication>

#include "gui/mainwindow.h"

int main(int argc, char* argv[]) {
    QApplication a(argc, argv);

    QSurfaceFormat fmt;
    fmt.setDepthBufferSize(24);
    //smoother display
#ifndef Q_OS_ANDROID
    fmt.setSamples(16);
#endif
    fmt.setVersion(4,6);
    fmt.setProfile(QSurfaceFormat::CoreProfile);
    fmt.setSwapInterval(1);
    QSurfaceFormat::setDefaultFormat(fmt);

    MainWindow w;
    w.show();
    return QApplication::exec();
}
