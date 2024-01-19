#include "gui/controlpointeditor.h"
#include "fractal/structure.h"

#include <QGraphicsRectItem>
#include <QMouseEvent>

namespace frac {
ControlPointEditor::ControlPointEditor() : QGraphicsView() {
    setScene(&m_scene);
    m_scene.setBackgroundBrush(Qt::white);
}

void ControlPointEditor::show(Structure const& s) {
    this->setStructure(s);
    this->redraw();
    QGraphicsView::show();
}

void ControlPointEditor::setStructure(Structure const& s) {
    m_coordinates.clear();
    float radius = 100.0f;
    float t = 220.0f;
    for (std::size_t i = 0; i < s.faces().size(); i++) {
        //add face to drawing
        std::size_t nbCtrlPts = s.nbControlPointsOfFace(i);
        m_coordinates.emplace_back();
        for (std::size_t j = 0; j < nbCtrlPts; j++) {
            m_coordinates[i].emplace_back(radius * qCos(static_cast<float>(j) * 2.0f * 3.1415926f / static_cast<float>(nbCtrlPts)) + t * static_cast<float>(i), radius * qSin(static_cast<float>(j) * 2.0f * 3.1415926f / static_cast<float>(nbCtrlPts)));
        }
    }
}

void ControlPointEditor::redraw() {
    m_scene.clear();
    m_scene.addLine(0, -1000, 0, 1000);
    m_scene.addLine(-1000, 0, 1000, 0);
    float thick = 10.0f;
    for (std::size_t i = 0; i < m_coordinates.size(); i++) {
        for (std::size_t j = 0; j < m_coordinates[i].size(); j++) {
            QGraphicsRectItem* r = m_scene.addRect(m_coordinates[i][j].x() - thick / 2.0f, m_coordinates[i][j].y() - thick / 2.0f, thick, thick, QPen(), Qt::black);
            r->setData(0, static_cast<int>(i));
            r->setData(1, static_cast<int>(j));
        }
        for (std::size_t j = 0; j < m_coordinates[i].size(); j++) {
            m_scene.addLine(m_coordinates[i][j].x(), m_coordinates[i][j].y(), m_coordinates[i][(j + 1) % m_coordinates[i].size()].x(), m_coordinates[i][(j + 1) % m_coordinates[i].size()].y());
        }
    }
}

void ControlPointEditor::mousePressEvent(QMouseEvent* event) {
    for (auto item: m_scene.items()) {
        if (item->data(0).isValid() && item->contains(this->mapToScene(event->pos()))) {
            m_pressedItem = item;
        }
    }
    QGraphicsView::mousePressEvent(event);
}

void ControlPointEditor::mouseReleaseEvent(QMouseEvent* event) {
    if (m_pressedItem) {
        m_coordinates[m_pressedItem->data(0).toInt()][m_pressedItem->data(1).toInt()] = this->mapToScene(event->pos());
        m_pressedItem = nullptr;
        this->redraw();
        this->update();
    }
    QGraphicsView::mouseReleaseEvent(event);
}

bool ControlPointEditor::isValidForStructure(Structure const& s) const {
    bool res = false;
    if (s.faces().size() == m_coordinates.size()) {
        res = true;
        for (std::size_t i = 0; i < s.faces().size(); i++) {
            if (m_coordinates[i].size() != s.nbControlPointsOfFace(i)) {
                res = false;
            }
        }
    }
    return res;
}

std::vector<std::vector<QPointF>> const& ControlPointEditor::coordinates() const {
    return m_coordinates;
}
} // frac