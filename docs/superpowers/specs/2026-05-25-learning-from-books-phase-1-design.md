# Learning From Books — Phase 1 Design

**Date**: 2026-05-25
**Status**: Approved for implementation planning
**Project codename**: Learning From Books — A System That Improves With Your Feedback
**Scope**: Phase 1 only (foundation + first book end-to-end + manual feedback)

---

## 1. Context & motivation

The user reads classic foundational books in systems thinking, neuroscience, psychology, economics, philosophy, history, strategy, and productivity. Manually building a NotebookLM-powered companion for each book is valuable but repetitive (proven by the existing Laws of Human Nature workflow).

The goal is a productized, repeatable system:

- Each book gets a hub page with summary, slides, audio overview, infographics, and curated research
- Readers (including future-self) submit feedback by email
- The system improves over time without manual orchestration
- The whole thing runs on free tiers wherever possible

Phase 1 codifies the manual pattern and ships a working public site. Phases 2–4 progressively automate it.

## 2. Goals & non-goals

### Phase 1 goals

1. Public GitHub Pages site at a stable URL hosting the Laws of Human Nature companion
2. Repeatable per-book template (folder layout, metadata schema, page structure) any new book can plug into
3. Gmail-based feedback intake with plus-addressing routing
4. Manual feedback workflow documented end-to-end (so Phase 2 has a clear spec to automate)
5. Zero recurring cost (free tiers only)
6. Zero Anthropic API key required for the autonomous parts (when they ship in Phase 2)
7. Fork-ready architecture: anyone can copy the repo and run their own book site by editing only config files (see §15)

### Non-goals (deferred to later phases)

- Phase 2: autonomous IMAP polling, Gemini intent classification, auto-commit, SMTP reply
- Phase 3: automated PDF discovery for a given book title
- Phase 4: auto-population of curated research (YouTube author talks, blog posts)
- Per-chapter infographics for Laws 2–18 (only Law 1 ships in Phase 1)
- Per-chapter slide URLs for all 18 chapters (only Law 1 required in Phase 1 to prove the pattern)

## 3. The four phases (system context)

Phase 1 is the foundation; phases 2–4 plug into it.

| Phase | Scope | Status |
|---|---|---|
| **1 · Foundation** | Repo, MkDocs site, GitHub Pages deploy, per-book template, manual feedback workflow, Laws of Human Nature seed | This spec |
| **2 · Closing the loop** | IMAP polling, Gemini intent classifier, NotebookLM/Nano-Banana dispatch, auto-commit, SMTP reply | Future spec |
| **3 · Book discovery** | Given a title, agent locates and ingests PDF autonomously | Future spec |
| **4 · Curated research** | YouTube talks, blog posts, academic commentary aggregated per book | Future spec |

## 4. Architectural decisions

Each decision was brainstormed; the chosen option is recorded here with the reasoning.

| Decision | Chosen | Rejected alternatives | Why |
|---|---|---|---|
| Hosting strategy | Single GitHub repo + GitHub Pages | Per-book repo; integrate into existing dba-site Quartz wiki | One repo keeps related content together; Pages avoids new infra; storage math fits comfortably (lean approach below) |
| Storage strategy | Lean — repo holds metadata + small markdown + compressed images; heavy assets externalized | Store PDFs + audio + slides in repo | PDFs go to Google Drive, audio stays in NotebookLM, slides are Google Slides URLs. ~3 MB/book → 300+ books fit in repo's 1 GB recommended cap |
| Email routing | One Gmail with plus-addressing per book | One Gmail per book; one Gmail per category | Single account avoids Google ToS risk; plus-addressing gives deterministic routing via `Delivered-To` header — no LLM needed to identify book |
| Autonomous-loop LLM | Gemini 2.5 Flash (free tier, 1500 req/day) | Claude Haiku via Anthropic API; Claude Routines | Zero Anthropic API key; one free Google AI Studio key suffices; Max subscription stays for user's manual work |
| Automation spine | GitHub Actions cron (free, 5-min min interval) | Claude Code Routines (Pro/Max only, 15/day cap, 1-hour min interval) | Free, more responsive, integrates with existing repo, secrets storage built-in |
| Site generator | MkDocs Material | Quartz; Astro+Starlight; Jekyll | Book-shaped UX (sections = books, pages = chapters); built-in search; iframe embeds work out-of-box; small config surface |
| Flashcards | NotebookLM-hosted (link/embed) | Build static markdown Q/A; build Anki export | NotebookLM already generates these; matches the "externalize heavy artifacts" pattern |
| Per-chapter slide rendering | iframe embed of Google Slides `/embed` URL | Static PNG export per slide | iframe stays in sync with the source deck; no rebuild on slide edits; works on mobile |
| Site categories taxonomy (initial) | 8: Psychology, Systems Thinking, Neuroscience, Economics, Philosophy, History, Strategy, Productivity | Tight list of 4; freeform tags | Seeds the user's actual reading domains; can grow on demand |

## 5. Token-optimized architecture

| Job | Tool | Cost | Why |
|---|---|---|---|
| Audio overview (Deep Dive podcast) | NotebookLM | Free | Native NotebookLM output, source-grounded |
| Slide decks (condensed + detailed) | NotebookLM | Free | Exports as Google Slides URL |
| Markdown chapter summaries | NotebookLM → export | Free | Same pattern as existing Laws of Human Nature |
| Flashcards per chapter | NotebookLM Flashcards | Free | Hosted in NotebookLM, linked from chapter page |
| Infographics | Nano Banana (Gemini image) | Free | Already wired in user's plugin set |
| Curated research (YouTube, blogs) | Gemini 2.5 Flash + Firecrawl | Free tiers | Bulk scrape + summarize |
| Email feedback parsing → intent (Phase 2) | Gemini 2.5 Flash | Free (1500 req/day) | Structured output, no Anthropic key needed |
| Orchestration (route + dispatch, Phase 2) | Gemini 2.5 Flash | Free | Decision tree fits easily in Flash's capabilities |
| User's manual work (this spec, future builds) | Claude Code on Max subscription | Included in Max | Stays with user; not in autonomous loop |

Steady-state operational cost: **~$0/month** (all free tiers, no Anthropic API key required for autonomous flow).

## 6. Repository layout

The new repo (separate from dba-site) is named **`learning-from-books-system-that-improves-with-your-feedback`**.

```
learning-from-books-system-that-improves-with-your-feedback/
├── .github/
│   └── workflows/
│       └── deploy.yml              # MkDocs build + Pages deploy
├── docs/                           # MkDocs source
│   ├── index.md                    # AUTO-GENERATED master grid
│   ├── stylesheets/
│   │   └── extra.css               # book cards + slides embed
│   └── books/
│       └── laws-of-human-nature/
│           ├── .pages              # awesome-pages nav config
│           ├── book.yaml           # metadata (excluded from build)
│           ├── index.md            # book landing page
│           ├── chapters/
│           │   ├── 01-irrationality.md
│           │   ├── 02-narcissism.md
│           │   └── ...
│           ├── infographics/
│           │   ├── cover.jpg
│           │   ├── 01-start.png
│           │   └── 01-end.png
│           ├── research/
│           │   ├── author-talks.md
│           │   ├── blog-posts.md
│           │   └── academic-commentary.md
│           └── feedback/
│               └── log.md          # excluded from build
├── scripts/
│   ├── build_index.py              # books → docs/index.md
│   ├── migrate_laws_of_human_nature.py
│   └── new_book.py                 # scaffold new book skeleton
├── mkdocs.yml
├── requirements.txt
├── feedback-protocol.md
└── README.md
```

### Per-book metadata schema (`book.yaml`)

```yaml
title: "The Laws of Human Nature"
author: "Robert Greene"
year: 2018
slug: "laws-of-human-nature"
categories: [psychology, behavior, leadership]
status: "active"               # active | draft | archived
chapters_total: 18
cover: "infographics/cover.jpg"
last_updated: "2026-05-25"

# external artifact URLs (all FREE platforms)
notebooklm_url: "https://notebooklm.google.com/notebook/<id>"
notebooklm_flashcards_url: "https://notebooklm.google.com/notebook/<id>/flashcards"
audio_overview_url: "https://notebooklm.google.com/notebook/<id>/audio"
slides_condensed_url: "https://docs.google.com/presentation/d/<id>"
slides_detailed_url: "https://docs.google.com/presentation/d/<id>"
drive_pdf_url: "https://drive.google.com/file/d/<id>"

# feedback routing
feedback_email: "learningfrombooks.feedback+lawsofhumannature@gmail.com"

# per-chapter inventory (for index page indicators + nav)
chapters:
  - num: 1
    title: "The Law of Irrationality"
    slug: "01-irrationality"
    slides_url: "https://docs.google.com/presentation/d/<id>"
  - num: 2
    title: "The Law of Narcissism"
    slug: "02-narcissism"
    slides_url: "https://docs.google.com/presentation/d/<id>"
  # ...18 total
```

### Per-chapter file format

```markdown
---
chapter: 1
title: "The Law of Irrationality"
slides_url: "https://docs.google.com/presentation/d/<id>"
notebooklm_section_url: "https://notebooklm.google.com/notebook/<id>#chapter-1"
key_concepts: [bias, emotion, self-awareness]
---

# Chapter 1 — The Law of Irrationality

> Short pull-quote or chapter thesis.

## Slide Deck

<div class="slides-embed">
  <iframe src="https://docs.google.com/presentation/d/<id>/embed?start=false&loop=false&delayms=3000"
          frameborder="0" allowfullscreen></iframe>
</div>

## Summary

Chapter summary (synthesized from NotebookLM).

## Study Guide

(Merged from NotebookLM-generated study guide.)

## Key Takeaways

- ...

## Listen

[Audio overview for this chapter →](<notebooklm_section_url>)
```

## 7. MkDocs configuration

`mkdocs.yml`:

```yaml
site_name: "Learning From Books"
site_description: "A System That Improves With Your Feedback"
site_url: "https://<user>.github.io/learning-from-books-system-that-improves-with-your-feedback/"
repo_url: "https://github.com/<user>/learning-from-books-system-that-improves-with-your-feedback"
repo_name: "GitHub"

theme:
  name: material
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      toggle: { icon: material/brightness-7, name: Switch to dark }
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      toggle: { icon: material/brightness-4, name: Switch to light }
  features:
    - navigation.instant
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - search.suggest
    - search.highlight
    - content.code.copy
    - toc.follow

plugins:
  - search
  - awesome-pages
  - tags

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed: { alternate_style: true }
  - attr_list
  - md_in_html
  - toc: { permalink: true }

extra_css:
  - stylesheets/extra.css

extra:
  social:
    - icon: fontawesome/solid/envelope
      link: mailto:learningfrombooks.feedback@gmail.com
      name: Send feedback

exclude_docs: |
  **/book.yaml
  **/feedback/log.md
```

### Master index (`docs/index.md`) — auto-generated

```markdown
# Learning From Books

A continuous improvement system for deep reading. Send feedback to any book's email — the system improves with your input.

<div class="book-grid">
<a class="book-card" href="books/laws-of-human-nature/">
  <img src="books/laws-of-human-nature/infographics/cover.jpg" alt="">
  <div class="card-meta">
    <h3>The Laws of Human Nature</h3>
    <p class="author">Robert Greene · 2018</p>
    <div class="tags"><span>psychology</span><span>behavior</span></div>
    <p class="status">18 chapters · updated 2026-05-25</p>
  </div>
</a>
</div>

## Browse by category

- [Psychology](tags.md#psychology)
- [Systems Thinking](tags.md#systems-thinking)
- [Neuroscience](tags.md#neuroscience)
- [Economics](tags.md#economics)
- [Philosophy](tags.md#philosophy)
- [History](tags.md#history)
- [Strategy](tags.md#strategy)
- [Productivity](tags.md#productivity)

## Request a book

Send the title + author to **[learningfrombooks.feedback+request@gmail.com](mailto:learningfrombooks.feedback+request@gmail.com)**.
```

### `scripts/build_index.py` behavior

- Walk `docs/books/*/book.yaml`
- Sort by `last_updated` descending
- Render Jinja2 template → `docs/index.md`
- Collect unique categories → write/update `docs/tags.md`
- Idempotent: re-running produces identical output if no `book.yaml` changed

### `extra.css` (key styles)

```css
.book-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1.25rem; margin: 2rem 0;
}
.book-card {
  display: block; border-radius: 12px; overflow: hidden;
  background: var(--md-default-bg-color); color: inherit;
  text-decoration: none; box-shadow: 0 2px 8px rgba(0,0,0,.08);
  transition: transform .15s, box-shadow .15s;
}
.book-card:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,.12); }
.book-card img { width: 100%; aspect-ratio: 3/4; object-fit: cover; display: block; }
.card-meta { padding: .75rem 1rem 1rem; }
.card-meta h3 { margin: 0 0 .25rem; font-size: 1rem; }
.author { font-size: .85rem; color: var(--md-default-fg-color--light); margin: 0; }
.tags { margin: .5rem 0; display: flex; gap: .4rem; flex-wrap: wrap; }
.tags span {
  background: var(--md-accent-fg-color--transparent);
  color: var(--md-accent-fg-color);
  padding: .15rem .5rem; border-radius: 4px; font-size: .75rem;
}
.slides-embed {
  position: relative; padding-bottom: 56.25%; height: 0;
  overflow: hidden; margin: 1.5rem 0; border-radius: 8px;
}
.slides-embed iframe {
  position: absolute; top: 0; left: 0;
  width: 100%; height: 100%; border: 0;
}
```

### Per-book `.pages` (awesome-pages plugin)

```yaml
title: "The Laws of Human Nature"
nav:
  - index.md
  - chapters
  - research
```

## 8. GitHub Actions deployment

`.github/workflows/deploy.yml`:

```yaml
name: Build and deploy site

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Regenerate master index
        run: python scripts/build_index.py

      - name: Build MkDocs site
        run: mkdocs build --strict

      - uses: actions/upload-pages-artifact@v3
        with:
          path: site

      - id: deployment
        uses: actions/deploy-pages@v4
```

`requirements.txt`:

```
mkdocs==1.6.1
mkdocs-material==9.5.49
mkdocs-awesome-pages-plugin==2.9.3
pyyaml==6.0.2
jinja2==3.1.4
```

One-time manual setup: GitHub repo → Settings → Pages → Source = "GitHub Actions" (not "Deploy from branch"). No `gh-pages` branch needed.

### Build latency budget (states Phase 2 expectations)

| Event | Latency |
|---|---|
| Push to `main` → Pages live | 45–90 seconds typical |
| GitHub Actions scheduled jobs | 5–30 minute drift possible at peak |
| Phase 2 feedback SLA target | Acknowledged within 1 hour, fulfilled within 4 hours |
| Phase 1 (manual) SLA target | Acknowledged within 24 hours, fulfilled within 48 hours |

## 9. Phase 1 manual feedback workflow

The manual workflow is intentional: it codifies what Phase 2 will automate.

### Feedback address pattern

`learningfrombooks.feedback+<bookslug>@gmail.com` (plus-addressing). Examples:

- `learningfrombooks.feedback+lawsofhumannature@gmail.com` → Laws of Human Nature
- `learningfrombooks.feedback+request@gmail.com` → new book request (reserved slug)
- `learningfrombooks.feedback+meta@gmail.com` → site-level feedback (reserved slug)

All deliver to one inbox; Gmail preserves the tag in the `Delivered-To` header for machine-readable routing.

### Accepted feedback intents (Phase 1 taxonomy)

| Intent | Example subject | Action |
|---|---|---|
| `more-flashcards` | "More flashcards on chapter 3" | Regenerate flashcards in NotebookLM |
| `infographic` | "Infographic for Law 7" | Generate via Nano Banana |
| `summary-rephrase` | "Make chapter 2 summary simpler" | Re-prompt NotebookLM with style hint |
| `audio-language` | "Audio overview in Hindi" | NotebookLM language switch + regenerate |
| `slide-rework` | "Condensed deck too dense" | Regenerate slides with new outline |
| `research-add` | "Found an author talk: <URL>" | Append to `research/author-talks.md` |
| `error` | "Typo in chapter 5, paragraph 4" | Fix in markdown, commit |
| `general` | freeform | Manual judgment |

### Manual workflow (7 steps, performed by the user)

1. **Receive** — Gmail notifies of new mail at `learningfrombooks.feedback+<slug>@gmail.com`
2. **Classify** — read subject + body; tag with one taxonomy intent above
3. **Act** — open NotebookLM / Nano Banana / chapter file and generate or edit the artifact
4. **Place** — commit the new/changed file under the correct subfolder of `docs/books/<slug>/`
5. **Log** — append a row to `docs/books/<slug>/feedback/log.md`:

   ```markdown
   ## 2026-05-26 — chapter-3 flashcards expanded
   - **From**: reader@example.com
   - **Intent**: more-flashcards
   - **Action**: Regenerated NotebookLM flashcards for chapter 3, updated URL in book.yaml
   - **Commit**: <sha>
   - **Reply sent**: yes
   ```
6. **Push** — `git push` → GitHub Action deploys → live in ~90 seconds
7. **Reply** — respond to the original email with a Pages URL pointing to the new artifact

### `feedback-protocol.md` (committed at repo root)

A single doc explains the above to: readers (what to send), future-self (how to act), the Phase 2 spec author (reference implementation).

Contents:
- The 8 intent types + what each triggers
- The 7-step manual workflow
- Sample email templates readers can copy
- The log format shown above

## 10. Seed migration: Laws of Human Nature

### Existing content inventory

Located in `dba-site/content/references/laws-of-human-nature/`:

| Asset | Count | Status |
|---|---|---|
| Chapter files (`law-01-…` to `law-18-…`) | 18 | Complete |
| Study guides (NotebookLM-generated) | 18 | Complete |
| Index files | 2 | Complete |
| Infographics | 2 PNGs | Only Law 1 START + END; Laws 2–18 pending |
| NotebookLM notebook | 1 | Exists, URL captured |
| Per-law slide decks (in NotebookLM) | 18 | URLs need extraction |
| Audio overview | 1 | URL needs extraction |
| Cover image | none | Generate via Nano Banana |

### Source → target mapping

```
content/references/laws-of-human-nature/
  index.md                                    → docs/books/laws-of-human-nature/index.md (rewritten as book landing)
  law-01-irrationality.md                     → docs/books/laws-of-human-nature/chapters/01-irrationality.md
  ...
  law-18-death-denial.md                      → docs/books/laws-of-human-nature/chapters/18-death-denial.md
  study-guides/law-NN-name-study-guide.md     → MERGED into matching chapter file as "## Study Guide" section
  infographics/law-01-irrationality-start.png → docs/books/laws-of-human-nature/infographics/01-start.png
  infographics/law-01-irrationality-end.png   → docs/books/laws-of-human-nature/infographics/01-end.png
```

### New files (don't exist in source)

```
docs/books/laws-of-human-nature/
  book.yaml
  .pages
  feedback/log.md
  research/author-talks.md         (stub)
  research/blog-posts.md           (stub)
  research/academic-commentary.md  (stub)
  infographics/cover.jpg           (Nano Banana generated)
```

### Migration script

`scripts/migrate_laws_of_human_nature.py` — one-shot, idempotent:

1. Read source dir from CLI arg (path to `dba-site/content/references/laws-of-human-nature/`)
2. For each `law-NN-*.md`:
   - Strip Quartz-specific frontmatter (`tags`, `category`)
   - Add MkDocs-compatible frontmatter (`chapter`, `title`, `slides_url` placeholder)
   - Read matching study guide file
   - Append as `## Study Guide` section
   - Append `## Slide Deck` section with iframe placeholder
   - Write to `docs/books/laws-of-human-nature/chapters/NN-slug.md`
3. Copy infographics, renaming (`law-01-irrationality-start.png` → `01-start.png`)
4. Generate `book.yaml` with all known metadata + URL placeholders
5. Write `.pages`, stub `research/`, empty `feedback/log.md`
6. Print summary: files written, URL placeholders that need manual fill-in

### Manual fill-in checklist (after migration script runs)

| Field | Source |
|---|---|
| `notebooklm_url` | Open existing notebook → copy URL |
| `notebooklm_flashcards_url` | NotebookLM Studio → Flashcards → copy URL |
| `audio_overview_url` | NotebookLM Studio → Audio Overview → copy URL |
| `slides_condensed_url` | Generate in NotebookLM if missing, share=anyone-with-link, copy URL |
| `slides_detailed_url` | Same, detailed version |
| `drive_pdf_url` | Upload PDF to Drive under new Gmail account, share, copy URL |
| Per-chapter `slides_url` (×18) | Extract from NotebookLM Studio per chapter — bulk task; Phase 1 requires Law 1 only |
| `cover.jpg` | Nano Banana: "Book cover, 'The Laws of Human Nature' by Robert Greene, classical philosophy aesthetic, dark indigo + gold" |
| Infographics 02–18 (×34) | Nano Banana per existing prompt template; not blocking Phase 1 |

### Fate of the dba-site wiki copy

**Chosen: Option B** — migrate to new repo, replace wiki copy with a stub linking out.

- Verified no other dba-site pages link to `references/laws-of-human-nature/` (grep returned no results) → safe to migrate
- After migration succeeds and new Pages site is live, replace `dba-site/content/references/laws-of-human-nature/index.md` with:

  ```markdown
  ---
  title: "Laws of Human Nature → Moved"
  ---

  # Laws of Human Nature

  The full companion (chapters, study guides, slides, audio overview, infographics) now lives in the **Learning From Books** system:

  → https://<user>.github.io/learning-from-books-system-that-improves-with-your-feedback/books/laws-of-human-nature/

  Feedback or requests: `learningfrombooks.feedback+lawsofhumannature@gmail.com`
  ```

- Delete the rest of `content/references/laws-of-human-nature/` in a separate commit/PR for easy revert if needed.

## 11. Acceptance criteria

Phase 1 is "done" only when every item below passes. Browser verification is mandatory; "files committed" is insufficient.

### Infrastructure

- [ ] Repo `learning-from-books-system-that-improves-with-your-feedback` exists on GitHub
- [ ] `main` branch contains all spec'd files
- [ ] `requirements.txt` pins MkDocs + Material + plugins
- [ ] Local `mkdocs serve` runs without errors at `http://localhost:8000`
- [ ] `mkdocs build --strict` passes
- [ ] GitHub Pages enabled, Source = "GitHub Actions"
- [ ] First push to `main` triggers `deploy.yml`, completes green within 3 minutes
- [ ] Public URL returns HTTP 200

### Content (Laws of Human Nature seed)

- [ ] `book.yaml` exists with all required fields populated (no `TODO` placeholders for the URLs)
- [ ] All 18 chapter files present in `docs/books/laws-of-human-nature/chapters/`
- [ ] Each chapter has slide iframe block; Law 1 has real slide URL
- [ ] Each chapter has merged "Study Guide" section
- [ ] Law 1 START + END infographics display correctly
- [ ] `cover.jpg` renders in master index card
- [ ] `feedback/log.md` exists with format header
- [ ] `research/` stubs present (3 files)
- [ ] `feedback-protocol.md` at repo root, documents 8 intent types + 7-step workflow

### Visual & UX (manual browser checks on the live URL)

- [ ] Master index shows hero + book card grid (1 card)
- [ ] Clicking the card opens book index page
- [ ] Sidebar shows: index → chapters (18 entries) → research
- [ ] Search finds chapter content (e.g. "rationality" → chapter 1)
- [ ] Dark mode toggle works, persists across reloads
- [ ] Mobile viewport: grid collapses, sidebar becomes burger menu, chapter pages readable
- [ ] Law 1 slide iframe renders and plays
- [ ] Audio overview link opens NotebookLM correctly
- [ ] `mailto:` links pre-fill correct `+lawsofhumannature` plus-address
- [ ] Tags page shows all 8 seeded categories
- [ ] Tag click filters to relevant books

### Operational

- [ ] Gmail `learningfrombooks.feedback@gmail.com` provisioned
- [ ] Test email to `learningfrombooks.feedback+lawsofhumannature@gmail.com` lands in inbox with correct `Delivered-To` header
- [ ] Google AI Studio API key created under same Gmail (stored locally, NOT committed — for Phase 2)
- [ ] Google Drive folder created; Laws of Human Nature PDF uploaded; share link active
- [ ] NotebookLM workspace exists under same Gmail; notebook visible
- [ ] dba-site wiki stub commit replaces full content; link to new Pages URL resolves

### Documentation

- [ ] `README.md` explains: what this repo is, how to add a book, where feedback goes
- [ ] `feedback-protocol.md` published as above
- [ ] `docs/books/laws-of-human-nature/index.md` is a complete book landing page

### Definition of done

User can open the live Pages URL on a phone, find Laws of Human Nature, read Law 1 with embedded slides and study guide, and send a feedback email that lands correctly in the Gmail inbox.

## 12. Risks & mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| **NotebookLM browser automation fragility (Phase 2)** | High | Phase 1 is manual — no automation risk now. Phase 2 spec must define a fallback: Gemini API for text generation + ElevenLabs for audio if NotebookLM UI shifts break Playwright flow. |
| **GitHub Actions cron drift** | Medium | Latency budget stated explicitly (1h ack, 4h fulfill) so Phase 2 expectations are grounded. |
| **Gmail single-account ToS** | Low | Plus-addressing is officially supported. One account avoids multi-account violation. |
| **PDF auto-discovery legal exposure (Phase 3)** | Medium | Phase 3 must restrict sourcing to: (a) user-uploaded PDFs, (b) Project Gutenberg / public domain, (c) author-permitted free PDFs. No Anna's Archive or pirated sources. Spec deferred but flagged now. |
| **Google Slides "anyone with link" exposure** | Low | All artifacts are derivative summaries of books the user owns; no proprietary content. Public sharing is intentional (the site is public). |
| **Google AI Studio free tier rate limit** | Low | 1500 req/day is comfortably above expected feedback volume; Phase 2 spec should add a hard daily cap + queue overflow handling. |
| **GitHub Pages bandwidth cap (100 GB/mo)** | Very low | Lean asset strategy keeps repo small; site would need ~30k page views/month to approach the cap. |

## 13. Open questions (resolve during user spec review)

None blocking. All major decisions were made during brainstorming.

Minor refinements possible at user review time:
- Whether to include a "Last updated: N days ago" badge on each book card (suggest: yes, simple to derive from `last_updated`)
- Whether the per-book `feedback/log.md` should be excluded from build or published as a transparency feature (suggest: publish — shows the system improving in public)

## 14. References

- Existing seed content: `dba-site/content/references/laws-of-human-nature/`
- Project memory: `[[project-laws-of-human-nature]]`
- Naming convention memory: `[[feedback-naming-style]]`
- NotebookLM MCP plugin (already authenticated for Playwright-based generation): in user's plugin set
- Nano Banana plugin (Gemini image generation): in user's plugin set
- MkDocs Material docs: https://squidfunk.github.io/mkdocs-material/
- MkDocs awesome-pages plugin: https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin
- Gmail plus-addressing reference: https://support.google.com/mail/answer/12096306
- Google AI Studio (Gemini API): https://aistudio.google.com/
- GitHub Pages with Actions deployment: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- Claude Code Routines doc (researched, rejected for this use case): https://code.claude.com/docs/en/routines

## 15. Design delta (2026-07-13): fork-ready architecture

Approved during scope-clarification brainstorm. Phase 1 scope unchanged; three build rules added so the repo works as a template others can fork.

### 15.1 Single config boundary

Everything personal to the site owner lives in exactly two places:

- `mkdocs.yml` — site name, site URL, GitHub repo URL
- per-book `books/<slug>/book.yaml` — feedback email, NotebookLM URLs, Drive PDF URL

Scripts (`build_index.py`, `new_book.py`, migration) read config only. **Zero hardcoded emails, usernames, or URLs in any `.py` file or workflow.** A forker edits two YAML files and nothing else.

### 15.2 Content/engine separation

- `books/<slug>/` = pure content — swappable per fork
- `scripts/`, `.github/workflows/`, `overrides/`, `docs/` templates = engine — forkable as-is

The engine never references `laws-of-human-nature` (or any book slug) by name. Acceptance check: `grep -r "laws-of-human-nature" scripts/ .github/` returns nothing.

### 15.3 Roadmap (recorded, not built)

| Phase | Added scope |
|---|---|
| 2 | Autonomous feedback loop (unchanged from §3) |
| 3 | Fork documentation — "make your own book site" guide, <1 hour setup for a stranger |
| 4+ | Cohort/study-group layer — shared reading schedules, discussion prompts, group flashcards |

Community contributions to *this* site (PRs adding books) are explicitly out of scope at every phase — clarified 2026-07-13.
