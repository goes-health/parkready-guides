src("grsm-seasonal", "Smokies seasonal road schedule (2026 season)", "https://www.nps.gov/grsm/planyourvisit/seasonalroads.htm")
src("grsm-cond", "Smokies current conditions & trail closures", "https://www.nps.gov/grsm/planyourvisit/conditions.htm")
src("grsm-bears", "Smokies black bears", "https://www.nps.gov/grsm/learn/nature/black-bears.htm")
src("grsm-fall", "News release: View elk and black bears safely this fall (Sep 14, 2026)", "https://www.nps.gov/grsm/learn/news/great-smoky-mountains-national-park-reminds-visitors-to-view-elk-and-black-bears-safely-this-fall.htm")
src("grsm-elk", "News release: Approaching elk is dangerous and illegal (Oct 7, 2026)", "https://www.nps.gov/grsm/learn/news/great-smoky-mountains-national-park-reminds-visitors-approaching-elk-is-both-dangerous-and-illegal.htm")
src("grsm-bullhead", "News release: Bullhead Trail reopens (Nov 19, 2026)", "https://www.nps.gov/grsm/learn/news/great-smoky-mountains-national-park-reopens-rehabilitated-bullhead-trail.htm")
src("grsm-directions", "Smokies directions & GPS warning", "https://www.nps.gov/grsm/planyourvisit/directions.htm")

PARKS.append({
 "slug": "great-smoky-mountains", "code": "grsm", "name": "Great Smoky Mountains National Park", "short": "Great Smoky Mountains",
 "state": "TN · NC",
 "tagline": "Kuwohi Road and Roaring Fork have their last week of the season (through Nov 29); rain arrives for Thanksgiving.",
 "summary": "The Smokies' primary roads (Newfound Gap Road/US-441, Little River Road and Laurel Creek Road) are open 24/7 year-round, weather permitting. NPS no longer lists last week's snow-and-ice closure alert for Kuwohi Road, and this is the last week of its season: Kuwohi Road and Roaring Fork Motor Nature Trail are scheduled to close for winter after Nov 29. Bullhead Trail reopened Nov 19 after a two-year rehabilitation. NWS forecasts a sunny Tuesday, then rain Wednesday night through Thanksgiving Day, with a chance of rain and snow at Newfound Gap Thursday night. There's no entrance fee, but any vehicle parked longer than 15 minutes needs a parking tag ($5 daily, $15 weekly, $40 annual).",
 "summary_sources": ["grsm-alerts", "grsm-seasonal", "grsm-bullhead", "nps-api", "nws"],
 "cta_reason": "Black bears feeding hard before winter, elk near Cherokee, wet cold that leads to hypothermia, and mountain roads where GPS and signal both fail. GOES works offline.",
 "fees": "No entrance fee. A parking tag is required for any vehicle parked more than 15 minutes: daily $5, weekly $15, annual $40. America the Beautiful passes are not accepted in place of a tag.",
 "fees_sources": ["grsm-alerts", "grsm-fees"],
 "closed": [
   {"name": "Seasonal secondary roads", "note": "Heintooga Ridge Road, Parson Branch Road and Rich Mountain Road are closed for the season. Straight Fork and the one-way section of Balsam Mountain Road are closed. Park Headquarters Road is closed for water and wastewater work.", "sources": ["grsm-alerts", "grsm-seasonal"]},
 ],
 "park_risks": [
   R("Black bears", "Over the last 10 years the Smokies averaged 339 reported negative human–bear encounters a year. In fall, bears feed heavily (up to 20,000 calories a day) and show up near roadsides. Approaching within 50 yards (150 ft) is illegal. If a black bear attacks and isn't after your food, fight back; don't play dead.", ["grsm-bears", "grsm-fall"], "bears"),
   R("Elk", "It's illegal to approach elk within 25 yards (75 ft). During the fall rut, bulls can be aggressive toward people, vehicles and pets. NPS closed the fields around Oconaluftee and Cataloochee to visitors during the rut, so obey any posted closures.", ["grsm-fall", "grsm-elk"], "wildlife"),
   R("Wet cold and fast-changing mountain weather", "Temperatures can vary 10–20°F between base and summit, and clear skies lower down don't guarantee the same up high. This week nights drop into the 30s (28°F at Newfound Gap Thursday night), and wet clothes plus wind on a ridge can still chill you fast.", ["nps-api", "nws"], "cold"),
   R("GPS and no signal", "NPS warns that GPS units may send drivers the wrong way on one-way roads or to dead ends, and points mobile users to offline maps for areas without cell service.", ["grsm-directions"], "weather"),
 ],
 "entrances": [
  {
   "slug": "gatlinburg-entrance", "name": "Gatlinburg Entrance (Sugarlands)", "gateway": "Gatlinburg, TN (US-441)", "nws": "grsm-gatlinburg", "status": "open",
   "status_label": "Open — Kuwohi Road's last week",
   "intro": "The Gatlinburg entrance on US-441 leads to Sugarlands Visitor Center and then up Newfound Gap Road over the crest to North Carolina. It's one of the park's three main entrances.",
   "conditions": [
     C("Newfound Gap Road (US-441) is a primary road, open 24/7 year-round, weather permitting. NWS forecast at Newfound Gap: sunny Tuesday, light rain Wednesday night into Thanksgiving, a chance of rain and snow Thursday night, highs around 37–51°F and lows near 28–38°F.", ["nps-api", "grsm-seasonal", "nws"], "open"),
     C("Kuwohi Road (formerly Clingmans Dome Road): NPS no longer lists the Nov 16 snow-and-ice closure alert. Its seasonal schedule runs through Nov 29, and it can close at any time for snow, ice or hazardous weather.", ["grsm-alerts", "grsm-seasonal"], "caution"),
     C("Roaring Fork Motor Nature Trail: open through Nov 29 (one-way and steep; no RVs, buses or vans over 25 ft, and no trailers).", ["grsm-seasonal"], "open"),
     C("Laurel Falls Trail is closed for rehabilitation (closed since Jan 2025 for about 18 months). Bullhead Trail, one of the routes to Mount Le Conte, reopened Nov 19 after rehabilitation.", ["grsm-cond", "grsm-bullhead"], "closed"),
     C("Park Headquarters Road is closed for Sugarlands water and wastewater work.", ["grsm-alerts"], "closed"),
     C("Parking tags are sold at the Gatlinburg Welcome Center and Sugarlands Visitor Center, and online. Visitor centers are open year-round except Christmas Day.", ["grsm-fees", "grsm-cond"], None),
   ],
   "risks": [
     R("Cold, wet crest", "Gatlinburg is forecast in the 50s, but Newfound Gap runs about 10°F colder, with light rain Wednesday night into Thanksgiving and a chance of rain and snow Thursday night. Bring a warm, waterproof layer for the overlooks.", ["nws"], "cold"),
     R("Roadside bears", "Fall is peak feeding time. Use pull-offs, get fully off the road, and stay 50 yards away. Never feed bears, and put trash in bear-proof containers.", ["grsm-fall", "grsm-bears"], "bears"),
     R("Short days on the trail", "This week in Gatlinburg: highs around 48–60°F, lows near 34–45°F, and rain showers Wednesday night through Thursday. Late-November sunset comes early, so carry a light and a layer in case a hike runs long.", ["nws"], "cold"),
   ],
   "prep": [
     ("Buy a parking tag first", "Required for any stop over 15 minutes; most trailheads have no tag machine."),
     ("Last call for Kuwohi", "The road's season ends Nov 29; check NPS alerts the morning you go."),
     ("Rain shell and warm, non-cotton layers", "Summit temps run 10–20°F colder than town."),
     ("Download GOES in Gatlinburg", "Before the signal drops on the climb."),
   ],
   "cta_reason": "Roadside bears, a colder crest and early sunsets. Download GOES in Gatlinburg so its offline hypothermia and wildlife guidance is ready.",
  },
  {
   "slug": "townsend-entrance", "name": "Townsend Entrance", "gateway": "Townsend, TN (TN-73)", "nws": "grsm-townsend", "status": "open",
   "status_label": "Open — rainy Thanksgiving",
   "intro": "The Townsend entrance on TN-73 is the 'quiet side' gateway to Little River Road, Laurel Creek Road and Cades Cove.",
   "conditions": [
     C("Little River Road and Laurel Creek Road: primary roads, open 24/7 year-round, weather permitting.", ["nps-api"], "open"),
     C("Cades Cove Loop Road: open sunrise to sunset daily, weather permitting.", ["grsm-seasonal"], "open"),
     C("Rich Mountain Road and Parson Branch Road (out of Cades Cove) are closed for the season. Forge Creek Road is open through Dec 31, subject to closures for snow, ice or mud.", ["grsm-alerts", "grsm-seasonal"], "closed"),
     C("Parking tags are sold at The Great Smokies Welcome Center in Townsend, Cades Cove Visitor Center and the Tremont Institute store. Cades Cove Campground is open year-round.", ["grsm-fees", "grsm-cond"], None),
   ],
   "risks": [
     R("Bear jams in Cades Cove", "Cades Cove is one of the park's best places to see bears, and one of the easiest places to get too close. Approaching within 50 yards is illegal. Use pull-offs and don't stop in the road.", ["grsm-fall", "grsm-bears"], "bears"),
     R("Cold mornings in the cove", "NWS forecast for Townsend: sunny Tuesday, rain showers Wednesday night through Thursday, highs around 49–61°F and lows near 31–42°F. Cold, wet early starts in Cades Cove call for layers.", ["nws"], "cold"),
     R("Little River's slick rocks", "Wet rocks and cold water make the Little River a fall and hypothermia risk. NPS links to USGS gauges for current flow.", ["grsm-cond"], "injury"),
   ],
   "prep": [
     ("Parking tag before Cades Cove", "Required for stops over 15 minutes."),
     ("Time Cades Cove for daylight", "The loop is open sunrise to sunset."),
     ("Download GOES in Townsend", "Before you head up Little River Road."),
   ],
   "cta_reason": "Cades Cove bears, cold mornings and slick river rock. Download GOES in Townsend so its offline wildlife and cold-weather guidance travels with you.",
  },
  {
   "slug": "cherokee-entrance", "name": "Cherokee Entrance (Oconaluftee)", "gateway": "Cherokee, NC (US-441)", "nws": "grsm-cherokee", "status": "open",
   "status_label": "Open — elk area",
   "intro": "The Cherokee entrance on US-441 in North Carolina leads to Oconaluftee Visitor Center and the Mountain Farm Museum, then north up Newfound Gap Road to the state line.",
   "conditions": [
     C("Newfound Gap Road (US-441): open 24/7 year-round, weather permitting. NWS forecasts light rain at Newfound Gap Wednesday night into Thanksgiving and a chance of rain and snow Thursday night.", ["nps-api", "nws"], "open"),
     C("Heintooga Ridge Road (off the Blue Ridge Parkway) is closed for the season, and Straight Fork and the one-way section of Balsam Mountain Road are closed.", ["grsm-alerts", "grsm-seasonal"], "closed"),
     C("Kuwohi Road: no current NPS closure alert; its season runs through Nov 29, subject to snow and ice closures.", ["grsm-alerts", "grsm-seasonal"], "caution"),
     C("Cataloochee Road: a year-round gravel road that may close for snow and ice.", ["grsm-seasonal"], None),
     C("Parking tags are sold at Oconaluftee Visitor Center and Kuwohi Visitor Center, and online.", ["grsm-fees"], None),
   ],
   "risks": [
     R("Elk in the Oconaluftee fields", "Stay at least 25 yards (75 ft) from elk; bulls in the fall rut can charge people, cars and pets. NPS closed these fields to visitors during the rut, so follow posted closures and ranger instructions.", ["grsm-fall", "grsm-elk"], "wildlife"),
     R("Bears along US-441", "Black bears move across the park feeding on acorns in fall. Never stop in the roadway to watch; use pull-offs.", ["grsm-fall"], "bears"),
     R("Chilly nights", "NWS forecast for Cherokee: sunny Tuesday, light rain Wednesday night into Thanksgiving, highs around 52–65°F and lows near 29–41°F.", ["nws"], "cold"),
   ],
   "prep": [
     ("Bring binoculars", "25 yards from elk and 50 from bears is the law."),
     ("Check alerts before heading up", "Kuwohi Road's season ends Nov 29 and it can close for ice."),
     ("Download GOES in Cherokee", "Before the climb toward the state line."),
   ],
   "cta_reason": "Elk in the fields, bears by the road and cold nights. Download GOES in Cherokee so its offline wildlife and cold guidance is on your phone.",
  },
 ],
})
