#!/usr/bin/env python3
"""Jaccard similarity on 5-word shingles between topic pages (CLAUDE.md rule 7: rewrite any pair > 15%).

Measures the page's own written content: everything inside <div class="page-content"> plus the FAQ
answers and the hero lead, minus book cards, collages, the sources list and Bible quotations (book
titles and shared verses are data, not copy). Header, footer, topic links and CTA band are excluded.

Usage: python3 tools/similarity.py [--dist DIR] [--limit 0.15]   Exit 1 if any pair is over the limit.
"""
import argparse
import re
import sys
from html import unescape
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPICS = ["christian-childrens-books", "bible-story-books-for-kids", "bedtime-stories-for-kids",
          "picture-books-for-kindergarten", "nature-books-for-kids", "childrens-books-about-kindness",
          "story-books-by-age", "coloring-books-for-kids", "books-for-teens"]


def words(raw):
    lead = re.search(r'<p class="hero__lead">(.*?)</p>', raw, re.S)
    body = re.search(r'<div class="page-content">(.*?)<section class="band band--soft">', raw, re.S).group(1)
    for pat in (r'<div class="books.*?</article>\s*</div>', r'<article class="book".*?</article>',
                r'<figure class="collage.*?</figure>', r'<aside class="sources".*?</aside>',
                r'<blockquote class="verse".*?</blockquote>'):
        body = re.sub(pat, " ", body, flags=re.S)
    text = (lead.group(1) if lead else "") + " " + body
    return re.findall(r"[a-z0-9']+", unescape(re.sub(r"<[^>]+>", " ", text)).lower())


def shingles(w, n=5):
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    ap.add_argument("--limit", type=float, default=0.15)
    a = ap.parse_args()
    pages = {t: words((Path(a.dist) / t / "index.html").read_text()) for t in TOPICS}
    rows, bad = [], 0
    for x, y in combinations(TOPICS, 2):
        sx, sy = shingles(pages[x]), shingles(pages[y])
        j = len(sx & sy) / len(sx | sy)
        rows.append((j, x, y))
        bad += j > a.limit
    rows.sort(reverse=True)
    for j, x, y in rows:
        print(f"{j:6.2%}  {x}  vs  {y}{'  OVER LIMIT' if j > a.limit else ''}")
    print("\nwords per page:", {t: len(w) for t, w in pages.items()})
    print(f"pairs: {len(rows)}, range {rows[-1][0]:.2%} to {rows[0][0]:.2%}, over {a.limit:.0%}: {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
