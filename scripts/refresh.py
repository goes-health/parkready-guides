#!/usr/bin/env python3
"""Weekly refresh for ParkReady Guides.

  python3 scripts/refresh.py --fetch     # pull fresh NPS alerts/parks + NWS forecasts into data/raw/
  python3 scripts/refresh.py             # compile data/raw/* into data/conditions.json (no network)

NPS Data API: set NPS_API_KEY (free key from https://www.nps.gov/subjects/developer/get-started.htm).
Falls back to DEMO_KEY (rate-limited). NWS (api.weather.gov) needs no key.
After refreshing: diff data/conditions.json, update scripts/parks/*.py for anything that changed,
bump WEEK in scripts/content.py, then run scripts/build.py.
"""
import json, os, subprocess, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw")
CODES = ["yell", "yose", "grca", "grsm", "zion", "glac"]

def curl(url, out):
    subprocess.run(["curl", "-s", "--max-time", "40", "-A", "ParkReadyGuides/0.1 (cbarcenas@goes.health)", url, "-o", out], check=False)

def fetch():
    key = os.environ.get("NPS_API_KEY", "DEMO_KEY")
    for c in CODES:
        curl(f"https://developer.nps.gov/api/v1/alerts?parkCode={c}&limit=100&api_key={key}", os.path.join(RAW, f"alerts-{c}.json"))
    curl(f"https://developer.nps.gov/api/v1/parks?parkCode={','.join(CODES)}&limit=10&api_key={key}", os.path.join(RAW, "parks.json"))
    curl(f"https://developer.nps.gov/api/v1/newsreleases?parkCode={','.join(CODES)}&limit=60&sort=-releaseDate&api_key={key}", os.path.join(RAW, "news.json"))
    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "nws.py")], cwd=ROOT, check=False)

def compile_():
    out = {"compiled_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
           "note": "Machine-fetched facts. Editorial page copy lives in scripts/parks/*.py and data/parks.json.",
           "sources": {"nps_alerts": "https://developer.nps.gov/api/v1/alerts", "nps_parks": "https://developer.nps.gov/api/v1/parks",
                       "nws": "https://api.weather.gov/"},
           "parks": {}}
    parks = {p["parkCode"]: p for p in json.load(open(os.path.join(RAW, "parks.json")))["data"]}
    news = json.load(open(os.path.join(RAW, "news.json"))).get("data", []) if os.path.exists(os.path.join(RAW, "news.json")) else []
    for c in CODES:
        a = json.load(open(os.path.join(RAW, f"alerts-{c}.json"))).get("data", [])
        p = parks.get(c, {})
        out["parks"][c] = {
            "name": p.get("fullName"), "url": p.get("url"),
            "alerts": [{"title": x["title"], "category": x["category"], "description": x["description"], "url": x.get("url") or None,
                        "last_indexed": x.get("lastIndexedDate")} for x in a],
            "operating_hours": [{"name": o["name"], "description": o["description"], "exceptions": [
                {"name": e["name"], "start": e["startDate"], "end": e["endDate"]} for e in o.get("exceptions", [])]} for o in p.get("operatingHours", [])],
            "entrance_fees": [{"title": f["title"], "cost": f["cost"]} for f in p.get("entranceFees", [])],
            "weather_info": p.get("weatherInfo"),
            "recent_news": [{"date": n["releaseDate"][:10], "title": n["title"], "url": n["url"]} for n in news if c in n.get("parkCode", "").split(",")][:8],
        }
    out["nws"] = json.load(open(os.path.join(RAW, "nws", "forecasts.json")))
    json.dump(out, open(os.path.join(ROOT, "data", "conditions.json"), "w"), indent=1, ensure_ascii=False)
    print("wrote data/conditions.json:", {c: len(v["alerts"]) for c, v in out["parks"].items()}, "alerts;", len(out["nws"]), "NWS points")

if __name__ == "__main__":
    if "--fetch" in sys.argv: fetch()
    compile_()
