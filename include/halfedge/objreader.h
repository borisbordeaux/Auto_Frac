#ifndef AUTOFRAC_OBJREADER_H
#define AUTOFRAC_OBJREADER_H

class QString;

namespace he {
class Mesh;
}

namespace he::reader {

void readOBJ(QString const& filename, he::Mesh& mesh);

} // he::reader

#endif //AUTOFRAC_OBJREADER_H
