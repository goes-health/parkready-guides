# ParkReady Guides — review notes (first batch, Week of Nov 9–15, 2026)

Built Thu Nov 12, 2026 (JST). This is a standalone static site, separate from HeatReady. There's no git repo and nothing is published. Preview it locally with `cd /workspace/goes-parks && python3 -m http.server 8765`, then open http://localhost:8765/.

## Pages (24 total)
| Page | Path |
|---|---|
| Home (what ParkReady is, why download GOES first, park and entrance index) | `index.html` |
| Yellowstone overview | `parks/yellowstone/index.html` |
| · North Entrance (Gardiner) | `parks/yellowstone/north-entrance.html` |
| · Northeast Entrance (Cooke City/Silver Gate) | `parks/yellowstone/northeast-entrance.html` |
| Yosemite overview | `parks/yosemite/index.html` |
| · Arch Rock (Hwy 140) | `parks/yosemite/arch-rock-entrance.html` |
| · Big Oak Flat (Hwy 120 W) | `parks/yosemite/big-oak-flat-entrance.html` |
| · South (Hwy 41) | `parks/yosemite/south-entrance.html` |
| · Hetch Hetchy | `parks/yosemite/hetch-hetchy-entrance.html` |
| Grand Canyon overview | `parks/grand-canyon/index.html` |
| · South Entrance (Tusayan) | `parks/grand-canyon/south-entrance.html` |
| · Desert View / East | `parks/grand-canyon/desert-view-east-entrance.html` |
| · North Rim (limited, closing) | `parks/grand-canyon/north-rim-entrance.html` |
| Great Smoky Mountains overview | `parks/great-smoky-mountains/index.html` |
| · Gatlinburg (Sugarlands) | `parks/great-smoky-mountains/gatlinburg-entrance.html` |
| · Townsend | `parks/great-smoky-mountains/townsend-entrance.html` |
| · Cherokee (Oconaluftee) | `parks/great-smoky-mountains/cherokee-entrance.html` |
| Zion overview | `parks/zion/index.html` |
| · South (Springdale) | `parks/zion/south-entrance.html` |
| · East (Mt. Carmel Jct) | `parks/zion/east-entrance.html` |
| · Kolob Canyons | `parks/zion/kolob-canyons-entrance.html` |
| Glacier overview | `parks/glacier/index.html` |
| · West Entrance (West Glacier) | `parks/glacier/west-entrance.html` |
| · St. Mary | `parks/glacier/st-mary-entrance.html` |

The site also includes `sitemap.xml` (24 URLs on https://parks.goes.health/), `robots.txt`, `.nojekyll`, and a canonical tag plus Open Graph tags on every page.

Each entrance page includes:
- a "Week of" badge;
- the official conditions for that entrance, with every line linked to its NPS or NWS source;
- the entrance fee;
- an NWS forecast table. It shows the build-time snapshot and switches to the live api.weather.gov forecast and alerts in the browser when online;
- 3–4 risk cards for that entrance, each with an "In GOES" line that maps the risk to an app feature using App Store wording;
- a "before you go in" checklist;
- park-wide risk cards;
- every active NPS alert, pulled from the NPS API;
- a GOES CTA near the top and a full CTA band, both with App Store and Google Play buttons and a reason tied to that park;
- the verbatim disclaimer and a line telling visitors to follow NPS rules and ranger instructions;
- links to the park's other entrances and a numbered source list.

The footer adds "not affiliated with the National Park Service".

## Data files
- `data/parks.json` holds all editorial content, the GOES links and claims, and a registry of 65 source URLs. It's generated from `scripts/content.py` and `scripts/parks/*.py`, which are the files to edit.
- `data/conditions.json` holds the machine-fetched facts for each park: NPS alerts, operating hours and exceptions, fees, recent NPS news, and the NWS forecast and alerts for all 19 entrance points, each with a timestamp.
- `data/raw/` holds the raw API JSON plus the HTML and text of every NPS page I read, as an audit trail. It's gitignored.

## How the weekly update should work (a routine can do this)
1. Run `NPS_API_KEY=… python3 scripts/refresh.py --fetch`. It re-pulls NPS alerts, parks and news, plus the NWS forecasts. It falls back to DEMO_KEY, which is rate-limited, so get a free NPS key.
2. Diff `data/conditions.json` and re-read the conditions page for each park (URLs are in the source registry). Update `scripts/parks/*.py` for anything that changed: closures, shuttle dates, advisories, forecast sentences. Bump `WEEK` in `scripts/content.py`.
3. Run `python3 scripts/build.py` to re-render all pages and the sitemap lastmod. Re-take previews with `scripts/screenshots.py`.
4. Add or drop entrance pages as entrances open or close. Next obvious changes:
   - Yellowstone West, South and East open to oversnow travel Dec 15.
   - Zion's shuttle stops Nov 29.
   - Kuwohi Road and Roaring Fork in the Smokies close Nov 29.
   - The Grand Canyon North Rim gate closes by Nov 30.
   - Many Glacier Road closes the third weekend of November.
   - Grand Canyon water and lodging may come back around Thanksgiving.

The risk sentences that quote the forecast (e.g. "snow showers Friday") are dated. They're the main thing to rewrite each week.

## Closures and surprises found (all from official sources fetched today)
- **Grand Canyon is day use only.** An Aug 29 flash flood broke the Transcanyon Waterline. That means:
  - Stage 4 water restrictions on the South Rim;
  - in-park overnight lodging suspended, dry camping only;
  - "bring your own water";
  - Phantom Ranch, both river bridges and the entire North Kaibab Trail closed, with no reopening estimate;
  - inner-canyon water off for the winter.

  In September NPS projected water pumping around Nov 16 and phased overnight service around Thanksgiving, and called those dates tentative. This is the biggest one.
- **North Rim:** open for limited day use only, with no services or fuel. The gate closes at sunset Nov 30 or at the first major snowstorm, and NWS forecasts snow showers there this Friday and Saturday. One NPS field (directionsInfo in the API) still says "Oct 1–Nov 14", which conflicts with the Sept 30 news release. I followed the news release, but the page says "check before you drive".
- **Yellowstone:** West, South and East entrances have been closed to cars since Nov 1. Only the North ↔ Northeast road is open. The Gardner River High Bridge has delays through Nov 24, and Biscuit Basin is still closed. NPS pages disagree on the East Entrance oversnow opening (Dec 15 vs Dec 22), and the page flags that.
- **Yosemite:** Tioga Road and Glacier Point Road temporarily close **today, Nov 12, at 5 pm** (forecast snow). That's why there's no Tioga page. There's an NWS Winter Storm Watch until Nov 17 for the South Entrance area. Dome Fire closures remain near Glacier Point Road.
- **Smokies:** NWS Winter Weather Advisory for Gatlinburg and Townsend until Nov 14, 7 am EST, with snow showers forecast at Newfound Gap Friday. Laurel Falls Trail is still closed, and the Bullhead Trail is closed Mon–Thu through Nov 19.
- **Zion:**
  - the Zion–Mt. Carmel Highway reopened Oct 9 after a Sept 30 rockfall, with a temporary gravel section;
  - Watchman Trail and Hidden Canyon are closed;
  - the cyanobacteria advisory is still on;
  - the shuttle ends Nov 28.
- **Glacier:**
  - Going-to-the-Sun Road is closed for the season at Avalanche Creek and Jackson Glacier Overlook;
  - **tularemia** was confirmed in Many Glacier (Oct 15) and the St. Mary Lake area (Sept 17);
  - there's no fuel or lodging in the park.
- **New fee:** the NPS API lists a **$100 nonresident fee** (non-US residents 16+, on top of the entrance fee) at Yellowstone, Yosemite, Grand Canyon, Zion and Glacier. It's mentioned in the fee lines on every page except the Smokies, which has no entrance fee.

## Things I deliberately left out or couldn't verify
- No wait times, bear-activity reports, incident counts or crowd levels unless NPS published them. The exceptions are NPS's own stats: Yellowstone's 91% figure and its 20+ hot-spring deaths, the Smokies' 339 negative bear encounters a year, Glacier's ~1,000 bears and its "no attacks on groups of 4+", and Yosemite's 300–500 black bears. The Grand Canyon "up to 2 hours" line is NPS's general guidance and is labeled that way.
- I couldn't get Glacier's live status for Many Glacier and Two Medicine roads (the NPS map is JavaScript-only), so those have no pages. The park page says to confirm by texting GNPROADS to 333111.
- Glacier's Apgar weekend winter hours come from an older NPS winter page, and the copy attributes them to that page. Whether the Smokies' rut-season field closures at Oconaluftee are still in effect isn't confirmed, so the copy says "obey posted closures".
- The cell-coverage messaging is phrased as "don't count on signal" and backed by NPS's own wording ("if cell service is available, dial 911"; "areas without cellular service"). I made no coverage claims for specific entrances.
- GOES claims come only from the App Store and Google Play listing and goes.health:
  - offline interactive assessment and 50+ how-to guides;
  - wildlife, hypothermia, frostbite, heat, altitude, tick, plant, UV and smoke risks;
  - 200+ tips across 60+ topics;
  - 7-day trial, then a subscription.

  Lipman and Little credentials come from the OIA press release and goes.health. I did **not** use "trusted by national parks" or "built with NPS PSAR rangers". Both appear in GOES marketing, but they could read as NPS endorsement on a park site.
- I used no official store badge artwork; the store buttons are styled text buttons. There are no affiliate links, reviews or ratings.

## Decisions for Camilo
1. **Domain and hosting:** parks.goes.health on GitHub Pages, a new repo like `goes-health/parkready-guides`, the same flow as HeatReady. A CNAME `parks` → `goes-health.github.io` at SiteGround.
2. **Name:** "ParkReady Guides by GOES Health" is used throughout. Is that OK?
3. **Attribution:** do you want App Store campaign tokens (`?ct=parkready-<park>-<entrance>`) and Play `referrer`/UTM on the store links, so downloads can be attributed per page? Each button already has a `data-cta` hook.
4. **Grand Canyon tone:** the page leads with the water and lodging emergency. Keep it that prominent?
5. **Should the NPS-ranger / "trusted by national parks" claims stay off this site?** That's my recommendation.
6. **Next parks:** Rocky Mountain, Grand Teton, Acadia, Joshua Tree, Death Valley, Olympic, Arches and Canyonlands. Winter brings demand for desert parks.
7. Confirm before the parent briefs the trip-planning agents: they should link the entrance page matching the traveler's route and date, and mention downloading GOES before the gate.

## Previews (`previews/`)
- Home: `home-desktop.png` (full page), `home-desktop-fold.png`, `home-mobile.png`
- Yellowstone North Entrance: `yellowstone-north-entrance-{desktop,desktop-fold,mobile}.png`
- Grand Canyon South Entrance: `grand-canyon-south-entrance-{desktop,desktop-fold,mobile}.png`
- Yosemite South Entrance: `yosemite-south-entrance-{desktop,desktop-fold,mobile}.png`
- Yellowstone park overview: `yellowstone-park-{desktop,desktop-fold,mobile}.png`

The mobile renders are 390 px wide at 2x.
