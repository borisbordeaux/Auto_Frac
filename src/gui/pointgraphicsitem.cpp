#include "gui/pointgraphicsitem.h"
#include <QPainter>
#include <QLabel>
#include <utility>

PointGraphicsItem::PointGraphicsItem(float x, float y, float size, QLabel* labelPerimeter, QLabel* labelArea, int valuePerimeter, int valueArea, QPen pen) :
        m_boundindRect(-size / 2.0f, -size / 2.0f, size, size), m_labelPerimeter(labelPerimeter), m_labelArea(labelArea), m_valuePerimeter(valuePerimeter), m_valueArea(valueArea), m_pen(std::move(pen)) {
    this->setPos(x, y);
    this->setFlag(QGraphicsItem::ItemIsSelectable);
}

QRectF PointGraphicsItem::boundingRect() const {
    return this->m_boundindRect;
}

void PointGraphicsItem::paint(QPainter* painter, const QStyleOptionGraphicsItem* /*option*/, QWidget* /*widget*/) {
    painter->setPen(m_pen);
    painter->drawEllipse(this->boundingRect());
}

void PointGraphicsItem::mouseReleaseEvent(QGraphicsSceneMouseEvent* event) {
    this->m_labelPerimeter->setText(QString::number(this->m_valuePerimeter));
    this->m_labelArea->setText(QString::number(this->m_valueArea));
    QGraphicsItem::mouseReleaseEvent(event);
}
