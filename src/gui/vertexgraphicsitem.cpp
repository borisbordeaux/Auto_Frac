#include "gui/vertexgraphicsitem.h"
#include "graph/vertex.h"
#include <QPainter>
#include <iostream>

VertexGraphicsItem::VertexGraphicsItem() : m_boundindRect(-10, -10, 20, 20), m_vertex(nullptr) {
    //this->setFlag(ItemIsMovable);
}

QRectF VertexGraphicsItem::boundingRect() const {
    return m_boundindRect;
}

void VertexGraphicsItem::paint(QPainter* painter, const QStyleOptionGraphicsItem* /*option*/, QWidget* /*widget*/) {
    painter->fillRect(m_boundindRect, Qt::black);
    QFont font;
    font.setPointSize(10);
    font.setBold(true);
    painter->setFont(font);
    painter->setPen(QColor(255,150,150));
    painter->drawText(m_boundindRect, Qt::AlignHCenter | Qt::AlignVCenter ,m_vertex->getName().data());
}

void VertexGraphicsItem::setCenter(int centerX, int centerY) {
    this->setPos(centerX, centerY);
}

int VertexGraphicsItem::getX() const {
    return static_cast<int>(this->pos().x());
}

int VertexGraphicsItem::getY() const {
    return static_cast<int>(this->pos().y());
}

void VertexGraphicsItem::setVertex(graph::Vertex* vertex) {
    this->m_vertex = vertex;
}

void VertexGraphicsItem::mousePressEvent(QGraphicsSceneMouseEvent* event) {
    std::cout << *this->m_vertex << std::endl;
    QGraphicsItem::mousePressEvent(event);
}

void VertexGraphicsItem::mouseReleaseEvent(QGraphicsSceneMouseEvent* event) {
    QGraphicsItem::mouseReleaseEvent(event);
}

void VertexGraphicsItem::mouseMoveEvent(QGraphicsSceneMouseEvent* event) {
    QGraphicsItem::mouseMoveEvent(event);
}
