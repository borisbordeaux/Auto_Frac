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

SchemeWindow::SchemeWindow(std::unique_ptr<frac::Structure> structure) :
        QWidget(nullptr), ui(new Ui::SchemeWindow), m_structure(std::move(structure)), m_graphicsView(new frac::SchemeEditor(*this)) {
    ui->setupUi(this);
    this->ui->graphicsViewLayout->addWidget(m_graphicsView);
    m_graphicsView->setScene(&m_scene);
    m_graphicsView->scale(1, -1.0);
    m_scene.setBackgroundBrush(Qt::white);
    m_lastControlPointIndex = -1;
    m_lastFaceIndex = -1;

    //roughly display faces with their control points all at same position
    float t = 420.0f;
    for (std::size_t i = 0; i < m_structure->faces().size(); i++) {
        //add face to drawing
        std::size_t nbCtrlPts = m_structure->nbControlPointsOfFace(i);
        m_coordinates.emplace_back();
        m_coordinatesTemp.emplace_back();
        for (std::size_t j = 0; j < nbCtrlPts; j++) {
            m_coordinates[i].emplace_back(t * static_cast<float>(i), 0);
            m_coordinatesTemp[i].emplace_back(m_coordinates[i][j]);
        }

        //then set a better position for the control points
        this->localDistributionFace(i, false);
        this->localDistributionFace(i, true);

        //set by default no rotation
        m_faceRotations.emplace_back(0);
    }

    connect(this->ui->pushButton_ok, &QPushButton::clicked, this, &SchemeWindow::valid);
    connect(this->ui->doubleSpinBox_controlPointX, &QDoubleSpinBox::valueChanged, this, &SchemeWindow::changeXCoordControlPoint);
    connect(this->ui->doubleSpinBox_controlPointY, &QDoubleSpinBox::valueChanged, this, &SchemeWindow::changeYCoordControlPoint);
    connect(this->ui->pushButton_save, &QPushButton::clicked, this, &SchemeWindow::save);
    connect(this->ui->pushButton_load, &QPushButton::clicked, this, &SchemeWindow::load);
    connect(this->ui->dial_rotationAngle, &QDial::valueChanged, this, &SchemeWindow::rotateFace);
    connect(this->ui->pushButton_localDistribution, &QPushButton::clicked, this, &SchemeWindow::localDistFace);
    connect(this->ui->radioButton_scheme, &QRadioButton::released, this, &SchemeWindow::updateTempDraw);
    connect(this->ui->radioButton_subdScheme, &QRadioButton::released, this, &SchemeWindow::updateTempDraw);
    connect(this->ui->checkBox_controlPoints, &QCheckBox::released, this, &SchemeWindow::updateTempDraw);
    connect(this->ui->doubleSpinBox_gapRadius, &QDoubleSpinBox::valueChanged, this, &SchemeWindow::updateTempDraw);
    connect(this->ui->doubleSpinBox_midCantorRadius, &QDoubleSpinBox::valueChanged, this, &SchemeWindow::updateTempDraw);

    this->redraw(false);
}

SchemeWindow::~SchemeWindow() {
    delete ui;
}

bool SchemeWindow::isValidForStructure(frac::Structure const& structure) const {
    bool res = false;
    //check if enough coordinates
    if (structure.faces().size() == m_coordinatesTemp.size()) {
        res = true;
        for (std::size_t i = 0; i < structure.faces().size(); i++) {
            if (m_coordinatesTemp[i].size() != structure.nbControlPointsOfFace(i)) {
                res = false;
            }
        }
    }
    //check if same adjacencies
    if (res) {
        if (m_structure != nullptr && m_structure->adjacencies().size() == structure.adjacencies().size()) {
            for (std::size_t i = 0; i < m_structure->adjacencies().size(); i++) {
                if (!m_structure->adjacencies()[i].equals(structure.adjacencies()[i])) {
                    res = false;
                }
            }
        } else {
            res = false;
        }
    }

    return res;
}

std::vector<std::vector<frac::Point2D>> SchemeWindow::coordinates() const {
    float scale = 0.01f;
    std::vector<std::vector<frac::Point2D>> result;
    for (std::vector<QPointF> const& facesCoords: m_coordinates) {
        result.emplace_back();
        for (QPointF const& p: facesCoords) {
            result[result.size() - 1].emplace_back(p.x() * scale, p.y() * scale);
        }
    }
    return result;
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

void SchemeWindow::rotateFace(int value) {
    this->ui->label_rotationAngle->setText(QString::number(value) + "°");
    if (m_lastFaceIndex != -1) {
        qreal degrees = value - m_faceRotations[m_lastFaceIndex];
        if (degrees == 0) { return; }
        m_faceRotations[m_lastFaceIndex] = value;
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

void SchemeWindow::localDistFace() {
    if (m_lastFaceIndex != -1) {
        this->localDistributionFace(m_lastFaceIndex, true);
        m_faceRotations[m_lastFaceIndex] = 0;
        this->ui->dial_rotationAngle->setValue(0);
        this->redraw(true);
    }
}

void SchemeWindow::redraw(bool useTempCoordinates) {
    std::vector<std::vector<QPointF>> const& coords = useTempCoordinates ? m_coordinatesTemp : m_coordinates;
    m_scene.clear();
    this->updateWithAdjacencies();
    for (std::size_t i = 0; i < coords.size(); i++) {
        if (this->ui->radioButton_scheme->isChecked()) {
            this->drawScheme(i, coords);
        } else {
            this->drawSubdScheme(i, coords);
        }
    }
    for (std::size_t i = 0; i < coords.size(); i++) {
        if (this->ui->checkBox_controlPoints->isChecked()) {
            this->drawControlPoints(i, coords);
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

void SchemeWindow::setCoords(std::size_t indexFace, std::size_t indexControlPoint, QPointF newPos) {
    m_coordinatesTemp[indexFace][indexControlPoint] = newPos;
    this->ui->doubleSpinBox_controlPointX->blockSignals(true);
    this->ui->doubleSpinBox_controlPointY->blockSignals(true);
    this->ui->doubleSpinBox_controlPointX->setValue(m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex].x());
    this->ui->doubleSpinBox_controlPointY->setValue(m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex].y());
    this->ui->doubleSpinBox_controlPointX->blockSignals(false);
    this->ui->doubleSpinBox_controlPointY->blockSignals(false);
}

void SchemeWindow::setSelected(int indexFace, int indexControlPoint) {
    setSelected(indexFace);
    m_lastControlPointIndex = indexControlPoint;
    this->ui->doubleSpinBox_controlPointX->blockSignals(true);
    this->ui->doubleSpinBox_controlPointY->blockSignals(true);
    this->ui->doubleSpinBox_controlPointX->setValue(m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex].x());
    this->ui->doubleSpinBox_controlPointY->setValue(m_coordinatesTemp[m_lastFaceIndex][m_lastControlPointIndex].y());
    this->ui->doubleSpinBox_controlPointX->blockSignals(false);
    this->ui->doubleSpinBox_controlPointY->blockSignals(false);
}

void SchemeWindow::setSelected(int indexFace) {
    m_lastFaceIndex = indexFace;
    this->ui->dial_rotationAngle->setValue(m_faceRotations[indexFace]);
}

void SchemeWindow::localDistributionFace(std::size_t indexFace, bool useTempCoordinates) {
    auto& coords = useTempCoordinates ? m_coordinatesTemp : m_coordinates;
    //barycenter coordinates
    qreal x = 0.0;
    qreal y = 0.0;

    //number of control points that are not intern (equivalent to the number of corners)
    float nbCtrlPtsF = 0.0f;
    for (std::size_t i = 0; i < coords[indexFace].size(); i++) {
        x += coords[indexFace][i].x();
        y += coords[indexFace][i].y();
        if (!m_structure->isInternControlPoint(i, indexFace)) {
            nbCtrlPtsF += 1.0f;
        }
    }
    x /= static_cast<float>(coords[indexFace].size());
    y /= static_cast<float>(coords[indexFace].size());

    //distribute points around the origin and add the computed barycenter to place correctly the face
    double radius = this->ui->doubleSpinBox_radiusDistribControlPoints->value();

    //for not intern control points
    float j = 0.0f;
    for (std::size_t i = 0; i < coords[indexFace].size(); i++) {
        if (!m_structure->isInternControlPoint(i, indexFace)) {
            coords[indexFace][i].setX(radius * qCos(static_cast<float>(j) * 2.0f * 3.1415926f / nbCtrlPtsF) + x);
            coords[indexFace][i].setY(radius * qSin(static_cast<float>(j) * 2.0f * 3.1415926f / nbCtrlPtsF) + y);
            j += 1.0f;
        }
    }

    int nbCtrlPts = static_cast<int>(coords[indexFace].size());
    bool firstInternCP = true;
    for (int i = 0; i < static_cast<int>(coords[indexFace].size()); i++) {
        if (m_structure->isInternControlPoint(i, indexFace)) {
            if (m_structure->bezierType() == frac::BezierType::Cubic_Bezier) {
                if (firstInternCP) {
                    QPointF P0 = coords[indexFace][i - 1];
                    QPointF P1 = coords[indexFace][(i + 2) % nbCtrlPts];
                    QPointF c = SchemeWindow::coordOfPointOnLineAt(1.f / 3.f, P0, P1);
                    coords[indexFace][i] = c;
                    firstInternCP = false;
                } else {
                    QPointF P0 = coords[indexFace][i - 2];
                    QPointF P1 = coords[indexFace][(i + 1) % nbCtrlPts];
                    QPointF c = SchemeWindow::coordOfPointOnLineAt(2.f / 3.f, P0, P1);
                    coords[indexFace][i] = c;
                    firstInternCP = true;
                }
            } else {
                coords[indexFace][i] = (coords[indexFace][i - 1] + coords[indexFace][(i + 1) % nbCtrlPts]) / 2.0f;
            }
        }
    }
}

void SchemeWindow::closeEvent(QCloseEvent* event) {
    for (std::size_t i = 0; i < m_coordinates.size(); i++) {
        for (std::size_t j = 0; j < m_coordinates[i].size(); j++) {
            m_coordinatesTemp[i][j] = m_coordinates[i][j];
        }
    }
    QWidget::closeEvent(event);
}

void SchemeWindow::drawScheme(std::size_t i, std::vector<std::vector<QPointF>> const& coords) {
    std::vector<std::pair<QLineF, QPen>> cantors;
    std::vector<std::pair<QPainterPath, QPen>> beziers;
    std::vector<QPointF> points;
    QPainterPath shapePath;
    shapePath.moveTo(coords[i][0]);
    std::size_t j = 0;
    for (frac::Edge const& e: m_structure->faces()[i].constData()) {
        std::vector<std::size_t> indices = m_structure->controlPointIndices(j, i);
        points.emplace_back(coords[i][indices[0]]);
        if (indices.size() == 2) { //CANTOR
            cantors.emplace_back(QLineF(coords[i][indices[0]], coords[i][indices[1]]), SchemeWindow::penOfEdge(e));

            shapePath.lineTo(coords[i][indices[1]]);
        }
        if (indices.size() == 3) { //BEZIER QUAD
            QPainterPath path;
            path.moveTo(coords[i][indices[0]]);
            path.quadTo(coords[i][indices[1]], coords[i][indices[2]]);
            beziers.emplace_back(path, SchemeWindow::penOfEdge(e));

            shapePath.quadTo(coords[i][indices[1]], coords[i][indices[2]]);
        }
        if (indices.size() == 4) { //BEZIER CUBIC
            QPainterPath path;
            path.moveTo(coords[i][indices[0]]);
            path.cubicTo(coords[i][indices[1]], coords[i][indices[2]], coords[i][indices[3]]);
            beziers.emplace_back(path, SchemeWindow::penOfEdge(e));

            shapePath.cubicTo(coords[i][indices[1]], coords[i][indices[2]], coords[i][indices[3]]);
        }
        j++;
    }
    shapePath.setFillRule(Qt::FillRule::WindingFill);
    QPen pen;
    pen.setBrush(Qt::transparent);
    auto pathItem = m_scene.addPath(shapePath, pen, QBrush(QColor("skyblue")));
    pathItem->setData(2, static_cast<unsigned int>(i));

    for (auto const& c: cantors) {
        m_scene.addLine(c.first, c.second);
    }
    for (auto const& p: beziers) {
        m_scene.addPath(p.first, p.second);
    }

    float thick = 10.0f;
    for (auto const& p: points) {
        m_scene.addEllipse(p.x() - thick / 2.0f, p.y() - thick / 2.0f, thick, thick, QPen(), Qt::black);
    }
}

void SchemeWindow::drawControlPoints(std::size_t i, std::vector<std::vector<QPointF>> const& coords) {
    float thick = 12.0f;
    bool secondIsIntern = m_structure->isInternControlPoint(1, i);
    bool thirdIsIntern = m_structure->isInternControlPoint(2, i);
    for (std::size_t j = 0; j < coords[i].size(); j++) {
        bool isIntern = m_structure->isInternControlPoint(j, i);
        bool isFirstEdge = (j == 0 || (j == 1 && !secondIsIntern) || (j == 2 && secondIsIntern && !thirdIsIntern) || (j == 3 && secondIsIntern && thirdIsIntern));
        QBrush brush = isFirstEdge ? Qt::green : (isIntern ? Qt::blue : Qt::black);
        QGraphicsEllipseItem* point = m_scene.addEllipse(coords[i][j].x() - thick / 2.0f, coords[i][j].y() - thick / 2.0f, thick, thick, QPen(), brush);
        int data0 = static_cast<int>(i);
        int data1 = static_cast<int>(j);
        bool onConstraint = false;
        for (frac::Adjacency const& adj: m_structure->adjacencies()) {
            if (adj.Face2 == i) {
                if (m_structure->isControlPointBelongEdge(j, i, adj.Edge2)) {
                    onConstraint = true;
                }
            }
        }
        if (!onConstraint) {
            point->setData(0, data0);
            point->setData(1, data1);
        }
    }
}

void SchemeWindow::drawSubdScheme(std::size_t i, std::vector<std::vector<QPointF>> const& coords) {
    this->drawSubdFace(i, coords);
    this->drawSubdEdges(i, coords);
    this->drawSubdReqEdges(i, coords);
    this->drawSubdInterior(i, coords);
    this->drawSubdLacuna(i, coords);
    this->drawSubdBlackPointsOnBoundary(i, coords);
    this->drawSubdBlackPointsOnLacuna(i, coords);
}

void SchemeWindow::drawSubdFace(std::size_t i, std::vector<std::vector<QPointF>> const& coords) {
    //some useful variables
    QPointF center(0, 0);
    for (auto p: coords[i]) {
        center += p;
    }
    center /= static_cast<float>(coords[i].size());

    frac::Face const& f = m_structure->faces()[i];

    QPainterPath shapePath;
    shapePath.moveTo(coords[i][0]);
    std::size_t j = 0;
    for (frac::Edge const& e: f.constData()) {
        std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
        QPointF nextBegin = coords[i][frac::utils::mod(j + nextStepJ, coords[i].size())];
        QPointF currentBegin = coords[i][j];

        if (e.edgeType() == frac::EdgeType::BEZIER) {
            if (m_structure->bezierType() == frac::BezierType::Cubic_Bezier) {
                shapePath.cubicTo(coords[i][j + 1], coords[i][j + 2], nextBegin);
            } else {
                shapePath.quadTo(coords[i][j + 1], nextBegin);
            }
        } else { // CANTOR
            unsigned int n = e.nbActualSubdivisions();
            QVector2D v = QVector2D(nextBegin - currentBegin);
            float length = static_cast<float>(this->ui->doubleSpinBox_midCantorRadius->value()) * v.length() / static_cast<float>(n + n - 1);
            QVector2D normal(-v.y(), v.x()); //rotation 90°
            normal.normalize();
            for (unsigned int k = 0; k < n; k++) {
                QPointF begin = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k) / static_cast<float>(n + n - 1), coords[i][j], nextBegin);
                QPointF end = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k + 1) / static_cast<float>(n + n - 1), coords[i][j], nextBegin);
                if (k != 0) {
                    //draw of required edge
                    QPointF endBefore = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k - 1) / static_cast<float>(n + n - 1), coords[i][j], nextBegin);
                    QPointF centerLine = (begin + endBefore) * 0.5f;
                    if (f.reqEdge().edgeType() == frac::EdgeType::CANTOR) {
                        QPointF pos = SchemeWindow::coordOfPointOnQuadCurveAt(0.5f, endBefore, (centerLine + (normal * length).toPointF()), begin);
                        shapePath.lineTo(pos);
                        shapePath.lineTo(begin);
                    } else {
                        shapePath.quadTo(centerLine + (normal * length).toPointF(), begin);
                    }
                }
                shapePath.lineTo(end);
            }
        }
        j += nextStepJ;
    }
    shapePath.setFillRule(Qt::FillRule::WindingFill);
    QPen pen;
    pen.setBrush(Qt::transparent);
    QGraphicsPathItem* pathItem = m_scene.addPath(shapePath, pen, QBrush(QColor("skyblue")));
    pathItem->setData(2, static_cast<unsigned int>(i));
}

void SchemeWindow::drawSubdEdges(std::size_t i, std::vector<std::vector<QPointF>> const& coords) {
    //some useful variables
    QPointF center(0, 0);
    for (auto p: coords[i]) {
        center += p;
    }
    center /= static_cast<float>(coords[i].size());

    frac::Face const& f = m_structure->faces()[i];

    //draw subdivided edges
    std::vector<std::pair<QLineF, QPen>> cantors;
    std::vector<std::pair<QPainterPath, QPen>> beziers;

    std::size_t j = 0;
    for (frac::Edge const& e: f.constData()) {
        std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
        QPointF nextBegin = coords[i][frac::utils::mod(j + nextStepJ, coords[i].size())];
        QPointF currentBegin = coords[i][j];

        if (e.edgeType() == frac::EdgeType::BEZIER) {
            if (m_structure->bezierType() == frac::BezierType::Cubic_Bezier) {
                QPainterPath path;
                path.moveTo(currentBegin);
                path.cubicTo(coords[i][j + 1], coords[i][j + 2], nextBegin);
                beziers.emplace_back(path, SchemeWindow::penOfEdge(e.subdivisions(f.reqEdge())[0]));
            } else {
                QPainterPath path;
                path.moveTo(currentBegin);
                path.quadTo(coords[i][j + 1], nextBegin);
                beziers.emplace_back(path, SchemeWindow::penOfEdge(e.subdivisions(f.reqEdge())[0]));
            }
        } else { // CANTOR
            unsigned int n = e.nbActualSubdivisions();
            QVector2D v = QVector2D(nextBegin - currentBegin);
            QVector2D normal(-v.y(), v.x()); //rotation 90°
            normal.normalize();
            for (unsigned int k = 0; k < n; k++) {
                QPointF begin = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k) / static_cast<float>(n + n - 1), coords[i][j], nextBegin);
                QPointF end = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k + 1) / static_cast<float>(n + n - 1), coords[i][j], nextBegin);
                //draw sub cantor
                cantors.emplace_back(QLineF(begin, end), SchemeWindow::penOfEdge(e.subdivisions(f.reqEdge())[0]));
            }
        }
        j += nextStepJ;
    }

    for (auto const& c: cantors) {
        m_scene.addLine(c.first, c.second);
    }
    for (auto const& p: beziers) {
        m_scene.addPath(p.first, p.second);
    }
}

void SchemeWindow::drawSubdReqEdges(std::size_t i, std::vector<std::vector<QPointF>> const& coords) {
    //some useful variables
    QPointF center(0, 0);
    for (auto p: coords[i]) {
        center += p;
    }
    center /= static_cast<float>(coords[i].size());

    frac::Face const& f = m_structure->faces()[i];

    //draw subdivided edges
    std::vector<std::pair<QLineF, QPen>> cantors;
    std::vector<std::pair<QPainterPath, QPen>> beziers;

    std::size_t j = 0;
    for (frac::Edge const& e: f.constData()) {
        std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
        QPointF nextBegin = coords[i][frac::utils::mod(j + nextStepJ, coords[i].size())];
        QPointF currentBegin = coords[i][j];

        if (e.edgeType() == frac::EdgeType::CANTOR) {
            unsigned int n = e.nbActualSubdivisions();
            QVector2D v = QVector2D(nextBegin - currentBegin);
            float length = static_cast<float>(this->ui->doubleSpinBox_midCantorRadius->value()) * v.length() / static_cast<float>(n + n - 1);
            QVector2D normal(-v.y(), v.x()); //rotation 90°
            normal.normalize();
            for (unsigned int k = 0; k < n; k++) {
                QPointF begin = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k) / static_cast<float>(n + n - 1), coords[i][j], nextBegin);
                if (k != 0) {
                    //draw of required edge
                    QPointF endBefore = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k - 1) / static_cast<float>(n + n - 1), coords[i][j], nextBegin);
                    QPointF centerLine = (begin + endBefore) * 0.5f;
                    if (f.reqEdge().edgeType() == frac::EdgeType::CANTOR) {
                        QPointF pos = SchemeWindow::coordOfPointOnQuadCurveAt(0.5f, endBefore, (centerLine + (normal * length).toPointF()), begin);
                        cantors.emplace_back(QLineF(endBefore, pos), SchemeWindow::penOfEdge(f.reqEdge()));
                        cantors.emplace_back(QLineF(pos, begin), SchemeWindow::penOfEdge(f.reqEdge()));
                    } else {
                        QPainterPath path;
                        path.moveTo(endBefore);
                        path.quadTo(centerLine + (normal * length).toPointF(), begin);
                        beziers.emplace_back(path, SchemeWindow::penOfEdge(f.reqEdge()));
                    }
                }
            }
        }
        j += nextStepJ;
    }

    for (auto const& c: cantors) {
        m_scene.addLine(c.first, c.second);
    }
    for (auto const& p: beziers) {
        m_scene.addPath(p.first, p.second);
    }
}

void SchemeWindow::drawSubdInterior(std::size_t i, std::vector<std::vector<QPointF>> const& coords) {
    //some useful variables
    QPointF center(0, 0);
    for (auto p: coords[i]) {
        center += p;
    }
    center /= static_cast<float>(coords[i].size());
    float meanDistanceToCenter = 0.0f;
    for (auto p: coords[i]) {
        meanDistanceToCenter += QVector2D(center - p).length();
    }
    meanDistanceToCenter /= static_cast<float>(coords[i].size());
    float diameter = meanDistanceToCenter * static_cast<float>(this->ui->doubleSpinBox_gapRadius->value());
    float radius = diameter / 2.0f;

    frac::Face const& f = m_structure->faces()[i];

    //there are some lines that are always here if face has no delay
    std::size_t j = 0;
    for (frac::Edge const& e: f.constData()) {
        std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
        QPointF nextBegin = coords[i][(j + nextStepJ) % coords[i].size()];
        QPointF currentBegin = coords[i][j];
        if (e.edgeType() == frac::EdgeType::BEZIER) {
            //there is a line between each subdivision
            unsigned int n = e.nbActualSubdivisions();
            for (unsigned int k = 0; k < n - 1; k++) {
                QPointF begin;
                if (m_structure->bezierType() == frac::BezierType::Cubic_Bezier) {
                    begin = SchemeWindow::coordOfPointOnCubicCurveAt(static_cast<float>(k + 1) / static_cast<float>(n), currentBegin, coords[i][j + 1], coords[i][j + 2], nextBegin);
                } else {
                    begin = SchemeWindow::coordOfPointOnQuadCurveAt(static_cast<float>(k + 1) / static_cast<float>(n), currentBegin, coords[i][j + 1], nextBegin);
                }
                //point from begin to central lacuna
                QPointF end(begin + (QVector2D(center - begin).normalized() * (QVector2D(center - begin).length() - radius)).toPointF());

                if (f.delay() == 0) {
                    m_scene.addLine(QLineF(begin, end), SchemeWindow::penOfEdge(f.adjEdge()));
                }
            }
        } else { //CANTOR
            //there is a line between each subdivision
            unsigned int n = e.nbActualSubdivisions();
            QVector2D v = QVector2D(nextBegin - currentBegin);
            float length = static_cast<float>(this->ui->doubleSpinBox_midCantorRadius->value()) * v.length() / static_cast<float>(n + n - 1);
            QVector2D normal(-v.y(), v.x()); //rotation 90°
            normal.normalize();
            for (unsigned int k = 1; k < n; k++) {
                QPointF begin = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k) / static_cast<float>(n + n - 1), currentBegin, nextBegin);
                QPointF endBefore = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k - 1) / static_cast<float>(n + n - 1), currentBegin, nextBegin);
                QPointF centerLine = (begin + endBefore) * 0.5f;
                QPointF beginLine = SchemeWindow::coordOfPointOnQuadCurveAt(0.5f, endBefore, centerLine + (normal * length).toPointF(), begin);

                QPointF end(beginLine + (QVector2D(center - beginLine).normalized() * (QVector2D(center - beginLine).length() - radius)).toPointF());

                if (f.delay() == 0) {
                    m_scene.addLine(QLineF(beginLine, end), SchemeWindow::penOfEdge(f.adjEdge()));
                }
            }
        }
        j += nextStepJ;
    }

    if (f.delay() == 0) {
        //then some lines are added depending on the algorithm of the face
        switch (f.algo()) {
            case frac::AlgorithmSubdivision::LinksSurroundDelay:
                j = 0;
                for (frac::Edge const& e: f.constData()) {
                    std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
                    if (e.isDelay()) {
                        QPointF begin = coords[i][j];
                        QPointF end = coords[i][(j + nextStepJ) % coords[i].size()];
                        QPointF endBeginLine(begin + (QVector2D(center - begin).normalized() * (QVector2D(center - begin).length() - radius)).toPointF());
                        QPointF endEndLine(end + (QVector2D(center - end).normalized() * (QVector2D(center - end).length() - radius)).toPointF());
                        m_scene.addLine(QLineF(begin, endBeginLine), SchemeWindow::penOfEdge(f.adjEdge()));
                        m_scene.addLine(QLineF(end, endEndLine), SchemeWindow::penOfEdge(f.adjEdge()));
                    }
                    j += nextStepJ;
                }
                break;
            case frac::AlgorithmSubdivision::LinksOnCorners:
                j = 0;
                for (frac::Edge const& e: f.constData()) {
                    std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
                    QPointF begin = coords[i][j];
                    QPointF end(begin + (QVector2D(center - begin).normalized() * (QVector2D(center - begin).length() - radius)).toPointF());
                    m_scene.addLine(QLineF(begin, end), SchemeWindow::penOfEdge(f.adjEdge()));
                    j += nextStepJ;
                }
                break;
            case frac::AlgorithmSubdivision::LinksSurroundDelayAndBezier:
                j = 0;
                for (std::size_t k = 0; k < f.constData().size(); k++) {
                    frac::Edge const& e = f.constData()[k];
                    frac::Edge const& e_next = f.constData()[(k + 1) % f.constData().size()];
                    std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
                    if (e.isDelay() && e_next.isDelay()) {
                        QPointF end = coords[i][(j + nextStepJ) % coords[i].size()];
                        QPointF endEndLine(end + (QVector2D(center - end).normalized() * (QVector2D(center - end).length() - radius)).toPointF());
                        m_scene.addLine(QLineF(end, endEndLine), SchemeWindow::penOfEdge(f.adjEdge()));
                    }
                    j += nextStepJ;
                }
                break;
            default:
                break;
        }
    }
}

void SchemeWindow::drawSubdLacuna(std::size_t i, std::vector<std::vector<QPointF>> const& coords) {
    //some useful variables
    QPointF center(0, 0);
    for (auto p: coords[i]) {
        center += p;
    }
    center /= static_cast<float>(coords[i].size());
    float meanDistanceToCenter = 0.0f;
    for (auto p: coords[i]) {
        meanDistanceToCenter += QVector2D(center - p).length();
    }
    meanDistanceToCenter /= static_cast<float>(coords[i].size());
    float diameter = meanDistanceToCenter * static_cast<float>(this->ui->doubleSpinBox_gapRadius->value());
    float radius = diameter / 2.0f;

    frac::Face const& f = m_structure->faces()[i];

    std::vector<QPointF> pointsOnCentralLacuna;

    //then draw interior depending on the algorithm
    //there are some lines that are always here if face has no delay
    std::size_t j = 0;
    for (frac::Edge const& e: f.constData()) {
        std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
        QPointF nextBegin = coords[i][(j + nextStepJ) % coords[i].size()];
        QPointF currentBegin = coords[i][j];
        if (e.edgeType() == frac::EdgeType::BEZIER) {
            //there is a line between each subdivision
            unsigned int n = e.nbActualSubdivisions();
            for (unsigned int k = 0; k < n - 1; k++) {
                QPointF begin;
                if (m_structure->bezierType() == frac::BezierType::Cubic_Bezier) {
                    begin = SchemeWindow::coordOfPointOnCubicCurveAt(static_cast<float>(k + 1) / static_cast<float>(n), currentBegin, coords[i][j + 1], coords[i][j + 2], nextBegin);
                } else {
                    begin = SchemeWindow::coordOfPointOnQuadCurveAt(static_cast<float>(k + 1) / static_cast<float>(n), currentBegin, coords[i][j + 1], nextBegin);
                }
                //point from begin to central lacuna
                QPointF end(begin + (QVector2D(center - begin).normalized() * (QVector2D(center - begin).length() - radius)).toPointF());

                if (f.delay() == 0) {
                    pointsOnCentralLacuna.emplace_back(end);
                }
            }
        } else { //CANTOR
            //there is a line between each subdivision
            unsigned int n = e.nbActualSubdivisions();
            QVector2D v = QVector2D(nextBegin - currentBegin);
            float length = static_cast<float>(this->ui->doubleSpinBox_midCantorRadius->value()) * v.length() / static_cast<float>(n + n - 1);
            QVector2D normal(-v.y(), v.x()); //rotation 90°
            normal.normalize();
            for (unsigned int k = 1; k < n; k++) {
                QPointF begin = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k) / static_cast<float>(n + n - 1), currentBegin, nextBegin);
                QPointF endBefore = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k - 1) / static_cast<float>(n + n - 1), currentBegin, nextBegin);
                QPointF centerLine = (begin + endBefore) * 0.5f;
                QPointF beginLine = SchemeWindow::coordOfPointOnQuadCurveAt(0.5f, endBefore, centerLine + (normal * length).toPointF(), begin);

                QPointF end(beginLine + (QVector2D(center - beginLine).normalized() * (QVector2D(center - beginLine).length() - radius)).toPointF());

                if (f.delay() == 0) {
                    pointsOnCentralLacuna.emplace_back(end);
                }
            }
        }
        j += nextStepJ;
    }

    if (f.delay() == 0) {
        //then some lines are added depending on the algorithm of the face
        switch (f.algo()) {
            case frac::AlgorithmSubdivision::LinksSurroundDelay:
                j = 0;
                for (frac::Edge const& e: f.constData()) {
                    std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
                    if (e.isDelay()) {
                        QPointF begin = coords[i][j];
                        QPointF end = coords[i][(j + nextStepJ) % coords[i].size()];
                        QPointF endBeginLine(begin + (QVector2D(center - begin).normalized() * (QVector2D(center - begin).length() - radius)).toPointF());
                        QPointF endEndLine(end + (QVector2D(center - end).normalized() * (QVector2D(center - end).length() - radius)).toPointF());
                        m_scene.addLine(QLineF(begin, endBeginLine), SchemeWindow::penOfEdge(f.adjEdge()));
                        m_scene.addLine(QLineF(end, endEndLine), SchemeWindow::penOfEdge(f.adjEdge()));

                        pointsOnCentralLacuna.emplace_back(endBeginLine);
                        pointsOnCentralLacuna.emplace_back(endEndLine);
                    }
                    j += nextStepJ;
                }
                break;
            case frac::AlgorithmSubdivision::LinksOnCorners:
                j = 0;
                for (frac::Edge const& e: f.constData()) {
                    std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
                    QPointF begin = coords[i][j];
                    QPointF end(begin + (QVector2D(center - begin).normalized() * (QVector2D(center - begin).length() - radius)).toPointF());
                    pointsOnCentralLacuna.emplace_back(end);
                    j += nextStepJ;
                }
                break;
            default:
                break;
        }

        //draw central lacuna
        if (f.gapEdge().edgeType() == frac::EdgeType::BEZIER) {
            m_scene.addEllipse(center.x() - radius, center.y() - radius, diameter, diameter, SchemeWindow::penOfEdge(f.gapEdge()), QBrush(Qt::white));
        } else {
            //need to sort the points based on their angle from the vertical line
            std::sort(pointsOnCentralLacuna.begin(), pointsOnCentralLacuna.end(), [center](QPointF a, QPointF b) -> bool {
                //compute the vectors from the center to the points
                QVector2D u1(a - center);
                QVector2D u2(b - center);
                //compute their angle compared to vertical
                float theta1 = qRadiansToDegrees(std::atan2(u1.x(), u1.y()));
                float theta2 = qRadiansToDegrees(std::atan2(u2.x(), u2.y()));
                //the angle above starts from 0 (vertical up vector) to 180 (vertical down vector)
                //the sign is positive if vector points to right, negative otherwise.
                //so we adjust the angle to have a value between 0 and 360
                if (theta1 < 0) {
                    theta1 += 360.0f;
                }
                if (theta2 < 0) {
                    theta2 += 360.0f;
                }
                //the sort function will compare the angles
                return theta1 < theta2;
            });
            //draw polygon with sorted points
            QPolygonF polygon;
            for (auto const& p: pointsOnCentralLacuna) {
                polygon << p;
            }
            m_scene.addPolygon(polygon, SchemeWindow::penOfEdge(f.gapEdge()), QBrush(Qt::white));
        }
    }
}

void SchemeWindow::drawSubdBlackPointsOnBoundary(std::size_t i, std::vector<std::vector<QPointF>> const& coords) {
    //some useful variables
    QPointF center(0, 0);
    for (auto p: coords[i]) {
        center += p;
    }
    center /= static_cast<float>(coords[i].size());

    frac::Face const& f = m_structure->faces()[i];

    //draw subdivided edges
    std::vector<QPointF> points;

    std::size_t j = 0;
    for (frac::Edge const& e: f.constData()) {
        std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
        QPointF nextBegin = coords[i][frac::utils::mod(j + nextStepJ, coords[i].size())];
        QPointF currentBegin = coords[i][j];

        points.emplace_back(currentBegin);

        if (e.edgeType() == frac::EdgeType::CANTOR) {
            unsigned int n = e.nbActualSubdivisions();
            for (unsigned int k = 0; k < n; k++) {
                QPointF begin = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k) / static_cast<float>(n + n - 1), coords[i][j], nextBegin);
                if (k != 0) {
                    //draw of required edge
                    QPointF endBefore = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k - 1) / static_cast<float>(n + n - 1), coords[i][j], nextBegin);

                    points.emplace_back(endBefore);
                    points.emplace_back(begin);
                }
            }
        }
        j += nextStepJ;
    }

    //then draw interior depending on the algorithm
    //there are some lines that are always here if face has no delay
    j = 0;
    for (frac::Edge const& e: f.constData()) {
        std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
        QPointF nextBegin = coords[i][(j + nextStepJ) % coords[i].size()];
        QPointF currentBegin = coords[i][j];
        if (e.edgeType() == frac::EdgeType::BEZIER) {
            //there is a line between each subdivision
            unsigned int n = e.nbActualSubdivisions();
            for (unsigned int k = 0; k < n - 1; k++) {
                QPointF begin;
                if (m_structure->bezierType() == frac::BezierType::Cubic_Bezier) {
                    begin = SchemeWindow::coordOfPointOnCubicCurveAt(static_cast<float>(k + 1) / static_cast<float>(n), currentBegin, coords[i][j + 1], coords[i][j + 2], nextBegin);
                } else {
                    begin = SchemeWindow::coordOfPointOnQuadCurveAt(static_cast<float>(k + 1) / static_cast<float>(n), currentBegin, coords[i][j + 1], nextBegin);
                }
                points.emplace_back(begin);
            }
        } else { //CANTOR
            //there is a line between each subdivision
            unsigned int n = e.nbActualSubdivisions();
            QVector2D v = QVector2D(nextBegin - currentBegin);
            float length = static_cast<float>(this->ui->doubleSpinBox_midCantorRadius->value()) * v.length() / static_cast<float>(n + n - 1);
            QVector2D normal(-v.y(), v.x()); //rotation 90°
            normal.normalize();
            for (unsigned int k = 1; k < n; k++) {
                QPointF begin = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k) / static_cast<float>(n + n - 1), currentBegin, nextBegin);
                QPointF endBefore = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k - 1) / static_cast<float>(n + n - 1), currentBegin, nextBegin);
                QPointF centerLine = (begin + endBefore) * 0.5f;
                QPointF beginLine = SchemeWindow::coordOfPointOnQuadCurveAt(0.5f, endBefore, centerLine + (normal * length).toPointF(), begin);
                points.emplace_back(beginLine);
            }
        }
        j += nextStepJ;
    }

    float thick = 10.0f;
    for (auto const& p: points) {
        m_scene.addEllipse(p.x() - thick / 2.0f, p.y() - thick / 2.0f, thick, thick, QPen(), Qt::black);
    }
}

void SchemeWindow::drawSubdBlackPointsOnLacuna(std::size_t i, std::vector<std::vector<QPointF>> const& coords) {
    //some useful variables
    QPointF center(0, 0);
    for (auto p: coords[i]) {
        center += p;
    }
    center /= static_cast<float>(coords[i].size());
    float meanDistanceToCenter = 0.0f;
    for (auto p: coords[i]) {
        meanDistanceToCenter += QVector2D(center - p).length();
    }
    meanDistanceToCenter /= static_cast<float>(coords[i].size());
    float diameter = meanDistanceToCenter * static_cast<float>(this->ui->doubleSpinBox_gapRadius->value());
    float radius = diameter / 2.0f;

    frac::Face const& f = m_structure->faces()[i];

    std::vector<QPointF> pointsOnCentralLacuna;

    //there are some lines that are always here if face has no delay
    std::size_t j = 0;
    for (frac::Edge const& e: f.constData()) {
        std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
        QPointF nextBegin = coords[i][(j + nextStepJ) % coords[i].size()];
        QPointF currentBegin = coords[i][j];
        if (e.edgeType() == frac::EdgeType::BEZIER) {
            //there is a line between each subdivision
            unsigned int n = e.nbActualSubdivisions();
            for (unsigned int k = 0; k < n - 1; k++) {
                QPointF begin;
                if (m_structure->bezierType() == frac::BezierType::Cubic_Bezier) {
                    begin = SchemeWindow::coordOfPointOnCubicCurveAt(static_cast<float>(k + 1) / static_cast<float>(n), currentBegin, coords[i][j + 1], coords[i][j + 2], nextBegin);
                } else {
                    begin = SchemeWindow::coordOfPointOnQuadCurveAt(static_cast<float>(k + 1) / static_cast<float>(n), currentBegin, coords[i][j + 1], nextBegin);
                }
                //point from begin to central lacuna
                QPointF end(begin + (QVector2D(center - begin).normalized() * (QVector2D(center - begin).length() - radius)).toPointF());

                if (f.delay() == 0) {
                    pointsOnCentralLacuna.emplace_back(end);
                }
            }
        } else { //CANTOR
            //there is a line between each subdivision
            unsigned int n = e.nbActualSubdivisions();
            QVector2D v = QVector2D(nextBegin - currentBegin);
            float length = static_cast<float>(this->ui->doubleSpinBox_midCantorRadius->value()) * v.length() / static_cast<float>(n + n - 1);
            QVector2D normal(-v.y(), v.x()); //rotation 90°
            normal.normalize();
            for (unsigned int k = 1; k < n; k++) {
                QPointF begin = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k) / static_cast<float>(n + n - 1), currentBegin, nextBegin);
                QPointF endBefore = SchemeWindow::coordOfPointOnLineAt(static_cast<float>(2 * k - 1) / static_cast<float>(n + n - 1), currentBegin, nextBegin);
                QPointF centerLine = (begin + endBefore) * 0.5f;
                QPointF beginLine = SchemeWindow::coordOfPointOnQuadCurveAt(0.5f, endBefore, centerLine + (normal * length).toPointF(), begin);

                QPointF end(beginLine + (QVector2D(center - beginLine).normalized() * (QVector2D(center - beginLine).length() - radius)).toPointF());

                if (f.delay() == 0) {
                    pointsOnCentralLacuna.emplace_back(end);
                }
            }
        }
        j += nextStepJ;
    }

    if (f.delay() == 0) {
        //then some lines are added depending on the algorithm of the face
        switch (f.algo()) {
            case frac::AlgorithmSubdivision::LinksSurroundDelay:
                j = 0;
                for (frac::Edge const& e: f.constData()) {
                    std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
                    if (e.isDelay()) {
                        QPointF begin = coords[i][j];
                        QPointF end = coords[i][(j + nextStepJ) % coords[i].size()];
                        QPointF endBeginLine(begin + (QVector2D(center - begin).normalized() * (QVector2D(center - begin).length() - radius)).toPointF());
                        QPointF endEndLine(end + (QVector2D(center - end).normalized() * (QVector2D(center - end).length() - radius)).toPointF());

                        pointsOnCentralLacuna.emplace_back(endBeginLine);
                        pointsOnCentralLacuna.emplace_back(endEndLine);
                    }
                    j += nextStepJ;
                }
                break;
            case frac::AlgorithmSubdivision::LinksOnCorners:
                j = 0;
                for (frac::Edge const& e: f.constData()) {
                    std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
                    QPointF begin = coords[i][j];
                    QPointF end(begin + (QVector2D(center - begin).normalized() * (QVector2D(center - begin).length() - radius)).toPointF());
                    pointsOnCentralLacuna.emplace_back(end);
                    j += nextStepJ;
                }
                break;
            case frac::AlgorithmSubdivision::LinksSurroundDelayAndBezier:
                j = 0;
                for (std::size_t k = 0; k < f.constData().size(); k++) {
                    frac::Edge const& e = f.constData()[k];
                    frac::Edge const& e_next = f.constData()[(k + 1) % f.constData().size()];
                    std::size_t nextStepJ = e.edgeType() == frac::EdgeType::BEZIER ? (m_structure->bezierType() == frac::BezierType::Cubic_Bezier ? 3 : 2) : 1;
                    if (e.isDelay() && e_next.isDelay()) {
                        QPointF end = coords[i][(j + nextStepJ) % coords[i].size()];
                        QPointF endEndLine(end + (QVector2D(center - end).normalized() * (QVector2D(center - end).length() - radius)).toPointF());
                        pointsOnCentralLacuna.emplace_back(endEndLine);
                    }
                    j += nextStepJ;
                }
                break;
            default:
                break;
        }

    }

    float thick = 10.0f;
    for (auto const& p: pointsOnCentralLacuna) {
        m_scene.addEllipse(p.x() - thick / 2.0f, p.y() - thick / 2.0f, thick, thick, QPen(), Qt::black);
    }
}

void SchemeWindow::updateTempDraw() {
    this->redraw();
}

void SchemeWindow::setStruct(std::unique_ptr<frac::Structure> structure) {
    m_structure = std::move(structure);
    this->redraw();
}

void SchemeWindow::translateFaceOf(std::size_t indexFace, QPointF translation) {
    for (QPointF& p: m_coordinatesTemp[indexFace]) {
        p.setX(p.x() + translation.x());
        p.setY(p.y() + translation.y());
    }
    this->redraw(true);
}

void SchemeWindow::translateStructOf(QPointF translation) {
    for (std::vector<QPointF>& face: m_coordinatesTemp) {
        for (QPointF& point: face) {
            point.setX(point.x() + translation.x());
            point.setY(point.y() + translation.y());
        }
    }
    this->redraw(true);
}

void SchemeWindow::scaleStructBy(float scale) {
    for (std::vector<QPointF>& face: m_coordinatesTemp) {
        for (QPointF& point: face) {
            point.setX(point.x() * scale);
            point.setY(point.y() * scale);
        }
    }
    this->redraw(true);
}

QPen SchemeWindow::penOfEdge(frac::Edge const& e) {
    QPen pen;
    pen.setJoinStyle(Qt::RoundJoin);
    if (e.isDelay()) {
        pen.setStyle(Qt::DotLine);

    }
    if (e.edgeType() == frac::EdgeType::BEZIER) {
        pen.setColor(QColor(0, std::max(0, 205 - static_cast<int>(e.nbSubdivisions() - 2) * 50), 0));
    } else {
        pen.setColor(QColor(0, 0, std::max(0, 255 - static_cast<int>(e.nbSubdivisions() - 2) * 50)));
    }
    pen.setWidth(5);
    return pen;
}

QPointF SchemeWindow::coordOfPointOnLineAt(float t, QPointF const& P0, QPointF const& P1) {
    frac::Point2D p0(static_cast<float>(P0.x()), static_cast<float>(P0.y()));
    frac::Point2D p1(static_cast<float>(P1.x()), static_cast<float>(P1.y()));
    frac::Point2D res = frac::utils::coordOfPointOnLineAt(t, p0, p1);
    return { res.x(), res.y() };
}

QPointF SchemeWindow::coordOfPointOnQuadCurveAt(float t, QPointF const& P0, QPointF const& P1, QPointF const& P2) {
    frac::Point2D p0(static_cast<float>(P0.x()), static_cast<float>(P0.y()));
    frac::Point2D p1(static_cast<float>(P1.x()), static_cast<float>(P1.y()));
    frac::Point2D p2(static_cast<float>(P2.x()), static_cast<float>(P2.y()));
    frac::Point2D res = frac::utils::coordOfPointOnQuadCurveAt(t, p0, p1, p2);
    return { res.x(), res.y() };
}

QPointF SchemeWindow::coordOfPointOnCubicCurveAt(float t, QPointF const& P0, QPointF const& P1, QPointF const& P2, QPointF const& P3) {
    frac::Point2D p0(static_cast<float>(P0.x()), static_cast<float>(P0.y()));
    frac::Point2D p1(static_cast<float>(P1.x()), static_cast<float>(P1.y()));
    frac::Point2D p2(static_cast<float>(P2.x()), static_cast<float>(P2.y()));
    frac::Point2D p3(static_cast<float>(P3.x()), static_cast<float>(P3.y()));
    frac::Point2D res = frac::utils::coordOfPointOnCubicCurveAt(t, p0, p1, p2, p3);
    return { res.x(), res.y() };
}
