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
    /**
     * @brief Construct a Model based on a mesh
     */
    Model() = default;

    /**
     * @brief getter
     * @return constant data of the polyhedron to be thrown to the GPU
     */
    [[nodiscard]] const float* constData() const { return m_data.constData(); }

    /**
     * @brief getter
     * @return constant data of edges to be thrown to the GPU
     */
    [[nodiscard]] const float* constDataEdge() const { return m_dataEdge.constData(); }

    /**
     * @brief getter
     * @return constant data of edges to be thrown to the GPU
     */
    [[nodiscard]] const float* constDataCircles() const { return m_dataCircles.constData(); }

    /**
     * @brief getter
     * @return constant data of vertices to be thrown to the GPU
     */
    [[nodiscard]] const float* constDataVertices() const { return m_dataVertices.constData(); }

    /**
     * @brief getter
     * @return the amount of data the polyhedron has
     */
    [[nodiscard]] int count() const { return m_count; }

    /**
     * @brief getter
     * @return the amount of data the edges has
     */
    [[nodiscard]] int countEdge() const { return m_countEdge; }

    /**
     * @brief getter
     * @return the amount of data the edges has
     */
    [[nodiscard]] int countCircles() const { return m_countCircle; }

    /**
     * @brief getter
     * @return the number of vertices the polyhedron has
     */
    [[nodiscard]] int vertexCount() const { return m_count / 8; }

    /**
     * @brief getter
     * @return the number of vertices the polyhedron has
     */
    [[nodiscard]] int vertexCountCircles() const { return m_countCircle / 8; }

    /**
     * @brief getter
     * @return the number of vertices the edges has
     */
    [[nodiscard]] int vertexCountEdge() const { return m_countEdge / 8; }


    /**
     * @brief getter
     * @return the amount of data the vertices has
     */
    [[nodiscard]] int countVertices() const { return m_countVertices; }

    /**
     * @brief getter
     * @return the number of vertices the mesh vertices has
     */
    [[nodiscard]] int vertexCountVertices() const { return m_countVertices / 8; }

    /**
     * @brief update the data of the polyhedron based
     * on its mesh, necessary when the mesh changed.
     * Calls updateDataEdge()
     */
    void updateData();

    /**
     * @brief update the data of the edges based
     * on its mesh, necessary when the mesh changed
     */
    void updateDataFaces();
    void updateDataEdge();
    void updateDataSphere();
    void updateDataCircles();
    void updateDataVertices();

    /**
     * @brief setter
     * @param mesh the mesh to set to this model.
     * Calls updateData()
     */
    void setMesh(he::Mesh* mesh);
    void setSphereMesh(he::Mesh* mesh);
    void addCircle(poly::Circle const& circle);
    void addCircleDual(poly::Circle const& circle);
    void resetCircles();

    /**
     * @brief set the selected face index
     * @param faceIndex the index of the face that is selected
     */
    void setSelected(int faceIndex);

    /**
     * @brief getter
     * @return the index of the selected face
     */
    [[nodiscard]] [[maybe_unused]] qsizetype indexSelectedFace() const;

    /**
     * @brief getter
     * @return a pointer to the selected face, nullptr if no face is selected
     */
    [[nodiscard]] [[maybe_unused]] he::Face* selectedFace();

private:

    /**
     * @brief add a face to the data
     * @param f the face to add
     * @param ID the face ID
     */
    void addFace(he::Face* f, int ID);

    /**
     * @brief add a vertex, its normal and its ID to the data
     * @param v the vertex to add
     * @param n the normal of the vertex
     * @param ID the ID of the face
     * @param isSelected has to be true if the face is selected
     */
    void addVertexFace(QVector3D const& v, QVector3D const& n, float ID, float isSelected);

    /**
     * @brief add a vertex to the edge data
     * @param v te vertex to add
     * @param ID the ID of the edge
     * @param isSelected has to be true if the edge is selected
     */
    void addVertexEdge(QVector3D const& v, QVector3D const& color, float ID, float isSelected);

    void addVertexCircle(QVector3D const& v, QVector3D const& color, float ID, float isSelected);

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

    /**
     * @brief getter
     * @return the number of triangles of the polyhedron
     */
    static qsizetype findNbOfTriangle(he::Mesh* mesh);

    /**
     * @brief getter
     * @return the number of edges
     */
    qsizetype findNbOfEdges() const;

    qsizetype findNbOfSegments() const;

    //the data of this model
    QVector<float> m_data;
    QVector<float> m_dataEdge;
    QVector<float> m_dataCircles;
    QVector<float> m_dataVertices;

    //the amount of data
    int m_count = 0;
    int m_countEdge = 0;
    int m_countCircle = 0;
    int m_countVertices = 0;

    //the mesh the model is based on
    he::Mesh* m_mesh = nullptr;
    he::Mesh* m_sphereMesh = nullptr;

    QVector<poly::Circle> m_circles;
    QVector<poly::Circle> m_circlesDual;

    //the index of the selected face
    int m_selectedFace = -1;

    float m_dashLength = 90.0f;
};

#endif // MODEL_H
