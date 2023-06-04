#ifndef AUTOFRAC_STRUCTUREPRINTER_H
#define AUTOFRAC_STRUCTUREPRINTER_H

#include <vector>

namespace frac {

class Structure;

class Face;

class Edge;

class StructurePrinter {
public:
    static void exportStruct(Structure const& s, bool planarControlPoints, std::string const& filename);
private:
    static void print_header();
    static void print_vertex_state();
    static void print_decl_of_edge(Edge const& edge);
    static void print_delay_cantor_decl(unsigned int n, unsigned int delay_count);
    static void print_cantor_n_state_decl(unsigned int n);
    static void print_delay_bezier_decl(unsigned int n, unsigned int delay_count);
    static void print_bezier_state_decl(unsigned int n);
    static void print_impl_of_edge(Edge const& edge);
    static void print_delay_cantor_impl(unsigned int n, unsigned int delay_count);
    static void print_cantor_n_state_impl(unsigned int n);
    static void print_delay_bezier_impl(unsigned int n, unsigned int delay_count);
    static void print_bezier_state_impl(unsigned int n);
    static std::vector<float> get_bezier_transformation(unsigned int i, unsigned int n);
    static void print_init_subds(Structure const& structure);
    static void print_edges_of_cell(Face const& cell);
    static void print_subd_of_cell(Face const& cell);
    static void print_space_of_cell(Face const& cell);
    static void print_prim_of_cell(Face const& cell);
    static void print_edge_adjacencies_of_cell(Face const& cell);
    static void print_plan_control_points(Structure const& structure);
    static void print_init_ctrl_pts_8_bezier();
    static void print_footer();
};
}
#endif //AUTOFRAC_STRUCTUREPRINTER_H
