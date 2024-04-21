#include "persistenthomology/persistenthomology.h"
#include "utils/utils.h"
#include <QString>

#include <gudhi/Rips_complex.h>
#include <gudhi/distance_functions.h>
#include <gudhi/Simplex_tree.h>
#include <gudhi/Persistent_cohomology.h>
#include <gudhi/Persistent_cohomology/Multi_field.h>
#include <gudhi/Points_off_io.h>

// Types definition
using SimplexTree = Gudhi::Simplex_tree<Gudhi::Simplex_tree_options_fast_persistence>;
using RipsComplex = Gudhi::rips_complex::Rips_complex<SimplexTree::Filtration_value>;
using MultiField = Gudhi::persistent_cohomology::Multi_field;
using PersistentCohomology = Gudhi::persistent_cohomology::Persistent_cohomology<SimplexTree, MultiField>;
using Point = std::vector<double>;
using PointsOffReader = Gudhi::Points_off_reader<Point>;

std::vector<frac::PersistentHomology::Cycles> frac::PersistentHomology::computePersistenceHomology(QString const& off_file_points, float r, float minLifeTime, int dimension) {
    PointsOffReader offReader(off_file_points.toStdString());
    RipsComplex ripsComplexFromFile(offReader.get_point_cloud(), r, Gudhi::Euclidean_distance());

    SimplexTree simplexTree;
    ripsComplexFromFile.create_complex(simplexTree, dimension);

    PersistentCohomology persistentCohomology(simplexTree);
    persistentCohomology.init_coefficients(2, 3);
    persistentCohomology.compute_persistent_cohomology(minLifeTime);

    std::vector<Cycles> res;
    std::cout << "end" << std::endl;

    std::stringstream stringStream;
    persistentCohomology.output_diagram(stringStream);

    std::string str;
    std::cout << "Results: " << std::endl;
    while (std::getline(stringStream, str)) {
        // all lines have 5 words
        // first is ignored and second is empty (2 spaces in output diagram)
        // third is dimension, fourth is birth, fifth is death
        std::vector<std::string> words = frac::utils::split(str, ' ');
        std::replace(words[3].begin(), words[3].end(), '.', ',');
        std::replace(words[4].begin(), words[4].end(), '.', ',');

        res.emplace_back(std::stoi(words[2]), std::stof(words[3]), std::stof(words[4]));
        std::cout << str << std::endl;
    }
    std::cout << std::to_string(res.size()) << " points" << std::endl;

    return res;
}
