#ifndef AUTOFRAC_BATCHVERTEX_H
#define AUTOFRAC_BATCHVERTEX_H

#include <QOpenGLShaderProgram>
#include <QOpenGLBuffer>
#include <QOpenGLVertexArrayObject>
#include "batchgraphicsitem.h"

namespace he {
class Mesh;

class Vertex;
}

class BatchVertex : public BatchGraphicsItem {
public:
    void init() override;
    void update() override;
    void updateData() override;
    void render(PickingType type) override;
    void setProjection(QMatrix4x4 matrix) override;
    void setCamera(Camera camera) override;

    void setMesh(he::Mesh* mesh);
    void setProjectionPoint(bool displayed);
    void setDisplayMesh(bool displayed);

    void setSelectedVertex(int vertexIndex);
    void setSelectedVertex2(int vertexIndex);
    he::Vertex* selectedVertex();
    he::Vertex* selectedVertex2();

private:
    void addVertex(QVector3D const& v, QVector3D const& color, float ID, float isSelected);

private:
    QVector<float> m_data;
    int m_count = 0;
    int m_floatsPerVertex = 8;

    QOpenGLVertexArrayObject m_vao;
    QOpenGLBuffer m_vbo;
    QOpenGLShaderProgram m_program;
    QOpenGLShaderProgram m_programPicking;

    int m_projMatrixLoc = 0;
    int m_viewMatrixLoc = 0;
    //Vertices picking
    int m_projMatrixPickingLoc = 0;
    int m_viewMatrixPickingLoc = 0;

    he::Mesh* m_mesh = nullptr;
    bool m_displayProjectionPoint = true;
    bool m_displayMesh = false;
    int m_selectedVertex = 0;
    int m_selectedVertex2 = 0;
};


#endif //AUTOFRAC_BATCHVERTEX_H
