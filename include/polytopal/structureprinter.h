#ifndef AUTOFRAC_POLY_STRUCTUREPRINTER_H
#define AUTOFRAC_POLY_STRUCTUREPRINTER_H

#include <string>
#include <vector>

#include "halfedge/mesh.h"
#include "utils/fileprinter.h"

namespace poly {

class Structure;

class Edge;

class Face;

class StructurePrinter {
public:
    StructurePrinter(poly::Structure const& s, bool planarControlPoints, std::string filename);
    void exportStruct();
private:
     void print_header();
     void print_vertex_state();
     void print_bezier_state_decl(unsigned int n);
     void print_bezier_state_impl(unsigned int n);
     void print_init_subds();
     void print_edges_of_cell(poly::Face const& cell);
     void print_subd_of_cell(poly::Face const& cell);
     void print_space_of_cell(poly::Face const& cell);
     void print_prim_of_cell(poly::Face const& cell);
     void print_edge_adjacencies_of_cell(poly::Face const& cell);
     void print_plan_control_points();
     void print_footer();

private:
    poly::Structure const& m_structure;
    bool m_planarControlPoints;
    std::string const m_filename;
    frac::FilePrinter m_filePrinter;
};

} // poly

#endif //AUTOFRAC_POLY_STRUCTUREPRINTER_H
