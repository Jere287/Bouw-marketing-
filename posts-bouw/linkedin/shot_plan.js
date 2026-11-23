const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 1.5 });
  await p.goto('file://' + process.cwd() + '/html_plan.html'); await p.waitForTimeout(600);
  await p.screenshot({ path: 'PLAN-SEMANAL/PLAN-SEMANAL.png', fullPage: true });
  await b.close();
})();
