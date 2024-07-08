#ifndef AUTOFRAC_POLYTOPAL2DWINDOW_H
#define AUTOFRAC_POLYTOPAL2DWINDOW_H

#include <QWidget>
#include <QTimer>
#include "halfedge/mesh.h"
#include "model.h"

class QStatusBar;
class QProgressBar;
class GLView;

QT_BEGIN_NAMESPACE
namespace Ui { class Polytopal2DWindow; }
QT_END_NAMESPACE

class Polytopal2DWindow : public QWidget {
Q_OBJECT

public:
    explicit Polytopal2DWindow(QWidget* parent = nullptr);
    ~Polytopal2DWindow() override;

    int inversionLevel() const { return m_inversionLevel; }
    void projectCirclesToPlan();
    void updateCircles();
    void updateCirclesDual();

    void updateUserData();

public slots:
    [[maybe_unused]] void slotOpenOBJFile();
    [[maybe_unused]] void slotExportAllFaces();
    [[maybe_unused]] void slotExportSelectedFace();
    [[maybe_unused]] void slotDisplayUnitSphereChanged();
    [[maybe_unused]] void slotCanonizeMesh();
    void canonicalizeStep();
    [[maybe_unused]] void slotDisplayAreaCircles();
    [[maybe_unused]] void slotDisplayDualAreaCircles();
    [[maybe_unused]] void slotDisplayMeshClicked();
    [[maybe_unused]] void slotIncreaseInversion();
    [[maybe_unused]] void slotDecreaseInversion();
    [[maybe_unused]] void slotProjectCirclesClicked();
    void animProjectStep();
    void animInversionStep();
    void increaseInversion();
    [[maybe_unused]] void slotExportOBJ();

    [[maybe_unused]] void slotTypeSelectionChanged(int index);
    [[maybe_unused]] void slotTypeRotationChanged(int index);
    [[maybe_unused]] void slotStartVideoAnimation();
    [[maybe_unused]] void slotAnimationRotation();
    [[maybe_unused]] void slotUpdateLabelPrecision(int value);

    [[maybe_unused]] void slotBarycentricSubdivision();
    [[maybe_unused]] void slotGeneralizedBarycentricSubdivision();

    [[maybe_unused]] void slotChangeTheme();

    [[maybe_unused]] void slotChangeUserData();

private:
    void updateEnablementPoly();
    void setInfo(std::string const& textInfo, int timeoutMs = 2000);
    void setInfoAdvancement(int percent);

private:
    Ui::Polytopal2DWindow* ui;

    QStatusBar *m_statusBar;

    he::Mesh m_mesh;
    he::Mesh m_sphereMesh;
    Model m_modelMesh;
    GLView* m_view;
    bool m_openedMesh;

    QTimer m_timerCanonicalize;
    std::vector<poly::Circle> m_circles;
    std::vector<poly::Circle> m_circlesDual;
    int m_inversionLevel;
    std::size_t m_circlesIndex;
    QTimer m_timerAnimProject;
    std::vector<poly::Circle> m_circlesAnimProject;
    std::vector<poly::Circle> m_circlesDualAnimProject;
    float m_tAnimProject = 0.0f;
    QTimer m_timerAnimInversion;
    float m_tAnimInversion = 0.0f;
    std::size_t m_nbInversions = 0;

    double m_firstError = -1.0;

    QProgressBar* m_progressBar = nullptr;

    bool m_canonicalized = false;
    int m_step = 0;
};


#endif //AUTOFRAC_POLYTOPAL2DWINDOW_H
