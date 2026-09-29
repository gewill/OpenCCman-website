"""Render the reviewed guide copy as dependency-free static HTML."""

from argparse import ArgumentParser
from html import escape
from pathlib import Path

from guide_content import ARTICLES, LOCALES

SITE = Path(__file__).resolve().parent.parent / "site"
ORIGIN = "https://openccman.gewill.org"
LANGUAGES = ("zh-Hans", "zh-Hant", "en")


def head(lang: str, path: str, title: str, description: str) -> str:
    canonical_path = path.removesuffix(".html")
    alternates = "".join(
        f'<link rel="alternate" hreflang="{other}" href="{ORIGIN}/{other}/{canonical_path}">'
        for other in LANGUAGES
    )
    return (
        f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f'<title>{escape(title)} — OpenCCman</title>'
        f'<meta name="description" content="{escape(description, quote=True)}">'
        '<meta name="theme-color" content="#f5f7fa">'
        '<link rel="icon" href="/assets/icon.png">'
        '<link rel="stylesheet" href="/assets/style.css">'
        f'<link rel="canonical" href="{ORIGIN}/{lang}/{canonical_path}">'
        f'{alternates}</head>'
    )


def shell(lang: str, path: str, title: str, description: str, body: str) -> str:
    copy = LOCALES[lang]
    is_hub = path == "guides/"
    hub_current = ' aria-current="page"' if is_hub else ""
    nav = (
        f'<a href="/{lang}/guides/"{hub_current}>{copy["label"]}</a>'
        f'<a href="/{lang}/changelog.html">{copy["changelog"]}</a>'
        f'<a href="/{lang}/support.html">{copy["support"]}</a>'
        f'<a href="/{lang}/privacy.html">{copy["privacy"]}</a>'
    )
    languages = ""
    for other in LANGUAGES:
        current = ' aria-current="page"' if other == lang else ""
        label = {"zh-Hans": "简体", "zh-Hant": "繁體", "en": "English"}[other]
        languages += f'<a href="/{other}/{path}" lang="{other}" hreflang="{other}"{current}>{label}</a>'
    return (
        head(lang, path, title, description)
        + '<body>'
        + f'<a class="skip" href="#main">{copy["skip"]}</a>'
        + f'<header><a class="brand" href="/{lang}/"><img src="/assets/icon.png" width="36" height="36" alt="">OpenCCman</a>'
        + f'<nav aria-label="{copy["label"]}">{nav}</nav>'
        + f'<nav class="languages" aria-label="{copy["language"]}">{languages}</nav></header>'
        + f'<main id="main">{body}</main>'
        + f'<footer><span>© 2026 OpenCCman</span><a href="/{lang}/guides/">{copy["label"]}</a>'
        + f'<a href="/{lang}/changelog.html">{copy["changelog"]}</a>'
        + f'<a href="/{lang}/privacy.html">{copy["privacy"]}</a>'
        + f'<a href="/{lang}/support.html">{copy["support"]}</a>'
        + '<a href="https://github.com/BYVoid/OpenCC">OpenCC</a></footer></body></html>\n'
    )


def hub(lang: str) -> str:
    copy = LOCALES[lang]
    cards = "".join(
        f'<a class="guide-card" href="/{lang}/guides/{slug}.html"><h3>{article[lang]["card"]}</h3>'
        f'<p>{article[lang]["summary"]}</p><span>{copy["read"]}</span></a>'
        for slug, article in ARTICLES.items()
    )
    order = "".join(f"<li>{item}</li>" for item in copy["order"])
    body = (
        '<article class="guide-page guide-hub">'
        f'<div class="guide-heading"><p class="eyebrow">OpenCCman · {copy["label"]}</p>'
        f'<h1>{copy["hub_title"]}</h1><p class="intro">{copy["hub_lede"]}</p></div>'
        f'<section><h2>{copy["start"]}</h2><div class="guide-grid">{cards}</div></section>'
        f'<section class="guide-order"><h2>{copy["order_title"]}</h2><ol>{order}</ol></section>'
        f'<p class="guide-scope">{copy["scope"]} <a href="/{lang}/changelog.html">{copy["changelog"]}</a></p>'
        f'{cta(lang)}</article>'
    )
    return shell(lang, "guides/", copy["hub_title"], copy["hub_description"], body)


def cta(lang: str) -> str:
    copy = LOCALES[lang]
    return (
        '<section class="guide-cta">'
        f'<h2>{copy["cta_title"]}</h2><p>{copy["cta_body"]}</p>'
        f'<a class="button" href="https://apps.apple.com/app/id6474449401">{copy["download"]}</a>'
        f'<a class="guide-support-link" href="/{lang}/support.html">{copy["support"]}</a>'
        '</section>'
    )


def article_page(lang: str, slug: str) -> str:
    copy = LOCALES[lang]
    article = ARTICLES[slug][lang]
    scope = (
        f'<p class="guide-scope">{article["scope"]}</p>'
        if "scope" in article
        else f'<p class="guide-scope">{copy["scope"]} <a href="/{lang}/changelog.html">{copy["changelog"]}</a></p>'
    )
    related = "".join(
        f'<li><a href="/{lang}/guides/{other_slug}.html">{other[lang]["card"]}</a></li>'
        for other_slug, other in ARTICLES.items() if other_slug != slug
    )
    body = (
        '<article class="guide-page guide-article">'
        f'<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/{lang}/">{copy["home"]}</a>'
        f' <span aria-hidden="true">/</span> <a href="/{lang}/guides/">{copy["label"]}</a></nav>'
        f'<div class="guide-heading"><p class="eyebrow">OpenCCman · {copy["label"]}</p>'
        f'<h1>{article["title"]}</h1><p class="intro">{article["lede"]}</p></div>'
        f'{scope}'
        f'<div class="guide-prose">{article["body"]}</div>'
        f'<section class="guide-related"><h2>{copy["related"]}</h2><ul>{related}</ul>'
        f'<p><a href="/{lang}/guides/">← {copy["back"]}</a></p></section>'
        f'{cta(lang)}</article>'
    )
    return shell(lang, f"guides/{slug}.html", article["title"], article["description"], body)


def pages() -> dict[Path, str]:
    rendered = {}
    for lang in LANGUAGES:
        directory = SITE / lang / "guides"
        rendered[directory / "index.html"] = hub(lang)
        for slug in ARTICLES:
            rendered[directory / f"{slug}.html"] = article_page(lang, slug)
    paths = [f"/{lang}/{page}" for lang in LANGUAGES for page in (
        "", "privacy", "support", "changelog", "guides/",
        *(f"guides/{slug}" for slug in ARTICLES),
    )]
    rendered[SITE / "sitemap.xml"] = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{ORIGIN}{path}</loc></url>\n" for path in paths)
        + "</urlset>\n"
    )
    rendered[SITE / "robots.txt"] = f"User-agent: *\nAllow: /\nSitemap: {ORIGIN}/sitemap.xml\n"
    return rendered


def run(check: bool = False) -> None:
    for path, content in pages().items():
        if check:
            assert path.exists() and path.read_text() == content, f"Outdated guide output: {path}"
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--check", action="store_true")
    run(check=parser.parse_args().check)
