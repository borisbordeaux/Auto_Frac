#version 460 core

in vec4 vertex;
in vec3 normal;
in float ID;
in float isSelected;

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
