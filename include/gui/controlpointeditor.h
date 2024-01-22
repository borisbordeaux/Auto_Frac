#ifndef AUTOFRAC_CONTROLPOINTEDITOR_H
#define AUTOFRAC_CONTROLPOINTEDITOR_H

#include <QGraphicsView>

namespace frac {

class Structure;

class ControlPointEditor : public QGraphicsView {
public:
    ControlPointEditor();
    void show();
    bool isValidForStructure(Structure* s) const;
    void setStructure(Structure* s);
    std::vector<std::vector<QPointF>> const& coordinates() const;

protected:
    void mousePressEvent(QMouseEvent* event) override;
    void mouseReleaseEvent(QMouseEvent* event) override;

private:
    void redraw();
    void updateWithAdjacencies();

private:
    QGraphicsScene m_scene;
    std::vector<std::vector<QPointF>> m_coordinates;
    QGraphicsItem* m_pressedItem = nullptr;
    Structure* m_structure = nullptr;
};

} // frac

#endif //AUTOFRAC_CONTROLPOINTEDITOR_H
