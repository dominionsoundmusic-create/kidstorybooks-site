#!/usr/bin/env python3
"""Build the static Kid Story Books site.

Pages live in src/pages as Jinja templates with a YAML front matter block.
Shared data: src/data/site.json (business, nav, social) and data/books.json (all 220 books).
Output goes to dist/ (committed; Netlify publishes it as-is, no build command).

Usage:
  python3 build.py              # full build to dist/, also writes docs/image-list.md
  python3 build.py --out DIR    # build somewhere else (no docs written)
"""
import argparse
import html
import json
import re
import shutil
import struct
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined, pass_context
from markupsafe import Markup

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
PAGES = SRC / "pages"
STATIC = SRC / "static"
IMAGES = STATIC / "images"
WEBP_DIR = IMAGES / "w"
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
BUILD_DATE = "2026-11-12"
WEBP_WIDTHS = (480, 800, 1200, 1600, 1920)


# ---------------------------------------------------------------- helpers
def image_size(path):
    """(width, height) of a JPEG/PNG/WebP file, or None."""
    data = path.read_bytes()
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", data[16:24])
    if data[:2] == b"\xff\xd8":
        i = 2
        while i < len(data):
            marker = data[i + 1]
            length = struct.unpack(">H", data[i + 2:i + 4])[0]
            if marker in (0xC0, 0xC1, 0xC2):
                h, w = struct.unpack(">HH", data[i + 5:i + 9])
                return w, h
            i += 2 + length
    return None


_webp_cache = {}


def webp_srcset(file):
    """Speed fix: every local photo also ships as WebP at 480/800/1200/1600/1920 wide."""
    if not file or file in _webp_cache:
        return _webp_cache.get(file, "")
    src = IMAGES / file
    if not src.exists() or src.suffix.lower() not in (".jpg", ".jpeg", ".png"):
        _webp_cache[file] = ""
        return ""
    from PIL import Image
    WEBP_DIR.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as im:
        full_w, full_h = im.size
        widths = sorted({w for w in WEBP_WIDTHS if w < full_w} | {full_w})
        parts = []
        for w in widths:
            name = f"{src.stem}-{w}.webp"
            dest = WEBP_DIR / name
            if not dest.exists() or dest.stat().st_mtime < src.stat().st_mtime:
                h = round(full_h * w / full_w)
                im.convert("RGB").resize((w, h), Image.LANCZOS).save(dest, "WEBP", quality=68, method=6)
            parts.append(f"/images/w/{name} {w}w")
    _webp_cache[file] = ", ".join(parts)
    return _webp_cache[file]


def url_for_source(rel):
    parts = list(rel.with_suffix("").parts)
    if parts == ["index"]:
        return "/"
    if parts == ["404"]:
        return "/404.html"
    if parts[-1] == "index":
        parts = parts[:-1]
    return "/" + "/".join(parts) + "/"


def out_path_for(url, out):
    if url == "/":
        return out / "index.html"
    if url == "/404.html":
        return out / "404.html"
    return out / url.strip("/") / "index.html"


def strip_tags(text):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", str(text)))).strip()


def minify_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};:,>])\s*", r"\1", css)
    return css.replace(";}", "}").strip()


# ---------------------------------------------------------------- builder
class Builder:
    def __init__(self, out, write_docs):
        self.out = out
        self.write_docs = write_docs
        self.site = json.loads((SRC / "data" / "site.json").read_text())
        self.books = json.loads((ROOT / "data" / "books.json").read_text())
        self.by_asin = {b["asin"]: b for b in self.books}
        self.cat = {c["key"]: c for c in self.site["categories"]}
        self.missing_images = {}
        self.css = minify_css((SRC / "templates" / "site.css").read_text())
        self.env = Environment(
            loader=FileSystemLoader([str(SRC / "templates"), str(PAGES)]),
            undefined=StrictUndefined,
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.env.globals.update(
            site=self.site,
            biz=self.site["business"],
            all_books=self.books,
            book=self.book,
            books=self.pick,
            cat=self.cat,
            photo=self.photo,
            webp_srcset=webp_srcset,
            inline_css=Markup(self.css),
            count=lambda key: sum(1 for b in self.books if b["category"] == key),
        )
        self.env.filters["plain"] = strip_tags
        self.env.filters["tojson_ld"] = lambda v: Markup(
            json.dumps(v, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
        self.env.filters["attr"] = lambda v: html.escape(str(v), quote=True)

    # ---- book data ----------------------------------------------------
    def book(self, asin):
        if asin not in self.by_asin:
            raise KeyError(f"unknown ASIN {asin}")
        return self.by_asin[asin]

    def pick(self, asins=None, category=None, limit=None):
        if asins:
            out = [self.book(a) for a in asins]
        else:
            out = [b for b in self.books if category is None or b["category"] == category]
        return out[:limit] if limit else out

    # ---- images -------------------------------------------------------
    @pass_context
    def photo(self, ctx, file, alt, desc, asins, size="1200x800"):
        """An in-body photo. Until the file exists, a cover collage stands in (never a broken image)."""
        page = ctx.get("page", {})
        w, h = (int(x) for x in size.split("x"))
        if (IMAGES / file).exists():
            real = image_size(IMAGES / file) or (w, h)
            tag = (f'<img src="/images/{file}" alt="{html.escape(alt, quote=True)}" width="{real[0]}" '
                   f'height="{real[1]}" loading="lazy" decoding="async">')
            srcset = webp_srcset(file)
            if srcset:
                tag = (f'<picture><source type="image/webp" srcset="{srcset}" '
                       f'sizes="(max-width: 800px) 100vw, 50vw">{tag}</picture>')
            return Markup(f'<figure class="photo">{tag}</figure>')
        entry = self.missing_images.setdefault(file, {"file": file, "size": size, "alt": alt,
                                                      "desc": desc, "pages": []})
        if page.get("url") not in entry["pages"]:
            entry["pages"].append(page.get("url", "?"))
        tpl = self.env.get_template("macros.html").make_module({"page": page})
        return Markup(tpl.collage(asins, alt, "collage--photo"))

    # ---- pages --------------------------------------------------------
    def load_pages(self):
        pages = []
        for path in sorted(PAGES.rglob("*.html")):
            rel = path.relative_to(PAGES)
            if rel.name.startswith("_"):
                continue
            text = path.read_text()
            m = FM_RE.match(text)
            if not m:
                raise SystemExit(f"{rel}: missing front matter")
            meta = yaml.safe_load(m.group(1)) or {}
            meta["url"] = url_for_source(rel)
            meta["source"] = str(rel)
            meta["body"] = text[m.end():]
            meta.setdefault("faqs", [])
            meta.setdefault("sources", [])
            meta.setdefault("shelf", [])
            meta.setdefault("noindex", False)
            meta.setdefault("type", "page")
            pages.append(meta)
        return pages

    def breadcrumbs(self, page):
        if page["url"] in ("/", "/404.html"):
            return []
        return [{"label": "Home", "href": "/"},
                {"label": page.get("crumb", page["h1"]), "href": page["url"]}]

    def jsonld(self, page):
        b = self.site["business"]
        origin = b["origin"]
        url = origin + page["url"]
        org_id = origin + "/#organization"
        org = {
            "@type": "Organization", "@id": org_id, "name": b["name"], "url": origin + "/",
            "logo": origin + "/apple-touch-icon.png", "description": b["description"],
            "founder": {"@type": "Person", "name": b["author"]},
            "parentOrganization": {"@type": "Organization", "name": b["parent"]},
            "sameAs": [s["url"] for s in self.site["social"]] + [b["amazon_author"]],
        }
        graph = [org]
        if page["url"] == "/":
            graph.append({"@type": "WebSite", "@id": origin + "/#website", "url": origin + "/",
                          "name": b["name"], "publisher": {"@id": org_id}, "inLanguage": "en-US"})
        if page["url"] == "/404.html":
            return {"@context": "https://schema.org", "@graph": graph}
        webpage = {"@type": {"about": "AboutPage", "books": "CollectionPage"}.get(page["type"], "WebPage"),
                   "@id": url + "#webpage", "url": url, "name": page["title"],
                   "description": page["description"], "inLanguage": "en-US",
                   "isPartOf": {"@id": origin + "/#website"}, "publisher": {"@id": org_id}}
        graph.append(webpage)
        crumbs = page["breadcrumbs"]
        if crumbs:
            graph.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": c["label"], "item": origin + c["href"]}
                for i, c in enumerate(crumbs)]})
            webpage["breadcrumb"] = {"@id": url + "#breadcrumb"}
        shelf = page.get("shelf_books") or []
        if shelf and page["type"] != "books":
            graph.append({"@type": "ItemList", "@id": url + "#books", "name": page.get("shelf_title", "Books"),
                          "itemListElement": [
                              {"@type": "ListItem", "position": i + 1, "item": {
                                  "@type": "Book", "name": bk["title"],
                                  "author": {"@type": "Person", "name": b["author"]},
                                  "publisher": {"@type": "Organization", "name": b["publisher"]},
                                  "url": b["amazon_dp"] + bk["asin"],
                                  "image": b["cover_url"] + bk["asin"] + ".jpg"}}
                              for i, bk in enumerate(shelf)]})
        if page["faqs"]:
            graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
                {"@type": "Question", "name": strip_tags(f["q"]),
                 "acceptedAnswer": {"@type": "Answer", "text": strip_tags(f["a"])}}
                for f in page["faqs"]]})
        return {"@context": "https://schema.org", "@graph": graph}

    def render(self, page, index):
        sel = page.get("shelf")
        if isinstance(sel, dict):
            page["shelf_books"] = self.pick(category=sel.get("category"), limit=sel.get("limit"))
        else:
            page["shelf_books"] = self.pick(asins=sel) if sel else []
        if page["type"] == "home":
            page["shelf_books"] = self.pick(asins=page["featured"])
        page["breadcrumbs"] = self.breadcrumbs(page)
        page["jsonld"] = self.jsonld(page)
        layout = page.get("layout", "page")
        source = ('{% extends "layouts/' + layout + '.html" %}\n'
                  '{% import "macros.html" as m with context %}\n' + page["body"])
        return self.env.from_string(source).render(page=page, pages=index)

    def build(self):
        if self.out.exists():
            shutil.rmtree(self.out)
        shutil.copytree(STATIC, self.out)
        pages = self.load_pages()
        index = {p["url"]: p for p in pages}
        for page in pages:
            out_html = self.render(page, index)
            dest = out_path_for(page["url"], self.out)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(out_html)
        if WEBP_DIR.exists():
            shutil.copytree(WEBP_DIR, self.out / "images" / "w", dirs_exist_ok=True)
        self.write_sitemap(pages)
        self.write_robots()
        if self.write_docs:
            self.write_image_list()
        print(f"Built {len(pages)} pages into {self.out}")
        if self.missing_images:
            print(f"{len(self.missing_images)} new photos listed in docs/image-list.md (cover collages stand in)")

    def write_sitemap(self, pages):
        origin = self.site["business"]["origin"]
        urls = sorted((p["url"] for p in pages if not p["noindex"] and p["url"] != "/404.html"),
                      key=lambda u: (u != "/", u))
        lines = ['<?xml version="1.0" encoding="UTF-8"?>',
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        lines += [f"  <url><loc>{origin}{u}</loc><lastmod>{BUILD_DATE}</lastmod></url>" for u in urls]
        lines.append("</urlset>")
        (self.out / "sitemap.xml").write_text("\n".join(lines) + "\n")

    def write_robots(self):
        origin = self.site["business"]["origin"]
        (self.out / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {origin}/sitemap.xml\n")

    def write_image_list(self):
        rows = sorted(self.missing_images.values(), key=lambda e: (e["size"] != "1920x1080", e["file"]))
        out = [
            "# New photos to make in Artistly",
            "",
            "Generated by build.py. Each photo already has its place in a page. Until the file exists in",
            "src/static/images/, the page shows a collage of real book covers there instead, so nothing",
            "looks broken. Save each one under the exact file name and size, run `python3 build.py`, and",
            "it appears (with WebP copies at 480/800/1200/1600/1920 wide made automatically).",
            "",
            "Heroes: none needed. Every hero uses a collage of real covers, so all photos are in-body.",
            "",
            f"Total: {len(rows)} photos.",
            "",
            "| # | File name | Size | Page(s) |",
            "|---|---|---|---|",
        ]
        for n, e in enumerate(rows, 1):
            kind = "hero" if e["size"] == "1920x1080" else "in-body"
            out.append(f"| {n} | {e['file']} | {e['size']} {kind} | {', '.join(e['pages'])} |")
        out.append("")
        for n, e in enumerate(rows, 1):
            out += [f"## {n}. {e['file']}", "", f"- Size: {e['size']} px", f"- Alt text: {e['alt']}", "",
                    "Artistly prompt: " + e["desc"] + " Bright, cheerful, clearly visible, children's books, "
                    "no text, no logos, no recognizable faces, subject positioned on right third of frame, "
                    "well lit.", ""]
        (ROOT / "docs" / "image-list.md").write_text("\n".join(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "dist"))
    args = ap.parse_args()
    out = Path(args.out).resolve()
    Builder(out, write_docs=(out == ROOT / "dist")).build()


if __name__ == "__main__":
    sys.exit(main())
