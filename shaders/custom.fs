#include std_head_fs.inc

varying vec3 lightVector;
varying float dist;
varying float lightFactor;

void main(void) {
#include std_main_mat.inc
#include std_light.inc
  float time = unif[16][0];
  gl_FragColor =  (1.0 - ffact) * texc + ffact * vec4(unif[4], unif[5][1]); // ------ combine using factors
  gl_FragColor.r = (sin(time/8.0) + 1.0)*0.5;
  gl_FragColor.g = (sin(time/7.0) + 1.0)*0.5*gl_FragColor.g;
  //gl_FragColor.b = (sin(time/7.3) + 1.0)*0.5*gl_FragColor.b;
  gl_FragColor.a *= unif[5][2];
}
