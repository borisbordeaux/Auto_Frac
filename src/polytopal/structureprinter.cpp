#include "polytopal/structureprinter.h"

#include "halfedge/face.h"
#include "polytopal/face.h"
#include "polytopal/structure.h"
#include "utils/fileprinter.h"
#include "utils/utils.h"


void poly::StructurePrinter::exportStruct() {
    this->print_header();
    this->print_vertex_state();
    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # all edges states");
    auto edges = m_structure.allEdges();
    for (auto const& edge: edges.data()) {
        this->print_bezier_state_decl(edge.nbSubs());
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # all edges impl");
    for (auto const& edge: edges.data()) {
        this->print_bezier_state_impl(edge.nbSubs());
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # all cells states");
    auto cells = m_structure.allFaces();
    for (auto const& c: cells.data()) {
        m_filePrinter.append_nl("    # " + c.toString());
        m_filePrinter.append_nl("    " + c.name() + " = Etat('" + c.name() + "', 0)");
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # subd of init");
    this->print_init_subds();

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # edges of all states");
    for (auto const& c: cells.data()) {
        this->print_edges_of_cell(c);
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # subdivisions of all states");
    for (auto const& c: cells.data()) {
        this->print_subd_of_cell(c);
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # build intern of all states");
    for (auto const& c: cells.data()) {
        m_filePrinter.append_nl("    " + c.name() + ".buildIntern()");
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # spaces of all states");
    for (auto const& c: cells.data()) {
        this->print_space_of_cell(c);
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # grid of all states");
    for (auto const& c: cells.data()) {
        m_filePrinter.append_nl("    " + c.name() + ".addGrid(Bord)");
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # prim of all states");
    for (auto const& c: cells.data()) {
        this->print_prim_of_cell(c);
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # constraints of all states");
    for (auto const& c: cells.data()) {
        m_filePrinter.append_nl("    # incidence constraints");
        m_filePrinter.append(poly::Face::s_incidenceConstraints[c.name()]);
        m_filePrinter.append_nl("    # adjacency constraints");
        if (poly::Face::s_adjacencyConstraints.find(c.name()) != poly::Face::s_adjacencyConstraints.end()) {
            m_filePrinter.append(poly::Face::s_adjacencyConstraints[c.name()]);
        }
        m_filePrinter.append_nl("    # edges adjacency constraints");
        this->print_edge_adjacencies_of_cell(c);
    }

    m_filePrinter.append_nl("    # constraints on init cells");
    m_filePrinter.append(m_structure.adjacencies());

    m_filePrinter.append_nl("    # control points");
    if (m_planarControlPoints) {
        this->print_plan_control_points();
    }

    this->print_footer();
    m_filePrinter.printToFile(m_filename);
}

void poly::StructurePrinter::print_header() {
    m_filePrinter.append_nl("from __future__ import division");
    m_filePrinter.append_nl("import sys");
    m_filePrinter.append_nl("import os");
    m_filePrinter.append_nl("");
    m_filePrinter.append_nl("directory = os.path.realpath(__file__)");
    m_filePrinter.append_nl("directory = directory[:directory.find('InterfaceBCIFS')] + 'python'");
    m_filePrinter.append_nl("if directory not in sys.path:");
    m_filePrinter.append_nl("    sys.path.append(directory)");
    m_filePrinter.append_nl("from etat import *");
    m_filePrinter.append_nl("");
    m_filePrinter.append_nl("");
    m_filePrinter.append_nl("def modele():");
    m_filePrinter.append_nl("    init = EtatInit()");
}

void poly::StructurePrinter::print_vertex_state() {
    m_filePrinter.append_nl("    s = Etat('s', 1)");
    m_filePrinter.append_nl("    s.subs = {Sub('0'): s}");
    m_filePrinter.append_nl("    s.buildIntern()");
}

void poly::StructurePrinter::print_bezier_state_decl(unsigned int n) {
    m_filePrinter.append_nl("    B" + std::to_string(n) + " = Etat('B" + std::to_string(n) + "', 1)");
    m_filePrinter.append_nl("    B" + std::to_string(n) + ".bords = {Bord('0'): s, Bord('1'): s}");
    m_filePrinter.append_nl("    B" + std::to_string(n) + ".permuts = {Permut('0'): B" + std::to_string(n) + "}");
}

void poly::StructurePrinter::print_bezier_state_impl(unsigned int n) {
    m_filePrinter.append("    B" + std::to_string(n) + ".subs = {");
    for (unsigned int i = 0; i < n - 1; ++i) {
        m_filePrinter.append("Sub('" + std::to_string(i) + "'): B" + std::to_string(n) + ", ");
    }
    m_filePrinter.append_nl("Sub('" + std::to_string(n - 1) + "'): B" + std::to_string(n) + "}");
    m_filePrinter.append_nl("    B" + std::to_string(n) + ".buildIntern()");
    m_filePrinter.append_nl("    B" + std::to_string(n) + ".space = [Bord_('0'), Intern_(''), Bord_('1')]");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Bord('0'), Bord('1'))");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Bord('1'), Bord('0'))");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Intern(''), Intern(''))");
    for (unsigned int i = 0; i < n; ++i) {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Sub(" + std::to_string(i) + "), Sub(" + std::to_string(n - i - 1) + ") + Permut('0'))");
    }
    m_filePrinter.append_nl("    B" + std::to_string(n) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]");
    m_filePrinter.append_nl("    B" + std::to_string(n) + ".prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
    for (unsigned int i = 0; i < n; ++i) {  // for each subdivision T0, T1, ... Tn-1
        m_filePrinter.append_nl("    B" + std::to_string(n) + ".initMat[Sub_('" + std::to_string(i) + "')] = FMat([");
        std::vector<float> t = frac::utils::get_bezier_quadratic_transformation(i, n);
        m_filePrinter.append_nl("        [" + frac::utils::to_string(t[0]) + ", " + frac::utils::to_string(t[1]) + ", " + frac::utils::to_string(t[2]) + "],");
        m_filePrinter.append_nl("        [" + frac::utils::to_string(t[3]) + ", " + frac::utils::to_string(t[4]) + ", " + frac::utils::to_string(t[5]) + "],");
        m_filePrinter.append_nl("        [" + frac::utils::to_string(t[6]) + ", " + frac::utils::to_string(t[7]) + ", " + frac::utils::to_string(t[8]) + "]]).setTyp('Const')");
    }
}

void poly::StructurePrinter::print_init_subds() {
    auto const& subds = m_structure.faces();
    m_filePrinter.append("    init.subs = {");
    int i = 0;
    for (auto const& s: subds) {
        if (i == 0) {
            m_filePrinter.append("Sub('" + std::to_string(i) + "'): " + s.name());
        } else {
            m_filePrinter.append(", Sub('" + std::to_string(i) + "'): " + s.name());
        }
        i += 1;
    }
    m_filePrinter.append_nl("}");
}

void poly::StructurePrinter::print_edges_of_cell(poly::Face const& cell) {
    m_filePrinter.append("    " + cell.name() + ".bords = {");
    int i = 0;
    for (auto const& edge: cell.constData()) {
        if (i == 0) {
            m_filePrinter.append("Bord('" + std::to_string(i) + "'): " + edge.name());
        } else {
            m_filePrinter.append(", Bord('" + std::to_string(i) + "'): " + edge.name());
        }
        i += 1;
    }
    m_filePrinter.append_nl("}");
}

void poly::StructurePrinter::print_subd_of_cell(poly::Face const& cell) {
    std::vector<poly::Face> subds = cell.subdivisions();
    m_filePrinter.append("    " + cell.name() + ".subs = {");
    int i = 0;
    for (poly::Face const& f: subds) {
        if (i == 0) {
            m_filePrinter.append("Sub('" + std::to_string(i) + "'): " + f.name());
        } else {
            m_filePrinter.append(", Sub('" + std::to_string(i) + "'): " + f.name());
        }
        i += 1;
    }
    m_filePrinter.append_nl("}");
}

void poly::StructurePrinter::print_space_of_cell(poly::Face const& cell) {
    m_filePrinter.append("    " + cell.name() + ".space = [");
    for (std::size_t i = 0; i < cell.len(); ++i) {
        if (i == 0) {
            m_filePrinter.append("Bord_('" + std::to_string(i) + "')");
        } else {
            m_filePrinter.append(", Bord_('" + std::to_string(i) + "')");
        }
    }
    m_filePrinter.append_nl("]");
}

void poly::StructurePrinter::print_prim_of_cell(poly::Face const& cell) {
    m_filePrinter.append_nl("    " + cell.name() + ".prim.elems = [Figure(2, [");
    for (std::size_t i = 0; i < cell.len(); ++i) {
        for (std::size_t j = 0; j < cell[i].nbSubs(); ++j) {
            if (cell[i].nbSubs() > 2) {
                m_filePrinter.append_nl("        Bord_('" + std::to_string(i) + "') + Sub('" + std::to_string(j) + "') + Bord('0'),");
            } else {
                for (std::size_t k = 0; k < cell[i].nbSubs(); ++k) {
                    m_filePrinter.append_nl("        Bord_('" + std::to_string(i) + "') + Sub('" + std::to_string(j) + "') + Sub('" + std::to_string(k) + "') + Bord('0'),");
                }
            }
        }
    }
    m_filePrinter.append_nl("    ])]");
}

void poly::StructurePrinter::print_edge_adjacencies_of_cell(poly::Face const& cell) {
    for (std::size_t i = 0; i < cell.len(); ++i) {
        m_filePrinter.append_nl("    " + cell.name() + "(Bord('" + std::to_string(i) + "') + Bord('1'), Bord('" + std::to_string(frac::utils::mod(i + 1, cell.len())) + "') + Bord('0'))");
    }
}

void poly::StructurePrinter::print_plan_control_points() {
    std::size_t max = m_structure.faces().size();
    for (std::size_t index_face = 0; index_face < max; ++index_face) {
        std::size_t nb_pts = m_structure.nbControlPointsOfFace(m_structure.faces()[index_face].face()->name().toUInt());
        m_filePrinter.append_nl("    init.initMat[Sub_('" + std::to_string(index_face) + "')] = FMat([");
        for (int j = 0; j < 3; ++j) {
            // x, y, z set to 0
            m_filePrinter.append("        [");
            for (std::size_t i = 0; i < nb_pts - 1; ++i) {
                m_filePrinter.append("0, ");
            }
            m_filePrinter.append_nl("0],");
        }
        // w
        m_filePrinter.append("        [");
        for (std::size_t i = 0; i < nb_pts - 1; ++i) {
            m_filePrinter.append("1, ");
        }
        m_filePrinter.append_nl("1]]).setTyp('Var')");
        // set z as const
        m_filePrinter.append_nl("    for i in range(init.initMat[Sub_('" + std::to_string(index_face) + "')].n):");
        m_filePrinter.append_nl("        init.initMat[Sub_('" + std::to_string(index_face) + "')][2, i].setTyp('Const')");
        m_filePrinter.append_nl("");
    }
}

void poly::StructurePrinter::print_footer() {
    m_filePrinter.append_nl("    return init");
    m_filePrinter.append_nl("");
    m_filePrinter.append_nl("");
    m_filePrinter.append_nl("if __name__ == '__main__':");
    m_filePrinter.append_nl("    print('modele()')");
    m_filePrinter.append_nl("    model_init = modele()");
    m_filePrinter.append_nl("    print('check()')");
    m_filePrinter.append_nl("    model_init.check()");
    m_filePrinter.append_nl("    print('solve()')");
    m_filePrinter.append_nl("    model_init.solve()");
    m_filePrinter.append_nl("    model_init.display()");
    m_filePrinter.append_nl("    print('End')");
}

poly::StructurePrinter::StructurePrinter(poly::Structure const& s, bool planarControlPoints, std::string filename) :
        m_structure(s), m_planarControlPoints(planarControlPoints), m_filename(std::move(filename)) {}
