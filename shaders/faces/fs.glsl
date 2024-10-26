#version 460 core

in vec3 vert;
in vec3 vertNormal;
in float selected;

out vec4 fragColor;

uniform vec3 lightPos;
uniform vec3 cameraPosition;
uniform vec4 color;

void main() {
    if (selected < 0.5) {
        vec3 ambientColor = 0.3 * color.rgb;
        vec3 diffuseColor = color.rgb;
        vec3 specularColor = vec3(1.0);
        vec3 N = normalize(vertNormal);
        vec3 L = normalize(lightPos - vert);

        // Lambert's cosine law
        float lambertian = max(dot(N, L), 0.0);
        float specular = 0.0;
        if (lambertian > 0.0) {
            vec3 R = reflect(-L, N);      // Reflected light vector
            vec3 V = normalize(cameraPosition - vert); // Vector to viewer
            // Compute the specular term
            float specAngle = max(dot(R, V), 0.0);
            specular = pow(specAngle, 20.0);
        }
        fragColor = vec4(ambientColor + lambertian * diffuseColor + specular * specularColor, color.a);
        //fragColor = vec4(ambientColor + lambertian * diffuseColor, color.a);
    } else {
        fragColor = vec4(1.0, 0.3, 0.3, 2.0 * color.a);
    }
}