#!/usr/bin/env python3
"""WCAG 2.x contrast ratios for every text/background pair the stylesheet uses.

Usage: python3 tools/contrast.py      Exit 1 if any text pair is under 4.5:1 (AA normal text)
or any non-text pair (focus ring, icon) is under 3:1.
"""
import sys

C = {"navy": "#16213E", "navy-2": "#22305A", "yellow": "#FFC93C", "yellow-soft": "#FFF4D1",
     "sky": "#3BA7E6", "sky-soft": "#E3F3FC", "coral": "#FF6B5B", "link": "#0B5A8E", "white": "#FFFFFF",
     "muted": "#3D4766", "footer-text": "#DDE3F0", "hover-yellow": "#FFD666",
     "cover-christian": "#8FD0F5", "cover-nature": "#9BE0A8", "cover-cookbooks": "#FFB3A8",
     "cover-coloring": "#FFE08A", "cover-teens": "#C9B8F2"}

TEXT = [  # (foreground, background, where)
    ("navy", "white", "body text, headings, cards"),
    ("navy", "yellow", "hero text, yellow bands, Buy buttons"),
    ("navy", "hover-yellow", "Buy button hover"),
    ("navy", "sky", "header bar, nav, sky bands, sky hero"),
    ("navy", "sky-soft", "tip boxes, soft bands, verse boxes"),
    ("navy", "yellow-soft", "note box, ghost button hover"),
    ("white", "navy", "navy buttons, footer text, active EN/ES"),
    ("white", "navy-2", "navy button hover"),
    ("yellow", "navy", "footer headings and quote"),
    ("footer-text", "navy", "footer disclaimer and copyright"),
    ("link", "white", "body links"),
    ("link", "sky-soft", "links in soft bands"),
    ("muted", "white", "book category label, card text"),
    ("muted", "sky-soft", "topic card text on soft band"),
    ("navy", "cover-christian", "cover fallback title"),
    ("navy", "cover-nature", "cover fallback title"),
    ("navy", "cover-cookbooks", "cover fallback title"),
    ("navy", "cover-coloring", "cover fallback title"),
    ("navy", "cover-teens", "cover fallback title"),
]
NONTEXT = [
    ("navy", "white", "focus ring on white"), ("navy", "sky", "focus ring / icons on header"),
    ("navy", "yellow", "focus ring on yellow"), ("yellow", "navy", "focus ring in footer"),
    ("navy", "sky", "footer social icon glyph on sky circle"), ("sky", "navy", "footer social circle on navy"),
]


def lum(h):
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    la, lb = sorted((lum(C[a]), lum(C[b])), reverse=True)
    return (la + 0.05) / (lb + 0.05)


bad = 0
print("| Text | Background | Ratio | AA | Where |\n|---|---|---|---|---|")
for fg, bg, where in TEXT:
    r = ratio(fg, bg)
    bad += r < 4.5
    print(f"| {fg} {C[fg]} | {bg} {C[bg]} | {r:.2f}:1 | {'pass' if r >= 4.5 else 'FAIL'} | {where} |")
print("\n| Non-text | Background | Ratio | 3:1 | Where |\n|---|---|---|---|---|")
for fg, bg, where in NONTEXT:
    r = ratio(fg, bg)
    bad += r < 3
    print(f"| {fg} {C[fg]} | {bg} {C[bg]} | {r:.2f}:1 | {'pass' if r >= 3 else 'FAIL'} | {where} |")
print(f"\nNot used: white on yellow ({ratio('white','yellow'):.2f}:1), white on sky ({ratio('white','sky'):.2f}:1), "
      f"white on coral ({ratio('white','coral'):.2f}:1). Coral is decorative only (borders).")
sys.exit(1 if bad else 0)
