#version 460 core

in vec3 vertPos;

out vec4 fragColor;

uniform vec3 lightPos;
uniform vec3 cameraPosition;

// 0 : transparent
// 1 : illuminated regions
// 2 : no specific coloring
uniform int renderType;

//nb readable floats
uniform uint nbVertices;

layout (std430, binding = 2) readonly buffer polyhedronData
{
    float polyhedronVertices[];
};

bool isInCircleInducedBy(vec3 vertexPosition) {
    return dot(vertPos, vertexPosition) > 1.0;
}

float checkInCircle(bool testAll) {
    float nb = 0.0;
    for (uint i = 0; i < nbVertices; i += 3) {
        vec3 pos = vec3(polyhedronVertices[i], polyhedronVertices[i + 1], polyhedronVertices[i + 2]);
        if (isInCircleInducedBy(pos)) {
            if (testAll) {
                nb += 1.0;
            } else {
                return 1.0;
            }
        }
    }
    return nb;
}

void main() {
    vec3 color = vec3(0.5);

    if (renderType == 0) {
        // transparent
        if (checkInCircle(false) > 0.5) {
            discard;
        }
    } else if (renderType == 1) {
        // illuminated regions
        color -= checkInCircle(true) * vec3(0.05);
    }

    vec3 ambientColor = 0.7 * color.rgb;
    vec3 diffuseColor = color.rgb;

    // the normal is the position since vertices are on the unit sphere
    // vec3 N = normalize(vertNormal);
    vec3 L = normalize(lightPos - vertPos);

    // Lambert's cosine law
    // float lambertian = max(dot(N, L), 0.0);
    float lambertian = max(dot(vertPos, L), 0.0);
    fragColor = vec4(ambientColor + lambertian * diffuseColor, 1.0);
}