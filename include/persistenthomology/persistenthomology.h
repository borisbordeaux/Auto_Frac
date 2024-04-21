#ifndef AUTOFRAC_PERSISTENTHOMOLOGY_H
#define AUTOFRAC_PERSISTENTHOMOLOGY_H

#include <vector>

class QString;

namespace frac::PersistentHomology {

struct Cycles {
    int Dim;
    float Birth;
    float Death;

    Cycles(int dim, float birth, float death) : Dim(dim), Birth(birth), Death(death) {}
};

std::vector<Cycles> computePersistenceHomology(QString const& off_file_points, float r, float minLifeTime, int dimension);

}

#endif //AUTOFRAC_PERSISTENTHOMOLOGY_H
