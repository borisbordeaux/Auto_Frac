#version 460 core

layout (location = 0) in vec4 vertex;
layout (location = 1) in vec3 color;
layout (location = 2) in float dist;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

out vec3 vecColor;
out float distance;

void main() {
    vecColor = color;
    distance = dist;
    gl_Position = projMatrix * mvMatrix * vertex;
}