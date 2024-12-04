#include "polytopal/polytopal.h"

#include <QHash>
#include "halfedge/mesh.h"
#include "halfedge/vertex.h"
#include "halfedge/halfedge.h"
#include "halfedge/face.h"
#include "gui/circle.h"
#include "utils/utils.h"

namespace {

he::Point3D closestPoint(he::Point3D const& B, he::Point3D const& C) {
    he::Point3D A(0, 0, 0);
    he::Point3D u = B - C;
    u.normalize();
    he::Point3D H = B + u * he::Point3D::dotProduct((A - B), u);
    he::Point3D BH = H - B;
    he::Point3D CH = H - C;
    he::Point3D BC = C - B;
    if (BH.lengthSquared() < BC.lengthSquared() && CH.lengthSquared() < BC.lengthSquared()) {
        return B + BH;
    } else if (CH.lengthSquared() > BC.lengthSquared()) {
        return B;
    } else {
        return C;
    }
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

void tangentify(he::Mesh& m, double d) {
    QHash<he::Vertex*, he::Point3D> transforms;

    for (he::HalfEdge* he: m.halfEdgesNoTwin()) {
        he::Vertex* p1 = he->origin();
        he::Vertex* p2 = he->next()->origin();
        he::Point3D closest = closestPoint(p1->posD(), p2->posD());

        // difference between the closest point and the sphere
        double l = 1.0 - closest.length();
        he::Point3D c = closest * l * d;

        if (!transforms.contains(p1)) {
            transforms[p1] = p1->posD();
        }
        if (!transforms.contains(p2)) {
            transforms[p2] = p2->posD();
        }

        transforms[p1] = transforms[p1] + c;
        transforms[p2] = transforms[p2] + c;
    }

    for (std::pair<he::Vertex*, he::Point3D> p: transforms.asKeyValueRange()) {
        p.first->setPosD(p.second);
    }
}

void recenter(he::Mesh& m) {
    he::Point3D barycenter { 0, 0, 0 };
    for (he::HalfEdge* he: m.halfEdgesNoTwin()) {
        barycenter += closestPoint(he->origin()->posD(), he->next()->origin()->posD());
    }
    barycenter /= static_cast<double>(m.halfEdgesNoTwin().size());

    for (he::Vertex* v: m.vertices()) {
        v->setPosD(v->posD() - barycenter);
    }
}
} //end anonymous namespace for local functions

void poly::canonicalizeMesh(he::Mesh& m, int steps, double d, bool recenterMesh) {
    for (int i = 0; i < steps; i++) {
        tangentify(m, d);
        if (recenterMesh) { recenter(m); }
        planarize(m);
    }
    m.updateFloatPosFromDoublePos();
}

std::vector<poly::InversiveCoordinates> poly::computeIlluminatedCircles(const he::Mesh& m) {
    std::vector<poly::InversiveCoordinates> res;
    for (he::Vertex* v: m.vertices()) {
        poly::InversiveCoordinates c { v->posD() };
        res.push_back(c);
    }
    return res;
}

std::vector<poly::InversiveCoordinates> poly::computeIlluminatedCirclesDual(he::Mesh const& m) {
    std::vector<poly::InversiveCoordinates> res;

    for (he::Face* f: m.faces()) {
        res.emplace_back(f->computePolar());
    }

    return res;
}

std::size_t poly::computeInversions(std::vector<poly::InversiveCoordinates>& circlesToInverse, std::vector<poly::InversiveCoordinates>& circlesInvertive, std::size_t index) {
    std::vector<poly::InversiveCoordinates> res;
    res.reserve((circlesToInverse.size() - index) * circlesInvertive.size());
    std::size_t count = 0;

    //inversion always in plan using inversive coordinates
    for (std::size_t i = index; i != circlesToInverse.size(); i++) {
        for (poly::InversiveCoordinates const& cInv: circlesInvertive) {
            if (circlesToInverse[i].inverter() != &cInv && !poly::InversiveCoordinates::areOrthogonal(circlesToInverse[i], cInv)) {
                poly::InversiveCoordinates inverted = poly::InversiveCoordinates::inverse(circlesToInverse[i], cInv);
                inverted.setInverter(&cInv);
                res.push_back(inverted);
                count++;
            }
        }
    }

    circlesToInverse.reserve(circlesToInverse.size() + res.size());
    circlesToInverse.insert(circlesToInverse.end(), res.begin(), res.end());

    return count;
}