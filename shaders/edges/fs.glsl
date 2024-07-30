#version 460 core

in vec3 vecColor;

out vec4 fragColor;

void main() {
    fragColor = vec4(vecColor, 1.0);
}