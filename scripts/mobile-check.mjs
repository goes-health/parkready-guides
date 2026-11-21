#!/usr/bin/env node
// ParkReady mobile-first QA gate. Run before every publish; exits non-zero on any failure.
//
//   npm install                              # once (installs playwright; uses system Chrome if present)
//   node scripts/mobile-check.mjs            # serves the repo root locally, checks every page in sitemap.xml
//   node scripts/mobile-check.mjs --base https://parks.goes.health/   # check the live site instead
//   node scripts/mobile-check.mjs --pages index.html,parks/zion/index.html --shots /tmp/shots
//
// Checks at 375x812, 390x844, 768x1024 and 1280x900:
//   viewport meta (device-width, initial-scale=1, zoom not disabled) · no horizontal scroll ·
//   compact header (<=72px tall on phones, park menu behind a toggle below 1200px, single row on desktop) ·
//   menu toggle opens/closes (aria-expanded, Escape) · text >=16px (labels >=12px, fine print >=14px) ·
//   tap targets >=44px on touch widths (links inside sentences exempt per WCAG 2.5.8; source chips >=24px) ·
//   a GOES App Store / Google Play button fully visible and tappable above the fold on phones ·
//   tables fit or scroll inside their own container · no JS errors.
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "playwright";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const SITE = "https://parks.goes.health/";
let base = opt("--base", null);
const shots = opt("--shots", null);
const onlyVp = opt("--viewports", null);

const VIEWPORTS = [
  { name: "375x812", width: 375, height: 812, mobile: true },
  { name: "390x844", width: 390, height: 844, mobile: true },
  { name: "768x1024", width: 768, height: 1024, mobile: true },
  { name: "1280x900", width: 1280, height: 900, mobile: false },
].filter(v => !onlyVp || onlyVp.split(",").includes(v.name));

// Pages: --pages list, else every <loc> in sitemap.xml (so new weekly pages are covered automatically).
let pages = opt("--pages", null)?.split(",");
if (!pages) {
  const sm = fs.readFileSync(path.join(ROOT, "sitemap.xml"), "utf8");
  pages = [...sm.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m => m[1].replace(SITE, "") || "index.html");
}

// Tiny static server for the repo root (no extra deps).
const TYPES = { ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript", ".svg": "image/svg+xml", ".png": "image/png", ".json": "application/json", ".txt": "text/plain", ".md": "text/markdown" };
let server;
if (!base) {
  server = http.createServer((req, res) => {
    let p = decodeURIComponent(new URL(req.url, "http://x").pathname);
    if (p.endsWith("/")) p += "index.html";
    const f = path.join(ROOT, p);
    if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end("not found"); }
    res.writeHead(200, { "content-type": TYPES[path.extname(f)] || "application/octet-stream" });
    fs.createReadStream(f).pipe(res);
  });
  await new Promise(r => server.listen(0, "127.0.0.1", r));
  base = `http://127.0.0.1:${server.address().port}/`;
}
if (!base.endsWith("/")) base += "/";

const chromePath = process.env.CHROME_PATH || ["/usr/bin/google-chrome", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"].find(p => fs.existsSync(p));
const browser = await chromium.launch({ executablePath: chromePath, args: ["--no-sandbox"] });
const IPHONE_UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1";

// In-page audit. Returns a list of failure strings.
function audit({ mobile, phone }) {
  const fails = [];
  const vw = document.documentElement.clientWidth, vh = window.innerHeight;
  const vis = el => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== "hidden" && cs.display !== "none" && !el.closest("[hidden],[aria-hidden='true']"); };
  const desc = el => { let s = el.tagName.toLowerCase(); if (el.id) s += "#" + el.id; if (el.className && typeof el.className === "string") s += "." + el.className.trim().split(/\s+/).join("."); const t = (el.textContent || "").trim().replace(/\s+/g, " ").slice(0, 40); return t ? `${s} "${t}"` : s; };

  // 1. viewport meta
  const vm = document.querySelector('meta[name="viewport"]')?.content || "";
  if (!/width=device-width/.test(vm) || !/initial-scale=1/.test(vm)) fails.push(`viewport meta missing/incorrect: "${vm}"`);
  if (/user-scalable\s*=\s*(no|0)|maximum-scale\s*=\s*1(\.0)?\b/.test(vm)) fails.push(`viewport meta disables zoom: "${vm}"`);

  // 2. horizontal scroll
  const sw = Math.max(document.documentElement.scrollWidth, document.body.scrollWidth);
  if (sw > vw + 1) {
    const culprits = [...document.querySelectorAll("body *")].filter(el => { const r = el.getBoundingClientRect(); return r.right > vw + 1 && vis(el); }).slice(0, 5).map(desc);
    fails.push(`horizontal scroll: page is ${sw}px wide in a ${vw}px viewport (${culprits.join("; ")})`);
  }

  // 3. header
  const header = document.querySelector("header.site-header");
  if (!header) fails.push("no header.site-header");
  else {
    const h = header.getBoundingClientRect().height;
    const maxH = phone ? 72 : 88;
    if (h > maxH) fails.push(`header is ${Math.round(h)}px tall (max ${maxH}px)`);
    const shown = [...header.querySelectorAll("a, button")].filter(vis);
    if (phone && shown.length > 3) fails.push(`header shows ${shown.length} links/buttons on a phone (max 3: logo, app CTA, menu): ${shown.map(desc).join("; ")}`);
  }

  // 4. text size
  const LABEL = ".pill, .src, .tag, .eyebrow, .badge, .meta, .wk, th, .store-btn small, .skip";
  const FINE = ".cta-disclaimer, .cta-terms, .trust-line, .footer-disclaimer, .forecast-status, .week-bar, .by";
  const small = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  for (let n; (n = walker.nextNode());) {
    if (!n.textContent.trim()) continue;
    const el = n.parentElement;
    if (!el || seen.has(el) || ["SCRIPT", "STYLE", "NOSCRIPT"].includes(el.tagName)) continue;
    seen.add(el);
    if (!vis(el)) continue;
    const fs = parseFloat(getComputedStyle(el).fontSize);
    const min = el.closest(LABEL) ? 12 : el.closest(FINE) ? 14 : 16;
    if (fs + 0.01 < min) small.push(`${desc(el)} ${fs}px<${min}`);
  }
  if (small.length) fails.push(`${small.length} text elements too small: ${small.slice(0, 6).join("; ")}${small.length > 6 ? " …" : ""}`);

  // 5. tap targets (touch widths only)
  if (mobile) {
    const bad = [];
    for (const el of document.querySelectorAll("a[href], button, summary, input, select, [role=button]")) {
      if (!vis(el) || el.classList.contains("skip")) continue;
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      // Inline link inside a sentence, or a source chip: WCAG 2.5.8 inline/24px rule.
      const block = el.parentElement?.closest("p, li, td, dd, span.src, div");
      const inline = el.closest(".src") || (cs.display === "inline" && block && block.textContent.trim().length > el.textContent.trim().length + 3);
      // WCAG 2.5.8: links inside a sentence are exempt; source chips need 24px; everything else 44px.
      if (inline && !el.closest(".src")) continue;
      const min = inline ? 24 : 44;
      if (r.height + 0.5 < min || (!inline && r.width + 0.5 < 44)) bad.push(`${desc(el)} ${Math.round(r.width)}x${Math.round(r.height)}<${min}`);
    }
    if (bad.length) fails.push(`${bad.length} tap targets too small: ${bad.slice(0, 6).join("; ")}${bad.length > 6 ? " …" : ""}`);
  }

  // 6. app CTA above the fold on phones
  if (phone) {
    const ok = [...document.querySelectorAll("a.store-btn, a[data-cta]")].some(a => {
      const r = a.getBoundingClientRect();
      if (!vis(a) || r.top < 0 || r.bottom > vh || r.left < 0 || r.right > vw) return false;
      const hit = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
      return hit && (hit === a || a.contains(hit));
    });
    if (!ok) fails.push("no App Store / Google Play button fully visible and tappable in the first screen");
  }

  // 7. tables fit or scroll in their own wrapper
  for (const t of document.querySelectorAll("table")) {
    if (!vis(t)) continue;
    const r = t.getBoundingClientRect();
    const wrap = t.closest(".table-wrap");
    const scrolls = wrap && /(auto|scroll)/.test(getComputedStyle(wrap).overflowX);
    if (r.right > vw + 1 && !scrolls) fails.push(`table overflows viewport without a scroll container`);
  }
  return fails;
}

const results = [];
for (const vp of VIEWPORTS) {
  const ctx = await browser.newContext({
    viewport: { width: vp.width, height: vp.height }, deviceScaleFactor: vp.width < 500 ? 3 : 1,
    isMobile: vp.mobile, hasTouch: vp.mobile, userAgent: vp.width < 500 ? IPHONE_UA : undefined,
  });
  // Keep the check deterministic and offline-friendly: block third-party requests (fonts still try; live NWS is skipped).
  await ctx.route(/api\.weather\.gov/, r => r.abort());
  for (const pg of pages) {
    const page = await ctx.newPage();
    const jsErrors = [];
    page.on("pageerror", e => jsErrors.push(e.message));
    const url = base + (pg === "index.html" ? "" : pg);
    let fails = [];
    try {
      const resp = await page.goto(url, { waitUntil: "load", timeout: 45000 });
      if (!resp || resp.status() >= 400) fails.push(`HTTP ${resp?.status()}`);
      await page.evaluate(() => document.fonts && document.fonts.ready);
      await page.waitForTimeout(150);
      const phone = vp.width < 640;
      fails.push(...await page.evaluate(audit, { mobile: vp.mobile, phone }));
      if (shots) {
        fs.mkdirSync(shots, { recursive: true });
        const name = pg.replace(/^parks\//, "").replace(/\/index\.html$/, "-park").replace(/\.html$/, "").replace(/\//g, "-").replace(/^index$/, "home");
        await page.evaluate(() => window.scrollTo(0, 0));
        await page.screenshot({ path: path.join(shots, `${name}-${vp.name}-fold.png`) });
        await page.screenshot({ path: path.join(shots, `${name}-${vp.name}-full.png`), fullPage: true });
      }
      // Menu toggle behaviour where the nav is collapsed.
      const toggle = page.locator(".nav-toggle");
      const toggleShown = (await toggle.count()) && (await toggle.isVisible());
      if (phone && !toggleShown) fails.push("no visible .nav-toggle menu button on phone");
      if (vp.width >= 1200 && toggleShown) fails.push(".nav-toggle visible at desktop width (nav should be inline)");
      if (toggleShown) {
        {
          await toggle.click({ timeout: 5000 });
          const st = await page.evaluate(() => {
            const t = document.querySelector(".nav-toggle"), nav = document.getElementById(t.getAttribute("aria-controls"));
            const links = nav ? [...nav.querySelectorAll("a")].filter(a => a.getBoundingClientRect().height > 0) : [];
            return { exp: t.getAttribute("aria-expanded"), n: links.length, small: links.filter(a => a.getBoundingClientRect().height < 44).length, overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1 };
          });
          if (st.exp !== "true" || st.n < 2) fails.push(`menu toggle did not open the menu (aria-expanded=${st.exp}, ${st.n} links)`);
          if (st.small) fails.push(`${st.small} menu links shorter than 44px`);
          if (st.overflow) fails.push("open menu causes horizontal scroll");
          if (shots && pg === "index.html") await page.screenshot({ path: path.join(shots, `home-menu-open-${vp.name}.png`) });
          await page.keyboard.press("Escape");
          if ((await toggle.getAttribute("aria-expanded")) !== "false") fails.push("Escape does not close the menu");
        }
      }
      if (jsErrors.length) fails.push(`JS errors: ${jsErrors.join(" | ")}`);
    } catch (e) { fails.push(`load error: ${e.message.split("\n")[0]}`); }
    results.push({ page: pg, viewport: vp.name, fails });
    await page.close();
  }
  await ctx.close();
}
await browser.close();
server?.close();

let bad = 0;
for (const r of results) {
  if (!r.fails.length) continue;
  bad++;
  console.log(`✗ ${r.page} @ ${r.viewport}`);
  for (const f of r.fails) console.log(`    - ${f}`);
}
console.log(`\nmobile-check: ${results.length - bad}/${results.length} page×viewport checks passed (${pages.length} pages × ${VIEWPORTS.length} viewports) against ${base}`);
process.exit(bad ? 1 : 0);
