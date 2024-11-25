#include "gui/batchcircle.h"

void BatchCircle::init() {
    this->initializeOpenGLFunctions();

    glPatchParameteri(GL_PATCH_VERTICES, 1);

    m_vao.create();
    m_vbo.create();

    m_vao.bind();
    m_vbo.bind();

    //enable enough attrib array for all the data of the circle's vertex
    glEnableVertexAttribArray(0); //center
    glEnableVertexAttribArray(1); //radius
    glEnableVertexAttribArray(2); //x axis
    glEnableVertexAttribArray(3); //y axis
    glEnableVertexAttribArray(4); //color
    glEnableVertexAttribArray(5); //ID
    //center
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, static_cast<int>(m_floatsPerVertex * sizeof(GLfloat)), nullptr);
    //radius
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, static_cast<int>(m_floatsPerVertex * sizeof(GLfloat)), reinterpret_cast<void*>(3 * sizeof(GLfloat)));
    //x axis
    glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, static_cast<int>(m_floatsPerVertex * sizeof(GLfloat)), reinterpret_cast<void*>(4 * sizeof(GLfloat)));
    //y axis
    glVertexAttribPointer(3, 3, GL_FLOAT, GL_FALSE, static_cast<int>(m_floatsPerVertex * sizeof(GLfloat)), reinterpret_cast<void*>(7 * sizeof(GLfloat)));
    //color
    glVertexAttribPointer(4, 3, GL_FLOAT, GL_FALSE, static_cast<int>(m_floatsPerVertex * sizeof(GLfloat)), reinterpret_cast<void*>(10 * sizeof(GLfloat)));
    //ID
    glVertexAttribPointer(5, 1, GL_FLOAT, GL_FALSE, static_cast<int>(m_floatsPerVertex * sizeof(GLfloat)), reinterpret_cast<void*>(13 * sizeof(GLfloat)));
    m_vbo.release();
    m_vao.release();

    //init shader for circles
    m_program.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/circles/vs.glsl");
    m_program.addShaderFromSourceFile(QOpenGLShader::TessellationControl, "../shaders/circles/tcs.glsl");
    m_program.addShaderFromSourceFile(QOpenGLShader::TessellationEvaluation, "../shaders/circles/tes.glsl");
    m_program.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/circles/fs.glsl");
    m_program.bindAttributeLocation("center", 0);
    m_program.bindAttributeLocation("radius", 1);
    m_program.bindAttributeLocation("axisX", 2);
    m_program.bindAttributeLocation("axisY", 3);
    m_program.bindAttributeLocation("color", 4);
    m_program.bindAttributeLocation("ID", 5);
    m_program.link();

    //get locations of uniforms
    m_program.bind();
    m_projMatrixLoc = m_program.uniformLocation("projMatrix");
    m_viewMatrixLoc = m_program.uniformLocation("mvMatrix");

    //init shader for circles picking
//    m_programPicking.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/circles/picking/vs.glsl");
//    m_programPicking.addShaderFromSourceFile(QOpenGLShader::Geometry, "../shaders/circles/picking/gs.glsl");
//    m_programPicking.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/circles/picking/fs.glsl");
//    m_programPicking.bindAttributeLocation("vertex", 0);
//    m_programPicking.bindAttributeLocation("color", 1);
//    m_programPicking.bindAttributeLocation("ID", 2);
//    m_programPicking.bindAttributeLocation("isSelected", 3);
//    m_programPicking.link();
//
//    //get location of uniforms
//    m_programPicking.bind();
//    m_projMatrixPickingLoc = m_programPicking.uniformLocation("projMatrix");
//    m_viewMatrixPickingLoc = m_programPicking.uniformLocation("mvMatrix");
//    m_invViewportPickingLoc = m_programPicking.uniformLocation("invViewport");
}

void BatchCircle::update() {
    m_vbo.bind();
    m_vbo.allocate(m_data.constData(), m_count * static_cast<int>(sizeof(GLfloat)));
    m_vbo.release();
}

void BatchCircle::render(PickingType type) {
    switch (type) {
        case PickingType::PickingCircle: {
//            bool cullFaceEnabled = glIsEnabled(GL_CULL_FACE);
//            if (cullFaceEnabled) {
//                glDisable(GL_CULL_FACE);
//            }
//            m_programPicking.bind();
//            m_vao.bind();
//            glDrawArrays(GL_LINES, 0, m_count / m_floatsPerVertex);
//            m_programPicking.release();
//            if (cullFaceEnabled) {
//                glEnable(GL_CULL_FACE);
//            }
//            break;
        }
        case PickingType::PickingNone:
            m_program.bind();
            m_vao.bind();
            glDrawArrays(GL_PATCHES, 0, static_cast<int>(m_circles.size()));
            m_program.release();
            break;
        case PickingType::PickingFace:
        case PickingType::PickingEdge:
        case PickingType::PickingVertex:
            break;
    }
}

void BatchCircle::setProjection(QMatrix4x4 matrix) {
    m_program.bind();
    m_program.setUniformValue(m_projMatrixLoc, matrix);
    m_program.release();

//    m_programPicking.bind();
//    m_programPicking.setUniformValue(m_projMatrixPickingLoc, matrix);
//    m_programPicking.release();
}

void BatchCircle::setCamera(Camera camera) {
    camera.zoom(0.001f);
    m_program.bind();
    m_program.setUniformValue(m_viewMatrixLoc, camera.getViewMatrix());
    m_program.release();

//    m_programPicking.bind();
//    m_programPicking.setUniformValue(m_viewMatrixPickingLoc, camera.getViewMatrix());
//    m_programPicking.release();
}

void BatchCircle::setInvViewport(float /*x*/, float /*y*/) {
//    m_programPicking.bind();
//    m_programPicking.setUniformValue(m_invViewportPickingLoc, x, y);
//    m_programPicking.release();
}

void BatchCircle::updateData() {
    //the amount of data of the circles
    m_count = 0;
    m_data.clear();

    //we resize the data for rapidity
    m_data.resize(m_circles.size() * m_floatsPerVertex);

    int ID = 1;
    for (gui::Circle const& c: m_circles) {
        bool isSelected = ID == m_selectedCircle;
        QVector3D color = isSelected ? QVector3D(0, 1, 0) : c.color();
        this->addVertexCircle(c.center(), c.radius(), c.axisX(), c.axisY(), color, static_cast<float>(ID));
        ID++;
    }

    this->update();
}

void BatchCircle::scaleCircles(float by) {
    if (this->selectedCircle() != nullptr) {
        this->selectedCircle()->setRadius(this->selectedCircle()->radius() + by);
    } else {
        for (gui::Circle& c: m_circles) {
            c.setRadius(c.radius() + by);
        }
    }
}

void BatchCircle::addCircle(gui::Circle const& circle) {
    m_circles.push_back(circle);
}

void BatchCircle::resetCircles() {
    m_circles.clear();
}

void BatchCircle::setSelectedCircle(int circleIndex) {
    m_selectedCircle = circleIndex;
}

gui::Circle* BatchCircle::selectedCircle() {
    gui::Circle* res = nullptr;

    if (m_selectedCircle - 1 >= 0 && m_selectedCircle - 1 < m_circles.size()) {
        res = &m_circles[m_selectedCircle - 1];
    }

    return res;
}

void BatchCircle::updateColorOfCircles(QVector3D const& color) {
    for (gui::Circle& c: m_circles) {
        c.setColor(color);
    }
    this->updateData();
}

QVector<gui::Circle> const& BatchCircle::circles() const {
    return m_circles;
}

void BatchCircle::addVertexCircle(QVector3D const& center, float radius, QVector3D const& xAxis, QVector3D const& yAxis, QVector3D const& color, float ID) {
    //add to the end of the data already added
    float* p = m_data.data() + m_count;
    //the coordinates of the vertex
    *p++ = center.x();
    *p++ = center.y();
    *p++ = center.z();
    *p++ = radius;
    *p++ = xAxis.x();
    *p++ = xAxis.y();
    *p++ = xAxis.z();
    *p++ = yAxis.x();
    *p++ = yAxis.y();
    *p++ = yAxis.z();
    *p++ = color.x();
    *p++ = color.y();
    *p++ = color.z();
    //the ID of the circle
    *p = ID;
    //we update the amount of data
    m_count += m_floatsPerVertex;
}

qsizetype BatchCircle::findNbOfSegmentsCircles() const {
    return 90 * m_circles.size();
}

int BatchCircle::renderOrder() {
    return 4;
}

int BatchCircle::pickingOrder() {
    return 0;
}
