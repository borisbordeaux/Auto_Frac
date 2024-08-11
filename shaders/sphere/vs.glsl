#version 460 core

in vec4 vertex;

out vec3 vert;
out vec3 vertNormal;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

void main() {
    vert = vertex.xyz;
    vertNormal = vertex.xyz;
    gl_Position = projMatrix * mvMatrix * vertex;
}
