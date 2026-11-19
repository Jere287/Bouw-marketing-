const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.cwd() + '/html_plan_doc.html'); await p.waitForTimeout(500);
  await p.pdf({ path: 'PLAN-SEMANAL/PLAN-SEMANAL.pdf', format: 'A4', printBackground: true, margin: { top: '16mm', bottom: '16mm', left: '14mm', right: '14mm' } });
  await b.close();
})();
