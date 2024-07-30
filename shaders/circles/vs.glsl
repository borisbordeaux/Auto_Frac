#version 460 core

in vec4 vertex;
in vec3 color;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

out vec3 vecColor;

void main() {
    gl_Position = projMatrix * mvMatrix * vertex;
    vecColor = color;
}