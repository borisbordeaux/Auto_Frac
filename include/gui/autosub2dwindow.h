#ifndef AUTOFRAC_AUTOSUB2DWINDOW_H
#define AUTOFRAC_AUTOSUB2DWINDOW_H

#include <QWidget>
#include "schemeeditor.h"
#include "fractal/structure.h"
#include "schemewindow.h"

class QStatusBar;

QT_BEGIN_NAMESPACE
namespace Ui { class AutoSub2DWindow; }
QT_END_NAMESPACE

class AutoSub2DWindow : public QWidget {
Q_OBJECT

public:
    explicit AutoSub2DWindow(QWidget* parent = nullptr);
    ~AutoSub2DWindow() override;

protected:
    void hideEvent(QHideEvent* event) override;

public slots:
    [[maybe_unused]] void slotGenerateScript();
    [[maybe_unused]] void slotAddFace();
    [[maybe_unused]] void slotDuplicateFace();
    [[maybe_unused]] void slotRemoveFace();
    [[maybe_unused]] void slotOnFaceSelected(int row);
    [[maybe_unused]] void slotOnEdgeSelected(int row);
    [[maybe_unused]] void slotOnFaceAdjTopologyChanged(int row);
    [[maybe_unused]] void slotOnFaceAdjNbSubdivisionsChanged(int value);
    [[maybe_unused]] void slotOnFaceAdjDelayChanged(int value);
    [[maybe_unused]] void slotOnFaceGapTopologyChanged(int row);
    [[maybe_unused]] void slotOnFaceGapNbSubdivisionsChanged(int value);
    [[maybe_unused]] void slotOnFaceGapDelayChanged(int value);
    [[maybe_unused]] void slotOnFaceReqTopologyChanged(int row);
    [[maybe_unused]] void slotOnFaceReqNbSubdivisionsChanged(int value);
    [[maybe_unused]] void slotOnFaceReqDelayChanged(int value);
    [[maybe_unused]] void slotOnFaceDelayChanged(int value);
    [[maybe_unused]] void slotOnFaceAlgoChanged(int row);
    [[maybe_unused]] void slotAddEdge();
    [[maybe_unused]] void slotRemoveEdge();
    [[maybe_unused]] void slotOnSelectedEdgeTopologyChanged(int row);
    [[maybe_unused]] void slotOnSelectedEdgeNbSubdivisionsChanged(int value);
    [[maybe_unused]] void slotOnSelectedEdgeDelayChanged(int value);
    [[maybe_unused]] void slotAddConstraint();
    [[maybe_unused]] void slotRemoveConstraint();
    [[maybe_unused]] void slotOnConstraintSelected(int row);
    [[maybe_unused]] void slotOnConstraintFace1Changed(int value);
    [[maybe_unused]] void slotOnConstraintEdge1Changed(int value);
    [[maybe_unused]] void slotOnConstraintFace2Changed(int value);
    [[maybe_unused]] void slotOnConstraintEdge2Changed(int value);
    [[maybe_unused]] void slotEditCP();
    [[maybe_unused]] void slotPlanarControlPointsChanged();
    [[maybe_unused]] void slotComputeNbCells();
    [[maybe_unused]] void slotComputeNbLacunas();
    [[maybe_unused]] void slotComputePorosityMetrics();

private:
    static frac::Adjacency toConstraint(QString const& constraintText);
    static QString fromConstraint(frac::Adjacency const& constraint);
    static std::size_t getNbCellsOfCell(std::string const& faceName, std::size_t level, std::unordered_map<std::string, std::unordered_map<std::string, std::size_t>>& cacheSubdivisions);
    static double getNbLacunaOfCell(std::string const& faceName, std::size_t level, std::unordered_map<std::string, std::unordered_map<std::string, std::size_t>>& cacheSubdivisions, std::unordered_map<std::string, double>& cacheLacunas);
    void updateEnablement();

    void setInfo(std::string const& textInfo, int timeoutMs = 2000);

    frac::CantorType getCantorType() const;
    frac::BezierType getBezierType() const;

private:
    Ui::AutoSub2DWindow* ui;
    QStatusBar *m_statusBar;

    //for gui fractal control points
    std::unique_ptr<SchemeWindow> m_schemeWindow;
};


#endif //AUTOFRAC_AUTOSUB2DWINDOW_H
