#ifndef MODEL_H
#define MODEL_H

#include <QVector>
#include <QVector3D>
#include "camera.h"
#include "gui/batchgraphicsitem.h"

namespace he {
class Vertex;

class HalfEdge;

class Face;

class Mesh;
}

namespace poly {
class Circle;
}

class Model {
public:
    Model() = default;

    //constant data to be thrown to the GPU
    const float* constDataEdge() const { return m_dataEdge.constData(); }

    const float* constDataCircles() const { return m_dataCircles.constData(); }

    const float* constDataCirclesDual() const { return m_dataCirclesDual.constData(); }

    const float* constDataVertices() const { return m_dataVertices.constData(); }

    //the number of floats of vertices (in GPU POV)
    int countEdge() const { return m_countEdge; }

    int countCircles() const { return m_countCircle; }

    int countCirclesDual() const { return m_countCircleDual; }

    int countVertices() const { return m_countVertices; }

    //the number of vertices (in GPU POV)
    int vertexCountEdge() const { return m_countEdge / 8; }

    int vertexCountCircles() const { return m_countCircle / 8; }

    int vertexCountCirclesDual() const { return m_countCircleDual / 6; }

    int vertexCountVertices() const { return m_countVertices / 8; }

    /**
     * @brief update all data that has to be displayed.
     * Calls all specific update data functions.
     */
    void updateData();

    void updateDataEdges();
    void updateDataCircles();
    void updateDataCirclesDual();
    void updateDataVertices();

    void setMesh(he::Mesh* mesh);

    void transformMesh(QMatrix4x4 const& transform);

    void scaleCircles(float by);

    void addCircle(poly::Circle const& circle);

    void addCircleDual(poly::Circle const& circle);
    void resetCircles();
    void resetCirclesDual();

    void setSelectedVertex(int vertexIndex);

    void setSelectedVertex2(int vertexIndex);

    void setSelectedEdge(int edgeIndex);

    void setSelectedCircle(int circleIndex);

    he::HalfEdge* selectedEdge();

    he::Vertex* selectedVertex();
    he::Vertex* selectedVertex2();

    poly::Circle* selectedCircle();

    void updateColorOfCircles(QVector3D const& color);
    void updateColorOfCirclesDual(QVector3D const& color);

    QVector<poly::Circle> const& circles() const;

    he::Mesh* mesh();

private:
    void addVertexEdge(QVector3D const& v, QVector3D const& color, float ID, float isSelected);

    void addVertexCircle(QVector3D const& v, QVector3D const& color, float ID, float isSelected);

    void addVertexCircleDual(QVector3D const& v, QVector3D const& color);

    void addVertex(QVector3D const& v, QVector3D const& color, float ID, float isSelected);

    qsizetype findNbOfSegmentsCircles() const;
    qsizetype findNbOfSegmentsCirclesDual() const;

private:
    //the data of this model
    QVector<float> m_dataEdge;
    QVector<float> m_dataCircles;
    QVector<float> m_dataCirclesDual;
    QVector<float> m_dataVertices;

    //the amount of data
    int m_countEdge = 0;
    int m_countCircle = 0;
    int m_countCircleDual = 0;
    int m_countVertices = 0;

    //the mesh the model is based on
    he::Mesh* m_mesh = nullptr;

    QVector<poly::Circle> m_circles;
    QVector<poly::Circle> m_circlesDual;

    //the index of the selected face
    int m_selectedVertex = 0;
    int m_selectedVertex2 = 0;
    int m_selectedEdge = 0;
    int m_selectedCircle = 0;
};

#endif // MODEL_H
