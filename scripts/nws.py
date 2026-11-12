import json, subprocess, sys, time
UA="ParkReadyGuides/0.1 (cbarcenas@goes.health)"
pts={
 "yell-north":(45.0290,-110.7080),"yell-northeast":(45.0040,-110.0050),
 "yose-arch-rock":(37.6870,-119.7300),"yose-big-oak-flat":(37.8000,-119.8740),"yose-south":(37.5070,-119.6320),"yose-hetch-hetchy":(37.8860,-119.8410),"yose-valley":(37.7456,-119.5936),
 "grca-south":(35.9930,-112.1210),"grca-desert-view":(36.0390,-111.8270),"grca-north-rim":(36.3360,-112.1170),
 "grsm-gatlinburg":(35.6850,-83.5370),"grsm-townsend":(35.6590,-83.7110),"grsm-cherokee":(35.5130,-83.3060),"grsm-newfound-gap":(35.6110,-83.4250),
 "zion-south":(37.2000,-112.9870),"zion-east":(37.2340,-112.8760),"zion-kolob":(37.4530,-113.2250),
 "glac-west":(48.5020,-113.9870),"glac-st-mary":(48.7460,-113.4370),
}
def get(u):
    for i in range(3):
        r=subprocess.run(["curl","-s","-A",UA,"-H","Accept: application/geo+json",u],capture_output=True,text=True).stdout
        try:
            d=json.loads(r)
            if 'properties' in d or 'features' in d: return d
        except: pass
        time.sleep(2)
    return {}
out={}
for k,(la,lo) in pts.items():
    p=get(f"https://api.weather.gov/points/{la},{lo}")
    fu=p.get('properties',{}).get('forecast')
    f=get(fu) if fu else {}
    a=get(f"https://api.weather.gov/alerts/active?point={la},{lo}")
    out[k]={"lat":la,"lon":lo,"forecast_url":fu,"forecast_page":f"https://forecast.weather.gov/MapClick.php?lat={la}&lon={lo}",
            "generated":f.get('properties',{}).get('generatedAt') or f.get('properties',{}).get('updateTime'),
            "periods":[{"name":x['name'],"temp":x['temperature'],"unit":x['temperatureUnit'],"short":x['shortForecast'],"detailed":x['detailedForecast'],"wind":x.get('windSpeed')} for x in f.get('properties',{}).get('periods',[])],
            "alerts":[{"event":x['properties']['event'],"headline":x['properties'].get('headline'),"ends":x['properties'].get('ends') or x['properties'].get('expires')} for x in a.get('features',[])]}
    print(k, len(out[k]['periods']), [x['event'] for x in out[k]['alerts']])
json.dump(out,open("data/raw/nws/forecasts.json","w"),indent=1)
