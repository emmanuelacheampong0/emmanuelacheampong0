(() => {
  'use strict';
  const canvas = document.querySelector('#sculpture');
  const shell = canvas.parentElement;
  let gl;
  try {gl = canvas.getContext('webgl', {alpha:true, antialias:false, powerPreference:'low-power', preserveDrawingBuffer:false});} catch (_) {}
  const fallback = () => shell.classList.add('no-webgl');
  if (!gl) {fallback(); return;}
  const vertex = 'attribute vec2 pos;void main(){gl_Position=vec4(pos,0.,1.);}';
  const fragment = `precision highp float;
  uniform vec2 resolution; uniform float time; uniform vec2 turn; uniform float shape;
  mat2 rot(float a){float s=sin(a),c=cos(a);return mat2(c,-s,s,c);}
  float torus(vec3 p,vec2 t){vec2 q=vec2(length(p.xz)-t.x,p.y);return length(q)-t.y;}
  float sm(float a,float b,float k){float h=clamp(.5+.5*(b-a)/k,0.,1.);return mix(b,a,h)-k*h*(1.-h);}
  float map(vec3 p){
    p.xz*=rot(turn.x+time*.17);p.yz*=rot(turn.y+.35);
    if(shape<.5){p.xy*=rot(.65);p.xz*=rot(p.y*.58);return torus(p,vec2(.86,.29));}
    if(shape<1.5){float a=torus(p,vec2(.83,.15));p.xy*=rot(1.5708);return sm(a,torus(p,vec2(.83,.15)),.19);}
    float a=length(p-vec3(.48,.1,0.))-.61;float b=length(p+vec3(.38,.17,0.))-.62;
    return sm(sm(a,b,.48),length(p-vec3(-.1,.6,.1))-.45,.35);
  }
  vec3 normal(vec3 p){vec2 e=vec2(.002,0.);return normalize(vec3(map(p+e.xyy)-map(p-e.xyy),map(p+e.yxy)-map(p-e.yxy),map(p+e.yyx)-map(p-e.yyx)));}
  void main(){
    vec2 uv=(gl_FragCoord.xy*2.-resolution)/resolution.y;
    vec3 ro=vec3(0.,0.,3.8),rd=normalize(vec3(uv,-2.25));float distance=0.;vec3 p;float hit=0.;
    for(int i=0;i<64;i++){p=ro+rd*distance;float d=map(p);if(d<.0015){hit=1.;break;}distance+=d*.85;if(distance>6.)break;}
    if(hit<.5){gl_FragColor=vec4(0.);return;}
    vec3 n=normal(p),light=normalize(vec3(-.7,1.,1.5)),view=-rd;
    float diff=max(dot(n,light),0.);float fres=pow(1.-max(dot(n,view),0.),3.);
    float spec=pow(max(dot(n,normalize(light+view)),0.),55.);
    float broad=pow(max(dot(n,normalize(vec3(1.,.5,1.)+view)),0.),12.);
    vec3 violet=vec3(.40,.14,.75),pink=vec3(.91,.55,.68),cyan=vec3(.20,.81,.79);
    vec3 base=mix(violet,pink,smoothstep(-.6,.65,n.y));base=mix(base,cyan,smoothstep(.1,.9,n.x)*.8);
    vec3 color=base*(.3+.73*diff)+vec3(1.)*spec*.95+vec3(.43,.6,.88)*broad*.22+vec3(.55,.77,.92)*fres*.45;
    gl_FragColor=vec4(pow(color,vec3(.86)),1.);
  }`;
  const compile = (type, source) => {
    const shader = gl.createShader(type);gl.shaderSource(shader,source);gl.compileShader(shader);
    if (!gl.getShaderParameter(shader,gl.COMPILE_STATUS)) {gl.deleteShader(shader);return null;}return shader;
  };
  const vs = compile(gl.VERTEX_SHADER,vertex), fs = compile(gl.FRAGMENT_SHADER,fragment);
  if (!vs || !fs) {fallback();return;}
  const program = gl.createProgram();gl.attachShader(program,vs);gl.attachShader(program,fs);gl.linkProgram(program);
  if (!gl.getProgramParameter(program,gl.LINK_STATUS)) {fallback();return;}
  gl.useProgram(program);
  const buffer = gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buffer);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,-1,1,1,-1,1,1]),gl.STATIC_DRAW);
  const pos = gl.getAttribLocation(program,'pos');gl.enableVertexAttribArray(pos);gl.vertexAttribPointer(pos,2,gl.FLOAT,false,0,0);
  const uniforms = Object.fromEntries(['resolution','time','turn','shape'].map(name=>[name,gl.getUniformLocation(program,name)]));
  let moving = !document.body.classList.contains('motion-off'), visible = true, shape = 0, spinX = -.6, spinY = .4, tx = -.6, ty = .4, dragging = false, previousX=0, previousY=0, elapsed=0, last=performance.now(), raf=0;
  const size = () => {
    const r = canvas.getBoundingClientRect(),scale = Math.min(window.devicePixelRatio||1,1.25);
    // Cap ray-marched pixels so the centerpiece stays modest on mobile hardware.
    const fit = Math.min(scale,Math.sqrt(600000/Math.max(1,r.width*r.height)));
    canvas.width = Math.max(1,Math.round(r.width*fit));canvas.height = Math.max(1,Math.round(r.height*fit));
    gl.viewport(0,0,canvas.width,canvas.height);gl.uniform2f(uniforms.resolution,canvas.width,canvas.height);
  };
  const render = now => {
    raf=0;
    const dt=Math.min(50,now-last);last=now;
    if (moving) elapsed+=dt*.001;
    spinX+=(tx-spinX)*.12;spinY+=(ty-spinY)*.12;
    gl.uniform1f(uniforms.time,elapsed);gl.uniform2f(uniforms.turn,spinX,spinY);gl.uniform1f(uniforms.shape,shape);gl.drawArrays(gl.TRIANGLES,0,6);
    if (visible && !document.hidden && (moving || dragging || Math.abs(tx-spinX)+Math.abs(ty-spinY)>.005)) raf=requestAnimationFrame(render);
  };
  const request = () => {if (!raf && visible && !document.hidden) {last=performance.now();raf=requestAnimationFrame(render);}};
  size();request();
  new ResizeObserver(() => {size();request();}).observe(canvas);
  new IntersectionObserver(entries => {visible=entries[0].isIntersecting;if(visible)request();else if(raf){cancelAnimationFrame(raf);raf=0;}}, {threshold:0}).observe(canvas);
  document.addEventListener('visibilitychange',request);
  window.addEventListener('portfolioMotion',event=>{moving=event.detail;request();});
  window.addEventListener('portfolioShape',event=>{shape=event.detail;request();});
  canvas.addEventListener('pointerdown',event=>{dragging=true;previousX=event.clientX;previousY=event.clientY;canvas.classList.add('dragging');canvas.setPointerCapture(event.pointerId);request();});
  canvas.addEventListener('pointermove',event=>{
    if(!dragging)return;tx+=(event.clientX-previousX)*.008;ty+=(event.clientY-previousY)*.008;previousX=event.clientX;previousY=event.clientY;request();
  });
  const stop = () => {dragging=false;canvas.classList.remove('dragging');};
  canvas.addEventListener('pointerup',stop);canvas.addEventListener('pointercancel',stop);canvas.addEventListener('lostpointercapture',stop);
  canvas.addEventListener('webglcontextlost',event=>{event.preventDefault();if(raf)cancelAnimationFrame(raf);fallback();});
})();
