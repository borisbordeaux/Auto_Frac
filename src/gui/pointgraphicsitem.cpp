#include "gui/pointgraphicsitem.h"
#include <QPainter>
#include <QLabel>
#include <utility>

PointGraphicsItem::PointGraphicsItem(float x, float y, float size, QLabel* labelPerimeter, QLabel* labelArea, QLabel* labelPorosity, int valuePerimeter, int valueArea, float porosity, QPen pen) :
        m_boundindRect(-size / 2.0f, -size / 2.0f, size, size),
        m_labelPerimeter(labelPerimeter), m_labelArea(labelArea), m_labelPorosity(labelPorosity),
        m_valuePerimeter(valuePerimeter), m_valueArea(valueArea), m_valuePorosity(porosity), m_pen(std::move(pen)) {
    this->setPos(x, y);
    this->setFlag(QGraphicsItem::ItemIsSelectable);
}

QRectF PointGraphicsItem::boundingRect() const {
    return m_boundindRect;
}

void PointGraphicsItem::paint(QPainter* painter, const QStyleOptionGraphicsItem* /*option*/, QWidget* /*widget*/) {
    painter->setPen(m_pen);
    painter->drawEllipse(this->boundingRect());
}

void PointGraphicsItem::mouseReleaseEvent(QGraphicsSceneMouseEvent* event) {
    m_labelPerimeter->setText(QString::number(m_valuePerimeter));
    m_labelArea->setText(QString::number(m_valueArea));
    m_labelPorosity->setText(QString::number(m_valuePorosity));
    QGraphicsItem::mouseReleaseEvent(event);
}
