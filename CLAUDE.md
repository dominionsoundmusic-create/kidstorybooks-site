# kidstorybooks.com: PLAYBOOK 2.0 REDESIGN. INSTRUCTIONS FOR CLAUDE CODE

You are rebuilding Maurice Johnson's children's book site kidstorybooks.com by running Dominic & Dalton's
Website Builder Prompt Playbook 2.0 (PLAYBOOK.md), Prompts 1 to 20, in full. Maurice's complaint about the
current site: "too spaced out" and he is "not crazy about the colors". Fix both.

## RUN STRAIGHT THROUGH. DO NOT STOP.
Maurice is not at his computer and cannot approve anything. Do NOT pause between playbook phases or ask
"continue?". Make reasonable decisions, write them in docs/decisions.md, and keep going until Prompt 20 is
finished and every check below passes. Work on the branch `build`; commit as you go and push `build` after
each phase so nothing is lost. The only reasons to stop early: something would cost money, deploy, change
Netlify or DNS, or change a repository other than this one.

## Source files (read all of them first)
- INTAKE.md: the facts. It wins over everything. UNKNOWN means leave it off the site.
- SERVICES.md: the page plan with URLs and main keywords. Follow it.
- data/books.json: all 220 books (asin, title, category, price). Every book on the site comes from here.
- keywords/Kid-Story-Books-Keywords-2026-11-12.xlsx (+ the .txt/.json raw pulls): Ubersuggest, US, Nov 12 2026.
  Write docs/keyword-plan.md: every keyword with 1,000+ searches (and every kid-specific keyword of any
  volume) is assigned to a page or listed unused with a one-line reason.
- PLAYBOOK.md: the 20 steps. Written for GHL AI Studio; apply its rules to this static build.
- The current index.html: read it for the book data and the existing social links, then move the old
  index.html and privacy-policy.html into docs/old-site/ with `git mv`. Never drag-and-drop deploy; this
  Netlify project (jazzy-kitsune-d2d250) is repo-linked, which is how the catalogue was lost once before.

## Architecture
Static pre-rendered HTML on Netlify. One central data file (src/data/site.json) plus data/books.json,
rendered by a small Python build script (build.py, Jinja2) into dist/. Commit dist/. netlify.toml with
`publish = "dist"` and no build command. Wherever the playbook says SSR, router or hydration, apply the static
equivalent and treat it as approved. Use dominionsoundmusic-create/70namesofgod-site (branch build) or
dominionsoundmusic-create/houston-powerwashing-pro (branch build) as the reference for build.py, the check
scripts and the speed fix, if you can reach them; otherwise write your own.

## Content rules
1. The site's job is to send parents, grandparents, teachers and churches to Amazon to buy Maurice's books.
   Every "Buy" button goes to https://www.amazon.com/dp/ASIN (target _blank, rel noopener). The author page
   link is https://www.amazon.com/author/dominionpublishing.
2. Book covers load from https://images-na.ssl-images-amazon.com/images/P/ASIN.jpg with width, height,
   alt (the title) and loading="lazy". If a cover fails to load, show a colored block with the title, never a
   broken image icon.
3. Never invent a book summary, age range, page count, lesson, review, rating, award, sales number or
   testimonial. Describe a book only by what its title and category say. Topic pages are written about the
   TOPIC (why bedtime stories matter, how to pick a picture book for a kindergartner, etc.), researched from
   real sources (pediatric and literacy organizations, libraries, universities), with a visible sources list.
4. Scripture: King James Version only, word for word. Check every quotation against a public-domain KJV JSON
   from GitHub with a small script (tools/check_kjv.py). Other translations described, never quoted.
5. Reader: parents and grandparents; plain words, short paragraphs, about a 7th-grade reading level.
6. Every page except privacy and 404: 3 to 6 FAQs written the way people search (use the Questions rows),
   rendered visibly AND as FAQPage JSON-LD. Also Book schema for the books on each page is fine (name, author
   Maurice Johnson, publisher Dominion Publishing, url to Amazon). No AggregateRating or Review schema.
7. Each page is written for its own keyword: main term in the title tag, H1, first paragraph and URL.
   Measure Jaccard similarity on 5-word shingles between topic pages; any pair above 15% gets rewritten.
   Record numbers in docs/qa.md.
8. No em dashes or en dashes in visible copy (the one exception is the Duplantis credit). No eyebrow labels
   above headings. American spelling. No emoji decoration. Banned phrases: "your trusted partner",
   "one-stop", "look no further", "unmatched", "cutting-edge", "elevate your", "in today's world", "delve",
   "tapestry", "embark".
9. Footer of every page: the Duplantis quote and disclaimer exactly as in INTAKE.md.
10. Mark every page with the HTML comment `dwdp:handwritten 2026-11-12` in the first 4KB.
11. Remove the old made-up testimonials. Do not replace them with anything.

## Design (Maurice's standing rules)
- Colors: bright and kid friendly but easy to read. Sunny yellow (#FFC93C or close), sky blue (#3BA7E6 or
  close), coral (#FF6B5B or close), with DARK NAVY (#16213E or close) for all body text and headings on
  white. Check every text/background pair passes WCAG AA contrast and record the ratios in docs/qa.md.
  Never white text on yellow. Never white boxes on white.
- TIGHTER LAYOUT. Maurice said the old site is "too spaced out". Section padding about 40 to 56px on
  desktop and 28 to 36px on phones, no giant empty gaps, headings close to their content. Measure: no
  vertical gap over 80px between blocks at 1440 px.
- Header/menu bar in a real brand color (sky blue or navy), never gray. Logo text "Kid Story Books".
- SOCIAL ICONS, top AND bottom of every page, as recognizable icons (inline SVG for Facebook, Instagram,
  TikTok), not text links: in the header bar and in the footer. Links in INTAKE.md. aria-label on each.
- EN/ES Google Translate toggle in the header on every page, in brand colors.
- Hero edge to edge (`--rail: clamp(22px, 5.5vw, 140px)`), headline and buttons on the left rail, main
  button above the fold. Hero image idea that needs no new art: a bright collage of 8 to 12 real book
  covers on the right side. Max height about 620px.
- Body text, photos and cards run FULL WIDTH on the rail, never a narrow center strip.
- Mostly WHITE sections broken by occasional bold color bands (e.g. hero, white, sky-blue band, white,
  yellow band). Plain sections pure white.
- Home page: a row of 4 category cards with photos/cover collages (Christian books, Bible stories, Bedtime
  stories, Nature books), featured books, links to every topic page, the Amazon author page button.
- Card rows 4 / 3 / 2 columns by width; any short last row centered. Book grids 6 / 4 / 3 / 2 columns.
- /books/: all 220 books with category filter buttons and a search box, loading in batches; works without
  JavaScript too (all books in the HTML).
- Speed fix exactly as on Maurice's other sites: self-hosted woff2 font, inline CSS, WebP 480/800/1200/1600/
  1920 srcset for any local photos, preloaded hero with fetchpriority high, delayed GA4 only once an ID
  exists (none yet), no render-blocking scripts.
- Images: every page needs a hero plus at least two in-body images. Cover collages count. Any new photo
  that does not exist yet goes in docs/image-list.md (heroes first: File name, Size 1920x1080 hero /
  1200x800 in-body, then an Artistly prompt: bright, cheerful, clearly visible, children's books, reading
  corners, no text, no logos, no recognizable faces, "subject positioned on right third of frame, well lit").
  Aim for 10 or fewer new images. Until they arrive, show a cover collage or a colored block, never a broken
  image.

## Before you finish (all must pass)
- `python3 build.py` then the check script: 0 errors (titles, one H1, canonicals https://kidstorybooks.com/,
  meta descriptions, FAQ block + JSON-LD present, every image has width/height/alt, no broken internal
  links, every ASIN in data/books.json appears on /books/).
- KJV check: 0 mismatches. Grep dist/ for em/en dashes, banned phrases, "testimonial", "5-star", "#1",
  "guarantee", "best-selling": fix every hit.
- No horizontal overflow at 1440, 1024, 768 and 390 px (do not hide overflow to pass). Screenshot the home
  page, /books/ and one topic page at 390, 1440 and 1920; look at every section; check the logo and H1 start
  near the left edge on wide screens.
- Independent fact-check: separate sub-agents that did not write the pages check every factual claim and
  source on the topic pages. Record it in docs/fact-check.md. Never say "fact-checked" unless it ran.
- Update sitemap.xml and robots.txt for the new URLs.

## Git
- Branch `build`. Commit as you go, push `build` after each phase. Do NOT push to main, do NOT change any
  Netlify setting, do NOT touch DNS, do NOT pay for anything. Maurice approves the look before it goes live.

## Final report (Maurice reads it on his phone, 5 lines max)
Pages built, checks passed, duplication range, fact-check result, how many images need Artistly, and the one
thing Maurice must do next.
