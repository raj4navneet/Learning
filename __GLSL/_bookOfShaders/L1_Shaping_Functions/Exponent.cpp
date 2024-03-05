// Author: Navneet Rao | Nav
// Title: Exponent

#ifdef GL_ES
precision mediump float;
#endif

#define PI 3.14159265359

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

float plot(vec2 st, float pct)
{
	// subtract and add on both side of the divide to create a line and return it
	return	smoothstep( pct-0.01, pct, st.y) - 
			smoothstep( pct, pct+0.01, st.y);
}

void main() 
{
    // get ST resolution
    vec2 st = gl_FragCoord.xy/u_resolution;
    // get a gradient with POW fnc curve
    float y = pow(st.x, 5.0);
    // Float to Vector
    vec3 COL1 = vec3(y);
    vec3 COL2 = vec3(0.0, 1.0, 0.0);
	// call plot fnc and get a curve
    float A = plot(st,y);
    //The function mix(x, y, a) calculates always x * (1−a) + y * a.
    //vec3 blend = (1.0-A)*COL1 + COL2*A;
    vec3 blend = mix(COL1, COL2, A);
    gl_FragColor = vec4(blend, 1.0);
}
