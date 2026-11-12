src("zion-cond", "Zion Current Conditions", "https://www.nps.gov/zion/planyourvisit/conditions.htm")
src("zion-hours", "Zion operating hours & facility hours", "https://www.nps.gov/zion/planyourvisit/hours.htm")
src("zion-shuttle", "Zion Canyon shuttle schedule", "https://www.nps.gov/zion/planyourvisit/zion-canyon-shuttle-system.htm")
src("zion-zmch", "News release: Zion-Mt. Carmel Highway reopens (Oct 9, 2026)", "https://www.nps.gov/zion/learn/news/2026-10-09-zmch.htm")
src("zion-large", "Zion large-vehicle restrictions", "https://www.nps.gov/zion/planyourvisit/large-vehicles.htm")
src("zion-cyano", "Zion toxic cyanobacteria advisory", "https://www.nps.gov/zion/planyourvisit/toxic-cyanobacteria-bloom-in-the-virgin-river-and-the-streams-of-zion-national-park.htm")
src("zion-angels", "Angels Landing permits", "https://www.nps.gov/zion/planyourvisit/angels-landing-hiking-permits.htm")
src("zion-kolob", "Kolob Canyons", "https://www.nps.gov/zion/planyourvisit/kolob-canyons.htm")
src("zion-safety", "Zion safety: flash floods, cliffs, hypothermia, water", "https://www.nps.gov/zion/planyourvisit/safety.htm")

PARKS.append({
 "slug": "zion", "code": "zion", "name": "Zion National Park", "short": "Zion",
 "state": "UT",
 "tagline": "Shuttle season ends Nov 28; cool days, cold canyon water, storms Friday night.",
 "summary": "Zion is open 24/7 year-round. The Zion Canyon shuttle is on its late-fall schedule through Nov 28 (first bus 7 am, last bus up-canyon 5 pm, last bus out of Temple of Sinawava 6:15 pm), with no shuttle service Nov 29 – Dec 25. NWS forecasts sunny days Thursday, then rain and thunderstorms Friday night into Saturday. The Narrows closes whenever NWS issues a Flash Flood Warning or the Virgin River tops 150 cfs.",
 "summary_sources": ["zion-shuttle", "zion-hours", "nws", "zion-cond"],
 "cta_reason": "Flash floods, cliff edges, cold water that causes hypothermia, and toxic cyanobacteria in the river. GOES carries offline guidance for all of these.",
 "fees": "Private vehicle $35. Non-US residents 16+ pay an additional $100 nonresident fee unless entering with an annual / America the Beautiful pass. Angels Landing requires a separate permit.",
 "fees_sources": ["zion-fees", "nps-api", "zion-angels"],
 "closed": [
   {"name": "Watchman Trail", "note": "Closed pending repairs.", "sources": ["zion-alerts"]},
   {"name": "Hidden Canyon / Observation Point from Zion Canyon", "note": "The East Rim Trail is partially closed by a large rockfall: Hidden Canyon is closed, and Observation Point can only be reached from the east.", "sources": ["zion-cond"]},
 ],
 "park_risks": [
   R("Flash floods", "Flash floods can happen at any time in Zion, carrying trees and boulders. The Narrows closes when flow exceeds 150 cfs or when NWS issues a Flash Flood Warning. Rain and thunderstorms are forecast Friday night into Saturday this week.", ["zion-safety", "zion-cond", "nws"], "weather"),
   R("Toxic cyanobacteria", "Don't drink water from rivers, streams or pools, and don't submerge your head in them. Use potable water, and treat spring water only as a last resort.", ["zion-cyano", "zion-alerts"], "injury"),
   R("Hypothermia in the canyons", "NPS: hypothermia is a major hazard in narrow canyons, and immersion in water is the fastest way to lose body heat. Avoid cotton and eat before you get chilled.", ["zion-safety"], "cold"),
   R("Cliffs", "Falls from cliffs on trails have caused deaths. Loose sand on stone is slippery, so stay on the trail and back from edges.", ["zion-safety"], "injury"),
 ],
 "entrances": [
  {
   "slug": "south-entrance", "name": "South Entrance", "gateway": "Springdale, UT (SR-9)", "nws": "zion-south", "status": "open",
   "status_label": "Open — shuttle through Nov 28",
   "intro": "The South Entrance at Springdale leads to the Zion Canyon Visitor Center, where shuttles leave for the Zion Canyon Scenic Drive, the Riverside Walk and The Narrows.",
   "conditions": [
     C("Zion Canyon shuttle, Oct 25 – Nov 28: first bus 7 am from the Visitor Center, last bus up-canyon 5 pm, last bus out of Temple of Sinawava 6:15 pm. No service Nov 29 – Dec 25. Springdale Line: 8 am – 6 pm through Nov 28.", ["zion-shuttle"], "open"),
     C("Zion Canyon Visitor Center, park store and wilderness desk: 8 am – 5 pm. Human History Museum: 10 am – 5 pm.", ["zion-hours"], None),
     C("Watchman Trail is closed pending repairs and Hidden Canyon is closed (rockfall). Angels Landing requires a permit.", ["zion-alerts", "zion-cond", "zion-angels"], "closed"),
     C("Parking is limited. When park lots fill, park in Springdale; vehicles outside designated spaces can be cited and towed.", ["zion-alerts"], "caution"),
     C("Watchman Campground is open year-round (reservations required). South Campground closes seasonally in winter.", ["zion-cond", "zion-hours"], None),
   ],
   "risks": [
     R("The Narrows in November", "Cold water and short days. Check USGS flow and the NWS forecast the morning you go; the route closes at 150 cfs or under a Flash Flood Warning. Showers and thunderstorms are forecast Friday night and Saturday.", ["zion-cond", "nws"], "cold"),
     R("Don't miss the last shuttle", "NPS says not to wait for the last shuttle of the day. Being stuck in the canyon after dark in November means a long, cold walk out.", ["zion-shuttle"], "cold"),
     R("Cyanobacteria in the Virgin River", "Don't drink river water or put your head under. NPS's advisory covers rivers, streams and pools parkwide.", ["zion-cyano"], "injury"),
   ],
   "prep": [
     ("Arrive early or park in Springdale", "Lots fill, and towing is enforced."),
     ("Note the last shuttle times", "Last bus up-canyon 5 pm; last out 6:15 pm through Nov 28."),
     ("A gallon of water per person per day", "NPS's desert rule applies even when it's cool."),
     ("Download GOES in Springdale", "Don't count on coverage in the canyon."),
   ],
   "cta_reason": "Flash floods, cold canyon water and cliff-edge trails. Download GOES in Springdale; its offline assessment and how-to guides work deep in the canyon.",
  },
  {
   "slug": "east-entrance", "name": "East Entrance", "gateway": "Mt. Carmel Junction, UT (SR-9)", "nws": "zion-east", "status": "open",
   "status_label": "Open — gravel section, size limits",
   "intro": "The East Entrance west of Mt. Carmel Junction starts the Zion–Mt. Carmel Highway: slickrock country, the Canyon Overlook Trail, and the historic tunnel down to Zion Canyon.",
   "conditions": [
     C("The Zion–Mt. Carmel Highway reopened to visitors Oct 9 after a Sept 30 rockfall. One section is temporarily gravel until it's repaved, so drive with caution and watch for crews and pedestrians.", ["zion-zmch"], "caution"),
     C("Large-vehicle restrictions: vehicles over the length, width, height or weight limits can't travel between Canyon Junction and the East Entrance and must go around through Springdale.", ["zion-alerts", "zion-large"], "caution"),
     C("Personal vehicles are allowed on the Zion–Mt. Carmel Highway year-round, including during shuttle season.", ["zion-hours"], "open"),
   ],
   "risks": [
     R("Slickrock edges", "Canyon Overlook and the slickrock pullouts have drop-offs. Sand on stone is slippery: stay back from edges and watch kids.", ["zion-safety"], "injury"),
     R("Colder, higher side of the park", "NWS forecast near the East Entrance: lows in the upper 30s, highs around 56–61°F, then rain and thunderstorms Friday night into Saturday.", ["nws"], "cold"),
     R("Lightning and flash floods", "Storms are in the forecast. NPS warns flash floods can occur at any time in Zion; avoid washes and narrow canyons when storms are around.", ["zion-safety", "nws"], "weather"),
   ],
   "prep": [
     ("Check your vehicle size", "Oversize vehicles must go around through Springdale."),
     ("Allow time for the gravel section", "A temporary surface after the rockfall."),
     ("Download GOES before Mt. Carmel Junction", "Plan for thin coverage on the east side."),
   ],
   "cta_reason": "Slickrock drop-offs, a cold, stormy weekend and a rebuilt road. Download GOES before Mt. Carmel Junction so its offline injury guidance is ready.",
  },
  {
   "slug": "kolob-canyons-entrance", "name": "Kolob Canyons Entrance", "gateway": "I-15 Exit 40 (near Cedar City)", "nws": "zion-kolob", "status": "open",
   "status_label": "Open — may close for snow or ice",
   "intro": "Kolob Canyons is Zion's quieter northwest district, at I-15 Exit 40, 17 miles south of Cedar City and about an hour from Zion Canyon. A five-mile scenic drive leads to viewpoints and wilderness trails.",
   "conditions": [
     C("Kolob Canyons Visitor Center: 8 am – 12 pm and 1 pm – 5 pm. All visitors must stop to show a pass or pay the entrance fee. The Kolob wilderness desk is closed until further notice; get wilderness permits in Zion Canyon.", ["zion-hours", "zion-kolob"], None),
     C("Kolob Canyons Road may close in winter for snow or ice, and pedestrians may not walk the road during plowing.", ["zion-kolob"], "caution"),
     C("Personal vehicles are allowed on Kolob Canyons Scenic Drive year-round.", ["zion-hours"], "open"),
   ],
   "risks": [
     R("Cold, exposed wilderness trails", "NWS forecast for Kolob: highs near 56–61°F, lows around 40°F, and showers and thunderstorms Friday night into Saturday. These are designated wilderness trails with few people around to help.", ["nws", "zion-kolob"], "cold"),
     R("Flash floods in narrow canyons", "Know the forecast before entering any narrow canyon and have a plan to reach high ground.", ["zion-safety"], "weather"),
   ],
   "prep": [
     ("Pay or show a pass at the visitor center", "Required for all visitors."),
     ("Get wilderness permits in Zion Canyon", "The Kolob desk is closed."),
     ("Download GOES before leaving I-15", "Offline guidance for remote trails."),
   ],
   "cta_reason": "Remote wilderness, cold weather and flash-flood canyons. Get GOES before you leave I-15 so its offline guidance comes with you.",
  },
 ],
})
