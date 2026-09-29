// Renderiza cada <section id> de posts.html a PNG con su tamaño propio.
// Uso: NODE_PATH=$(npm root -g) node render.js
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const out = path.join(__dirname, 'png');
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1800, height: 2100 } });
  await page.goto('file://' + path.join(__dirname, 'posts.html'));
  await page.evaluate(() => document.fonts.ready);
  for (const el of await page.$$('section[id]')) {
    const id = await el.getAttribute('id');
    await el.screenshot({ path: path.join(out, `${id}.png`) });
    console.log('ok', id);
  }
  await browser.close();
})();
