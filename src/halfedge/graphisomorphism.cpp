#include "halfedge/graphisomorphism.h"

#include <map>
#include <vector>
#include <string>

#include "halfedge/mesh.h"
#include "halfedge/halfedge.h"

namespace {
std::string computePathFromHalfEdge(he::HalfEdge* he) {
    std::string res;
    std::map<he::Vertex*, int> visitedNodesID;
    std::vector<he::HalfEdge*> visitedHalfEdges;

    visitedHalfEdges.emplace_back(he);

    //TODO: implement algorithm of the paper "A simple and efficient algorithm for determining isomorphism of planar triply connected graphs, Weinberg"

    return res;
}

std::vector<std::string> computePathMatrix(const he::Mesh& mesh) {
    std::vector<std::string> result;
    for (he::HalfEdge* he: mesh.halfEdges()) {
        //for all halfedges, on both direction
        result.push_back(computePathFromHalfEdge(he));
    }
    std::sort(result.begin(), result.end());
    return result;
}
}

bool he::GraphComparator::areIsomorph(he::Mesh const& mesh1, he::Mesh const& mesh2) {
    std::vector<std::string> matrix1 = computePathMatrix(mesh1);
    std::vector<std::string> matrix2 = computePathMatrix(mesh2);

    if (matrix1.size() != matrix2.size() || matrix1.empty() || matrix2.empty()) {
        return false;
    }

    return matrix1.at(0) == matrix2.at(0);
}


