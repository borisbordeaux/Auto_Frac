#ifndef AUTOFRAC_CONTROLPOINTEDITOR_H
#define AUTOFRAC_CONTROLPOINTEDITOR_H

#include <QGraphicsView>
#include <QPushButton>

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

protected:
    void mousePressEvent(QMouseEvent* event) override;
    void mouseReleaseEvent(QMouseEvent* event) override;
    void closeEvent(QCloseEvent* event) override;

private:
    void redraw(bool useCurrentCoordinates);
    void updateWithAdjacencies();

private:
    QGraphicsScene m_scene;
    QPushButton* m_okButton;
    std::vector<std::vector<QPointF>> m_coordinates;
    std::vector<std::vector<QPointF>> m_coordinatesTemp;
    QGraphicsItem* m_pressedItem = nullptr;
    Structure* m_structure = nullptr;
};

} // frac

#endif //AUTOFRAC_CONTROLPOINTEDITOR_H
