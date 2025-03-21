#version 460 core

in vec3 vecCol;

out vec4 fragColor;

void main() {
    fragColor = vec4(vecCol, 1.0);
}