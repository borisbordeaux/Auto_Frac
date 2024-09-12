#version 460 core

in vec4 vertex;
in vec3 color;
in float ID;
in float isSelected;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

out vec3 vecColor;

void main() {
    gl_Position = projMatrix * mvMatrix * vertex;
    if (isSelected > 0.0) {
        vecColor = vec3(0.0, 0.6, 0.0);
    } else {
        vecColor = color;
    }
}