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
out vec3 pickingColor;
out float selected;
uniform mat4 projMatrix;
uniform mat4 mvMatrix;
uniform mat3 normalMatrix;
void main() {
    vert = vertex.xyz;
    vertNormal = normalMatrix * normal;
    int id = int(ID + 0.2);
    int mask = 255;
    pickingColor.z = float(id & mask) / 255.0;
    pickingColor.y = float((id >> 8) & mask) / 255.0;
    pickingColor.x = float((id >> 16) & mask) / 255.0;
    selected = isSelected;
    gl_Position = projMatrix * mvMatrix * vertex;
}
)";

//fragment shader for faces
static const char* fragmentShaderSource = R"(
#version 460 core
in highp vec3 vert;
in highp vec3 vertNormal;
in highp vec3 pickingColor;
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
      fragColor = vec4(pickingColor, 1.0);
   }
}
)";

//vertex shaders for edges
static const char* vertexShaderSourceEdge = R"(
#version 460 core
in vec4 vertex;
in vec3 color;
in float ID;
in float isSelected;
uniform mat4 projMatrix;
uniform mat4 mvMatrix;
uniform bool isPicking;
out vec3 vecColor;
void main() {
    gl_Position = mvMatrix * vertex;
    if (isPicking) {
        int id = int(ID + 0.2);
        int mask = 255;
        vecColor.z = float(id & mask) / 255.0;
        vecColor.y = float((id >> 8) & mask) / 255.0;
        vecColor.x = float((id >> 16) & mask) / 255.0;
    } else if (isSelected > 0.0) {
        vecColor = vec3(1.0, 1.0, 1.0);
    } else {
        vecColor = color;
    }
}
)";

//geometry shader for edges when picking
static const char* geometryShader = R"(
#version 460 core
layout (lines) in;
layout (triangle_strip, max_vertices = 4) out;
in vec3 vecColor[];
out highp vec3 vecCol;
uniform mat4 projMatrix;
uniform mat4 mvMatrix;
void main()
{
    vecCol = vecColor[0];
    float r = 0.01;
    vec4 p1 = gl_in[0].gl_Position;
    vec4 p2 = gl_in[1].gl_Position;
    vec2 dir = normalize(p2.xy - p1.xy);
    vec2 normal = vec2(dir.y, -dir.x);
    vec4 offset1, offset2;
    offset1 = vec4(normal * r, 0, 0);
    offset2 = vec4(normal * r, 0, 0);
    vec4 coords[4];
    coords[0] = p1 + offset1;
    coords[1] = p1 - offset1;
    coords[2] = p2 + offset2;
    coords[3] = p2 - offset2;
    for (int i = 0; i < 4; ++i) {
        coords[i] = projMatrix * coords[i];
        gl_Position = coords[i];
        EmitVertex();
    }
    EndPrimitive();
}
)";

//fragment shader for edges
static const char* fragmentShaderSourceEdge = R"(
#version 460 core
//in vec3 vecCol;
out vec4 fragColor;
void main() {
    //fragColor = vec4(vecCol, 1.0);
    fragColor = vec4(1.0);
}
)";

//vertex shaders for vertices
static const char* vertexShaderSourceVertices = R"(
#version 460 core
in vec4 vertex;
in vec3 color;
in float ID;
in float isSelected;
uniform mat4 projMatrix;
uniform mat4 mvMatrix;
uniform bool isPicking;
out vec3 vecColor;
void main() {
    gl_Position = projMatrix * mvMatrix * vertex;
    if (isPicking) {
        gl_PointSize = 64.0;
        int id = int(ID + 0.2);
        int mask = 255;
        vecColor.z = float(id & mask) / 255.0;
        vecColor.y = float((id >> 8) & mask) / 255.0;
        vecColor.x = float((id >> 16) & mask) / 255.0;
    } else {
        gl_PointSize = 8.0;
        if (isSelected > 0.5) {
            vecColor = vec3(1.0, 1.0, 1.0);
        } else {
            vecColor = color;
        }
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
