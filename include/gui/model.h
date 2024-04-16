#ifndef MODEL_H
#define MODEL_H

#include <QVector>
#include <QVector3D>

namespace he {
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
    [[nodiscard]] const float* constDataFace() const { return m_dataFace.constData(); }

    [[nodiscard]] const float* constDataSphere() const { return m_dataSphere.constData(); }

    [[nodiscard]] const float* constDataEdge() const { return m_dataEdge.constData(); }

    [[nodiscard]] const float* constDataCircles() const { return m_dataCircles.constData(); }

    [[nodiscard]] const float* constDataCirclesDual() const { return m_dataCirclesDual.constData(); }

    [[nodiscard]] const float* constDataVertices() const { return m_dataVertices.constData(); }

    //the number of floats of vertices (in GPU POV)
    [[nodiscard]] int countFace() const { return m_countFace; }

    [[nodiscard]] int countSphere() const { return m_countSphere; }

    [[nodiscard]] int countEdge() const { return m_countEdge; }

    [[nodiscard]] int countCircles() const { return m_countCircle; }

    [[nodiscard]] int countCirclesDual() const { return m_countCircleDual; }

    [[nodiscard]] int countVertices() const { return m_countVertices; }

    //the number of vertices (in GPU POV)
    [[nodiscard]] int vertexCountFace() const { return m_countFace / 8; }

    [[nodiscard]] int vertexCountSphere() const { return m_countSphere / 8; }

    [[nodiscard]] int vertexCountEdge() const { return m_countEdge / 8; }

    [[nodiscard]] int vertexCountCircles() const { return m_countCircle / 8; }

    [[nodiscard]] int vertexCountCirclesDual() const { return m_countCircleDual / 8; }

    [[nodiscard]] int vertexCountVertices() const { return m_countVertices / 8; }

    /**
     * @brief update all data that has to be displayed.
     * Calls all specific update data functions.
     */
    void updateData();

    /**
     * @brief update specific data based on the mesh,
     * necessary when the mesh changed
     */
    void updateDataFaces();
    void updateDataSphere();
    void updateDataEdge();
    void updateDataCircles();
    void updateDataCirclesDual();
    void updateDataVertices();

    /**
     * @brief setter
     * @param mesh the mesh to set to this model.
     * Calls updateData()
     */
    void setMesh(he::Mesh* mesh);

    /**
     * @brief Apply a transform to the mesh and update faces, edges and vertices data
     * @param transform the transform to apply on the vertices
     */
    void transformMesh(QMatrix4x4 const& transform);

    /**
     * @brief setter for the sphere mesh, update the sphere data
     * @param mesh
     */
    void setSphereMesh(he::Mesh* mesh);

    /**
     * @brief getter
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

    /**
     * @brief Sets the selected edge index
     * @param edgeIndex the index of the edge that is selected
     */
    void setSelectedEdge(int edgeIndex);

    /**
     * @brief getter
     * @return a pointer to the selected face, nullptr if no face is selected
     */
    [[nodiscard]] he::Face* selectedFace();


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

    void addVertexCircleDual(QVector3D const& v, QVector3D const& color, float ID, float isSelected);

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
     * @brief getter
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

    //the amount of data
    int m_countFace = 0;
    int m_countSphere = 0;
    int m_countEdge = 0;
    int m_countCircle = 0;
    int m_countCircleDual = 0;
    int m_countVertices = 0;

    //the mesh the model is based on
    he::Mesh* m_mesh = nullptr;
    he::Mesh* m_sphereMesh = nullptr;

    QVector<poly::Circle> m_circles;
    QVector<poly::Circle> m_circlesDual;

    //the index of the selected face
    int m_selectedFace = 0;
    int m_selectedVertex = 0;
    int m_selectedEdge = 0;

    const float m_dashLength = 90.0f;
};

#endif // MODEL_H
