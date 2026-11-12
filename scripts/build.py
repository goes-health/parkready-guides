#!/usr/bin/env python3
"""Render ParkReady Guides static site from data/parks.json + data/conditions.json."""
import json, os, html, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Public base URL. Override with PARKREADY_BASE if needed.
BASE = os.environ.get("PARKREADY_BASE", "https://parks.goes.health/")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import agents
subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "content.py")], check=True)
D = json.load(open(os.path.join(ROOT, "data", "parks.json")))
COND = json.load(open(os.path.join(ROOT, "data", "conditions.json")))
WEEK, GOES, TAGS, S, PARKS = D["week"], D["goes"], D["goes_tags"], D["sources"], D["parks"]
e = html.escape

APPLE = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M16.4 12.6c0-2.5 2-3.7 2.1-3.8-1.2-1.7-3-1.9-3.6-2-1.5-.2-3 .9-3.8.9-.8 0-2-.9-3.3-.9-1.7 0-3.3 1-4.2 2.5-1.8 3.1-.5 7.7 1.3 10.2.9 1.2 1.9 2.6 3.2 2.6 1.3-.1 1.8-.8 3.3-.8 1.6 0 2 .8 3.3.8 1.4 0 2.3-1.3 3.1-2.5 1-1.4 1.4-2.8 1.4-2.9 0 0-2.8-1.1-2.8-4.1zM14 5.1c.7-.9 1.2-2 1-3.1-1 0-2.2.7-2.9 1.5-.6.7-1.2 1.9-1 3 1.1.1 2.2-.6 2.9-1.4z"/></svg>'
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M3.6 2.3c-.3.3-.4.7-.4 1.2v17c0 .5.1.9.4 1.2l9.5-9.7-9.5-9.7zm10.6 10.8 2.6 2.6-11 6.3 8.4-8.9zm0-2.2L5.8 2l11 6.3-2.6 2.6zm3.9-1.8 3 1.7c.9.5.9 1.9 0 2.4l-3 1.7-2.8-2.9 2.8-2.9z"/></svg>'

def stores(alt_android=True, where=""):
    return (f'<div class="stores">'
            f'<a class="store-btn" href="{GOES["ios"]}" rel="noopener" data-cta="ios{where}">{APPLE}<span><small>Download on the</small><b>App Store</b></span></a>'
            f'<a class="store-btn{" alt" if alt_android else ""}" href="{GOES["android"]}" rel="noopener" data-cta="android{where}">{PLAY}<span><small>Get it on</small><b>Google Play</b></span></a>'
            f'</div>')

def chips(keys, rel):
    out = []
    for i, k in enumerate(keys):
        s = S[k]
        out.append(f'<a href="{e(s["url"])}" title="{e(s["label"])}" rel="noopener">{e(short_label(k))}</a>')
    return f'<span class="src" aria-label="Sources">{"".join(out)}</span>'

def short_label(k):
    if k == "nws" or k.startswith("nws-"): return "NWS"
    if k == "nps-api": return "NPS API"
    if k == "airnow": return "AirNow"
    if k.endswith("-alerts"): return "NPS alert"
    if k.endswith("-fees"): return "NPS fees"
    lab = S[k]["label"]
    if lab.startswith("News release"): return "NPS news"
    return "NPS"

STATUS_TXT = {"open": "Open", "caution": "Heads-up", "closed": "Closed", None: "Info"}

def page(rel, title, desc, canonical, body, active=None, extra_head=""):
    nav = [("index.html", "Parks", "home")] + [(f"parks/{p['slug']}/index.html", p["short"].replace("Great Smoky Mountains", "Smokies"), p["slug"]) for p in PARKS]
    navhtml = "".join(f'<a href="{rel}{h}"{" aria-current=\"page\"" if a == active else ""} class="{"hide-sm" if a not in ("home",) else ""}">{e(t)}</a>' for h, t, a in nav)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">
  <link rel="canonical" href="{BASE}{canonical}">
  <link rel="alternate" type="text/markdown" href="{BASE}{agents.md_path(canonical)}">
  <link rel="describedby" href="{BASE}llms.txt">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:url" content="{BASE}{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="ParkReady Guides by GOES Health">
  <meta name="theme-color" content="#2F5D50">
  <link rel="icon" href="{rel}assets/brand/logomark/logomark_yellow.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{rel}assets/css/site.css">
  <link rel="stylesheet" href="{rel}assets/css/parks.css">{extra_head}
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="inner">
      <a class="brand-lockup" href="{rel}index.html">
        <img class="goes-logo" src="{rel}assets/brand/logo/GOES_black.svg" alt="GOES" width="70" height="22">
        <span class="divider" aria-hidden="true"></span>
        <span class="site-name">ParkReady Guides<span class="by">by GOES Health</span></span>
      </a>
      <nav class="nav" aria-label="Primary">{navhtml}<a class="nav-cta" href="#get-goes">Get the app</a></nav>
    </div>
  </header>
  <div class="week-bar"><div class="inner"><span class="wk">{e(WEEK["label"])}</span><span>Conditions pulled from official NPS and National Weather Service sources on {fmt_date(WEEK["fetched"])}. <a href="#sources">See sources</a></span></div></div>
  <main id="main">
{body}
  </main>
  <footer class="site-footer">
    <img class="footer-pattern" src="{rel}assets/brand/pattern/Pattern_BotLeft.svg" alt="" aria-hidden="true">
    <div class="inner">
      <div class="footer-brand">
        <img class="goes-logo" src="{rel}assets/brand/logo/GOES_offwhite.svg" alt="GOES" width="64" height="20">
        <span><strong>ParkReady Guides</strong> by <a href="{GOES["platform"]}">GOES Health</a> — weekly national park entrance briefings.</span>
        <p class="footer-disclaimer">{e(GOES["disclaimer"])} Always follow official National Park Service rules, posted closures and ranger instructions. ParkReady Guides is not affiliated with or endorsed by the National Park Service. Conditions change quickly; check the linked NPS pages before you go. In an emergency, call 911.</p>
      </div>
      <div>
        <p style="margin:0 0 .4rem"><a href="{GOES["ios"]}" rel="noopener">GOES on the App Store</a></p>
        <p style="margin:0 0 .4rem"><a href="{GOES["android"]}" rel="noopener">GOES on Google Play</a></p>
        <p style="margin:0"><a href="{GOES["site"]}">goes.health</a></p>
      </div>
    </div>
  </footer>
</body>
</html>
'''

def fmt_date(iso):
    import datetime
    d = datetime.date.fromisoformat(iso)
    return d.strftime("%b %-d, %Y")

def cta_band(reason, rel, where=""):
    return f'''
      <section class="section" id="get-goes">
        <div class="wrap-narrow">
          <div class="cta-band">
            <img class="goes-mark" src="{rel}assets/brand/logo/GOES_offwhite.svg" alt="GOES" width="90" height="28">
            <p class="partner-line">Your outdoor safety companion</p>
            <h2>When signal drops, GOES steps in.</h2>
            <p class="reason">{e(reason)}</p>
            <ul class="feature-list">
              <li><strong>Works with no cell service:</strong> interactive health assessment and 50+ visual how-to guides, available offline.</li>
              <li><strong>Location-specific risks:</strong> wildlife (bears, venomous snakes), hypothermia, frostbite, heat illness, altitude, ticks, poisonous plants, UV and smoke/air quality.</li>
              <li><strong>200+ prevention tips across 60+ medical topics,</strong> also available offline.</li>
              <li><strong>Built by wilderness medicine physicians:</strong> founded by Dr. Grant Lipman, former Stanford Emergency Medicine professor and director of its wilderness medicine fellowship; Chief Medical Officer Dr. Colin Little, MD, FAWM.</li>
            </ul>
            {stores(where=where)}
            <p class="cta-disclaimer">Free to download. Premium features need a monthly or annual subscription after a 7-day free trial. {e(GOES["disclaimer"])} Follow official NPS rules and ranger instructions.</p>
          </div>
        </div>
      </section>'''

def offline_callout(text, where=""):
    return f'''<div class="offline-callout"><div><strong>When signal drops, GOES steps in.</strong><p>{e(text)}</p></div>{stores(where=where)}</div>'''

def risk_cards(risks, rel):
    out = []
    for r in risks:
        g = f'<p class="goes-line"><b>In GOES</b>{e(TAGS[r["goes"]])}</p>' if r.get("goes") else ""
        out.append(f'<div class="card risk-card"><h3>{e(r["title"])}</h3><p>{e(r["body"])} {chips(r["sources"], rel)}</p>{g}</div>')
    return '<div class="grid grid-2">' + "".join(out) + "</div>"

def cond_list(conds, rel):
    out = []
    for c in conds:
        st = c.get("status")
        out.append(f'<li class="{st or ""}"><span class="tag">{STATUS_TXT[st]}</span>{e(c["text"])} {chips(c["sources"], rel)}</li>')
    return '<ul class="cond-list">' + "".join(out) + "</ul>"

def nps_alerts(code, rel):
    al = COND["parks"][code]["alerts"]
    if not al: return '<p>No active NPS alerts were listed when we fetched.</p>'
    items = []
    for a in al:
        link = f' <a href="{e(a["url"])}" rel="noopener">More</a>' if a.get("url") else ""
        items.append(f'<li class="{"closed" if a["category"]=="Park Closure" else ("caution" if a["category"] in ("Caution","Danger") else "")}"><span class="tag">{e(a["category"])}</span><strong>{e(a["title"])}.</strong> {e(a["description"])}{link}</li>')
    return '<ul class="cond-list">' + "".join(items) + "</ul>"

def forecast_block(nkey):
    n = COND["nws"][nkey]
    rows = "".join(f'<tr><td>{e(p["name"])}</td><td>{p["temp"]}°{e(p["unit"])}</td><td>{e(p["short"])}</td><td>{e(p["wind"] or "")}</td></tr>' for p in n["periods"][:8])
    alerts = "".join(f'<div class="wx-alert"><strong>{e(a["event"])}</strong> — {e(a["headline"] or "")}</div>' for a in n["alerts"])
    return f'''
          <div class="forecast" data-forecast-url="{e(n["forecast_url"] or "")}" data-lat="{n["lat"]}" data-lon="{n["lon"]}">
            <div class="forecast-head"><span class="forecast-status" aria-live="polite">Snapshot from the National Weather Service, fetched {fmt_date(WEEK["fetched"])}. Live forecast loads below if you're online.</span><a href="{e(n["forecast_page"])}" rel="noopener">Full NWS forecast</a></div>
            <div class="wx-alerts">{alerts}</div>
            <div class="table-wrap"><table><thead><tr><th scope="col">Period</th><th scope="col">Temp</th><th scope="col">Forecast</th><th scope="col">Wind</th></tr></thead><tbody>{rows}</tbody></table></div>
          </div>'''

def sources_section(keys, park_code=None):
    seen, items = set(), []
    for k in keys:
        if k in seen: continue
        seen.add(k)
        items.append(f'<li><a href="{e(S[k]["url"])}" rel="noopener">{e(S[k]["label"])}</a></li>')
    return f'''
      <section class="section" id="sources">
        <div class="wrap-narrow">
          <p class="eyebrow">Sources</p>
          <h2>Where this week's information comes from</h2>
          <p class="section-intro">{e(WEEK["fetched_note"])} We don't publish wait times, bear sightings or conditions we can't source. Check the official pages before you go — they're updated more often than we are.</p>
          <ol class="sources-list">{"".join(items)}</ol>
        </div>
      </section>'''

def collect_keys(p, ent=None):
    keys = []
    if ent:
        for c in ent["conditions"]: keys += c["sources"]
        for r in ent["risks"]: keys += r["sources"]
        keys += ["nws"]
    keys += p["summary_sources"] + p["fees_sources"]
    for c in p["closed"]: keys += c["sources"]
    for r in p["park_risks"]: keys += r["sources"]
    keys += [f'{p["code"]}-alerts', f'{p["code"]}-home', "nps-api", "goes-app"]
    return keys

def ent_pills(p, rel, current=None):
    li = []
    for en in p["entrances"]:
        cur = ' aria-current="page"' if current == en["slug"] else ""
        li.append(f'<li><a href="{rel}parks/{p["slug"]}/{en["slug"]}.html"{cur}>{e(en["name"])}</a><span class="pill {en["status"]}">{e(en["status_label"])}</span></li>')
    return '<ul class="ent-list">' + "".join(li) + "</ul>"

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(content)

URLS = []

# ---------------- entrance pages
for p in PARKS:
    for en in p["entrances"]:
        rel = "../../"
        path = f'parks/{p["slug"]}/{en["slug"]}.html'
        URLS.append(path)
        title = f'{p["short"]} {en["name"]} This Week ({WEEK["label"].replace("Week of ", "")}): Conditions & Safety — ParkReady'
        desc = f'{p["short"]} {en["name"]} ({en["gateway"]}) this week: official NPS road and entrance status, NWS forecast, the risks that matter in mid-November, and why to download the GOES offline safety app before you lose signal.'
        others = [x for x in p["entrances"] if x["slug"] != en["slug"]]
        body = f'''
    <article>
      <section class="hero park-hero">
        <img class="hero-pattern" src="{rel}assets/brand/pattern/Pattern_TopRight.svg" alt="" aria-hidden="true">
        <div class="wrap-narrow">
          <p class="kicker"><a href="{rel}index.html">Parks</a> / <a href="index.html">{e(p["short"])}</a> / {e(en["name"])}</p>
          <p class="eyebrow">{e(p["short"])} · {e(en["gateway"])}</p>
          <h1>{e(p["short"])} {e(en["name"])}: this week</h1>
          <p><span class="pill {en["status"]}">{e(en["status_label"])}</span> <span class="badge" style="margin:0 0 0 .4rem">{e(WEEK["label"])}</span></p>
          <p class="lead">{e(en["intro"])}</p>
          <div class="actions">
            <a class="btn btn-secondary" href="#conditions">This week's conditions</a>
            <a class="btn btn-secondary" href="#risks">Risks here now</a>
            <a class="btn btn-primary" href="#get-goes">Get GOES before you lose signal</a>
          </div>
          {offline_callout(en["cta_reason"], "-top")}
        </div>
      </section>

      <section class="section" id="conditions">
        <div class="wrap-narrow">
          <p class="eyebrow">Official conditions</p>
          <h2>This week at the {e(en["name"])}</h2>
          <p class="section-intro">From NPS pages and alerts fetched {fmt_date(WEEK["fetched"])}. Each line links to its source.</p>
          {cond_list(en["conditions"], rel)}
          <p class="rules-note"><strong>Entrance fee:</strong> {e(p["fees"])} {chips(p["fees_sources"], rel)}</p>
        </div>
      </section>

      <section class="section" id="weather">
        <div class="wrap-narrow">
          <p class="eyebrow">Weather</p>
          <h2>Forecast near the {e(en["name"])}</h2>
          {forecast_block(en["nws"])}
        </div>
      </section>

      <section class="section" id="risks">
        <div class="risk-wrap">
          <div>
            <p class="eyebrow">Know the risks</p>
            <h2>What actually matters here in mid-November</h2>
            <p class="section-intro">The goal is a good trip, not a scary one. These are the hazards NPS highlights for this area and season, and what to do about each.</p>
          </div>
          {risk_cards(en["risks"], rel)}
        </div>
      </section>

      <section class="section" id="prep">
        <div class="wrap-narrow">
          <p class="eyebrow">Before you go in</p>
          <h2>Checklist for the {e(en["name"])}</h2>
          <ul class="checklist">{"".join(f"<li><strong>{e(a)}</strong><span>{e(b)}</span></li>" for a, b in en["prep"])}</ul>
          <p class="rules-note">Follow official NPS rules, posted closures and ranger instructions. They override anything on this page.</p>
        </div>
      </section>

      <section class="section" id="parkwide">
        <div class="risk-wrap">
          <div>
            <p class="eyebrow">Park-wide</p>
            <h2>{e(p["short"])} risks everywhere in the park</h2>
          </div>
          {risk_cards(p["park_risks"], rel)}
        </div>
      </section>

      <section class="section" id="nps-alerts">
        <div class="wrap-narrow">
          <p class="eyebrow">NPS alerts</p>
          <h2>All active {e(p["short"])} alerts</h2>
          <p class="section-intro">Pulled from the NPS Data API on {fmt_date(WEEK["fetched"])}; the same alerts appear on <a href="https://www.nps.gov/{p["code"]}/planyourvisit/conditions.htm" rel="noopener">nps.gov/{p["code"]}</a>.</p>
          {nps_alerts(p["code"], rel)}
        </div>
      </section>
{cta_band(en["cta_reason"], rel, "-band")}

      <section class="section">
        <div class="wrap-narrow">
          <p class="eyebrow">Other {e(p["short"])} entrances</p>
          {ent_pills(p, rel, en["slug"])}
          <p style="margin-top:1rem"><a href="index.html">{e(p["short"])} overview, closures and park-wide risks →</a></p>
        </div>
      </section>
{sources_section(collect_keys(p, en))}
    </article>'''
        write(path, page(rel, title, desc, path, body, active=p["slug"], extra_head=f'\n  <script src="{rel}assets/js/live-forecast.js" defer></script>'))

# ---------------- park overview pages
for p in PARKS:
    rel = "../../"
    path = f'parks/{p["slug"]}/index.html'
    URLS.append(path)
    title = f'{p["short"]} This Week ({WEEK["label"].replace("Week of ", "")}): Open Entrances, Closures & Safety — ParkReady'
    desc = f'{p["name"]} this week: which entrances are open, seasonal closures, official NPS alerts, mid-November risks and the GOES offline safety app.'
    ent_cards = "".join(f'''<div class="card park-card"><p class="meta">{e(en["gateway"])}</p><h3><a class="title-link" href="{en["slug"]}.html">{e(en["name"])}</a></h3><p>{e(en["intro"])}</p><p style="margin-top:.75rem"><span class="pill {en["status"]}">{e(en["status_label"])}</span></p><p style="margin-top:.75rem"><a href="{en["slug"]}.html">This week at {e(en["name"])} →</a></p></div>''' for en in p["entrances"])
    closed = "".join(f'<li class="closed"><span class="tag">Closed / limited</span><strong>{e(c["name"])}.</strong> {e(c["note"])} {chips(c["sources"], rel)}</li>' for c in p["closed"])
    body = f'''
    <article>
      <section class="hero park-hero">
        <img class="hero-pattern" src="{rel}assets/brand/pattern/Pattern_TopRight.svg" alt="" aria-hidden="true">
        <div class="wrap-narrow">
          <p class="kicker"><a href="{rel}index.html">Parks</a> / {e(p["short"])}</p>
          <p class="eyebrow">{e(p["state"])} · {e(WEEK["label"])}</p>
          <h1>{e(p["name"])} this week</h1>
          <p class="lead"><strong>{e(p["tagline"])}</strong></p>
          <p class="lead">{e(p["summary"])} {chips(p["summary_sources"], rel)}</p>
          <div class="actions">
            <a class="btn btn-secondary" href="#entrances">Open entrances</a>
            <a class="btn btn-secondary" href="#closed">Closed this week</a>
            <a class="btn btn-primary" href="#get-goes">Get GOES before you lose signal</a>
          </div>
          {offline_callout(p["cta_reason"], "-top")}
        </div>
      </section>

      <section class="section" id="entrances">
        <div class="wrap">
          <p class="eyebrow">Entrances open this week</p>
          <h2>Pick your entrance</h2>
          <div class="grid grid-2">{ent_cards}</div>
        </div>
      </section>

      <section class="section" id="closed">
        <div class="wrap-narrow">
          <p class="eyebrow">Seasonal closures</p>
          <h2>Closed or limited this week</h2>
          <ul class="cond-list closed-list">{closed}</ul>
          <p class="rules-note"><strong>Entrance fee:</strong> {e(p["fees"])} {chips(p["fees_sources"], rel)}</p>
        </div>
      </section>

      <section class="section" id="risks">
        <div class="risk-wrap">
          <div>
            <p class="eyebrow">Know the risks</p>
            <h2>What matters in {e(p["short"])} right now</h2>
            <p class="section-intro">Teach, don't scare: these are the hazards NPS emphasizes this season, with what to do.</p>
          </div>
          {risk_cards(p["park_risks"], rel)}
        </div>
      </section>

      <section class="section" id="nps-alerts">
        <div class="wrap-narrow">
          <p class="eyebrow">NPS alerts</p>
          <h2>Active {e(p["short"])} alerts</h2>
          <p class="section-intro">From the NPS Data API, fetched {fmt_date(WEEK["fetched"])}. Live version: <a href="https://www.nps.gov/{p["code"]}/planyourvisit/conditions.htm" rel="noopener">nps.gov/{p["code"]} conditions</a>.</p>
          {nps_alerts(p["code"], rel)}
          <p class="rules-note">Follow official NPS rules, posted closures and ranger instructions. They override anything on this page.</p>
        </div>
      </section>
{cta_band(p["cta_reason"], rel, "-band")}
{sources_section(collect_keys(p) + [k for en in p["entrances"] for c in en["conditions"] for k in c["sources"]])}
    </article>'''
    write(path, page(rel, title, desc, path, body, active=p["slug"]))

# ---------------- home
def jsonld():
    n_ent = sum(len(p["entrances"]) for p in PARKS)
    org = {"@type": "Organization", "name": "GOES Health", "url": GOES["site"]}
    data = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": BASE + "#website", "name": "ParkReady Guides", "url": BASE,
         "description": "Weekly U.S. national park entrance briefings: open entrances, official NPS closures, NWS forecasts and what to prepare for.",
         "publisher": org, "inLanguage": "en"},
        {"@type": "Dataset", "name": f"ParkReady weekly national park entrance conditions — {WEEK['label']}",
         "description": f"This week's official National Park Service alerts and closures and National Weather Service forecasts for {n_ent} open entrances at {len(PARKS)} U.S. national parks, with seasonal preparation guidance. Updated weekly.",
         "url": BASE, "creator": org, "isAccessibleForFree": True,
         "temporalCoverage": f"{WEEK['start']}/{WEEK['end']}", "dateModified": WEEK["fetched"],
         "spatialCoverage": [{"@type": "Place", "name": p["name"]} for p in PARKS],
         "isBasedOn": ["https://www.nps.gov/subjects/developer/api-documentation.htm", "https://www.weather.gov/documentation/services-web-api"],
         "distribution": [{"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": BASE + "conditions.json"},
                          {"@type": "DataDownload", "encodingFormat": "text/markdown", "contentUrl": BASE + "llms.txt"}]},
    ]}
    return '\n  <script type="application/ld+json">' + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + '</script>'

rel = ""
cards = []
for p in PARKS:
    cl = "; ".join(c["name"].split(" (")[0] for c in p["closed"])
    cards.append(f'''<div class="card park-card"><p class="meta">{e(p["state"])}</p><h3><a class="title-link" href="parks/{p["slug"]}/index.html">{e(p["short"])}</a></h3><p class="tag">{e(p["tagline"])}</p>{ent_pills(p, rel)}<p style="margin-top:.75rem;font-size:.85rem"><strong>Closed / limited:</strong> {e(cl)}</p></div>''')
home_keys = []
for p in PARKS: home_keys += p["summary_sources"]
home_keys += ["nps-api", "nws", "goes-app"]
body = f'''
    <section class="hero park-hero">
      <img class="hero-pattern" src="assets/brand/pattern/Pattern_TopRight.svg" alt="" aria-hidden="true">
      <div class="wrap-narrow">
        <span class="badge">{e(WEEK["label"])}</span>
        <h1>What's open this week — and what to know before you go.</h1>
        <p class="lead">ParkReady Guides are weekly entrance briefings for America's busiest national parks: which entrances are open, this week's official closures and weather, and what to prepare for at that entrance and season — bears, bison, thermal ground, ice, flash floods, altitude. Every fact links to the National Park Service or National Weather Service page it came from.</p>
        <div class="actions">
          <a class="btn btn-secondary" href="#parks">Find your park</a>
          <a class="btn btn-primary" href="#get-goes">Get GOES before you lose signal</a>
        </div>
        {offline_callout("Many park entrances are the last reliable signal you'll have. Download GOES at the gate so its medical assessment, how-to guides and prevention tips work with zero bars.", "-top")}
      </div>
    </section>

    <section class="section" id="parks">
      <div class="wrap">
        <p class="eyebrow">First batch · 6 parks · 17 entrances</p>
        <h2>National parks this week</h2>
        <p class="section-intro">Mid-November is shoulder season: many entrances and high roads are closed, services are thin, and weather turns fast. We only publish pages for entrances that are open; closures are listed on each park page.</p>
        <div class="grid grid-2">{"".join(cards)}</div>
      </div>
    </section>

    <section class="section-dark">
      <div class="wrap">
        <h2>Get GOES on your phone before the gate.</h2>
        <p class="section-intro">Download it while you still have signal. After the gate, you may not.</p>
        <div class="grid grid-3 why-grid">
          <div class="card"><h3>Offline by design</h3><p>Interactive health assessment, 50+ visual how-to guides and 200+ prevention tips across 60+ medical topics, all on your phone with no cell service.</p></div>
          <div class="card"><h3>Risks for where you are</h3><p>Location-specific indicators for bears, venomous snakes and other wildlife, plus hypothermia, frostbite, heat illness, altitude illness, ticks, poisonous plants, UV and smoke.</p></div>
          <div class="card"><h3>Written by wilderness doctors</h3><p>Founded by Dr. Grant Lipman, former Stanford Emergency Medicine professor and director of its wilderness medicine fellowship. Chief Medical Officer: Dr. Colin Little, MD, FAWM.</p></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap-narrow prose">
        <p class="eyebrow">How ParkReady works</p>
        <h2>Updated weekly. Sourced, not guessed.</h2>
        <p>Each week we pull official alerts and operating hours from the NPS Data API, read each park's conditions, roads and news pages, and grab National Weather Service point forecasts for every entrance. Pages show a "Week of" label and list every source, so you can check anything yourself.</p>
        <p>We don't publish entrance wait times, bear sightings, or incident counts we can't source. If NPS hasn't said it, neither do we. Conditions change hourly in winter, so check the linked NPS page or call the park's road line the morning you go.</p>
        <p class="rules-note">Follow official NPS rules, posted closures and ranger instructions. ParkReady Guides is not affiliated with the National Park Service.</p>
      </div>
    </section>
{cta_band("Put GOES on your phone before the entrance so wildlife, weather and injury guidance is ready once you're in the park — even with no signal.", rel, "-band")}
{sources_section(home_keys)}'''
URLS.insert(0, "")
write("index.html", page(rel, "ParkReady Guides — National Park Entrance Conditions & Safety, This Week | GOES Health",
      "Weekly national park entrance briefings: open entrances, official NPS closures, NWS forecasts, and what to prepare for this week — plus the GOES app, your outdoor safety companion that works offline.",
      "", body, active="home", extra_head=jsonld()))

# ---------------- sitemap / robots
lastmod = WEEK["fetched"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{BASE}{u}</loc><lastmod>{lastmod}</lastmod><changefreq>weekly</changefreq></url>\n" for u in URLS) + "</urlset>\n"
write("sitemap.xml", sm)
agent_files = agents.emit(ROOT, BASE, D, COND, URLS, write)
write(".nojekyll", "")
print("built", len(URLS), "pages +", len(agent_files), "agent files (llms.txt, markdown, conditions.json, robots.txt)")
