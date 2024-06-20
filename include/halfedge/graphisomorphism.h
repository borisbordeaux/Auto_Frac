#ifndef AUTOFRAC_GRAPHISOMORPHISM_H
#define AUTOFRAC_GRAPHISOMORPHISM_H

namespace he {
class Mesh;

class HalfEdge;

namespace GraphComparator {
bool areIsomorph(he::Mesh const& mesh1, he::Mesh const& mesh2, bool compareNamesOfHalfEdges = false);
}

}

#endif //AUTOFRAC_GRAPHISOMORPHISM_H
