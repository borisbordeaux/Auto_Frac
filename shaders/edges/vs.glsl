#version 460 core

layout (location = 0) in vec4 vertex;
layout (location = 1) in vec3 color;
layout (location = 2) in float ID;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

out vec3 vecColor;

void main() {
    gl_Position = projMatrix * mvMatrix * vertex;
    vecColor = color;
}