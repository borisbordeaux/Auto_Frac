#include "gui/batchcircledual.h"

void BatchCircleDual::init() {
    this->initializeOpenGLFunctions();

    m_ibo.setUsagePattern(QOpenGLBuffer::DynamicDraw);
    m_vao.create();
    m_vbo.create();
    m_ibo.create();

    m_vao.bind();
    m_vbo.bind();
    //enable enough attrib array for all the data of the edge's vertex
    glEnableVertexAttribArray(0); //coordinates
    glEnableVertexAttribArray(1); //color
    glEnableVertexAttribArray(2); //distance
    //coordinates
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 7 * sizeof(GLfloat), nullptr);
    //color
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 7 * sizeof(GLfloat), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //distance
    glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 7 * sizeof(GLfloat), reinterpret_cast<void*>(6 * sizeof(GLfloat)));
    m_ibo.bind();
    m_vbo.release();
    m_vao.release();

    //init shader for circles dual
    m_program.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/circlesdual/vs.glsl");
    m_program.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/circlesdual/fs.glsl");
    m_program.bindAttributeLocation("vertex", 0);
    m_program.bindAttributeLocation("color", 1);
    m_program.bindAttributeLocation("dist", 2);
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

    m_ibo.bind();
    m_ibo.allocate(m_indices.constData(), m_countIndices * static_cast<int>(sizeof(unsigned int)));
    m_ibo.release();
}

void BatchCircleDual::render(PickingType type) {
    switch (type) {
        case PickingType::PickingNone:
            glEnable(GL_PRIMITIVE_RESTART_FIXED_INDEX);
            m_program.bind();
            m_vao.bind();
            //glDrawArrays(GL_LINE_STRIP, 0, m_count / m_floatsPerVertex);
            glDrawElements(GL_LINES, m_countIndices, GL_UNSIGNED_INT, nullptr);

            m_program.release();
            glDisable(GL_PRIMITIVE_RESTART_FIXED_INDEX);
            break;
        case PickingType::PickingCircle:
        case PickingType::PickingFace:
        case PickingType::PickingEdge:
        case PickingType::PickingVertex:
            break;
    }
}

void BatchCircleDual::setProjection(QMatrix4x4 matrix) {
    m_proj = matrix;
    m_program.bind();
    m_program.setUniformValue(m_projMatrixLoc, matrix);
    m_program.release();
}

void BatchCircleDual::setCamera(Camera camera) {
    camera.zoom(0.001f);
    m_view = camera.getViewMatrix();
    m_program.bind();
    m_program.setUniformValue(m_viewMatrixLoc, m_view);
    m_program.release();
}

void BatchCircleDual::setInvViewport(float w, float h) {
    m_w = 1.0f / w;
    m_h = 1.0f / h;
    this->updateData();
}

void BatchCircleDual::updateData() {
    //the amount of data of the circles
    m_count = 0;
    m_countIndices = 0;
    m_data.clear();
    m_indices.clear();

    qsizetype nb = 90;

    //the number of edges
    qsizetype nbOfEdges = nb * m_circles.size();

    //for each edge, there are 2 vertices
    qsizetype nbOfAdd = 2 * nbOfEdges;

    //we resize the data for rapidity
    m_data.resize((nb + 1) * m_circles.size() * 7); //the vertex at angle 0 and 360 are note the same (same position but not the same distance for dashed lines)
    m_indices.resize(nbOfAdd);

    //compute of length
    QMatrix4x4 mvp = m_proj * m_view;

    QMatrix4x4 windowMatrix;
    windowMatrix.scale(m_w / 2.0f, m_h / 2.0f, 1.0f);
    windowMatrix.translate(1.0f, 1.0f, 0.0f);

    unsigned int j = 0;
    for (gui::Circle const& c: m_circles) {
        float dist = 0.0f;
        QVector2D vpPt;
        for (int i = 0; i <= 360; i += static_cast<int>(360 / nb)) {
            float alpha = qDegreesToRadians(static_cast<float>(i));
            float x = c.center().x() + c.radius() * std::cos(alpha) * c.axisX().x() + c.radius() * std::sin(alpha) * c.axisY().x();
            float y = c.center().y() + c.radius() * std::cos(alpha) * c.axisX().y() + c.radius() * std::sin(alpha) * c.axisY().y();
            float z = c.center().z() + c.radius() * std::cos(alpha) * c.axisX().z() + c.radius() * std::sin(alpha) * c.axisY().z();

            if (i == 0) {
                m_indices[m_countIndices] = j;
                m_countIndices++;
            } else {
                m_indices[m_countIndices] = j;
                m_countIndices++;
                if (i != 360) {
                    m_indices[m_countIndices] = j;
                    m_countIndices++;
                }
            }
            QVector4D clip = mvp * QVector4D(x, y, z, 1.0);
            QVector4D ndc = clip / clip.w();
            QVector4D vpC = windowMatrix * ndc;
            float len = i == 0 ? 0.0f : (vpPt - vpC.toVector2D()).length();
            vpPt = vpC.toVector2D();
            dist += len;
            this->addVertexCircle({ x, y, z }, c.color(), dist);
            j++;
        }
    }

    this->update();
}

void BatchCircleDual::addCircle(const gui::Circle& circle) {
    m_circles.push_back(circle);
}

void BatchCircleDual::resetCircles() {
    m_circles.clear();
    m_indices.clear();
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

void BatchCircleDual::addVertexCircle(const QVector3D& v, const QVector3D& color, float dist) {
    //add to the end of the data already added
    float* p = m_data.data() + m_count;
    //the coordinates of the vertex
    *p++ = v.x();
    *p++ = v.y();
    *p++ = v.z();
    *p++ = color.x();
    *p++ = color.y();
    *p++ = color.z();
    *p = dist;
    //we update the amount of data
    m_count += 7;
}

