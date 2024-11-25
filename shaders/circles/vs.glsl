#version 460 core

layout (location = 0) in vec3 center;
layout (location = 1) in float radius;
layout (location = 2) in vec3 xAxis;
layout (location = 3) in vec3 yAxis;
layout (location = 4) in vec3 color;
layout (location = 5) in float ID;

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
