"""Render every page of the site as dependency-free static HTML.

Copy comes from guide_content.py and site_content.py; conversions come from
specimens.json (real OpenCC 1.4.2 output). The build also records which
characters each self-hosted font must contain (font_glyphs.json) so fonts.py can
subset them and check.py can prove the subsets still cover every page.
"""

import json
import math
import random
import re
from argparse import ArgumentParser
from html import escape
from pathlib import Path

from guide_content import ARTICLES, LOCALES
from site_content import CHANGELOG, HOME, LANG_CELLS, NOT_FOUND, PRIVACY, PROOF, ROOT, SUPPORT, UI

SCRIPTS = Path(__file__).resolve().parent
SITE = SCRIPTS.parent / "site"
ORIGIN = "https://openccman.gewill.org"
LANGUAGES = ("zh-Hans", "zh-Hant", "en")
APP_STORE = "https://apps.apple.com/app/id6474449401"
PRESET_ORDER = ("t2s", "s2t", "s2twp", "s2hk")
OUT_LANG = {"t2s": "zh-Hans", "s2t": "zh-Hant", "s2twp": "zh-Hant-TW", "s2hk": "zh-Hant-HK"}
HOME_SPECIMENS = ("mouse", "queen", "hair", "line", "printer")
SPEC = json.loads((SCRIPTS / "specimens.json").read_text(encoding="utf-8"))
SPEC_BY_ID = {s["id"]: s for s in SPEC["specimens"]}


def esc(text):
    return escape(text, quote=True)


# Characters each self-hosted face must carry ------------------------------------

GLYPHS = {"serif-sc": set(), "serif-tc": set(), "hand": set()}


def display(text, lang):
    """Record text set in the display serif; Latin display text uses the SC subset."""
    GLYPHS["serif-tc" if lang.startswith("zh-Hant") else "serif-sc"].update(text)
    return text


def hand(text):
    GLYPHS["hand"].update(text)
    return text


def plain(html):
    return re.sub(r"<[^>]+>", "", html)


# Hand-drawn marks ---------------------------------------------------------------

def _catmull(points):
    d = f"M{points[0][0]:.1f} {points[0][1]:.1f}"
    for i in range(len(points) - 1):
        p0 = points[i - 1] if i else points[i]
        p1, p2 = points[i], points[i + 1]
        p3 = points[i + 2] if i + 2 < len(points) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f"C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d


def ring_path(n, variant):
    """A pen loop around n cells: slightly tilted, wobbling, overshooting its start."""
    rnd = random.Random(n * 7919 + variant * 104729)
    width, height = n * 100 + 29, 129
    cx, cy = width / 2, height / 2
    rx, ry = width / 2 - 9, height / 2 - 9
    rot = math.radians(rnd.uniform(-2.5, 2.5))
    start = math.radians(rnd.uniform(195, 235))
    sweep = math.radians(360 + rnd.uniform(24, 38))
    steps = 30 + 4 * n
    ph1, ph2 = rnd.uniform(0, math.tau), rnd.uniform(0, math.tau)
    points = []
    for k in range(steps + 1):
        t = k / steps
        a = start + sweep * t
        wobble = 1 + 0.03 * math.sin(2 * a + ph1) + 0.018 * math.sin(3 * a + ph2)
        grow = 1 + 0.06 * (t - 0.5)
        x, y = rx * wobble * grow * math.cos(a), ry * wobble * grow * math.sin(a)
        points.append((cx + x * math.cos(rot) - y * math.sin(rot), cy + x * math.sin(rot) + y * math.cos(rot)))
    return _catmull(points)


RINGS = {str(n): [ring_path(n, v) for v in range(3)] for n in range(1, 6)}
KEEP = "M7.2 1.5L12.3 10.2L1.8 10.6L7 1.9"


def ring_svg(n, variant):
    d = RINGS[str(min(n, 5))][variant % 3]
    return (f'<svg class="ring" viewBox="0 0 {n * 100 + 29} 129" preserveAspectRatio="none" '
            f'aria-hidden="true" focusable="false"><path d="{d}" pathLength="100"/></svg>')


def icon(cls, box, d):
    return f'<svg class="{cls}" viewBox="{box}" aria-hidden="true" focusable="false"><path d="{d}"/></svg>'


GO = icon("go arrow", "0 0 40 12", "M1 6H38M32 1.5L38.5 6L32 10.5")
LINK_ARROW = icon("arrow", "0 0 34 12", "M1 6H32M26.5 1.5L33 6L26.5 10.5")
EXT = icon("arrow", "0 0 14 14", "M3 11L11 3M5.5 3H11V8.5")
CHEV = icon("arrow", "0 0 7 12", "M1 1L6 6L1 11")
NEXT = icon("arrow", "0 0 18 18", "M15.2 9.4a6.2 6.2 0 1 1-2.3-5M13.6 1.4l-.5 3.4-3.3-.4")
NOTE_ARROW = icon("arrow", "0 0 16 8", "M1 4H14M10.5 1L14.5 4L10.5 7")
VIA = icon("arrow", "0 0 56 14", "M1 7H53M47 2L54 7L47 12")
TRI = icon("arrow", "0 0 12 11", "M6 1.2L11 9.8H1Z")
CHECK = icon("arrow", "0 0 12 11", "M1.5 6L4.6 9L10.5 1.8")
PLAY = '<svg class="tri" viewBox="0 0 30 34" aria-hidden="true" focusable="false"><path d="M3 2.5L27.5 17L3 31.5Z"/></svg>'
KEEP_SVG = f'<svg class="keep" viewBox="0 0 14 12" aria-hidden="true" focusable="false"><path d="{KEEP}" pathLength="100"/></svg>'
CARET = ('<svg class="caret" viewBox="0 0 32 36" aria-hidden="true" focusable="false">'
         '<path d="M3 33L16.2 4L29 33" pathLength="100"/></svg>')
WARN = (f'<svg class="mk" viewBox="0 0 129 129" aria-hidden="true" focusable="false">'
        f'<path d="{RINGS["1"][2]}"/><path d="M64.5 36V76M64.5 92V93"/></svg>')


# Manuscript headings -------------------------------------------------------------

LATIN_RUN = re.compile(r"[A-Za-z0-9][A-Za-z0-9 .\-+/]*[A-Za-z0-9]|[A-Za-z0-9]")


def ms_text(text, keep_together=(), breaks=()):
    """CJK sits one character per cell; a Latin run spans whole cells."""
    out, pos = [], 0
    for match in LATIN_RUN.finditer(text):
        out.append(esc(text[pos:match.start()].replace(" ", "")))
        run = match.group(0)
        cells = max(1, math.ceil(len(run) * 0.34 + 0.25))
        out.append(f'<span class="lat n{cells}">{esc(run)}</span>')
        pos = match.end()
    out.append(esc(text[pos:].replace(" ", "")))
    html = "".join(out)
    for word in keep_together:
        html = html.replace(esc(word), f'<span class="nw">{esc(word)}</span>', 1)
    for word in breaks:
        if word:
            html = html.replace(esc(word), esc(word) + "<wbr>", 1)
    return html


def heading(tag, text, lang, cls="", attrs="", keep_together=(), breaks=()):
    display(text, lang)
    if lang == "en":
        return f'<{tag} class="ms ms-latin {cls}"{attrs}><span class="ms-t">{esc(text)}</span></{tag}>'
    return f'<{tag} class="ms {cls}"{attrs}><span class="ms-t">{ms_text(text, keep_together, breaks)}</span></{tag}>'


# Page shell -------------------------------------------------------------------------

def page_path(lang, key):
    if key == "home":
        return f"/{lang}/"
    if key == "guides":
        return f"/{lang}/guides/"
    if key.startswith("guide:"):
        return f"/{lang}/guides/{key[6:]}.html"
    return f"/{lang}/{key}.html"


def canonical(lang, key):
    return ORIGIN + page_path(lang, key).removesuffix(".html")


def masthead(lang, key):
    u = UI[lang]
    links = []
    for item in ("guides", "changelog", "support", "privacy"):
        current = ""
        if key == item:
            current = ' aria-current="page"'
        elif item == "guides" and key.startswith("guide:"):
            current = ' aria-current="true"'
        links.append(f'<a href="{page_path(lang, item)}"{current}>{u[item]}</a>')
    cells = []
    for other, glyph, name in LANG_CELLS:
        current = ' aria-current="page"' if other == lang else ""
        display(glyph, other)
        cells.append(f'<a href="{page_path(other, key)}" lang="{other}" hreflang="{other}" '
                     f'aria-label="{name}" title="{name}"{current}>{glyph}</a>')
    return (
        f'<a class="skip" href="#main">{u["skip"]}</a>'
        '<header class="masthead"><div class="wrap masthead-in">'
        f'<a class="brand" href="{page_path(lang, "home")}"><img src="/assets/icon.png" width="32" height="32" alt="">OpenCCman</a>'
        f'<p class="imprint">{u["imprint"]}</p>'
        f'<nav class="nav" aria-label="{u["nav"]}">{"".join(links)}</nav>'
        f'<nav class="langs" aria-label="{u["langs"]}">{"".join(cells)}</nav>'
        '</div></header>'
    )


def colophon(lang):
    u = UI[lang]
    return (
        '<footer class="colophon"><div class="wrap colophon-in">'
        '<span>© 2026 OpenCCman</span>'
        f'<nav aria-label="{u["foot"]}">'
        f'<a href="{page_path(lang, "guides")}">{u["guides"]}</a><a href="{page_path(lang, "changelog")}">{u["changelog"]}</a>'
        f'<a href="{page_path(lang, "privacy")}">{u["privacy"]}</a><a href="{page_path(lang, "support")}">{u["support"]}</a>'
        '<a href="https://github.com/gewill/OpenCCman">GitHub</a>'
        '<a href="https://github.com/BYVoid/OpenCC">OpenCC</a></nav>'
        f'<span class="count" data-count="{u["count"]}" hidden></span>'
        '</div></footer>'
    )


def head(lang, title, description, key=None, fonts=(), specimens=False):
    links = ""
    if key:
        links = f'<link rel="canonical" href="{canonical(lang, key)}">' + "".join(
            f'<link rel="alternate" hreflang="{other}" href="{canonical(other, key)}">' for other in LANGUAGES)
    preload = "".join(
        f'<link rel="preload" href="/assets/fonts/{name}.woff2" as="font" type="font/woff2" crossorigin>' for name in fonts)
    scripts = ('<script src="/assets/specimens.js" defer></script>' if specimens else "") + \
        '<script src="/assets/site.js" defer></script>'
    return (
        f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f'<title>{esc(title)}</title><meta name="description" content="{esc(description)}">'
        '<meta name="theme-color" content="#f7f9f6" media="(prefers-color-scheme: light)">'
        '<meta name="theme-color" content="#121714" media="(prefers-color-scheme: dark)">'
        f'<link rel="icon" href="/assets/icon.png">{preload}<link rel="stylesheet" href="/assets/style.css">'
        f'{links}{scripts}</head>'
    )


def serif(lang):
    """Faces the first viewport needs; Latin display (the wordmark, English headings) uses the SC subset."""
    return ("serif-tc", "serif-sc") if lang == "zh-Hant" else ("serif-sc",)


def document(lang, key, title, description, body, fonts=None, specimens=False, body_class=""):
    fonts = fonts if fonts is not None else serif(lang)
    classes = f' class="{body_class}"' if body_class else ""
    return (head(lang, title, description, key, fonts, specimens)
            + f'<body{classes}>{masthead(lang, key)}<main id="main">{body}</main>{colophon(lang)}</body></html>\n')


def stamp(label, href=APP_STORE):
    return f'<a class="stamp" href="{href}">{esc(label)}{EXT}</a>'


def note(lang, html):
    mark = UI[lang]["note"]
    if lang != "en":
        hand(mark)
    return f'<aside class="note"><span class="note-mark" aria-hidden="true">{mark}</span><p>{html}</p></aside>'


# Proof desk ------------------------------------------------------------------------

def marks(variant, preset, t):
    out_lang = OUT_LANG[preset]
    segs, outs, notes = [], [], []
    mark = j = 0
    for seg in variant["segs"]:
        kind = seg["k"]
        cells = "".join(
            f'<span>{esc(ch)}{KEEP_SVG if kind == "keep" and i in seg.get("keep", []) else ""}</span>'
            for i, ch in enumerate(seg["s"]))
        if kind == "same":
            segs.append(f'<span class="seg k-same"><span class="fix" lang="{out_lang}"></span>'
                        f'<span class="cells">{cells}</span><span class="why"></span></span>')
        else:
            fix = "" if kind == "keep" else esc(seg["o"])
            ring = "" if kind == "keep" else ring_svg(len(seg["s"]), mark)
            segs.append(f'<span class="seg k-{kind} i{mark}"><span class="fix" lang="{out_lang}">{fix}</span>'
                        f'<span class="cells">{cells}</span>{ring}<span class="why">{t["kinds"][kind]}</span></span>')
            item = f'<li class="k-{kind}"><span class="from">{esc(seg["s"])}</span>'
            if kind != "keep":
                item += (f'{NOTE_ARROW}<span class="vh">{t["to"]}</span>'
                         f'<span class="to" lang="{out_lang}">{esc(seg["o"])}</span>')
            item += f'<span class="kind">{t["kinds"][kind]}</span>'
            if seg.get("alt"):
                item += f'<span class="alt">{esc(t["alt"].format(seg["alt"]))}</span>'
            notes.append(item + "</li>")
            mark += 1
        changed = kind not in ("same", "keep")
        for ch in seg["o"]:
            outs.append(f'<span class="{"chg " if changed else ""}j{j}">{esc(ch)}</span>')
            j += 1
    return "".join(segs), "".join(outs), "".join(notes)


def record_specimens(ids):
    """The script can show any preset of any specimen, so every glyph ships."""
    for key in ids:
        for preset, variant in SPEC_BY_ID[key]["variants"].items():
            hand(variant["src"])
            hand(variant["out"])
            display(variant["out"], OUT_LANG[preset])


def proof_desk(lang, ids, preset="s2twp", group="preset"):
    t = PROOF[lang]
    record_specimens(ids)
    variant = SPEC_BY_ID[ids[0]]["variants"][preset]
    segs, outs, notes = marks(variant, preset, t)
    radios = "".join(
        f'<label><input type="radio" name="{group}" value="{p}"{" checked" if p == preset else ""}>'
        f'<span>{esc(t["presets"][p])}</span></label>' for p in PRESET_ORDER)
    src_lang = "zh-Hant" if preset == "t2s" else "zh-Hans"
    summary = t["summary"].replace("{src}", variant["src"]).replace("{out}", variant["out"])
    return (
        f'<figure class="proof" data-proof data-group="{group}" data-specimens="{" ".join(ids)}" aria-labelledby="proof-caption">'
        f'<div class="proof-bar"><fieldset class="presets"><legend class="vh">{t["legend"]}</legend>{radios}</fieldset>'
        f'<button class="proof-next" type="button" hidden>{NEXT}<span>{t["next"]}</span></button></div>'
        f'<div class="proof-rows" aria-hidden="true"><span class="proof-label">{t["src"]}</span>'
        f'<div class="line src" lang="{src_lang}">{segs}</div>'
        f'<span class="proof-label">{t["out"]}</span><p class="out" lang="{OUT_LANG[preset]}">{outs}</p></div>'
        f'<p class="vh" data-summary>{esc(summary)}</p>'
        f'<div class="proof-foot"><ol class="proof-notes" aria-label="{t["notes"]}">{notes}</ol></div>'
        '<p class="vh" data-live aria-live="polite"></p>'
        f'<figcaption class="proof-caption" id="proof-caption">{t["caption"]}</figcaption>'
        '</figure>'
    )


def emphasised(variant):
    return "".join(
        f'<span class="chg">{esc(seg["o"])}</span>' if seg["k"] not in ("same", "keep") else esc(seg["o"])
        for seg in variant["segs"])


# Home -------------------------------------------------------------------------------

def feature_figs(lang):
    f = HOME[lang]["fig"]
    printer = SPEC_BY_ID["printer"]["variants"]["s2twp"]
    hair = SPEC_BY_ID["hair"]["variants"]["s2twp"]
    display(printer["src"], "zh-Hans")
    display(printer["out"], "zh-Hant-TW")
    hand(hair["src"])
    display(hair["out"], "zh-Hant-TW")
    chips = "".join(
        ('<span class="on">' if p == "s2twp" else "<span>") + esc(PROOF[lang]["presets"][p]) + "</span>"
        for p in PRESET_ORDER)
    shortcut = (
        '<figure class="fig fig-shortcut">'
        f'<div class="window"><div class="window-bar" aria-hidden="true"><span>{f["other_app"]}</span></div>'
        f'<p class="window-body" lang="zh-Hans"><mark>{esc(printer["src"])}</mark></p></div>'
        f'<span class="keycap">{f["key"]}</span>'
        '<div class="branches">'
        f'<div class="branch"><span class="branch-title">{LINK_ARROW}{f["replace"]}</span>'
        f'<p class="result" lang="zh-Hant-TW">{emphasised(printer)}</p></div>'
        f'<div class="branch"><span class="branch-title">{LINK_ARROW}{f["open"]}</span>'
        '<div class="mini-app"><img src="/assets/icon.png" width="28" height="28" alt=""><b>OpenCCman</b>'
        f'<span>{f["app_line"]}</span></div></div>'
        '</div>'
        f'<figcaption class="fig-label">{f["fig_caption"]}</figcaption>'
        '</figure>'
    )
    layout = (
        '<figure class="fig fig-layout" data-layout="side">'
        '<div class="fig-head"><span class="fig-label">Mac · iPad</span>'
        f'<div class="seg-toggle" role="group" aria-label="{f["layout_label"]}" hidden>'
        f'<button type="button" data-layout-to="side" aria-pressed="true">{f["side"]}</button>'
        f'<button type="button" data-layout-to="stacked" aria-pressed="false">{f["stacked"]}</button></div></div>'
        f'<div class="panes"><div class="pane pane-src"><span class="fig-label">{f["src"]}</span><p lang="zh-Hans">{esc(hair["src"])}</p></div>'
        f'<div class="pane pane-out"><span class="fig-label">{f["out"]}</span><p lang="zh-Hant-TW">{esc(hair["out"])}</p></div></div>'
        f'<p class="chips">{chips}</p>'
        '</figure>'
    )
    txt = (
        '<figure class="fig fig-txt">'
        '<div class="file"><span class="file-name">essay.txt</span><span class="file-lines" aria-hidden="true"><i></i><i></i><i></i></span></div>'
        f'<div class="via">{VIA}<span>{f["local"]}</span></div>'
        '<div class="file file-out"><span class="file-name">essay-converted.txt</span><span class="file-lines" aria-hidden="true"><i></i><i></i><i></i></span></div>'
        f'<p class="chips">{"".join(f"<span>{esc(c)}</span>" for c in f["chips"])}</p>'
        '</figure>'
    )
    return [shortcut, layout, txt]


def toc(lang, annotated=False, exclude=None):
    rows = []
    for index, (slug, article) in enumerate(ARTICLES.items(), 1):
        if slug == exclude:
            continue
        a = article[lang]
        display(a["card"], lang)
        pencil = ""
        if annotated:
            order = LOCALES[lang]["order"][index - 1]
            if lang != "en":
                hand(order)
            pencil = f'<span class="pencil">{order}</span>'
        rows.append(
            f'<li><a href="{page_path(lang, "guide:" + slug)}"><span class="no">{index}{ring_svg(1, index)}</span>'
            f'<span class="tx"><span class="t">{a["card"]}</span><span class="s">{a["summary"]}</span></span>'
            f'{pencil}{GO}</a></li>')
    return f'<ol class="toc{" toc-annotated" if annotated else ""}">{"".join(rows)}</ol>'


def home(lang):
    h = HOME[lang]
    display("".join(h["h1"]), lang)
    if lang == "en":
        h1 = f'<h1 class="ms ms-xl ms-latin hero-title" id="hero-title"><span class="ms-t">{esc(h["h1"][0])}</span></h1>'
    else:
        h1 = ('<h1 class="ms ms-xl hero-title" id="hero-title"><span class="ms-t">'
              + "".join(f'<span class="ln">{esc(line)}</span>' for line in h["h1"]) + "</span></h1>")
    features = ""
    for (title, text), fig in zip(h["features"], feature_figs(lang)):
        display(title, lang)
        features += f'<article class="feature"><div><h3>{title}</h3><p>{text}</p></div>{fig}</article>'
    video = f"/assets/motion/openccman-2-{lang}"
    features_title = heading("h2", h["features_title"], lang, attrs=' id="features-title"')
    film_title = heading("h2", h["film_title"], lang, attrs=' id="film-title"')
    guides_title = heading("h2", h["guides_title"], lang, attrs=' id="guides-title"')
    closing_title = heading("h2", h["closing_title"], lang, cls="ms-xl", attrs=' id="closing-title"',
                            breaks=(h["closing_break"],))
    body = (
        '<section class="wrap hero" aria-labelledby="hero-title"><div class="hero-copy">'
        f'{h1}<p class="lede">{h["intro"]}</p>'
        f'<div class="actions">{stamp(UI[lang]["download"])}<p class="meta platforms">{h["platforms"]}</p></div>'
        f'</div>{proof_desk(lang, list(HOME_SPECIMENS))}</section>'
        '<section class="wrap section" aria-labelledby="features-title">'
        f'{features_title}'
        f'<div class="features-list">{features}</div></section>'
        '<section class="wrap section" aria-labelledby="film-title">'
        f'{film_title}'
        f'<p class="body-copy">{h["film_lead"]}</p>'
        '<div class="film-plate" data-film>'
        f'<video controls preload="none" playsinline width="1600" height="900" poster="{video}.jpg" aria-describedby="film-note">'
        f'<source src="{video}.mp4" type="video/mp4"><a href="{video}.mp4">{h["film_download"]}</a></video>'
        f'<button class="film-play" type="button" hidden aria-label="{h["film_play"]}"><span class="disc">{ring_svg(1, 2)}{PLAY}</span></button>'
        '</div>'
        f'<p class="film-caption meta" id="film-note"><span>{h["film_note"]}</span><span>{h["film_load"]}</span></p>'
        '</section>'
        '<section class="wrap section" aria-labelledby="guides-title">'
        f'{guides_title}'
        f'<p class="body-copy">{h["guides_body"]}</p>'
        f'<div class="toc-block">{toc(lang)}</div>'
        f'<p class="more"><a class="slip-link" href="{page_path(lang, "guides")}"><span>{h["guides_link"]}</span>{LINK_ARROW}</a></p>'
        '</section>'
        '<section class="wrap closing" aria-labelledby="closing-title">'
        f'{closing_title}'
        f'<p class="lede">{h["closing_body"]}</p><div class="actions">{stamp(UI[lang]["download"])}</div>'
        '</section>'
    )
    return document(lang, "home", h["title"], h["description"], body, fonts=serif(lang) + ("hand",), specimens=True,
                    body_class="page-home")


# Guides ------------------------------------------------------------------------------

def cta(lang):
    c = LOCALES[lang]
    display(c["cta_title"], lang)
    return (f'<section class="cta-sheet" aria-labelledby="cta-title"><div><h2 id="cta-title">{c["cta_title"]}</h2>'
            f'<p>{c["cta_body"]}</p></div><div class="actions">{stamp(c["download"])}'
            f'<a href="{page_path(lang, "support")}">{UI[lang]["support"]}</a></div></section>')


def hub(lang):
    c = LOCALES[lang]
    changelog = page_path(lang, "changelog")
    title_html = heading("h1", c["hub_title"], lang, cls="ms-xl", keep_together=(c["label"],))
    if lang != "en":
        hand(c["order_title"])
    scope = note(lang, f'{c["scope"]} <a href="{changelog}">{UI[lang]["changelog"]}</a>')
    body = (
        f'<div class="wrap"><header class="page-head">{title_html}'
        f'<div class="hub-intro"><p class="lede">{c["hub_lede"]}</p>{scope}</div>'
        '</header>'
        '<section class="section" aria-labelledby="start-title">'
        f'<div class="toc-head"><h2 id="start-title">{c["start"]}</h2><span>{c["order_title"]}</span></div>'
        f'{toc(lang, annotated=True)}</section>'
        f'{cta(lang)}</div>'
    )
    return document(lang, "guides", c["hub_title"] + " — OpenCCman", c["hub_description"], body,
                    fonts=serif(lang) + ("hand",))


def preset_table(lang):
    t = PROOF[lang]
    samples = [SPEC_BY_ID["noodle"], SPEC_BY_ID["bed"]]
    definitions = dict(re.findall(r"<dt>(.*?)</dt><dd>(.*?)</dd>", ARTICLES["choose-preset"][lang]["body"]))
    back = SPEC["taiwanToSimplified"]
    display(back["src"], "zh-Hant-TW")
    display(back["out"], "zh-Hans")
    labels = {
        "zh-Hans": ("预设", "说明", "表头是原文，着重号标出每个预设改动的字。简体中文一行把台湾正体结果转回简体：字形变了，用语保持原样。示例均为 OpenCC 1.4.2 实际转换结果。"),
        "zh-Hant": ("預設", "說明", "表頭是原文，著重號標出每個預設改動的字。簡體中文一列把臺灣正體結果轉回簡體：字形變了，用語維持原樣。範例均為 OpenCC 1.4.2 實際轉換結果。"),
        "en": ("Preset", "What it does", "Column headings are the source text; dots mark the characters each preset changes. The Simplified Chinese row converts the Taiwan result back: the characters change, the Taiwan terms stay. All examples are actual OpenCC 1.4.2 output."),
    }[lang]
    head_cells = "".join(f'<th scope="col" lang="zh-Hans">{esc(s["base"])}</th>' for s in samples)
    for s in samples:
        display(s["base"], "zh-Hans")
    rows = []
    for preset in PRESET_ORDER:
        name = t["presets"][preset]
        display(name, lang)
        if preset == "t2s":
            cells = (f'<td class="sample pair" colspan="2"><span lang="zh-Hant-TW">{esc(back["src"])}</span>'
                     f'<span lang="zh-Hans"><span class="via-inline">{NOTE_ARROW}</span>{esc(back["out"])}</span></td>')
        else:
            cells = "".join(f'<td class="sample" lang="{OUT_LANG[preset]}">{emphasised(s["variants"][preset])}</td>'
                            for s in samples)
        rows.append(f'<tr><th scope="row">{name}</th>{cells}<td>{definitions[name]}</td></tr>')
    return (f'<div class="presets-table-wrap"><table class="presets-table"><caption>{labels[2]}</caption>'
            f'<thead><tr><th scope="col">{labels[0]}</th>{head_cells}<th scope="col">{labels[1]}</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div>')


def article(lang, slug):
    c, a = LOCALES[lang], ARTICLES[slug][lang]
    changelog = page_path(lang, "changelog")
    body = re.sub(r'<aside class="guide-note">(.*?)</aside>',
                  lambda m: note(lang, m.group(1)).replace('class="note"', 'class="note guide-note"'),
                  a["body"], flags=re.S)
    if slug == "choose-preset":
        body = re.sub(r'<dl class="guide-definitions">.*?</dl>', lambda m: preset_table(lang), body, flags=re.S)
    for h2 in re.findall(r"<h2>(.*?)</h2>", body):
        display(plain(h2), lang)
    display(c["related"], lang)
    scope = a.get("scope") or f'{c["scope"]} <a href="{changelog}">{UI[lang]["changelog"]}</a>'
    page = (
        '<div class="wrap"><header class="page-head">'
        f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{page_path(lang, "home")}">{c["home"]}</a>{CHEV}'
        f'<a href="{page_path(lang, "guides")}">{c["label"]}</a></nav>'
        f'{heading("h1", a["title"], lang)}<p class="lede">{a["lede"]}</p></header>'
        f'<div class="reading"><aside class="margin">{note(lang, scope)}</aside><div class="prose">{body}</div></div>'
        f'<section class="related" aria-labelledby="related-title"><h2 id="related-title">{c["related"]}</h2>'
        f'{toc(lang, exclude=slug)}'
        f'<p class="more"><a class="slip-link" href="{page_path(lang, "guides")}"><span>{c["back"]}</span>{LINK_ARROW}</a></p></section>'
        f'{cta(lang)}</div>'
    )
    return document(lang, f"guide:{slug}", a["title"] + " — OpenCCman", a["description"], page)


# Changelog, support, privacy ------------------------------------------------------------

def changelog(lang):
    c = CHANGELOG[lang]
    entries = []
    for release in c["releases"]:
        digits = "".join(f"<span>{esc(ch)}</span>" for ch in release["version"])
        badge = (f'<p class="status">{TRI}{release["status"]}</p>' if "status" in release
                 else f'<p class="status done">{CHECK}{release["date"]}</p>')
        groups = ""
        for label, items in release["groups"]:
            display(label, lang)
            groups += f'<div><h3>{label}</h3><ul class="ticks">{"".join(f"<li>{i}</li>" for i in items)}</ul></div>'
        release_note = note(lang, release["note"]) if "note" in release else ""
        entries.append(
            f'<section class="release" aria-labelledby="{release["id"]}"><div class="release-no">'
            f'<h2 class="ms ms-l digits" id="{release["id"]}" aria-label="{release["version"]}">{digits}</h2>{badge}</div>'
            f'<div class="release-body">{release_note}{groups}</div></section>')
    history = c["history"]
    history_title = heading("h2", history["title"], lang, cls="ms-s", attrs=f' id="{history["id"]}"')
    entries.append(
        f'<section class="release" aria-labelledby="{history["id"]}"><div class="release-no">{history_title}'
        f'<p class="meta">{history["range"]}</p></div><div class="release-body"><div>'
        f'<ul class="ticks">{"".join(f"<li>{i}</li>" for i in history["items"])}</ul><p>{history["link"]}</p></div></div></section>')
    body = (f'<div class="wrap"><header class="page-head">{heading("h1", c["title"], lang, cls="ms-xl")}'
            f'<p class="lede">{c["intro"]}</p></header>{"".join(entries)}</div>')
    return document(lang, "changelog", c["title"] + " — OpenCCman", c["description"], body)


def support(lang):
    s = SUPPORT[lang]
    items = "".join(f"<li><span>{item}</span><i></i></li>" for item in s["details"])
    restore_title = heading("h2", s["restore_title"], lang, attrs=' id="restore-title"')
    body = (
        f'<div class="wrap"><header class="page-head">{heading("h1", s["title"], lang, cls="ms-xl")}'
        f'<p class="lede">{s["intro"]}</p></header>'
        '<div class="support-grid"><div class="support-main">'
        f'<div class="actions">{stamp(s["email_label"], "mailto:" + s["email"])}<p class="meta">{s["email"]}</p></div>'
        '<section class="section-tight" aria-labelledby="restore-title">'
        f'{restore_title}'
        f'<p class="body-copy">{s["restore_body"]}</p>'
        f'<p class="links"><a href="{s["refund_url"]}">{s["refund_label"]}</a><a href="{page_path(lang, "privacy")}">{UI[lang]["privacy"]}</a></p>'
        '</section></div>'
        f'<aside class="form-slip" aria-labelledby="slip-title"><p id="slip-title">{s["details_lead"]}</p><ol>{items}</ol>'
        f'<p class="warn">{WARN}<span>{s["warning"]}</span></p></aside>'
        '</div></div>'
    )
    return document(lang, "support", s["title"] + " — OpenCCman", s["description"], body)


def privacy(lang):
    p = PRIVACY[lang]
    rows = ""
    for gloss, paragraph in p["sections"]:
        hand(gloss)
        rows += f'<div class="gloss-row"><h2 class="gloss">{gloss}</h2><p>{paragraph}</p></div>'
    body = (
        f'<div class="wrap"><header class="page-head">{heading("h1", p["title"], lang, cls="ms-xl")}'
        f'<p class="meta">{p["updated"]}</p></header><div class="glossed">{rows}</div>'
        f'<p class="more"><a class="slip-link" href="{page_path(lang, "home")}"><span>{p["back"]}</span>{LINK_ARROW}</a></p></div>'
    )
    return document(lang, "privacy", p["title"] + " — OpenCCman", p["description"], body, fonts=serif(lang) + ("hand",))


# 404 and language chooser -----------------------------------------------------------------

def not_found():
    n = NOT_FOUND
    lines = "".join(f'<p class="lede" lang="{lang}">{text}</p>' for lang, text in n["lines"])
    links = "".join(
        f'<a class="slip-link" href="{href}" lang="{lang}"><span>{label}</span>{LINK_ARROW}</a>' for lang, href, label in n["links"])
    return (
        f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
        f'<title>{n["title"]}</title><meta name="theme-color" content="#f7f9f6">'
        '<link rel="icon" href="/assets/icon.png"><link rel="stylesheet" href="/assets/style.css"></head>'
        '<body class="page-404"><main id="main" class="wrap missing">'
        f'<div class="missing-row" aria-hidden="true"><p class="ms ms-xl"><span class="ms-t">&#8203;</span></p>{CARET}</div>'
        f'<h1 class="missing-title">{n["heading"]}</h1>{lines}<p class="actions">{links}</p>'
        '</main></body></html>\n'
    )


def chooser():
    cells = ""
    for code, glyph, name in LANG_CELLS:
        display(glyph, code)
        cells += (f'<li><a href="/{code}/" lang="{code}" hreflang="{code}"><span class="big">{glyph}</span>'
                  f'<span>{name}</span></a></li>')
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>{ROOT["title"]}</title><meta name="theme-color" content="#f7f9f6">'
        '<link rel="icon" href="/assets/icon.png"><link rel="stylesheet" href="/assets/style.css"></head>'
        '<body class="page-chooser"><main id="main" class="wrap chooser">'
        '<h1 class="brand"><img src="/assets/icon.png" width="40" height="40" alt="">OpenCCman</h1>'
        f'<p class="chooser-prompt">{ROOT["prompt"]}</p><ul class="lang-cells">{cells}</ul>'
        '</main><script src="/assets/language.js"></script></body></html>\n'
    )


# Build -----------------------------------------------------------------------------------

def specimens_js():
    data = {"engine": SPEC["engine"], "maxRing": 5, "rings": RINGS, "keep": KEEP, "outLang": OUT_LANG,
            "i18n": PROOF, "specimens": SPEC["specimens"]}
    return "window.OCCMAN = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n"


def pages():
    for key in GLYPHS:
        GLYPHS[key].clear()
    rendered = {}
    for lang in LANGUAGES:
        rendered[SITE / lang / "index.html"] = home(lang)
        rendered[SITE / lang / "guides" / "index.html"] = hub(lang)
        for slug in ARTICLES:
            rendered[SITE / lang / "guides" / f"{slug}.html"] = article(lang, slug)
        rendered[SITE / lang / "changelog.html"] = changelog(lang)
        rendered[SITE / lang / "support.html"] = support(lang)
        rendered[SITE / lang / "privacy.html"] = privacy(lang)
    rendered[SITE / "404.html"] = not_found()
    rendered[SITE / "index.html"] = chooser()
    rendered[SITE / "assets" / "specimens.js"] = specimens_js()
    paths = [f"/{lang}/{page}" for lang in LANGUAGES for page in (
        "", "privacy", "support", "changelog", "guides/", *(f"guides/{slug}" for slug in ARTICLES))]
    rendered[SITE / "sitemap.xml"] = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{ORIGIN}{path}</loc></url>\n" for path in paths)
        + "</urlset>\n"
    )
    rendered[SITE / "robots.txt"] = f"User-agent: *\nAllow: /\nSitemap: {ORIGIN}/sitemap.xml\n"
    glyphs = {key: "".join(sorted(ch for ch in chars if not ch.isspace())) for key, chars in GLYPHS.items()}
    rendered[SCRIPTS / "font_glyphs.json"] = json.dumps(glyphs, ensure_ascii=False, indent=1) + "\n"
    return rendered


def run(check=False):
    for path, content in pages().items():
        if check:
            assert path.exists() and path.read_text(encoding="utf-8") == content, \
                f"Outdated build output: {path.relative_to(SCRIPTS.parent)}; run scripts/build_site.py"
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--check", action="store_true")
    run(check=parser.parse_args().check)
