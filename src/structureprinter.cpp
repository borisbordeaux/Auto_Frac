#include <iostream>
#include "structureprinter.h"

#include "face.h"
#include "structure.h"
#include "fileprinter.h"

void frac::StructurePrinter::exportStruct(const frac::Structure& structure, bool planarControlPoints) {
    StructurePrinter::print_header();
    StructurePrinter::print_vertex_state();
    FilePrinter::append_nl("    ##############################");
    FilePrinter::append_nl("    # all edges states");
    auto edges = structure.allEdges();
    for (auto const& edge: edges.data()) {
        StructurePrinter::print_decl_of_edge(edge);
    }

    FilePrinter::append_nl("    ##############################");
    FilePrinter::append_nl("    # all edges impl");
    for (auto const& edge: edges.data()) {
        StructurePrinter::print_impl_of_edge(edge);
    }

    FilePrinter::append_nl("    ##############################");
    FilePrinter::append_nl("    # all cells states");
    auto cells = structure.allFaces();
    for (auto const& c: cells.data()) {
        FilePrinter::append_nl("    # " + c.toString());
        FilePrinter::append_nl("    " + c.name() + " = Etat('" + c.name() + "', 0)");
    }

    FilePrinter::append_nl("    ##############################");
    FilePrinter::append_nl("    # subd of init");
    StructurePrinter::print_init_subds(structure);

    FilePrinter::append_nl("    ##############################");
    FilePrinter::append_nl("    # edges of all states");
    for (auto const& c: cells.data()) {
        StructurePrinter::print_edges_of_cell(c);
    }

    FilePrinter::append_nl("    ##############################");
    FilePrinter::append_nl("    # subdivisions of all states");
    for (auto const& c: cells.data()) {
        StructurePrinter::print_subd_of_cell(c);
    }

    FilePrinter::append_nl("    ##############################");
    FilePrinter::append_nl("    # build intern of all states");
    for (auto const& c: cells.data()) {
        FilePrinter::append_nl("    " + c.name() + ".buildIntern()");
    }

    FilePrinter::append_nl("    ##############################");
    FilePrinter::append_nl("    # spaces of all states");
    for (auto const& c: cells.data()) {
        StructurePrinter::print_space_of_cell(c);
    }

    FilePrinter::append_nl("    ##############################");
    FilePrinter::append_nl("    # grid of all states");
    for (auto const& c: cells.data()) {
        FilePrinter::append_nl("    " + c.name() + ".addGrid(Bord)");
    }

    FilePrinter::append_nl("    ##############################");
    FilePrinter::append_nl("    # prim of all states");
    for (auto const& c: cells.data()) {
        StructurePrinter::print_prim_of_cell(c);
    }

    FilePrinter::append_nl("    ##############################");
    FilePrinter::append_nl("    # constraints of all states");
    for (auto const& c: cells.data()) {
        FilePrinter::append_nl("    # incidence constraints");
        FilePrinter::append(Face::s_incidenceConstraints[c.name()]);
        FilePrinter::append_nl("    # adjacency constraints");
        if (Face::s_adjacencyConstraints.find(c.name()) != Face::s_adjacencyConstraints.end()) {
            FilePrinter::append(Face::s_adjacencyConstraints[c.name()]);
        }
        FilePrinter::append_nl("    # edges adjacency constraints");
        StructurePrinter::print_edge_adjacencies_of_cell(c);
    }

    FilePrinter::append_nl("    # constraints on init cells");
    FilePrinter::append(structure.adjacencies());

    FilePrinter::append_nl("    # control points");
    if (planarControlPoints) {
        StructurePrinter::print_plan_control_points(structure);
    }
    StructurePrinter::print_init_ctrl_pts_8_bezier();

    StructurePrinter::print_footer();
    FilePrinter::printToFile("result.py");
    std::cout << "Finished, result is in result.py" << std::endl;
}

void frac::StructurePrinter::print_header() {
    FilePrinter::append_nl("from __future__ import division");
    FilePrinter::append_nl("import sys");
    FilePrinter::append_nl("import os");
    FilePrinter::append_nl("");
    FilePrinter::append_nl("directory = os.path.realpath(__file__)");
    FilePrinter::append_nl("directory = directory[:directory.find('InterfaceBCIFS')] + 'python'");
    FilePrinter::append_nl("if directory not in sys.path:");
    FilePrinter::append_nl("    sys.path.append(directory)");
    FilePrinter::append_nl("from etat import *");
    FilePrinter::append_nl("");
    FilePrinter::append_nl("");
    FilePrinter::append_nl("def modele():");
    FilePrinter::append_nl("    init = EtatInit()");
}

void frac::StructurePrinter::print_vertex_state() {
    FilePrinter::append_nl("    s = Etat('s', 1)");
    FilePrinter::append_nl("    s.subs = {Sub('0'): s}");
    FilePrinter::append_nl("    s.buildIntern()");
}

void frac::StructurePrinter::print_decl_of_edge(const frac::Edge& edge) {
    if (edge.edgeType() == EdgeType::CANTOR) {
        if (edge.isDelay()) {
            StructurePrinter::print_delay_cantor_decl(edge.nbSubdivisions(), edge.delay());
        } else {
            StructurePrinter::print_cantor_n_state_decl(edge.nbSubdivisions());
        }
    } else {
        if (edge.isDelay()) {
            StructurePrinter::print_delay_bezier_decl(edge.nbSubdivisions(), edge.delay());
        } else {
            StructurePrinter::print_bezier_state_decl(edge.nbSubdivisions());
        }
    }
}

void frac::StructurePrinter::print_delay_cantor_decl(unsigned int n, unsigned int delay_count) {
    FilePrinter::append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + " = Etat('C" + std::to_string(n) + "_" + std::to_string(delay_count) + "', 0)");
    FilePrinter::append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".bords = {Bord('0'): s, Bord('1'): s}");
    FilePrinter::append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".permuts = {Permut('0'): C" + std::to_string(n) + "_" + std::to_string(delay_count) + "}");
}

void frac::StructurePrinter::print_cantor_n_state_decl(unsigned int n) {
    FilePrinter::append_nl("    C" + std::to_string(n) + " = Etat('C" + std::to_string(n) + "', 0)");
    FilePrinter::append_nl("    C" + std::to_string(n) + ".bords = {Bord('0'): s, Bord('1'): s}");
    FilePrinter::append_nl("    C" + std::to_string(n) + ".permuts = {Permut('0'): C" + std::to_string(n) + "}");
}

void frac::StructurePrinter::print_delay_bezier_decl(unsigned int n, unsigned int delay_count) {
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + " = Etat('B" + std::to_string(n) + "_" + std::to_string(delay_count) + "', 1)");
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".bords = {Bord('0'): s, Bord('1'): s}");
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".permuts = {Permut('0'): B" + std::to_string(n) + "_" + std::to_string(delay_count) + "}");
}

void frac::StructurePrinter::print_bezier_state_decl(unsigned int n) {
    FilePrinter::append_nl("    B" + std::to_string(n) + " = Etat('B" + std::to_string(n) + "', 1)");
    FilePrinter::append_nl("    B" + std::to_string(n) + ".bords = {Bord('0'): s, Bord('1'): s}");
    FilePrinter::append_nl("    B" + std::to_string(n) + ".permuts = {Permut('0'): B" + std::to_string(n) + "}");
}

void frac::StructurePrinter::print_impl_of_edge(const frac::Edge& edge) {
    if (edge.edgeType() == EdgeType::CANTOR) {
        if (edge.isDelay()) {
            StructurePrinter::print_delay_cantor_impl(edge.nbSubdivisions(), edge.delay());
        } else {
            StructurePrinter::print_cantor_n_state_impl(edge.nbSubdivisions());
        }
    } else {
        if (edge.isDelay()) {
            StructurePrinter::print_delay_bezier_impl(edge.nbSubdivisions(), edge.delay());
        } else {
            StructurePrinter::print_bezier_state_impl(edge.nbSubdivisions());
        }
    }
}

void frac::StructurePrinter::print_delay_cantor_impl(unsigned int n, unsigned int delay_count) {
    FilePrinter::append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".subs = {Sub('0'): " + (delay_count > 1 ? "C" + std::to_string(n) + "_" + std::to_string(delay_count - 1) : "C" + std::to_string(n)) + "}");
    FilePrinter::append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".buildIntern()");
    FilePrinter::append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".space = [Bord_('0'), Bord_('1')]");
    FilePrinter::append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Bord('0'), Bord('1'))");
    FilePrinter::append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Bord('1'), Bord('0'))");
    FilePrinter::append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Sub('0'), Sub('0') + Permut('0'))");
    FilePrinter::append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Bord('0') + Sub('0'), Sub('0') + Bord('0'))");
    FilePrinter::append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Bord('1') + Sub('0'), Sub('0') + Bord('1'))");
    FilePrinter::append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".grid.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
    FilePrinter::append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
}

void frac::StructurePrinter::print_cantor_n_state_impl(unsigned int n) {
    FilePrinter::append("    C" + std::to_string(n) + ".subs = {");
    for (int i = 0; i < n - 1; ++i) {
        FilePrinter::append("Sub('" + std::to_string(i) + "'): C" + std::to_string(n) + ", ");
    }
    FilePrinter::append_nl("Sub('" + std::to_string(n - 1) + "'): C" + std::to_string(n) + "}");
    FilePrinter::append_nl("    C" + std::to_string(n) + ".buildIntern()");
    FilePrinter::append_nl("    C" + std::to_string(n) + ".space = [Bord_('0'), Bord_('1')]");
    FilePrinter::append_nl("    C" + std::to_string(n) + "(Permut('0') + Bord('0'), Bord('1'))");
    FilePrinter::append_nl("    C" + std::to_string(n) + "(Permut('0') + Bord('1'), Bord('0'))");
    for (int i = 0; i < n; ++i) {
        FilePrinter::append_nl("    C" + std::to_string(n) + "(Permut('0') + Sub('" + std::to_string(i) + "'), Sub('" + std::to_string(n - i - 1) + "') + Permut('0'))");
    }
    FilePrinter::append_nl("    C" + std::to_string(n) + "(Bord('0') + Sub('0'), Sub('0') + Bord('0'))");
    FilePrinter::append_nl("    C" + std::to_string(n) + "(Bord('1') + Sub('0'), Sub(" + std::to_string(n - 1) + ") + Bord('1'))");
    FilePrinter::append_nl("    C" + std::to_string(n) + ".grid.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
    unsigned int m = n * 2 - 1;
    unsigned int prem = m - 1;
    unsigned int deux = 1;
    FilePrinter::append_nl("    C" + std::to_string(n) + ".initMat[Sub_('0') + Bord('1')] = FMat([");
    FilePrinter::append_nl("        [" + std::to_string(float(prem) / float(m)) + "],");
    FilePrinter::append_nl("        [" + std::to_string(float(deux) / float(m)) + "]]).setTyp('Const')");
    prem = prem - 1;
    deux = deux + 1;
    for (int j = 0; j < n - 2; ++j) {
        FilePrinter::append_nl("    C" + std::to_string(n) + ".initMat[Sub_('" + std::to_string(j + 1) + "')] = FMat([");
        FilePrinter::append_nl("        [" + std::to_string(float(prem) / float(m)) + ", " + std::to_string(float(prem - 1) / float(m)) + "],");
        FilePrinter::append_nl("        [" + std::to_string(float(deux) / float(m)) + ", " + std::to_string(float(deux + 1) / float(m)) + "]]).setTyp('Const')");
        prem = prem - 2;
        deux = deux + 2;
    }
    FilePrinter::append_nl("    C" + std::to_string(n) + ".initMat[Sub_('" + std::to_string(n - 1) + "') + Bord('0')] = FMat([");
    FilePrinter::append_nl("        [" + std::to_string(float(prem) / float(m)) + "],");
    FilePrinter::append_nl("        [" + std::to_string(float(deux) / float(m)) + "]]).setTyp('Const')");
}

void frac::StructurePrinter::print_delay_bezier_impl(unsigned int n, unsigned int delay_count) {
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".subs = {Sub('0'): " + (delay_count > 1 ? "B" + std::to_string(n) + "_" + std::to_string(delay_count - 1) : "B" + std::to_string(n)) + "}");
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".buildIntern()");
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".space = [Bord_('0'), Intern_(''), Bord_('1')]");
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Bord('0'), Bord('1'))");
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Bord('1'), Bord('0'))");
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Intern(''), Intern(''))");
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Sub('0'), Sub('0') + Permut('0'))");
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Bord('0') + Sub('0'), Sub('0') + Bord('0'))");
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Bord('1') + Sub('0'), Sub('0') + Bord('1'))");
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]");
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
    FilePrinter::append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".initMat[Sub_('0') + Intern('')] = FMat([");
    FilePrinter::append_nl("        [0.0],");
    FilePrinter::append_nl("        [1.0],");
    FilePrinter::append_nl("        [0.0]]).setTyp('Const')");
}

void frac::StructurePrinter::print_bezier_state_impl(unsigned int n) {
    FilePrinter::append("    B" + std::to_string(n) + ".subs = {");
    for (int i = 0; i < n - 1; ++i) {
        FilePrinter::append("Sub('" + std::to_string(i) + "'): B" + std::to_string(n) + ", ");
    }
    FilePrinter::append_nl("Sub('" + std::to_string(n - 1) + "'): B" + std::to_string(n) + "}");
    FilePrinter::append_nl("    B" + std::to_string(n) + ".buildIntern()");
    FilePrinter::append_nl("    B" + std::to_string(n) + ".space = [Bord_('0'), Intern_(''), Bord_('1')]");
    FilePrinter::append_nl("    B" + std::to_string(n) + "(Permut('0') + Bord('0'), Bord('1'))");
    FilePrinter::append_nl("    B" + std::to_string(n) + "(Permut('0') + Bord('1'), Bord('0'))");
    FilePrinter::append_nl("    B" + std::to_string(n) + "(Permut('0') + Intern(''), Intern(''))");
    for (int i = 0; i < n; ++i) {
        FilePrinter::append_nl("    B" + std::to_string(n) + "(Permut('0') + Sub(" + std::to_string(i) + "), Sub(" + std::to_string(n - i - 1) + ") + Permut('0'))");
    }
    FilePrinter::append_nl("    B" + std::to_string(n) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]");
    FilePrinter::append_nl("    B" + std::to_string(n) + ".prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
    for (int i = 0; i < n; ++i) {  // for each subdivision T0, T1, ... Tn-1
        FilePrinter::append_nl("    B" + std::to_string(n) + ".initMat[Sub_('" + std::to_string(i) + "')] = FMat([");
        auto t = StructurePrinter::get_bezier_transfo(i, n);
        FilePrinter::append_nl("        [" + std::to_string(t[0]) + ", " + std::to_string(t[1]) + ", " + std::to_string(t[2]) + "],");
        FilePrinter::append_nl("        [" + std::to_string(t[3]) + ", " + std::to_string(t[4]) + ", " + std::to_string(t[5]) + "],");
        FilePrinter::append_nl("        [" + std::to_string(t[6]) + ", " + std::to_string(t[7]) + ", " + std::to_string(t[8]) + "]]).setTyp('Const')");
    }
}

std::vector<float> frac::StructurePrinter::get_bezier_transfo(unsigned int i, unsigned int n) {
    float denominator { static_cast<float>(n * n) };
    return { static_cast<float>(((i - n) * (i - n))) / denominator,
             static_cast<float>(((i - n) * (1. + i - n)) / denominator),
             static_cast<float>(((1. + i - n) * (1. + i - n)) / denominator),
             static_cast<float>((2. * i * (n - i)) / denominator),
             static_cast<float>((n + 2. * i * n - 2. * i * (i + 1.)) / denominator),
             static_cast<float>((-2. * (1. + i - n) * (1. + i)) / denominator),
             static_cast<float>((i * i, i * (1. + i)) / denominator),
             static_cast<float>(((i + 1.) * (i + 1.)) / denominator)
    };
}

void frac::StructurePrinter::print_init_subds(const frac::Structure& structure) {
    auto subds = structure.allFaces();
    FilePrinter::append("    init.subs = {");
    int i = 0;
    for (auto const& s: subds.data()) {
        if (i == 0) {
            FilePrinter::append("Sub('" + std::to_string(i) + "'): " + s.name());
        } else {
            FilePrinter::append(", Sub('" + std::to_string(i) + "'): " + s.name());
        }
        i += 1;
    }
    FilePrinter::append_nl("}");
}

void frac::StructurePrinter::print_edges_of_cell(const frac::Face& cell) {
    FilePrinter::append("    " + cell.name() + ".bords = {");
    int i = 0;
    for (auto const& edge: cell.data()) {
        if (i == 0) {
            FilePrinter::append("Bord('" + std::to_string(i) + "'): " + edge.toString());
        } else {
            FilePrinter::append(", Bord('" + std::to_string(i) + "'): " + edge.toString());
        }
        i += 1;
    }
    FilePrinter::append_nl("}");
}

void frac::StructurePrinter::print_subd_of_cell(const frac::Face& cell) {
    auto subds = cell.subdivisions();
    FilePrinter::append("    " + cell.name() + ".subs = {");
    int i = 0;
    for (auto const& s: subds) {
        if (i == 0) {
            FilePrinter::append("Sub('" + std::to_string(i) + "'): " + s.name());
        } else {
            FilePrinter::append(", Sub('" + std::to_string(i) + "'): " + s.name());
        }
        i += 1;
    }
    FilePrinter::append_nl("}");
}

void frac::StructurePrinter::print_space_of_cell(const frac::Face& cell) {
    FilePrinter::append("    " + cell.name() + ".space = [");
    for (int i = 0; i < cell.len(); ++i) {
        if (i == 0) {
            FilePrinter::append("Bord_('" + std::to_string(i) + "')");
        } else {
            FilePrinter::append(", Bord_('" + std::to_string(i) + "')");
        }
    }
    FilePrinter::append_nl("]");
}

void frac::StructurePrinter::print_prim_of_cell(const frac::Face& cell) {
    FilePrinter::append("    " + cell.name() + ".prim.elems = [Figure(2, [");
    for (int i = 0; i < cell.len(); ++i) {
        if (i == 0) {
            if (cell[i].edgeType() == EdgeType::BEZIER && cell[i].delay() == 0) {
                FilePrinter::append("Bord_('" + std::to_string(i) + "') + Sub('0') + Sub('0') + Bord('0'), Bord_('" + std::to_string(i) + "') + Sub('0') + Sub('1') + Bord('0'), Bord_('" + std::to_string(i) + "') + Sub('1') + Sub('0') + Bord('0'), Bord_('" + std::to_string(i) + "') + Sub('1') + Sub('1') + Bord('0')");
            } else {
                FilePrinter::append("Bord_('" + std::to_string(i) + "') + Bord('0')");
            }
        } else if (cell[i].edgeType() == EdgeType::BEZIER && cell[i].delay() == 0) {
            FilePrinter::append(", Bord_('" + std::to_string(i) + "') + Sub('0') + Sub('0') + Bord('0'), Bord_('" + std::to_string(i) + "') + Sub('0') + Sub('1') + Bord('0'), Bord_('" + std::to_string(i) + "') + Sub('1') + Sub('0') + Bord('0'), Bord_('" + std::to_string(i) + "') + Sub('1') + Sub('1') + Bord('0')");
        } else {
            FilePrinter::append(", Bord_('" + std::to_string(i) + "') + Bord('0')");
        }
    }
    FilePrinter::append_nl("])]");
}

void frac::StructurePrinter::print_edge_adjacencies_of_cell(const frac::Face& cell) {
    for (int i = 0; i < cell.len(); ++i) {
        FilePrinter::append_nl("    " + cell.name() + "(Bord('" + std::to_string(i) + "') + Bord('1'), Bord('" + std::to_string((i + 1) % cell.len()) + "') + Bord('0'))");
    }
}

void frac::StructurePrinter::print_plan_control_points(const frac::Structure& structure) {
    std::size_t max = structure.faces().size();
    for (int index_face = 0; index_face < max; ++index_face) {
        std::size_t nb_pts = structure.nbControlPointsOfFace(index_face);
        FilePrinter::append_nl("    init.initMat[Sub_('" + std::to_string(index_face) + "')] = FMat([");
        for (int j = 0; j < 3; ++j) {
            // x, y, z set to 0
            FilePrinter::append("        [");
            for (int i = 0; i < nb_pts - 1; ++i) {
                FilePrinter::append("0, ");
            }
            FilePrinter::append_nl("0],");
        }
        // w
        FilePrinter::append("        [");
        for (int i = 0; i < nb_pts - 1; ++i) {
            FilePrinter::append("1, ");
        }
        FilePrinter::append_nl("1]]).setTyp('Var')");
        // set z as const
        FilePrinter::append_nl("    for i in range(init.initMat[Sub_('" + std::to_string(index_face) + "')].n):");
        FilePrinter::append_nl("        init.initMat[Sub_('" + std::to_string(index_face) + "')][2, i].setTyp('Const')");
        FilePrinter::append_nl("");
        index_face += 1;
    }
}

void frac::StructurePrinter::print_init_ctrl_pts_8_bezier() {
    FilePrinter::append_nl("    a = 5");
    FilePrinter::append_nl("    b = 10");
    FilePrinter::append_nl("    init.initMat[Sub_('0')] = FMat([");
    FilePrinter::append_nl("        [-a, 0, a, a, b, b, b, a, a, 0,-a,-a,-b,-b,-b,-a],");
    FilePrinter::append_nl("        [ b, b, b, a, a, 0,-a,-a,-b,-b,-b,-a,-a, 0, a, a],");
    FilePrinter::append_nl("        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],");
    FilePrinter::append_nl("        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]).setTyp('Var') # weight of control points");
}

void frac::StructurePrinter::print_footer() {
    FilePrinter::append_nl("    return init");
    FilePrinter::append_nl("");
    FilePrinter::append_nl("");
    FilePrinter::append_nl("if __name__ == '__main__':");
    FilePrinter::append_nl("    print('modele()')");
    FilePrinter::append_nl("    model_init = modele()");
    FilePrinter::append_nl("    print('check()')");
    FilePrinter::append_nl("    model_init.check()");
    FilePrinter::append_nl("    print('solve()')");
    FilePrinter::append_nl("    model_init.solve()");
    FilePrinter::append_nl("    model_init.display()");
    FilePrinter::append_nl("    print('End')");
}
