"""Render preview screenshots (desktop full page + mobile). Needs: python -m http.server 8765 in site root.
Run with a Python that has playwright; uses the system Chrome at /usr/bin/google-chrome."""
from playwright.sync_api import sync_playwright
import os
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "previews")
PAGES = [("home", ""), ("yellowstone-north-entrance", "parks/yellowstone/north-entrance.html"),
         ("grand-canyon-south-entrance", "parks/grand-canyon/south-entrance.html"),
         ("yosemite-south-entrance", "parks/yosemite/south-entrance.html"),
         ("yellowstone-park", "parks/yellowstone/index.html")]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    for name, path in PAGES:
        for label, vp, mobile in [("desktop", {"width": 1280, "height": 900}, False), ("mobile", {"width": 390, "height": 844}, True)]:
            ctx = b.new_context(viewport=vp, device_scale_factor=2 if mobile else 1, is_mobile=mobile, has_touch=mobile)
            pg = ctx.new_page()
            pg.goto(f"http://localhost:8765/{path}", wait_until="networkidle", timeout=60000)
            pg.wait_for_timeout(1200)
            pg.screenshot(path=f"{OUT}/{name}-{label}.png", full_page=True)
            if not mobile:
                pg.screenshot(path=f"{OUT}/{name}-{label}-fold.png", full_page=False)
            ctx.close()
            print("saved", name, label)
    b.close()
