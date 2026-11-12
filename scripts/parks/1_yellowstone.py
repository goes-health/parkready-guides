src("yell-roads", "Yellowstone Park Roads (updated Nov 3, 2026)", "https://www.nps.gov/yell/planyourvisit/parkroads.htm")
src("yell-close-nov1", "News release: Most Yellowstone roads and entrances close Nov. 1, 2026 (Oct 21)", "https://www.nps.gov/yell/learn/news/26026.htm")
src("yell-hours", "Yellowstone operating dates (updated Nov 9, 2026)", "https://www.nps.gov/yell/planyourvisit/hours.htm")
src("yell-safety", "Yellowstone safety: thermal areas, wildlife, bears", "https://www.nps.gov/yell/planyourvisit/safety.htm")

PARKS.append({
 "slug": "yellowstone", "code": "yell", "name": "Yellowstone National Park", "short": "Yellowstone",
 "state": "WY · MT · ID",
 "tagline": "Winter shoulder season: only the North ↔ Northeast road is open to cars.",
 "summary": "Yellowstone closed its West, South and East entrances and nearly all roads to regular vehicles on Nov. 1. Until snowmobile and snowcoach season starts Dec. 15, the only way to drive into the park is the road between the North Entrance (Gardiner, MT) and the Northeast Entrance (Cooke City/Silver Gate, MT), through Mammoth Hot Springs, Tower Junction and Lamar Valley.",
 "summary_sources": ["yell-close-nov1", "yell-roads", "yell-alerts"],
 "cta_reason": "Grizzly and black bear country, thermal ground that can scald, bison and elk along the road, and a single winter road where you can't count on a signal. GOES keeps its injury assessment, how-to guides and prevention tips on your phone offline.",
 "fees": "Private vehicle $35. Non-US residents 16+ pay an additional $100 nonresident fee unless entering with an annual / America the Beautiful pass.",
 "fees_sources": ["yell-fees", "nps-api"],
 "closed": [
   {"name": "West Entrance (West Yellowstone, MT)", "note": "Closed to cars Nov 1 – Dec 14 (shoulder season). Opens to commercially guided snowmobiles and snowcoaches Dec 15.", "sources": ["yell-close-nov1", "nps-api"]},
   {"name": "South Entrance (from Grand Teton)", "note": "Closed to cars Nov 1 – Dec 14. Opens to oversnow travel Dec 15.", "sources": ["yell-close-nov1", "nps-api"]},
   {"name": "East Entrance (from Cody, WY)", "note": "Closed to cars Nov 1 – Dec 14. Oversnow dates differ between NPS pages (Park Roads lists Dec 15; operating hours list Dec 22) — confirm before planning.", "sources": ["yell-roads", "nps-api"]},
 ],
 "park_risks": [
   R("Thermal areas (scald burns)", "Burns from thermal features are a common cause of serious injury and death in Yellowstone. Ground that looks solid can be a thin crust over superheated water. Stay on boardwalks, keep kids close, and never touch runoff. More than 20 people have died after entering or falling into hot springs. Biscuit Basin (near Old Faithful) remains closed after the July 2024 hydrothermal explosion.", ["yell-safety", "yell-alerts"], "injury"),
   R("Bears", "All of Yellowstone is grizzly and black bear country. Stay at least 100 yards from bears and wolves, carry bear spray where you can reach it, hike in groups of 3+, make noise, and avoid carcasses. Since 1970, 91% of people injured by bears in Yellowstone were hiking alone or with one partner.", ["yell-safety"], "bears"),
   R("Bison, elk and other wildlife", "Stay at least 25 yards from bison, elk and all other animals (100 yards from bears, wolves and cougars). The safest view is usually from inside your car.", ["yell-safety"], "wildlife"),
   R("Winter driving and cold", "NPS asks fall and winter drivers to watch the weather, keep plans flexible, expect limited services and closures without notice, pack blankets and cold-weather essentials, and keep a full tank.", ["yell-close-nov1"], "cold"),
 ],
 "entrances": [
  {
   "slug": "north-entrance", "name": "North Entrance", "gateway": "Gardiner, MT", "nws": "yell-north", "status": "open",
   "status_label": "Open to cars (year-round road)",
   "intro": "The North Entrance at Gardiner, Montana is the only Yellowstone entrance open to wheeled vehicles all year, and right now it's one of only two ways to drive in. From here the road climbs to Mammoth Hot Springs and continues east through Tower Junction and Lamar Valley to the Northeast Entrance.",
   "conditions": [
     C("Open year-round to regular vehicles: North Entrance → Mammoth → Tower Junction → Lamar Valley → Northeast Entrance. Every other park road is closed to cars (oversnow travel only from Dec 15).", ["yell-roads", "yell-close-nov1"], "open"),
     C("Gardner River High Bridge (0.5 mi southeast of Mammoth, toward Tower): single-lane traffic with up to 15-minute delays, 24/7, through Nov 24, 2026. Vehicles 8'6\"+ wide, 75'+ long or 80,000+ lbs can't cross.", ["yell-roads", "yell-alerts"], "caution"),
     C("Mammoth to Norris is closed to cars; it opens to oversnow vehicles Dec 15, 2026.", ["yell-roads"], "closed"),
     C("Open at Mammoth per NPS operating dates: Albright Visitor Center, Mammoth Campground (first-come, first-served after Oct 15), Mammoth General Store, Mammoth Medical Clinic (closed on Thanksgiving), Mammoth Hot Springs Hotel & Cabins, Post Office. The Mammoth gas station is listed as closed — fill up in Gardiner.", ["yell-hours"], "open"),
     C("Road status: call (307) 344-2117 or text 82190 to 888-777 for Yellowstone road alerts.", ["yell-roads"], None),
   ],
   "risks": [
     R("Thermal terraces at Mammoth", "Mammoth Hot Springs is the main thermal area you can reach by car right now. Stay on boardwalks and designated trails; thermal runoff can burn. Pets aren't allowed on boardwalks or in thermal areas. If you feel sick in a thermal area, leave immediately — gases can build up.", ["yell-safety"], "injury"),
     R("Elk and bison around Mammoth and the road", "The rule: at least 25 yards from elk and bison, 100 yards from bears and wolves. If an animal moves toward you, back away. It's illegal to stay near any animal at a distance that disturbs it.", ["yell-safety"], "wildlife"),
     R("Bears may still be active", "NPS treats all of Yellowstone as bear country. Carry bear spray on any walk away from the car, hike in a group, and never leave packs or coolers unattended.", ["yell-safety"], "bears"),
     R("Cold, ice and short days", "This week's NWS forecast for Gardiner: highs around 55–64°F, lows in the mid-30s, with a chance of rain and snow showers by Saturday. NPS asks drivers to carry blankets and keep a full tank.", ["nws", "yell-close-nov1"], "cold"),
   ],
   "prep": [
     ("Fill the tank in Gardiner", "NPS lists the Mammoth gas station as closed for winter."),
     ("Download offline maps + the GOES app before the arch", "NPS says to dial 911 \u201cif cell service is available\u201d — don't plan around it."),
     ("Bear spray within reach", "One can per person, in a holster, not in the pack. NPS: spray when a charging bear is 30–60 ft away."),
     ("Pack winter layers and a blanket", "Even after a 60°F afternoon, nights drop near freezing."),
     ("Check road status the morning you go", "(307) 344-2117, or text 82190 to 888-777."),
   ],
   "cta_reason": "Mammoth's thermal terraces, elk and bison along the road, and grizzly country beyond. Download GOES in Gardiner so its injury assessment, how-to guides and prevention tips work without a signal.",
  },
  {
   "slug": "northeast-entrance", "name": "Northeast Entrance", "gateway": "Cooke City & Silver Gate, MT", "nws": "yell-northeast", "status": "open",
   "status_label": "Open to cars, reached via Gardiner",
   "intro": "The Northeast Entrance near Silver Gate and Cooke City, Montana sits at the far end of Yellowstone's only winter road. With the Beartooth Highway closed for the season, the way to Cooke City in winter is through the park from Gardiner and Lamar Valley.",
   "conditions": [
     C("Open year-round for wheeled vehicles between the North and Northeast entrances, through Lamar Valley.", ["yell-roads", "nps-api"], "open"),
     C("Beartooth Highway (US-212, Cooke City to Red Lodge): closed for the season.", ["yell-roads"], "closed"),
     C("Chief Joseph Scenic Byway (WY-296): in winter, 9 miles between Cooke City and Pilot Creek close to wheeled vehicles (oversnow only). That segment is normally open to cars mid-May through early November — check WYDOT before relying on it.", ["yell-roads"], "caution"),
     C("Campgrounds near this entrance are closed: Slough Creek (seasonal) and Pebble Creek (closed until further notice for flood recovery). Tower-Roosevelt services are closed for the winter.", ["yell-hours"], "closed"),
   ],
   "risks": [
     R("Lamar Valley wildlife: bison, wolves, bears", "Use pullouts, stay in or near your vehicle, keep 100 yards from wolves and bears and 25 yards from bison. Don't stop in the travel lane.", ["yell-safety"], "wildlife"),
     R("Bear country right up to town", "Hike in a group of 3+, make noise, carry bear spray, and if you find a carcass, leave by the way you came and report it.", ["yell-safety"], "bears"),
     R("Remote, cold and far from help", "This week's NWS forecast near Silver Gate: lows in the upper 20s, and a chance of snow showers Saturday. Services in the northeast corner are closed for the winter; the nearest year-round park facilities are back at Mammoth.", ["nws", "yell-hours"], "cold"),
   ],
   "prep": [
     ("Plan an out-and-back trip", "With Beartooth closed, Cooke City is reached through the park from Gardiner."),
     ("Fuel, food and water for the whole drive", "Tower-Roosevelt services are closed."),
     ("Bear spray, traction and warm layers", "Lamar Valley pullouts get icy and cold at dawn and dusk."),
     ("Download GOES + offline maps in Gardiner", "Expect no signal on much of the route."),
   ],
   "cta_reason": "Wolves, bison and grizzlies in Lamar Valley, sub-freezing nights and closed services. Get GOES before you lose signal so its offline assessment and prevention tips are there if something goes wrong.",
  },
 ],
})
