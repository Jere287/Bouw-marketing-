// Renderiza html/<pieza>.html a png/<pieza>.png al tamaño exacto
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  fs.mkdirSync('png', { recursive: true });
  const list = fs.readFileSync('html/list.txt', 'utf8').trim().split('\n');
  for (const row of list) {
    const [name, size] = row.split(':');
    const [w, h] = size.split('x').map(Number);
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + process.cwd() + '/html/' + name + '.html');
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(150);
    await p.screenshot({ path: 'png/' + name + '.png', clip: { x: 0, y: 0, width: w, height: h } });
    await p.close();
  }
  await b.close();
})();
