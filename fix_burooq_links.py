import glob

old = '''Abu Dhabi, UAE | <a href="tel:971544389066">+971544389066</a> |
<a href="https://wa.me/971544389066">WhatsApp</a>
</div>
</footer>'''

new = '''Abu Dhabi, UAE | <a href="tel:971544389066">+971544389066</a> |
<a href="https://wa.me/971544389066">WhatsApp</a> |
<a href="https://burooq.net">burooq.net</a>
</div>
</footer>'''

targets = [
    "articles/best-cctv-camera-system-home-small-business-buying-guide.html",
    "articles/4k-cctv-camera-system-villas-abu-dhabi.html",
    "articles/cctv-remote-monitoring-mobile-alerts-abu-dhabi.html",
    "articles/wired-vs-wireless-cctv-cameras-advantages-disadvantages.html",
    "articles/how-to-choose-best-cctv-camera-home-business-abu-dhabi.html",
]

fixed = 0
for fp in targets:
    with open(fp, encoding="utf-8") as f:
        html = f.read()
    if old not in html:
        print("PATTERN NOT FOUND, skipping:", fp)
        continue
    html = html.replace(old, new, 1)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(html)
    fixed += 1
    print("Fixed:", fp)

print(f"\nTotal fixed: {fixed}/{len(targets)}")
