#version 460 core

in vec3 vert;
in vec3 vertNormal;
in float selected;

out vec4 fragColor;

uniform vec3 lightPos;
uniform vec3 cameraPosition;

void main() {
    if (selected < 0.5) {
        vec3 fragVertModel = vert;
        vec3 fragNormalModel = vertNormal;
        vec3 L = normalize(lightPos - fragVertModel);
        float diffuse = abs(dot(fragNormalModel, L));
        vec3 R = reflect(-L, fragNormalModel);
        vec3 V = normalize(cameraPosition - fragVertModel);
        float RV = max(dot(R, V), 0.0);
        float specular = pow(RV, 100.0);
        vec3 specularColor = specular * vec3(0.99, 0.1, 0.1);
        vec3 color = vec3(0.36, 0.64, 0.89);
        vec3 ambientColor = 0.4 * color;
        vec3 diffuseColor = diffuse * color;
        fragColor = vec4(clamp(specularColor + ambientColor + diffuseColor, 0.0, 1.0), 0.4);
    } else {
        fragColor = vec4(1.0, 0.3, 0.3, 0.4);
    }
}