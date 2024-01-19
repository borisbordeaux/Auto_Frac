#ifndef AUTOFRAC_CONTROLPOINTEDITOR_H
#define AUTOFRAC_CONTROLPOINTEDITOR_H

#include <QGraphicsView>

namespace frac {

class Structure;

class ControlPointEditor : public QGraphicsView {
public:
    ControlPointEditor();
    void show(Structure const& s);
    bool isValidForStructure(Structure const& s) const;
    std::vector<std::vector<QPointF>> const& coordinates() const;

protected:
    void mousePressEvent(QMouseEvent* event) override;
    void mouseReleaseEvent(QMouseEvent* event) override;

private:
    void setStructure(Structure const& s);
    void redraw();

private:
    QGraphicsScene m_scene;
    std::vector<std::vector<QPointF>> m_coordinates;
    QGraphicsItem* m_pressedItem = nullptr;
};

} // frac

#endif //AUTOFRAC_CONTROLPOINTEDITOR_H
