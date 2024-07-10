#version 460 core

in vec4 vertex;
in vec3 normal;

out vec3 vert;
out vec3 vertNormal;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

void main() {
    vert = vertex.xyz;
    vertNormal = normal;
    gl_Position = projMatrix * mvMatrix * vertex;
}
