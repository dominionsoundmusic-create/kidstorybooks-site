# kidstorybooks-site

Kid Story Books (kidstorybooks.com): Maurice Johnson's children's books, sold on Amazon.

Static site. Pages are in `src/pages/` (Jinja + YAML front matter), shared data in `src/data/site.json`
and `data/books.json` (all 220 books). `python3 build.py` writes `dist/`, which is committed and is what
Netlify publishes (`netlify.toml`: `publish = "dist"`, no build command). Needs Python 3 with Jinja2,
PyYAML, Pillow and openpyxl; the browser checks need Node with Playwright.

Checks (all must pass before merging):

    python3 build.py && python3 tools/check.py && python3 tools/check_kjv.py \
      && python3 tools/similarity.py && python3 tools/contrast.py \
      && node tools/shots.js && node tools/functional.js

Docs: `docs/qa.md` (results and handoff), `docs/decisions.md`, `docs/fact-check.md`, `docs/keyword-plan.md`,
`docs/image-list.md` (photos to make), `docs/fact-brief.md`, `docs/architecture.md`.
The old hand-written site is kept in `docs/old-site/`. Never drag-and-drop deploy.
