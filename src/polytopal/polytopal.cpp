#include "polytopal/polytopal.h"

#include <QHash>
#include <QColor>
#include "halfedge/mesh.h"
#include "halfedge/vertex.h"
#include "halfedge/halfedge.h"
#include "halfedge/face.h"
#include "utils/utils.h"

namespace {

he::Point3D closestPoint(he::Point3D const& p1, he::Point3D const& p2) {
    he::Point3D u = p2 - p1;
    u.normalize();
    he::Point3D ba = -p1;

    he::Point3D BH = u * he::Point3D::dotProduct(ba, u);
    return p1 + BH;
}

QVector3D closestPoint(QVector3D const& p1, QVector3D const& p2) {
    QVector3D u = p2 - p1;
    u.normalize();
    QVector3D ba = -p1;

    QVector3D BH = u * QVector3D::dotProduct(ba, u);
    return p1 + BH;
}

he::Point3D barycenter(std::vector<he::Point3D> const& positions) {
    he::Point3D res { 0, 0, 0 };
    for (he::Point3D const& p: positions) {
        res += p;
    }
    res /= static_cast<double>(positions.size());
    return res;
}

he::Point3D barycenter(std::vector<he::Vertex*> const& positions) {
    he::Point3D res { 0, 0, 0 };
    for (he::Vertex* v: positions) {
        res += v->posD();
    }
    res /= static_cast<double>(positions.size());
    return res;
}

he::Point3D approxNormal(std::vector<he::Vertex*> const& vertices) {
    he::Point3D n { 0, 0, 0 };
    int s = static_cast<int>(vertices.size());
    for (int i = 0; i < s; i++) {
        he::Point3D cur = vertices[i]->posD();
        he::Point3D nxt = vertices[frac::utils::mod(i + 1, s)]->posD();
        he::Point3D prv = vertices[frac::utils::mod(i - 1, s)]->posD();
        he::Point3D x = nxt - cur;
        he::Point3D y = prv - cur;
        n += he::Point3D::crossProduct(x, y);
    }
    n /= static_cast<double>(s);
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
        he::Point3D A = barycenter(vertices);
        //approx normal of the plan
        he::Point3D n = approxNormal(vertices);
        //plan equation
        double a = n.x();
        double b = n.y();
        double c = n.z();
        double d = -n.x() * A.x() - n.y() * A.y() - n.z() * A.z();
        //projection of all points on the plan
        for (he::Vertex* v: vertices) {
            double lambda = (a * v->posD().x() + b * v->posD().y() + c * v->posD().z() + d) / (a * a + b * b + c * c);
            v->setPosD(v->posD() - n * lambda * 0.1);
        }
    }
}

void planarize(he::Mesh& m) {
    for (he::Face* f: m.faces()) {
        if (f->nbEdges() > 3) {
            planarize(f);
        }
    }
}

void tangentify(he::Mesh& m) {
    std::vector<he::HalfEdge*> alreadyTreated;
    QHash<he::Vertex*, he::Point3D> transforms;

    for (he::HalfEdge* he: m.halfEdges()) {
        if (std::find(alreadyTreated.begin(), alreadyTreated.end(), he) == alreadyTreated.end()) {
            he::Vertex* p1 = he->origin();
            he::Vertex* p2 = he->next()->origin();
            he::Point3D closest = closestPoint(p1->posD(), p2->posD());

            // difference between the closest point and the sphere
            double l = 1.0 - closest.length();
            he::Point3D c = closest * l * 0.1;

            if (!transforms.contains(p1)) {
                transforms[p1] = p1->posD();
            }
            if (!transforms.contains(p2)) {
                transforms[p2] = p2->posD();
            }

            transforms[p1] = transforms[p1] + c;
            transforms[p2] = transforms[p2] + c;

            alreadyTreated.push_back(he->twin());
        }
    }

    for (std::pair<he::Vertex*, he::Point3D> p: transforms.asKeyValueRange()) {
        p.first->setPosD(p.second);
    }
}

void recenter(he::Mesh& m) {
    std::vector<he::HalfEdge*> alreadyTreated;
    std::vector<he::Point3D> positions;
    for (he::HalfEdge* he: m.halfEdges()) {
        if (std::find(alreadyTreated.begin(), alreadyTreated.end(), he) == alreadyTreated.end()) {
            positions.push_back(closestPoint(he->origin()->posD(), he->next()->origin()->posD()));
            alreadyTreated.push_back(he->twin());
        }
    }
    he::Point3D bary = barycenter(positions);
    for (he::Vertex* v: m.vertices()) {
        v->setPosD(v->posD() - bary);
    }
}

void projectToPlan(QVector3D& point) {
    point.setX(point.x() / (1.0f - point.z()));
    point.setY(point.y() / (1.0f - point.z()));
    point.setZ(0.0f);
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

} //end anonymous namespace for local functions


void poly::setMeshToOrigin(he::Mesh& m) {
    std::vector<he::Point3D> positions;

    for (he::Vertex* v: m.vertices()) {
        positions.push_back(v->posD());
    }

    he::Point3D bary = barycenter(positions);

    for (he::Vertex* v: m.vertices()) {
        v->setPosD(v->posD() - bary);
    }
}

void poly::canonicalizeMesh(he::Mesh& m) {
    tangentify(m);
    recenter(m);
    planarize(m);
    m.updateFloatPosFromDoublePos();
}

std::vector<poly::Circle> poly::computeIlluminatedCircles(const he::Mesh& m) {
    std::vector<poly::Circle> res;

    int colorIndex = 15;

    for (he::Vertex* v: m.vertices()) {
#if 0
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
        }
#else
        float coef = 1.0f / qSqrt(v->pos().lengthSquared() - 1.0f);
        poly::Circle c { coef * v->pos().x(), coef * v->pos().y(), coef * v->pos().z(), coef };
#endif
        c.setColor({ colors[colorIndex % 16].redF(), colors[colorIndex % 16].greenF(), colors[colorIndex % 16].blueF() });
        res.push_back(c);
        //colorIndex++;
    }

    return res;
}

std::vector<poly::Circle> poly::computeIlluminatedCirclesDual(he::Mesh const& m) {
    std::vector<poly::Circle> res;
    int colorIndex = 15;

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
            c.setColor({ colors[colorIndex % 16].redF(), colors[colorIndex % 16].greenF(), colors[colorIndex % 16].blueF() });
            res.push_back(c);
        }
    }

    return res;
}

std::size_t poly::computeInversions(std::vector<poly::Circle>& circlesToInverse, std::vector<poly::Circle>& circlesInvertive, std::size_t index) {
    std::vector<poly::Circle> res;
    res.reserve((circlesToInverse.size() - index) * circlesInvertive.size());
    std::size_t count = 0;

    //inversion always in plan using inversive coordinates
    for (std::size_t i = index; i != circlesToInverse.size(); i++) {
        for (poly::Circle const& cInv: circlesInvertive) {
            float precision = 0.003f;
            if (circlesToInverse[i].inversionCircle() != &cInv && !poly::Circle::areOrthogonalCircles(circlesToInverse[i], cInv)) {
                if (circlesToInverse[i].radius() > precision) {
                    poly::Circle inverted = poly::Circle::inverse(circlesToInverse[i], cInv);
                    inverted.setInversionCircle(&cInv);
                    inverted.updateR3Coord();
                    //for animations
                    inverted.setOldCircleBeforeInversion(circlesToInverse[i]);
                    inverted.setNewCircleAfterInversion(inverted);
                    res.push_back(inverted);
                    count++;
                }
            }
        }
    }

    circlesToInverse.reserve(circlesToInverse.size() + res.size());
    circlesToInverse.insert(circlesToInverse.end(), res.begin(), res.end());

    return count;
}