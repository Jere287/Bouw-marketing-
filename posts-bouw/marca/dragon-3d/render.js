const {chromium}=require('playwright');const fs=require('fs');const http=require('http');const path=require('path');
const dir=__dirname;const jobs=JSON.parse(process.argv[2]);const size=+process.argv[3]||1200;
const srv=http.createServer((q,r)=>{const f=path.join(dir,decodeURIComponent(q.url.split('?')[0]));const t={'.js':'text/javascript','.html':'text/html','.glb':'model/gltf-binary'}[path.extname(f)]||'application/octet-stream';fs.readFile(f,(e,b)=>{if(e){r.writeHead(404);r.end();return}r.writeHead(200,{'content-type':t});r.end(b)})}).listen(8765,async()=>{
const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage();p.on('console',m=>console.log('LOG',m.text()));p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('http://localhost:8765/r.html');await p.waitForFunction('window.READY',null,{timeout:120000});
console.log(await p.evaluate('window.ANIMS'));
for(const j of jobs){const u=await p.evaluate(o=>window.shot(o),{...j,size});fs.writeFileSync(path.join(dir,'out',j.name+'.png'),Buffer.from(u.split(',')[1],'base64'));console.log('ok',j.name)}
await b.close();srv.close();});
