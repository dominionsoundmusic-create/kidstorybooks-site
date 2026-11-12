# Independent fact-check (2026-11-12)

## Who checked
Three separate sub-agents that did not write any page checked the nine topic pages and the About page.
Full tables, one row per claim, are in `docs/fact-check/`:

| Group | Pages | Claims checked | Supported | Partly / cannot verify | Wrong or unsupported |
|---|---|---:|---:|---:|---:|
| A | bedtime, Bible stories, Christian | 45 | 31 | 11 | 3 |
| B | kindergarten picture books, nature, kindness | 44 | 30 | 14 | 0 (7 must-fix: citation or wording) |
| C | story books by age, coloring, teens, About | 56 | about 43 | 9 | 4 |
| **Total** | **10 pages** | **145** | **about 104** | | |

## How it was checked (important limit)
The sandbox network blocks the source websites themselves (healthychildren.org, cdc.gov, naeyc.org and
so on): pages cannot be opened. So each research claim was checked with web search limited to the
cited organization's own domain. A claim counts as supported only when a search result from that
organization's own site says it. This is weaker than opening each page. Before launch, spot-check the
Sources links by hand (they all appeared in search under the titles the pages give).

Also checked:
- Bible references (book and chapter for each story in the Bible-story list) against the KJV text: all 10 correct.
- All 8 Scripture quotations: word for word KJV (tools/check_kjv.py, 0 mismatches).
- Every statement about a book against data/books.json (title, category, price only).
- About page facts against INTAKE.md: all match; no UNKNOWN item appears.
- No reviews, ratings, awards, sales figures or testimonials anywhere.

## What was wrong, and what changed
Every must-fix item was corrected in the source pages (src/pages/) using the checkers' wording:

| Page | Problem found | Fix |
|---|---|---|
| Bedtime | Shelf said every title has night/moon/stars/sleep in it; Felix the Flashlight and The Owl Who Loved the Day do not | Removed both from the shelf and collage; label now includes "nocturnal" (The Nocturnal Friend) |
| Bedtime | "Five minutes every night does more good" and "most families read a few minutes to half an hour" could not be verified | Removed; now "even a few minutes counts" |
| Christian | "A second reading is when kids start asking questions" placed next to the NAEYC citation | Removed |
| Christian | FAQs matched specific books to ages 2-3 and 6-8 | Rewritten without matching any book to an age |
| Christian | "Church leaders agree" overstated Barna | "Many church leaders say the same" |
| Christian | Title capitals changed (EL SHADDAI, ELOHIM, JEHOVAH-SHALOM) | Exact titles from books.json |
| Bible / Kindergarten | Dialogic reading cited to the wrong Reading Rockets page; "understanding" not backed | Cites Reading Rockets "Dialogic Reading"; claim is now "oral language and vocabulary" |
| Bible | "Some of the first Bible stories many children hear" not verifiable | "Some of the best-known stories in the Bible" |
| Nature | NAEYC "born scientists" line cited to the wrong article; "cannot do it alone" unconfirmed | Cites NAEYC "More Than a Foundation" (2017); unconfirmed sentence removed |
| Nature | AAP "better motor skills" unconfirmed | Removed; obesity, nearsightedness and learning-outcome claims kept (confirmed) |
| Nature | "Information books with colorful photos" tied to kindergarten; really first grade | Removed from nature page; kindergarten page now says "as children grow" |
| Nature | Salmon called an ocean animal | FAQ now says salmon spend their adult years at sea |
| Kindness | ZERO TO THREE tip cited to the wrong page; aimed at toddlers | Cites ZERO TO THREE "24 to 36 Months: Social-Emotional Development"; says "with toddlers" |
| All pages | Amazon box said the author page "lists every title" (unverifiable) | "shows his books in one place" |
| Coloring | "Puzzle books mix words and pictures" (not in the title) | "are word puzzle books, as their titles say" |
| Coloring | FAQ matched books to 9 and 10 year olds | Rewritten without an age match |
| Coloring | "Adults can mostly watch" attributed to ZERO TO THREE (wording not confirmed) | Removed |
| Teens | "Slim" book (a length claim); FAQ called non-Christian-category teen books Christian | "slim" removed; FAQ now names only Quiet Strength (Volume 1): God Made My Mind and points to Amazon |
| Teens | "Questions many teens ask" unsupported | "big questions, as their titles show" |
| By age | AAP board books "from birth" (results say about 4 to 8 months); "Three is when that starts" not in CDC | "for babies"; sentence removed |
| About | "Amazon handles the printing" not in INTAKE.md | "payment and delivery" |

The corrections only remove claims, soften them or swap in the source the checkers found. The
changed text was not sent through a second full fact-check pass.

## Result
After fixes: no known wrong or unsupported claim remains on the topic pages or the About page.
Verification method: web search results from each organization's own site (pages could not be opened).
