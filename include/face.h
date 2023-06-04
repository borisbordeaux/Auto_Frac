#ifndef AUTOFRAC_FACE_H
#define AUTOFRAC_FACE_H

#include "edge.h"
#include "uniquevector.h"

#include <map>
#include <vector>
#include <optional>

namespace frac {

class Face {
public:
    explicit Face(std::vector<Edge> edges, unsigned int delay = 0, const Edge& adjEdge = { EdgeType::CANTOR, 2 }, const Edge& gapEdge = { EdgeType::BEZIER, 2 }, const Edge& reqEdge = { EdgeType::BEZIER, 2 });

    [[nodiscard]] std::vector<Edge> const& constData() const;
    [[nodiscard]] std::vector<Edge>& data();
    [[nodiscard]] int firstInterior() const;
    [[nodiscard]] int lastInterior() const;
    [[nodiscard]] std::size_t len() const;
    [[nodiscard]] std::string name() const;
    [[nodiscard]] int offset() const;
    [[nodiscard]] Edge adjEdge() const;
    [[nodiscard]] Edge gapEdge() const;
    [[nodiscard]] Edge reqEdge() const;
    [[nodiscard]] unsigned int delay() const;
    void setAdjEdge(Edge const& edge);
    void setGapEdge(Edge const& edge);
    void setReqEdge(Edge const& edge);
    void setDelay(unsigned int delay);
    void setFirstInterior(int index);
    [[nodiscard]] std::vector<Face> subdivisions() const;
    [[nodiscard]] UniqueVector<Face> allSubdivisions() const;

    Edge const& operator[](std::size_t index) const;
    bool operator==(Face const& other) const;
    friend std::ostream& operator<<(std::ostream& os, const Face& edge);

    [[nodiscard]] std::string toString() const;

    static std::map<std::string, std::string> s_incidenceConstraints;
    static std::map<std::string, std::string> s_adjacencyConstraints;
    static void reset();

private:
    std::vector<Edge> m_data;
    unsigned int m_delay;
    Edge m_adjEdge;
    Edge m_gapEdge;
    Edge m_reqEdge;
    std::string m_name;
    int m_offset;
    int m_firstInterior;

    static UniqueVector<Face> s_existingFaces;

    static void addAdjacencyConstraint(Face const& face, Face const& faceSub1, Face const& faceSub2, unsigned int indexSubFace1, unsigned int indexBordFace1, unsigned int indexSubFace2, unsigned int indexBordFace2);
    static void addIncidenceConstraint(Face const& face, Face const& faceSub, unsigned int indexParentEdge, unsigned int indexSubEdge, unsigned int indexSubFaceEdge, unsigned int indexSubFace);

    static int computeOffset(Face const& face, Face const& other);
    static std::optional<Edge> edgeIfRequired(const Edge& edge, const Edge& reqEdge);
};

} // frac

#endif //AUTOFRAC_FACE_H
