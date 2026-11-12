#!/usr/bin/env python3
"""Ping IndexNow (Bing, Yandex, Seznam, Naver, ...) after a weekly publish.
Usage: python3 scripts/indexnow.py            # submit llms.txt, feed, sitemap and every page
       python3 scripts/indexnow.py --dry-run
Key lives in data/indexnow.json; build.py publishes it as <key>.txt at the site root.
No account or login needed. Run only after GitHub Pages has finished deploying."""
import json, os, sys, urllib.request, urllib.parse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.environ.get("PARKREADY_BASE", "https://goes-health.github.io/parkready-guides/")
key = json.load(open(os.path.join(ROOT, "data", "indexnow.json")))["key"]
D = json.load(open(os.path.join(ROOT, "data", "parks.json")))
urls = [BASE, BASE + "llms.txt", BASE + "conditions.json", BASE + "sitemap.xml", BASE + "index.md"]
for p in D["parks"]:
    urls += [f'{BASE}parks/{p["slug"]}/', f'{BASE}parks/{p["slug"]}/index.md']
    for en in p["entrances"]:
        urls += [f'{BASE}parks/{p["slug"]}/{en["slug"]}.html', f'{BASE}parks/{p["slug"]}/{en["slug"]}.md']
body = {"host": urllib.parse.urlparse(BASE).netloc, "key": key, "keyLocation": f"{BASE}{key}.txt", "urlList": urls}
if "--dry-run" in sys.argv:
    print(json.dumps(body, indent=1)); sys.exit()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=json.dumps(body).encode(),
                             headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print("IndexNow:", r.status, len(urls), "URLs")
except urllib.error.HTTPError as e:
    print("IndexNow:", e.code, e.read()[:300].decode(errors="replace")); sys.exit(1)
