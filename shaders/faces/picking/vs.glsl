#version 460 core

layout (location = 0) in vec4 vertex;
layout (location = 1) in vec3 normal;
layout (location = 2) in float ID;
layout (location = 3) in float isSelected;

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
