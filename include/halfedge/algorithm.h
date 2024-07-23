#ifndef AUTOFRAC_ALGORITHM_H
#define AUTOFRAC_ALGORITHM_H

namespace he {
class Mesh;

namespace algo {

void barycentricSubdivision(he::Mesh& mesh);

void generalizedBarycentricSubdivision(he::Mesh& mesh, int nbSubsCornerEdges = 2, int nbSubsEdgeEdges = 2);

void loopSubdivision(he::Mesh& mesh);

}
}

#endif //AUTOFRAC_ALGORITHM_H
