#include "gui/schemeeditor.h"

#include "gui/schemewindow.h"
#include <QGraphicsRectItem>
#include <QMouseEvent>

namespace frac {
SchemeEditor::SchemeEditor(SchemeWindow& schemeWindow) : QGraphicsView(), m_schemeWindow(schemeWindow) {
    setRenderHint(QPainter::Antialiasing);
}

void SchemeEditor::mousePressEvent(QMouseEvent* event) {
    if (event->button() == Qt::LeftButton) {
        QPointF sceneCoords = this->mapToScene(event->pos());
        for (QGraphicsItem* item: scene()->items()) {
            if (item->data(0).isValid() && item->contains(sceneCoords)) {
                m_pressedItem = { item->data(0).toUInt(), item->data(1).toUInt() };
                m_schemeWindow.setSelected(static_cast<int>(m_pressedItem->first), static_cast<int>(m_pressedItem->second));
                break;
            } else if (item->data(2).isValid() && item->contains(sceneCoords)) {
                m_lastCoords = sceneCoords;
                m_currentFace = item->data(2).toUInt();
                m_schemeWindow.setSelected(item->data(2).toInt());
                break;
            }
        }
    }
    if (event->button() == Qt::RightButton) {
        QPointF sceneCoords = this->mapToScene(event->pos());
        for (QGraphicsItem* item: scene()->items()) {
            if (item->data(2).isValid() && item->contains(sceneCoords)) {
                m_lastCoords = sceneCoords;
                m_currentStruct = true;
                break;
            }
        }
    }
    QGraphicsView::mousePressEvent(event);
}

void SchemeEditor::mouseReleaseEvent(QMouseEvent* event) {
    m_pressedItem = std::nullopt;
    m_currentFace = std::nullopt;
    m_currentStruct = false;
    QGraphicsView::mouseReleaseEvent(event);
}

void SchemeEditor::mouseMoveEvent(QMouseEvent* event) {
    if (m_pressedItem.has_value()) {
        QPointF sceneCoords = this->mapToScene(event->pos());
        m_schemeWindow.setCoords(m_pressedItem->first, m_pressedItem->second, sceneCoords);
        m_schemeWindow.redraw();
        this->update();
    }
    if (m_currentFace.has_value()) {
        QPointF sceneCoords = this->mapToScene(event->pos());
        m_schemeWindow.translateFaceOf(m_currentFace.value(), sceneCoords - m_lastCoords);
        m_lastCoords = sceneCoords;
    }
    if (m_currentStruct) {
        QPointF sceneCoords = this->mapToScene(event->pos());
        m_schemeWindow.translateStructOf(sceneCoords - m_lastCoords);
        m_lastCoords = sceneCoords;
    }
    QGraphicsView::mouseMoveEvent(event);
}

void SchemeEditor::wheelEvent(QWheelEvent* event) {
    QPointF sceneCoords = this->mapToScene(event->position().toPoint());
    for (QGraphicsItem* item: scene()->items()) {
        if (item->data(2).isValid() && item->contains(sceneCoords)) {
            if (event->angleDelta().y() < 0) {
                m_schemeWindow.scaleStructBy(1.01f);
            } else {
                m_schemeWindow.scaleStructBy(1.0f / 1.01f);
            }
            return;
        }
    }
    QGraphicsView::wheelEvent(event);
}
} // frac