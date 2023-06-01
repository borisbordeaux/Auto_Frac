#include "fileprinter.h"
#include <iostream>
#include <fstream>
#include <ostream>

std::string frac::FilePrinter::s_output;

void frac::FilePrinter::append(const std::string& text) {
    FilePrinter::s_output += text;
}

void frac::FilePrinter::append_nl(const std::string& text) {
    FilePrinter::s_output += text + '\n';
}

void frac::FilePrinter::printToFile(const std::string& filename) noexcept {
    std::ofstream file;
    try {
        file.open(filename);
        file << FilePrinter::s_output;
    } catch (std::runtime_error const& error) {
        std::cerr << error.what() << std::endl;
    }
    try {
        if (file.is_open()) {
            file.close();
        }
    } catch (std::runtime_error const& error) {
        std::cerr << error.what() << std::endl;
    }
}
