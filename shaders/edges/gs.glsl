#version 460 core

layout (lines) in;
layout (triangle_strip, max_vertices = 4) out;

in vec3 vecColor[];

out vec3 vecCol;

uniform vec2 invViewport;

void main()
{
    vecCol = vecColor[0];
    float r = 1.5;
    vec4 p1 = gl_in[0].gl_Position;
    vec4 p2 = gl_in[1].gl_Position;
    vec2 dir = normalize(p2.xy - p1.xy);
    vec2 normal = vec2(dir.y, -dir.x);
    vec4 offset1, offset2;
    offset1 = vec4(normal * invViewport * r * p1.w, 0, 0);
    offset2 = vec4(normal * invViewport * r * p2.w, 0, 0);
    vec4 coords[4];
    coords[0] = p1 + offset1;
    coords[1] = p1 - offset1;
    coords[2] = p2 + offset2;
    coords[3] = p2 - offset2;
    for (int i = 0; i < 4; ++i) {
        gl_Position = coords[i];
        EmitVertex();
    }
    EndPrimitive();
}