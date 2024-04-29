#include "gui/schemeeditor.h"

#include "gui/schemewindow.h"
#include <QGraphicsRectItem>
#include <QMouseEvent>

namespace frac {
SchemeEditor::SchemeEditor(SchemeWindow& schemeWindow) : QGraphicsView(), m_schemeWindow(schemeWindow) {
}

void SchemeEditor::mousePressEvent(QMouseEvent* event) {
    if (event->button() == Qt::LeftButton) {
        QPointF sceneCoords = this->mapToScene(event->pos());// - QPointF(this->pos().x(), -this->pos().y());
        for (QGraphicsItem* item: scene()->items()) {
            if (item->data(0).isValid() && item->contains(sceneCoords)) {
                m_pressedItem = { item->data(0).toUInt(), item->data(1).toUInt() };
                m_schemeWindow.setSelected(static_cast<int>(m_pressedItem->first), static_cast<int>(m_pressedItem->second));
            }
        }
    }
    QGraphicsView::mousePressEvent(event);
}

void SchemeEditor::mouseReleaseEvent(QMouseEvent* event) {
    m_pressedItem = std::nullopt;
    QGraphicsView::mouseReleaseEvent(event);
}

void SchemeEditor::mouseMoveEvent(QMouseEvent* event) {
    if (m_pressedItem.has_value()) {
        QPointF sceneCoords = this->mapToScene(event->pos());// - QPointF(this->pos().x(), -this->pos().y());
        m_schemeWindow.setCoords(m_pressedItem->first, m_pressedItem->second, sceneCoords);
        m_schemeWindow.redraw();
        this->update();
    }
    QGraphicsView::mouseMoveEvent(event);
}
} // frac