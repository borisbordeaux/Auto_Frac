#version 460 core

in vec3 vecColor;
in float distance;

out vec4 fragColor;

void main() {
    float dashSize = 10.0;
    float gapSize = 10.0;
    if (fract(distance / (dashSize + gapSize)) > dashSize/(dashSize + gapSize)) {
        discard;
    }
    fragColor = vec4(vecColor, 1.0);
}