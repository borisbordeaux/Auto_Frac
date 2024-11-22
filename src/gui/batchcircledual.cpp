#include "gui/batchcircledual.h"

void BatchCircleDual::init() {
    this->initializeOpenGLFunctions();

    m_vao.create();
    m_vbo.create();

    m_vao.bind();
    m_vbo.bind();

    //enable enough attrib array for all the data of the edge's vertex
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //color
    //coordinates
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), nullptr);
    //color
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    m_vbo.release();
    m_vao.release();

    //init shader for circles dual
    m_program.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/circlesdual/vs.glsl");
    m_program.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/circlesdual/fs.glsl");
    m_program.bindAttributeLocation("vertex", 0);
    m_program.bindAttributeLocation("color", 1);
    m_program.link();

    //get locations of uniforms
    m_program.bind();
    m_projMatrixLoc = m_program.uniformLocation("projMatrix");
    m_viewMatrixLoc = m_program.uniformLocation("mvMatrix");
}

void BatchCircleDual::update() {
    m_vbo.bind();
    m_vbo.allocate(m_data.constData(), m_count * static_cast<int>(sizeof(GLfloat)));
    m_vbo.release();
}

void BatchCircleDual::render(PickingType type) {
    switch (type) {
        case PickingType::PickingNone:
            m_program.bind();
            m_vao.bind();
            glDrawArrays(GL_LINES, 0, m_count / m_floatsPerVertex);
            m_program.release();
            break;
        case PickingType::PickingCircle:
        case PickingType::PickingFace:
        case PickingType::PickingEdge:
        case PickingType::PickingVertex:
            break;
    }
}

void BatchCircleDual::setProjection(QMatrix4x4 matrix) {
    m_program.bind();
    m_program.setUniformValue(m_projMatrixLoc, matrix);
    m_program.release();
}

void BatchCircleDual::setCamera(Camera camera) {
    camera.zoom(0.001f);
    m_program.bind();
    m_program.setUniformValue(m_viewMatrixLoc, camera.getViewMatrix());
    m_program.release();
}

void BatchCircleDual::updateData() {
    //the amount of data of the circles
    m_count = 0;
    m_data.clear();

    //the number of edges
    qsizetype nbOfEdges = findNbOfSegmentsCircles();

    //for each edge, there are 2 vertices
    qsizetype nbOfAdd = 2 * nbOfEdges;

    //we resize the data for rapidity
    m_data.resize(nbOfAdd * 8);

    QVector3D first;
    for (gui::Circle const& c: m_circles) {
        for (int i = 0; i < 360; i += 4) {
            float alpha = qDegreesToRadians(static_cast<float>(i));
            float x = c.center().x() + c.radius() * std::cos(alpha) * c.axisX().x() + c.radius() * std::sin(alpha) * c.axisY().x();
            float y = c.center().y() + c.radius() * std::cos(alpha) * c.axisX().y() + c.radius() * std::sin(alpha) * c.axisY().y();
            float z = c.center().z() + c.radius() * std::cos(alpha) * c.axisX().z() + c.radius() * std::sin(alpha) * c.axisY().z();
            if (i == 0) {
                first = { x, y, z };
            } else {
                this->addVertexCircle({ x, y, z }, c.color());
            }
            this->addVertexCircle({ x, y, z }, c.color());
            if (i == 356) {
                this->addVertexCircle(first, c.color());
            }
        }
    }

    this->update();
}

void BatchCircleDual::addCircle(const gui::Circle& circle) {
    m_circles.push_back(circle);
}

void BatchCircleDual::resetCircles() {
    m_circles.clear();
}

void BatchCircleDual::updateColorOfCircles(const QVector3D& color) {
    for (gui::Circle& c: m_circles) {
        c.setColor(color);
    }
    this->updateData();
}

int BatchCircleDual::renderOrder() {
    return 4;
}

int BatchCircleDual::pickingOrder() {
    return 0;
}

void BatchCircleDual::addVertexCircle(const QVector3D& v, const QVector3D& color) {
    //add to the end of the data already added
    float* p = m_data.data() + m_count;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p++ = v.z();
    *p++ = color.x();
    *p++ = color.y();
    *p = color.z();
    //we update the amount of data
    m_count += 6;
}

qsizetype BatchCircleDual::findNbOfSegmentsCircles() const {
    return 90 * m_circles.size();
}
