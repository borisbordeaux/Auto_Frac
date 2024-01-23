#include "gui/controlpointeditor.h"

#include "fractal/structure.h"
#include <QGraphicsRectItem>
#include <QMouseEvent>
#include <QVBoxLayout>
#include <QPushButton>
#include <QLabel>
#include <QDoubleSpinBox>
#include <QFormLayout>
#include <QFile>
#include <QJsonObject>
#include <QJsonArray>
#include <QJsonDocument>

namespace frac {
ControlPointEditor::ControlPointEditor() : QGraphicsView() {
    this->setScene(&m_scene);
    this->scale(1, -1.0);
    m_scene.setBackgroundBrush(Qt::white);

    QVBoxLayout * layout = new QVBoxLayout(this);
    QHBoxLayout * hLayout = new QHBoxLayout();
    QFormLayout * hLayoutButton = new QFormLayout();
    hLayout->setAlignment(Qt::AlignRight);
    layout->setAlignment(Qt::AlignBottom);
    layout->addLayout(hLayout);
    hLayout->addLayout(hLayoutButton);
    m_okButton = new QPushButton("OK");
    m_changeCoordButton = new QPushButton("Change coordinates");
    m_saveButton = new QPushButton("Save...");
    m_loadButton = new QPushButton("Load...");
    m_xSlider = new QDoubleSpinBox();
    m_ySlider = new QDoubleSpinBox();
    m_xSlider->setRange(-1000, 1000);
    m_ySlider->setRange(-1000, 1000);
    hLayoutButton->addRow(new QLabel("x"), m_xSlider);
    hLayoutButton->addRow(new QLabel("y"), m_ySlider);
    hLayoutButton->addRow(m_changeCoordButton);
    hLayoutButton->addRow(m_saveButton, m_loadButton);
    hLayout->addWidget(m_okButton);
    connect(m_okButton, &QPushButton::clicked, this, &ControlPointEditor::valid);
    connect(m_changeCoordButton, &QPushButton::clicked, this, &ControlPointEditor::changeCoord);
    connect(m_saveButton, &QPushButton::clicked, this, &ControlPointEditor::save);
    connect(m_loadButton, &QPushButton::clicked, this, &ControlPointEditor::load);
}

void ControlPointEditor::show() {
    if (m_structure != nullptr) {
        m_lastControlPointIndex = -1;
        m_lastFaceIndex = -1;
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
    auto const& coords = useCurrentCoordinates ? m_coordinatesTemp : m_coordinates;
    m_scene.clear();
    m_scene.addLine(0, -10, 0, 10);
    m_scene.addLine(-10, 0, 10, 0);
    float thick = 15.0f;
    this->updateWithAdjacencies();
    for (std::size_t i = 0; i < coords.size(); i++) {
        for (std::size_t j = 0; j < coords[i].size(); j++) {
            QBrush brush = m_structure->isInternControlPoint(j, i) ? Qt::blue : Qt::black;
            QGraphicsRectItem* r = m_scene.addRect(coords[i][j].x() - thick / 2.0f, coords[i][j].y() - thick / 2.0f, thick, thick, QPen(), brush);
            r->setData(0, static_cast<int>(i));
            r->setData(1, static_cast<int>(j));
            r->setFlag(QGraphicsRectItem::GraphicsItemFlag::ItemIsMovable);
        }
        QPainterPath path;
        for (std::size_t j = 0; j < coords[i].size(); j++) {
            bool nextIsIntern = m_structure->isInternControlPoint((j + 1) % coords[i].size(), i);
            path.moveTo(coords[i][j]);
            if (nextIsIntern) {
                path.quadTo(coords[i][j + 1], coords[i][(j + 2) % coords[i].size()]);
                j++;
            } else {
                path.lineTo(coords[i][(j + 1) % coords[i].size()]);
            }
        }
        m_scene.addPath(path);
    }
}

void ControlPointEditor::mousePressEvent(QMouseEvent* event) {
    if (event->button() == Qt::LeftButton) {
        for (QGraphicsItem* item: m_scene.items()) {
            if (item->data(0).isValid() && item->contains(this->mapToScene(event->pos()))) {
                m_pressedItem = item;
            }
        }
    }
    QGraphicsView::mousePressEvent(event);
}

void ControlPointEditor::mouseReleaseEvent(QMouseEvent* event) {
    if (m_pressedItem != nullptr) {
        m_lastFaceIndex = m_pressedItem->data(0).toInt();
        m_lastControlPointIndex = m_pressedItem->data(1).toInt();
        m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex] = this->mapToScene(event->pos());
        m_pressedItem = nullptr;
        m_xSlider->setValue(m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex].x());
        m_ySlider->setValue(m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex].y());
        this->redraw(true);
        this->update();
    }
    QGraphicsView::mouseReleaseEvent(event);
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

[[maybe_unused]] void ControlPointEditor::closeEvent(QCloseEvent* event) {
    for (std::size_t i = 0; i < m_coordinates.size(); i++) {
        for (std::size_t j = 0; j < m_coordinates[i].size(); j++) {
            m_coordinatesTemp[i][j] = m_coordinates[i][j];
        }
    }
    QWidget::closeEvent(event);
}

void ControlPointEditor::changeCoord() {
    qDebug() << "translate";
    if (m_lastFaceIndex != -1) {
        m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex].setX(m_xSlider->value());
        m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex].setY(m_ySlider->value());
        this->redraw(true);
        qDebug() << "translation done";
    }
}

void ControlPointEditor::save() {
    qDebug() << "Saving coordinates...";
    QFile saveFile("ctrlPts.json");
    if (!saveFile.open(QIODevice::WriteOnly)) {
        qWarning("Couldn't open save file.");
        return;
    }
    QJsonObject json;
    QJsonArray faces;

    for (auto const& i: m_coordinatesTemp) {
        QJsonArray arrayX;
        QJsonArray arrayY;
        for (QPointF const& j: i) {
            arrayX.append(j.x());
            arrayY.append(j.y());
        }
        QJsonObject a;
        a["x"] = arrayX;
        a["y"] = arrayY;
        faces.append(a);
    }
    json["coords"] = faces;
    saveFile.write(QJsonDocument(json).toJson());
    qDebug() << "Coordinates saved";
}

void ControlPointEditor::load() {
    qDebug() << "Loading coordinates...";

    QFile loadFile("ctrlPts.json");
    if (!loadFile.open(QIODevice::ReadOnly)) {
        qWarning("Couldn't open save file.");
        return;
    }

    QByteArray saveData = loadFile.readAll();
    QJsonDocument loadDoc(QJsonDocument::fromJson(saveData));
    QJsonObject json = loadDoc.object();

    std::vector<std::vector<QPointF>> coords;

    if (const QJsonValue v = json["coords"]; v.isArray()) {
        const QJsonArray faces = v.toArray();
        for (QJsonValueConstRef const& face: faces) {
            coords.emplace_back();
            if (const QJsonValue x = face.toObject().value("x"); x.isArray()) {
                const QJsonArray coordsX = x.toArray();
                for (QJsonValueConstRef const& coordX: coordsX) {
                    if (coordX.isDouble()) {
                        coords[coords.size() - 1].emplace_back(coordX.toDouble(), 0.0f);
                    }
                }
            }
            std::size_t i = 0;
            if (const QJsonValue y = face.toObject().value("y"); y.isArray()) {
                const QJsonArray coordsY = y.toArray();
                for (QJsonValueConstRef const& coordY: coordsY) {
                    if (coordY.isDouble()) {
                        coords[coords.size() - 1][i].setY(coordY.toDouble());
                    }
                    i++;
                }
            }
        }
    }

    bool sameSize = m_coordinatesTemp.size() == coords.size();
    if (sameSize) {
        for (std::size_t i = 0; i < coords.size(); i++) {
            if (coords[i].size() != m_coordinatesTemp[i].size()) {
                sameSize = false;
            }
        }
    }
    if (sameSize) {
        //copy data
        for (std::size_t i = 0; i < coords.size(); i++) {
            for (std::size_t j = 0; j < coords[i].size(); j++) {
                m_coordinatesTemp[i][j] = coords[i][j];
            }
        }
        qDebug() << "Coordinates loaded";
        this->redraw(true);
    } else {
        qDebug() << "Coordinates not loaded, not for same structure!";
    }
}
} // frac