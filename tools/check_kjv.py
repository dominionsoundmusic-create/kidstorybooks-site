#!/usr/bin/env python3
"""Check every Scripture quotation on the built site against the public-domain KJV (tools/data/kjv.json).

Quotations are marked up as <blockquote class="verse" data-ref="Book C:V">"text"</blockquote>.
Comparison ignores case, quote marks, apostrophe style and spacing, but every word and punctuation
mark must match. Also flags any blockquote or "(KJV)"-style citation outside that markup, and any
other translation abbreviation (NIV, ESV, NKJV, NLT...) used next to a quotation.

Usage: python3 tools/check_kjv.py [--dist DIR]     Exit 1 on any mismatch.
"""
import argparse
import json
import re
import sys
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KJV = json.loads((ROOT / "tools" / "data" / "kjv.json").read_bytes().decode("utf-8-sig"))
BOOKS = {b["name"].lower(): b for b in KJV}


def norm(s):
    s = unescape(s).replace("’", "'").replace("‘", "'").replace("“", "").replace("”", "")
    s = s.replace('"', "")
    s = re.sub(r"\s+([,;:.!?])", r"\1", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def lookup(ref):
    m = re.fullmatch(r"(.+?) (\d+):(\d+)", ref)
    book, c, v = m.group(1).lower(), int(m.group(2)), int(m.group(3))
    return BOOKS[book]["chapters"][c - 1][v - 1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    dist = Path(ap.parse_args().dist)
    checked, bad = 0, 0
    for f in sorted(dist.rglob("*.html")):
        raw = f.read_text()
        for m in re.finditer(r'<blockquote class="verse" data-ref="([^"]+)"><p>(.*?)</p><cite>(.*?)</cite></blockquote>', raw, re.S):
            ref, quoted, cite = m.groups()
            checked += 1
            want = lookup(ref)
            ok = norm(quoted) == norm(want) and "(KJV)" in cite
            bad += not ok
            print(f"{'OK      ' if ok else 'MISMATCH'} {f.relative_to(dist)}  {ref}")
            if not ok:
                print(f"   site: {norm(quoted)}\n   KJV:  {norm(want)}")
        if raw.count("<blockquote") != raw.count('<blockquote class="verse"'):
            bad += 1
            print(f"MISMATCH {f.relative_to(dist)}: blockquote without verse markup")
        for t in re.findall(r"\((?:NIV|ESV|NKJV|NLT|NASB|CSB|MSG|AMP)\)", raw):
            bad += 1
            print(f"MISMATCH {f.relative_to(dist)}: other translation quoted {t}")
    print(f"\n{checked} quotations checked, {bad} mismatches")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
