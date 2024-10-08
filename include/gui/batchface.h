#ifndef AUTOFRAC_BATCHFACE_H
#define AUTOFRAC_BATCHFACE_H

#include <QOpenGLShaderProgram>
#include <QOpenGLBuffer>
#include <QOpenGLVertexArrayObject>
#include "batchgraphicsitem.h"

namespace he {
class Mesh;

class Face;
}

class BatchFace : public BatchGraphicsItem {
public:
    void init() override;
    void update() override;
    void updateData() override;
    void render(PickingType type) override;

    void setProjection(QMatrix4x4 projection) override;
    void setCamera(Camera camera) override;
    void setLight(QVector3D lightPos) override;

    void setMesh(he::Mesh* mesh);

    void setSelectedFace(int faceIndex);
    he::Face* selectedFace();

    int priority() override { return 1; }

private:
    static qsizetype findNbOfTriangle(he::Mesh* mesh);
    void addFace(he::Face* f, int ID);
    void triangle(QVector3D const& pos1, QVector3D const& pos2, QVector3D const& pos3, float ID, float isSelected);
    void addVertexFace(QVector3D const& v, QVector3D const& n, float ID, float isSelected);

private:
    QVector<float> m_data;
    int m_count = 0;
    int m_floatsPerVertex = 8;

    QOpenGLVertexArrayObject m_vao;
    QOpenGLBuffer m_vbo;
    QOpenGLShaderProgram m_program;
    QOpenGLShaderProgram m_programPicking;

    //Faces viewing
    int m_projMatrixLoc = 0;
    int m_viewMatrixLoc = 0;
    int m_lightPosLoc = 0;
    int m_cameraPosLoc = 0;
    //Faces picking
    int m_projMatrixPickingLoc = 0;
    int m_viewMatrixPickingLoc = 0;

    he::Mesh* m_mesh = nullptr;
    int m_selectedFace = 0;
};


#endif //AUTOFRAC_BATCHFACE_H
