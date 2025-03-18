#version 460 core

in vec3 vertPos;

out vec4 fragColor;

uniform vec3 lightPos;
uniform vec3 cameraPosition;
uniform uint displayNorth;

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

float checkInCircle(bool testAll) {
    vec3 normalizedPos = normalize(vertPos);
    float nb = 0.0;
    for (uint i = 0; i < nbVertices; i += 3) {
        vec3 pos = vec3(polyhedronVertices[i], polyhedronVertices[i + 1], polyhedronVertices[i + 2]);
        if (dot(normalizedPos, pos) > 1.0) { //test if in circle
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
    if (displayNorth != 0) {
        if (length(normalize(vertPos) - vec3(0.0, 0.0, 1.0)) < 0.02) {
            fragColor = vec4(1.0, 0.0, 0.0, 1.0);
            return;
        }
    }

    vec3 color = vec3(0.65);

    if (renderType == 0) {
        // transparent
        color = vec3(0.5);
        if (checkInCircle(false) > 0.5) {
            discard;
        }
    } else if (renderType == 1) {
        // illuminated regions
        color = vec3(0.5);
        color += checkInCircle(true) * vec3(0.15);
    }

    vec3 ambientColor = 0.6 * color.rgb;
    vec3 diffuseColor = color.rgb;
    vec3 specularColor = vec3(0.2);

    // the normal is the position since vertices are on the unit sphere
    vec3 N = normalize(vertPos);
    vec3 L = normalize(lightPos - vertPos);

    // Lambert's cosine law
    float lambertian = max(dot(N, L), 0.0);

    float specular = 0.0;

    if (lambertian > 0.0) {
        vec3 R = reflect(-L, N);      // Reflected light vector
        vec3 V = normalize(cameraPosition - vertPos); // Vector to viewer
        // Compute the specular term
        float specAngle = max(dot(R, V), 0.0);
        specular = pow(specAngle, 5.0);
    }

    fragColor = vec4(ambientColor + lambertian * diffuseColor + specular * specularColor, 1.0);
}