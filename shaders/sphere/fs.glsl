#version 460 core

in vec3 vert;
in vec3 vertNormal;

out vec4 fragColor;

uniform vec3 lightPos;
uniform vec3 cameraPosition;

//nb readable floats
uniform uint nbVertices;

layout(std430, binding = 2) readonly buffer polyhedronData
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
    vec3 fragVertModel = vert;
    vec3 fragNormalModel = vertNormal;
    vec3 L = normalize(lightPos - fragVertModel);
    float diffuse = abs(dot(fragNormalModel, L));
    vec3 R = reflect(-L, fragNormalModel);
    vec3 V = normalize(cameraPosition - fragVertModel);
    float RV = max(dot(R, V), 0.0);
    float specular = pow(RV, 100.0);
    vec3 specularColor = specular * vec3(0.2, 0.2, 0.2);
    vec3 color = vec3(0.6);
    color -= checkInCircle()*vec3(0.1);
    vec3 ambientColor = 0.4 * color;
    vec3 diffuseColor = diffuse * color;
    fragColor = vec4(clamp(specularColor + ambientColor + diffuseColor, 0.0, 1.0), 1.0);
}