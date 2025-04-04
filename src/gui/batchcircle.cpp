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
    m_program.addShaderFromSourceFile(QOpenGLShader::Geometry, "../shaders/circles/gs.glsl");
    m_program.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/circles/fs.glsl");
    m_program.link();

    //get locations of uniforms
    m_program.bind();
    m_projMatrixLoc = m_program.uniformLocation("projMatrix");
    m_viewMatrixLoc = m_program.uniformLocation("mvMatrix");
    m_invViewportLoc = m_program.uniformLocation("invViewport");
    m_windowMatrixLoc = m_program.uniformLocation("windowMatrix");
    m_leftPlaneLoc = m_program.uniformLocation("leftPlane");
    m_rightPlaneLoc = m_program.uniformLocation("rightPlane");
    m_topPlaneLoc = m_program.uniformLocation("topPlane");
    m_bottomPlaneLoc = m_program.uniformLocation("bottomPlane");

    //init shader for circles picking
    m_programPicking.addShaderFromSourceFile(QOpenGLShader::Vertex, "../shaders/circles/picking/vs.glsl");
    m_programPicking.addShaderFromSourceFile(QOpenGLShader::TessellationControl, "../shaders/circles/picking/tcs.glsl");
    m_programPicking.addShaderFromSourceFile(QOpenGLShader::TessellationEvaluation, "../shaders/circles/picking/tes.glsl");
    m_programPicking.addShaderFromSourceFile(QOpenGLShader::Geometry, "../shaders/circles/picking/gs.glsl");
    m_programPicking.addShaderFromSourceFile(QOpenGLShader::Fragment, "../shaders/circles/picking/fs.glsl");
    m_programPicking.link();

    //get location of uniforms
    m_programPicking.bind();
    m_projMatrixPickingLoc = m_programPicking.uniformLocation("projMatrix");
    m_viewMatrixPickingLoc = m_programPicking.uniformLocation("mvMatrix");
    m_invViewportPickingLoc = m_programPicking.uniformLocation("invViewport");
    m_windowMatrixPickingLoc = m_programPicking.uniformLocation("windowMatrix");
    m_leftPlanePickingLoc = m_programPicking.uniformLocation("leftPlane");
    m_rightPlanePickingLoc = m_programPicking.uniformLocation("rightPlane");
    m_topPlanePickingLoc = m_programPicking.uniformLocation("topPlane");
    m_bottomPlanePickingLoc = m_programPicking.uniformLocation("bottomPlane");
}

void BatchCircle::update() {
    m_vbo.bind();
    m_vbo.allocate(m_data.constData(), m_count * static_cast<int>(sizeof(GLfloat)));
    m_vbo.release();
}

void BatchCircle::render(PickingType type) {
    switch (type) {
        case PickingType::PickingCircle: {
            bool cullFaceEnabled = glIsEnabled(GL_CULL_FACE);
            if (cullFaceEnabled) {
                glDisable(GL_CULL_FACE);
            }
            m_programPicking.bind();
            m_vao.bind();
            glDrawArrays(GL_PATCHES, 0, static_cast<int>(m_circles.size()));
            m_programPicking.release();
            if (cullFaceEnabled) {
                glEnable(GL_CULL_FACE);
            }
            break;
        }
        case PickingType::PickingNone: {
            bool cullFaceEnabled = glIsEnabled(GL_CULL_FACE);
            if (cullFaceEnabled) {
                glDisable(GL_CULL_FACE);
            }
            m_program.bind();
            m_vao.bind();
            glDrawArrays(GL_PATCHES, 0, static_cast<int>(m_circles.size()));
            m_program.release();
            if (cullFaceEnabled) {
                glEnable(GL_CULL_FACE);
            }
            break;
        }
        case PickingType::PickingCircleDual:
        case PickingType::PickingFace:
        case PickingType::PickingEdge:
        case PickingType::PickingVertex:
            break;
    }
}

void BatchCircle::setProjection(QMatrix4x4 matrix) {
    m_projMatrix = matrix;

    m_program.bind();
    m_program.setUniformValue(m_projMatrixLoc, m_projMatrix);
    this->sendUniformsPlaneFrustum();
    m_program.release();

    m_programPicking.bind();
    m_programPicking.setUniformValue(m_projMatrixPickingLoc, m_projMatrix);
    this->sendUniformsPlaneFrustum(true);
    m_programPicking.release();
}

void BatchCircle::setCamera(Camera camera) {
    camera.zoom(0.001f);
    m_viewMatrix = camera.getViewMatrix();

    m_program.bind();
    m_program.setUniformValue(m_viewMatrixLoc, m_viewMatrix);
    this->sendUniformsPlaneFrustum();
    m_program.release();

    m_programPicking.bind();
    m_programPicking.setUniformValue(m_viewMatrixPickingLoc, m_viewMatrix);
    this->sendUniformsPlaneFrustum(true);
    m_programPicking.release();
}

void BatchCircle::setInvViewport(float x, float y) {
    float w = 1.0f / x;
    float h = 1.0f / y;
    QMatrix4x4 windowMatrix;
    windowMatrix.scale(w / 2.0f, h / 2.0f, 1.0f);
    windowMatrix.translate(1.0f, 1.0f);
    m_program.bind();
    m_program.setUniformValue(m_invViewportLoc, x, y);
    m_program.setUniformValue(m_windowMatrixLoc, windowMatrix);
    m_program.release();
    m_programPicking.bind();
    m_programPicking.setUniformValue(m_invViewportPickingLoc, x, y);
    m_programPicking.setUniformValue(m_windowMatrixPickingLoc, windowMatrix);
    m_programPicking.release();
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

void BatchCircle::removeSelectedCircle() {
    if (m_selectedCircle - 1 >= 0 && m_selectedCircle - 1 < m_circles.size()) {
        m_circles.removeAt(m_selectedCircle - 1);
        m_selectedCircle = 0;
    }
    this->updateData();
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

int BatchCircle::renderOrder() {
    return 4;
}

int BatchCircle::pickingOrder() {
    return 0;
}

QVector4D BatchCircle::planeOf(const QVector3D& p0, const QVector3D& p1, const QVector3D& p2, QMatrix4x4 const& invProjView) {
    QVector4D pt0 = invProjView * QVector4D(p0, 1.0);
    QVector4D pt1 = invProjView * QVector4D(p1, 1.0);
    QVector4D pt2 = invProjView * QVector4D(p2, 1.0);
    pt0 /= pt0.w();
    pt1 /= pt1.w();
    pt2 /= pt2.w();
    QVector3D normal = QVector3D::crossProduct(pt1.toVector3D() - pt0.toVector3D(), pt2.toVector3D() - pt0.toVector3D());
    normal.normalize();
    QVector4D plane = normal.toVector4D();
    plane.setW(-QVector3D::dotProduct(normal, pt0.toVector3D()));
    return plane;
}

void BatchCircle::sendUniformsPlaneFrustum(bool picking) {
    QMatrix4x4 inverseProjView = (m_projMatrix * m_viewMatrix).inverted();
    QVector3D mmm { -1, -1, -1 };
    QVector3D mmp { -1, -1, +1 };
    QVector3D mpp { -1, +1, +1 };
    QVector3D pmm { +1, -1, -1 };
    QVector3D pmp { +1, -1, +1 };
    QVector3D ppm { +1, +1, -1 };
    QVector3D ppp { +1, +1, +1 };
    if (picking) {
        m_programPicking.setUniformValue(m_leftPlanePickingLoc, BatchCircle::planeOf(mmp, mmm, mpp, inverseProjView));
        m_programPicking.setUniformValue(m_rightPlanePickingLoc, BatchCircle::planeOf(pmp, ppp, pmm, inverseProjView));
        m_programPicking.setUniformValue(m_topPlanePickingLoc, BatchCircle::planeOf(ppp, mpp, ppm, inverseProjView));
        m_programPicking.setUniformValue(m_bottomPlanePickingLoc, BatchCircle::planeOf(pmp, pmm, mmp, inverseProjView));
    } else {
        m_program.setUniformValue(m_leftPlaneLoc, BatchCircle::planeOf(mmp, mmm, mpp, inverseProjView));
        m_program.setUniformValue(m_rightPlaneLoc, BatchCircle::planeOf(pmp, ppp, pmm, inverseProjView));
        m_program.setUniformValue(m_topPlaneLoc, BatchCircle::planeOf(ppp, mpp, ppm, inverseProjView));
        m_program.setUniformValue(m_bottomPlaneLoc, BatchCircle::planeOf(pmp, pmm, mmp, inverseProjView));
    }
}

int BatchCircle::selectedCircleIndex() const {
    return m_selectedCircle - 1;
}
