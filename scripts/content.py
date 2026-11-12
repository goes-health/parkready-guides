"""ParkReady Guides — editorial content for the week of Nov 9–15, 2026.
Every 'this week' fact cites a source key from S. Facts were fetched on
2026-11-12 (JST) from nps.gov, the NPS Data API, and api.weather.gov.
Weekly: run scripts/refresh.py, review/edit the park content files, rebuild.
"""
import json, os, glob

WEEK = {"label": "Week of Nov 9–15, 2026", "start": "2026-11-09", "end": "2026-11-15",
        "fetched": "2026-11-12", "fetched_note": "Fetched Thu Nov 12, 2026 (JST), which is Wed Nov 11 evening in US time zones."}

S = {}
def src(key, label, url): S[key] = {"label": label, "url": url}

for code, name in [("yell","Yellowstone"),("yose","Yosemite"),("grca","Grand Canyon"),("grsm","Great Smoky Mountains"),("zion","Zion"),("glac","Glacier")]:
    src(f"{code}-alerts", f"NPS {name} alerts (NPS Data API, fetched Nov 12)", f"https://www.nps.gov/{code}/planyourvisit/conditions.htm")
    src(f"{code}-home", f"NPS {name} National Park", f"https://www.nps.gov/{code}/index.htm")
    src(f"{code}-fees", f"NPS {name} fees & passes", f"https://www.nps.gov/{code}/planyourvisit/fees.htm")
src("nps-api", "NPS Data API (parks, operating hours, fees)", "https://www.nps.gov/subjects/developer/api-documentation.htm")
src("nws", "National Weather Service point forecasts (api.weather.gov, fetched Nov 12)", "https://www.weather.gov/")
src("airnow", "AirNow fire & smoke map", "https://fire.airnow.gov/")
src("goes-app", "GOES app listing (App Store)", "https://apps.apple.com/us/app/goes-outdoor-health-safety/id1576527901")

GOES = {
  "ios": "https://apps.apple.com/us/app/goes-outdoor-health-safety/id1576527901",
  "android": "https://play.google.com/store/apps/details?id=com.goes.mobile",
  "site": "https://goes.health/", "platform": "https://goes.health/platform",
  "disclaimer": "GOES provides guidance. It is not a substitute for professional medical care.",
}

# Wording mirrors the GOES App Store / Google Play listing.
GOES_TAGS = {
  "bears": "Wildlife Encounters: location-specific risk indicators for bears and other dangerous animals",
  "wildlife": "Wildlife Encounters: location-specific risk indicators for dangerous animals",
  "snakes": "Wildlife Encounters (venomous snakes) + Poisonous Plants (poison oak, ivy, sumac)",
  "cold": "Environmental Health: hypothermia and frostbite assessments",
  "heat": "Environmental Health: heat illness assessment",
  "altitude": "High Altitude Illness: personalized altitude risk",
  "smoke": "Respiratory Hazards: smoke, pollution and pollen (AQI) monitoring",
  "uv": "Sunburn: UV-based burn risk",
  "ticks": "Tick Risk: location- and season-specific tick activity",
  "injury": "Offline interactive health assessment + 50+ visual how-to guides",
  "weather": "125+ extreme weather alerts",
}

def R(title, body, srcs, goes=None):
    return {"title": title, "body": body, "sources": srcs, "goes": goes}

def C(text, srcs, status=None):
    return {"text": text, "sources": srcs, "status": status}

PARKS = []
_here = os.path.dirname(os.path.abspath(__file__))
for f in sorted(glob.glob(os.path.join(_here, "parks", "*.py"))):
    exec(open(f).read())

if __name__ == "__main__":
    out = {"week": WEEK, "goes": GOES, "goes_tags": GOES_TAGS, "sources": S, "parks": PARKS}
    json.dump(out, open(os.path.join(_here, "..", "data", "parks.json"), "w"), indent=1, ensure_ascii=False)
    bad = set()
    for p in PARKS:
        keys = list(p["summary_sources"]) + list(p["fees_sources"])
        for c in p["closed"]: keys += c["sources"]
        for r in p["park_risks"]: keys += r["sources"]
        for e in p["entrances"]:
            for c in e["conditions"]: keys += c["sources"]
            for r in e["risks"]: keys += r["sources"]
        bad |= {k for k in keys if k not in S}
    print("parks:", len(PARKS), "entrances:", sum(len(p["entrances"]) for p in PARKS), "missing source keys:", bad or "none")
