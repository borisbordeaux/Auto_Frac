#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include "computations/computation.h"
#include "utils/measures.h"
#include <QString>
#include <QHash>
#include <QDebug>
#include <QColor>

#include "halfedge/mesh.h"
#include "halfedge/vertex.h"
#include "halfedge/halfedge.h"
#include "halfedge/face.h"
#include "utils/utils.h"
#include "polytopal/inversivecoordinates.h"

void frac::DensityComputation::computeDensity(QString const& file, int value, bool showAllImages) {
    cv::destroyAllWindows();
    cv::Mat img = cv::imread(file.toStdString(), cv::IMREAD_GRAYSCALE);
    cv::threshold(img, img, 1, 255, cv::THRESH_BINARY);
    cv::imshow(std::string("Image"), img);

    frac::utils::computeDensity(img, value, showAllImages);
}

namespace {
QVector3D closestPoint(QVector3D const& p1, QVector3D const& p2) {
    QVector3D u = p2 - p1;
    u.normalize();
    QVector3D ba = -p1;

    QVector3D BH = (QVector3D::dotProduct(ba, u)) * u;
    return p1 + BH;
}

QVector3D barycenter(std::vector<QVector3D> const& positions) {
    QVector3D res { 0, 0, 0 };
    for (QVector3D const& p: positions) {
        res += p;
    }
    res /= static_cast<float>(positions.size());
    return res;
}

QVector3D barycenter(std::vector<he::Vertex*> const& positions) {
    QVector3D res { 0, 0, 0 };
    for (he::Vertex* v: positions) {
        res += v->pos();
    }
    res /= static_cast<float>(positions.size());
    return res;
}

QVector3D approxNormal(std::vector<he::Vertex*> const& vertices) {
    QVector3D n { 0, 0, 0 };
    int s = static_cast<int>(vertices.size());
    for (int i = 0; i < s; i++) {
        QVector3D cur = vertices[i]->pos();
        QVector3D nxt = vertices[frac::utils::mod(i + 1, s)]->pos();
        QVector3D prv = vertices[frac::utils::mod(i - 1, s)]->pos();
        QVector3D x = nxt - cur;
        QVector3D y = prv - cur;
        n += QVector3D::crossProduct(x, y);
    }
    n /= static_cast<float>(s);
    return n;
}

void planarize(he::Face* f) {
    he::HalfEdge* he = f->halfEdge();
    he::HalfEdge* heNxt = he;
    std::vector<he::Vertex*> vertices;
    do {
        vertices.push_back(heNxt->origin());
        heNxt = heNxt->next();
    } while (heNxt != he);
    if (vertices.size() > 3) {
        //point the plan pass through
        QVector3D A = barycenter(vertices);
        //approx normal of the plan
        QVector3D n = approxNormal(vertices);
        //plan equation
        float a = n.x();
        float b = n.y();
        float c = n.z();
        float d = -n.x() * A.x() - n.y() * A.y() - n.z() * A.z();
        //projection of all points on the plan
        for (he::Vertex* v: vertices) {
            float lambda = (a * v->pos().x() + b * v->pos().y() + c * v->pos().z() + d) / (a * a + b * b + c * c);
            v->setPos(v->pos() - lambda * n * 0.2f);
        }
    }
}

void tangentify(he::Mesh& m) {
    std::vector<he::HalfEdge*> alreadyTreated;
    QHash<he::Vertex*, QVector3D> transforms;

    for (he::HalfEdge* he: m.halfEdges()) {
        if (std::find(alreadyTreated.begin(), alreadyTreated.end(), he) == alreadyTreated.end()) {
            he::Vertex* p1 = he->origin();
            he::Vertex* p2 = he->next()->origin();
            QVector3D closest = closestPoint(p1->pos(), p2->pos());

            // difference between the closest point and the sphere
            float l = 1.0f - closest.length();
            QVector3D c = closest * l * 0.3f;

            if (!transforms.contains(p1)) {
                transforms[p1] = p1->pos();
            }
            if (!transforms.contains(p2)) {
                transforms[p2] = p2->pos();
            }

            transforms[p1] = transforms[p1] + c;
            transforms[p2] = transforms[p2] + c;

            alreadyTreated.push_back(he->twin());
        }
    }

    for (std::pair<he::Vertex*, QVector3D> p: transforms.asKeyValueRange()) {
        p.first->setPos(p.second);
    }

}

void recenter(he::Mesh& m) {
    std::vector<he::HalfEdge*> alreadyTreated;
    std::vector<QVector3D> positions;

    for (he::HalfEdge* he: m.halfEdges()) {
        if (std::find(alreadyTreated.begin(), alreadyTreated.end(), he) == alreadyTreated.end()) {
            positions.push_back(closestPoint(he->origin()->pos(), he->next()->origin()->pos()));
            alreadyTreated.push_back(he->twin());
        }
    }

    QVector3D bary = barycenter(positions);

    for (he::Vertex* v: m.vertices()) {
        v->setPos(v->pos() - bary);
    }
}

void planarize(he::Mesh& m) {
    for (he::Face* f: m.faces()) {
        planarize(f);
    }
}

void projectToPlan(QVector3D& point) {
    point.setX(point.x() / (1.0f - point.z()));
    point.setY(point.y() / (1.0f - point.z()));
    point.setZ(0.0f);
}

[[maybe_unused]] void projectToPlan(poly::Circle& circle) {
    QVector3D p1 = circle.center() + circle.radius() * circle.axisX();
    QVector3D p2 = circle.center() - circle.radius() * circle.axisX();
    QVector3D p3 = circle.center() + circle.radius() * circle.axisY();
    projectToPlan(p1);
    projectToPlan(p2);
    projectToPlan(p3);
    circle.from3Points(p1, p2, p3);
}

[[maybe_unused]] void projectToSphere(QVector3D& point) {
    float denom = 1.0f + point.x() * point.x() + point.y() * point.y();
    point.setX(2.0f * point.x() / denom);
    point.setY(2.0f * point.y() / denom);
    point.setZ((denom - 2.0f) / denom);
}

[[maybe_unused]] void projectToSphere(poly::Circle& circle) {
    QVector3D p1 = circle.center() + circle.radius() * circle.axisX();
    QVector3D p2 = circle.center() - circle.radius() * circle.axisX();
    QVector3D p3 = circle.center() + circle.radius() * circle.axisY();
    projectToSphere(p1);
    projectToSphere(p2);
    projectToSphere(p3);
    circle.from3Points(p1, p2, p3);
}

[[maybe_unused]] poly::Circle projectToSphereC(poly::Circle const& circle) {
    QVector3D p1 = circle.center() + circle.radius() * circle.axisX();
    QVector3D p2 = circle.center() - circle.radius() * circle.axisX();
    QVector3D p3 = circle.center() + circle.radius() * circle.axisY();
    projectToSphere(p1);
    projectToSphere(p2);
    projectToSphere(p3);
    poly::Circle res = circle;
    res.from3Points(p1, p2, p3);
    res.setColor(circle.color());
    return res;
}

[[maybe_unused]] QVector3D inversion(QVector3D const& point, poly::Circle const& circleInv) {
    QVector3D OA = point - circleInv.center();
    QVector3D OB = OA.normalized() * (circleInv.radius() * circleInv.radius() / OA.length());
    return circleInv.center() + OB;
}

[[maybe_unused]] poly::Circle inversion(poly::Circle const& circleToInv, poly::Circle const& circleInv) {
    // inverts 2 points of the circle that are on a diameter, then construct the
    // circle whose center is the middle of the 2 inverted points
    // and whose radius is half the distance of the 2 inverted points
    QVector3D p1 = circleToInv.center();
    QVector3D dir = (circleToInv.center() - circleInv.center());

    // normalize direction, if both circles share their center,
    // then the direction is arbitrary the X axis
    if (qFuzzyIsNull(dir.lengthSquared())) {
        dir = { 1.0f, 0.0f, 0.0f };
    } else {
        dir.normalize();
    }
    p1 += circleToInv.radius() * dir;

    QVector3D p2 = circleToInv.center();
    p2 -= circleToInv.radius() * dir;

    QVector3D p1Inv = inversion(p1, circleInv);
    QVector3D p2Inv = inversion(p2, circleInv);

    QVector3D vecRadius = (p2Inv - p1Inv) / 2.0f;

    return { p1Inv + vecRadius, vecRadius.length(), &circleInv };
}

QColor colors[16] = {
        QColor(Qt::blue),
        QColor(Qt::darkRed),
        QColor(Qt::darkGreen),
        QColor(Qt::cyan),
        QColor(Qt::magenta),
        QColor(Qt::yellow),
        QColor(Qt::darkCyan),
        QColor(Qt::green),
        QColor(Qt::darkBlue),
        QColor(Qt::darkMagenta),
        QColor(Qt::darkYellow),
        QColor(Qt::darkGray),
        QColor(Qt::gray),
        QColor(Qt::lightGray),
        QColor(Qt::black),
        QColor(Qt::white)
};

}

void frac::Canonizer::setMeshToOrigin(he::Mesh& m) {
    std::vector<QVector3D> positions;

    for (he::Vertex* v: m.vertices()) {
        positions.push_back(v->pos());
    }

    QVector3D bary = barycenter(positions);

    for (he::Vertex* v: m.vertices()) {
        v->setPos(v->pos() - bary);
    }
}

void frac::Canonizer::canonicalizeMesh(he::Mesh& m) {
    tangentify(m);
    recenter(m);
    planarize(m);
}

std::vector<poly::Circle> frac::PolyCircle::computeIlluminatedCircles(const he::Mesh& m) {
    std::vector<poly::Circle> res;

    //int i = 0;

    for (he::Vertex* v: m.vertices()) {
        QList<he::HalfEdge*> otherHE = v->otherHalfEdges();
        if (otherHE.size() > 1) {
            QVector3D v1 = closestPoint(v->pos(), v->halfEdge()->next()->origin()->pos());
            QVector3D v2 = closestPoint(otherHE[0]->origin()->pos(), otherHE[0]->next()->origin()->pos());
            QVector3D v3 = closestPoint(otherHE[1]->origin()->pos(), otherHE[1]->next()->origin()->pos());

            //always project to plan
            projectToPlan(v1);
            projectToPlan(v2);
            projectToPlan(v3);

            poly::Circle c { v1, v2, v3 };
            c.setAxisX({ 1, 0, 0 });
            c.setAxisY({ 0, 1, 0 });
            c.setColor({ colors[14].redF(), colors[14].greenF(), colors[14].blueF() });
            //c.setColor({ colors[i % 17].redF(), colors[i % 17].greenF(), colors[i % 17].blueF() });
            res.push_back(c);
            //i++;
        }
    }

    return res;
}

std::vector<poly::Circle> frac::PolyCircle::computeIlluminatedCirclesDual(he::Mesh const& m) {
    std::vector<poly::Circle> res;

    for (he::Face* f: m.faces()) {
        std::vector<he::HalfEdge*> allHE = f->allHalfEdges();
        if (allHE.size() > 2) {
            QVector3D v1 = closestPoint(allHE[0]->origin()->pos(), allHE[0]->next()->origin()->pos());
            QVector3D v2 = closestPoint(allHE[1]->origin()->pos(), allHE[1]->next()->origin()->pos());
            QVector3D v3 = closestPoint(allHE[2]->origin()->pos(), allHE[2]->next()->origin()->pos());

            //always project to plan
            projectToPlan(v1);
            projectToPlan(v2);
            projectToPlan(v3);

            poly::Circle c { v1, v2, v3 };
            c.setAxisX({ 1, 0, 0 });
            c.setAxisY({ 0, 1, 0 });
            c.setColor({ 0.0f, 0.0f, 0.0f });
            res.push_back(c);
        }
    }

    return res;
}

std::size_t frac::PolyCircle::computeInversions(std::vector<poly::Circle>& circlesToInverse, std::vector<poly::Circle>& circlesInvertive, std::size_t index) {
    std::vector<poly::Circle> res;
    res.reserve((circlesToInverse.size() - index) * circlesInvertive.size());
    std::size_t count = 0;

    /*if (!projected) {
        // project circles to do inversion in plan, we will later reproject to sphere
        for (poly::Circle& cInv: circlesInvertive) {
            projectToPlan(cInv);
        }
        for (std::size_t i = index; i != circlesToInverse.size(); i++) {
            projectToPlan(circlesToInverse[i]);
        }
    }*/

    //inversion always in plan using inversive coordinates
    for (std::size_t i = index; i != circlesToInverse.size(); i++) {
        for (poly::Circle const& cInv: circlesInvertive) {
            float precision = 0.003f;
#if 1
            if (circlesToInverse[i].inversionCircle() != &cInv && !poly::Circle::areOrthogonalCircles(circlesToInverse[i], cInv)) {
                if (circlesToInverse[i].radius() > precision) {
                    poly::Circle inverted = poly::Circle::inverse(circlesToInverse[i], cInv);
                    inverted.setInversionCircle(&cInv);
                    inverted.updateR3Coord();
                    inverted.setOldCircleBeforeInversion(circlesToInverse[i]);
                    inverted.setNewCircleAfterInversion(inverted);
                    res.push_back(inverted);
                    count++;
                }
            }
#else
            //inversion from plan to sphere space
            //if not already inverted and circle not too small
            if (circlesToInverse[i].inversionCircle() != &cInv && circlesToInverse[i].radius() > precision) {
                poly::InversiveCoordinates circleToInverse(circlesToInverse[i]);
                poly::InversiveCoordinates inversionCircle(cInv);
                //if not orthogonal
                if (!poly::InversiveCoordinates::areOrthogonal(circleToInverse, inversionCircle)) {
                    poly::InversiveCoordinates inverted = poly::InversiveCoordinates::inverse(circleToInverse, inversionCircle);
                    poly::Circle circleInverted = inverted.toCircle();
                    circleInverted.setInversionCircle(&cInv);
                    circleInverted.setColor(circlesToInverse[i].color());
                    if (!projected) {
                        circleInverted.setOldCircleBeforeInversion(projectToSphereC(circlesToInverse[i]));
                        circleInverted.setNewCircleAfterInversion(projectToSphereC(circleInverted));
                    } else {
                        circleInverted.setOldCircleBeforeInversion(circlesToInverse[i]);
                        circleInverted.setNewCircleAfterInversion(circleInverted);
                    }
                    res.push_back(circleInverted);
                    count++;
                }
            }
#endif
        }
    }

    circlesToInverse.reserve(circlesToInverse.size() + res.size());
    circlesToInverse.insert(circlesToInverse.end(), res.begin(), res.end());

    //reproject to sphere if needed
    /*if (!projected) {
        for (poly::Circle& cInv: circlesInvertive) {
            projectToSphere(cInv);
        }
        for (std::size_t i = index; i != circlesToInverse.size(); i++) {
            projectToSphere(circlesToInverse[i]);
        }
    }*/

    return count;
}
