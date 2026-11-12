# ParkReady Guides — by GOES Health

Weekly national-park entrance briefings (open entrances, official NPS closures, NWS forecasts, real seasonal risks) that drive downloads of the GOES offline outdoor-safety app.

- Static site, no build dependencies beyond Python 3 + bs4 (for refresh only). Publish the repo root (`index.html`, `parks/`, `assets/`, `sitemap.xml`, `robots.txt`, `.nojekyll`).
- Live at https://parks.goes.health/
- Editorial copy: `scripts/content.py` + `scripts/parks/*.py` → exported to `data/parks.json`.
- Machine-fetched facts: `data/conditions.json` (NPS alerts, operating hours, fees, recent NPS news, NWS forecasts) compiled from `data/raw/`.

## Weekly update
```
NPS_API_KEY=xxxx python3 scripts/refresh.py --fetch   # NPS Data API + api.weather.gov -> data/raw, data/conditions.json
git diff data/conditions.json                          # what changed?
# edit scripts/parks/*.py for any changed closures/hours; bump WEEK in scripts/content.py
python3 scripts/build.py                               # renders all pages + sitemap
```
Entrance pages also load the live NWS forecast in the browser (assets/js/live-forecast.js); the build-time snapshot is the fallback.
