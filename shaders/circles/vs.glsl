#version 460 core

in vec3 center;
in float radius;
in vec3 xAxis;
in vec3 yAxis;
in vec3 color;
in float ID;

out vec3 vecCenter;
out float vecRadius;
out vec3 vecXAxis;
out vec3 vecYAxis;
out vec3 vecColor;

void main() {
    gl_Position = vec4(center, 1.0);
    vecCenter = center;
    vecRadius = radius;
    vecXAxis = xAxis;
    vecYAxis = yAxis;
    vecColor = color;
}
