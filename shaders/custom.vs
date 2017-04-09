#include std_head_vs.inc

varying vec3 lightVector;
varying float dist;
varying float lightFactor;

float rand(vec2 co){
  return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
}

void main(void) {
  vec3 normout;
#include std_main_vs.inc

  vec3 inray = vec3(relPosn - vec4(unif[6], 0.0)); // ----- vector from the camera to this vertex
  dist = length(inray);
  
  float time = unif[16][0];
  float curr = (sin(time) + 1.0)*0.5*10.0;
  float diff = abs(mod(vertex.y*400.0,10.0) - curr)/3.0;

  float z = mod(vertex.y + time*3.0, 4.0);
  float x = mod(vertex.z + time*3.0, 4.0);
  float r1seed = floor(time*10.0)/10.0;
  float r1 = rand(vec2(r1seed, r1seed*r1seed));
  gl_Position = modelviewmatrix[1] * vec4(vertex,1.0)
  // Glitching is fun.
  + vec4(
  	(r1 + 0.5)*0.8*step(19.8, mod(time - 1.0,20.0))*2.0*sin(x*(3.5 + 0.5*r1))/x,
  	0.0,
  	0.0,
  	(r1 + 0.5)*step(34.5, mod(time,35.0))*2.0*sin(z*4.)/z
  	);
  gl_PointSize = unib[2][2] / dist;
}