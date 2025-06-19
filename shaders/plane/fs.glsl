#version 460 core

in vec2 vertPos;

out vec4 fragColor;

//nb readable floats
uniform uint nbVertices;

uniform uint useColors;

layout (std430, binding = 3) readonly buffer polyhedronData
{
    float polyhedronVertices[]; //2 floats center, 1 float radius, 3 floats color
};

bool checkInCircle() {
    for (uint i = 0; i < nbVertices; i += 6) {
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
    if (useColors == 0) {
        if (nbVertices == 0 || checkInCircle()) {
            discard;
        }
        fragColor = vec4(0.8, 0.8, 0.8, 1.0);
    } else {
        uint nbCircles = 0;
        vec3 blendColor = vec3(0);
        for (uint i = 0; i < nbVertices; i += 6) {
            vec2 center = vec2(polyhedronVertices[i], polyhedronVertices[i + 1]);
            float radius = polyhedronVertices[i + 2];
            if (radius > 0) {
                if (length(center - vertPos) < radius) { //test if in circle
                    blendColor += vec3(polyhedronVertices[i + 3], polyhedronVertices[i + 4], polyhedronVertices[i + 5]);
                    nbCircles += 1;
                }
            } else {
                if (length(center - vertPos) > -radius) { //test if in circle
                    blendColor += vec3(polyhedronVertices[i + 3], polyhedronVertices[i + 4], polyhedronVertices[i + 5]);
                    nbCircles += 1;
                }
            }
        }
        if (nbCircles == 0) {
            discard;
        } else {
            fragColor = vec4(blendColor / float(nbCircles), 1.0);
        }
    }
}