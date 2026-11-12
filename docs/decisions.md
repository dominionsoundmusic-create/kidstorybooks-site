# Decisions log (Playbook 2.0 run, 2026-11-12)

Maurice was not available, so these calls were made during the build. Each can be reversed.

- **D-01 Static build.** The playbook's SSR, router and hydration rules are applied as static pre-rendered
  HTML (see docs/architecture.md). Every page works with JavaScript off.
- **D-02 Old files.** `index.html` and `privacy-policy.html` moved to `docs/old-site/` with `git mv`.
  Favicons, the Dominion logo and `_redirects` moved into `src/static/`. Old `robots.txt` and
  `sitemap.xml` replaced by build output. `/privacy-policy.html` now 301s to `/privacy-policy/`.
- **D-03 /kids-cookbooks/ dropped.** SERVICES.md says to drop a topic page with fewer than 6 real fitting
  books. Only one of the 32 cookbooks is a kids' book by its title ("FLOUR & FROSTING: The Ultimate
  Kids' Baking Book"); the rest are adult cookbooks ("Elevated Southern", "High-Protein", "Type 2 Table"
  and so on). All 32 cookbooks still appear on /books/ under the Cookbooks filter.
- **D-04 All other planned topic pages kept.** Fitting titles counted from data/books.json:
  Bible stories 9, bedtime (night, nocturnal, moon, star, lullaby or sleep in the title) 9, kindness / sharing /
  feelings 9, kindergarten animal-title shelf 18, nature 34, coloring and activity 9, teens 9, Christian 65,
  by-age (titles that state an age) 15.
- **D-05 Prices left off.** books.json prices are list prices copied from the old site. Amazon prices
  change, so the site sends people to Amazon for the current price instead of showing a number that
  may be wrong.
- **D-06 Old claims removed.** The three made-up testimonials, the five-star "Loved by Families" badge,
  "Fan Favorites", "loved by kids and parents alike", "10+ Categories" and "All Ages Welcome" are gone
  and nothing replaces them.
- **D-07 Google Analytics.** The old pages loaded GA4 `G-EKXVSCT3S2`, but CLAUDE.md says no GA4 ID
  exists yet, and the old privacy policy said the site used no analytics. The new site ships with the
  delayed-GA4 code ready and the ID left blank (`src/data/site.json` -> `analytics.ga4_id`), so the
  privacy policy stays true. Question for Maurice: paste `G-EKXVSCT3S2` there to turn it back on (and
  the privacy policy line about analytics must then be updated).
- **D-08 Email removed from privacy policy.** The old policy listed an email address; INTAKE.md says
  email is UNKNOWN, so the policy now points to the Facebook page Message button.
- **D-09 Custom storybooks.** The Facebook bio says "we can create a storybook for you to publish on
  Amazon". Price, process and terms are UNKNOWN, so there is no page or offer. Question for Maurice.
- **D-10 Font.** Nunito (SIL Open Font License), self-hosted as one variable woff2 file (39 KB), preloaded.
  Rounded and friendly for a kids' site, easy to read.
- **D-11 Header in sky blue with navy text.** Navy on sky blue is 5.9:1 (AA). White on sky blue fails, so
  it is never used. Buttons are navy with white text or yellow with navy text. Coral is used only as
  the keyboard focus ring and never behind text.
- **D-12 Hero art.** No hero photos are needed: every hero shows real book covers on the right.
  In-body photos that do not exist yet show a cover collage until they are made (docs/image-list.md).
- **D-13 Book covers.** Covers hotlink Amazon's public cover URL as CLAUDE.md requires. A small inline
  script swaps any cover that fails (or comes back as Amazon's 1x1 placeholder) for a colored block with
  the title. Amazon's image host is blocked inside the build sandbox, so every screenshot shows those
  colored blocks; on the live site the real covers load.
- **D-14 Research method.** The sandbox network blocks the source sites themselves (healthychildren.org,
  cdc.gov and so on). Research and the independent fact-check were done with web search results from
  those organizations' own domains, not by opening the pages. Only claims rated high confidence were used.
  See docs/research-notes.md and docs/fact-check.md.
- **D-15 Pinterest and YouTube left off** (UNKNOWN in INTAKE.md).
