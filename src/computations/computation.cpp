#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include "computations/computation.h"
#include "utils/measures.h"
#include <QString>
#include <QHash>
#include <QDebug>

#include "halfedge/mesh.h"
#include "halfedge/vertex.h"
#include "halfedge/halfedge.h"
#include "halfedge/face.h"
#include "utils/utils.h"

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

void project(QVector3D& point) {
    point.setX(point.x() / (1.0f - point.z()));
    point.setY(point.y() / (1.0f - point.z()));
    point.setZ(0.0f);
}

QVector3D inversion(QVector3D const& point, poly::Circle const& circleInv) {
    QVector3D OA = point - circleInv.center();
    QVector3D OB = OA.normalized() * (circleInv.radius() * circleInv.radius() / OA.length());
    return circleInv.center() + OB;
}

poly::Circle inversion(poly::Circle const& circleToInv, poly::Circle const& circleInv) {
    QVector3D p1 = circleToInv.center();
    p1.setX(p1.x() + circleToInv.radius());

    QVector3D p2 = circleToInv.center();
    p2.setY(p2.y() + circleToInv.radius());

    QVector3D p3 = circleToInv.center();
    p3.setX(p3.x() - circleToInv.radius());

    QVector3D p1Inv = inversion(p1, circleInv);
    QVector3D p2Inv = inversion(p2, circleInv);
    QVector3D p3Inv = inversion(p3, circleInv);
    return { p1Inv, p2Inv, p3Inv };
}

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

std::vector<poly::Circle> frac::PolyCircle::computeIlluminatedCircles(const he::Mesh& m, bool projected) {
    std::vector<poly::Circle> res;

    for (he::Vertex* v: m.vertices()) {
        QList<he::HalfEdge*> otherHE = v->otherHalfEdges();
        if (otherHE.size() > 1) {
            QVector3D v1 = closestPoint(v->pos(), v->halfEdge()->next()->origin()->pos());
            QVector3D v2 = closestPoint(otherHE[0]->origin()->pos(), otherHE[0]->next()->origin()->pos());
            QVector3D v3 = closestPoint(otherHE[1]->origin()->pos(), otherHE[1]->next()->origin()->pos());

            if (projected) {
                project(v1);
                project(v2);
                project(v3);
            }

            res.emplace_back(v1, v2, v3);
        }
    }

    return res;
}

std::vector<poly::Circle> frac::PolyCircle::computeIlluminatedCirclesDual(he::Mesh const& m, bool projected) {
    std::vector<poly::Circle> res;

    for (he::Face* f: m.faces()) {
        std::vector<he::HalfEdge*> allHE = f->allHalfEdges();
        if (allHE.size() > 2) {
            QVector3D v1 = closestPoint(allHE[0]->origin()->pos(), allHE[0]->next()->origin()->pos());
            QVector3D v2 = closestPoint(allHE[1]->origin()->pos(), allHE[1]->next()->origin()->pos());
            QVector3D v3 = closestPoint(allHE[2]->origin()->pos(), allHE[2]->next()->origin()->pos());

            if (projected) {
                project(v1);
                project(v2);
                project(v3);
            }

            res.emplace_back(v1, v2, v3);
        }
    }

    return res;
}

void frac::PolyCircle::computeInversions(std::vector<poly::Circle>& circlesToInverse, std::vector<poly::Circle>& circlesInvertive) {
    std::vector<poly::Circle> res;
    res.reserve(circlesToInverse.size() * circlesInvertive.size());
    for (poly::Circle const& cToInv: circlesToInverse) {
        for (poly::Circle const& cInv: circlesInvertive) {
            //TODO: check if the circle is orthogonal to the invertion circle, since it will remain the same, we have to avoid the computation
            res.push_back(inversion(cToInv, cInv));
        }
    }
    circlesToInverse.insert(circlesToInverse.end(), res.begin(), res.end());
}
