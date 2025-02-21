#version 460 core

in vec2 vertPos;

out vec4 fragColor;

//nb readable floats
uniform uint nbVertices;

layout (std430, binding = 3) readonly buffer polyhedronData
{
    float polyhedronVertices[];
};

bool checkInCircle() {
    float nb = 0.0;
    for (uint i = 0; i < nbVertices; i += 3) {
        vec2 center = vec2(polyhedronVertices[i], polyhedronVertices[i + 1]);
        float radius = polyhedronVertices[i + 2];
        if (radius > 0) {
            if (length(center - vertPos) < radius) { //test if in circle
                return true;
            }
        } else {
            if (length(center - vertPos) > -radius) { //test if in circle
                return true;
            }
        }
    }
    return false;
}

void main() {
    if (nbVertices == 0 || checkInCircle()) {
        discard;
    }

    fragColor = vec4(0.8, 0.8, 0.8, 1.0);
}