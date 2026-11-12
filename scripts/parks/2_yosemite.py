src("yose-cond", "Yosemite Current Conditions (updated Nov 11, 2026)", "https://www.nps.gov/yose/planyourvisit/conditions.htm")
src("yose-hours", "Yosemite operating hours (Hetch Hetchy daylight hours)", "https://www.nps.gov/yose/planyourvisit/hours.htm")
src("yose-driving", "Yosemite driving directions, fuel & GPS warning", "https://www.nps.gov/yose/planyourvisit/driving.htm")
src("yose-bears", "Yosemite bears", "https://www.nps.gov/yose/learn/nature/bears.htm")
src("yose-hetch", "Yosemite: Hetch Hetchy day hikes", "https://www.nps.gov/yose/planyourvisit/hetchhetchy.htm")
src("yose-dome", "Dome Fire update, Oct 13, 2026", "https://www.nps.gov/yose/learn/news/dome-fire-update-october-13-2026-morning.htm")
src("nws-hanford-wsw", "NWS Hanford: Winter Storm Watch (issued Nov 11, until Nov 17 4 am PST)", "https://forecast.weather.gov/MapClick.php?lat=37.507&lon=-119.632")

PARKS.append({
 "slug": "yosemite", "code": "yose", "name": "Yosemite National Park", "short": "Yosemite",
 "state": "CA",
 "tagline": "Snow on the way: Tioga and Glacier Point roads close Nov 12 at 5 pm.",
 "summary": "Yosemite is open 24 hours a day, but the high country is shutting down. NPS announced that Tioga Road (Hwy 120 through the park) and Glacier Point Road temporarily close Thursday, Nov 12 at 5 pm because snow is forecast. Wawona Road (Hwy 41), El Portal Road (Hwy 140) and Big Oak Flat Road (Hwy 120 west) are open. Carry tire chains: they can become mandatory at any time, even for 4WD.",
 "summary_sources": ["yose-alerts", "yose-cond"],
 "cta_reason": "Black bears active in every part of the park, slick granite by the rivers, and a winter storm on the way. GOES works offline, so its assessment and how-to guides still help if a fall or a cold soaking happens out of signal.",
 "fees": "Private vehicle $35. Non-US residents 16+ pay an additional $100 nonresident fee unless entering with an annual / America the Beautiful pass.",
 "fees_sources": ["yose-fees", "nps-api"],
 "closed": [
   {"name": "Tioga Pass Entrance (Hwy 120 east, from Lee Vining)", "note": "Tioga Road temporarily closes Thu Nov 12 at 5 pm for forecast snow, and no overnight parking is allowed on it. NPS says the Tioga Pass Entrance is closed from approximately November through late May or June, so there's no entrance page for it this week.", "sources": ["yose-alerts", "yose-cond", "nps-api"]},
   {"name": "Glacier Point Road", "note": "Temporarily closes Thu Nov 12 at 5 pm for forecast snow. Part of the Glacier Point Road area remains under a Dome Fire safety closure.", "sources": ["yose-alerts", "yose-cond"]},
 ],
 "park_risks": [
   R("Black bears in all areas", "NPS: bears remain active in all areas of the park. Store food properly, use bear-proof dumpsters, and stay at least 50 yards from bears in forest and meadows — but yell at and scare away a bear that approaches you or is in a developed area. Yosemite has an estimated 300–500 black bears and no grizzlies.", ["yose-cond", "yose-bears"], "bears"),
   R("Rivers and slick rock", "Waterfalls are flowing low, as usual for November, but NPS still asks visitors to use caution along rivers and creeks: rocks are slippery even when dry.", ["yose-cond"], "injury"),
   R("Winter storm, chains and ice", "NWS Hanford issued a Winter Storm Watch (Nov 11, until Nov 17, 4 am PST) for the park's southern area, and the forecast calls for rain and thunderstorms Friday, with snow possible at higher elevations. Carry chains even with 4WD and expect icy spots on mostly dry roads.", ["nws-hanford-wsw", "yose-cond", "nws"], "cold"),
   R("Smoke and air quality", "The Dome Fire (Sept–Oct) was 86% contained with minimal activity as of NPS's Oct 13 update, and fire closures remain around the Glacier Point Road area. Air quality can still be affected by fires elsewhere or prescribed burns, so check current AQI before strenuous hikes.", ["yose-dome", "yose-cond", "airnow"], "smoke"),
 ],
 "entrances": [
  {
   "slug": "arch-rock-entrance", "name": "Arch Rock Entrance", "gateway": "El Portal / Mariposa (Hwy 140)", "nws": "yose-arch-rock", "status": "open",
   "status_label": "Open — Hwy 140 / El Portal Road",
   "intro": "Arch Rock is the Highway 140 entrance from Merced, Mariposa and El Portal, along the Merced River. NPS puts it about 20–25 minutes from Yosemite Valley.",
   "conditions": [
     C("El Portal Road (Hwy 140): open.", ["yose-cond"], "open"),
     C("Yosemite Valley roads: open, with 15-minute delays on weekdays 7 am – 7 pm at El Capitan Bridge (stabilization work through December 2026). The Valley Loop Trail crossing at El Capitan Bridge is closed on weekdays.", ["yose-cond"], "caution"),
     C("Valley campgrounds: Upper Pines and Camp 4 open (reservation required). Lower Pines and North Pines are closed.", ["yose-cond"], None),
     C("Fuel: 24/7 by credit card at El Portal, Wawona and Crane Flat. There's no gas in Yosemite Valley.", ["yose-driving"], None),
     C("Half Dome cables are down for the season.", ["yose-cond"], "closed"),
   ],
   "risks": [
     R("Merced River banks", "The river is low, but NPS warns rocks are slippery even when dry. Stay off wet granite near waterfalls and the river's edge.", ["yose-cond"], "injury"),
     R("Valley bears", "Bears are active in all areas, including the Valley. Use food lockers and bear-proof trash cans, and never leave food unattended at picnic spots.", ["yose-cond", "yose-bears"], "bears"),
     R("Rain and thunderstorms Friday", "This week's NWS forecast for the Arch Rock area: sunny and about 66°F Thursday, then light rain and showers/thunderstorms Friday into Friday night.", ["nws"], "weather"),
   ],
   "prep": [
     ("Fuel at El Portal or before", "No gas in the Valley."),
     ("Chains in the trunk", "Chains can become mandatory at any time, even with 4WD."),
     ("Follow road signs over GPS", "NPS: when your GPS and a road sign disagree, the sign is right."),
     ("Download GOES before the canyon", "Don't count on coverage in the Merced canyon and Valley."),
   ],
   "cta_reason": "Bears in the Valley, slick river rock and a wet, stormy Friday. Get GOES before the canyon so its offline injury assessment and how-to guides are ready without a signal.",
  },
  {
   "slug": "big-oak-flat-entrance", "name": "Big Oak Flat Entrance", "gateway": "Groveland (Hwy 120 west)", "nws": "yose-big-oak-flat", "status": "open",
   "status_label": "Open — weekday delays",
   "intro": "Big Oak Flat is the Highway 120 entrance from the Bay Area via Groveland, next to Hodgdon Meadow. With Tioga Road closing, Hwy 120 inside the park now leads only toward Crane Flat and Yosemite Valley (about 45 minutes away).",
   "conditions": [
     C("Big Oak Flat Road: open, with 15-minute delays on weekdays for fire-safety vegetation work between Foresta and Big Oak Flat.", ["yose-cond"], "caution"),
     C("Tioga Road (east of Crane Flat) temporarily closes Thu Nov 12 at 5 pm for forecast snow. No overnight parking on Tioga Road.", ["yose-alerts"], "closed"),
     C("Hodgdon Meadow Campground (by this entrance): open, first-come, first-served. Crane Flat, Tamarack Flat and White Wolf campgrounds are closed.", ["yose-cond"], None),
     C("Fuel: Crane Flat, 24/7 by credit card.", ["yose-driving"], None),
   ],
   "risks": [
     R("Freezing nights and wet snow", "This week's NWS forecast here: sunny and about 69°F Thursday, then rain and thunderstorms Friday, a Friday-night low near 27°F, and a chance of rain and snow. Being wet in freezing weather is how hikers get hypothermia.", ["nws"], "cold"),
     R("Bears at campgrounds and pullouts", "Hodgdon Meadow is open. Use the food lockers, keep a clean camp, and stay 50 yards from bears in the forest.", ["yose-cond", "yose-bears"], "bears"),
     R("Road work and wildlife on the road", "Expect weekday work zones on Big Oak Flat Road. NPS posts signs where bears have been hit by vehicles, so drive the speed limit.", ["yose-cond", "yose-bears"], "wildlife"),
   ],
   "prep": [
     ("Chains, even with 4WD", "Chains can become mandatory at any time."),
     ("Allow extra time on weekdays", "15-minute delays on Big Oak Flat Road."),
     ("Don't plan on Tioga", "It closes Nov 12 at 5 pm."),
     ("Download GOES in Groveland", "Before the climb into the park."),
   ],
   "cta_reason": "Sub-freezing nights, a wet storm and bears around camp. Download GOES before Groveland so its hypothermia guidance and offline how-to guides work without a signal.",
  },
  {
   "slug": "south-entrance", "name": "South Entrance", "gateway": "Fish Camp / Oakhurst (Hwy 41)", "nws": "yose-south", "status": "open",
   "status_label": "Open — Winter Storm Watch",
   "intro": "The South Entrance on Highway 41 from Fresno, Oakhurst and Fish Camp leads to the Mariposa Grove of Giant Sequoias, Wawona, and then Yosemite Valley, a little over an hour north.",
   "conditions": [
     C("Wawona Road (Hwy 41): open.", ["yose-cond"], "open"),
     C("NWS Winter Storm Watch for this area, issued Nov 11, in effect until Nov 17 at 4 am PST.", ["nws-hanford-wsw"], "caution"),
     C("Mariposa Grove Road: open only to vehicles displaying a disability placard. Everyone else takes the free shuttle from the Mariposa Grove Welcome Plaza, which runs approximately late April through November.", ["yose-cond"], None),
     C("Wawona Campground: open, reservation required until Nov 29. Bridalveil Creek Campground: closed.", ["yose-cond"], None),
     C("Glacier Point Road temporarily closes Thu Nov 12 at 5 pm. An area east of Wawona Road and south of Glacier Point Road remains closed after the Dome Fire; the Chilnualna Falls trail has reopened.", ["yose-alerts", "yose-cond"], "closed"),
     C("Fuel: Wawona, 24/7 by credit card.", ["yose-driving"], None),
   ],
   "risks": [
     R("Winter storm on Hwy 41", "The NWS forecast here shows rain and thunderstorms Friday, then a chance of rain and snow with a low near 29°F. Chain controls can start with little notice.", ["nws", "nws-hanford-wsw", "yose-cond"], "cold"),
     R("Fire-scarred areas", "Stay out of the posted Dome Fire closure area. Burned slopes can drop rocks and trees, especially in rain.", ["yose-cond", "yose-dome"], "injury"),
     R("Bears in the groves and around Wawona", "Bears are active parkwide. Store food properly and keep your distance in forest and meadows.", ["yose-cond"], "bears"),
   ],
   "prep": [
     ("Watch the forecast until you leave", "The Winter Storm Watch runs through Nov 17."),
     ("Chains and a full tank", "Fuel at Wawona; carry chains even with 4WD."),
     ("Plan on the shuttle for Mariposa Grove", "Private cars need a disability placard."),
     ("Download GOES in Oakhurst or Fish Camp", "Before you drive into the forest."),
   ],
   "cta_reason": "A winter storm watch, fire-scarred slopes and bears in the groves. Get GOES before Fish Camp so its offline cold-weather and injury guidance is ready.",
  },
  {
   "slug": "hetch-hetchy-entrance", "name": "Hetch Hetchy Entrance", "gateway": "Evergreen Road (off Hwy 120)", "nws": "yose-hetch-hetchy", "status": "limited",
   "status_label": "Daylight only — closes for snow",
   "intro": "Hetch Hetchy is Yosemite's quiet northwest corner, a reservoir valley at about 3,900 feet reached on Evergreen and Hetch Hetchy roads off Hwy 120. NPS puts it about 1.5 hours from Yosemite Valley.",
   "conditions": [
     C("Hetch Hetchy Road: open sunrise to sunset only, and closed when it's snowing or snow is forecast overnight. Day visitors must leave by sunset; the road is closed to all vehicles overnight.", ["yose-cond", "yose-hours", "nps-api"], "caution"),
     C("No current trail closures in the Hetch Hetchy area.", ["yose-cond"], "open"),
     C("Swimming and boating are prohibited in the reservoir (it's a drinking water supply). Pets aren't allowed on the dam or trails.", ["yose-hetch"], None),
   ],
   "risks": [
     R("Getting caught by darkness", "Sunset comes early in mid-November and the gate closes at sunset. Turn around with daylight to spare: a twisted ankle on the Wapama Falls trail can turn into a cold night out.", ["yose-hours", "yose-hetch"], "injury"),
     R("Rattlesnakes and poison oak", "NPS's Hetch Hetchy page tells hikers to watch for rattlesnakes and poison oak.", ["yose-hetch"], "snakes"),
     R("Storm closures", "Friday's NWS forecast here has rain and thunderstorms with a low near 28°F that night. If snow is forecast overnight, the road may not open.", ["nws", "yose-cond"], "cold"),
   ],
   "prep": [
     ("Call before you drive", "209/372-0200, then press 1, 1 for current road conditions."),
     ("Be out before sunset", "The road is gated overnight."),
     ("Water, sunscreen and a map", "NPS's own Hetch Hetchy checklist."),
     ("Download GOES before the turnoff", "Snakebite and poisonous-plant guidance that works offline."),
   ],
   "cta_reason": "Rattlesnakes, poison oak and a sunset gate. Download GOES before the turnoff; its wildlife and poisonous-plant guidance works without a signal.",
  },
 ],
})
