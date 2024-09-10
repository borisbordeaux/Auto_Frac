#ifndef MODEL_H
#define MODEL_H

#include <QVector>
#include <QVector3D>

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
    const float* constDataFace() const { return m_dataFace.constData(); }

    const float* constDataSphere() const { return m_dataSphere.constData(); }

    const float* constDataEdge() const { return m_dataEdge.constData(); }

    const float* constDataCircles() const { return m_dataCircles.constData(); }

    const float* constDataCirclesDual() const { return m_dataCirclesDual.constData(); }

    const float* constDataVertices() const { return m_dataVertices.constData(); }

    const float* constDataDebugLine() const { return m_dataDebugLine.constData(); }

    //the number of floats of vertices (in GPU POV)
    int countFace() const { return m_countFace; }

    int countSphere() const { return m_countSphere; }

    int countEdge() const { return m_countEdge; }

    int countCircles() const { return m_countCircle; }

    int countCirclesDual() const { return m_countCircleDual; }

    int countVertices() const { return m_countVertices; }

    int countDebugLine() const { return m_countDebugLine; }

    //the number of vertices (in GPU POV)
    int vertexCountFace() const { return m_countFace / 8; }

    int vertexCountSphere() const { return m_countSphere / 3; }

    int vertexCountEdge() const { return m_countEdge / 8; }

    int vertexCountCircles() const { return m_countCircle / 8; }

    int vertexCountCirclesDual() const { return m_countCircleDual / 6; }

    int vertexCountVertices() const { return m_countVertices / 8; }

    int vertexCountDebugLine() const { return m_countDebugLine / 3; }

    /**
     * @brief update all data that has to be displayed.
     * Calls all specific update data functions.
     */
    void updateData();

    /**
     * @brief update specific data based on the mesh
     */
    void updateDataFaces();
    void updateDataSphere();
    void updateDataEdges();
    void updateDataCircles();
    void updateDataCirclesDual();
    void updateDataVertices();

    /**
     * @param mesh the mesh to set to this model.
     * Calls updateData()
     */
    void setMesh(he::Mesh* mesh);

    /**
     * @brief Apply a transform to the mesh and update faces, edges and vertices data
     * @param transform the transform to apply on the vertices
     */
    void transformMesh(QMatrix4x4 const& transform);

    void scaleCircles(float by);

    /**
     * @brief setter for the sphere mesh, update the sphere data
     * @param mesh
     */
    void setSphereMesh(he::Mesh* mesh);

    /**
     * @return a pointer to the sphere mesh
     */
    he::Mesh* sphereMesh() const;

    /**
     * @brief Adds circle to the data
     * @param circle the circle to add
     */
    void addCircle(poly::Circle const& circle);

    /**
     * @brief Adds dual circle to the data
     * @param circle the dual circle to add
     */
    void addCircleDual(poly::Circle const& circle);
    void resetCircles();
    void resetCirclesDual();

    /**
     * @brief Sets the selected face index
     * @param faceIndex the index of the face that is selected
     */
    void setSelectedFace(int faceIndex);

    /**
     * @brief Sets the selected vertex index
     * @param vertexIndex the index of the vertex that is selected
     */
    void setSelectedVertex(int vertexIndex);
    void setSelectedVertex2(int vertexIndex);

    /**
     * @brief Sets the selected edge index
     * @param edgeIndex the index of the edge that is selected
     */
    void setSelectedEdge(int edgeIndex);

    /**
     * @brief Sets the selected circle index
     * @param circleIndex the index of the circle that is selected
     */
    void setSelectedCircle(int circleIndex);

    /**
     * @return a pointer to the selected face, nullptr if no face is selected
     */
    he::Face* selectedFace();

    /**
     * @return a pointer to the selected edge, nullptr if no edge is selected
     */
    he::HalfEdge* selectedEdge();

    /**
     * @return a pointer to the selected vertex, nullptr if no vertex is selected
     */
    he::Vertex* selectedVertex();
    he::Vertex* selectedVertex2();

    /**
     * @return a pointer to the selected circle, nullptr if no circle is selected
     */
    poly::Circle* selectedCircle();

    void updateColorOfCircles(QVector3D const& color);
    void updateColorOfCirclesDual(QVector3D const& color);

    QVector<poly::Circle> const& circles() const;

    void addDebugLine(QVector3D const& v1, QVector3D const& v2);
    void clearDebugLine();

    he::Mesh* mesh();

private:

    /**
     * @brief add a face to the data
     * @param f the face to add
     * @param ID the face ID
     */
    void addFace(he::Face* f, int ID);

    void addFaceSphere(he::Face* f);

    /**
     * @brief add a vertex, its normal and its ID to the data
     * @param v the vertex to add
     * @param n the normal of the vertex
     * @param ID the ID of the face
     * @param isSelected has to be true if the face is selected
     */
    void addVertexFace(QVector3D const& v, QVector3D const& n, float ID, float isSelected);
    void addVertexSphere(QVector3D const& v);

    /**
     * @brief add a vertex to the edge data
     * @param v te vertex to add
     * @param ID the ID of the edge
     * @param isSelected has to be true if the edge is selected
     */
    void addVertexEdge(QVector3D const& v, QVector3D const& color, float ID, float isSelected);

    void addVertexCircle(QVector3D const& v, QVector3D const& color, float ID, float isSelected);

    void addVertexCircleDual(QVector3D const& v, QVector3D const& color);

    void addVertex(QVector3D const& v, QVector3D const& color, float ID, float isSelected);

    /**
     * @brief computes the normal of the 3 vertices and
     * add the vertices and their normal to the data.
     * Be aware to add vertices in trigonometric order
     * @param x1, y1, z1 the values of the first vertex
     * @param x2, y2, z2 the values of the second vertex
     * @param x3, y3, z3 the values of the third vertex
     * @param ID the ID of the face
     * @param isSelected has to be true if the face is selected
     */
    void triangle(QVector3D const& pos1, QVector3D const& pos2, QVector3D const& pos3, float ID, float isSelected);
    void triangleSphere(const QVector3D& pos1, const QVector3D& pos2, const QVector3D& pos3);

    /**
     * @return the number of triangles of the polyhedron
     */
    static qsizetype findNbOfTriangle(he::Mesh* mesh);

    qsizetype findNbOfSegmentsCircles() const;
    qsizetype findNbOfSegmentsCirclesDual() const;

private:
    //the data of this model
    QVector<float> m_dataFace;
    QVector<float> m_dataSphere;
    QVector<float> m_dataEdge;
    QVector<float> m_dataCircles;
    QVector<float> m_dataCirclesDual;
    QVector<float> m_dataVertices;
    QVector<float> m_dataDebugLine;

    //the amount of data
    int m_countFace = 0;
    int m_countSphere = 0;
    int m_countEdge = 0;
    int m_countCircle = 0;
    int m_countCircleDual = 0;
    int m_countVertices = 0;
    int m_countDebugLine = 0;

    //the mesh the model is based on
    he::Mesh* m_mesh = nullptr;
    he::Mesh* m_sphereMesh = nullptr;

    QVector<poly::Circle> m_circles;
    QVector<poly::Circle> m_circlesDual;

    //the index of the selected face
    int m_selectedFace = 0;
    int m_selectedVertex = 0;
    int m_selectedVertex2 = 0;
    int m_selectedEdge = 0;
    int m_selectedCircle = 0;
};

#endif // MODEL_H
