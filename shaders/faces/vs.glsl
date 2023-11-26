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
uniform mat3 normalMatrix;

void main() {
    vert = vertex.xyz;
    vertNormal = normalMatrix * normal;
    selected = isSelected;
    gl_Position = projMatrix * mvMatrix * vertex;
}
