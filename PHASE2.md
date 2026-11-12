# Phase 2: more keyword pages (Maurice, Nov 12 2026)

Maurice: "You can make pages for all these keywords. Some of them are like 46 difficulty, but that's okay. We
need to make pages for them. I can sell some of my books." Phase 1 (13 pages) is done and passed every check.
Phase 2 adds pages for the keyword clusters below. SEO difficulty up to about 50 is fine.

Every rule in CLAUDE.md and INTAKE.md still applies (KJV only and checked, no invented book details, FAQs +
JSON-LD, similarity under 15%, tight layout, social icons, Duplantis footer, `dwdp:handwritten 2026-11-12`,
images, all checks). Run straight through, commit and push `build` as you go, do not touch main or Netlify.

## The rule for every new page
Each page is written for its own keyword and is genuinely useful on its own: real research on the topic for
parents, with a sources list, plus the real books from data/books.json whose TITLE or CATEGORY fits.
- Topic pages (seasons, animals, feelings): build only if at least 4 real books fit by title. If fewer fit,
  skip the page and log it in docs/decisions.md with the count.
- Bible story pages: the Bible story itself is the content (who, what happened, what it teaches kids), with
  the key KJV verses quoted exactly. Link any of Maurice's books whose title matches the story or the
  christian category. These pages do NOT need 4 matching books.
- Never a page for trademarked characters/brands, the Bedtime Stories movie, adult topics, free printables,
  or custom/personalized books (see SERVICES.md "Do NOT target").
- Sensitive topics (death, grief, divorce, adoption, autism, disabilities, anxiety): only if real titles fit,
  written gently, with sources from pediatric or child-psychology organizations. Otherwise skip and log.
- Link every new page from the right hub page (/bible-story-books-for-kids/, /christian-childrens-books/,
  /bedtime-stories-for-kids/, /nature-books-for-kids/, /childrens-books-about-kindness/, /coloring-books-for-kids/)
  and add them to the "Find books by topic" section and the sitemap.

## Bible story pages (under /bible-stories/, hub = /bible-story-books-for-kids/)
Main keywords from the spreadsheet (US monthly searches):
- bible stories for kindergartners 22.2K (make this its own page: /bible-stories-for-kindergarten/)
- childhood bible stories 18.1K (fold into the hub page as a supporting term if it doesn't fit a page)
- Joseph 9.9K + 2.4K · Christmas / Jesus' birth 5.4K + 1.9K · Elijah 4.4K · Moses 4.4K · Abraham 4.4K
- Noah / Noah's ark 3.6K + 720 · David and Goliath 2.9K + 3.6K · Samson (and Delilah) 3.6K + 2.9K + 720
- Lazarus 3.6K · Jacob 2.9K · Easter 2.9K · Daniel 2.4K · Job 2.4K · Ruth 1.9K + 2.4K · Paul 2.4K
- Zacchaeus 1.9K · Adam and Eve 1.9K · Esther 1.9K · Samuel 1.9K · Jonah and the whale 1.6K + 720
- Cain and Abel 1.6K · King David 1.6K · Enoch 1.3K · creation 1K · prodigal son 1K · Jericho 1K
- Shadrach, Meshach and Abednego 880 · Deborah 880 · Joshua 720
- Topic pages: bible stories about forgiveness 880 · bible stories about faith / trusting God 880 + 590 ·
  short bible stories 720 · bible stories in order 590 · bedtime stories from the bible 1K (put this one under
  /bedtime-stories-for-kids/bible/)
URL pattern: /bible-stories/noahs-ark/, /bible-stories/david-and-goliath/ and so on. KJV only.

## Seasonal and holiday children's books (only if 4+ titles fit)
christmas childrens books 9.9K · halloween childrens books 6.6K · childrens books about fall 3.6K ·
thanksgiving · easter childrens books 1.9K · valentines day 1.9K · winter 1.6K · pumpkins 1.3K
(Christian families: a Halloween page should be written respectfully, e.g. "fall and harvest books"; Maurice
is a Christian author, log the choice.)

## Animal and nature topics (only if 4+ titles fit)
childrens books with animals 4.4K · dinosaurs 5.4K · cats 3.6K · dogs 2.9K · dragons 2.9K · horses 1.3K ·
ocean 1K · space 2.4K · science 2.9K · unicorn 1K · bugs/butterflies/frogs if titles fit

## Feelings and character topics (only if 4+ titles fit)
childrens books on sharing 2.4K · respect 1K · empathy 1.3K · feelings 1.9K · anxiety 2.9K · grief / death
2.4K + 2.9K · divorce 1.6K · adoption 1.3K · autism 1.9K · disabilities 1K

## Reading-style pages (only if they can be written honestly)
read aloud childrens books 6.6K · childrens books series 22.2K (only for Maurice's real series, e.g. titles
with "Volume" in them) · funny childrens books 2.4K · childrens books poetry 4.4K · nonfiction 6.6K ·
short bedtime stories for kindergarteners 6.6K · 5 minute bedtime stories 1.6K · bedtime stories for
preschool 6.6K · coloring books preschool 6.6K · coloring books for teens 1K · christmas / easter coloring books

## At the end
Update docs/keyword-plan.md, docs/qa.md and docs/fact-check.md (independent fact-check sub-agents again for
every new page). Final report, 5 lines max: how many new pages, which were skipped and why, checks passed,
images needed, and the one thing Maurice must do next.
