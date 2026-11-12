// Layout QA with Playwright: horizontal overflow, empty vertical gaps, left-rail position, screenshots.
// Usage: node tools/shots.js [--shots] [--pages /,/books/] [--widths 390,768,1024,1440,1920]
// Serves dist/ itself on a free port. Amazon cover images are blocked in the sandbox, so covers
// show their colored title fallback (which is also how we prove the fallback works).
const { chromium } = require('playwright');
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const DIST = path.join(ROOT, 'dist');
const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf(k); return i > -1 ? args[i + 1] : d; };
const SHOTS = args.includes('--shots');
const OUT = path.join(ROOT, 'docs', 'screenshots');

function listPages() {
  const out = [];
  (function walk(dir) {
    for (const f of fs.readdirSync(dir)) {
      const p = path.join(dir, f);
      if (fs.statSync(p).isDirectory()) walk(p);
      else if (f === 'index.html') out.push('/' + path.relative(DIST, dir).split(path.sep).join('/') + (dir === DIST ? '' : '/'));
    }
  })(DIST);
  return out.map(u => u.replace('//', '/')).sort();
}

function serve() {
  const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.ico': 'image/x-icon', '.xml': 'application/xml', '.txt': 'text/plain' };
  const srv = http.createServer((req, res) => {
    let p = decodeURIComponent(req.url.split('?')[0]);
    if (p.endsWith('/')) p += 'index.html';
    const f = path.join(DIST, p);
    if (!f.startsWith(DIST) || !fs.existsSync(f)) { res.writeHead(404, { 'content-type': 'text/html' }); res.end(fs.readFileSync(path.join(DIST, '404.html'))); return; }
    res.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' });
    res.end(fs.readFileSync(f));
  });
  return new Promise(r => srv.listen(0, () => r(srv)));
}

(async () => {
  const srv = await serve();
  const base = `http://127.0.0.1:${srv.address().port}`;
  const pages = opt('--pages', '') ? opt('--pages').split(',') : listPages();
  const widths = opt('--widths', '390,768,1024,1440').split(',').map(Number);
  const browser = await chromium.launch();
  let problems = 0;
  const report = [];
  if (SHOTS) fs.mkdirSync(OUT, { recursive: true });
  for (const w of widths) {
    const ctx = await browser.newContext({ viewport: { width: w, height: 900 }, deviceScaleFactor: SHOTS ? 2 : 1 });
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(String(e)));
    // Block third-party requests (Amazon covers, Google Translate) so runs are deterministic.
    await page.route(/^https?:\/\/(?!127\.0\.0\.1)/, r => r.abort());
    for (const u of pages) {
      await page.goto(base + u, { waitUntil: 'load' });
      await page.waitForTimeout(150);
      const m = await page.evaluate(() => {
        const doc = document.documentElement;
        const overflow = doc.scrollWidth - doc.clientWidth;
        const wide = [];
        if (overflow > 0) {
          for (const el of document.querySelectorAll('body *')) {
            const r = el.getBoundingClientRect();
            if (r.right > doc.clientWidth + 1 && getComputedStyle(el).position !== 'fixed') { wide.push(el.tagName + '.' + el.className); if (wide.length > 4) break; }
          }
        }
        // Empty vertical bands: union of y-ranges of visible content leaves inside <main>.
        const sel = 'main h1, main h2, main h3, main p, main li, main .cover, main .btn, main img, main figure, main input, main .tcard, main .book';
        const spans = [];
        for (const el of document.querySelectorAll(sel)) {
          const r = el.getBoundingClientRect();
          const cs = getComputedStyle(el);
          if (r.height < 1 || r.width < 1 || cs.visibility === 'hidden') continue;
          spans.push([r.top + scrollY, r.bottom + scrollY]);
        }
        spans.sort((a, b) => a[0] - b[0]);
        let gaps = [], end = spans.length ? spans[0][1] : 0;
        for (const [t, b] of spans) { if (t - end > 80) gaps.push([Math.round(end), Math.round(t - end)]); end = Math.max(end, b); }
        const logo = document.querySelector('.logo').getBoundingClientRect().left;
        const h1 = document.querySelector('h1').getBoundingClientRect().left;
        return { overflow, wide, gaps, logo: Math.round(logo), h1: Math.round(h1), height: doc.scrollHeight };
      });
      const issues = [];
      if (m.overflow > 0) issues.push(`horizontal overflow ${m.overflow}px: ${m.wide.join(', ')}`);
      if (w === 1440 && m.gaps.length) issues.push(`gaps over 80px at y/size: ${JSON.stringify(m.gaps)}`);
      if (w >= 1440 && (m.logo > 150 || m.h1 > 150)) issues.push(`logo/H1 not near left edge (logo ${m.logo}px, h1 ${m.h1}px)`);
      if (errors.length) issues.push('JS errors: ' + errors.splice(0).join(' | '));
      report.push(`${w}px ${u} logo@${m.logo} h1@${m.h1} height ${m.height}${issues.length ? '  PROBLEM: ' + issues.join('; ') : '  ok'}`);
      problems += issues.length;
      if (SHOTS) {
        const name = (u === '/' ? 'home' : u.replace(/\//g, '')) + `-${w}.png`;
        await page.screenshot({ path: path.join(OUT, name), fullPage: true });
      }
    }
    await ctx.close();
  }
  await browser.close();
  srv.close();
  console.log(report.join('\n'));
  console.log(`\n${problems} problems`);
  process.exit(problems ? 1 : 0);
})();
