#version 460 core

layout (vertices = 1) out;

in vec3 vecCenter[];
in float vecRadius[];
in vec3 vecXAxis[];
in vec3 vecYAxis[];
in vec3 vecColor[];

out vec3 center[];
out float radius[];
out vec3 xAxis[];
out vec3 yAxis[];
out vec3 color[];

uniform vec3 cameraPosition;

void main() {
    gl_out[gl_InvocationID].gl_Position = gl_in[gl_InvocationID].gl_Position;
    center[gl_InvocationID] = vecCenter[gl_InvocationID];
    radius[gl_InvocationID] = vecRadius[gl_InvocationID];
    xAxis[gl_InvocationID] = vecXAxis[gl_InvocationID];
    yAxis[gl_InvocationID] = vecYAxis[gl_InvocationID];
    color[gl_InvocationID] = vecColor[gl_InvocationID];

    if (gl_InvocationID == 0) {
        float dist = length(vecCenter[0] - cameraPosition);
        float ratio = vecRadius[0] / dist;
        //radius of 1, dist of 8 => 60 pts
        //if dist +++ then nb ---
        //if radius +++ then nb +++
        int nb = max(3, int(60.0 * 8 * ratio));
        gl_TessLevelOuter[0] = 1.0; // one line to tesselate
        gl_TessLevelOuter[1] = nb; // 10 points per line to be changed in the future
    }
}