#ifndef AUTOFRAC_POINTGRAPHICSITEM_H
#define AUTOFRAC_POINTGRAPHICSITEM_H

#include <QGraphicsItem>
#include <QPen>

class QLabel;

class PointGraphicsItem : public QGraphicsItem {
public:
    explicit PointGraphicsItem(float x, float y, float size, QLabel* labelPerimeter, QLabel* labelArea, QLabel* labelPorosity, int valuePerimeter, int valueArea, float porosity, QPen pen);

    [[nodiscard]] QRectF boundingRect() const override;

    void paint(QPainter* painter, const QStyleOptionGraphicsItem* option, QWidget* widget) override;

protected:
    void mouseReleaseEvent(QGraphicsSceneMouseEvent* event) override;

private:
    QRectF m_boundindRect;
    QLabel* m_labelPerimeter;
    QLabel* m_labelArea;
    QLabel* m_labelPorosity;
    int m_valuePerimeter;
    int m_valueArea;
    float m_valuePorosity;
    QPen m_pen;
};

#endif //AUTOFRAC_POINTGRAPHICSITEM_H
