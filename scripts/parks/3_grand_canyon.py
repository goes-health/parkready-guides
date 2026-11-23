src("grca-cond", "Grand Canyon Alerts & Conditions", "https://www.nps.gov/grca/planyourvisit/conditions.htm")
src("grca-key", "Grand Canyon Key Hiking Messages (updated Oct 27, 2026)", "https://www.nps.gov/grca/planyourvisit/key-messages.htm")
src("grca-water", "News release: Projected dates for restoring water to the South Rim (Sep 19, 2026)", "https://www.nps.gov/grca/learn/news/grand-canyon-national-park-announces-projected-dates-for-restoring-water-to-south-rim.htm")
src("grca-lodging", "News release: Stage 3 water conservation and South Rim lodging reopens Nov 20 (Nov 18, 2026)", "https://www.nps.gov/grca/learn/news/transitions-to-stage-3-water-conservation-measures-and-south-rim-lodging-reopens-nov-20.htm")
src("grca-trails", "News release: Select inner canyon trails reopen (Oct 26, 2026)", "https://www.nps.gov/grca/learn/news/select-inner-canyon-trails-reopen-in-grand-canyon-national-park.htm")
src("grca-fire", "News release: Stage 2 fire restrictions rescinded on South Rim (Nov 4, 2026)", "https://www.nps.gov/grca/learn/news/stage-2-fire-restrictions-rescinded-on-south-rim.htm")
src("grca-nr", "News release: Modified fall operations at the North Rim (Sep 30, 2026)", "https://www.nps.gov/grca/learn/news/modified-fall-operations-north-rim-2026.htm")
src("grca-safety", "Grand Canyon safety: elevation, rim edges, winter", "https://www.nps.gov/grca/planyourvisit/safety.htm")
src("grca-hours", "Grand Canyon operating hours", "https://www.nps.gov/grca/planyourvisit/hours.htm")

PARKS.append({
 "slug": "grand-canyon", "code": "grca", "name": "Grand Canyon National Park", "short": "Grand Canyon",
 "state": "AZ",
 "tagline": "South Rim hotels reopened Nov 20 and water rules eased to Stage 3. Still pack water for the trail.",
 "summary": "Good news at Grand Canyon: on Friday, Nov. 20 the park moved from Stage 4 to Stage 3 water conservation, and South Rim hotels reopened to overnight guests (El Tovar, Thunderbird, Kachina, Bright Angel, Maswik and Yavapai lodges). NPS says food and beverage services are resuming gradually and asks everyone to keep conserving water. The Aug. 29 flash flood that damaged the Transcanyon Waterline still has inner-canyon water off and Phantom Ranch and the North Kaibab Trail closed. Both South Rim entrances are open 24/7, and NWS forecasts a sunny, dry week.",
 "summary_sources": ["grca-lodging", "grca-alerts", "grca-key", "nws"],
 "cta_reason": "7,000-foot rims, icy overlook paths, a rim edge with no second chances, and no water in the inner canyon. GOES carries altitude, cold and dehydration guidance offline.",
 "fees": "Private vehicle $35 (cash is not accepted at the entrances). Non-US residents 16+ pay an additional $100 nonresident fee unless entering with an annual / America the Beautiful pass.",
 "fees_sources": ["grca-fees", "nps-api"],
 "closed": [
   {"name": "Phantom Ranch, Bright Angel Campground, Black & Silver bridges, entire North Kaibab Trail", "note": "Closed after flash flooding, with no estimated reopening. Boat Beach is closed except for emergencies and brief scouting.", "sources": ["grca-key", "grca-trails", "grca-alerts"]},
 ],
 "park_risks": [
   R("Water: carry your own on the trail", "The South Rim moved to Stage 3 water conservation on Nov 20, and NPS asks visitors to keep conserving. Inner-canyon water is off everywhere (1.5 Mile and 3 Mile resthouses, Havasupai Gardens) for the rest of the winter. Potable water tanks are at the Bright Angel and South Kaibab trailheads. Carry all your water or a reliable treatment method.", ["grca-lodging", "grca-key", "grca-trails", "grca-alerts"], "injury"),
   R("Elevation", "The South Rim is about 7,000 ft and the North Rim about 8,000 ft. NPS warns the altitude and dry air can cause dehydration, nausea, shortness of breath and exhaustion, so take your time at overlooks.", ["grca-safety"], "altitude"),
   R("The rim edge and ice", "Stay on trails and walkways, at least 6 feet from the edge, and never climb railings. In winter, walkways can be icy; NPS recommends over-the-shoe traction and hiking poles.", ["grca-safety"], "injury"),
   R("Inner canyon hiking", "Temperatures rise about 5.5°F for every 1,000 ft you descend. Rescue isn't guaranteed and response can be delayed. Rockfall is common during or after rain and freeze/thaw, and flash floods can hit with no warning.", ["grca-key", "grca-trails"], "cold"),
 ],
 "entrances": [
  {
   "slug": "south-entrance", "name": "South Entrance", "gateway": "Tusayan, AZ (Hwy 64 / 180)", "nws": "grca-south", "status": "open",
   "status_label": "Open 24/7 — lodging reopened Nov 20",
   "intro": "The South Entrance just north of Tusayan is the main gate into Grand Canyon's South Rim (NPS says it gets the most traffic). It leads to Grand Canyon Village, the main visitor center and the Bright Angel and South Kaibab trailheads.",
   "conditions": [
     C("Open 24 hours a day, 7 days a week. Credit cards and America the Beautiful passes accepted; cash is not accepted.", ["grca-hours", "nps-api"], "open"),
     C("NPS notes this station has the longest lines, with waits of up to 2 hours between 9:30 am and 4 pm. That's NPS's general guidance, not a live wait time. Desert View (East) usually has shorter waits.", ["nps-api"], "caution"),
     C("South Rim lodging reopened to overnight guests Fri Nov 20: El Tovar, Thunderbird, Kachina, Bright Angel, Maswik and Yavapai lodges. Food and beverage services are resuming gradually; check NPS for current dining hours.", ["grca-lodging"], "open"),
     C("Stage 2 fire restrictions were lifted on the South Rim Nov 4; Stage 1 remains. Campfires at Mather Campground are allowed only in established rings.", ["grca-fire"], None),
     C("Open trails: Bright Angel to River Resthouse, Plateau Point, River Trail, South Kaibab to the Black Bridge, and Tonto Trail (Tip-Off to Havasupai Gardens). Expect intermittent closures for Bright Angel Trail repairs, and, since Nov 18, intermittent delays just above 3-Mile Resthouse for rockfall mitigation work.", ["grca-key", "grca-trails", "grca-alerts"], "open"),
   ],
   "risks": [
     R("Dehydration in high, dry air", "At 7,000 feet in desert air you lose water fast. The South Rim is on Stage 3 water conservation and inner-canyon water stations are off, so fill up at the rim and carry what you need.", ["grca-safety", "grca-key"], "altitude"),
     R("Cold mornings and icy rim paths", "NWS forecast for the South Rim this week: sunny and dry, highs around 46–59°F, but lows as cold as 16°F. Shady stretches of trail can stay icy, and freeze/thaw increases rockfall.", ["nws", "grca-key"], "cold"),
     R("Hiking down is the easy half", "NPS: rescue is not guaranteed and response can be delayed. If you feel nauseated, dizzy or exhausted, stop, rest, and slowly eat and drink. Don't force fluids; drinking too much can cause hyponatremia.", ["grca-key", "grca-trails"], "injury"),
   ],
   "prep": [
     ("Water for everyone, plus treatment if hiking", "Stage 3 conservation; inner-canyon water is off."),
     ("In-park lodging is back", "South Rim hotels reopened Nov 20; book with the lodge directly."),
     ("Card, not cash, at the gate", "Cash isn't accepted."),
     ("Traction devices for icy walkways", "NPS recommends them in winter."),
     ("Download GOES in Tusayan", "Before you're on the rim or below it."),
   ],
   "cta_reason": "High altitude, icy rim paths and no water below the rim this season. Download GOES in Tusayan; its altitude, cold and dehydration guidance works offline.",
  },
  {
   "slug": "desert-view-east-entrance", "name": "Desert View (East) Entrance", "gateway": "Cameron, AZ (SR 64 via US 89)", "nws": "grca-desert-view", "status": "open",
   "status_label": "Open 24/7",
   "intro": "The East Entrance at Desert View is 25 miles west of Cameron on State Route 64, reached via US 89 through the Navajo Nation. It's 32 miles east of Grand Canyon Village, and NPS says waits here are usually shorter than at the South Entrance.",
   "conditions": [
     C("Open 24 hours a day, 7 days a week. Credit cards and passes accepted; cash is not accepted.", ["grca-hours", "nps-api"], "open"),
     C("NPS says most Desert View services are open. Desert View Campground is seasonal (NPS lists an April–October season).", ["nps-api"], None),
     C("Park-wide: Stage 3 water conservation since Nov 20, when South Rim lodging also reopened. NPS asks everyone to keep conserving water.", ["grca-lodging"], "caution"),
   ],
   "risks": [
     R("Cold at the Watchtower", "NWS forecast for Desert View: sunny all week, highs around 40–53°F and lows around 28–37°F. The rim is exposed, so it feels colder in any wind.", ["nws"], "cold"),
     R("Long, remote approach", "US 89 and SR 64 cross long empty stretches. NPS advises keeping your gas tank full and carrying water in the car.", ["grca-safety"], "weather"),
     R("Edges and overlooks", "Stay 6 feet back from the edge and behind railings, and watch children closely.", ["grca-safety"], "injury"),
   ],
   "prep": [
     ("Fuel and water before Cameron", "NPS: distances are deceiving out here."),
     ("Layers and a windproof shell", "Sunny, but cold mornings on an exposed rim."),
     ("Download GOES before the drive in", "Plan for gaps in coverage."),
   ],
   "cta_reason": "A cold, windy rim and long remote drives. Download GOES before Cameron so its offline guidance is on your phone when coverage drops.",
  },
  {
   "slug": "north-rim-entrance", "name": "North Rim Entrance", "gateway": "Jacob Lake, AZ (SR 67)", "nws": "grca-north-rim", "status": "limited",
   "status_label": "Limited day use — closes Nov 30",
   "intro": "The North Rim entrance station is on State Route 67, 30 miles south of Jacob Lake. In fall 2026 the North Rim is in modified operations: day use only, with no services. The gate closes for winter at sunset Nov 30 or after the first major snowstorm, whichever comes first.",
   "conditions": [
     C("North Rim: limited fall day use only. NO SERVICES — the campground, store and gas station are closed, and there's no fuel inside the park.", ["grca-cond", "grca-nr"], "caution"),
     C("The SR 67 entrance gate closes at sunset Nov 30, 2026, or after the first major snowstorm, whichever comes first. NWS forecasts a sunny, dry week here, but conditions can change quickly at 8,000 feet, so check before you drive.", ["grca-nr", "nws"], "caution"),
     C("All North Rim water is off. The North Kaibab Trail is closed in its entirety.", ["grca-key"], "closed"),
     C("Stage 2 fire restrictions remain in effect on the North Rim for the rest of 2026.", ["grca-fire"], None),
     C("Road conditions: Arizona Highway Information, 1-888-411-ROAD (7623). Nearest lodging, food and fuel: Jacob Lake, about 45 miles north.", ["grca-nr"], None),
   ],
   "risks": [
     R("Snow at 8,000 feet", "NPS: snow, ice and rain are common here this time of year. NWS forecast this week: sunny and dry, highs around 34–50°F, and lows around 19–29°F.", ["grca-nr", "nws"], "cold"),
     R("Very limited emergency response", "NPS says emergency response on the North Rim will be extremely limited and response times may be significantly delayed. Travel self-sufficient.", ["grca-nr"], "injury"),
     R("Altitude", "The North Rim is about 8,000 ft. Take it slow if you've come up from lower elevations.", ["grca-safety"], "altitude"),
   ],
   "prep": [
     ("Full tank at Jacob Lake or before", "No fuel in the park."),
     ("All the food, water and warm gear you need", "No services at all on the North Rim."),
     ("Check that the gate is still open", "1-888-411-ROAD. The first big snowstorm can close it before Nov 30."),
     ("Download GOES before Jacob Lake", "You'll be far from help and likely out of signal."),
   ],
   "cta_reason": "Freezing nights at 8,000 feet, no services and slow rescue. If you go, get GOES first so its offline assessment and cold-weather guidance travel with you.",
  },
 ],
})
