# Playbook 2.0, Prompts 2 and 3: Architecture check, baseline and route matrix

## Prompt 2: architecture result
The playbook is written for a GHL AI Studio TanStack Start SSR project. This site is not that, and
CLAUDE.md says to apply the static equivalent of every SSR, router or hydration rule.

- Before: two hand-written files (index.html, 120 KB with all 220 books inline; privacy-policy.html),
  `_redirects`, `sitemap.xml`, `robots.txt`, favicons. No build step. Netlify project
  jazzy-kitsune-d2d250 is linked to the repo.
- After: static pre-rendered HTML. `build.py` (Python 3, Jinja2, PyYAML, Pillow) renders
  `src/pages/*.html` (Jinja + YAML front matter) with `src/data/site.json` and `data/books.json`
  into `dist/`. `dist/` is committed. `netlify.toml` has `publish = "dist"` and no build command.
- "SSR" equivalent: every title, description, canonical, Open Graph tag, JSON-LD block, H1 and all
  body copy (including all 220 books on /books/) is in the HTML file Netlify serves. JavaScript only
  adds the mobile menu, the EN/ES toggle, the /books/ filter and search, and the cover fallback.
- "Router" equivalent: one HTML file per URL (`/x/` -> `dist/x/index.html`), plain links.
- "Hydration" equivalent: none needed. Pages work with JavaScript turned off.
- Commands: `python3 build.py`, `python3 tools/check.py`, `python3 tools/similarity.py`,
  `python3 tools/check_kjv.py`, `python3 tools/contrast.py`, `python3 tools/keyword_plan.py`,
  `node tools/shots.js` (Playwright layout/overflow/gap checks and screenshots).

## Prompt 3: baseline
- Pre-existing state: no build, no tests. Old pages kept for reference in `docs/old-site/`.
- Old-site remnants to remove: three made-up testimonials, "Loved by Families" five-star badge,
  "200+ Books Published / 10+ Categories / All Ages Welcome" stats, emoji decoration, em dashes,
  Google Fonts (replaced by self-hosted font), an email address that INTAKE marks UNKNOWN, a
  John 3:16 link with no checked quotation, "Fan Favorites" and "loved by kids and parents" claims.

## Route matrix
| Route | Type | Source | Nav | Sitemap | Indexable | Status |
|---|---|---|---|---|---|---|
| / | home | src/pages/index.html | logo + Home | yes | yes | built |
| /books/ | catalogue (all 220) | src/pages/books.html + data/books.json | yes | yes | yes | built |
| /christian-childrens-books/ | topic | src/pages/christian-childrens-books.html | yes (Topics) | yes | yes | built |
| /bible-story-books-for-kids/ | topic | src/pages/bible-story-books-for-kids.html | yes (Topics) | yes | yes | built |
| /bedtime-stories-for-kids/ | topic | src/pages/bedtime-stories-for-kids.html | yes (Topics) | yes | yes | built |
| /picture-books-for-kindergarten/ | topic | src/pages/picture-books-for-kindergarten.html | yes (Topics) | yes | yes | built |
| /nature-books-for-kids/ | topic | src/pages/nature-books-for-kids.html | yes (Topics) | yes | yes | built |
| /coloring-books-for-kids/ | topic | src/pages/coloring-books-for-kids.html | yes (Topics) | yes | yes | built |
| /books-for-teens/ | topic | src/pages/books-for-teens.html | yes (Topics) | yes | yes | built |
| /story-books-by-age/ | topic | src/pages/story-books-by-age.html | yes (Topics) | yes | yes | built |
| /childrens-books-about-kindness/ | topic | src/pages/childrens-books-about-kindness.html | yes (Topics) | yes | yes | built |
| /kids-cookbooks/ | topic | n/a | n/a | n/a | n/a | DROPPED (decisions.md D-03) |
| /about/ | about | src/pages/about.html | yes | yes | yes | built |
| /privacy-policy/ | legal | src/pages/privacy-policy.html | footer | yes | yes | built |
| /404.html | 404 | src/pages/404.html | no | no | noindex | built |
| /privacy-policy.html | redirect 301 -> /privacy-policy/ | src/static/_redirects | no | no | n/a | built |
| /blog/* | redirect 301 -> / (kept from Sep 2026) | src/static/_redirects | no | no | n/a | kept |

## Stage plan
Phase 1 (P1 to P3): this file, fact-brief.md, decisions.md. Phase 2 (P4 to P6): site.json, brand
tokens, header/footer/nav. Phase 3 (P7 to P12): home, /books/, nine topic pages, about, privacy.
Phase 4 (P13 to P15): no forms (none approved, documented skip), social icons, media + image list.
Phase 5 (P16 to P17): SEO checks, remnant sweep. Phase 6 (P18 to P20): browser QA, fact-check,
final handoff in docs/qa.md.
