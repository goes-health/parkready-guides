src("glac-roads", "Glacier directions, transportation & road status", "https://www.nps.gov/glac/planyourvisit/directions.htm")
src("glac-hours", "Glacier operating hours & seasons", "https://www.nps.gov/glac/planyourvisit/hours.htm")
src("glac-winter", "Glacier: visiting in winter", "https://www.nps.gov/glac/planyourvisit/winter.htm")
src("glac-bears", "Glacier bear safety", "https://www.nps.gov/glac/planyourvisit/bears.htm")
src("glac-cond", "Glacier current conditions & safety", "https://www.nps.gov/glac/planyourvisit/conditions.htm")
src("glac-tula-mg", "News release: Tularemia detected in Many Glacier Valley (Oct 15, 2026)", "https://www.nps.gov/glac/learn/news/tularemia-detected-in-glacier-national-park-s-many-glacier-valley.htm")
src("glac-tula-sm", "News release: Tularemia detected in St. Mary Lake area (Sep 17, 2026)", "https://www.nps.gov/glac/learn/news/tularemia-detected-in-st-mary-lake-area-of-glacier-national-park.htm")

PARKS.append({
 "slug": "glacier", "code": "glac", "name": "Glacier National Park", "short": "Glacier",
 "state": "MT",
 "tagline": "Going-to-the-Sun Road closed at Avalanche Creek and Jackson Glacier Overlook for the season.",
 "summary": "Glacier is open 24 hours a day, 365 days a year, but it's in its late-fall, low-service season. Going-to-the-Sun Road is closed for the season at Avalanche Creek on the west side and at Jackson Glacier Overlook on the east. The lower road from West Glacier to Lake McDonald Lodge is plowed year-round, weather permitting. There's no fuel inside the park and no in-park lodging this time of year. Entrance fees still apply; use the self-pay stations when entrances aren't staffed.",
 "summary_sources": ["glac-alerts", "glac-winter", "glac-roads", "nps-api"],
 "cta_reason": "Grizzly country with nearly 1,000 bears, cold water that is the park's leading cause of death, and almost no services. GOES works offline when you're out of signal.",
 "fees": "Private vehicle $35 (self-pay when stations are unstaffed). Non-US residents 16+ pay an additional $100 nonresident fee unless entering with an annual / America the Beautiful pass.",
 "fees_sources": ["glac-fees", "nps-api"],
 "closed": [
   {"name": "Going-to-the-Sun Road alpine section (Logan Pass)", "note": "Closed for the season between Avalanche Creek (west) and Jackson Glacier Overlook (east). Open sections may change at any time due to winter weather.", "sources": ["glac-alerts"]},
   {"name": "Many Glacier and Two Medicine", "note": "No entrance pages this week. NPS says Many Glacier Road closes the third weekend in November (weather permitting) and Two Medicine Road closes once snow requires it. Confirm on the NPS road status map, or text GNPROADS to 333111.", "sources": ["glac-hours", "glac-roads"]},
 ],
 "park_risks": [
   R("Grizzly and black bears", "Glacier has habitat for nearly 1,000 bears of both species. Stay 100 yards from bears and wolves (25 yards from other wildlife), carry bear spray, make noise and hike in groups: Glacier has had no reported attacks on groups of four or more. In fall, bears forage hard before denning.", ["glac-bears", "glac-cond", "glac-hours"], "bears"),
   R("Cold water", "Water is the number one cause of fatalities in Glacier. Use extreme caution near lakes and streams.", ["glac-cond"], "cold"),
   R("Tularemia", "NPS confirmed tularemia in dead snowshoe hares in Many Glacier (Oct 15 release) and the St. Mary Lake area (Sept 17 release). Use insect repellent, check for ticks, don't touch carcasses, drink only treated or boiled water, and see a doctor if you get fever, chills or sores within two weeks of your visit.", ["glac-tula-mg", "glac-tula-sm"], "ticks"),
   R("Winter self-sufficiency", "Most businesses and services in and near the park are closed from early October to late May. Expect cold, blustery days and be entirely self-sufficient.", ["glac-hours", "glac-cond"], "cold"),
 ],
 "entrances": [
  {
   "slug": "west-entrance", "name": "West Entrance", "gateway": "West Glacier, MT (US-2)", "nws": "glac-west", "status": "open",
   "status_label": "Open — road to Avalanche Creek",
   "intro": "The West Entrance at West Glacier is the park's year-round front door to Apgar Village, Lake McDonald and the lower Going-to-the-Sun Road. It's about 33 miles from Kalispell.",
   "conditions": [
     C("Going-to-the-Sun Road is open from West Glacier and closed for the season at Avalanche Creek. NPS's winter page says the road from West Glacier to Lake McDonald Lodge is plowed year-round, weather permitting.", ["glac-alerts", "glac-winter"], "open"),
     C("Beyond the closure gate, the unplowed road is open to hikers and bicyclists, and to skiing and snowshoeing once there's snow.", ["glac-hours", "glac-winter"], None),
     C("Apgar Visitor Center restrooms are open year-round, with a water bottle filling station (about 2 miles north of the entrance). NPS's winter page says the visitor center opens on weekends in winter.", ["glac-hours", "glac-winter"], None),
     C("Apgar Campground offers primitive camping (vault toilet, no running water, first-come, first-served). There's no lodging in the park this time of year.", ["glac-hours"], None),
     C("No fuel inside the park. Road alerts: text GNPROADS to 333111, tune to Travelers' Information Station 1610 AM, or call 406-888-7800.", ["glac-roads", "glac-winter"], None),
   ],
   "risks": [
     R("Bears on the lower road and trails", "Bears may still be active and foraging before denning. Carry bear spray, call out and clap (NPS says bells aren't enough), and don't stop near roadside bears: drive at least 100 yards past before pulling over.", ["glac-bears", "glac-hours"], "bears"),
     R("Lake McDonald's cold water", "Water is the park's top cause of death. Slick shoreline rocks and near-freezing water make a fall dangerous within minutes.", ["glac-cond"], "cold"),
     R("Fog and short days", "NWS forecast for West Glacier this week: areas of fog, highs near 50–54°F, lows near 35°F, and a slight chance of light rain Saturday.", ["nws"], "weather"),
   ],
   "prep": [
     ("Fuel and food in West Glacier or Columbia Falls", "No gas in the park; Apgar's camp store may or may not be open."),
     ("Bear spray, even for short walks", "NPS: bears may still be active."),
     ("Pay at the self-pay station", "Fees apply when the booth is unstaffed."),
     ("Download GOES before the entrance", "Plan for no signal past Apgar."),
   ],
   "cta_reason": "Grizzly country, ice-cold lake water and almost no services. Download GOES in West Glacier so its offline bear, cold-water and injury guidance comes with you.",
  },
  {
   "slug": "st-mary-entrance", "name": "St. Mary Entrance", "gateway": "St. Mary, MT (US-89)", "nws": "glac-st-mary", "status": "limited",
   "status_label": "Open — road to Jackson Glacier Overlook",
   "intro": "St. Mary is the east-side entrance to Going-to-the-Sun Road, along St. Mary Lake. It's about 125 miles from Great Falls via US-89 and Browning.",
   "conditions": [
     C("Going-to-the-Sun Road is closed for the season at Jackson Glacier Overlook on the east side. Open sections can change at any time due to winter weather.", ["glac-alerts"], "caution"),
     C("St. Mary Visitor Center is closed for the winter. Primitive camping is available year-round at St. Mary Campground.", ["glac-winter", "glac-hours"], "closed"),
     C("Tularemia was confirmed in a dead snowshoe hare in the St. Mary Lake area (Sept 17 release).", ["glac-tula-sm"], "caution"),
     C("No fuel inside the park. The St. Mary grocery store sometimes stays open in fall; full-service groceries are in Browning.", ["glac-roads", "glac-hours"], None),
   ],
   "risks": [
     R("East-side wind and cold", "Glacier sits where Pacific air from the west meets arctic air from the northeast. NWS forecast for St. Mary this week: mostly cloudy, highs around 54–62°F, lows near 36–46°F. Expect colder, harsher conditions higher up.", ["nws", "glac-cond", "nps-api"], "cold"),
     R("Bears", "Grizzlies and black bears live on both sides of the Divide. Make noise, hike in a group, and carry bear spray where you can reach it.", ["glac-bears"], "bears"),
     R("Tularemia and ticks", "Don't touch dead animals, use repellent, check for ticks, and drink only treated or boiled water.", ["glac-tula-sm"], "ticks"),
   ],
   "prep": [
     ("Fuel and supplies in Browning or St. Mary", "No fuel in the park."),
     ("Bear spray and windproof layers", "The east side is exposed."),
     ("Treat all water", "Tularemia advisory in the St. Mary Lake area."),
     ("Download GOES before St. Mary", "Plan for no signal inside the park."),
   ],
   "cta_reason": "Grizzlies, a tularemia advisory and wind off the Divide. Download GOES before St. Mary so its offline tick, wildlife and cold guidance is ready.",
  },
 ],
})
