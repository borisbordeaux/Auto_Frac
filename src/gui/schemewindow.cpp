#include "gui/schemewindow.h"
#include "ui_schemewindow.h"

#include <QFileDialog>
#include <QJsonObject>
#include <QJsonArray>
#include <QJsonDocument>
#include <QGraphicsRectItem>
#include <QVector2D>
#include <QMouseEvent>

#include "fractal/structure.h"
#include "utils/utils.h"

SchemeWindow::SchemeWindow(frac::Structure* structure) :
        QWidget(nullptr), ui(new Ui::SchemeWindow), m_structure(structure), m_graphicsView(new frac::ControlPointEditor(*this)) {
    ui->setupUi(this);
    this->ui->graphicsViewLayout->addWidget(m_graphicsView);
    m_graphicsView->setScene(&m_scene);
    m_graphicsView->scale(1, -1.0);
    m_scene.setBackgroundBrush(Qt::white);
    m_lastControlPointIndex = -1;
    m_lastFaceIndex = -1;

    m_coordinates.clear();
    m_coordinatesTemp.clear();
    float radius = 100.0f;
    float t = 220.0f;
    for (std::size_t i = 0; i < structure->faces().size(); i++) {
        //add face to drawing
        std::size_t nbCtrlPts = structure->nbControlPointsOfFace(i);
        m_coordinates.emplace_back();
        m_coordinatesTemp.emplace_back();
        for (std::size_t j = 0; j < nbCtrlPts; j++) {
            m_coordinates[i].emplace_back(radius * qCos(static_cast<float>(j) * 2.0f * 3.1415926f / static_cast<float>(nbCtrlPts)) + t * static_cast<float>(i), radius * qSin(static_cast<float>(j) * 2.0f * 3.1415926f / static_cast<float>(nbCtrlPts)));
            m_coordinatesTemp[i].emplace_back(m_coordinates[i][j]);
        }
    }

    connect(this->ui->pushButton_ok, &QPushButton::clicked, this, &SchemeWindow::valid);
    connect(this->ui->doubleSpinBox_controlPointX, &QDoubleSpinBox::valueChanged, this, &SchemeWindow::changeXCoordControlPoint);
    connect(this->ui->doubleSpinBox_controlPointY, &QDoubleSpinBox::valueChanged, this, &SchemeWindow::changeYCoordControlPoint);
    connect(this->ui->pushButton_save, &QPushButton::clicked, this, &SchemeWindow::save);
    connect(this->ui->pushButton_load, &QPushButton::clicked, this, &SchemeWindow::load);
    connect(this->ui->pushButton_rotation, &QPushButton::clicked, this, &SchemeWindow::rotateFace);
    connect(this->ui->pushButton_translation, &QPushButton::clicked, this, &SchemeWindow::translateFace);
    connect(this->ui->pushButton_localDistribution, &QPushButton::clicked, this, &SchemeWindow::localDistFace);

    this->redraw(false);
}

SchemeWindow::~SchemeWindow() {
    delete ui;
}

bool SchemeWindow::isValidForStructure(frac::Structure* structure) const {
    bool res = false;
    //check if enough coordinates
    if (structure->faces().size() == m_coordinatesTemp.size()) {
        res = true;
        for (std::size_t i = 0; i < structure->faces().size(); i++) {
            if (m_coordinatesTemp[i].size() != structure->nbControlPointsOfFace(i)) {
                res = false;
            }
        }
    }
    //check if same adjacencies
    if (res) {
        if (m_structure != nullptr && m_structure->adjacencies().size() == structure->adjacencies().size()) {
            for (std::size_t i = 0; i < m_structure->adjacencies().size(); i++) {
                if (!m_structure->adjacencies()[i].equals(structure->adjacencies()[i])) {
                    res = false;
                }
            }
        } else {
            res = false;
        }
    }

    return res;
}

std::vector<std::vector<QPointF>> const& SchemeWindow::coordinates() const {
    return m_coordinates;
}

void SchemeWindow::valid() {
    for (std::size_t i = 0; i < m_coordinates.size(); i++) {
        for (std::size_t j = 0; j < m_coordinates[i].size(); j++) {
            m_coordinates[i][j] = m_coordinatesTemp[i][j];
        }
    }
    this->close();
}

void SchemeWindow::save() {
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

void SchemeWindow::load() {
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

void SchemeWindow::rotateFace() {
    if (m_lastFaceIndex != -1) {
        qreal degrees = this->ui->doubleSpinBox_rotationAngle->value();
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

void SchemeWindow::translateFace() {
    if (m_lastFaceIndex != -1) {
        qreal x = this->ui->doubleSpinBox_translationX->value();
        qreal y = this->ui->doubleSpinBox_translationY->value();
        for (QPointF& p: m_coordinatesTemp[m_lastFaceIndex]) {
            p.setX(p.x() + x);
            p.setY(p.y() + y);
        }
        this->redraw(true);
    }
}

void SchemeWindow::localDistFace() {
    if (m_lastFaceIndex != -1) {
        //barycenter coordinates
        qreal x = 0.0;
        qreal y = 0.0;

        //number of control points that are not intern (equivalent to the number of corners)
        float nbCtrlPtsF = 0.0f;
        for (std::size_t i = 0; i < m_coordinatesTemp[m_lastFaceIndex].size(); i++) {
            x += m_coordinatesTemp[m_lastFaceIndex][i].x();
            y += m_coordinatesTemp[m_lastFaceIndex][i].y();
            if (!m_structure->isInternControlPoint(i, m_lastFaceIndex)) {
                nbCtrlPtsF += 1.0f;
            }
        }
        x /= static_cast<float>(m_coordinatesTemp[m_lastFaceIndex].size());
        y /= static_cast<float>(m_coordinatesTemp[m_lastFaceIndex].size());

        //distribute points around the origin and add the computed barycenter to place correctly the face
        double radius = 100.0;

        //for not intern control points
        float j = 0.0f;
        for (std::size_t i = 0; i < m_coordinatesTemp[m_lastFaceIndex].size(); i++) {
            if (!m_structure->isInternControlPoint(i, m_lastFaceIndex)) {
                m_coordinatesTemp[m_lastFaceIndex][i].setX(radius * qCos(static_cast<float>(j) * 2.0f * 3.1415926f / nbCtrlPtsF) + x);
                m_coordinatesTemp[m_lastFaceIndex][i].setY(radius * qSin(static_cast<float>(j) * 2.0f * 3.1415926f / nbCtrlPtsF) + y);
                j+= 1.0f;
            }
        }

        int nbCtrlPts = static_cast<int>(m_coordinatesTemp[m_lastFaceIndex].size());
        for (int i = 0; i < static_cast<int>(m_coordinatesTemp[m_lastFaceIndex].size()); i++) {
            if (m_structure->isInternControlPoint(i, m_lastFaceIndex)) {
                m_coordinatesTemp[m_lastFaceIndex][i].setX((m_coordinatesTemp[m_lastFaceIndex][frac::utils::mod(i - 1, nbCtrlPts)].x() + m_coordinatesTemp[m_lastFaceIndex][frac::utils::mod(i + 1, nbCtrlPts)].x()) / 2.0);
                m_coordinatesTemp[m_lastFaceIndex][i].setY((m_coordinatesTemp[m_lastFaceIndex][frac::utils::mod(i - 1, nbCtrlPts)].y() + m_coordinatesTemp[m_lastFaceIndex][frac::utils::mod(i + 1, nbCtrlPts)].y()) / 2.0);
            }
        }

        this->redraw(true);
    }
}

void SchemeWindow::redraw(bool useCurrentCoordinates) {
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
            }
        }
        shapePath.setFillRule(Qt::FillRule::WindingFill);
        m_scene.addPath(shapePath, QPen(), QBrush(Qt::GlobalColor::lightGray));

        //draw gaps
        QPointF center(0, 0);
        for (auto j: coords[i]) {
            center += j;
        }
        center /= static_cast<float>(coords[i].size());
        float meanDistanceToCenter = 0.0f;
        for (auto j: coords[i]) {
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
            //r->setFlag(QGraphicsRectItem::GraphicsItemFlag::ItemIsMovable);
        }
    }
}

void SchemeWindow::updateWithAdjacencies() {
    for (frac::Adjacency const& adj: m_structure->adjacencies()) {
        std::vector<std::size_t> const& indicesFace1 = m_structure->controlPointIndices(adj.Edge1, adj.Face1);
        std::vector<std::size_t> const& indicesFace2 = m_structure->controlPointIndices(adj.Edge2, adj.Face2, true);

        for (std::size_t i = 0; i < indicesFace2.size(); i++) {
            m_coordinatesTemp[adj.Face2][indicesFace2[i]] = m_coordinatesTemp[adj.Face1][indicesFace1[i]];
            m_coordinates[adj.Face2][indicesFace2[i]] = m_coordinates[adj.Face1][indicesFace1[i]];
        }
    }
}

void SchemeWindow::changeXCoordControlPoint(double value) {
    if (m_lastFaceIndex != -1 && m_lastControlPointIndex != -1) {
        m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex].setX(value);
        this->redraw(true);
    }
}

void SchemeWindow::changeYCoordControlPoint(double value) {
    if (m_lastFaceIndex != -1 && m_lastControlPointIndex != -1) {
        m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex].setY(value);
        this->redraw(true);
    }
}

void SchemeWindow::setCoords(size_t indexFace, size_t indexControlPoint, QPointF newPos) {
    m_coordinatesTemp[indexFace][indexControlPoint] = newPos;
}

void SchemeWindow::setSelected(int indexFace, int indexControlPoint) {
    m_lastFaceIndex = indexFace;
    m_lastControlPointIndex = indexControlPoint;
}
