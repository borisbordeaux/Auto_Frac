#include "polytopal/structure.h"

poly::Structure::Structure(he::Mesh const& mesh) : m_mesh(mesh) {}

std::string poly::Structure::toString() const {
    return this->m_mesh.toString().toStdString();
}
