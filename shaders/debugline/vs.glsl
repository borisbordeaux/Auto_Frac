#version 460 core

layout (location = 0) in vec4 vertex;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

out vec3 vecColor;

void main() {
    gl_Position = projMatrix * mvMatrix * vertex;
    vecColor = vec3(0.0, 0.0, 1.0);
}