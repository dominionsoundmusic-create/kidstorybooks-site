# Fact-check B: kindergarten, nature, kindness pages

Checker: independent sub-agent (did not write the pages). Date: 2026-11-12.
Method: the readable text in `<main>` was pulled from the built HTML in dist/. Research claims were checked with WebSearch (standard mode), limited to each organization's own domain. **Every verdict comes from search results. The source pages themselves were not opened** (the sandbox blocks WebFetch). Book claims were checked against data/books.json (title, category, price only). Scripture was checked against the KJV text from memory. tools/check_kjv.py is the formal check for that.

Source URLs: all 14 cited URLs came back in domain-limited search results under the exact title the page cites. They look like the real pages.

## /picture-books-for-kindergarten/

| # | Claim (short quote) | Source cited | Verdict | Note |
|---|---|---|---|---|
| 1 | "At five and six, children can follow a plot with a problem and a fix, guess why a character feels... remember a story from one day to the next" | none directly (CDC 5-year page is listed) | PARTLY | CDC 5 yrs: tells a story with at least 2 events and says what comes next in a well-known story. The rest is general and fair, but no source is attached. |
| 2 | Reading Rockets suggests "an interesting picture book every day, along with predictable books... and information books with lots of colorful photos" for this age | Reading Rockets (Repeated Interactive Read Alouds; Tutoring Strategies) | PARTLY | Search results support a daily read-aloud of a sophisticated picture book plus predictable books. The Tutoring Strategies page puts information books with photographs at "around early first grade", not kindergarten. |
| 3 | Ohio State: five books a day, about 1.4 million more words by kindergarten than children never read to | Ohio State News (2019) | SUPPORTED | news.osu.edu: about 1.48M words by age 5 vs 4,662. This is a modeled estimate. |
| 4 | "The lead researcher said the real gap is likely even bigger" | Ohio State News | SUPPORTED | Logan called the estimate conservative. |
| 5 | Reading Rockets: dialogic reading "builds oral language, vocabulary and understanding" | Reading Rockets (Tutoring Strategies) | PARTLY | Reading Rockets supports oral language and vocabulary gains, but on its own Dialogic Reading and Preschool Language pages, not the cited one. "Understanding" was not confirmed. |
| 6 | CDC suggests asking "What is happening in the picture?" / "What do you think will happen next?", then asking for more details | CDC Milestones by 5 Years | SUPPORTED | Found on cdc.gov's milestone guidance. |
| 7 | NAEYC tells families to reread favorites; "each time, your child notices something new" | NAEYC Fall in Love with Reading | SUPPORTED (paraphrase) | NAEYC: rereading lets children "absorb information over time" and master the story. |
| 8 | "Teachers often choose a handful of new words to explain while reading" | Reading Rockets (Repeated Interactive Read Alouds) | SUPPORTED | The Text Talk approach briefly defines a few target words. |
| 9 | "By age 5, most children can tell a story with at least two events" | CDC | SUPPORTED | CDC milestone at 5 yrs ("most" = 75%+). |
| 10 | "Do sharks really have teeth that fall out?" (sets up an info-book search) | none | SUPPORTED (general fact) | Sharks shed and replace teeth all their lives. |
| 11 | Nature page "has life cycle books on frogs, ladybugs, sea turtles and more" | books.json | SUPPORTED | These titles exist in the nature category. |
| 12 | Animal shelf: "titles with an animal in the name" | books.json | SUPPORTED | All 18 ASINs exist, all childrens category, and each title names an animal. |
| 13 | Kofi and Kwame, The Butterfly Sisters, The New Little Sister listed as "stories about brothers, sisters" | books.json | SUPPORTED (title only) | The section is headed "friendship and family" and the books are described by title only. Fine. |
| 14 | FAQ: kindness page has "titles about sharing, the Golden Rule and feelings" | books.json | SUPPORTED | |
| 15 | "Amazon author page lists every Kid Story Books title... with the formats Amazon has for each book" | none | CANNOT VERIFY | It is not confirmed that all 220 titles appear on the author page. This shared block is on all three pages. |

## /nature-books-for-kids/

| # | Claim (short quote) | Source cited | Verdict | Note |
|---|---|---|---|---|
| 1 | "Thirty-four nature and science books... including three with Spanish titles" | books.json | SUPPORTED | 34 in the nature category. The 3 Spanish titles are confirmed. |
| 2 | NAEYC describes young children "as active scientists from the day they are born" | NAEYC Looking at the World (2019); Nurturing the Scientist | SUPPORTED by NAEYC, WRONG CITATION | The wording is from NAEYC's "More Than a Foundation: Young Children Are Capable STEM Learners" (Young Children, Nov 2017). It was not found in the May 2019 column. |
| 3 | NAEYC says being a born scientist "does not mean a child can do it all alone"; adults help | same | PARTLY | This is likely the same Nov 2017 article. It was not confirmed in either cited source. |
| 4 | Frog stages "egg, tadpole, froglet, frog" | none | SUPPORTED (general fact) | |
| 5 | Life cycle book titles listed; "Many have 'Ages 3-5' in the title" | books.json | SUPPORTED | |
| 6 | Bamboo / Ivy / Redwood books "pair a plant with a character trait" | books.json | SUPPORTED | Based on the title wording. |
| 7 | Reading Rockets "sorts science books for kids into several kinds, from narrative... to hands-on books that teach a skill... like a field guide" | Reading Rockets Five Kinds of STEM-themed Nonfiction | SUPPORTED | Five kinds. Active nonfiction includes field guides. |
| 8 | Reading Rockets "also suggests information books with lots of colorful photos or pictures to help young children build knowledge" | Reading Rockets Repeated Interactive Read Alouds | CANNOT VERIFY / PARTLY | Not found on the cited page. A Reading Rockets tutoring page mentions information books with photographs, for about early first grade. |
| 9 | AAP: children play harder outdoors and need chances to play outside every day | HealthyChildren.org Playing Outside | SUPPORTED | |
| 10 | AAP links outdoor time with "better motor skills and a lower risk of obesity and nearsightedness" | same | PARTLY | Obesity and myopia were confirmed. "Motor skills" was not in the results. |
| 11 | "studies that found children who spent more time exploring nature had better learning outcomes" | same | SUPPORTED | |
| 12 | NAEYC: model curiosity, "I wonder what would happen..." | NAEYC Nurturing the Scientist | SUPPORTED | |
| 13 | NAEYC: do not correct a child's science ideas right away; ask how they could find out | same | SUPPORTED | |
| 14 | Genesis 1:1 "In the beginning God created the heaven and the earth." | KJV | SUPPORTED | Matches the KJV word for word. |
| 15 | FAQ: "Ocean animals on this shelf include The Lifecycle of a Salmon, Lifecycle of a Sea Turtle and Lifecycle of a Penguin" | books.json | PARTLY | Sea turtle: yes. Penguins feed at sea: acceptable. Salmon hatch and spawn in fresh water and spend their adult years in the ocean, so "ocean animal" is loose. No ocean-titled book exists. |
| 16 | FAQ: "Several titles here say Ages 3-5 right in the title" | books.json | SUPPORTED | |
| 17 | Author page block (same as kindergarten #15) | none | CANNOT VERIFY | |

## /childrens-books-about-kindness/

| # | Claim (short quote) | Source cited | Verdict | Note |
|---|---|---|---|---|
| 1 | Making Caring Common (Harvard GSE) suggests using stories to build empathy: ask about more than one character, not just the hero; with older kids, ask how they would feel in that character's place | MCC How to Use Stories... | SUPPORTED | |
| 2 | MCC: make caring a priority; kind matters as much as happy; "be kind and be happy" | MCC 7 Tips | SUPPORTED | MCC's wording: "the most important thing is that you're kind and that you're happy." |
| 3 | CASEL "includes learning to understand and manage emotions, to feel and show empathy for others, and to build healthy relationships" | CASEL What Is SEL? | SUPPORTED | CASEL's definition says "supportive relationships", which is close enough. |
| 4 | "CASEL, a leading group in that field" | CASEL | SUPPORTED | |
| 5 | ZERO TO THREE suggests asking which child looks mad or afraid | ZERO TO THREE Books About Feelings for Babies and Toddlers | SUPPORTED by ZTT, possibly a different page | The search tied the prompt to ZTT's toddler social-emotional guidance (24-36 Months page). The cited page appeared in the same results, but the exact quote was not confirmed on it. |
| 6 | Books on kindness "Chosen because the title names kindness, sharing, love or a feeling" | books.json | SUPPORTED | All 8 ASINs exist with the listed categories. |
| 7 | Barnaby Bear... Winter Share and Bountiful Bramble "have sharing right in the title" | books.json | SUPPORTED | |
| 8 | Conscious Discipline, Worry Cloud, Seed of Worry "all name a feeling in the title" | books.json | SUPPORTED | |
| 9 | "Sharing God's Love and We Love Because He First Loved Us... also connect kindness with faith" | books.json | SUPPORTED (title-level) | Both are in the Christian category and their titles mention love. This is a mild inference, but acceptable. |
| 10 | Ephesians 4:32 KJV quote | KJV | SUPPORTED | Word for word. |
| 11 | Matthew 7:12 KJV quote | KJV | SUPPORTED | Word for word. |
| 12 | Author page block | none | CANNOT VERIFY | |

No invented reviews, ratings, awards, sales figures or testimonials were found on any of the three pages. No book plot, lesson, age range (beyond "Ages 3-5" in titles), page count or format claims were found.

## Must fix

1. **Nature, NAEYC "active scientists from the day they are born" (#2, #3):** wrong citation. Add the source "NAEYC, More Than a Foundation: Young Children Are Capable STEM Learners (Young Children, Nov 2017)", https://www.naeyc.org/resources/pubs/yc/nov2017/stem-learners. Check the "not alone" sentence against that article, or cut it.
2. **Kindergarten #2 and Nature #8, Reading Rockets "information books with lots of colorful photos":** not supported for kindergarten on the cited pages. Suggested wording: "Reading Rockets suggests reading a rich picture book aloud every day, along with predictable books that repeat lines. As children grow, add true information books with photos about the world." On the nature page, drop the "also suggests..." sentence or attribute it to the Tutoring Strategies page with the first-grade framing.
3. **Kindergarten #5, dialogic reading:** cite Reading Rockets "Dialogic Reading: An Effective Way to Read Aloud with Young Children" (https://www.readingrockets.org/topics/early-literacy-development/articles/dialogic-reading-effective-way-read-aloud-young-children), and change "builds oral language, vocabulary and understanding" to "builds oral language and vocabulary".
4. **Nature #10, AAP "better motor skills":** not confirmed. Use "It links more outdoor time with a lower risk of obesity and nearsightedness..." or confirm motor skills on the page first.
5. **Nature #15, ocean FAQ:** say "Animals that live in or depend on the ocean include Lifecycle of a Sea Turtle and Lifecycle of a Penguin. Salmon spend their adult years at sea: see The Lifecycle of a Salmon."
6. **Kindness #5, ZERO TO THREE:** confirm the quote is on the cited page, or add/replace the source with ZERO TO THREE "24-36 Months: Social-Emotional Development" (https://www.zerotothree.org/resource/24-36-months-social-emotional-development/). Also note that this tip is aimed at toddlers.
7. **All three pages, author page block:** "lists every Kid Story Books title in one place" cannot be verified. Suggested wording: "Maurice Johnson's Amazon author page shows his books in one place, with the formats Amazon offers."
