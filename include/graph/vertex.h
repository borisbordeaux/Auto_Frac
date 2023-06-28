#ifndef AUTOFRAC_GRAPH_VERTEX_H
#define AUTOFRAC_GRAPH_VERTEX_H

#include <string>
#include <vector>

namespace graph {

class Vertex {
public:
    explicit Vertex(std::string name);
    [[nodiscard]] std::string const& getName() const;
    [[nodiscard]] std::vector<Vertex*> const& getParents() const;
    [[nodiscard]] std::vector<Vertex*> const& getChildren() const;
    [[nodiscard]] std::size_t getParentsSize() const;
    [[nodiscard]] std::size_t getChildrenSize() const;
    [[nodiscard]] Vertex* getParent(std::size_t index) const;
    [[nodiscard]] Vertex* getChild(std::size_t index) const;
    void addParent(Vertex* v);
    void addChild(Vertex* v);
    friend std::ostream& operator<<(std::ostream& os, const graph::Vertex& face);
    void setCenter(double centerX, double centerY);
    [[nodiscard]] double getX() const;
    [[nodiscard]] double getY() const;
private:
    std::string m_name;
    std::vector<Vertex*> m_parents;
    std::vector<Vertex*> m_children;

    //graphics info
    double m_centerX;
    double m_centerY;
};

} // graph

#endif //AUTOFRAC_GRAPH_VERTEX_H
