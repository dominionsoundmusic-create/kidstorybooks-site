# Fact-check A: bedtime, Bible story and Christian pages

Checked 2026-11-12 by an independent sub-agent that did not write the pages. I read the `<main>` text and JSON-LD of the built HTML in dist/.

**How the checks were done**
- **Research claims:** I used WebSearch, limited to each organization's own domain. The sandbox blocks opening the sites themselves, so a verdict of SUPPORTED means a search result from that organization's domain stated the claim. I did not open the full pages.
- **Bible references:** I checked them against my own knowledge and against en_kjv.json, looking for a key word in each cited chapter.
- **KJV quotations:** I compared each one word for word with en_kjv.json.
- **Book claims:** I compared them with data/books.json (220 books; 65 in the christian category).

## 1. /bedtime-stories-for-kids/

| # | Claim (short quote) | Source cited | Verdict | Note |
|---|---|---|---|---|
| 1 | Bedtime routine = "same calm steps, in the same order, every night in the hour before lights out"; reading is one of the most common steps, with bath and brushing teeth | Mindell & Williamson 2018 (PMC6587181) | SUPPORTED | PMC results describe the routine as caregiver-directed activities "every night in the hour before lights out" and name bath, brushing teeth and reading as the core activities. |
| 2 | "A 2018 review... the more often families kept a routine like this, the better their children tended to sleep" | Mindell & Williamson 2018 | SUPPORTED | The review reports a dose-dependent link between routine and sleep. The data is largely observational, and the page's wording ("tended to") is appropriately careful. |
| 3 | Bonding and social-emotional benefits are "ideas still being studied, not proven facts" | Mindell & Williamson 2018 | SUPPORTED | Search summaries say the review presents these as hypotheses. |
| 4 | Reach Out and Read is "a national early literacy group that works through pediatricians" | Reach Out and Read | SUPPORTED | |
| 5 | ROR says children read to more often have "stronger language and listening skills and stronger bonds" | Reach Out and Read, Child Development | SUPPORTED (search) | ROR pages tie reading aloud to language/literacy skills and emotional closeness. "Listening" was not stated word for word, but it falls within "language". |
| 6 | AAP order: "brush teeth, read a favorite book or two, then go to bed" | AAP HealthyChildren, Brush Book Bed | SUPPORTED | The URL and title match the real page. |
| 7 | "The AAP advises no screens in the hour before bed and keeping TVs, tablets and phones out of children's bedrooms" (tip and FAQ) | AAP HealthyChildren, Healthy Sleep Habits | SUPPORTED (search) | HealthyChildren.org: "turn off all screens at least 60 minutes/1 hour before bedtime"; it also recommends keeping devices out of the bedroom. The URL and title match the real page (the live URL uses capital letters in the slug; the lowercase version normally resolves). |
| 8 | "CDC says children ages 3 to 5 need 10 to 13 hours of sleep in every 24 hours, counting naps" | CDC, About Sleep | SUPPORTED | The URL matches the real CDC page. |
| 9 | "That is a lot more than most adults get" | none | SUPPORTED (general knowledge) | CDC recommends 7+ hours for adults. This is common knowledge, and nobody would dispute it. |
| 10 | "Young children learn from hearing a story many times" | ZERO TO THREE | SUPPORTED | ZTT: "young children need to hear the same story many times to fully understand it." |
| 11 | "Reading every night matters more than reading for a long time" / FAQ: "A five-minute story read every night does more good than a long one read once in a while" | none | CANNOT VERIFY | No source on the page says this. The routine review is about how consistent the routine is, not how long the reading lasts. It is worded as a fact. |
| 12 | FAQ: "Most families read for a few minutes up to about half an hour" | none | CANNOT VERIFY | It reads like a statistic, but no source is given. |
| 13 | "These titles have night, moon, stars, lullabies or sleep in their names." | data/books.json | NOT SUPPORTED | 3 of the 11 books on the shelf do not: **Felix the Flashlight: A Story of Shining Bright**, **The Owl Who Loved the Day**, **The Nocturnal Friend: Oliver's Brightest Day** ("nocturnal" is close to night, but none of the listed words appears). |
| 14 | Psalm 4:8 KJV quotation | KJV | SUPPORTED | Matches word for word. |
| 15 | Book category labels (Children's stories / Christian) | books.json | SUPPORTED | Spot-checked; they match. |

## 2. /bible-story-books-for-kids/

| # | Claim (short quote) | Source cited | Verdict | Note |
|---|---|---|---|---|
| 1 | "Noah, Jonah, David and Moses are some of the first Bible stories many children hear" | none | CANNOT VERIFY | A low-risk general statement, but no source is given. |
| 2 | ZTT "says young children learn through repetition and need to hear the same story many times"; "Adults may tire of a book long before a child does" | ZERO TO THREE, 12 to 24 Months | PARTLY | ZTT says both things word for word. However, the cited page is about **12 to 24 month olds**, and this page applies it to 3 and 4 year olds. |
| 3 | CDC milestones are "things most children (about three out of four) can do by each age" | CDC milestone pages | SUPPORTED | CDC: milestones are set where at least 75% of children show them. |
| 4 | By 3: asks "who, what, where, why" questions; keeps up a short back-and-forth talk | CDC Milestones by 3 Years | SUPPORTED | CDC: "at least two back-and-forth exchanges". The URL matches. |
| 5 | By 4: "can tell what comes next in a story they know well" | CDC Milestones by 4 Years | SUPPORTED | CDC lists this as a cognitive milestone. The URL matches. |
| 6 | By 5: "tell a story with at least two events and answer simple questions about a book" | CDC Milestones by 5 Years | SUPPORTED | Both appear in the CDC 5-year list. The URL matches. |
| 7 | Reading Rockets notes "research shows [dialogic reading] builds oral language, vocabulary and understanding" | Reading Rockets, Tutoring Strategies for Preschool and Kindergarten | PARTLY | Reading Rockets does report positive effects of dialogic reading on oral language, but the search found it on a different Reading Rockets page, **"Preschool Language and Literacy Practices"** (/topics/preschool-and-child-care/articles/preschool-language-and-literacy-practices). The cited Tutoring Strategies page is real (the URL matches its title), but the search snippets did not show it discussing dialogic reading research. "Understanding" (comprehension) is not clearly supported. |
| 8 | List: Creation Gen 1-2; Noah Gen 6-9; Babel Gen 11; Baby Moses Ex 2; Red Sea Ex 14; David and Goliath 1 Sam 17; Elijah and widow's son 1 Kings 17; Jonah 1-2; birth of Jesus Luke 2; Jesus and the children Mark 10 | Bible | SUPPORTED (all 10) | Each chapter was confirmed in the KJV JSON (key words such as ark, Babel, "ark of bulrushes", Goliath, widow, fish, manger and "little children" appear in the cited chapters). |
| 9 | FAQ: "baby Moses in the basket" | Bible | SUPPORTED (minor) | KJV Exodus 2:3 says "ark of bulrushes". "Basket" is the usual plain-English description. This is not an error. |
| 10 | "Titles named after a Bible story, person or holy day, in Bible order" | books.json | SUPPORTED | The order runs Genesis to Easter. The Loving Father (a Luke 15 parable) is placed correctly before Easter. |
| 11 | 2 Timothy 3:15 KJV quotation | KJV | SUPPORTED | Matches word for word. |
| 12 | Topic card "Noah, Jonah, David, Moses and more, told for young readers" (also appears on other pages) | books.json | PARTLY | "Told for young readers" describes who the books are written for, which the titles and the category ("christian") do not state. The risk is low on a children's book site, but strictly it goes beyond the data. |
| 13 | FAQ: "Kid Story Books does not label books by age, because the titles do not say an age" | books.json | SUPPORTED | |

## 3. /christian-childrens-books/

| # | Claim (short quote) | Source cited | Verdict | Note |
|---|---|---|---|---|
| 1 | "Sixty-five Christian children's books"; "All 65 Christian books" | books.json | SUPPORTED | 65 books are in the christian category. |
| 2 | "That is where much of a child's faith is shaped." followed by "Church leaders agree." | Barna | PARTLY | Barna says clergy rank *parents as most responsible* for faith formation. That is not the same as saying faith is mostly shaped at home, so "agree" stretches it. |
| 3 | Barna/Cardus: "nearly all Protestant pastors and Catholic priests ranked parents first, ahead of the church" | Barna, Who Is Responsible... | SUPPORTED | 99% of Protestant pastors and 96% of Catholic priests ranked parents first; the church came second. The URL matches. |
| 4 | "In an earlier Barna survey, most parents of children under 13 said that job was theirs, too" | Barna, Parents Accept Responsibility... | SUPPORTED | 85% of parents of children under 13. The URL matches. |
| 5 | Pew: "A religious upbringing often leads to a religious adulthood, though not always" | Pew 2016 | SUPPORTED | Pew: a religious upbringing is linked to retention but is "no guarantee". |
| 6 | Pew: adults whose parents talked about faith a lot were more likely to keep their parents' faith | Pew 2016 | SUPPORTED | Pew states this almost word for word. The URL matches. |
| 7 | Pew 2020 teens report listed as a source | Pew 2020 | N/A | The source is real and the URL matches, but no sentence on the page draws on it. Either cite it for a claim or drop it. |
| 8 | "NAEYC... tells families to reread children's favorites" | NAEYC, Fall in Love with Reading | SUPPORTED | Tip 5 is about rereading familiar stories. The URL matches. |
| 9 | "A second reading is when kids start asking questions." | NAEYC (by placement) | NOT SUPPORTED | NAEYC says rereading lets children "absorb information over time and... master the whole story". It does not say questions start on the second reading. The page presents this as a fact sitting next to the NAEYC citation. |
| 10 | Names-of-God group, prayer and thanks titles, verse-in-title titles | books.json | SUPPORTED | All titles exist. Note that the copy changes the case or punctuation of some titles: "Jehovah Shalom" (actual: JEHOVAH-SHALOM), "El Shaddai" (EL SHADDAI), "Elohim The Creator" (ELOHIM). That is cosmetic, not a factual error. |
| 11 | "Faith stories with fun characters. Franklin's Leap of Faith, Ernie the Eraser's Gift of Grace..." | books.json | PARTLY (low risk) | "Fun characters" is a mild judgment of quality. "Faith stories" is supported by the titles plus the Christian category. |
| 12 | FAQ 2-3 yr olds: "Short titles like My Heart Is Happy: A Little Book of God's Blessings fit this kind of reading" | books.json | NOT SUPPORTED | This implies the book is short and suits 2 and 3 year olds. Nothing in books.json gives a length or an age. "A Little Book" is in the title, but that does not establish age fit. |
| 13 | FAQ 6-8 yr olds: "The Jehovah Jireh, Jehovah Rapha and El Shaddai books are examples" | books.json | PARTLY | It is true that they are built around one name of God. Placing them under a question about 6 to 8 year olds implies an age fit that the data does not give. |
| 14 | "Seeking First: Matthew 6:33 and The Prayer of Salvation: Romans 10:9-10 name a verse right on the cover" | books.json | SUPPORTED | The verse is in the title, so it is on the cover. |
| 15 | "Maurice Johnson's Amazon author page lists every Kid Story Books title in one place, with the formats Amazon has for each book" (all three pages) | none | CANNOT VERIFY | I could not open Amazon. Author pages do not always list every title, especially ones published under a publisher name. |
| 16 | Deuteronomy 6:7 KJV quotation | KJV | SUPPORTED | Matches word for word. |
| 17 | Prayer example "like you did for Noah" | Bible | SUPPORTED | It is consistent with Genesis 6 to 9. |

No invented reviews, ratings, awards, sales figures or testimonials were found on any of the three pages. The JSON-LD on these pages has no Book descriptions or ratings (ItemList only).

## Must fix

1. **Bedtime, shelf intro (NOT SUPPORTED):** "These titles have night, moon, stars, lullabies or sleep in their names." This is false for Felix the Flashlight, The Owl Who Loved the Day and The Nocturnal Friend. Suggested wording: "These titles have night, moon, stars, lullabies, sleep or nighttime things such as owls, fireflies and flashlights in their names." Or remove those three books from the shelf.
2. **Christian, tips (NOT SUPPORTED):** "A second reading is when kids start asking questions." Suggested wording: "NAEYC, the national early childhood group, tells families to reread children's favorites, because hearing a story again helps a child take it in and master the whole story."
3. **Christian, FAQ 2-3 year olds (NOT SUPPORTED):** "Short titles like My Heart Is Happy... fit this kind of reading." Suggested wording: "A title such as My Heart Is Happy: A Little Book of God's Blessings is about God's blessings; check the book's Amazon page for its length before you buy."
4. **Bible page, dialogic reading (PARTLY):** Re-cite to Reading Rockets "Preschool Language and Literacy Practices" (https://www.readingrockets.org/topics/preschool-and-child-care/articles/preschool-language-and-literacy-practices), or confirm that the Tutoring Strategies page says it. Change "builds oral language, vocabulary and understanding" to "builds oral language and vocabulary".
5. **Bible page, ZERO TO THREE (PARTLY):** The source is about 12 to 24 months. Suggested wording: "ZERO TO THREE, a national early childhood group, says even toddlers learn through repetition and need to hear the same story many times to fully understand it." Or cite an age-appropriate source.
6. **Bedtime, unsourced reading-length claims (CANNOT VERIFY):** Change "Reading every night matters more than reading for a long time" and "A five-minute story read every night does more good than a long one read once in a while" to opinion or advice wording, for example: "A short story read every night keeps the routine going, and the routine is what helps." Change "Most families read for a few minutes up to about half an hour" to "Many families read for a few minutes; some read longer."

## Should fix (lower risk)

- **Christian:** "Church leaders agree." Change to "Church leaders put parents first, too."
- **Christian FAQ 6-8:** Reword so it does not imply the books fit that age, for example: "Books built around one name of God, such as the Jehovah Jireh and Jehovah Rapha books, give an older child something to look up."
- **Christian sources:** The Pew 2020 teens source is not used by any sentence. Cite it or drop it.
- **All pages:** "Amazon author page lists every Kid Story Books title". Change to "Maurice Johnson's Amazon author page shows his books in one place."
- **Topic card:** "told for young readers". Consider "Noah, Jonah, David, Moses and more".
