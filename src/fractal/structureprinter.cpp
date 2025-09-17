#include "fractal/structureprinter.h"

#include "fractal/face.h"
#include "fractal/structure.h"
#include "utils/utils.h"
#include "utils/point2d.h"
#include "massspringsystem/massspringsystem.h"

frac::StructurePrinter::StructurePrinter(frac::Structure const& structure, bool planarControlPoints, std::string filename, std::vector<std::vector<Point2D>> const& coords) :
        m_structure(structure), m_planarControlPoints(planarControlPoints), m_filename(std::move(filename)), m_coords(coords) {}

void frac::StructurePrinter::exportStruct() {
    m_filePrinter.reset();
    this->print_header();
    this->print_vertex_state();
    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # all edges states");
    auto edges = m_structure.allEdges();
    for (auto const& edge: edges.data()) {
        this->print_decl_of_edge(edge);
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # all edges impl");
    for (auto const& edge: edges.data()) {
        this->print_impl_of_edge(edge);
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
        m_filePrinter.append(Face::s_incidenceConstraints[c.name()]);
        m_filePrinter.append_nl("    # adjacency constraints");
        if (Face::s_adjacencyConstraints.find(c.name()) != Face::s_adjacencyConstraints.end()) {
            m_filePrinter.append(Face::s_adjacencyConstraints[c.name()]);
        }
        m_filePrinter.append_nl("    # edges adjacency constraints");
        this->print_edge_adjacencies_of_cell(c);
    }

    m_filePrinter.append_nl("    # constraints on init cells");
    m_filePrinter.append(m_structure.strAdjacencies());

    m_filePrinter.append_nl("    # control points");
    if (m_planarControlPoints) {
        if (m_coords.empty()) {
            this->print_plan_control_points();
        } else {
            this->print_plan_coords_control_points();
        }
    }

    this->print_footer();
    m_filePrinter.printToFile(m_filename);
}

void frac::StructurePrinter::print_header() {
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

void frac::StructurePrinter::print_vertex_state() {
    m_filePrinter.append_nl("    s = Etat('s', 1)");
    m_filePrinter.append_nl("    s.subs = {Sub('0'): s}");
    m_filePrinter.append_nl("    s.buildIntern()");
}

void frac::StructurePrinter::print_decl_of_edge(const frac::Edge& edge) {
    if (edge.edgeType() == EdgeType::CANTOR) {
        if (edge.isDelay()) {
            this->print_delay_cantor_decl(edge.nbSubdivisions(), edge.delay());
        } else {
            this->print_cantor_n_state_decl(edge.nbSubdivisions());
        }
    } else {
        if (edge.isDelay()) {
            this->print_delay_bezier_decl(edge.nbSubdivisions(), edge.delay());
        } else {
            this->print_bezier_state_decl(edge.nbSubdivisions());
        }
    }
}

void frac::StructurePrinter::print_delay_cantor_decl(unsigned int n, unsigned int delay_count) {
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + " = Etat('C" + std::to_string(n) + "_" + std::to_string(delay_count) + "', " + (m_structure.cantorType() == CantorType::Cubic_Cantor ? "2" : (m_structure.cantorType() == CantorType::Quadratic_Cantor ? "1" : "0")) + ")");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".bords = {Bord('0'): s, Bord('1'): s}");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".permuts = {Permut('0'): C" + std::to_string(n) + "_" + std::to_string(delay_count) + "}");
}

void frac::StructurePrinter::print_cantor_n_state_decl(unsigned int n) {
    m_filePrinter.append_nl("    C" + std::to_string(n) + " = Etat('C" + std::to_string(n) + "', " + (m_structure.cantorType() == CantorType::Cubic_Cantor ? "2" : (m_structure.cantorType() == CantorType::Quadratic_Cantor ? "1" : "0")) + ")");
    m_filePrinter.append_nl("    C" + std::to_string(n) + ".bords = {Bord('0'): s, Bord('1'): s}");
    m_filePrinter.append_nl("    C" + std::to_string(n) + ".permuts = {Permut('0'): C" + std::to_string(n) + "}");
}

void frac::StructurePrinter::print_delay_bezier_decl(unsigned int n, unsigned int delay_count) {
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + " = Etat('B" + std::to_string(n) + "_" + std::to_string(delay_count) + "', " + (m_structure.bezierType() == BezierType::Cubic_Bezier ? "2" : "1") + ")");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".bords = {Bord('0'): s, Bord('1'): s}");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".permuts = {Permut('0'): B" + std::to_string(n) + "_" + std::to_string(delay_count) + "}");
}

void frac::StructurePrinter::print_bezier_state_decl(unsigned int n) {
    m_filePrinter.append_nl("    B" + std::to_string(n) + " = Etat('B" + std::to_string(n) + "', " + (m_structure.bezierType() == BezierType::Cubic_Bezier ? "2" : "1") + ")");
    m_filePrinter.append_nl("    B" + std::to_string(n) + ".bords = {Bord('0'): s, Bord('1'): s}");
    m_filePrinter.append_nl("    B" + std::to_string(n) + ".permuts = {Permut('0'): B" + std::to_string(n) + "}");
}

void frac::StructurePrinter::print_impl_of_edge(const frac::Edge& edge) {
    if (edge.edgeType() == EdgeType::CANTOR) {
        if (edge.isDelay()) {
            this->print_delay_cantor_impl(edge.nbSubdivisions(), edge.delay());
        } else {
            this->print_cantor_n_state_impl(edge.nbSubdivisions());
        }
    } else {
        if (edge.isDelay()) {
            this->print_delay_bezier_impl(edge.nbSubdivisions(), edge.delay());
        } else {
            this->print_bezier_state_impl(edge.nbSubdivisions());
        }
    }
}

void frac::StructurePrinter::print_delay_cantor_impl(unsigned int n, unsigned int delay_count) {
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".subs = {Sub('0'): " + (delay_count > 1 ? "C" + std::to_string(n) + "_" + std::to_string(delay_count - 1) : "C" + std::to_string(n)) + "}");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".buildIntern()");
    if (m_structure.cantorType() == frac::CantorType::Linear_Cantor) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".space = [Bord_('0'), Bord_('1')]");
    } else if (m_structure.cantorType() == frac::CantorType::Quadratic_Cantor) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".space = [Bord_('0'), Intern_(''), Bord_('1')]");
    } else {//cubic
        m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".space = [Bord_('0'), Intern_('0'), Intern_('1'), Bord_('1')]");
    }
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Bord('0'), Bord('1'))");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Bord('1'), Bord('0'))");

    //permut intern
    if (m_structure.cantorType() == frac::CantorType::Quadratic_Cantor) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Intern(''), Intern(''))");
    } else if (m_structure.cantorType() == frac::CantorType::Cubic_Cantor) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Intern('0'), Intern('1'))");
        m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Intern('1'), Intern('0'))");
    }

    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Sub('0'), Sub('0') + Permut('0'))");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Bord('0') + Sub('0'), Sub('0') + Bord('0'))");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Bord('1') + Sub('0'), Sub('0') + Bord('1'))");

    if (m_structure.cantorType() == frac::CantorType::Linear_Cantor) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".grid.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
    } else if (m_structure.cantorType() == frac::CantorType::Quadratic_Cantor) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]");
    } else {//cubic
        m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_('0'), Intern_('1'), Bord_('1')])]");
    }

    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");

    //matrices for intern points
    if (m_structure.cantorType() == CantorType::Cubic_Cantor) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".initMat[Sub_('0') + Intern('0')] = FMat([");
        m_filePrinter.append_nl("        [0.0],");
        m_filePrinter.append_nl("        [1.0],");
        m_filePrinter.append_nl("        [0.0],");
        m_filePrinter.append_nl("        [0.0]]).setTyp('Const')");

        m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".initMat[Sub_('0') + Intern('1')] = FMat([");
        m_filePrinter.append_nl("        [0.0],");
        m_filePrinter.append_nl("        [0.0],");
        m_filePrinter.append_nl("        [1.0],");
        m_filePrinter.append_nl("        [0.0]]).setTyp('Const')");
    } else if (m_structure.cantorType() == CantorType::Quadratic_Cantor) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".initMat[Sub_('0') + Intern('')] = FMat([");
        m_filePrinter.append_nl("        [0.0],");
        m_filePrinter.append_nl("        [1.0],");
        m_filePrinter.append_nl("        [0.0]]).setTyp('Const')");
    }
}

void frac::StructurePrinter::print_cantor_n_state_impl(unsigned int n) {
    m_filePrinter.append("    C" + std::to_string(n) + ".subs = {");
    for (unsigned int i = 0; i < n - 1; ++i) {
        m_filePrinter.append("Sub('" + std::to_string(i) + "'): C" + std::to_string(n) + ", ");
    }
    m_filePrinter.append_nl("Sub('" + std::to_string(n - 1) + "'): C" + std::to_string(n) + "}");
    m_filePrinter.append_nl("    C" + std::to_string(n) + ".buildIntern()");

    if (m_structure.cantorType() == frac::CantorType::Linear_Cantor) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + ".space = [Bord_('0'), Bord_('1')]");
    } else if (m_structure.cantorType() == frac::CantorType::Quadratic_Cantor) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + ".space = [Bord_('0'), Intern_(''), Bord_('1')]");
    } else {//cubic
        m_filePrinter.append_nl("    C" + std::to_string(n) + ".space = [Bord_('0'), Intern_('0'), Intern_('1'), Bord_('1')]");
    }

    m_filePrinter.append_nl("    C" + std::to_string(n) + "(Permut('0') + Bord('0'), Bord('1'))");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "(Permut('0') + Bord('1'), Bord('0'))");
    for (unsigned int i = 0; i < n; ++i) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + "(Permut('0') + Sub('" + std::to_string(i) + "'), Sub('" + std::to_string(n - i - 1) + "') + Permut('0'))");
    }

    //permut intern
    if (m_structure.cantorType() == frac::CantorType::Quadratic_Cantor) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + "(Permut('0') + Intern(''), Intern(''))");
    } else if (m_structure.cantorType() == frac::CantorType::Cubic_Cantor) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + "(Permut('0') + Intern('0'), Intern('1'))");
        m_filePrinter.append_nl("    C" + std::to_string(n) + "(Permut('0') + Intern('1'), Intern('0'))");
    }

    m_filePrinter.append_nl("    C" + std::to_string(n) + "(Bord('0') + Sub('0'), Sub('0') + Bord('0'))");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "(Bord('1') + Sub('0'), Sub(" + std::to_string(n - 1) + ") + Bord('1'))");

    if (m_structure.cantorType() == frac::CantorType::Linear_Cantor) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + ".grid.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
    } else if (m_structure.cantorType() == frac::CantorType::Quadratic_Cantor) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]");
    } else {//cubic
        m_filePrinter.append_nl("    C" + std::to_string(n) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_('0'), Intern_('1'), Bord_('1')])]");
    }

    //matrices
    if (m_structure.cantorType() == frac::CantorType::Linear_Cantor) {
        for (unsigned int i = 0; i < n; ++i) {  // for each subdivision T0, T1, ... Tn-1
            m_filePrinter.append_nl("    C" + std::to_string(n) + ".initMat[Sub_('" + std::to_string(i) + "')] = FMat([");
            std::vector<float> t = frac::utils::get_cantor_linear_transformation(i, n);
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[0]) + ", " + frac::utils::to_string(t[1]) + "],");
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[2]) + ", " + frac::utils::to_string(t[3]) + "]]).setTyp('Const')");
        }
    } else if (m_structure.cantorType() == frac::CantorType::Quadratic_Cantor) {
        for (unsigned int i = 0; i < n; ++i) {  // for each subdivision T0, T1, ... Tn-1
            m_filePrinter.append_nl("    C" + std::to_string(n) + ".initMat[Sub_('" + std::to_string(i) + "')] = FMat([");
            std::vector<float> t = frac::utils::get_cantor_quadratic_transformation(i, n);
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[0]) + ", " + frac::utils::to_string(t[1]) + ", " + frac::utils::to_string(t[2]) + "],");
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[3]) + ", " + frac::utils::to_string(t[4]) + ", " + frac::utils::to_string(t[5]) + "],");
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[6]) + ", " + frac::utils::to_string(t[7]) + ", " + frac::utils::to_string(t[8]) + "]]).setTyp('Const')");
        }
    } else {//cubic
        for (unsigned int i = 0; i < n; ++i) {  // for each subdivision T0, T1, ... Tn-1
            m_filePrinter.append_nl("    C" + std::to_string(n) + ".initMat[Sub_('" + std::to_string(i) + "')] = FMat([");
            std::vector<float> t = frac::utils::get_cantor_cubic_transformation(i, n);
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[0]) + ", " + frac::utils::to_string(t[1]) + ", " + frac::utils::to_string(t[2]) + ", " + frac::utils::to_string(t[3]) + "],");
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[4]) + ", " + frac::utils::to_string(t[5]) + ", " + frac::utils::to_string(t[6]) + ", " + frac::utils::to_string(t[7]) + "],");
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[8]) + ", " + frac::utils::to_string(t[9]) + ", " + frac::utils::to_string(t[10]) + ", " + frac::utils::to_string(t[11]) + "],");
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[12]) + ", " + frac::utils::to_string(t[13]) + ", " + frac::utils::to_string(t[14]) + ", " + frac::utils::to_string(t[15]) + "]]).setTyp('Const')");
        }
    }
}

void frac::StructurePrinter::print_delay_bezier_impl(unsigned int n, unsigned int delay_count) {
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".subs = {Sub('0'): " + (delay_count > 1 ? "B" + std::to_string(n) + "_" + std::to_string(delay_count - 1) : "B" + std::to_string(n)) + "}");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".buildIntern()");
    if (m_structure.bezierType() == BezierType::Cubic_Bezier) {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".space = [Bord_('0'), Intern_('0'), Intern_('1'), Bord_('1')]");
    } else {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".space = [Bord_('0'), Intern_(''), Bord_('1')]");
    }
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Bord('0'), Bord('1'))");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Bord('1'), Bord('0'))");
    if (m_structure.bezierType() == BezierType::Cubic_Bezier) {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Intern('0'), Intern('1'))");
        m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Intern('1'), Intern('0'))");
    } else {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Intern(''), Intern(''))");
    }
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Sub('0'), Sub('0') + Permut('0'))");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Bord('0') + Sub('0'), Sub('0') + Bord('0'))");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Bord('1') + Sub('0'), Sub('0') + Bord('1'))");
    if (m_structure.bezierType() == BezierType::Cubic_Bezier) {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_('0'), Intern_('1'), Bord_('1')])]");
    } else {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]");
    }
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
    if (m_structure.bezierType() == BezierType::Cubic_Bezier) {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".initMat[Sub_('0') + Intern('0')] = FMat([");
        m_filePrinter.append_nl("        [0.0],");
        m_filePrinter.append_nl("        [1.0],");
        m_filePrinter.append_nl("        [0.0],");
        m_filePrinter.append_nl("        [0.0]]).setTyp('Const')");

        m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".initMat[Sub_('0') + Intern('1')] = FMat([");
        m_filePrinter.append_nl("        [0.0],");
        m_filePrinter.append_nl("        [0.0],");
        m_filePrinter.append_nl("        [1.0],");
        m_filePrinter.append_nl("        [0.0]]).setTyp('Const')");
    } else {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".initMat[Sub_('0') + Intern('')] = FMat([");
        m_filePrinter.append_nl("        [0.0],");
        m_filePrinter.append_nl("        [1.0],");
        m_filePrinter.append_nl("        [0.0]]).setTyp('Const')");
    }
}

void frac::StructurePrinter::print_bezier_state_impl(unsigned int n) {
    m_filePrinter.append("    B" + std::to_string(n) + ".subs = {");
    for (unsigned int i = 0; i < n - 1; ++i) {
        m_filePrinter.append("Sub('" + std::to_string(i) + "'): B" + std::to_string(n) + ", ");
    }
    m_filePrinter.append_nl("Sub('" + std::to_string(n - 1) + "'): B" + std::to_string(n) + "}");
    m_filePrinter.append_nl("    B" + std::to_string(n) + ".buildIntern()");
    if (m_structure.bezierType() == BezierType::Cubic_Bezier) {
        m_filePrinter.append_nl("    B" + std::to_string(n) + ".space = [Bord_('0'), Intern_('0'), Intern_('1'), Bord_('1')]");
    } else {
        m_filePrinter.append_nl("    B" + std::to_string(n) + ".space = [Bord_('0'), Intern_(''), Bord_('1')]");
    }
    m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Bord('0'), Bord('1'))");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Bord('1'), Bord('0'))");
    if (m_structure.bezierType() == BezierType::Cubic_Bezier) {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Intern('0'), Intern('1'))");
        m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Intern('1'), Intern('0'))");
    } else {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Intern(''), Intern(''))");
    }
    for (unsigned int i = 0; i < n; ++i) {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Sub(" + std::to_string(i) + "), Sub(" + std::to_string(n - i - 1) + ") + Permut('0'))");
    }
    if (m_structure.bezierType() == BezierType::Cubic_Bezier) {
        m_filePrinter.append_nl("    B" + std::to_string(n) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_('0'), Intern_('1'), Bord_('1')])]");
    } else {
        m_filePrinter.append_nl("    B" + std::to_string(n) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]");
    }
    m_filePrinter.append_nl("    B" + std::to_string(n) + ".prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
    if (m_structure.bezierType() == BezierType::Cubic_Bezier) {
        for (unsigned int i = 0; i < n; ++i) {  // for each subdivision T0, T1, ... Tn-1
            m_filePrinter.append_nl("    B" + std::to_string(n) + ".initMat[Sub_('" + std::to_string(i) + "')] = FMat([");
            std::vector<float> t = frac::utils::get_bezier_cubic_transformation(i, n);
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[0]) + ", " + frac::utils::to_string(t[1]) + ", " + frac::utils::to_string(t[2]) + ", " + frac::utils::to_string(t[3]) + "],");
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[4]) + ", " + frac::utils::to_string(t[5]) + ", " + frac::utils::to_string(t[6]) + ", " + frac::utils::to_string(t[7]) + "],");
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[8]) + ", " + frac::utils::to_string(t[9]) + ", " + frac::utils::to_string(t[10]) + ", " + frac::utils::to_string(t[11]) + "],");
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[12]) + ", " + frac::utils::to_string(t[13]) + ", " + frac::utils::to_string(t[14]) + ", " + frac::utils::to_string(t[15]) + "]]).setTyp('Const')");
        }
    } else {
        for (unsigned int i = 0; i < n; ++i) {  // for each subdivision T0, T1, ... Tn-1
            m_filePrinter.append_nl("    B" + std::to_string(n) + ".initMat[Sub_('" + std::to_string(i) + "')] = FMat([");
            std::vector<float> t = frac::utils::get_bezier_quadratic_transformation(i, n);
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[0]) + ", " + frac::utils::to_string(t[1]) + ", " + frac::utils::to_string(t[2]) + "],");
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[3]) + ", " + frac::utils::to_string(t[4]) + ", " + frac::utils::to_string(t[5]) + "],");
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[6]) + ", " + frac::utils::to_string(t[7]) + ", " + frac::utils::to_string(t[8]) + "]]).setTyp('Const')");
        }
    }
}

void frac::StructurePrinter::print_init_subds() {
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

void frac::StructurePrinter::print_edges_of_cell(frac::Face const& cell) {
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

void frac::StructurePrinter::print_subd_of_cell(frac::Face const& cell) {
    std::vector<frac::Face> subds = cell.subdivisions();
    m_filePrinter.append("    " + cell.name() + ".subs = {");
    int i = 0;
    for (frac::Face const& f: subds) {
        if (i == 0) {
            m_filePrinter.append("Sub('" + std::to_string(i) + "'): " + f.name());
        } else {
            m_filePrinter.append(", Sub('" + std::to_string(i) + "'): " + f.name());
        }
        i += 1;
    }
    m_filePrinter.append_nl("}");
}

void frac::StructurePrinter::print_space_of_cell(frac::Face const& cell) {
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

void frac::StructurePrinter::print_prim_of_cell(frac::Face const& cell) {
    m_filePrinter.append_nl("    " + cell.name() + ".prim.elems = [Figure(2, [");
    for (std::size_t i = 0; i < cell.len(); ++i) {
        if (cell[i].edgeType() == EdgeType::BEZIER && cell[i].delay() == 0) {
            for (std::size_t j = 0; j < cell[i].nbSubdivisions(); ++j) {
                if (cell[i].nbSubdivisions() > 2) {
                    m_filePrinter.append_nl("        Bord_('" + std::to_string(i) + "') + Sub('" + std::to_string(j) + "') + Bord('0'),");
                } else {
                    for (std::size_t k = 0; k < cell[i].nbSubdivisions(); ++k) {
                        m_filePrinter.append_nl("        Bord_('" + std::to_string(i) + "') + Sub('" + std::to_string(j) + "') + Sub('" + std::to_string(k) + "') + Bord('0'),");
                    }
                }
            }
        } else {
            m_filePrinter.append_nl("        Bord_('" + std::to_string(i) + "') + Bord('0'),");
        }
    }
    m_filePrinter.append_nl("    ])]");
}

void frac::StructurePrinter::print_edge_adjacencies_of_cell(frac::Face const& cell) {
    for (std::size_t i = 0; i < cell.len(); ++i) {
        m_filePrinter.append_nl("    " + cell.name() + "(Bord('" + std::to_string(i) + "') + Bord('1'), Bord('" + std::to_string(utils::mod(i + 1, cell.len())) + "') + Bord('0'))");
    }
}

void frac::StructurePrinter::print_plan_control_points() {
    std::size_t max = m_structure.faces().size();
    for (std::size_t index_face = 0; index_face < max; ++index_face) {
        std::size_t nb_pts = m_structure.nbControlPointsOfFace(index_face);
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

void frac::StructurePrinter::print_plan_coords_control_points() {
    for (std::size_t index_face = 0; index_face < m_coords.size(); ++index_face) {
        std::size_t nb_pts = m_coords[index_face].size();
        m_filePrinter.append_nl("    init.initMat[Sub_('" + std::to_string(index_face) + "')] = FMat([");

        //x
        m_filePrinter.append("        [");
        for (std::size_t i = 0; i < nb_pts - 1; ++i) {
            m_filePrinter.append(frac::utils::to_string(static_cast<float>(m_coords[index_face][i].x())) + ", ");
        }
        m_filePrinter.append_nl(frac::utils::to_string(static_cast<float>(m_coords[index_face][nb_pts - 1].x())) + "],");

        //y
        m_filePrinter.append("        [");
        for (std::size_t i = 0; i < nb_pts - 1; ++i) {
            m_filePrinter.append(frac::utils::to_string(static_cast<float>(m_coords[index_face][i].y())) + ", ");
        }
        m_filePrinter.append_nl(frac::utils::to_string(static_cast<float>(m_coords[index_face][nb_pts - 1].y())) + "],");

        //z
        m_filePrinter.append("        [");
        for (std::size_t i = 0; i < nb_pts - 1; ++i) {
            m_filePrinter.append("0, ");
        }
        m_filePrinter.append_nl("0],");

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

void frac::StructurePrinter::print_footer() {
    //for automatic subdivision algorithm
    //m_filePrinter.append_nl("    auto = Auto(init)");
    //m_filePrinter.append_nl("    auto.autoSubs(300)");
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

void frac::StructurePrinter::exportMassSpringSystemStruct() {
    frac::Set<frac::Face> faces = m_structure.allFaces();
    for (frac::Face const& f: faces) {
        // export one file for each face that has not a delay
        if (f.delay() != 0) continue;
        m_filePrinter.reset();
        std::size_t dim = f.nbControlPoints(m_structure.bezierType(), m_structure.cantorType());
        mss::MassSpringSystem system(dim);

        std::size_t nbMasses = 0;
        std::vector<frac::Face> const& subdivisions = f.subdivisions();
        for (frac::Face const& subdivision: subdivisions) {
            nbMasses += subdivision.nbControlPoints(m_structure.bezierType(), m_structure.cantorType());
        }
        nbMasses -= subdivisions.size() * f.adjEdge().nbControlPoints(m_structure.bezierType(), m_structure.cantorType());

        for (std::size_t i = 0; i < nbMasses; i++) {
            system.addMass(0.9);
        }

        // ( index of subface, index of edge, index of control point ) -> index of mass
        using Key = std::tuple<std::size_t, std::size_t, std::size_t>;
        std::map<Key, std::size_t> mapIndices;
        std::size_t currentMassIndex = 0;
        for (std::size_t indexSubFace = 0; indexSubFace < subdivisions.size(); indexSubFace++) {
            for (std::size_t indexEdge = 0; indexEdge < subdivisions[indexSubFace].len(); indexEdge++) {
                for (std::size_t indexControlPoint = 0; indexControlPoint < subdivisions[indexSubFace][indexEdge].nbControlPoints(m_structure.bezierType(), m_structure.cantorType()); indexControlPoint++) {
                    if (indexSubFace == 0) {
                        // the last control point of last edge is associated to the same mass as the first control point of the first edge, that is the 0-th mass
                        if (indexEdge == subdivisions[indexSubFace].len() - 1 && indexControlPoint == subdivisions[indexSubFace][indexEdge].nbControlPoints(m_structure.bezierType(), m_structure.cantorType()) - 1) {
                            mapIndices[Key(indexSubFace, indexEdge, indexControlPoint)] = 0;
                        } else {
                            // for all other edges, we just need to check if the first control point of the edge is shared by the last of the previous edge
                            // it is always the case, except for the first edge
                            if (indexControlPoint == 0 && indexEdge != 0) {
                                // try to find the index associated to the last control point of the previous edge
                                auto it = mapIndices.find(Key(indexSubFace, indexEdge - 1, subdivisions[indexSubFace][indexEdge - 1].nbControlPoints(m_structure.bezierType(), m_structure.cantorType()) - 1));
                                if (it != mapIndices.end()) {
                                    // if index found, reuse it
                                    mapIndices[Key(indexSubFace, indexEdge, indexControlPoint)] = it->second;
                                } else {
                                    // else association to the next available mass
                                    mapIndices[Key(indexSubFace, indexEdge, indexControlPoint)] = currentMassIndex;
                                    currentMassIndex++;
                                }
                            } else {
                                // for all other control points of the edge, association to the next available mass
                                mapIndices[Key(indexSubFace, indexEdge, indexControlPoint)] = currentMassIndex;
                                currentMassIndex++;
                            }
                        }
                    } else {
                        // for all other subfaces, the association must take care of adjacencies
                        // indices associated to the last interior edge already exist
                        // the last control point of last edge is associated to the same mass as the first control point of the first edge
                        if (indexEdge == subdivisions[indexSubFace].len() - 1 && indexControlPoint == subdivisions[indexSubFace][indexEdge].nbControlPoints(m_structure.bezierType(), m_structure.cantorType()) - 1) {
                            mapIndices[Key(indexSubFace, indexEdge, indexControlPoint)] = mapIndices[Key(indexSubFace, 0, 0)];
                        } else {
                            // two different cases : is it the last interior edge or not?
                            if (subdivisions[indexSubFace].lastInterior() == static_cast<int>(indexEdge)) {
                                // if last interior edge, retrieve the indices from the first interior edge of the previous subface
                                std::size_t nbIndicesOfCurrentEdge = subdivisions[indexSubFace][indexEdge].nbControlPoints(m_structure.bezierType(), m_structure.cantorType());
                                Key oldKey(indexSubFace - 1, subdivisions[indexSubFace - 1].firstInterior(), nbIndicesOfCurrentEdge - indexControlPoint - 1);
                                mapIndices[Key(indexSubFace, indexEdge, indexControlPoint)] = mapIndices[oldKey];
                            } else {
                                // if not the last interior edge
                                // it could be the first interior edge of the last subface
                                // or the previous edge of the first interior edge of the last subface
                                if (indexSubFace == subdivisions.size() - 1 && static_cast<int>(indexEdge) == subdivisions[indexSubFace].firstInterior()) {
                                    // if first interior edge of the last subface
                                    // retrieve indices from the last interior edge of the first subface
                                    std::size_t nbIndicesOfCurrentEdge = subdivisions[indexSubFace][indexEdge].nbControlPoints(m_structure.bezierType(), m_structure.cantorType());
                                    Key oldKey(0, subdivisions[0].lastInterior(), nbIndicesOfCurrentEdge - indexControlPoint - 1);
                                    mapIndices[Key(indexSubFace, indexEdge, indexControlPoint)] = mapIndices[oldKey];
                                    if (indexControlPoint == 0) {
                                        // we need to fix the last control point of the previous edge
                                        // it is always associated to a new mass, but it needs to be
                                        // the same as the first control point of the first interior edge
                                        std::size_t nbIndicesOfLastEdge = subdivisions[indexSubFace][indexEdge - 1].nbControlPoints(m_structure.bezierType(), m_structure.cantorType());
                                        mapIndices[Key(indexSubFace, indexEdge - 1, nbIndicesOfLastEdge - 1)] = mapIndices[oldKey];
                                        currentMassIndex--;
                                    }
                                } else {
                                    // we just need to check if the first control point of the edge is shared by the last of the previous edge
                                    // it is always the case, except for the first edge
                                    if (indexControlPoint == 0) {
                                        if (indexEdge != 0) {
                                            // find the index associated to the last control point of the previous edge
                                            Key oldKey(indexSubFace, indexEdge - 1, subdivisions[indexSubFace][indexEdge - 1].nbControlPoints(m_structure.bezierType(), m_structure.cantorType()) - 1);
                                            mapIndices[Key(indexSubFace, indexEdge, indexControlPoint)] = mapIndices[oldKey];
                                        } else {
                                            // for the first edge, we need to check if the last edge is the last interior edge
                                            if (subdivisions[indexSubFace].lastInterior() == static_cast<int>(subdivisions[indexSubFace].len() - 1)) {
                                                // if the last edge is the last interior edge
                                                // we must retrieve the mass index from the first interior edge of the previous subface
                                                mapIndices[Key(indexSubFace, indexEdge, indexControlPoint)] = mapIndices[Key(indexSubFace - 1, subdivisions[indexSubFace - 1].firstInterior(), 0)];
                                            } else {
                                                // if the last edge is not the last interior edge
                                                // associate to a new index
                                                mapIndices[Key(indexSubFace, indexEdge, indexControlPoint)] = currentMassIndex;
                                                currentMassIndex++;
                                            }
                                        }
                                    } else {
                                        // the last control point of the lacuna edge is associated to
                                        // the first control point of the lacuna edge of the previous subface
                                        if (indexControlPoint == subdivisions[indexSubFace][indexEdge].nbControlPoints(m_structure.bezierType(), m_structure.cantorType()) - 1 && subdivisions[indexSubFace].firstInterior() + 1 == static_cast<int>(indexEdge)) {
                                            Key oldKey(indexSubFace - 1, subdivisions[indexSubFace - 1].firstInterior() + 1, 0);
                                            mapIndices[Key(indexSubFace, indexEdge, indexControlPoint)] = mapIndices[oldKey];
                                        } else {
                                            // for all other control points of the edge, association to the next available mass
                                            mapIndices[Key(indexSubFace, indexEdge, indexControlPoint)] = currentMassIndex;
                                            currentMassIndex++;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        for (auto const& constraint: frac::Face::s_incidences[f.name()]) {
            frac::EdgeType edgeType = f[constraint.Edge1].edgeType();
            std::size_t nbControlPoints = f[constraint.Edge1].nbControlPoints(m_structure.bezierType(), m_structure.cantorType());
            std::vector<std::size_t> controlPointsIndices = f.controlPointIndices(constraint.Edge1, m_structure.bezierType(), m_structure.cantorType(), false);
            std::vector<float> transformation;
            if (f[constraint.Edge1].isDelay()) {
                for (std::size_t i = 0; i < nbControlPoints; i++) {
                    for (std::size_t j = 0; j < nbControlPoints; j++) {
                        transformation.push_back(i == j ? 1 : 0);
                    }
                }
            } else {
                if (edgeType == frac::EdgeType::CANTOR) {
                    switch (m_structure.cantorType()) {
                        case CantorType::Linear_Cantor:
                            transformation = frac::utils::get_cantor_linear_transformation(constraint.SubEdge1, f[constraint.Edge1].nbSubdivisions());
                            break;
                        case CantorType::Quadratic_Cantor:
                            transformation = frac::utils::get_cantor_quadratic_transformation(constraint.SubEdge1, f[constraint.Edge1].nbSubdivisions());
                            break;
                        case CantorType::Cubic_Cantor:
                            transformation = frac::utils::get_cantor_cubic_transformation(constraint.SubEdge1, f[constraint.Edge1].nbSubdivisions());
                            break;
                    }
                } else {
                    switch (m_structure.bezierType()) {
                        case BezierType::Linear_Bezier:
                            transformation = frac::utils::get_bezier_linear_transformation(constraint.SubEdge1, f[constraint.Edge1].nbSubdivisions());
                            break;
                        case BezierType::Quadratic_Bezier:
                            transformation = frac::utils::get_bezier_quadratic_transformation(constraint.SubEdge1, f[constraint.Edge1].nbSubdivisions());
                            break;
                        case BezierType::Cubic_Bezier:
                            transformation = frac::utils::get_bezier_cubic_transformation(constraint.SubEdge1, f[constraint.Edge1].nbSubdivisions());
                            break;
                    }
                }
            }

            for (std::size_t indexControlPoint = 0; indexControlPoint < nbControlPoints; indexControlPoint++) {
                mss::Mass& m = system.masses().at(mapIndices[Key(constraint.SubFace2, constraint.Edge2, indexControlPoint)]);
                if (!m.fixed()) {
                    m.setFixed(true);
                    // reset coordinates
                    for (std::size_t i = 0; i < dim; i++) {
                        m.position().at(i) = 0;
                    }
                    // fill coordinates
                    for (std::size_t i = 0; i < controlPointsIndices.size(); i++) {
                        std::size_t columnIndex = indexControlPoint;
                        std::size_t rowIndex = i;
                        std::size_t index = controlPointsIndices.size() * rowIndex + columnIndex;
                        m.position().at(controlPointsIndices[i]) = transformation[index];
                    }
                }
            }
        }

        for (std::size_t indexSubFace = 0; indexSubFace < subdivisions.size(); indexSubFace++) {
            for (std::size_t indexEdge = 0; indexEdge < subdivisions[indexSubFace].len(); indexEdge++) {
                for (std::size_t indexControlPoint = 0; indexControlPoint < subdivisions[indexSubFace][indexEdge].nbControlPoints(m_structure.bezierType(), m_structure.cantorType()) - 1; indexControlPoint++) {
                    if (static_cast<int>(indexEdge) != subdivisions[indexSubFace].lastInterior()) {
                        system.addSpring(mapIndices[Key(indexSubFace, indexEdge, indexControlPoint)], mapIndices[Key(indexSubFace, indexEdge, indexControlPoint + 1)], 0.01, 0.0);
                    }
                }
            }
        }

        m_filePrinter.append(system.toString());
        m_filePrinter.printToFile(m_filename + f.name() + ".mss");
    }
}

