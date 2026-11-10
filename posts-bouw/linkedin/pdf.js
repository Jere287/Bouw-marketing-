// Une las 6 láminas del carrusel en un PDF (LinkedIn lo publica como "documento")
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const files = fs.readdirSync('png').filter(f => /^C\d\d-/.test(f)).sort();
  const imgs = files.map(f => `<img src="file://${process.cwd()}/png/${f}" style="width:1080px;height:1350px;display:block;page-break-after:always">`).join('');
  fs.writeFileSync('html/_carrusel.html', `<html><body style="margin:0">${imgs}</body></html>`);
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.cwd() + '/html/_carrusel.html'); await p.waitForTimeout(400);
  await p.pdf({ path: 'BOUW-carrusel-4-campos.pdf', width: '1080px', height: '1350px', printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
  await b.close();
})();
