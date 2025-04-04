#version 460 core

layout (location = 0) in vec4 vertex;
layout (location = 1) in vec3 color;
layout (location = 2) in float dist;
layout (location = 3) in float ID;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

out vec3 vecColor;
out float distance;

void main() {
    distance = dist;
    gl_Position = projMatrix * mvMatrix * vertex;
    int id = int(ID + 0.2);
    int mask = 255;
    vecColor.z = float(id & mask) / 255.0;
    vecColor.y = float((id >> 8) & mask) / 255.0;
    vecColor.x = float((id >> 16) & mask) / 255.0;
}