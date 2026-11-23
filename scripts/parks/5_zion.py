src("zion-cond", "Zion Current Conditions", "https://www.nps.gov/zion/planyourvisit/conditions.htm")
src("zion-hours", "Zion operating hours & facility hours", "https://www.nps.gov/zion/planyourvisit/hours.htm")
src("zion-shuttle", "Zion Canyon shuttle schedule", "https://www.nps.gov/zion/planyourvisit/zion-canyon-shuttle-system.htm")
src("zion-zmch", "News release: Zion-Mt. Carmel Highway reopens (Oct 9, 2026)", "https://www.nps.gov/zion/learn/news/2026-10-09-zmch.htm")
src("zion-large", "Zion large-vehicle restrictions", "https://www.nps.gov/zion/planyourvisit/large-vehicles.htm")
src("zion-cyano", "Zion toxic cyanobacteria advisory", "https://www.nps.gov/zion/planyourvisit/toxic-cyanobacteria-bloom-in-the-virgin-river-and-the-streams-of-zion-national-park.htm")
src("zion-angels", "Angels Landing permits", "https://www.nps.gov/zion/planyourvisit/angels-landing-hiking-permits.htm")
src("zion-kolob", "Kolob Canyons", "https://www.nps.gov/zion/planyourvisit/kolob-canyons.htm")
src("udot-zion", "UDOT Zion Canyon fiber project: construction update (Nov 20, 2026)", "https://udotinput.utah.gov/ziontechnology")
src("zion-narrows", "Zion: The Narrows (permits, closures)", "https://www.nps.gov/zion/planyourvisit/thenarrows.htm")
src("zion-safety", "Zion safety: flash floods, cliffs, hypothermia, water", "https://www.nps.gov/zion/planyourvisit/safety.htm")

PARKS.append({
 "slug": "zion", "code": "zion", "name": "Zion National Park", "short": "Zion",
 "state": "UT",
 "tagline": "Last week of shuttle service (through Nov 28), the tunnel's nightly closures are over, and a sunny week ahead.",
 "summary": "Zion is open 24/7 year-round. The Zion Canyon shuttle is on its late-fall schedule through Nov 28 (first bus 7 am, last bus up-canyon 5 pm, last bus out of Temple of Sinawava 6:15 pm), with no shuttle service Nov 29 – Dec 25. From Nov 29 you can drive the Zion Canyon Scenic Drive in your own car. NPS no longer lists last week's high-water closure of the top-down Narrows route (that through-hike needs a wilderness permit), and the Zion–Mt. Carmel Tunnel's nightly closures for fiber-optic work ended Nov 20. The road to Lava Point and the West Rim Trailhead is now closed for the season. NWS forecasts sunny, dry weather all week, with highs in the upper 50s to upper 60s in Springdale. The Narrows closes whenever NWS issues a Flash Flood Warning or the Virgin River tops 150 cfs.",
 "summary_sources": ["zion-shuttle", "zion-hours", "zion-alerts", "udot-zion", "nws", "zion-cond"],
 "cta_reason": "Flash floods, cliff edges, cold water that causes hypothermia, and toxic cyanobacteria in the river. GOES carries offline guidance for all of these.",
 "fees": "Private vehicle $35. Non-US residents 16+ pay an additional $100 nonresident fee unless entering with an annual / America the Beautiful pass. Angels Landing requires a separate permit.",
 "fees_sources": ["zion-fees", "nps-api", "zion-angels"],
 "closed": [
   {"name": "Lava Point and West Rim Trailhead road", "note": "Regular seasonal closure for snow; Lava Point Overlook is also closed. NPS will lift it when the snow melts.", "sources": ["zion-alerts"]},
   {"name": "Watchman Trail", "note": "Closed pending repairs.", "sources": ["zion-alerts"]},
   {"name": "Hidden Canyon / Observation Point from Zion Canyon", "note": "The East Rim Trail is partially closed by a large rockfall: Hidden Canyon is closed, and Observation Point can only be reached from the east.", "sources": ["zion-cond"]},
 ],
 "park_risks": [
   R("Flash floods", "Flash floods can happen at any time in Zion, carrying trees and boulders. The Narrows closes when flow exceeds 150 cfs or when NWS issues a Flash Flood Warning. This week's NWS forecast is sunny and dry, but always check it the morning you go.", ["zion-safety", "zion-cond", "nws"], "weather"),
   R("Toxic cyanobacteria", "Don't drink water from rivers, streams or pools, and don't submerge your head in them. Use potable water, and treat spring water only as a last resort.", ["zion-cyano", "zion-alerts"], "injury"),
   R("Hypothermia in the canyons", "NPS: hypothermia is a major hazard in narrow canyons, and immersion in water is the fastest way to lose body heat. Avoid cotton and eat before you get chilled.", ["zion-safety"], "cold"),
   R("Cliffs", "Falls from cliffs on trails have caused deaths. Loose sand on stone is slippery, so stay on the trail and back from edges.", ["zion-safety"], "injury"),
 ],
 "entrances": [
  {
   "slug": "south-entrance", "name": "South Entrance", "gateway": "Springdale, UT (SR-9)", "nws": "zion-south", "status": "open",
   "status_label": "Open — last shuttle week",
   "intro": "The South Entrance at Springdale leads to the Zion Canyon Visitor Center, where shuttles leave for the Zion Canyon Scenic Drive, the Riverside Walk and The Narrows.",
   "conditions": [
     C("Zion Canyon shuttle, Oct 25 – Nov 28: first bus 7 am from the Visitor Center, last bus up-canyon 5 pm, last bus out of Temple of Sinawava 6:15 pm. No service Nov 29 – Dec 25, when you can drive the Scenic Drive in your own vehicle. Springdale Line: 8 am – 6 pm through Nov 28.", ["zion-shuttle", "zion-hours"], "open"),
     C("Zion Canyon Visitor Center, park store and wilderness desk: 8 am – 5 pm. Human History Museum: 10 am – 5 pm.", ["zion-hours"], None),
     C("The Narrows: NPS no longer lists last week's high-water closure of the top-down route. Bottom-up to Big Spring needs no permit; the 16-mile top-down through-hike needs a wilderness permit. It closes above 150 cfs or under a Flash Flood Warning.", ["zion-alerts", "zion-narrows"], "open"),
     C("Watchman Trail is closed pending repairs and Hidden Canyon is closed (rockfall). Angels Landing requires a permit.", ["zion-alerts", "zion-cond", "zion-angels"], "closed"),
     C("UDOT fiber work on SR-9 at the west end of Springdale (daytime, through Nov 25): expect one-way traffic with minor delays. Crews pause for the holiday from noon Nov 25.", ["udot-zion"], "caution"),
     C("Parking is limited. When park lots fill, park in Springdale; vehicles outside designated spaces can be cited and towed.", ["zion-alerts"], "caution"),
     C("Watchman Campground is open year-round (reservations required). South Campground closes seasonally in winter.", ["zion-cond", "zion-hours"], None),
   ],
   "risks": [
     R("The Narrows in November", "Cold water and short days. Check USGS flow and the NWS forecast the morning you go; the route closes at 150 cfs or under a Flash Flood Warning. NWS forecasts a dry week in Springdale (highs around 58–68°F, lows near 36–42°F), but the water stays cold, so dress in non-cotton layers.", ["zion-cond", "zion-narrows", "nws"], "cold"),
     R("Don't miss the last shuttle", "NPS says not to wait for the last shuttle of the day. Being stuck in the canyon after dark in November means a long, cold walk out.", ["zion-shuttle"], "cold"),
     R("Cyanobacteria in the Virgin River", "Don't drink river water or put your head under. NPS's advisory covers rivers, streams and pools parkwide.", ["zion-cyano"], "injury"),
   ],
   "prep": [
     ("Arrive early or park in Springdale", "Lots fill, and towing is enforced."),
     ("Note the last shuttle times", "Last bus up-canyon 5 pm; last out 6:15 pm. Final shuttle day is Nov 28."),
     ("A gallon of water per person per day", "NPS's desert rule applies even when it's cool."),
     ("Download GOES in Springdale", "Don't count on coverage in the canyon."),
   ],
   "cta_reason": "Flash floods, cold canyon water and cliff-edge trails. Download GOES in Springdale; its offline assessment and how-to guides work deep in the canyon.",
  },
  {
   "slug": "east-entrance", "name": "East Entrance", "gateway": "Mt. Carmel Junction, UT (SR-9)", "nws": "zion-east", "status": "open",
   "status_label": "Open — tunnel open overnight again",
   "intro": "The East Entrance west of Mt. Carmel Junction starts the Zion–Mt. Carmel Highway: slickrock country, the Canyon Overlook Trail, and the historic tunnel down to Zion Canyon.",
   "conditions": [
     C("Zion–Mt. Carmel Tunnel: last week's nightly fiber-optic closures ended Nov 20. UDOT's Nov 20 update lists no tunnel work this week; fiber crews on US-89 near Mt. Carmel Junction and Orderville are working along the shoulders with minimal traffic impact.", ["zion-alerts", "udot-zion"], "open"),
     C("The Zion–Mt. Carmel Highway reopened to visitors Oct 9 after a Sept 30 rockfall. One section is temporarily gravel until it's repaved, so drive with caution and watch for crews and pedestrians.", ["zion-zmch"], "caution"),
     C("Large-vehicle restrictions: vehicles over the length, width, height or weight limits can't travel between Canyon Junction and the East Entrance and must go around through Springdale.", ["zion-alerts", "zion-large"], "caution"),
     C("Personal vehicles are allowed on the Zion–Mt. Carmel Highway year-round, including during shuttle season.", ["zion-hours"], "open"),
   ],
   "risks": [
     R("Slickrock edges", "Canyon Overlook and the slickrock pullouts have drop-offs. Sand on stone is slippery: stay back from edges and watch kids.", ["zion-safety"], "injury"),
     R("Colder, higher side of the park", "NWS forecast near the East Entrance: sunny and dry all week, highs around 47–57°F, but lows down to about 25°F, so expect frosty mornings.", ["nws"], "cold"),
     R("Short days and flash floods", "This week is dry, but NPS warns flash floods can occur at any time in Zion; avoid washes and narrow canyons when storms are around, and plan around a late-November sunset.", ["zion-safety", "nws"], "weather"),
   ],
   "prep": [
     ("Tunnel is open around the clock again", "Nightly closures ended Nov 20."),
     ("Check your vehicle size", "Oversize vehicles must go around through Springdale."),
     ("Allow time for the gravel section", "A temporary surface after the rockfall."),
     ("Download GOES before Mt. Carmel Junction", "Plan for thin coverage on the east side."),
   ],
   "cta_reason": "Slickrock drop-offs, frosty mornings and a rebuilt road. Download GOES before Mt. Carmel Junction so its offline injury guidance is ready.",
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
     R("Cold, exposed wilderness trails", "NWS forecast for Kolob: sunny and dry, with patchy frost early in the week, highs around 47–57°F, and lows near 29–40°F. These are designated wilderness trails with few people around to help.", ["nws", "zion-kolob"], "cold"),
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
