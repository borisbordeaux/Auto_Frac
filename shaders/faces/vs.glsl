#version 460 core

layout (location = 0) in vec4 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in float ID;
layout (location = 3) in float isSelected;

out vec3 vert;
out vec3 vertNormal;
out float selected;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

void main() {
    vert = vertex.xyz;
    vertNormal = normal;
    selected = isSelected;
    gl_Position = projMatrix * mvMatrix * vertex;
}
