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
    const float* constDataCircles() const { return m_dataCircles.constData(); }

    const float* constDataCirclesDual() const { return m_dataCirclesDual.constData(); }

    //the number of floats of vertices (in GPU POV)
    int countCircles() const { return m_countCircle; }

    int countCirclesDual() const { return m_countCircleDual; }

    //the number of vertices (in GPU POV)
    int vertexCountCircles() const { return m_countCircle / 8; }

    int vertexCountCirclesDual() const { return m_countCircleDual / 6; }

    /**
     * @brief update all data that has to be displayed.
     * Calls all specific update data functions.
     */
    void updateData();

    void updateDataCircles();
    void updateDataCirclesDual();

    void setMesh(he::Mesh* mesh);

    void transformMesh(QMatrix4x4 const& transform);

    void scaleCircles(float by);

    void addCircle(poly::Circle const& circle);

    void addCircleDual(poly::Circle const& circle);
    void resetCircles();
    void resetCirclesDual();

    void setSelectedCircle(int circleIndex);

    poly::Circle* selectedCircle();

    void updateColorOfCircles(QVector3D const& color);
    void updateColorOfCirclesDual(QVector3D const& color);

    QVector<poly::Circle> const& circles() const;

    he::Mesh* mesh();

private:
    void addVertexCircle(QVector3D const& v, QVector3D const& color, float ID, float isSelected);

    void addVertexCircleDual(QVector3D const& v, QVector3D const& color);

    qsizetype findNbOfSegmentsCircles() const;
    qsizetype findNbOfSegmentsCirclesDual() const;

private:
    //the data of this model
    QVector<float> m_dataCircles;
    QVector<float> m_dataCirclesDual;

    //the amount of data
    int m_countCircle = 0;
    int m_countCircleDual = 0;

    //the mesh the model is based on
    he::Mesh* m_mesh = nullptr;

    QVector<poly::Circle> m_circles;
    QVector<poly::Circle> m_circlesDual;

    //the index of the selected face
    int m_selectedCircle = 0;
};

#endif // MODEL_H
