#ifndef AUTOFRAC_OBJWRITER_H
#define AUTOFRAC_OBJWRITER_H

class QString;

namespace he {
class Mesh;
}

namespace he::writer {

void writeOBJ(QString const& filename, he::Mesh const& mesh);

} // he::reader

#endif //AUTOFRAC_OBJWRITER_H
