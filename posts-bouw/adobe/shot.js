const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1700, height: 2000 } });
  for (const d of process.argv.slice(2)) {
    await p.goto('file://' + process.cwd() + '/html/' + d + '.preview.html');
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(400);
    const n = await p.locator('.slide').count();
    for (let i = 0; i < n; i++) {
      await p.locator('.slide').nth(i).screenshot({ path: 'png/' + d + '-' + String(i + 1).padStart(2, '0') + '.png' });
    }
  }
  await b.close();
})();
