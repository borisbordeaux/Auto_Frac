#version 460 core

layout (location = 0) in vec4 vertex;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

void main() {
    gl_Position = projMatrix * mvMatrix * vertex;
}