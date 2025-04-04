#version 460 core

in vec3 vecCol;
in float dist;

out vec4 fragColor;

void main() {
    float dashSize = 10.0;
    float gapSize = 10.0;
    if (fract(dist / (dashSize + gapSize)) > dashSize/(dashSize + gapSize)) {
        discard;
    }
    fragColor = vec4(vecCol, 1.0);
}