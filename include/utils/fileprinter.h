#ifndef AUTOFRAC_FILEPRINTER_H
#define AUTOFRAC_FILEPRINTER_H

#include <string>

namespace frac {

class FilePrinter {
public:
    static void append(std::string const& text);
    static void append_nl(std::string const& text);
    static void printToFile(std::string const& filename);
    static void reset();
private:
    static std::string s_output;
};
}

#endif //AUTOFRAC_FILEPRINTER_H
