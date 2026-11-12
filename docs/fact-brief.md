# Playbook 2.0, Prompt 1: Client fact brief (Kid Story Books)

Source of truth: INTAKE.md (wins over everything), then SERVICES.md, data/books.json and the
old site (docs/old-site/). Built 2026-11-12.

| Item | Value | Status |
|---|---|---|
| Official name on site | Kid Story Books | Confirmed |
| Publisher on the books | Dominion Publishing | Confirmed |
| Author on every book | Maurice Johnson | Confirmed |
| Parent company | Dominion Digital Group | Confirmed |
| Owner location | East Texas (Big Sandy, Texas 75755). No street address on the site. | Confirmed, address DO NOT DISPLAY |
| Primary category | Children's book author site; sends readers to Amazon. No cart, no checkout. | Confirmed |
| Services / "products" | 220 books in 6 categories (childrens 71, christian 65, nature 34, cookbooks 32, coloring 9, teens 9) | Confirmed (data/books.json) |
| Book facts we know | Title, category, price only. Summaries, ages, page counts, lessons UNKNOWN unless the title says so. | Confirmed limit |
| Formats | Mostly paperback; do not promise a format for a specific book | Confirmed limit |
| Service area | Not applicable (books ship through Amazon). No area pages. | Confirmed |
| Phone | UNKNOWN | Deferrable (site points to Facebook Message button) |
| Email | UNKNOWN | Deferrable. The old privacy policy listed an email; INTAKE says UNKNOWN, so it is removed. |
| Hours | Not applicable | n/a |
| Primary call to action | Buy on Amazon (each book: https://www.amazon.com/dp/ASIN) | Confirmed |
| Secondary call to action | Browse all 220 books / Amazon author page https://www.amazon.com/author/dominionpublishing | Confirmed |
| Brand colors | Sunny yellow #FFC93C, sky blue #3BA7E6, coral #FF6B5B, dark navy #16213E text | Confirmed (CLAUDE.md design rules) |
| Logo | Text logo "Kid Story Books" | Confirmed |
| Favicon | favicon.svg / favicon.ico / apple-touch-icon.png from old site | Confirmed |
| Typography | Rounded, friendly, self-hosted woff2 (Nunito, SIL OFL) | Decision (docs/decisions.md) |
| Business story | Christian author; 65 christian titles; publishes under Dominion Publishing | Confirmed |
| Reviews / awards / sales | UNKNOWN. None may appear. Old testimonials were made up and are removed. | Confirmed: none |
| Facebook | https://www.facebook.com/bestkidstorybooks | Confirmed |
| Instagram | https://www.instagram.com/bestkidstorybooks/ | Confirmed |
| TikTok | https://www.tiktok.com/@bestkidstorybooks | Confirmed |
| Pinterest, YouTube | UNKNOWN, left off | Deferrable |
| Google Business Profile | none | n/a |
| Forms, maps, review widgets | none (no contact form by instruction) | Confirmed |
| Analytics | Old site carried GA4 G-EKXVSCT3S2; CLAUDE.md says "none yet". See decisions.md D-07. | Contradictory, resolved conservatively |
| Domain / canonical | https://kidstorybooks.com/ (trailing-slash URLs) | Confirmed |
| Required pages | SERVICES.md page plan (13 routes + 404) | Confirmed |
| Must not appear | Invented summaries, ages, ratings, reviews, awards, testimonials; trademarked characters; custom storybook offer; non-KJV Scripture quotes | Confirmed |
| Footer quote | "I believe the unbelievable, I receive the impossible, because it's doable." (Jesse Duplantis) plus the disclaimer, exact | Confirmed |
| Photos / video | No real photos supplied. No video. Book covers from Amazon are the main imagery. | Deferrable (docs/image-list.md) |

## Questions that need Maurice (none block the preview)
1. Custom storybooks: the Facebook bio offers to "create a storybook for you to publish on Amazon". Price, process and terms are unknown, so the site does not mention it. Do you want a page for it?
2. Analytics: keep the old GA4 ID G-EKXVSCT3S2? (See decisions.md D-07.)
3. A public email address for the privacy policy, or keep "message us on Facebook"?
4. Pinterest and YouTube links, if you want them shown.

## Launch blockers
None for the preview. Going live needs Maurice's approval of the look (merge `build` to main is his call).
