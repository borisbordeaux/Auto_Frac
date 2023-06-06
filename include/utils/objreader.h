#ifndef AUTOFRAC_OBJREADER_H
#define AUTOFRAC_OBJREADER_H

class QString;

namespace poly {
class Mesh;
}

namespace poly::reader {

void readOBJ(QString const& filename, poly::Mesh& mesh);

} // poly

#endif //AUTOFRAC_OBJREADER_H
