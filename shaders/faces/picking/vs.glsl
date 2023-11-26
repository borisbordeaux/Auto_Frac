#version 460 core

in vec4 vertex;
in vec3 normal;
in float ID;
in float isSelected;

out vec3 pickingColor;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

void main() {
    int id = int(ID + 0.2);
    int mask = 255;
    pickingColor.z = float(id & mask) / 255.0;
    pickingColor.y = float((id >> 8) & mask) / 255.0;
    pickingColor.x = float((id >> 16) & mask) / 255.0;
    gl_Position = projMatrix * mvMatrix * vertex;
}
