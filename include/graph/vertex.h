#ifndef AUTOFRAC_GRAPH_VERTEX_H
#define AUTOFRAC_GRAPH_VERTEX_H

#include <string>
#include <vector>

class VertexGraphicsItem;

namespace graph {

class Vertex {
public:
    explicit Vertex(std::string name);
    [[nodiscard]] std::string const& getName() const;
    [[nodiscard]] std::vector<Vertex*> const& getParents() const;
    [[nodiscard]] std::vector<Vertex*> const& getChildren() const;
    [[nodiscard]] std::vector<Vertex*> & getParents();
    [[nodiscard]] std::vector<Vertex*> & getChildren();
    [[nodiscard]] std::size_t getParentsSize() const;
    [[nodiscard]] std::size_t getChildrenSize() const;
    [[nodiscard]] Vertex* getParent(std::size_t index) const;
    [[nodiscard]] Vertex* getChild(std::size_t index) const;
    void addParent(Vertex* v);
    void addChild(Vertex* v);
    friend std::ostream& operator<<(std::ostream& os, const graph::Vertex& face);

    void setCenter(int centerX, int centerY);
    [[nodiscard]] int getX() const;
    [[nodiscard]] int getY() const;

    [[nodiscard]] VertexGraphicsItem* graphicsItem() const;
private:
    std::string m_name;
    std::vector<Vertex*> m_parents;
    std::vector<Vertex*> m_children;

    //graphics info
    VertexGraphicsItem* m_item;
};

} // graph

#endif //AUTOFRAC_GRAPH_VERTEX_H
