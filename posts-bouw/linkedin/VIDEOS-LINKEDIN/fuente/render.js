const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const B=process.argv[2];
(async()=>{const b=await chromium.launch();
for(const k of fs.readdirSync(B)){const d=path.join(B,k);const cfg=JSON.parse(fs.readFileSync(d+'/cfg.json'));const [vx,vy,vw,vh]=cfg.box;
 for(const f of fs.readdirSync(d).filter(x=>x.endsWith('.html'))){const n=f.replace('.html','');
  let w=1080,h=1350; if(n=='mask'){w=vw;h=vh} if(n=='bar'){w=936;h=6}
  const p=await b.newPage({viewport:{width:w,height:h}});await p.goto('file://'+d+'/'+f);
  await p.evaluate(()=>document.fonts.ready);await p.evaluate(()=>Promise.all([...document.images].map(i=>i.complete?1:new Promise(r=>{i.onload=i.onerror=r}))));
  await p.screenshot({path:d+'/'+n+'.png',omitBackground:n!='mask',clip:{x:0,y:0,width:w,height:h}});await p.close();}}
await b.close();})();
