#version 460 core

in vec3 pickingColor;

out vec4 fragColor;

void main() {
    fragColor = vec4(pickingColor, 1.0);
}