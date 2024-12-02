#version 460 core
#define PI 3.1415926535897932384626433832795

layout(isolines, equal_spacing, ccw) in;

in vec3 center[];
in float radius[];
in vec3 xAxis[];
in vec3 yAxis[];
in vec3 color[];

out vec3 vecColor;

uniform mat4 projMatrix;
uniform mat4 mvMatrix;

void main() {
    float n = gl_TessLevelOuter[0]; //nb of tessellated lines
    float alpha = (gl_TessCoord.x + n * gl_TessCoord.y) * 2.0 * PI / n;
    vec3 vertPos = center[0] + radius[0] * (cos(alpha) * xAxis[0] + sin(alpha) * yAxis[0]);
    gl_Position = projMatrix * mvMatrix * vec4(vertPos, 1.0);
    vecColor = color[0];
}