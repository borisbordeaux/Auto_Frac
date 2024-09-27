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
    QVector<float> m_dataVertices;
    int m_countVertices = 0;
    int m_floatsPerVertex = 8;

    QOpenGLVertexArrayObject m_vaoVertices;
    QOpenGLBuffer m_vboVertices;
    QOpenGLShaderProgram* m_programVertices = nullptr;
    QOpenGLShaderProgram* m_programVerticesPicking = nullptr;
    int m_projMatrixLocVertices = 0;
    int m_mvMatrixLocVertices = 0;
    //Vertices picking
    int m_projMatrixPickingLocVertices = 0;
    int m_mvMatrixPickingLocVertices = 0;

    he::Mesh* m_mesh = nullptr;
    bool m_displayProjectionPoint = true;
    bool m_displayMesh = false;
    int m_selectedVertex = 0;
    int m_selectedVertex2 = 0;
};


#endif //AUTOFRAC_BATCHVERTEX_H
