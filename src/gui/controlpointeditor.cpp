#include "gui/controlpointeditor.h"

#include "fractal/structure.h"
#include "utils/utils.h"
#include <QGraphicsRectItem>
#include <QMouseEvent>
#include <QVBoxLayout>
#include <QPushButton>
#include <QLabel>
#include <QDoubleSpinBox>
#include <QFrame>
#include <QFormLayout>
#include <QFile>
#include <QJsonObject>
#include <QJsonArray>
#include <QJsonDocument>
#include <QMatrix4x4>
#include <QFileDialog>

namespace frac {
ControlPointEditor::ControlPointEditor() : QGraphicsView() {
    this->setScene(&m_scene);
    this->scale(1, -1.0);
    m_scene.setBackgroundBrush(Qt::white);

    QVBoxLayout* layout = new QVBoxLayout(this);
    QHBoxLayout* hLayout = new QHBoxLayout();
    QFormLayout* hLayoutButton = new QFormLayout();
    hLayout->setAlignment(Qt::AlignRight);
    layout->setAlignment(Qt::AlignBottom);
    layout->addLayout(hLayout);
    hLayout->addLayout(hLayoutButton);
    QPushButton* okButton = new QPushButton("OK");
    QPushButton* changeCoordButton = new QPushButton("Change coordinates");
    QPushButton* saveButton = new QPushButton("Save...");
    QPushButton* loadButton = new QPushButton("Load...");
    QPushButton* rotateButton = new QPushButton("Rotate");
    QPushButton* translateButton = new QPushButton("Translate");
    QPushButton* localDistButton = new QPushButton("Local Distribution");
    m_xCoord = new QDoubleSpinBox();
    m_yCoord = new QDoubleSpinBox();
    m_angle = new QDoubleSpinBox();
    m_xTranslate = new QDoubleSpinBox();
    m_yTranslate = new QDoubleSpinBox();
    m_xCoord->setRange(-1000, 1000);
    m_yCoord->setRange(-1000, 1000);
    m_angle->setRange(-360, 360);
    m_xTranslate->setRange(-1000, 1000);
    m_yTranslate->setRange(-1000, 1000);
    hLayoutButton->addRow(m_xCoord, m_yCoord);
    hLayoutButton->addRow(changeCoordButton);
    QFrame* hline = new QFrame();
    hline->setFrameShape(QFrame::HLine);
    hLayoutButton->addRow(hline);
    hLayoutButton->addRow(saveButton, loadButton);
    hLayoutButton->addRow(m_angle, rotateButton);
    hLayoutButton->addRow(m_xTranslate, m_yTranslate);
    hLayoutButton->addRow(translateButton);
    hLayoutButton->addRow(localDistButton);

    hLayoutButton->setRowWrapPolicy(QFormLayout::DontWrapRows);
    hLayoutButton->setFieldGrowthPolicy(QFormLayout::ExpandingFieldsGrow);
    hLayoutButton->setFormAlignment(Qt::AlignHCenter | Qt::AlignTop);
    hLayoutButton->setLabelAlignment(Qt::AlignRight);
    hLayout->addWidget(okButton);
    connect(okButton, &QPushButton::clicked, this, &ControlPointEditor::valid);
    connect(changeCoordButton, &QPushButton::clicked, this, &ControlPointEditor::changeCoord);
    connect(saveButton, &QPushButton::clicked, this, &ControlPointEditor::save);
    connect(loadButton, &QPushButton::clicked, this, &ControlPointEditor::load);
    connect(rotateButton, &QPushButton::clicked, this, &ControlPointEditor::rotateFace);
    connect(translateButton, &QPushButton::clicked, this, &ControlPointEditor::translateFace);
    connect(localDistButton, &QPushButton::clicked, this, &ControlPointEditor::localDistFace);
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
    float thick = 12.0f;
    this->updateWithAdjacencies();
    for (std::size_t i = 0; i < coords.size(); i++) {
        QPainterPath shapePath;
        //draw lines
        for (std::size_t j = 0; j < coords[i].size(); j++) {
            bool nextIsIntern = m_structure->isInternControlPoint((j + 1) % coords[i].size(), i);
            //QPen pen { nextIsIntern ? Qt::green : Qt::blue, j == 0 ? 3.0 : 2.0 };
            if (nextIsIntern) {
                if (shapePath.isEmpty())
                    shapePath.moveTo(coords[i][j]);
                shapePath.quadTo(coords[i][j + 1], coords[i][(j + 2) % coords[i].size()]);
                j++;
            } else {
                if (shapePath.isEmpty())
                    shapePath.moveTo(coords[i][j].x(), coords[i][j].y());
                shapePath.lineTo(coords[i][(j + 1) % coords[i].size()].x(), coords[i][(j + 1) % coords[i].size()].y());
                //m_scene.addLine(coords[i][j].x(), coords[i][j].y(), coords[i][(j + 1) % coords[i].size()].x(), coords[i][(j + 1) % coords[i].size()].y(), pen);
            }
        }
        shapePath.setFillRule(Qt::FillRule::WindingFill);
        m_scene.addPath(shapePath, QPen(), QBrush(Qt::GlobalColor::lightGray));

        //draw gaps
        QPointF center(0, 0);
        for (auto j : coords[i]) {
            center += j;
        }
        center /= static_cast<float>(coords[i].size());
        float meanDistanceToCenter = 0.0f;
        for (auto j : coords[i]) {
            meanDistanceToCenter += QVector2D(center - j).length();
        }
        meanDistanceToCenter /= static_cast<float>(coords[i].size());
        float diameter = meanDistanceToCenter * 0.8f;
        m_scene.addEllipse(center.x() - diameter / 2.0f, center.y() - diameter / 2.0f, diameter, diameter, QPen(), QBrush(Qt::white));

        //draw control points
        bool secondIsIntern = m_structure->isInternControlPoint(1, i);
        for (std::size_t j = 0; j < coords[i].size(); j++) {
            bool isIntern = m_structure->isInternControlPoint(j, i);
            bool isFirstEdge = (j == 0 || (j == 1 && !secondIsIntern) || (j == 2 && secondIsIntern));
            QBrush brush = isFirstEdge ? Qt::green : (isIntern ? Qt::blue : Qt::black);
            QGraphicsRectItem* r = m_scene.addRect(coords[i][j].x() - thick / 2.0f, coords[i][j].y() - thick / 2.0f, thick, thick, QPen(), brush);
            r->setData(0, static_cast<int>(i));
            r->setData(1, static_cast<int>(j));
            r->setFlag(QGraphicsRectItem::GraphicsItemFlag::ItemIsMovable);
        }
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
        m_xCoord->setValue(m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex].x());
        m_yCoord->setValue(m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex].y());
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
        m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex].setX(m_xCoord->value());
        m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex].setY(m_yCoord->value());
        this->redraw(true);
        qDebug() << "translation done";
    }
}

void ControlPointEditor::save() {
    qDebug() << "Saving coordinates...";
    QString file = QFileDialog::getSaveFileName(this, "Save a JSON File...", "../json", "JSON Files (*.json)");
    QFile saveFile(file);
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
    QString file = QFileDialog::getOpenFileName(this, "Open a JSON File...", "../json", "JSON Files (*.json)");
    QFile loadFile(file);
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

void ControlPointEditor::rotateFace() {
    if (m_lastFaceIndex != -1) {
        qreal degrees = m_angle->value();
        qreal radians = qDegreesToRadians(degrees);
        QPointF barycenter { 0.0, 0.0 };
        for (QPointF& p: m_coordinatesTemp[m_lastFaceIndex]) {
            barycenter.setX(barycenter.x() + p.x());
            barycenter.setY(barycenter.y() + p.y());
        }
        barycenter.setX(barycenter.x() / static_cast<qreal>(m_coordinatesTemp[m_lastFaceIndex].size()));
        barycenter.setY(barycenter.y() / static_cast<qreal>(m_coordinatesTemp[m_lastFaceIndex].size()));
        for (QPointF& p: m_coordinatesTemp[m_lastFaceIndex]) {
            //set to origin
            p.setX(p.x() - barycenter.x());
            p.setY(p.y() - barycenter.y());
            //rotate
            qreal x = p.x() * qCos(radians) - p.y() * qSin(radians);
            qreal y = p.x() * qSin(radians) + p.y() * qCos(radians);
            //restore to face position
            p.setX(x + barycenter.x());
            p.setY(y + barycenter.y());
        }
        this->redraw(true);
    }
}

void ControlPointEditor::translateFace() {
    if (m_lastFaceIndex != -1) {
        qreal x = m_xTranslate->value();
        qreal y = m_yTranslate->value();
        for (QPointF& p: m_coordinatesTemp[m_lastFaceIndex]) {
            p.setX(p.x() + x);
            p.setY(p.y() + y);
        }
        this->redraw(true);
    }
}

void ControlPointEditor::localDistFace() {
    if (m_lastFaceIndex != -1) {
        //compute barycenter
        qreal x = 0.0;
        qreal y = 0.0;
        for (QPointF& p: m_coordinatesTemp[m_lastFaceIndex]) {
            x += p.x();
            y += p.y();
        }
        x /= static_cast<double>(m_coordinatesTemp[m_lastFaceIndex].size());
        y /= static_cast<double>(m_coordinatesTemp[m_lastFaceIndex].size());

        //distribute points around the origin and add the computed barycenter to place correctly the face
        float nbCtrlPtsF = static_cast<float>(m_coordinatesTemp[m_lastFaceIndex].size());
        int nbCtrlPts = static_cast<int>(m_coordinatesTemp[m_lastFaceIndex].size());
        double radius = 100.0;
        int i = 0;
        for (QPointF& p: m_coordinatesTemp[m_lastFaceIndex]) {
            if (!m_structure->isInternControlPoint(i, m_lastFaceIndex)) {
                p.setX(radius * qCos(static_cast<float>(i) * 2.0f * 3.1415926f / nbCtrlPtsF) + x);
                p.setY(radius * qSin(static_cast<float>(i) * 2.0f * 3.1415926f / nbCtrlPtsF) + y);
            }
            i++;
        }
        i = 0;
        for (QPointF& p: m_coordinatesTemp[m_lastFaceIndex]) {
            if (m_structure->isInternControlPoint(i, m_lastFaceIndex)) {
                p.setX((m_coordinatesTemp[m_lastFaceIndex][frac::utils::mod(i - 1, nbCtrlPts)].x() + m_coordinatesTemp[m_lastFaceIndex][frac::utils::mod(i + 1, nbCtrlPts)].x()) / 2.0);
                p.setY((m_coordinatesTemp[m_lastFaceIndex][frac::utils::mod(i - 1, nbCtrlPts)].y() + m_coordinatesTemp[m_lastFaceIndex][frac::utils::mod(i + 1, nbCtrlPts)].y()) / 2.0);
            }
            i++;
        }

        this->redraw(true);
    }
}
} // frac