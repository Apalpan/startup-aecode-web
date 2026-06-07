// QA opcional: valida estructura del index.html y toma screenshots reales.
// Uso: node _qa.js   (requiere @playwright/mcp o playwright instalado + chromium)
const fs = require('fs');
const path = require('path');

const h = fs.readFileSync('index.html', 'utf8');

// 1) sintaxis del JS inline
const m = h.match(/<script>([\s\S]*)<\/script>/);
try { new Function(m[1]); console.log('JS syntax: OK'); }
catch (e) { console.log('JS syntax ERROR:', e.message); }

// 2) balance de tags
for (const t of ['section','article','div','header','footer','main','aside','ul','li','button']) {
  const o = (h.match(new RegExp('<' + t + '[ >]', 'g')) || []).length;
  const c = (h.match(new RegExp('</' + t + '>', 'g')) || []).length;
  console.log(`tag ${t}: ${o}/${c} ${o === c ? 'OK' : 'MISMATCH'}`);
}

// 3) assets
for (const a of ['aecode-logo.svg','aecodito.png']) console.log(`asset ${a}: ${fs.existsSync(a) ? 'exists' : 'MISSING'}`);

// 4) screenshots
(async () => {
  let chromium;
  const APP = process.env.APPDATA || '';
  for (const c of ['playwright',
                   path.join(APP, 'npm', 'node_modules', '@playwright', 'mcp', 'node_modules', 'playwright'),
                   path.join(APP, 'npm', 'node_modules', 'playwright')]) {
    try { ({ chromium } = require(c)); break; } catch {}
  }
  if (!chromium) return console.log('playwright no encontrado — instala con: npx playwright install chromium');

  // localizar un chromium cacheado (cualquier build) si el default no coincide
  let exe;
  try {
    const base = path.join(process.env.LOCALAPPDATA || '', 'ms-playwright');
    const dir = fs.readdirSync(base).filter(d => d.startsWith('chromium-')).sort().pop();
    const p = path.join(base, dir, 'chrome-win64', 'chrome.exe');
    if (fs.existsSync(p)) exe = p;
  } catch {}

  let browser;
  try { browser = await chromium.launch(exe ? { executablePath: exe } : {}); }
  catch (e) { return console.log('launch falló:', e.message, '\n→ npx playwright install chromium'); }

  const url = 'file://' + path.resolve('index.html').replace(/\\/g, '/');
  const errors = [];
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
  const page = await ctx.newPage();
  page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1800);
  await page.screenshot({ path: '_qa_desktop_top.png' });
  await page.evaluate(() => document.getElementById('metricas').scrollIntoView());
  await page.waitForTimeout(1200);
  await page.screenshot({ path: '_qa_desktop_metrics.png' });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1500);
  await page.screenshot({ path: '_qa_mobile_top.png' });
  console.log('console errors:', errors.length ? errors : 'none');
  await browser.close();
})();
