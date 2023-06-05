#include "utils/fileprinter.h"
#include <fstream>
#include <ostream>

std::string frac::FilePrinter::s_output;

void frac::FilePrinter::append(const std::string& text) {
    FilePrinter::s_output += text;
}

void frac::FilePrinter::append_nl(const std::string& text) {
    FilePrinter::s_output += text + '\n';
}

void frac::FilePrinter::printToFile(const std::string& filename) {
    std::ofstream file;
    file.open(filename, std::ofstream::out | std::ofstream::trunc);
    file << FilePrinter::s_output;
}

void frac::FilePrinter::reset() {
    FilePrinter::s_output.clear();
}
