#ifndef AUTOFRAC_POLY_STRUCTUREPRINTER_H
#define AUTOFRAC_POLY_STRUCTUREPRINTER_H

#include <string>
#include <vector>

#include "halfedge/mesh.h"

namespace poly {

class Structure;

class Edge;

class Face;

class StructurePrinter {
public:
    static void exportStruct(poly::Structure const& s, bool planarControlPoints, std::string const& filename);
private:
    static void print_header();
    static void print_vertex_state();
    static void print_bezier_state_decl(unsigned int n);
    static void print_bezier_state_impl(unsigned int n);
    static std::vector<float> get_bezier_transformation(unsigned int i, unsigned int n);
    static void print_init_subds(Structure const& structure);
    static void print_edges_of_cell(poly::Face const& cell);
    static void print_subd_of_cell(poly::Face const& cell);
    static void print_space_of_cell(poly::Face const& cell);
    static void print_prim_of_cell(poly::Face const& cell);
    static void print_edge_adjacencies_of_cell(poly::Face const& cell);
    static void print_plan_control_points(poly::Structure const& structure);
    static void print_footer();
};

} // poly

#endif //AUTOFRAC_POLY_STRUCTUREPRINTER_H
