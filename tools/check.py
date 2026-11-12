#!/usr/bin/env python3
"""Rule and SEO checks over the built site in dist/ (CLAUDE.md "Before you finish").

Checks every page for: title, exactly one H1, canonical on https://kidstorybooks.com/, meta description,
Open Graph tags, valid single JSON-LD block, FAQ block + FAQPage JSON-LD (3 to 6, same count),
every <img> has width/height/alt, no broken internal links, Amazon links (dp/ASIN, new tab, noopener),
social icons with aria-labels in header and footer, EN/ES toggle, footer quote and disclaimer, the
handwritten marker, banned phrases, em/en dashes, and that every ASIN in data/books.json is on /books/.

Usage: python3 tools/check.py [--dist DIR]     Exit code 1 if any error.
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORIGIN = "https://kidstorybooks.com"
SITE = json.loads((ROOT / "src" / "data" / "site.json").read_text())
QUOTE = SITE["footer_quote"]
CREDIT_LINE = f'{QUOTE["text"]} {QUOTE["credit"]}'
BANNED = [r"your trusted partner", r"one-stop", r"look no further", r"\bunmatched\b", r"cutting-edge",
          r"elevate your", r"in today's world", r"\bdelve", r"\btapestry", r"\bembark", r"testimonial",
          r"5-star", r"five[- ]star", r"#1\b", r"guarantee", r"best-selling", r"bestselling", r"lorem",
          r"\bTODO\b", r"award-winning", r"\bcolour", r"\bfavourite", r"\bpersonalis"]
NO_FAQ = {"/privacy-policy/", "/404.html"}


class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.text, self.skip, self.h1, self.title, self._t = [], 0, 0, "", False
        self.meta, self.links, self.imgs, self.ids, self.canonical = {}, [], [], [], None
        self.jsonld, self._ld, self._in_ld = [], "", False
        self.headings, self._h = [], None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag in ("script", "style"):
            self.skip += 1
            if a.get("type") == "application/ld+json":
                self._in_ld, self._ld = True, ""
        if tag == "title":
            self._t = True
        if tag == "h1":
            self.h1 += 1
        if tag in ("h1", "h2", "h3"):
            self._h = [tag, ""]
        if tag == "meta" and (a.get("name") or a.get("property")):
            self.meta[a.get("name") or a.get("property")] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        if tag == "a":
            self.links.append(a)
        if tag == "img":
            self.imgs.append(a)

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
            if self._in_ld:
                self.jsonld.append(self._ld)
                self._in_ld = False
        if tag == "title":
            self._t = False
        if self._h and tag == self._h[0]:
            self.headings.append(tuple(self._h))
            self._h = None

    def handle_data(self, data):
        if self._in_ld:
            self._ld += data
        if self._t:
            self.title += data
        if self._h:
            self._h[1] += data
        if not self.skip:
            self.text.append(data)


def url_of(path, dist):
    rel = path.relative_to(dist).as_posix()
    if rel == "index.html":
        return "/"
    if rel == "404.html":
        return "/404.html"
    return "/" + rel[: -len("index.html")]


def resolve(href, dist):
    href = href.split("#")[0].split("?")[0]
    if not href:
        return True
    if href.startswith(ORIGIN):
        href = href[len(ORIGIN):] or "/"
    p = dist / href.lstrip("/")
    return (p / "index.html").exists() if href.endswith("/") else p.exists()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    dist = Path(ap.parse_args().dist).resolve()
    errors, warnings = [], []
    titles, descs = defaultdict(list), defaultdict(list)
    files = sorted(dist.rglob("*.html"))
    sitemap = (dist / "sitemap.xml").read_text()
    for f in files:
        url = url_of(f, dist)
        raw = f.read_text()
        p = Parser()
        p.feed(raw)
        text = re.sub(r"\s+", " ", " ".join(p.text))
        err = lambda m: errors.append(f"{url}: {m}")
        warn = lambda m: warnings.append(f"{url}: {m}")
        noindex = 'name="robots" content="noindex' in raw

        # copy rules on visible text + title + description
        visible = text + " " + p.title + " " + p.meta.get("description", "")
        for pat in BANNED:
            for mt in re.finditer(pat, visible, re.I):
                err(f"banned phrase /{pat}/: ...{visible[max(0, mt.start()-50):mt.end()+50]}...")
        for mt in re.finditer("[—–]", visible.replace(QUOTE["credit"], "")):
            err(f"em/en dash: ...{visible[max(0, mt.start()-40):mt.end()+40]}...")
        if "dwdp:handwritten 2026-11-12" not in raw[:4096]:
            err("handwritten marker missing from first 4KB")
        if unescape(CREDIT_LINE) not in text or QUOTE["disclaimer"] not in text:
            err("footer quote or disclaimer missing or altered")
        if text.count("Duplantis") < 3:
            err("Duplantis credit incomplete")
        # SEO basics
        if p.h1 != 1:
            err(f"expected one h1, found {p.h1}")
        if not p.title.strip():
            err("missing title")
        if len(p.title) > 65:
            warn(f"title {len(p.title)} chars: {p.title}")
        d = p.meta.get("description", "")
        if not d:
            err("missing meta description")
        elif not 110 <= len(d) <= 165:
            warn(f"description {len(d)} chars")
        titles[p.title].append(url)
        descs[d].append(url)
        if url != "/404.html":
            if p.canonical != ORIGIN + url:
                err(f"canonical {p.canonical} != {ORIGIN + url}")
            if f"<loc>{ORIGIN}{url}</loc>" not in sitemap:
                err("missing from sitemap.xml")
        elif not noindex:
            err("404 page must be noindex")
        for k in ("og:title", "og:description", "og:url", "og:image"):
            if not p.meta.get(k, "").strip():
                err(f"missing {k}")
        if not p.meta.get("og:image", "").startswith("https://"):
            err("og:image not absolute https")
        # JSON-LD
        if len(p.jsonld) != 1:
            err(f"expected one JSON-LD block, found {len(p.jsonld)}")
        faq_ld = 0
        for block in p.jsonld:
            try:
                data = json.loads(block)
            except json.JSONDecodeError as e:
                err(f"invalid JSON-LD: {e}")
                continue
            types = [g.get("@type") for g in data.get("@graph", [])]
            if len(types) != len(set(types)):
                err(f"duplicate JSON-LD types {types}")
            if re.search(r'"(AggregateRating|Review)"', block):
                err("Review/AggregateRating schema is not allowed")
            for g in data.get("@graph", []):
                if g.get("@type") == "FAQPage":
                    faq_ld = len(g["mainEntity"])
        faq_vis = raw.count('class="faq__item"')
        if faq_vis != faq_ld:
            err(f"visible FAQs ({faq_vis}) != FAQPage entries ({faq_ld})")
        if url not in NO_FAQ and not 3 <= faq_vis <= 6:
            err(f"needs 3 to 6 FAQs, has {faq_vis}")
        # headings order
        last = 1
        for tag, label in p.headings:
            lvl = int(tag[1])
            if lvl > last + 1:
                warn(f"heading jumps h{last} -> {tag}: {label.strip()[:50]}")
            last = lvl
        # links
        for a in p.links:
            href = (a.get("href") or "").strip()
            if href in ("", "#"):
                err("empty href")
                continue
            if href.startswith("https://www.amazon.com/"):
                if not re.fullmatch(r"https://www\.amazon\.com/(dp/[A-Z0-9]{10}|author/dominionpublishing|privacy)", href):
                    err(f"unexpected Amazon URL {href}")
                if a.get("target") != "_blank" or "noopener" not in (a.get("rel") or ""):
                    err(f"Amazon link without target=_blank rel=noopener: {href}")
                continue
            if href.startswith(("http://", "https://", "mailto:", "tel:")) and not href.startswith(ORIGIN):
                if href.startswith(("mailto:", "tel:")):
                    err(f"contact link not allowed (UNKNOWN in INTAKE): {href}")
                continue
            if not resolve(href, dist):
                err(f"broken internal link {href}")
        # images
        for im in p.imgs:
            src = im.get("src", "")
            if im.get("alt") is None:
                err(f"img missing alt: {src}")
            if not im.get("width") or not im.get("height"):
                err(f"img missing width/height: {src}")
            if src.startswith("/") and not (dist / src.lstrip("/")).exists():
                err(f"missing image file {src}")
        dup = {i for i in p.ids if p.ids.count(i) > 1}
        if dup:
            err(f"duplicate ids {sorted(dup)}")
        # header/footer furniture
        head = raw.split('<header class="site-header">', 1)[-1].split("</header>", 1)[0]
        foot = raw.split('<footer class="site-footer">', 1)[-1].split("</footer>", 1)[0]
        for name in ("Facebook", "Instagram", "TikTok"):
            for where, chunk in (("header", head), ("footer", foot)):
                if f'aria-label="Kid Story Books on {name}' not in chunk or "<svg" not in chunk:
                    err(f"{name} icon missing in {where}")
        if 'data-lang="es"' not in head:
            err("EN/ES toggle missing from header")
        if "Kid Story Books</span>" not in head:
            err("logo text missing")

    for t, urls in titles.items():
        if len(urls) > 1:
            errors.append(f"duplicate title on {urls}")
    for d, urls in descs.items():
        if len(urls) > 1:
            errors.append(f"duplicate description on {urls}")
    # every ASIN on /books/
    books = json.loads((ROOT / "data" / "books.json").read_text())
    cat = (dist / "books" / "index.html").read_text()
    missing = [b["asin"] for b in books if f"/dp/{b['asin']}\"" not in cat]
    if missing:
        errors.append(f"/books/: {len(missing)} ASINs missing: {missing[:10]}")
    if cat.count('class="book"') != len(books):
        errors.append(f"/books/: {cat.count('class=\"book\"')} book cards, expected {len(books)}")
    # sitemap / robots / redirects
    if "Sitemap: https://kidstorybooks.com/sitemap.xml" not in (dist / "robots.txt").read_text():
        errors.append("robots.txt missing sitemap line")
    if "/404.html" in sitemap:
        errors.append("404 listed in sitemap")
    red = (dist / "_redirects").read_text()
    if "/privacy-policy.html  /privacy-policy/  301" not in red:
        errors.append("_redirects: /privacy-policy.html -> /privacy-policy/ missing")
    for line in red.splitlines():
        parts = line.split()
        if parts and not parts[0].startswith("#") and not resolve(parts[1], dist):
            errors.append(f"_redirects target missing: {line}")
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\n{len(files)} pages checked, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
