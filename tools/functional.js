// Functional QA (Playbook Prompt 19): menu, submenu, /books/ filter + search + batches, EN/ES cookie,
// cover fallback, external link attributes, 404, and the catalogue with JavaScript turned off.
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const DIST = path.resolve(__dirname, '..', 'dist');
const srv = http.createServer((q, r) => {
  let p = decodeURIComponent(q.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html';
  const f = path.join(DIST, p);
  if (!fs.existsSync(f)) { r.writeHead(404, { 'content-type': 'text/html' }); r.end(fs.readFileSync(path.join(DIST, '404.html'))); return; }
  const t = { '.html': 'text/html', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.woff2': 'font/woff2' }[path.extname(f)] || 'application/octet-stream';
  r.writeHead(200, { 'content-type': t }); r.end(fs.readFileSync(f));
});
const results = [];
const check = (name, ok, extra = '') => results.push(`${ok ? 'PASS' : 'FAIL'}  ${name}${extra ? '  (' + extra + ')' : ''}`);
srv.listen(0, async () => {
  const base = `http://127.0.0.1:${srv.address().port}`;
  const b = await chromium.launch();
  const errs = [];
  // Desktop
  let ctx = await b.newContext({ viewport: { width: 1440, height: 900 } });
  let pg = await ctx.newPage(); pg.on('pageerror', e => errs.push(String(e)));
  await pg.route(/^https?:\/\/(?!127)/, r => r.abort());
  await pg.goto(base + '/');
  await pg.click('.sub-toggle');
  check('desktop: More Topics submenu opens on click', await pg.isVisible('.sub a[href="/nature-books-for-kids/"]'));
  await pg.keyboard.press('Escape'); await pg.mouse.move(5, 700);
  check('desktop: Escape closes submenu', !(await pg.isVisible('.sub a[href="/nature-books-for-kids/"]')));
  await pg.waitForTimeout(300);
  check('cover fallback: blocked covers become title blocks (no broken images)', await pg.evaluate(() => document.querySelectorAll('.hero .cover--none').length >= 6 && document.querySelectorAll('.hero .cover img').length === 0));
  const ext = await pg.evaluate(() => [...document.querySelectorAll('a[href^="https://"]')].filter(a => a.target !== '_blank' || !/noopener/.test(a.rel)).map(a => a.href));
  check('every external link opens in a new tab with rel=noopener', ext.length === 0, ext.slice(0, 3).join(' '));
  await pg.click('a.logo');
  check('logo links to home', new URL(pg.url()).pathname === '/');
  // ES toggle
  await pg.click('.lang__btn[data-lang="es"]');
  await pg.waitForLoadState('load');
  const ck = await ctx.cookies();
  check('ES button sets googtrans=/en/es and reloads', ck.some(c => c.name === 'googtrans' && c.value === '/en/es'));
  check('ES button shows pressed after reload', await pg.getAttribute('.lang__btn[data-lang="es"]', 'aria-pressed') === 'true');
  await pg.click('.lang__btn[data-lang="en"]'); await pg.waitForLoadState('load');
  check('EN button clears the cookie', !(await ctx.cookies()).some(c => c.name === 'googtrans' && c.value));
  // /books/
  await pg.goto(base + '/books/');
  const vis = () => pg.evaluate(() => [...document.querySelectorAll('#book-list .book')].filter(c => !c.hidden).length);
  check('/books/: first batch shows 48', await vis() === 48);
  await pg.click('#show-more');
  check('/books/: Show more adds the next 48', await vis() === 96);
  await pg.click('.filter[data-filter="teens"]');
  check('/books/: Teens filter shows 9', await vis() === 9);
  await pg.click('.filter[data-filter="christian"]');
  check('/books/: Christian filter shows 48 of 65 then all after Show more', await vis() === 48 && (await pg.click('#show-more'), await vis()) === 65);
  await pg.click('.filter[data-filter="all"]');
  await pg.fill('#book-search', 'noah');
  check('/books/: search "noah" finds Noah\'s Ark', await vis() === 1 && (await pg.textContent('#book-list .book:not([hidden]) .book__title')).includes("Noah"));
  await pg.fill('#book-search', 'zzzz');
  check('/books/: empty search says so', (await pg.textContent('#book-count')).startsWith('No books'));
  // 404
  const resp = await pg.goto(base + '/no-such-page/');
  check('404 page served with noindex and a way back', resp.status() === 404 && (await pg.content()).includes('noindex') && await pg.isVisible('a[href="/books/"]'));
  await ctx.close();
  // Phone menu
  ctx = await b.newContext({ viewport: { width: 390, height: 800 }, hasTouch: true });
  pg = await ctx.newPage(); pg.on('pageerror', e => errs.push(String(e)));
  await pg.route(/^https?:\/\/(?!127)/, r => r.abort());
  await pg.goto(base + '/bedtime-stories-for-kids/');
  check('phone: menu hidden until tapped', !(await pg.isVisible('.site-nav__link[href="/books/"]')));
  await pg.click('.nav-toggle');
  check('phone: Menu button opens the nav', await pg.isVisible('.site-nav__link[href="/books/"]') && await pg.getAttribute('.nav-toggle', 'aria-expanded') === 'true');
  check('phone: social icons and EN/ES visible in header', await pg.isVisible('.social--header a[aria-label*="TikTok"]') && await pg.isVisible('.lang__btn[data-lang="es"]'));
  await ctx.close();
  // No JavaScript
  ctx = await b.newContext({ viewport: { width: 1024, height: 800 }, javaScriptEnabled: false });
  pg = await ctx.newPage();
  await pg.route(/^https?:\/\/(?!127)/, r => r.abort());
  await pg.goto(base + '/books/');
  check('no JS: all 220 books visible on /books/', await pg.evaluate(() => [...document.querySelectorAll('#book-list .book')].filter(c => c.offsetParent).length) === 220);
  check('no JS: nav links visible', await pg.isVisible('.site-nav__link[href="/about/"]'));
  await ctx.close();
  await b.close(); srv.close();
  check('no JavaScript errors on any tested page', errs.length === 0, errs.join(' | '));
  console.log(results.join('\n'));
  const fails = results.filter(r => r.startsWith('FAIL')).length;
  console.log(`\n${results.length - fails} passed, ${fails} failed`);
  process.exit(fails ? 1 : 0);
});
