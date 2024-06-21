#include "fractal/structure3dprinter.h"
#include "utils/utils.h"

#include <utility>

namespace frac {
Structure3DPrinter::Structure3DPrinter(const Structure3D& structure, std::string filename) :
        m_structure(structure), m_filename(std::move(filename)) {

}

void Structure3DPrinter::exportStruct() {
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
    m_filePrinter.append_nl("    # all faces states");
    frac::Set<frac::Face> faces = m_structure.allFaces();
    for (frac::Face const& c: faces.data()) {
        m_filePrinter.append_nl("    # " + c.toString());
        m_filePrinter.append_nl("    " + c.name() + " = Etat('" + c.name() + "', 0)");
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # all volumes states");
    frac::Set<frac::Volume> volumes = m_structure.allVolumes();
    for (frac::Volume const& v: volumes.data()) {
        m_filePrinter.append_nl("    # " + v.toString());
        m_filePrinter.append_nl("    " + v.name() + " = Etat('" + v.name() + "', 0)");
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # subd of init");
    this->print_init_subds();

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # edges of all faces");
    for (auto const& c: faces.data()) {
        this->print_edges_of_face(c);
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # edges of all volumes");
    for (frac::Volume const& v: volumes.data()) {
        this->print_edges_of_volume(v);
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # subdivisions of all faces");
    for (auto const& c: faces.data()) {
        this->print_subd_of_face(c);
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # subdivisions of all volumes");
    for (frac::Volume const& v: volumes.data()) {
        this->print_subd_of_volume(v);
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # build intern of all faces");
    for (frac::Face const& f: faces.data()) {
        m_filePrinter.append_nl("    " + f.name() + ".buildIntern()");
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # build intern of all volumes");
    for (frac::Volume const& v: volumes.data()) {
        m_filePrinter.append_nl("    " + v.name() + ".buildIntern()");
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # spaces of all faces");
    for (frac::Face const& f: faces.data()) {
        this->print_space_of_face(f);
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # spaces of all volumes");
    for (frac::Volume const& v: volumes.data()) {
        this->print_space_of_volume(v);
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # grid of all faces");
    for (frac::Face const& f: faces.data()) {
        m_filePrinter.append_nl("    " + f.name() + ".addGrid(Bord)");
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # grid of all volumes");
    for (frac::Volume const& v: volumes.data()) {
        m_filePrinter.append_nl("    " + v.name() + ".addGrid(Bord)");
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # prim of all volumes");
    for (frac::Volume const& v: volumes.data()) {
        this->print_prim_of_volume(v);
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # constraints of all faces");
    for (frac::Face const& c: faces.data()) {
        m_filePrinter.append_nl("    # incidence constraints");
        m_filePrinter.append(Face::s_incidenceConstraints[c.name()]);
        m_filePrinter.append_nl("    # adjacency constraints");
        if (Face::s_adjacencyConstraints.find(c.name()) != Face::s_adjacencyConstraints.end()) {
            m_filePrinter.append(Face::s_adjacencyConstraints[c.name()]);
        }
        m_filePrinter.append_nl("    # edges adjacency constraints");
        this->print_edge_adjacencies_of_face(c);
    }

    m_filePrinter.append_nl("    ##############################");
    m_filePrinter.append_nl("    # constraints of all volumes");
    for (frac::Volume const& v: volumes.data()) {
        m_filePrinter.append_nl("    # incidence constraints");
        m_filePrinter.append(frac::Volume::s_incidenceConstraints[v.name()]);
        m_filePrinter.append_nl("    # adjacency constraints");
        if (frac::Volume::s_adjacencyConstraints.find(v.name()) != frac::Volume::s_adjacencyConstraints.end()) {
            m_filePrinter.append(frac::Volume::s_adjacencyConstraints[v.name()]);
        }
        m_filePrinter.append_nl("    # edges adjacency constraints");
        this->print_edge_adjacencies_of_volume(v);
    }

    //m_filePrinter.append_nl("    # constraints on init faces");
    //m_filePrinter.append(m_structure.strAdjacencies());

    this->print_footer();
    m_filePrinter.printToFile(m_filename);
}

void Structure3DPrinter::print_header() {
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

void Structure3DPrinter::print_vertex_state() {
    m_filePrinter.append_nl("    s = Etat('s', 1)");
    m_filePrinter.append_nl("    s.subs = {Sub('0'): s}");
    m_filePrinter.append_nl("    s.buildIntern()");
}

void Structure3DPrinter::print_decl_of_edge(Edge const& edge) {
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

void Structure3DPrinter::print_delay_cantor_decl(unsigned int n, unsigned int delay_count) {
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + " = Etat('C" + std::to_string(n) + "_" + std::to_string(delay_count) + "', 0)");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".bords = {Bord('0'): s, Bord('1'): s}");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".permuts = {Permut('0'): C" + std::to_string(n) + "_" + std::to_string(delay_count) + "}");
}

void Structure3DPrinter::print_cantor_n_state_decl(unsigned int n) {
    m_filePrinter.append_nl("    C" + std::to_string(n) + " = Etat('C" + std::to_string(n) + "', 0)");
    m_filePrinter.append_nl("    C" + std::to_string(n) + ".bords = {Bord('0'): s, Bord('1'): s}");
    m_filePrinter.append_nl("    C" + std::to_string(n) + ".permuts = {Permut('0'): C" + std::to_string(n) + "}");
}

void Structure3DPrinter::print_delay_bezier_decl(unsigned int n, unsigned int delay_count) {
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + " = Etat('B" + std::to_string(n) + "_" + std::to_string(delay_count) + "', " + (m_structure.isBezierCubic() ? "2" : "1") + ")");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".bords = {Bord('0'): s, Bord('1'): s}");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".permuts = {Permut('0'): B" + std::to_string(n) + "_" + std::to_string(delay_count) + "}");
}

void Structure3DPrinter::print_bezier_state_decl(unsigned int n) {
    m_filePrinter.append_nl("    B" + std::to_string(n) + " = Etat('B" + std::to_string(n) + "', " + (m_structure.isBezierCubic() ? "2" : "1") + ")");
    m_filePrinter.append_nl("    B" + std::to_string(n) + ".bords = {Bord('0'): s, Bord('1'): s}");
    m_filePrinter.append_nl("    B" + std::to_string(n) + ".permuts = {Permut('0'): B" + std::to_string(n) + "}");
}

void Structure3DPrinter::print_impl_of_edge(const Edge& edge) {
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

void Structure3DPrinter::print_delay_cantor_impl(unsigned int n, unsigned int delay_count) {
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".subs = {Sub('0'): " + (delay_count > 1 ? "C" + std::to_string(n) + "_" + std::to_string(delay_count - 1) : "C" + std::to_string(n)) + "}");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".buildIntern()");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".space = [Bord_('0'), Bord_('1')]");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Bord('0'), Bord('1'))");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Bord('1'), Bord('0'))");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Sub('0'), Sub('0') + Permut('0'))");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Bord('0') + Sub('0'), Sub('0') + Bord('0'))");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Bord('1') + Sub('0'), Sub('0') + Bord('1'))");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".grid.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "_" + std::to_string(delay_count) + ".prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
}

void Structure3DPrinter::print_cantor_n_state_impl(unsigned int n) {
    m_filePrinter.append("    C" + std::to_string(n) + ".subs = {");
    for (unsigned int i = 0; i < n - 1; ++i) {
        m_filePrinter.append("Sub('" + std::to_string(i) + "'): C" + std::to_string(n) + ", ");
    }
    m_filePrinter.append_nl("Sub('" + std::to_string(n - 1) + "'): C" + std::to_string(n) + "}");
    m_filePrinter.append_nl("    C" + std::to_string(n) + ".buildIntern()");
    m_filePrinter.append_nl("    C" + std::to_string(n) + ".space = [Bord_('0'), Bord_('1')]");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "(Permut('0') + Bord('0'), Bord('1'))");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "(Permut('0') + Bord('1'), Bord('0'))");
    for (unsigned int i = 0; i < n; ++i) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + "(Permut('0') + Sub('" + std::to_string(i) + "'), Sub('" + std::to_string(n - i - 1) + "') + Permut('0'))");
    }
    m_filePrinter.append_nl("    C" + std::to_string(n) + "(Bord('0') + Sub('0'), Sub('0') + Bord('0'))");
    m_filePrinter.append_nl("    C" + std::to_string(n) + "(Bord('1') + Sub('0'), Sub(" + std::to_string(n - 1) + ") + Bord('1'))");
    m_filePrinter.append_nl("    C" + std::to_string(n) + ".grid.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
    unsigned int m = n * 2 - 1;
    unsigned int prem = m - 1;
    unsigned int deux = 1;
    m_filePrinter.append_nl("    C" + std::to_string(n) + ".initMat[Sub_('0') + Bord('1')] = FMat([");
    m_filePrinter.append_nl("        [" + frac::utils::to_string(float(prem) / float(m)) + "],");
    m_filePrinter.append_nl("        [" + frac::utils::to_string(float(deux) / float(m)) + "]]).setTyp('Const')");
    prem = prem - 1;
    deux = deux + 1;
    for (unsigned int j = 0; j < n - 2; ++j) {
        m_filePrinter.append_nl("    C" + std::to_string(n) + ".initMat[Sub_('" + std::to_string(j + 1) + "')] = FMat([");
        m_filePrinter.append_nl("        [" + frac::utils::to_string(float(prem) / float(m)) + ", " + utils::to_string(float(prem - 1) / float(m)) + "],");
        m_filePrinter.append_nl("        [" + frac::utils::to_string(float(deux) / float(m)) + ", " + utils::to_string(float(deux + 1) / float(m)) + "]]).setTyp('Const')");
        prem = prem - 2;
        deux = deux + 2;
    }
    m_filePrinter.append_nl("    C" + std::to_string(n) + ".initMat[Sub_('" + std::to_string(n - 1) + "') + Bord('0')] = FMat([");
    m_filePrinter.append_nl("        [" + frac::utils::to_string(float(prem) / float(m)) + "],");
    m_filePrinter.append_nl("        [" + frac::utils::to_string(float(deux) / float(m)) + "]]).setTyp('Const')");
}

void Structure3DPrinter::print_delay_bezier_impl(unsigned int n, unsigned int delay_count) {
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".subs = {Sub('0'): " + (delay_count > 1 ? "B" + std::to_string(n) + "_" + std::to_string(delay_count - 1) : "B" + std::to_string(n)) + "}");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".buildIntern()");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".space = [Bord_('0'), Intern_(''), Bord_('1')]");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Bord('0'), Bord('1'))");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Bord('1'), Bord('0'))");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Intern(''), Intern(''))");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Permut('0') + Sub('0'), Sub('0') + Permut('0'))");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Bord('0') + Sub('0'), Sub('0') + Bord('0'))");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + "(Bord('1') + Sub('0'), Sub('0') + Bord('1'))");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "_" + std::to_string(delay_count) + ".initMat[Sub_('0') + Intern('')] = FMat([");
    m_filePrinter.append_nl("        [0.0],");
    m_filePrinter.append_nl("        [1.0],");
    m_filePrinter.append_nl("        [0.0]]).setTyp('Const')");
}

void Structure3DPrinter::print_bezier_state_impl(unsigned int n) {
    m_filePrinter.append("    B" + std::to_string(n) + ".subs = {");
    for (unsigned int i = 0; i < n - 1; ++i) {
        m_filePrinter.append("Sub('" + std::to_string(i) + "'): B" + std::to_string(n) + ", ");
    }
    m_filePrinter.append_nl("Sub('" + std::to_string(n - 1) + "'): B" + std::to_string(n) + "}");
    m_filePrinter.append_nl("    B" + std::to_string(n) + ".buildIntern()");
    if (m_structure.isBezierCubic()) {
        m_filePrinter.append_nl("    B" + std::to_string(n) + ".space = [Bord_('0'), Intern_('0'), Intern_('1'), Bord_('1')]");
    } else {
        m_filePrinter.append_nl("    B" + std::to_string(n) + ".space = [Bord_('0'), Intern_(''), Bord_('1')]");
    }
    m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Bord('0'), Bord('1'))");
    m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Bord('1'), Bord('0'))");
    if (m_structure.isBezierCubic()) {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Intern('0'), Intern('1'))");
        m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Intern('1'), Intern('0'))");
    } else {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Intern(''), Intern(''))");
    }
    for (unsigned int i = 0; i < n; ++i) {
        m_filePrinter.append_nl("    B" + std::to_string(n) + "(Permut('0') + Sub(" + std::to_string(i) + "), Sub(" + std::to_string(n - i - 1) + ") + Permut('0'))");
    }
    if (m_structure.isBezierCubic()) {
        m_filePrinter.append_nl("    B" + std::to_string(n) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_('0'), Intern_('1'), Bord_('1')])]");
    } else {
        m_filePrinter.append_nl("    B" + std::to_string(n) + ".grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]");
    }
    m_filePrinter.append_nl("    B" + std::to_string(n) + ".prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]");
    if (m_structure.isBezierCubic()) {
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
            std::vector<float> t = frac::utils::get_bezier_transformation(i, n);
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[0]) + ", " + frac::utils::to_string(t[1]) + ", " + frac::utils::to_string(t[2]) + "],");
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[3]) + ", " + frac::utils::to_string(t[4]) + ", " + frac::utils::to_string(t[5]) + "],");
            m_filePrinter.append_nl("        [" + frac::utils::to_string(t[6]) + ", " + frac::utils::to_string(t[7]) + ", " + frac::utils::to_string(t[8]) + "]]).setTyp('Const')");
        }
    }
}

void Structure3DPrinter::print_init_subds() {
    std::vector<frac::Volume> const& subds = m_structure.volumes();
    m_filePrinter.append("    init.subs = {");
    int i = 0;
    for (frac::Volume const& s: subds) {
        if (i == 0) {
            m_filePrinter.append("Sub('" + std::to_string(i) + "'): " + s.name());
        } else {
            m_filePrinter.append(", Sub('" + std::to_string(i) + "'): " + s.name());
        }
        i += 1;
    }
    m_filePrinter.append_nl("}");
}

void Structure3DPrinter::print_edges_of_face(Face const& face) {
    m_filePrinter.append("    " + face.name() + ".bords = {");
    int i = 0;
    for (frac::Edge const& edge: face.constData()) {
        if (i == 0) {
            m_filePrinter.append("Bord('" + std::to_string(i) + "'): " + edge.name());
        } else {
            m_filePrinter.append(", Bord('" + std::to_string(i) + "'): " + edge.name());
        }
        i += 1;
    }
    m_filePrinter.append_nl("}");
}

void Structure3DPrinter::print_subd_of_face(Face const& face) {
    std::vector<frac::Face> subds = face.subdivisions();
    m_filePrinter.append("    " + face.name() + ".subs = {");
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

void Structure3DPrinter::print_space_of_face(Face const& face) {
    m_filePrinter.append("    " + face.name() + ".space = [");
    for (std::size_t i = 0; i < face.len(); ++i) {
        if (i == 0) {
            m_filePrinter.append("Bord_('" + std::to_string(i) + "')");
        } else {
            m_filePrinter.append(", Bord_('" + std::to_string(i) + "')");
        }
    }
    m_filePrinter.append_nl("]");
}

void Structure3DPrinter::print_edge_adjacencies_of_face(Face const& face) {
    for (std::size_t i = 0; i < face.len(); ++i) {
        m_filePrinter.append_nl("    " + face.name() + "(Bord('" + std::to_string(i) + "') + Bord('1'), Bord('" + std::to_string(utils::mod(i + 1, face.len())) + "') + Bord('0'))");
    }
}

void Structure3DPrinter::print_edges_of_volume(Volume const& volume) {
    m_filePrinter.append("    " + volume.name() + ".bords = {");
    int i = 0;
    for (frac::Face const& face: volume.faces()) {
        if (i == 0) {
            m_filePrinter.append("Bord('" + std::to_string(i) + "'): " + face.name());
        } else {
            m_filePrinter.append(", Bord('" + std::to_string(i) + "'): " + face.name());
        }
        i += 1;
    }
    m_filePrinter.append_nl("}");
}

void Structure3DPrinter::print_subd_of_volume(Volume const& volume) {
    std::vector<frac::Volume> subds = volume.subdivisions();
    m_filePrinter.append("    " + volume.name() + ".subs = {");
    int i = 0;
    for (frac::Volume const& v: subds) {
        if (i == 0) {
            m_filePrinter.append("Sub('" + std::to_string(i) + "'): " + v.name());
        } else {
            m_filePrinter.append(", Sub('" + std::to_string(i) + "'): " + v.name());
        }
        i += 1;
    }
    m_filePrinter.append_nl("}");
}

void Structure3DPrinter::print_space_of_volume(Volume const& volume) {
    m_filePrinter.append("    " + volume.name() + ".space = [");
    for (std::size_t i = 0; i < volume.len(); ++i) {
        if (i == 0) {
            m_filePrinter.append("Bord_('" + std::to_string(i) + "')");
        } else {
            m_filePrinter.append(", Bord_('" + std::to_string(i) + "')");
        }
    }
    m_filePrinter.append_nl("]");
}

void Structure3DPrinter::print_prim_of_volume(Volume const& volume) {
    m_filePrinter.append_nl("    " + volume.name() + ".prim.elems = [");
    for (std::size_t i = 0; i < volume.len(); i++) {
        m_filePrinter.append_nl("    Figure(2, [");
        for (std::size_t j = 0; j < volume[i].len(); j++) {
            m_filePrinter.append_nl("        Bord_('" + std::to_string(i) + "') + Bord_('" + std::to_string(j) + "') + Bord('0'),");
        }
        m_filePrinter.append_nl("    ]),");
    }
    m_filePrinter.append_nl("    ]");
}

void Structure3DPrinter::print_edge_adjacencies_of_volume(Volume const& volume) {
    m_filePrinter.append_nl("    #TODO: Add edge adjacencies of volume " + volume.name());
}

void Structure3DPrinter::print_footer() {
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

} // frac