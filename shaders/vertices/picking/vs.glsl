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
    gl_PointSize = 64.0;
    int id = int(ID + 0.2);
    int mask = 255;
    vecColor.z = float(id & mask) / 255.0;
    vecColor.y = float((id >> 8) & mask) / 255.0;
    vecColor.x = float((id >> 16) & mask) / 255.0;
}