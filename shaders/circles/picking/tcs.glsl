#version 460 core
#define PI 3.1415926535897932384626433832795

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

uniform mat4 projMatrix;
uniform mat4 mvMatrix;
uniform mat4 windowMatrix;
uniform vec4 leftPlane;
uniform vec4 rightPlane;
uniform vec4 topPlane;
uniform vec4 bottomPlane;

bool checkInFrustum() {
    // implementation of sphere/frustum intersection test:
    // https://github.com/gszauer/GamePhysicsCookbook/blob/master/Code/Geometry3D.cpp#L1874
    // test if it is completely outside one face (distance to plane)
    // if so, then it is outside
    // we check only left, right, top & bottom planes
    // it is largely enough to have a gain in performance

    bool insideLeftPlane = dot(center[gl_InvocationID], leftPlane.xyz) + leftPlane.w < radius[gl_InvocationID];
    bool insideRightPlane = dot(center[gl_InvocationID], rightPlane.xyz) + rightPlane.w < radius[gl_InvocationID];
    bool insideTopPlane = dot(center[gl_InvocationID], topPlane.xyz) + topPlane.w < radius[gl_InvocationID];
    bool insideBottomPlane = dot(center[gl_InvocationID], bottomPlane.xyz) + bottomPlane.w < radius[gl_InvocationID];

    return insideLeftPlane && insideRightPlane && insideTopPlane && insideBottomPlane;
}

void main() {
    gl_out[gl_InvocationID].gl_Position = gl_in[gl_InvocationID].gl_Position;
    center[gl_InvocationID] = vecCenter[gl_InvocationID];
    radius[gl_InvocationID] = vecRadius[gl_InvocationID];
    xAxis[gl_InvocationID] = vecXAxis[gl_InvocationID];
    yAxis[gl_InvocationID] = vecYAxis[gl_InvocationID];
    color[gl_InvocationID] = vecColor[gl_InvocationID];

    if (gl_InvocationID == 0) {

        bool inFrustum = checkInFrustum();

        if (inFrustum) {
            //center in window coordinates
            vec4 clipCenter = projMatrix * mvMatrix * vec4(center[0], 1.0);
            vec4 ndcCenter = clipCenter / clipCenter.w;
            vec4 vpcCenter = windowMatrix * ndcCenter;

            //point at the X axis of the circle in window coordinates
            vec4 clipPointX = projMatrix * mvMatrix * vec4(center[0] + radius[0] * xAxis[0], 1.0);
            vec4 ndcPointX = clipPointX / clipPointX.w;
            vec4 vpcPointX = windowMatrix * ndcPointX;

            //point at the Y axis of the circle in window coordinates
            vec4 clipPointY = projMatrix * mvMatrix * vec4(center[0] + radius[0] * yAxis[0], 1.0);
            vec4 ndcPointY = clipPointY / clipPointY.w;
            vec4 vpcPointY = windowMatrix * ndcPointY;

            //radius in pixels
            float vpcRadius = max(length(vpcCenter - vpcPointX), length(vpcCenter - vpcPointY));

            //number of lines is a quarter of the perimeter length in pixels
            int nb = max(3, int(PI * vpcRadius / 2.0));

            //number of lines to tessellate (max 64)
            gl_TessLevelOuter[0] = min(64, nb / 64 + 1);

            //number of segments per line, same amount for each line (max 64)
            gl_TessLevelOuter[1] = min(64, nb / gl_TessLevelOuter[0]);
        } else {
            //number of lines to tessellate
            gl_TessLevelOuter[0] = 1.0;
            //number of segments per line
            gl_TessLevelOuter[1] = 3;
        }
    }
}