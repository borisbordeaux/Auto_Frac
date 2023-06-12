#include "polytopal/structureprinter.h"

#include "polytopal/face.h"
#include "polytopal/structure.h"
#include "utils/fileprinter.h"
#include "utils/utils.h"


void poly::StructurePrinter::exportStruct(const poly::Structure& structure, bool planarControlPoints, std::string const& filename) {
    StructurePrinter::print_header();
    StructurePrinter::print_vertex_state();
    frac::FilePrinter::append_nl("    ##############################");
    frac::FilePrinter::append_nl("    # all edges states");
    auto edges = structure.allEdges();
    for (auto const& edge: edges.data()) {
        StructurePrinter::print_bezier_state_decl(edge.nbSubs());
    }

    frac::FilePrinter::append_nl("    ##############################");
    frac::FilePrinter::append_nl("    # all edges impl");
    for (auto const& edge: edges.data()) {
        StructurePrinter::print_bezier_state_impl(edge.nbSubs());
    }

    frac::FilePrinter::append_nl("    ##############################");
    frac::FilePrinter::append_nl("    # all cells states");
    auto cells = structure.allFaces();
    for (auto const& c: cells.data()) {
        frac::FilePrinter::append_nl("    # " + c.toString());
        frac::FilePrinter::append_nl("    " + c.name() + " = Etat('" + c.name() + "', 0)");
    }

    frac::FilePrinter::append_nl("    ##############################");
    frac::FilePrinter::append_nl("    # subd of init");
    StructurePrinter::print_init_subds(structure);

    frac::FilePrinter::append_nl("    ##############################");
    frac::FilePrinter::append_nl("    # edges of all states");
    for (auto const& c: cells.data()) {
        StructurePrinter::print_edges_of_cell(c);
    }

    frac::FilePrinter::append_nl("    ##############################");
    frac::FilePrinter::append_nl("    # subdivisions of all states");
    for (auto const& c: cells.data()) {
        StructurePrinter::print_subd_of_cell(c);
    }

    frac::FilePrinter::append_nl("    ##############################");
    frac::FilePrinter::append_nl("    # build intern of all states");
    for (auto const& c: cells.data()) {
        frac::FilePrinter::append_nl("    " + c.name() + ".buildIntern()");
    }

    frac::FilePrinter::append_nl("    ##############################");
    frac::FilePrinter::append_nl("    # spaces of all states");
    for (auto const& c: cells.data()) {
        StructurePrinter::print_space_of_cell(c);
    }

    frac::FilePrinter::append_nl("    ##############################");
    frac::FilePrinter::append_nl("    # grid of all states");
    for (auto const& c: cells.data()) {
        frac::FilePrinter::append_nl("    " + c.name() + ".addGrid(Bord)");
    }

    frac::FilePrinter::append_nl("    ##############################");
    frac::FilePrinter::append_nl("    # prim of all states");
    for (auto const& c: cells.data()) {
        StructurePrinter::print_prim_of_cell(c);
    }

    frac::FilePrinter::append_nl("    ##############################");
    frac::FilePrinter::append_nl("    # constraints of all states");
    for (auto const& c: cells.data()) {
        frac::FilePrinter::append_nl("    # incidence constraints");
        frac::FilePrinter::append(poly::Face::s_incidenceConstraints[c.name()]);
        frac::FilePrinter::append_nl("    # adjacency constraints");
        if (poly::Face::s_adjacencyConstraints.find(c.name()) != poly::Face::s_adjacencyConstraints.end()) {
            frac::FilePrinter::append(poly::Face::s_adjacencyConstraints[c.name()]);
        }
        frac::FilePrinter::append_nl("    # edges adjacency constraints");
        StructurePrinter::print_edge_adjacencies_of_cell(c);
    }

    frac::FilePrinter::append_nl("    # constraints on init cells");
    frac::FilePrinter::append(structure.adjacencies());

    frac::FilePrinter::append_nl("    # control points");
    if (planarControlPoints) {
        StructurePrinter::print_plan_control_points(structure);
    }

    StructurePrinter::print_footer();
    frac::FilePrinter::printToFile(filename);
}

void poly::StructurePrinter::print_header() {
    frac::FilePrinter::append_nl("from __future__ import division");
    frac::FilePrinter::append_nl("import sys");
    frac::FilePrinter::append_nl("import os");
    frac::FilePrinter::append_nl("");
    frac::FilePrinter::append_nl("directory = os.path.realpath(__file__)");
    frac::FilePrinter::append_nl("directory = directory[:directory.find('InterfaceBCIFS')] + 'python'");
    frac::FilePrinter::append_nl("if directory not in sys.path:");
    frac::FilePrinter::append_nl("    sys.path.append(directory)");
    frac::FilePrinter::append_nl("from etat import *");
    frac::FilePrinter::append_nl("");
    frac::FilePrinter::append_nl("");
    frac::FilePrinter::append_nl("def modele():");
    frac::FilePrinter::append_nl("    init = EtatInit()");
}

void poly::StructurePrinter::print_vertex_state() {
    frac::FilePrinter::append_nl("    s = Etat('s', 1)");
    frac::FilePrinter::append_nl("    s.subs = {Sub('0'): s}");
    frac::FilePrinter::append_nl("    s.buildIntern()");
}

void poly::StructurePrinter::print_bezier_state_decl(unsigned int n) {
    frac::FilePrinter::append_nl("    B" + std::to_string(n) + " = Etat('B" + std::to_string(n) + "', 1)");
    frac::FilePrinter::append_nl("    B" + std::to_string(n) + ".bords = {Bord('0'): s, Bord('1'): s}");
    frac::FilePrinter::append_nl("    B" + std::to_string(n) + ".permuts = {Permut('0'): B" + std::to_string(n) + "}");
}

void poly::StructurePrinter::print_bezier_state_impl(unsigned int n) {
    frac::FilePrinter::append("    B" + std::to_string(n) + ".subs = {");
    for (unsigned int i = 0; i < n - 1; ++i) {
        frac::FilePrinter::append("Sub('" + std::to_string(i) + "'): B" + std::to_string(n) + ", ");
    }
    frac::FilePrinter::append_nl("Sub('" + std::to_string(n - 1) + "'): B" + std::to_string(n) + "}");
    frac::FilePrinter::append_nl("    B" + std::to_string(n) + ".buildIntern()");
    frac::FilePrinter::append_nl("    B" + std::to_string(n) + ".space = [Bord_('0'), Intern_(''), Bord_('1')]");
    frac::FilePrinter::append_nl("    B" + std::to_string(n) + "(Permut('0') + Bord('0'), Bord('1'))");
    frac::FilePrinter::append_nl("    B" + std::to_string(n) + "(Permut('0') + Bord('1'), Bord('0'))");
    frac::FilePrinter::append_nl("    B" + std::to_string(n) + "(Permut('0') + Intern(''), Intern(''))");
    for (unsigned int i = 0; i < n; ++i) {
        frac::FilePrinter::append_nl("    B" + std::to_string(n) + "(Permut('0') + Sub(" + std::to_string(i) + "), Sub(" + std::to_string(n - i - 1) + ") + Permut('0'))");
    }
    frac::FilePrinter::append_nl("    B" + std::to_string(n) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]");
    frac::FilePrinter::append_nl("    B" + std::to_string(n) + ".prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
    for (unsigned int i = 0; i < n; ++i) {  // for each subdivision T0, T1, ... Tn-1
        frac::FilePrinter::append_nl("    B" + std::to_string(n) + ".initMat[Sub_('" + std::to_string(i) + "')] = FMat([");
        std::vector<float> t = StructurePrinter::get_bezier_transformation(i, n);
        frac::FilePrinter::append_nl("        [" + frac::utils::to_string(t[0]) + ", " + frac::utils::to_string(t[1]) + ", " + frac::utils::to_string(t[2]) + "],");
        frac::FilePrinter::append_nl("        [" + frac::utils::to_string(t[3]) + ", " + frac::utils::to_string(t[4]) + ", " + frac::utils::to_string(t[5]) + "],");
        frac::FilePrinter::append_nl("        [" + frac::utils::to_string(t[6]) + ", " + frac::utils::to_string(t[7]) + ", " + frac::utils::to_string(t[8]) + "]]).setTyp('Const')");
    }
}

std::vector<float> poly::StructurePrinter::get_bezier_transformation(unsigned int i, unsigned int n) {
    float denominator { static_cast<float>(n * n) };
    return { static_cast<float>((i - n) * (i - n)) / denominator,
             static_cast<float>((i - n) * (1 + i - n)) / denominator,
             static_cast<float>((1 + i - n) * (1 + i - n)) / denominator,
             static_cast<float>(2 * i * (n - i)) / denominator,
             static_cast<float>(n + 2 * i * n - 2 * i * (i + 1)) / denominator,
             static_cast<float>(-2 * (1 + i - n) * (1 + i)) / denominator,
             static_cast<float>(i * i) / denominator,
             static_cast<float>(i * (1 + i)) / denominator,
             static_cast<float>((i + 1) * (i + 1)) / denominator
    };
}

void poly::StructurePrinter::print_init_subds(const poly::Structure& structure) {
    auto const& subds = structure.faces();
    frac::FilePrinter::append("    init.subs = {");
    int i = 0;
    for (auto const& s: subds) {
        if (i == 0) {
            frac::FilePrinter::append("Sub('" + std::to_string(i) + "'): " + s.name());
        } else {
            frac::FilePrinter::append(", Sub('" + std::to_string(i) + "'): " + s.name());
        }
        i += 1;
    }
    frac::FilePrinter::append_nl("}");
}

void poly::StructurePrinter::print_edges_of_cell(const poly::Face& cell) {
    frac::FilePrinter::append("    " + cell.name() + ".bords = {");
    int i = 0;
    for (auto const& edge: cell.constData()) {
        if (i == 0) {
            frac::FilePrinter::append("Bord('" + std::to_string(i) + "'): " + edge.name());
        } else {
            frac::FilePrinter::append(", Bord('" + std::to_string(i) + "'): " + edge.name());
        }
        i += 1;
    }
    frac::FilePrinter::append_nl("}");
}

void poly::StructurePrinter::print_subd_of_cell(const poly::Face& cell) {
    std::vector<poly::Face> subds = cell.subdivisions();
    frac::FilePrinter::append("    " + cell.name() + ".subs = {");
    int i = 0;
    for (poly::Face const& f: subds) {
        if (i == 0) {
            frac::FilePrinter::append("Sub('" + std::to_string(i) + "'): " + f.name());
        } else {
            frac::FilePrinter::append(", Sub('" + std::to_string(i) + "'): " + f.name());
        }
        i += 1;
    }
    frac::FilePrinter::append_nl("}");
}

void poly::StructurePrinter::print_space_of_cell(const poly::Face& cell) {
    frac::FilePrinter::append("    " + cell.name() + ".space = [");
    for (std::size_t i = 0; i < cell.len(); ++i) {
        if (i == 0) {
            frac::FilePrinter::append("Bord_('" + std::to_string(i) + "')");
        } else {
            frac::FilePrinter::append(", Bord_('" + std::to_string(i) + "')");
        }
    }
    frac::FilePrinter::append_nl("]");
}

void poly::StructurePrinter::print_prim_of_cell(const poly::Face& cell) {
    frac::FilePrinter::append("    " + cell.name() + ".prim.elems = [Figure(2, [");
    for (std::size_t i = 0; i < cell.len(); ++i) {
        if (i == 0) {
            frac::FilePrinter::append("Bord_('" + std::to_string(i) + "') + Sub('0') + Sub('0') + Bord('0'), Bord_('" + std::to_string(i) + "') + Sub('0') + Sub('1') + Bord('0'), Bord_('" + std::to_string(i) + "') + Sub('1') + Sub('0') + Bord('0'), Bord_('" + std::to_string(i) + "') + Sub('1') + Sub('1') + Bord('0')");
        } else {
            frac::FilePrinter::append(", Bord_('" + std::to_string(i) + "') + Sub('0') + Sub('0') + Bord('0'), Bord_('" + std::to_string(i) + "') + Sub('0') + Sub('1') + Bord('0'), Bord_('" + std::to_string(i) + "') + Sub('1') + Sub('0') + Bord('0'), Bord_('" + std::to_string(i) + "') + Sub('1') + Sub('1') + Bord('0')");
        }
    }
    frac::FilePrinter::append_nl("])]");
}

void poly::StructurePrinter::print_edge_adjacencies_of_cell(const poly::Face& cell) {
    for (std::size_t i = 0; i < cell.len(); ++i) {
        frac::FilePrinter::append_nl("    " + cell.name() + "(Bord('" + std::to_string(i) + "') + Bord('1'), Bord('" + std::to_string(frac::utils::mod(i + 1, cell.len())) + "') + Bord('0'))");
    }
}

void poly::StructurePrinter::print_plan_control_points(const poly::Structure& structure) {
    std::size_t max = structure.faces().size();
    for (std::size_t index_face = 0; index_face < max; ++index_face) {
        std::size_t nb_pts = structure.nbControlPointsOfFace(index_face);
        frac::FilePrinter::append_nl("    init.initMat[Sub_('" + std::to_string(index_face) + "')] = FMat([");
        for (int j = 0; j < 3; ++j) {
            // x, y, z set to 0
            frac::FilePrinter::append("        [");
            for (std::size_t i = 0; i < nb_pts - 1; ++i) {
                frac::FilePrinter::append("0, ");
            }
            frac::FilePrinter::append_nl("0],");
        }
        // w
        frac::FilePrinter::append("        [");
        for (std::size_t i = 0; i < nb_pts - 1; ++i) {
            frac::FilePrinter::append("1, ");
        }
        frac::FilePrinter::append_nl("1]]).setTyp('Var')");
        // set z as const
        frac::FilePrinter::append_nl("    for i in range(init.initMat[Sub_('" + std::to_string(index_face) + "')].n):");
        frac::FilePrinter::append_nl("        init.initMat[Sub_('" + std::to_string(index_face) + "')][2, i].setTyp('Const')");
        frac::FilePrinter::append_nl("");
        index_face += 1;
    }
}

void poly::StructurePrinter::print_footer() {
    frac::FilePrinter::append_nl("    return init");
    frac::FilePrinter::append_nl("");
    frac::FilePrinter::append_nl("");
    frac::FilePrinter::append_nl("if __name__ == '__main__':");
    frac::FilePrinter::append_nl("    print('modele()')");
    frac::FilePrinter::append_nl("    model_init = modele()");
    frac::FilePrinter::append_nl("    print('check()')");
    frac::FilePrinter::append_nl("    model_init.check()");
    frac::FilePrinter::append_nl("    print('solve()')");
    frac::FilePrinter::append_nl("    model_init.solve()");
    frac::FilePrinter::append_nl("    model_init.display()");
    frac::FilePrinter::append_nl("    print('End')");
}
