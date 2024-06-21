#ifndef AUTOFRAC_STRUCTURE3DPRINTER_H
#define AUTOFRAC_STRUCTURE3DPRINTER_H

#include "structure3d.h"
#include "utils/fileprinter.h"

namespace frac {

class Structure3DPrinter {
public:
    Structure3DPrinter(frac::Structure3D const& structure, std::string filename);
    void exportStruct();
private:
    void print_header();
    void print_vertex_state();
    void print_decl_of_edge(frac::Edge const& edge);
    void print_delay_cantor_decl(unsigned int n, unsigned int delay_count);
    void print_cantor_n_state_decl(unsigned int n);
    void print_delay_bezier_decl(unsigned int n, unsigned int delay_count);
    void print_bezier_state_decl(unsigned int n);
    void print_impl_of_edge(frac::Edge const& edge);
    void print_delay_cantor_impl(unsigned int n, unsigned int delay_count);
    void print_cantor_n_state_impl(unsigned int n);
    void print_delay_bezier_impl(unsigned int n, unsigned int delay_count);
    void print_bezier_state_impl(unsigned int n);
    void print_init_subds();
    void print_edges_of_face(frac::Face const& face);
    void print_subd_of_face(frac::Face const& face);
    void print_space_of_face(frac::Face const& face);
    void print_edge_adjacencies_of_face(frac::Face const& face);
    void print_edges_of_volume(frac::Volume const& volume);
    void print_subd_of_volume(frac::Volume const& volume);
    void print_space_of_volume(frac::Volume const& volume);
    void print_prim_of_volume(frac::Volume const& volume);
    void print_edge_adjacencies_of_volume(frac::Volume const& volume);
    void print_footer();

private:
    frac::Structure3D const& m_structure;
    std::string const m_filename;
    frac::FilePrinter m_filePrinter;
};

} // frac

#endif //AUTOFRAC_STRUCTURE3DPRINTER_H
