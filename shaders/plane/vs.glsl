#version 460 core

layout (location = 0) in vec4 vertex;

out vec2 vertPos;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

void main() {
    vertPos = vertex.xy;
    gl_Position = projMatrix * mvMatrix * vertex;
}
