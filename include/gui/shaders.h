#ifndef SHADERS_H
#define SHADERS_H

//vertex shader for faces
static const char* vertexShaderSource = R"(
#version 460 core
in vec4 vertex;
in vec3 normal;
in float ID;
in float isSelected;
out vec3 vert;
out vec3 vertNormal;
out float pickingColor;
out float selected;
uniform mat4 projMatrix;
uniform mat4 mvMatrix;
uniform mat3 normalMatrix;
void main() {
    vert = vertex.xyz;
    vertNormal = normalMatrix * normal;
    pickingColor = ID/255.0;
    selected = isSelected;
    gl_Position = projMatrix * mvMatrix * vertex;
}
)";

//fragment shader for faces
static const char* fragmentShaderSource = R"(
#version 460 core
in highp vec3 vert;
in highp vec3 vertNormal;
in highp float pickingColor;
in highp float selected;
out highp vec4 fragColor;
uniform highp vec3 lightPos;
uniform highp vec3 cameraPosition;
uniform highp mat4 model;
uniform bool isPicking;
void main() {
   if(!isPicking){
      if(selected < 0.5){
         highp vec3 fragVertModel = (model*vec4(vert, 1.0)).xyz;
         highp vec3 fragNormalModel = vertNormal;
         highp vec3 L = normalize(lightPos - fragVertModel);
         highp float diffuse = max(dot(fragNormalModel, L), 0.0);
         highp vec3 R = reflect(-L, fragNormalModel);
         highp vec3 V = normalize(cameraPosition - fragVertModel);
         highp float RV = max(dot(R,V), 0.0);
         highp float specular = pow(RV, 100.0);
         highp vec3 specularColor = specular * vec3(0.3,0.3,0.6);
         highp vec3 color = vec3(0.4, 0.4, 1.0);
         highp vec3 ambientColor = 0.6 * color;
         highp vec3 diffuseColor = diffuse * color;
         fragColor = vec4(clamp(specularColor+ambientColor+diffuseColor, 0.0, 1.0), 1.0);
      }else{
         fragColor = vec4(1.0, 0.3, 0.3, 1.0);
      }
   }else{
      fragColor = vec4(pickingColor, pickingColor, pickingColor, 1.0);
   }
}
)";

//vertex shaders for edges
static const char* vertexShaderSourceEdge = R"(
#version 460 core
in highp vec4 vertex;
in highp vec3 color;
in float ID;
in float isSelected;
uniform highp mat4 projMatrix;
uniform highp mat4 mvMatrix;
uniform bool isPicking;
out highp vec3 vecColor;
void main() {
    gl_Position = projMatrix * mvMatrix * vertex;
    if (isPicking) {
        vecColor = vec3(ID/255.0, ID/255.0, ID/255.0);
    } else if (isSelected > 0.5) {
        vecColor = vec3(1.0, 1.0, 1.0);
    } else {
        vecColor = color;
    }
}
)";

//fragment shader for edges
static const char* fragmentShaderSourceEdge = R"(
#version 460 core
in highp vec3 vecColor;
out highp vec4 fragColor;
void main() {
    fragColor = vec4(vecColor, 1.0);
}
)";

//vertex shaders for vertices
static const char* vertexShaderSourceVertices = R"(
#version 460 core
in highp vec4 vertex;
in highp vec3 color;
in float ID;
in float isSelected;
uniform highp mat4 projMatrix;
uniform highp mat4 mvMatrix;
uniform bool isPicking;
out highp vec3 vecColor;
void main() {
    gl_Position = projMatrix * mvMatrix * vertex;
    if (isPicking) {
        gl_PointSize = 32.0;
    } else {
        gl_PointSize = 8.0;
    }
    if (isPicking) {
        if (ID > 255.0) {
            vecColor.x = 1.0;
            float id = ID - 255.0;
            if (id > 255.0) {
                vecColor.y = 1.0;
                id = id - 255.0;
                vecColor.z = id / 255.0;
            } else {
                vecColor.yz = vec2(id / 255.0, 0.0);
            }
        } else {
            vecColor = vec3(ID / 255.0, 0.0, 0.0);
        }
    } else if (isSelected > 0.5) {
        vecColor = vec3(1.0, 1.0, 1.0);
    } else {
        vecColor = color;
    }
})";

//fragment shader for vertices
static const char* fragmentShaderSourceVertices = R"(
#version 460 core
in highp vec3 vecColor;
out highp vec4 fragColor;
void main() {
    fragColor = vec4(vecColor, 1.0);
}
)";

#endif // SHADERS_H
