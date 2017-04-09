precision mediump float;

varying vec2 uv;

uniform sampler2D tex0;
uniform sampler2D tex1;
uniform vec3 unif[20];

void main(void){

  // Extract uniforms.
  float w = unif[15][0];
  float h = unif[15][1];
  float time = unif[16][0];
  vec2 res = vec2(w,h);
  vec4 c = texture2D(tex0, uv);
  
  vec2 aspect = res/min(w,h);
  vec2 uvscaled = uv/res;

  vec2 p = (uvscaled - .5) *aspect;

  float sf = 3.0;
  vec4 rv = texture2D(tex1, uv*sf + sf*time/200.0);
  vec4 gv = texture2D(tex1, uv*sf - sf*time/199.0);
  vec4 bv = texture2D(tex1, uv*sf + sf*time/20.0);

  vec4 n = vec4(rv.x,gv.y,bv.z,1.0);


  gl_FragColor = mix(n ,c, 0.9);
  gl_FragColor.a = unif[5][2];
}
