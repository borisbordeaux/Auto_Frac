#ifndef AUTOFRAC_SCHEMEEDITOR_H
#define AUTOFRAC_SCHEMEEDITOR_H

#include <QGraphicsView>

class SchemeWindow;

namespace frac {

class SchemeEditor : public QGraphicsView {

public:
    explicit SchemeEditor(SchemeWindow& schemeWindow);

protected:
    void mousePressEvent(QMouseEvent* event) override;
    void mouseMoveEvent(QMouseEvent* event) override;
    void mouseReleaseEvent(QMouseEvent* event) override;

private:
    SchemeWindow& m_schemeWindow;
    std::optional<std::pair<std::size_t,std::size_t>> m_pressedItem = std::nullopt;
    std::optional<std::size_t > m_currentFace = std::nullopt;
    QPointF m_lastCoords;
};

} // frac

#endif //AUTOFRAC_SCHEMEEDITOR_H
