#version 460 core

in vec4 vertex;
in vec3 color;
in float dist;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

out vec3 vecColor;
out float distance;

void main() {
    vecColor = color;
    distance = dist;
    gl_Position = projMatrix * mvMatrix * vertex;
}