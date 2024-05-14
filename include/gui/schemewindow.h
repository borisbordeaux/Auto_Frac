#ifndef AUTOFRAC_SCHEMEWINDOW_H
#define AUTOFRAC_SCHEMEWINDOW_H

#include <QWidget>
#include <QGraphicsScene>
#include "schemeeditor.h"

namespace frac {
class Structure;

class Edge;
}

QT_BEGIN_NAMESPACE
namespace Ui { class SchemeWindow; }
QT_END_NAMESPACE

class SchemeWindow : public QWidget {
Q_OBJECT

public:
    explicit SchemeWindow(std::unique_ptr<frac::Structure> structure);
    ~SchemeWindow() override;

    bool isValidForStructure(frac::Structure const& structure) const;
    std::vector<std::vector<QPointF>> const& coordinates() const;

    void setCoords(std::size_t indexFace, std::size_t indexControlPoint, QPointF newPos);
    void setSelected(int indexFace, int indexControlPoint);
    void setSelected(int indexFace);
    void redraw(bool useTempCoordinates = true);

    void setStruct(std::unique_ptr<frac::Structure> structure);

    void translateFaceOf(std::size_t indexFace, QPointF translation);
    void translateStructOf(QPointF translation);

    void scaleStructBy(float scale);

public slots:
    void valid();
    void changeXCoordControlPoint(double value);
    void changeYCoordControlPoint(double value);
    void save();
    void load();
    void rotateFace(int value);
    void localDistFace();
    void updateTempDraw();

protected:
    void closeEvent(QCloseEvent* event) override;

private:
    void localDistributionFace(std::size_t indexFace, bool useTempCoordinates);
    void updateWithAdjacencies();

    void drawScheme(std::size_t i, std::vector<std::vector<QPointF>> const& coords);
    void drawControlPoints(std::size_t i, std::vector<std::vector<QPointF>> const& coords);
    void drawSubdScheme(std::size_t i, std::vector<std::vector<QPointF>> const& coords);

    void drawSubdFace(std::size_t i, std::vector<std::vector<QPointF>> const& coords);
    void drawSubdEdges(std::size_t i, std::vector<std::vector<QPointF>> const& coords);
    void drawSubdReqEdges(std::size_t i, std::vector<std::vector<QPointF>> const& coords);
    void drawSubdInterior(std::size_t i, std::vector<std::vector<QPointF>> const& coords);
    void drawSubdLacuna(std::size_t i, std::vector<std::vector<QPointF>> const& coords);
    void drawSubdBlackPointsOnBoundary(std::size_t i, std::vector<std::vector<QPointF>> const& coords);
    void drawSubdBlackPointsOnLacuna(std::size_t i, std::vector<std::vector<QPointF>> const& coords);
    static QPen penOfEdge(frac::Edge const& e);

private:
    Ui::SchemeWindow* ui;
    std::unique_ptr<frac::Structure> m_structure;
    QGraphicsScene m_scene;
    QGraphicsView* m_graphicsView;

    std::vector<std::vector<QPointF>> m_coordinates;
    std::vector<std::vector<QPointF>> m_coordinatesTemp;

    std::vector<int> m_faceRotations;

    int m_lastFaceIndex = -1;
    int m_lastControlPointIndex = -1;
};


#endif //AUTOFRAC_SCHEMEWINDOW_H
