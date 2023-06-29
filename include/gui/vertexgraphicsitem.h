#ifndef AUTOFRAC_VERTEXGRAPHICSITEM_H
#define AUTOFRAC_VERTEXGRAPHICSITEM_H

#include <QGraphicsItem>

namespace graph {
class Vertex;
}

class VertexGraphicsItem : public QGraphicsItem {
public:
    explicit VertexGraphicsItem();
    [[nodiscard]] QRectF boundingRect() const override;
    void paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* widget) override;

    void setCenter(int centerX, int centerY);
    [[nodiscard]] int getX() const;
    [[nodiscard]] int getY() const;

    void setVertex(graph::Vertex* vertex);

protected:
    void mousePressEvent(QGraphicsSceneMouseEvent* event) override;
    void mouseReleaseEvent(QGraphicsSceneMouseEvent* event) override;
    void mouseMoveEvent(QGraphicsSceneMouseEvent* event) override;

private:
    QRectF m_boundindRect;

    graph::Vertex* m_vertex;
};


#endif //AUTOFRAC_VERTEXGRAPHICSITEM_H
