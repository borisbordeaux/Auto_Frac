#version 460 core

layout(isolines, fractional_odd_spacing, ccw) in;

in vec3 center[];
in float radius[];
in vec3 xAxis[];
in vec3 yAxis[];
in vec3 color[];

out vec3 vecColor;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

void main() {
    gl_Position = projMatrix * mvMatrix * vec4(center[0], 1.0);
    vecColor = color[0];
}