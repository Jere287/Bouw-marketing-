const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();fs.mkdirSync('png',{recursive:true});
for(const f of fs.readdirSync('html_antes_despues').filter(f=>f.endsWith('.html'))){
 const n=f.replace('.html','');const p=await b.newPage({viewport:{width:1080,height:1350}});
 await p.goto('file://'+process.cwd()+'/html_antes_despues/'+f);
 await p.evaluate(()=>document.fonts.ready);
 await p.evaluate(()=>Promise.all([...document.images].map(i=>i.complete?1:new Promise(r=>{i.onload=i.onerror=r}))));
 await p.waitForTimeout(150);await p.screenshot({path:'png/'+n+'.png'});await p.close();console.log(n)}
await b.close()})();
