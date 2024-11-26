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

bool checkInFrustum() {
    // implementation of sphere/frustum intersection test:
    // https://github.com/gszauer/GamePhysicsCookbook/blob/master/Code/Geometry3D.cpp#L1874
    // test if it is completely outside one face (distance to plane)
    // if so, then it is outside, else it might be inside
    // so test if min distance to corners is < to radius
    // if so, then it is inside, else it is outside
    vec4 p001 = inverse(projMatrix * mvMatrix) * vec4(-1.0, -1.0,  1.0, 1.0); p001 /= p001.w;
    vec4 p011 = inverse(projMatrix * mvMatrix) * vec4(-1.0,  1.0,  1.0, 1.0);
    vec4 p101 = inverse(projMatrix * mvMatrix) * vec4( 1.0, -1.0,  1.0, 1.0);
    vec4 p111 = inverse(projMatrix * mvMatrix) * vec4( 1.0,  1.0,  1.0, 1.0);
    vec4 p000 = inverse(projMatrix * mvMatrix) * vec4(-1.0, -1.0, -1.0, 1.0);
    vec4 p010 = inverse(projMatrix * mvMatrix) * vec4(-1.0,  1.0, -1.0, 1.0);
    vec4 p100 = inverse(projMatrix * mvMatrix) * vec4( 1.0, -1.0, -1.0, 1.0);
    vec4 p110 = inverse(projMatrix * mvMatrix) * vec4( 1.0,  1.0, -1.0, 1.0);
    // get all coords of the frustum
    // c_world = inverse(projMatrix * mvMatrix) * vec4(c_ncd, 1);
    // c_world /= c_world / c_world.w;
    // get all normals of the planes
    // check scalar product with all plane normals
    return true;
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

        int nb = 1;

        if (inFrustum){
            //center in window coordinates
            vec4 clipCenter = projMatrix * mvMatrix * vec4(center[0], 1.0);
            vec4 ndcCenter = clipCenter / clipCenter.w;
            vec4 vpcCenter = windowMatrix * ndcCenter;

            //north of the circle in window coordinates
            vec4 clipNorth = projMatrix * mvMatrix * vec4(center[0] + radius[0] * xAxis[0], 1.0);
            vec4 ndcNorth = clipNorth / clipNorth.w;
            vec4 vpcNorth = windowMatrix * ndcNorth;

            //radius in pixels
            float vpcRadius = length(vpcCenter - vpcNorth);

            //arbitrary number of lines for the circle corresponding to its perimeter length in pixels
            nb = max(nb, 2 * int(PI * vpcRadius));
        }

        gl_TessLevelOuter[0] = 3.0;//lines to tessellate
        gl_TessLevelOuter[1] = nb;
    }
}