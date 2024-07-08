#include "halfedge/graphisomorphism.h"

#include <map>
#include <vector>
#include <string>

#include "halfedge/mesh.h"
#include "halfedge/halfedge.h"

namespace {

std::string idToStr(std::size_t ID, std::size_t maxNodes) {
    if (maxNodes < 10) {
        return "," + std::to_string(ID);
    } else {
        return ((ID < 10) ? ",0" : ",") + std::to_string(ID);
    }
}

/**
 * Compute the Euler path beginning by the given halfedge
 * @param he the first halfedge of the path
 * @param clockwise indicates the cycle order of edges
 * @param maxNodes the maximum number of nodes in the graph
 * @return a pair of 2 strings: the first is the topologic code,
 * the second is the code defined by the halfedges types
 */
std::pair<std::string, std::string> computeEulerPathFromHalfEdge(he::HalfEdge* he, bool clockwise, std::size_t maxNodes) {
    //algorithm of the paper "A simple and efficient algorithm for determining isomorphism of planar triply connected graphs, Weinberg"
    std::string resTopo = maxNodes < 10 ? "1" : "01";
    std::string resType = he->userData().toStdString();
    std::map<he::Vertex*, std::size_t> visitedNodesID;
    std::vector<he::HalfEdge*> visitedHalfEdges;
    he::HalfEdge* currentHalfEdge = he;

    //beginning insertions
    visitedNodesID[he->origin()] = visitedNodesID.size() + 1;

    bool end = false;
    while (!end) {
        //find conditions for next halfedge
        bool newNodeReached = visitedNodesID.find(currentHalfEdge->next()->origin()) == visitedNodesID.end();
        bool newVisitedHalfEdge = std::find(visitedHalfEdges.begin(), visitedHalfEdges.end(), currentHalfEdge->twin()) == visitedHalfEdges.end();

        //mark the current halfedge as visited
        visitedHalfEdges.emplace_back(currentHalfEdge);

        //if non already visited node, set its ID (and mark it as visited)
        if (newNodeReached) {
            visitedNodesID[currentHalfEdge->next()->origin()] = visitedNodesID.size() + 1;
        }

        //write the visited node ID in the path
        resTopo += idToStr(visitedNodesID[currentHalfEdge->next()->origin()], maxNodes);
        resType += "," + currentHalfEdge->userData().toStdString();

        //find next halfedge
        if (newNodeReached) {
            //follow on rightmost or leftmost halfedge depending on the rotation order
            currentHalfEdge = clockwise ? currentHalfEdge->twin()->prev()->twin() : currentHalfEdge->next();
        }

        if (!newNodeReached && newVisitedHalfEdge) {
            //go back
            currentHalfEdge = currentHalfEdge->twin();
        }

        if (!newNodeReached && !newVisitedHalfEdge) {
            //go to next right or left halfedge (depending on the rotation order) not previously traversed in that direction
            he::HalfEdge* nextHalfEdge = clockwise ? currentHalfEdge->twin()->prev()->twin() : currentHalfEdge->next();
            while (std::find(visitedHalfEdges.begin(), visitedHalfEdges.end(), nextHalfEdge) != visitedHalfEdges.end() && nextHalfEdge != currentHalfEdge->twin()) {
                nextHalfEdge = clockwise ? nextHalfEdge->prev()->twin() : nextHalfEdge->twin()->next();
            }

            if (nextHalfEdge == currentHalfEdge->twin()) {
                end = true;
            } else {
                currentHalfEdge = nextHalfEdge;
            }
        }
    }

    return { resTopo, resType };
}

std::vector<std::pair<std::string, std::string>> computeEulerPathMatrix(he::Mesh const& mesh) {
    std::vector<std::pair<std::string, std::string>> result;
    for (he::HalfEdge* he: mesh.halfEdges()) {
        //for all halfedges (on both direction), compute clockwise and counterclockwise paths
        result.push_back(computeEulerPathFromHalfEdge(he, true, mesh.vertices().size()));
        result.push_back(computeEulerPathFromHalfEdge(he, false, mesh.vertices().size()));
    }
    return result;
}
}

bool he::GraphComparator::areIsomorph(he::Mesh const& mesh1, he::Mesh const& mesh2, bool compareUserData) {
    std::vector<std::pair<std::string, std::string>> matrix1 = computeEulerPathMatrix(mesh1);
    std::pair<std::string, std::string> code2 = computeEulerPathFromHalfEdge(mesh2.halfEdges()[0], false, mesh2.vertices().size());

    if (compareUserData) {
        return std::find(matrix1.begin(), matrix1.end(), code2) != matrix1.end();
    } else {
        return std::find_if(matrix1.begin(), matrix1.end(), [&code2](auto const& a) { return a.first == code2.first; }) != matrix1.end();
    }
}
