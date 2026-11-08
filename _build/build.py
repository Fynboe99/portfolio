#!/usr/bin/env python3
"""Builds the static site from content.py.  Run from the repo root:  python3 _build/build.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from content import SITE, INTRO, PROJECTS, ABOUT

DIMS = json.load(open(os.path.join(HERE, "dims.json")))

import hashlib
def ver(path):
    return hashlib.md5(open(os.path.join(ROOT, path), "rb").read()).hexdigest()[:8]
CSS_V = ver("assets/site.css")
JS_V = ver("assets/site.js")


def img(key, sizes="100vw", cls="", eager=False, alt=""):
    w, h = DIMS[key]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img class="{cls}" src="/assets/img/{key}-2000.webp" '
            f'srcset="/assets/img/{key}-1000.webp 1000w, /assets/img/{key}-2000.webp 2000w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{alt}" decoding="async" {load}>')


VID_DIMS = {"glyptoteket": (1000, 1000), "dovely": (1280, 720), "vk-horse": (720, 520), "vakkerbo-hero": (1600, 844), "portrait": (900, 700), "palmes-horse": (720, 1280)}


def flex_cells(items, render):
    """Row of images/videos with equal heights and no cropping: each cell grows by its aspect ratio."""
    out = []
    for k in items:
        w, h = DIMS[k] if k in DIMS else VID_DIMS[k]
        out.append(f'<div class="cell" style="flex: {w / h:.4f} 1 0">{render(k)}</div>')
    return "".join(out)


def video(name, cls=""):
    return (f'<video class="{cls}" src="/assets/video/{name}.mp4" poster="/assets/video/{name}.jpg" '
            f'muted loop playsinline autoplay preload="metadata"></video>')


def deco(name, cls):
    return f'<img class="deco {cls}" src="/assets/deco/{name}.webp" alt="" aria-hidden="true" loading="lazy">'


def words(text):
    return " ".join(f'<span class="w"><span style="--i:{i}">{w}</span></span>' for i, w in enumerate(text.split()))


def vt(slug):
    return "t-" + slug.replace("-", "")


def caption(text):
    return f'<figcaption>{text}</figcaption>' if text else ""


def head(title, desc, path, body_cls=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#fefcf0">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE['url']}/assets/img/mtpl-cover-2000.webp">
<link rel="canonical" href="{SITE['url']}{path}">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="preload" href="/assets/fonts/bricolage-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v={CSS_V}">
<script>document.documentElement.classList.add('js')</script>
</head>
<body class="{body_cls}">
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <a class="brand" href="/" aria-label="Bastian Fynboe, home">
    <img class="brand-mark" src="/assets/deco/logo.webp" alt="" width="28" height="28">
    <span>Bastian Fynboe</span>
  </a>
  <nav>
    <a href="/#work">Work</a>
    <a href="/#about">About</a>
    <a href="/#contact">Contact</a>
  </nav>
</header>
<main id="main">
"""


FOOT_T = """</main>
<footer class="foot">
  <span>© Bastian Øster Fynboe</span>
  <span>Copenhagen</span>
  <a href="#main">Back to top</a>
</footer>
<div class="preview" aria-hidden="true"></div>
<script src="/assets/site.js?v=JSV" defer></script>
</body>
</html>
"""


FOOT = FOOT_T.replace("JSV", JS_V)


def contact_block():
    tel = SITE['phone'].replace(' ', '')
    return f"""
<section class="contact" id="contact">
  <div class="contact-text">
    <p class="contact-line">Send me an email, a text or call, and I'll look like this&nbsp;→</p>
    <a class="contact-mail" href="mailto:{SITE['email']}">{SITE['email']}</a>
    <a class="contact-phone" href="tel:{tel}">{SITE['phone']}</a>
  </div>
  <div class="contact-face">{video('portrait')}</div>
</section>
"""


def index():
    h = [head(SITE["title"], SITE["description"], "/", "home")]
    facts = "".join(f'<div class="fact"><span class="label">{k}</span><span>{v}</span></div>' for k, v in INTRO["facts"])
    h.append(f"""
<section class="hero intro-seq">
  <div class="hero-text">
    <h1 class="hello">{words(INTRO['hello'])}</h1>
    <p class="hero-lead">{INTRO['text']}</p>
  </div>
  <div class="hero-face">{video('portrait')}</div>
  <div class="facts">{facts}</div>
</section>

<section class="work" id="work">
  <ol class="index">
""")
    for i, p in enumerate(PROJECTS):
        h.append(f"""
    <li>
      <a class="row" href="/work/{p['slug']}/" data-preview="/assets/img/{p['cover']}-1000.webp" data-ratio="{DIMS[p['cover']][0] / DIMS[p['cover']][1]:.4f}">
        <span class="row-title" style="view-transition-name: {vt(p['slug'])}">{p['title']}{deco('spiral-blue', 'row-spiral')}</span>
        <span class="row-kind">{p['kind']}</span>
        <span class="row-year">{p['year']}</span>
        <span class="row-thumb">{img(p['cover'], '(max-width: 800px) 100vw, 1px', alt='')}</span>
      </a>
    </li>""")
    h.append("\n  </ol>\n</section>\n")

    lists = "".join(
        f'<div class="about-list"><span class="label">{t}</span><ul>' + "".join(f"<li>{x}</li>" for x in items) + "</ul></div>"
        for t, items in ABOUT["lists"])
    body = "".join(f'<p >{x}</p>' for x in ABOUT["body"])
    h.append(f"""
<section class="about" id="about">
  <div class="about-body">{body}</div>
  <div class="about-lists">{lists}</div>
</section>
""")
    h.append(contact_block())
    h.append(FOOT)
    return "".join(h)


def block_html(b):
    kind = b[0]
    if kind == "text":
        _, label, text = b
        return f'<section class="text-block"><span class="label">{label}</span><p>{text}</p></section>'
    if kind == "full":
        _, key, cap = b
        return f'<figure class="fig fig--full reveal-img">{img(key, "(min-width: 900px) 92vw, 100vw")}{caption(cap)}</figure>'
    if kind in ("pair", "trio"):
        _, keys, cap = b
        sz = "(min-width: 900px) 46vw, 50vw" if kind == "pair" else "(min-width: 900px) 30vw, 33vw"
        cells = flex_cells(keys, lambda k: img(k, sz))
        return f'<figure class="fig fig--row reveal-img"><div class="row-fig">{cells}</div>{caption(cap)}</figure>'
    if kind == "videos":
        _, names, cap = b
        cls = "fig--row" if len(names) > 1 else "fig--solo"
        if len(names) == 1 and VID_DIMS[names[0]][1] > VID_DIMS[names[0]][0]:
            cls += " tall"
        cells = flex_cells(names, lambda n: video(n))
        return f'<figure class="fig {cls}"><div class="row-fig">{cells}</div>{caption(cap)}</figure>'
    raise ValueError(kind)


def case(i, p):
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    h = [head(f"{p['title']} — {SITE['name']}", p["lead"], f"/work/{p['slug']}/", "case-page")]
    meta = "".join(f'<div><span class="label">{k}</span><span>{v}</span></div>' for k, v in p["meta"])
    if p.get("video"):
        cover = video(p["video"], "cover-media")
    else:
        cover = img(p["cover"], "100vw", "cover-media", eager=True, alt=f"{p['title']} for {p['client']}")
    dots = 'dots-pink' if i % 2 else 'dots-blue'
    h.append(f"""
<article class="case">
  <header class="case-head intro-seq">
    <a class="back" href="/#work">All work</a>
    <h1 class="case-title" style="view-transition-name: {vt(p['slug'])}">{p['title']}</h1>
    <p class="case-lead">{p['lead']}</p>
    <div class="case-meta">{meta}</div>
  </header>
  <figure class="case-cover">{cover}</figure>
  <div class="case-body">
    {''.join(block_html(b) for b in p['blocks'])}
  </div>
  <a class="next" href="/work/{nxt['slug']}/">
    <span class="label">Next project</span>
    <span class="next-title"><span style="view-transition-name: {vt(nxt['slug'])}">{nxt['title']}</span> {deco('spiral-blue', 'next-spiral')}</span>
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
