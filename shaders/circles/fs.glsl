#version 460 core

in vec3 vecCol;

out vec4 fragColor;

uniform uint useColors;

void main() {
    if (useColors == 0) {
        fragColor = vec4(vecCol, 1.0);
    } else {
        fragColor = vec4(0.0, 0.0, 0.0, 1.0);
    }
}