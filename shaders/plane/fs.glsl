#version 460 core

in vec3 vertPos;

out vec4 fragColor;

//nb readable floats
uniform uint nbVertices;

layout (std430, binding = 3) readonly buffer polyhedronData
{
    float polyhedronVertices[];
};

float checkInCircle() {
    float nb = 0.0;
    for (uint i = 0; i < nbVertices; i += 4) {
        vec3 center = vec3(polyhedronVertices[i], polyhedronVertices[i + 1], polyhedronVertices[i + 2]);
        float radius = polyhedronVertices[i + 3];
        if (radius > 0) {
            if (length(center - vertPos) < radius) { //test if in circle
                nb += 1.0;
            }
        } else {
            if (length(center - vertPos) > -radius) { //test if in circle
                nb += 1.0;
            }
        }
    }
    return nb;
}

void main() {
    vec3 color = vec3(0.95);

    float nb = checkInCircle();
    if (nb < 0.5){
        discard;
    }
    color -= nb * vec3(0.05);

    fragColor = vec4(color, 1.0);
}