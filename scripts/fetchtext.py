import sys, re, subprocess, hashlib, os
from bs4 import BeautifulSoup
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
out="/workspace/goes-parks/data/raw/html"
for url in sys.argv[1:]:
    name=re.sub(r'[^a-z0-9]+','_',url.split('nps.gov/')[-1].lower())[:90]
    html=subprocess.run(["curl","-sL","-A",UA,"--max-time","30",url],capture_output=True,text=True).stdout
    open(f"{out}/{name}.html","w").write(html)
    s=BeautifulSoup(html,"html.parser")
    for t in s(["script","style","nav","header","footer","noscript"]): t.decompose()
    main=s.find(id="cs_control_main") or s.find("main") or s.find(id="main") or s.body or s
    txt=re.sub(r'\n\s*\n+','\n',main.get_text("\n"))
    txt=re.sub(r'[ \t]+',' ',txt)
    open(f"{out}/{name}.txt","w").write(txt)
    print(f"##### {url} -> {name}.txt ({len(txt)} chars)")
