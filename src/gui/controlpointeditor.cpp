#include "gui/controlpointeditor.h"

#include "fractal/structure.h"
#include <QGraphicsRectItem>
#include <QMouseEvent>
#include <QVBoxLayout>

namespace frac {
ControlPointEditor::ControlPointEditor() : QGraphicsView() {
    this->setScene(&m_scene);
    this->scale(1, -1.0);
    m_scene.setBackgroundBrush(Qt::white);

    m_okButton = new QPushButton(tr("&OK"), this);
    connect(m_okButton, &QPushButton::clicked, this, &ControlPointEditor::valid);
}

void ControlPointEditor::show() {
    if (m_structure != nullptr) {
        this->redraw(false);
        QGraphicsView::show();
    }
}

void ControlPointEditor::setStructure(Structure* s) {
    m_structure = s;
    m_coordinates.clear();
    m_coordinatesTemp.clear();
    float radius = 100.0f;
    float t = 220.0f;
    for (std::size_t i = 0; i < s->faces().size(); i++) {
        //add face to drawing
        std::size_t nbCtrlPts = s->nbControlPointsOfFace(i);
        m_coordinates.emplace_back();
        m_coordinatesTemp.emplace_back();
        for (std::size_t j = 0; j < nbCtrlPts; j++) {
            m_coordinates[i].emplace_back(radius * qCos(static_cast<float>(j) * 2.0f * 3.1415926f / static_cast<float>(nbCtrlPts)) + t * static_cast<float>(i), radius * qSin(static_cast<float>(j) * 2.0f * 3.1415926f / static_cast<float>(nbCtrlPts)));
            m_coordinatesTemp[i].emplace_back(m_coordinates[i][j]);
        }
    }
}

void ControlPointEditor::redraw(bool useCurrentCoordinates) {
    m_scene.clear();
    m_scene.addLine(0, -1000, 0, 1000);
    m_scene.addLine(-1000, 0, 1000, 0);
    float thick = 10.0f;
    this->updateWithAdjacencies();
    auto const& coords = useCurrentCoordinates ? m_coordinatesTemp : m_coordinates;
    for (std::size_t i = 0; i < coords.size(); i++) {
        for (std::size_t j = 0; j < coords[i].size(); j++) {
            QGraphicsRectItem* r = m_scene.addRect(coords[i][j].x() - thick / 2.0f, coords[i][j].y() - thick / 2.0f, thick, thick, QPen(), Qt::black);
            r->setData(0, static_cast<int>(i));
            r->setData(1, static_cast<int>(j));
            r->setFlag(QGraphicsRectItem::GraphicsItemFlag::ItemIsMovable);
        }
        for (std::size_t j = 0; j < coords[i].size(); j++) {
            m_scene.addLine(coords[i][j].x(), coords[i][j].y(), coords[i][(j + 1) % coords[i].size()].x(), coords[i][(j + 1) % coords[i].size()].y());
        }
    }
}

void ControlPointEditor::mousePressEvent(QMouseEvent* event) {
    for (QGraphicsItem* item: m_scene.items()) {
        if (item->data(0).isValid() && item->contains(this->mapToScene(event->pos()))) {
            m_pressedItem = item;
        }
    }
    QGraphicsView::mousePressEvent(event);
}

void ControlPointEditor::mouseReleaseEvent(QMouseEvent* event) {
    QGraphicsView::mouseReleaseEvent(event);
    if (m_pressedItem != nullptr) {
        m_coordinatesTemp[m_pressedItem->data(0).toInt()][m_pressedItem->data(1).toInt()] = this->mapToScene(event->pos());
        m_pressedItem = nullptr;
        this->redraw(true);
        this->update();
    }
}

bool ControlPointEditor::isValidForStructure(Structure* s) const {
    bool res = false;
    //check if enough coordinates
    if (s->faces().size() == m_coordinatesTemp.size()) {
        res = true;
        for (std::size_t i = 0; i < s->faces().size(); i++) {
            if (m_coordinatesTemp[i].size() != s->nbControlPointsOfFace(i)) {
                res = false;
            }
        }
    }
    //check if same adjacencies
    if (res) {
        if (m_structure != nullptr && m_structure->adjacencies().size() == s->adjacencies().size()) {
            for (std::size_t i = 0; i < m_structure->adjacencies().size(); i++) {
                if (!m_structure->adjacencies()[i].equals(s->adjacencies()[i])) {
                    res = false;
                }
            }
        } else {
            res = false;
        }
    }

    return res;
}

std::vector<std::vector<QPointF>> const& ControlPointEditor::coordinates() const {
    return m_coordinates;
}

void ControlPointEditor::updateWithAdjacencies() {
    for (frac::Adjacency const& adj: m_structure->adjacencies()) {
        std::vector<std::size_t> const& indicesFace1 = m_structure->controlPointIndices(adj.Edge1, adj.Face1);
        std::vector<std::size_t> const& indicesFace2 = m_structure->controlPointIndices(adj.Edge2, adj.Face2, true);

        for (std::size_t i = 0; i < indicesFace2.size(); i++) {
            m_coordinatesTemp[adj.Face2][indicesFace2[i]] = m_coordinatesTemp[adj.Face1][indicesFace1[i]];
            m_coordinates[adj.Face2][indicesFace2[i]] = m_coordinates[adj.Face1][indicesFace1[i]];
        }
    }
}

void ControlPointEditor::valid() {
    for (std::size_t i = 0; i < m_coordinates.size(); i++) {
        for (std::size_t j = 0; j < m_coordinates[i].size(); j++) {
            m_coordinates[i][j] = m_coordinatesTemp[i][j];
        }
    }
    this->close();
}

void ControlPointEditor::closeEvent(QCloseEvent* event) {
    for (std::size_t i = 0; i < m_coordinates.size(); i++) {
        for (std::size_t j = 0; j < m_coordinates[i].size(); j++) {
            m_coordinatesTemp[i][j] = m_coordinates[i][j];
        }
    }
    QWidget::closeEvent(event);
}
} // frac