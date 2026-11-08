#!/usr/bin/env python3
"""Builds the static site from content.py.  Run from the repo root:  python3 _build/build.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from content import SITE, INTRO, PROJECTS, ABOUT

DIMS = json.load(open(os.path.join(HERE, "dims.json")))


def img(key, sizes="100vw", cls="", eager=False, alt=""):
    w, h = DIMS[key]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img class="{cls}" src="/assets/img/{key}-2000.webp" '
            f'srcset="/assets/img/{key}-1000.webp 1000w, /assets/img/{key}-2000.webp 2000w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{alt}" decoding="async" {load}>')


def video(name, cls=""):
    return (f'<video class="{cls}" src="/assets/video/{name}.mp4" poster="/assets/video/{name}.jpg" '
            f'muted loop playsinline autoplay preload="metadata"></video>')


def caption(text):
    return f'<figcaption>{text}</figcaption>' if text else ""


def head(title, desc, path):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE['url']}/assets/img/mtpl-cover-2000.webp">
<link rel="canonical" href="{SITE['url']}{path}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300..500;1,6..72,300..500&family=Inter:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <a class="brand" href="/">{SITE['name']}</a>
  <nav>
    <a href="/#work">Work</a>
    <a href="/#about">About</a>
    <a href="/#contact">Contact</a>
  </nav>
</header>
<main id="main">
"""


FOOT = """</main>
<footer class="foot">
  <span>© Bastian Øster Fynboe</span>
  <span>Copenhagen</span>
  <a href="#main" class="totop">Back to top ↑</a>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""


def contact_block():
    return f"""
<section class="contact" id="contact">
  <p class="label reveal">Contact</p>
  <a class="contact-mail reveal" href="mailto:{SITE['email']}">{SITE['email']}</a>
  <p class="contact-sub reveal">Or call <a href="tel:{SITE['phone'].replace(' ', '')}">{SITE['phone']}</a>. Always happy to talk.</p>
</section>
"""


def index():
    h = [head(SITE["title"], SITE["description"], "/")]
    facts = "".join(f'<div class="fact"><span class="label">{k}</span><span>{v}</span></div>' for k, v in INTRO["facts"])
    h.append(f"""
<section class="intro">
  <h1 class="statement reveal">{INTRO['statement']}</h1>
  <div class="facts reveal">{facts}</div>
</section>

<section class="work" id="work">
  <div class="section-head reveal"><span class="label">Selected projects</span><span class="label">{len(PROJECTS):02d}</span></div>
  <div class="grid">
""")
    for i, p in enumerate(PROJECTS):
        size = "card--wide" if i < 2 else "card--half"
        sizes = "(min-width: 900px) 90vw, 100vw" if i < 2 else "(min-width: 900px) 45vw, 100vw"
        media = img(p["cover"], sizes=sizes, eager=(i == 0), alt=f"{p['title']} for {p['client']}")
        h.append(f"""
    <a class="card {size} reveal" href="/work/{p['slug']}/">
      <div class="card-media">{media}</div>
      <div class="card-meta">
        <span class="num">{i + 1:02d}</span>
        <span class="card-title">{p['title']}</span>
        <span class="card-kind">{p['kind']}</span>
        <span class="card-year">{p['year']}</span>
      </div>
    </a>""")
    h.append("\n  </div>\n</section>\n")

    lists = "".join(
        f'<div class="about-list"><span class="label">{t}</span><ul>' + "".join(f"<li>{x}</li>" for x in items) + "</ul></div>"
        for t, items in ABOUT["lists"])
    body = "".join(f"<p>{x}</p>" for x in ABOUT["body"])
    h.append(f"""
<section class="about" id="about">
  <p class="label reveal">About</p>
  <p class="about-lead reveal">{ABOUT['lead']}</p>
  <div class="about-body reveal">{body}</div>
  <div class="about-lists reveal">{lists}</div>
</section>
""")
    h.append(contact_block())
    h.append(FOOT)
    return "".join(h)


def block_html(b):
    kind = b[0]
    if kind == "text":
        _, label, text = b
        return f'<section class="text-block reveal"><span class="label">{label}</span><p>{text}</p></section>'
    if kind == "full":
        _, key, cap = b
        return f'<figure class="fig fig--full reveal">{img(key, "(min-width: 900px) 92vw, 100vw")}{caption(cap)}</figure>'
    if kind in ("pair", "trio"):
        _, keys, cap = b
        sz = "(min-width: 900px) 46vw, 100vw" if kind == "pair" else "(min-width: 900px) 30vw, 100vw"
        imgs = "".join(f'<div class="cell">{img(k, sz)}</div>' for k in keys)
        return f'<figure class="fig fig--{kind} reveal"><div class="row">{imgs}</div>{caption(cap)}</figure>'
    if kind == "videos":
        _, names, cap = b
        vids = "".join(f'<div class="cell">{video(n)}</div>' for n in names)
        return f'<figure class="fig fig--pair reveal"><div class="row">{vids}</div>{caption(cap)}</figure>'
    raise ValueError(kind)


def case(i, p):
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    h = [head(f"{p['title']} — {SITE['name']}", p["lead"], f"/work/{p['slug']}/")]
    meta = "".join(f'<div><span class="label">{k}</span><span>{v}</span></div>' for k, v in p["meta"])
    if p.get("video"):
        cover = video(p["video"], "cover-media")
    else:
        cover = img(p["cover"], "100vw", "cover-media", eager=True, alt=f"{p['title']} for {p['client']}")
    h.append(f"""
<article class="case">
  <header class="case-head">
    <p class="label reveal"><span class="num">{i + 1:02d}</span> {p['kind']}</p>
    <h1 class="case-title reveal">{p['title']}</h1>
    <p class="case-lead reveal">{p['lead']}</p>
    <div class="case-meta reveal">{meta}</div>
  </header>
  <figure class="case-cover reveal">{cover}</figure>
  <div class="case-body">
    {''.join(block_html(b) for b in p['blocks'])}
  </div>
  <a class="next reveal" href="/work/{nxt['slug']}/">
    <span class="label">Next project</span>
    <span class="next-title">{nxt['title']} <span class="arrow">→</span></span>
  </a>
</article>
""")
    h.append(contact_block())
    h.append(FOOT)
    return "".join(h)


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)


write("index.html", index())
for i, p in enumerate(PROJECTS):
    write(f"work/{p['slug']}/index.html", case(i, p))
print("Built", 1 + len(PROJECTS), "pages")
