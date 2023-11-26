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
    gl_PointSize = 8.0;
    if (isSelected > 0.5) {
        vecColor = vec3(1.0, 1.0, 1.0);
    } else {
        vecColor = color;
    }
}