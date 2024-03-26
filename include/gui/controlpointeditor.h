#ifndef AUTOFRAC_CONTROLPOINTEDITOR_H
#define AUTOFRAC_CONTROLPOINTEDITOR_H

#include <QGraphicsView>

class QPushButton;

class QDoubleSpinBox;

namespace frac {

class Structure;

class ControlPointEditor : public QGraphicsView {

public:
    explicit ControlPointEditor();
    void show();
    bool isValidForStructure(Structure* s) const;
    void setStructure(Structure* s);
    std::vector<std::vector<QPointF>> const& coordinates() const;

public slots:
    void valid();
    void changeCoord();
    void save();
    void load();
    void rotateFace();
    void translateFace();
    void localDistFace();

protected:
    void mousePressEvent(QMouseEvent* event) override;
    void mouseReleaseEvent(QMouseEvent* event) override;
    [[maybe_unused]] void closeEvent(QCloseEvent* event) override;

private:
    void redraw(bool useCurrentCoordinates);
    void updateWithAdjacencies();

private:
    QGraphicsScene m_scene;
    QDoubleSpinBox* m_xCoord;
    QDoubleSpinBox* m_yCoord;
    QDoubleSpinBox* m_angle;
    QDoubleSpinBox* m_xTranslate;
    QDoubleSpinBox* m_yTranslate;
    std::vector<std::vector<QPointF>> m_coordinates;
    std::vector<std::vector<QPointF>> m_coordinatesTemp;
    QGraphicsItem* m_pressedItem = nullptr;
    Structure* m_structure = nullptr;

    int m_lastFaceIndex = -1;
    int m_lastControlPointIndex = -1;
};

} // frac

#endif //AUTOFRAC_CONTROLPOINTEDITOR_H
