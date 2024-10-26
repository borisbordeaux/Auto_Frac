#version 460 core

in vec3 vert;
in vec3 vertNormal;

out vec4 fragColor;

uniform vec3 lightPos;
uniform vec3 cameraPosition;

//nb readable floats
uniform uint nbVertices;

layout (std430, binding = 2) readonly buffer polyhedronData
{
    float polyhedronVertices[];
};

bool isInCircleInducedBy(vec3 vertexPosition) {
    return dot(vert, vertexPosition) > 1.0;
}

float checkInCircle() {
    float nb = 0.0;
    for (uint i = 0; i < nbVertices; i += 3) {
        vec3 pos = vec3(polyhedronVertices[i], polyhedronVertices[i + 1], polyhedronVertices[i + 2]);
        if (isInCircleInducedBy(pos)) {
            nb += 1.0;
        }
    }
    return nb;
}

void main() {
    /*if(checkInCircle() > 0.5){
        discard;
    }*/

    vec3 color = vec3(0.5);
    color -= checkInCircle() * vec3(0.1);

    vec3 ambientColor = 0.7 * color.rgb;
    vec3 diffuseColor = color.rgb;

    vec3 N = normalize(vertNormal);
    vec3 L = normalize(lightPos - vert);

    // Lambert's cosine law
    float lambertian = max(dot(N, L), 0.0);
    fragColor = vec4(ambientColor + lambertian * diffuseColor, 1.0);
}