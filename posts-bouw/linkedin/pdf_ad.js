// Carrusel "6 desperdicios" (AD10) en PDF para subir como documento a LinkedIn
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const files = fs.readdirSync('png').filter(f => f.startsWith('AD10-')).sort();
  const html = '<html><body style="margin:0">' + files.map(f => `<img src="file://${process.cwd()}/png/${f}" style="width:1080px;height:1350px;display:block;page-break-after:always">`).join('') + '</body></html>';
  fs.writeFileSync('_ad.html', html);
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.cwd() + '/_ad.html'); await p.waitForTimeout(1500);
  await p.pdf({ path: 'BOUW-carrusel-6-desperdicios.pdf', width: '1080px', height: '1350px', printBackground: true, pageRanges: '1-' + files.length });
  await b.close(); fs.unlinkSync('_ad.html'); console.log(files.length, 'láminas');
})();
