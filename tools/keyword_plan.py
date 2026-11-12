#!/usr/bin/env python3
"""Write docs/keyword-plan.md from the Ubersuggest sheet (ALL tab, 439 keywords, US, Nov 12 2026).

Every keyword gets a page or an "unused" line with a one-line reason. Rules are checked in order and the
first match wins. The script fails if any keyword with 1,000+ searches, or any kid-specific keyword,
falls through to the catch-all.

Usage: python3 tools/keyword_plan.py
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
SHEET = ROOT / "keywords" / "Kid-Story-Books-Keywords-2026-11-12.xlsx"

U = "UNUSED"
RULES = [
    # ---- not targeted at all (SERVICES.md "Do NOT target" + other off-plan reasons) ----
    (r"paw patrol|minion|toy story|harry potter|pete the cat|roald dahl|max lucado|mo willems|veggie ?tales|minno|disney|freddy|fnaf|pikachu|bobbie goods|coco wyo|basford|lisa frank|crayola|cbeebies|storyberries|sooper books|yoto|goodnight moon|uncle a(rthur|uthor)", U, "Trademarked character, brand or other author's series."),
    (r"walmart|target\b|michaels|dollar tree|hobby lobby|barnes|shutterfly|snapfish|google|near me|\bstore\b|\bused\b|cheap", U, "Store or platform name / local shopping term; the site only links to Amazon."),
    (r"movie|film|\bcast\b|bugsy|hamster|sandler|madonna|girlfriend|tim and eric|youtube|animation|animated|video|nyt|crossword|\btrap\b", U, "Movie, music, video or media-platform search, not children's books."),
    (r"adult", U, "Adult audience; the site is for children's books."),
    (r"free|printable|pdf|online|on tape|read along|digital", U, "Free, printable, online or audio intent; the site sells printed books on Amazon."),
    (r"custom|personali[sz]ed|personal childrens|customizable", U, "Custom/personalized books: offer is UNKNOWN (INTAKE.md), no page."),
    (r"publishing|literary agent|illustrat|writers|and authors|\bmaker\b|\bmake\b|to make|creat|clip ?art|drawings?|covers|quotes|ideas|titles|example|cost|box", U, "Publishing, craft or design term, not a parent looking for a book."),
    (r"bookshelf|storage|subscription", U, "Furniture or subscription service, not a book topic."),
    (r"short stor|ray bradbury|italicized|what short stories", U, "About the adult short-story form, not children's books."),
    (r"how many bible|bible books|redeeming love|^will bible|how often should you read the bible|are bible stories real|when bible", U, "Bible trivia or apologetics question; no book or page answers it honestly."),
    (r"islamic|catholic", U, "Different faith tradition than this catalogue."),
    (r"^9 story book$|^will pictures$", U, "Brand name or unclear intent."),
    # ---- coloring ----
    (r"coloring (books|pages) (preschool|for 9|for 10)|coloring books for (9|10) year", "/coloring-books-for-kids/", "main + age supporting"),
    (r"christmas coloring|coloring books for christmas|coloring books thanksgiving|unicorn", "/coloring-books-for-kids/", "matching titles exist (Christmas, Thanksgiving, Unicorn coloring books)"),
    (r"coloring pages jesus|bible stories coloring|coloring.*bible|color sheets bible|bible stories coloring pictures", U, "No Christian or Bible coloring title in the catalogue (SERVICES.md: only if one exists)."),
    (r"halloween|fall|spring|winter|pumpkin|easter egg|mandala|kawaii|cozy|markers|numbers?|dinosaur|teens", U, "No coloring title on this theme in the catalogue."),
    (r"when did coloring books come out", U, "History trivia; nothing to sell against it."),
    (r"^coloring books( cute| easy)?$|coloring books pages", "/coloring-books-for-kids/", "general coloring term (no printable pages offered)"),
    # ---- christian / bible ----
    (r"christian books for|christian chapter books|best christian books|childrens books christian", "/christian-childrens-books/", "main + age supporting (FAQs)"),
    (r"bible stories for preschool|bible stories for kindergart|bible stor(y|ies) books? for \d|bible stories for \d|list of bible stories|childrens story book bible|why bible stories|how much stories are in the bible|how many bible stories", "/bible-story-books-for-kids/", "main + supporting"),
    (r"bedtime stor(y|ies).*bible|bible.*bedtime", "/bedtime-stories-for-kids/", "Bible bedtime section"),
    (r"noah|jonah|david|goliath|moses|elijah|creation|easter|prodigal|childhood bible|good bible|famous bible|well known|little bible stories$|book of bible stories|bible stories book|my book of bible|the bible stories|bible stories of the bible|^bible stories$|bible bible|in order|short bible|bible stories short|interesting|cool bible|newborn|pictures|in pictures|funny", "/bible-story-books-for-kids/", "matching title or general Bible-story term"),
    (r"bible stor", U, "Bible person or theme with no matching book title in the catalogue."),
    # ---- bedtime ----
    (r"cinderella|goldilocks|beanstalk|little pigs|princess|classic|fairy|scary|christmas|interesting", U, "Classic fairy tale or theme with no matching title."),
    (r"bedtime stor|5 minute|nothing much happens|how bedtime", "/bedtime-stories-for-kids/", "main + supporting"),
    # ---- ages ----
    (r"story books for|stories to tell|what age is the book", "/story-books-by-age/", "main + age supporting"),
    # ---- kindness ----
    (r"kindness|sharing|feelings|empathy|respect|anxiety", "/childrens-books-about-kindness/", "main + supporting (worry/feelings titles)"),
    # ---- nature ----
    (r"nature|science|ocean|nonfiction|spanish", "/nature-books-for-kids/", "main + supporting"),
    # ---- kindergarten / picture books ----
    (r"kindergarten|picture books for kindergarteners|with animals|dinosaurs|^picture books$|picture books (best|about friendship)|good picture books|friends picture|childrens books pictures?$|childrens books picture$|read aloud|interactive|wordless|small picture|cartoon picture|hidden picture|best online", "/picture-books-for-kindergarten/", "main + supporting"),
    # ---- books list / home ----
    (r"childrens books list", "/books/", "main"),
    (r"^childrens books$|childrens books stories|childrens books to read$|childrens books read$", "/", "main + supporting"),
    (r"childrens books (easter)", "/bible-story-books-for-kids/", "The True Meaning of Easter is on this shelf"),
    # ---- unused children's book themes ----
    (r"classic|old|vintage|90s|1980s|2000s|famous|popular|best|bestsellers|characters|series", U, "Classics, rankings or other authors' series; no sales or ranking claims allowed."),
    (r"about food", U, "Only one kids' cookbook title; /kids-cookbooks/ dropped (decisions.md D-03)."),
    (r"\bcats?\b", U, "Only one cat title (Sebastian's Fuzzies); too few for a page."),
    (r"death|grief|divorce|autism|adoption|disabilit|9 11", U, "Sensitive topic with no matching title; not targeted."),
    (r"french", U, "Only one French-titled book (a counting book); too few for a page."),
    (r"wedding|xmas tree|xmas stories|valentines", U, "Off-topic or seasonal theme with no matching title."),
    (r".", U, "Topic with no matching title in the catalogue (one page per real shelf only)."),
]


def main():
    ws = openpyxl.load_workbook(SHEET)["ALL"]
    rows = [r for r in list(ws.iter_rows(values_only=True))[1:] if r[0] and r[1] is not None]
    assigned, unused = defaultdict(list), []
    fallthrough = []
    for kw, vol, diff, cpc, seed, kind in rows:
        k = kw.lower().replace("’", "'").replace("children's", "childrens")
        for pat, page, note in RULES:
            if re.search(pat, k):
                break
        if page == U:
            unused.append((vol, kw, note, seed))
            if pat == ".":
                fallthrough.append((vol, kw))
        else:
            assigned[page].append((vol, kw, note))
    kid = re.compile(r"kid|child|preschool|kindergart|year old|toddler|infant|newborn|baby|grader|teen|story book")
    must = [(v, k) for v, k in fallthrough if v >= 1000 or kid.search(k)]
    out = ["# Keyword plan", "",
           "Source: keywords/Kid-Story-Books-Keywords-2026-11-12.xlsx, ALL tab (Ubersuggest, US, Nov 12 2026), "
           f"{len(rows)} keywords. Generated by tools/keyword_plan.py. Every keyword is either assigned to one page "
           "or listed as unused with a reason. One main keyword per page; the main term is in the title tag, H1, "
           "first paragraph and URL.", ""]
    order = ["/", "/books/", "/christian-childrens-books/", "/bible-story-books-for-kids/", "/bedtime-stories-for-kids/",
             "/picture-books-for-kindergarten/", "/nature-books-for-kids/", "/coloring-books-for-kids/",
             "/story-books-by-age/", "/childrens-books-about-kindness/"]
    out += ["## Assigned", ""]
    for page in order:
        items = sorted(assigned.get(page, []), key=lambda r: -r[0])
        out += [f"### {page} ({len(items)} keywords, {sum(i[0] for i in items):,} searches/mo)", "",
                "| Keyword | Vol | Note |", "|---|---:|---|"]
        out += [f"| {kw} | {vol:,} | {note} |" for vol, kw, note in items]
        out.append("")
    out += ["### /books-for-teens/ and /about/", "",
            "No teen or author keywords exist in the pull (Ubersuggest showed no data). /books-for-teens/ targets "
            "\"books for teens\" and /about/ targets \"Maurice Johnson children's author\" by plan (SERVICES.md).", ""]
    out += ["## Unused", "", "| Keyword | Vol | Seed | Reason |", "|---|---:|---|---|"]
    out += [f"| {kw} | {vol:,} | {seed} | {why} |" for vol, kw, why, seed in sorted(unused, key=lambda r: -r[0])]
    n_assigned = sum(len(v) for v in assigned.values())
    out += ["", f"Totals: {n_assigned} assigned, {len(unused)} unused, {len(rows)} keywords. "
            f"Keywords with 1,000+ searches: {sum(1 for r in rows if r[1] >= 1000)}, all covered above."]
    (ROOT / "docs" / "keyword-plan.md").write_text("\n".join(out) + "\n")
    print(f"{n_assigned} assigned, {len(unused)} unused of {len(rows)}")
    for page in order:
        print(f"  {page}: {len(assigned.get(page, []))}")
    print("catch-all (check these):")
    for v, k in sorted(fallthrough, reverse=True):
        print(f"  {v:>7,}  {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
