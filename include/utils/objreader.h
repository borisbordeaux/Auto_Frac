#ifndef AUTOFRAC_OBJREADER_H
#define AUTOFRAC_OBJREADER_H

class QString;

namespace he {
class Mesh;
}

namespace he::reader {

void readOBJ(QString const& filename, he::Mesh& mesh);

} // he::reader

namespace graph {
class IncidenceGraph;
}

namespace graph::reader {

void readOBJ4(QString const& filename, graph::IncidenceGraph& g);

} // graph::reader

#endif //AUTOFRAC_OBJREADER_H
