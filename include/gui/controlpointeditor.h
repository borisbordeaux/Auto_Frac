#ifndef AUTOFRAC_CONTROLPOINTEDITOR_H
#define AUTOFRAC_CONTROLPOINTEDITOR_H

#include <QGraphicsView>

class SchemeWindow;

namespace frac {

class ControlPointEditor : public QGraphicsView {

public:
    explicit ControlPointEditor(SchemeWindow& schemeWindow);

protected:
    void mousePressEvent(QMouseEvent* event) override;
    void mouseMoveEvent(QMouseEvent* event) override;
    void mouseReleaseEvent(QMouseEvent* event) override;

private:
    SchemeWindow& m_schemeWindow;
    std::optional<std::pair<std::size_t,std::size_t>> m_pressedItem = std::nullopt;
};

} // frac

#endif //AUTOFRAC_CONTROLPOINTEDITOR_H
