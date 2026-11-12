# QA report and handoff (Playbook 2.0, Prompts 16 to 20)

Date: 2026-11-12. Branch: `build`. Nothing deployed, no Netlify or DNS change, `main` untouched.
Rebuild and re-check everything with:

```
python3 build.py && python3 tools/check.py && python3 tools/check_kjv.py && python3 tools/similarity.py && python3 tools/contrast.py && node tools/shots.js && node tools/functional.js
```

## Summary
| Check | Result |
|---|---|
| Build (`python3 build.py`) | 14 pages, 0 errors |
| Site check (`tools/check.py`): titles, one H1, canonicals, descriptions, OG tags, one valid JSON-LD block, FAQ visible = FAQPage (3 to 6), img width/height/alt, internal links, Amazon links (new tab, noopener), social icons top and bottom, EN/ES toggle, footer quote + disclaimer, handwritten marker, banned phrases, dashes, all 220 ASINs on /books/, sitemap, robots, redirects | 0 errors, 0 warnings |
| KJV (`tools/check_kjv.py`) | 8 quotations, 0 mismatches (negative test: one changed word is caught) |
| Duplication (`tools/similarity.py`), Jaccard on 5-word shingles, 9 topic pages, 36 pairs | 0.00% to 1.51%, none over 15% |
| Contrast (`tools/contrast.py`) | all 19 text pairs pass AA (lowest 5.95:1 navy on sky blue); all non-text pairs pass 3:1 |
| Layout (`tools/shots.js`): 13 pages x 390/768/1024/1440/1920 | 65 of 65 ok: no horizontal overflow (nothing hidden to pass), no empty vertical gap over 80px at 1440, logo and H1 at 79px from the left at 1440 and 106px at 1920 |
| Functional (`tools/functional.js`) | 21 of 21 pass |
| Grep of dist/ for em/en dashes, banned phrases, "testimonial", "5-star", "#1", "guarantee", "best-selling", old email, old GA ID, Google Fonts, emoji | 0 hits in visible copy (only hits: the allowed Duplantis credit dash, CSS color codes like #16213E, and a source URL slug) |
| Fact-check (3 independent sub-agents) | 145 claims; every must-fix corrected; see docs/fact-check.md. Method: search results from each organization's own site, because the sandbox blocks opening the pages |

## Routes
| URL | Title | H1 | FAQs | Indexed | Status |
|---|---|---|---:|---|---|
| / | Children's Books by Maurice Johnson / Kid Story Books | Children's Books for Reading Together | 5 | yes | pass |
| /books/ | Children's Books List: All 220 Kid Story Books Titles | Children's Books List: All 220 Titles | 3 | yes | pass |
| /christian-childrens-books/ | Christian Children's Books by Maurice Johnson / Kid Story Books | Christian Children's Books | 4 | yes | pass |
| /bible-story-books-for-kids/ | Bible Stories for Preschoolers: Bible Story Books for Kids | Bible Stories for Preschoolers and Kindergartners | 5 | yes | pass |
| /bedtime-stories-for-kids/ | Bedtime Stories for Kids: Calm Books for Preschool and Up | Bedtime Stories for Kids | 5 | yes | pass |
| /picture-books-for-kindergarten/ | Picture Books for Kindergarteners: How to Choose and Read | Picture Books for Kindergarteners | 4 | yes | pass |
| /nature-books-for-kids/ | Children's Books About Nature: Life Cycle and Science Books | Children's Books About Nature | 4 | yes | pass |
| /childrens-books-about-kindness/ | Children's Books on Kindness, Sharing and Feelings | Children's Books on Kindness | 4 | yes | pass |
| /story-books-by-age/ | Story Books for 3 Year Olds and Up: Choosing by Age | Story Books for 3 Year Olds, and Every Age After | 4 | yes | pass |
| /coloring-books-for-kids/ | Coloring Books for Preschool Kids and Up / Kid Story Books | Coloring Books for Preschool Kids and Up | 4 | yes | pass |
| /books-for-teens/ | Books for Teens: Faith, Affirmations and Black History | Books for Teens | 4 | yes | pass |
| /about/ | About Maurice Johnson, Children's Author / Kid Story Books | About Maurice Johnson, Children's Author | 4 | yes | pass |
| /privacy-policy/ | Privacy Policy / Kid Story Books | Privacy Policy | 0 | yes | pass |
| /404.html | Page Not Found / Kid Story Books | Oops, that page is not here | 0 | no (noindex) | pass |
| /privacy-policy.html | 301 to /privacy-policy/ | | | | rule in _redirects (Netlify applies it on deploy; not testable locally) |
| /blog/* | 301 to / (kept from Sep 2026) | | | | kept |

## Main keyword placement (rule 7)
URL uses the topic slug from SERVICES.md; /bible-story-books-for-kids/ keeps its planned URL and carries "bible stories for preschoolers" in title, H1 and first paragraph. /about/ targets "Maurice Johnson children's author". Full assignment of all 437 keywords: docs/keyword-plan.md.

| Page | Main keyword | Title | H1 | First paragraph | URL |
|---|---|---|---|---|---|
| / | children's books | yes | yes | yes | yes |
| /books/ | children's books list | yes | yes | yes | yes |
| /christian-childrens-books/ | christian children's books | yes | yes | yes | yes |
| /bible-story-books-for-kids/ | bible stories for preschoolers | yes | yes | yes | yes |
| /bedtime-stories-for-kids/ | bedtime stories for kids | yes | yes | yes | yes |
| /picture-books-for-kindergarten/ | picture books for kindergarteners | yes | yes | yes | yes |
| /nature-books-for-kids/ | children's books about nature | yes | yes | yes | yes |
| /childrens-books-about-kindness/ | children's books on kindness | yes | yes | yes | yes |
| /story-books-by-age/ | story books for 3 year olds | yes | yes | yes | yes |
| /coloring-books-for-kids/ | coloring books for preschool | yes | yes | yes | yes |
| /books-for-teens/ | books for teens | yes | yes | yes | yes |

## Contrast ratios (WCAG 2.x)
| Text | Background | Ratio | AA | Where |
|---|---|---|---|---|
| navy #16213E | white #FFFFFF | 15.89:1 | pass | body text, headings, cards |
| navy #16213E | yellow #FFC93C | 10.35:1 | pass | hero text, yellow bands, Buy buttons |
| navy #16213E | hover-yellow #FFD666 | 11.40:1 | pass | Buy button hover |
| navy #16213E | sky #3BA7E6 | 5.95:1 | pass | header bar, nav, sky bands, sky hero |
| navy #16213E | sky-soft #E3F3FC | 14.00:1 | pass | tip boxes, soft bands, verse boxes |
| navy #16213E | yellow-soft #FFF4D1 | 14.47:1 | pass | note box, ghost button hover |
| white #FFFFFF | navy #16213E | 15.89:1 | pass | navy buttons, footer text, active EN/ES |
| white #FFFFFF | navy-2 #22305A | 12.82:1 | pass | navy button hover |
| yellow #FFC93C | navy #16213E | 10.35:1 | pass | footer headings and quote |
| footer-text #DDE3F0 | navy #16213E | 12.35:1 | pass | footer disclaimer and copyright |
| link #0B5A8E | white #FFFFFF | 7.32:1 | pass | body links |
| link #0B5A8E | sky-soft #E3F3FC | 6.45:1 | pass | links in soft bands |
| muted #3D4766 | white #FFFFFF | 9.16:1 | pass | book category label, card text |
| muted #3D4766 | sky-soft #E3F3FC | 8.07:1 | pass | topic card text on soft band |
| navy #16213E | cover-christian #8FD0F5 | 9.47:1 | pass | cover fallback title |
| navy #16213E | cover-nature #9BE0A8 | 10.31:1 | pass | cover fallback title |
| navy #16213E | cover-cookbooks #FFB3A8 | 9.28:1 | pass | cover fallback title |
| navy #16213E | cover-coloring #FFE08A | 12.32:1 | pass | cover fallback title |
| navy #16213E | cover-teens #C9B8F2 | 8.80:1 | pass | cover fallback title |

| Non-text | Background | Ratio | 3:1 | Where |
|---|---|---|---|---|
| navy #16213E | white #FFFFFF | 15.89:1 | pass | focus ring on white |
| navy #16213E | sky #3BA7E6 | 5.95:1 | pass | focus ring / icons on header |
| navy #16213E | yellow #FFC93C | 10.35:1 | pass | focus ring on yellow |
| yellow #FFC93C | navy #16213E | 10.35:1 | pass | focus ring in footer |
| navy #16213E | sky #3BA7E6 | 5.95:1 | pass | footer social icon glyph on sky circle |
| sky #3BA7E6 | navy #16213E | 5.95:1 | pass | footer social circle on navy |

Not used: white on yellow (1.54:1), white on sky (2.67:1), white on coral (2.80:1). Coral is decorative only (borders).

## Duplication between topic pages (Jaccard, 5-word shingles)
Measured on each page's own copy (hero lead, body, FAQs), not on book cards, collages, source lists,
Bible quotations, header or footer. Limit 15%.

```
 1.51%  bible-story-books-for-kids  vs  coloring-books-for-kids
 1.16%  bible-story-books-for-kids  vs  story-books-by-age
 1.12%  bible-story-books-for-kids  vs  picture-books-for-kindergarten
 0.75%  christian-childrens-books  vs  childrens-books-about-kindness
 0.71%  story-books-by-age  vs  coloring-books-for-kids
 0.68%  nature-books-for-kids  vs  childrens-books-about-kindness
 0.46%  christian-childrens-books  vs  books-for-teens
 0.42%  christian-childrens-books  vs  coloring-books-for-kids
 0.42%  christian-childrens-books  vs  nature-books-for-kids
 0.40%  picture-books-for-kindergarten  vs  nature-books-for-kids
 0.38%  christian-childrens-books  vs  story-books-by-age
 0.32%  picture-books-for-kindergarten  vs  childrens-books-about-kindness
 0.31%  christian-childrens-books  vs  picture-books-for-kindergarten
 0.31%  nature-books-for-kids  vs  story-books-by-age
 0.29%  coloring-books-for-kids  vs  books-for-teens
 0.23%  christian-childrens-books  vs  bible-story-books-for-kids
 0.23%  bedtime-stories-for-kids  vs  nature-books-for-kids
 0.22%  christian-childrens-books  vs  bedtime-stories-for-kids
 0.22%  picture-books-for-kindergarten  vs  story-books-by-age
 0.19%  childrens-books-about-kindness  vs  books-for-teens
 0.19%  nature-books-for-kids  vs  books-for-teens
 0.18%  picture-books-for-kindergarten  vs  books-for-teens
 0.17%  story-books-by-age  vs  books-for-teens
 0.17%  bedtime-stories-for-kids  vs  books-for-teens
 0.16%  picture-books-for-kindergarten  vs  coloring-books-for-kids
 0.16%  childrens-books-about-kindness  vs  story-books-by-age
 0.15%  bedtime-stories-for-kids  vs  coloring-books-for-kids
 0.15%  bedtime-stories-for-kids  vs  childrens-books-about-kindness
 0.14%  bedtime-stories-for-kids  vs  picture-books-for-kindergarten
 0.14%  bedtime-stories-for-kids  vs  story-books-by-age
 0.14%  bible-story-books-for-kids  vs  bedtime-stories-for-kids
 0.09%  nature-books-for-kids  vs  coloring-books-for-kids
 0.09%  bible-story-books-for-kids  vs  books-for-teens
 0.08%  bible-story-books-for-kids  vs  childrens-books-about-kindness
 0.08%  bible-story-books-for-kids  vs  nature-books-for-kids
 0.00%  childrens-books-about-kindness  vs  coloring-books-for-kids

words per page: {'christian-childrens-books': 630, 'bible-story-books-for-kids': 719, 'bedtime-stories-for-kids': 749, 'picture-books-for-kindergarten': 674, 'nature-books-for-kids': 610, 'childrens-books-about-kindness': 595, 'story-books-by-age': 712, 'coloring-books-for-kids': 599, 'books-for-teens': 484}
pairs: 36, range 0.00% to 1.51%, over 15%: 0
```

## Layout and responsive (Prompt 18)
Real Chromium via Playwright. Amazon cover images are blocked inside the sandbox, so every screenshot
shows the colored title block a reader would see if a cover failed to load (this is the fallback
working, not a bug). On the live site the real covers load.

Screenshots (home, /books/, bedtime topic page at 390, 1440 and 1920): `docs/screenshots/`.
Reviewed by eye: header bar in sky blue with logo, menu, three social icons and EN/ES; hero edge to edge
with headline and buttons on the left rail and the main button above the fold; covers collage on the
right; white sections broken by sky and yellow bands; book grids 6/4/3/2 columns; card rows 4/3/2 with
the short last row centered; tips 3/2/1; footer navy with icons, quote and disclaimer.

Fixed during QA: section padding cut to 40px (two sections now meet at 80px or less); hero bottom padding;
a clipped third row of hero covers; links on the sky band switched to navy; focus ring changed from coral
(2.8:1 on white, too low) to navy with a yellow halo; tip boxes now center a short last row; covers show
the colored title block while loading instead of a white box; phone hero shows one even row of covers.

```
390px / logo@22 h1@22 height 9330  ok
390px /about/ logo@22 h1@22 height 5694  ok
390px /bedtime-stories-for-kids/ logo@22 h1@22 height 10245  ok
390px /bible-story-books-for-kids/ logo@22 h1@22 height 9804  ok
390px /books-for-teens/ logo@22 h1@22 height 8960  ok
390px /books/ logo@22 h1@22 height 12698  ok
390px /childrens-books-about-kindness/ logo@22 h1@22 height 9847  ok
390px /christian-childrens-books/ logo@22 h1@22 height 20405  ok
390px /coloring-books-for-kids/ logo@22 h1@22 height 9402  ok
390px /nature-books-for-kids/ logo@22 h1@22 height 13932  ok
390px /picture-books-for-kindergarten/ logo@22 h1@22 height 11105  ok
390px /privacy-policy/ logo@22 h1@22 height 3518  ok
390px /story-books-by-age/ logo@22 h1@22 height 11051  ok
768px / logo@42 h1@42 height 6649  ok
768px /about/ logo@42 h1@42 height 5044  ok
768px /bedtime-stories-for-kids/ logo@42 h1@42 height 7702  ok
768px /bible-story-books-for-kids/ logo@42 h1@42 height 7642  ok
768px /books-for-teens/ logo@42 h1@42 height 7258  ok
768px /books/ logo@42 h1@42 height 9747  ok
768px /childrens-books-about-kindness/ logo@42 h1@42 height 7693  ok
768px /christian-childrens-books/ logo@42 h1@42 height 15924  ok
768px /coloring-books-for-kids/ logo@42 h1@42 height 7201  ok
768px /nature-books-for-kids/ logo@42 h1@42 height 11257  ok
768px /picture-books-for-kindergarten/ logo@42 h1@42 height 8522  ok
768px /privacy-policy/ logo@42 h1@42 height 2379  ok
768px /story-books-by-age/ logo@42 h1@42 height 8582  ok
1024px / logo@56 h1@56 height 4946  ok
1024px /about/ logo@56 h1@56 height 3165  ok
1024px /bedtime-stories-for-kids/ logo@56 h1@56 height 5947  ok
1024px /bible-story-books-for-kids/ logo@56 h1@56 height 5861  ok
1024px /books-for-teens/ logo@56 h1@56 height 5488  ok
1024px /books/ logo@56 h1@56 height 7515  ok
1024px /childrens-books-about-kindness/ logo@56 h1@56 height 5739  ok
1024px /christian-childrens-books/ logo@56 h1@56 height 12042  ok
1024px /coloring-books-for-kids/ logo@56 h1@56 height 5544  ok
1024px /nature-books-for-kids/ logo@56 h1@56 height 8281  ok
1024px /picture-books-for-kindergarten/ logo@56 h1@56 height 6493  ok
1024px /privacy-policy/ logo@56 h1@56 height 2001  ok
1024px /story-books-by-age/ logo@56 h1@56 height 5990  ok
1440px / logo@79 h1@79 height 4321  ok
1440px /about/ logo@79 h1@79 height 3573  ok
1440px /bedtime-stories-for-kids/ logo@79 h1@79 height 5137  ok
1440px /bible-story-books-for-kids/ logo@79 h1@79 height 5074  ok
1440px /books-for-teens/ logo@79 h1@79 height 4976  ok
1440px /books/ logo@79 h1@79 height 5469  ok
1440px /childrens-books-about-kindness/ logo@79 h1@79 height 5312  ok
1440px /christian-childrens-books/ logo@79 h1@79 height 8840  ok
1440px /coloring-books-for-kids/ logo@79 h1@79 height 4960  ok
1440px /nature-books-for-kids/ logo@79 h1@79 height 6582  ok
1440px /picture-books-for-kindergarten/ logo@79 h1@79 height 5388  ok
1440px /privacy-policy/ logo@79 h1@79 height 1900  ok
1440px /story-books-by-age/ logo@79 h1@79 height 5719  ok
1920px / logo@106 h1@106 height 4637  ok
1920px /about/ logo@106 h1@106 height 4066  ok
1920px /bedtime-stories-for-kids/ logo@106 h1@106 height 5613  ok
1920px /bible-story-books-for-kids/ logo@106 h1@106 height 5452  ok
1920px /books-for-teens/ logo@106 h1@106 height 5440  ok
1920px /books/ logo@106 h1@106 height 6161  ok
1920px /childrens-books-about-kindness/ logo@106 h1@106 height 5881  ok
1920px /christian-childrens-books/ logo@106 h1@106 height 10150  ok
1920px /coloring-books-for-kids/ logo@106 h1@106 height 5486  ok
1920px /nature-books-for-kids/ logo@106 h1@106 height 7482  ok
1920px /picture-books-for-kindergarten/ logo@106 h1@106 height 6044  ok
1920px /privacy-policy/ logo@106 h1@106 height 1710  ok
1920px /story-books-by-age/ logo@106 h1@106 height 6442  ok

0 problems
```

## Functional (Prompt 19)
```
PASS  desktop: More Topics submenu opens on click
PASS  desktop: Escape closes submenu
PASS  cover fallback: blocked covers become title blocks (no broken images)
PASS  every external link opens in a new tab with rel=noopener
PASS  logo links to home
PASS  ES button sets googtrans=/en/es and reloads
PASS  ES button shows pressed after reload
PASS  EN button clears the cookie
PASS  /books/: first batch shows 48
PASS  /books/: Show more adds the next 48
PASS  /books/: Teens filter shows 9
PASS  /books/: Christian filter shows 48 of 65 then all after Show more
PASS  /books/: search "noah" finds Noah's Ark
PASS  /books/: empty search says so
PASS  404 page served with noindex and a way back
PASS  phone: menu hidden until tapped
PASS  phone: Menu button opens the nav
PASS  phone: social icons and EN/ES visible in header
PASS  no JS: all 220 books visible on /books/
PASS  no JS: nav links visible
PASS  no JavaScript errors on any tested page

21 passed, 0 failed
```
Forms (Prompt 13): none. INTAKE.md says no contact form; people are pointed to the Facebook Message button.
Reviews (Prompt 14): none exist and none were added. Social links: Facebook, Instagram, TikTok, each with
an aria-label, in the header and footer of every page, opening in a new tab. Not verified: that the three
social URLs load (the sandbox cannot reach them); they are copied exactly from INTAKE.md.
Google Translate: the ES button sets the `googtrans` cookie and reloads (tested). The Google script itself
cannot load in the sandbox, so the actual Spanish translation is not verified here.

## Speed fix
| Item | Status |
|---|---|
| Self-hosted font | Nunito variable, one woff2 (39 KB), preloaded, `font-display: swap` |
| Inline CSS | Yes, the whole stylesheet is inlined (no CSS request) |
| Render-blocking scripts | None: a tiny inline cover-fallback script, JSON-LD, and `site.js` with `defer` (3.6 KB) |
| Hero | first cover preloaded with `fetchpriority="high"`; first three hero covers `fetchpriority="high"`, none lazy |
| Below-fold images | `loading="lazy"` with width and height on every image |
| WebP 480/800/1200/1600/1920 | built automatically by build.py for any local photo (none exist yet; the 10 Artistly photos will get them) |
| GA4 | delayed loader in place, no ID set (see decisions.md D-07) |
| Page weight (gzip) | home 11 KB, topic pages 10 to 19 KB, /books/ (all 220 books) 26 KB |

## SEO (Prompt 16)
Every indexable page has a unique title, description, canonical on https://kidstorybooks.com/, Open Graph
tags with an absolute https image, exactly one H1, and one JSON-LD graph (Organization, WebSite on home,
WebPage/CollectionPage/AboutPage, BreadcrumbList, ItemList of Book items with author Maurice Johnson and
publisher Dominion Publishing, FAQPage). No Review or AggregateRating schema. The 404 page is noindex and
not in the sitemap. sitemap.xml lists the 13 indexable URLs; robots.txt points to it.

## Remnant sweep (Prompt 17)
Removed: the made-up testimonials, five-star badge, "Fan Favorites", stats band, emoji, em dashes, Google
Fonts, the email address (UNKNOWN in INTAKE), the old GA4 tag (see D-07), the unchecked John 3:16 link.
No lorem, TODO, placeholder text, empty links or duplicate IDs (checked by tools/check.py).

## Remaining items
- 10 new photos to make in Artistly (docs/image-list.md). Until then, cover collages stand in.
- Questions for Maurice (docs/fact-brief.md): custom storybooks page, GA4 ID, public email, Pinterest/YouTube.
- Spot-check the Sources links by hand before launch (the sandbox could not open them).
- Maurice approves the look, then merges `build` into `main` himself. Netlify publishes `dist/`
  (netlify.toml: `publish = "dist"`, no build command).

## Readiness
Ready for Maurice's review on the `build` branch. Not live. Every required check passed; the items
above that could not be verified inside the sandbox are listed as such.
