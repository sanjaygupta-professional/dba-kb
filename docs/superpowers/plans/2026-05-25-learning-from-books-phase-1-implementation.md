# Learning From Books — Phase 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a public GitHub Pages site hosting the Laws of Human Nature companion as the seed for a reusable per-book template, with a documented manual feedback workflow that Phase 2 will later automate.

**Architecture:** New standalone GitHub repo, MkDocs Material static site, GitHub Actions deploys to Pages. Each book is a folder under `docs/books/<slug>/` with a `book.yaml` metadata file, chapter pages with embedded Google Slides iframes, and links out to NotebookLM artifacts. Gmail plus-addressing routes per-book feedback to a single inbox.

**Tech Stack:** Python 3.12, MkDocs 1.6 + Material 9.5, mkdocs-awesome-pages-plugin, pyyaml, jinja2, GitHub Actions, GitHub Pages, NotebookLM, Google Drive, Gmail plus-addressing.

**Spec reference:** `docs/superpowers/specs/2026-05-25-learning-from-books-phase-1-design.md`

> **Delta (2026-07-13) — fork-ready architecture (spec §15), binding on every task B–J:**
> 1. All owner-specific values (emails, usernames, URLs) live only in `mkdocs.yml` and per-book `book.yaml`. Zero hardcoded personal values in any `.py` file or workflow.
> 2. Engine (`scripts/`, `.github/workflows/`, `overrides/`) never references a book slug by name. Acceptance: `grep -r "laws-of-human-nature" scripts/ .github/` returns nothing.
> 3. Reviewers must check both rules on every task.

**Working directories:**
- **New repo (Phases B–H + J)**: `~/learning-from-books/` (fresh clone after Task 6)
- **Existing dba-site wiki (Phase I)**: `/home/sanjayg4/dba-site/` (for stub commit)

---

## Phase A — Operational setup (manual user actions, no code)

Tasks A1–A5 are user actions outside the code. They must complete before code tasks can ship.

### Task A1: Provision Gmail account

**Files:** none (manual setup)

- [ ] **Step 1: Create the Gmail account**

In a browser, go to `https://accounts.google.com/signup`. Create account with:
- Email: `learningfrombooks.feedback@gmail.com`
- Use a separate browser profile or incognito so this account stays distinct from your personal one
- Enable 2FA (required for app passwords in Task A2)

- [ ] **Step 2: Verify plus-addressing works**

From your personal email, send a test message to: `learningfrombooks.feedback+testing@gmail.com`

Open the new inbox. The message must arrive with `Delivered-To: learningfrombooks.feedback+testing@gmail.com` visible in the message headers (Gmail → more options → "Show original").

- [ ] **Step 3: Generate a Gmail app password (Phase 2 prep)**

Account → Security → 2-Step Verification → App Passwords → generate one for "Learning From Books". Store it in your password manager. **Do not commit anywhere.** Phase 2 will use it for SMTP/IMAP.

### Task A2: Create Google AI Studio API key

**Files:** none (manual setup)

- [ ] **Step 1: Visit AI Studio**

Signed in as `learningfrombooks.feedback@gmail.com`, open `https://aistudio.google.com/apikey`.

- [ ] **Step 2: Create API key**

Click "Create API key" → "Create API key in new project". Name the project `learning-from-books`. Copy the key.

- [ ] **Step 3: Store securely**

Save the key in your password manager labeled `LFB_GEMINI_API_KEY`. **Do not commit.** Phase 2 will load it via GitHub Actions secret.

### Task A3: Create Google Drive folder and upload PDF

**Files:** none (manual setup)

- [ ] **Step 1: Create folder**

Signed in as `learningfrombooks.feedback@gmail.com`, open Drive → New → Folder → name `Books/Laws of Human Nature`.

- [ ] **Step 2: Upload PDF**

Drag the existing PDF of *The Laws of Human Nature* by Robert Greene into that folder.

- [ ] **Step 3: Share with link**

Right-click the PDF → Share → "Anyone with the link can view" → Copy link. Save the URL for Task F4.

### Task A4: Verify NotebookLM access + capture URLs

**Files:** none (manual setup)

- [ ] **Step 1: Open NotebookLM**

Signed in as `learningfrombooks.feedback@gmail.com`, open `https://notebooklm.google.com/`.

- [ ] **Step 2: Verify the Laws of Human Nature notebook**

If the notebook already exists under another Google account, copy it into this new account: download the source PDF list and re-upload to a fresh notebook here. Otherwise create the notebook now and upload the PDF from Task A3.

- [ ] **Step 3: Capture notebook URLs**

In a scratch file (don't commit yet) record:
- Notebook URL (browser address bar of the notebook)
- Audio Overview URL (Studio panel → Audio Overview → share/copy link)
- Flashcards URL (Studio panel → Flashcards → share/copy link)
- For each of the 18 per-chapter slide decks: title + Google Slides URL

These get pasted into `book.yaml` in Task F4.

### Task A5: Create GitHub repository

**Files:** none (manual setup via gh CLI or web)

- [ ] **Step 1: Create the repo on GitHub**

```bash
gh repo create learning-from-books-system-that-improves-with-your-feedback --public --description "Learning From Books — A System That Improves With Your Feedback"
```

Replace with web UI flow if `gh` CLI is not configured: visit `https://github.com/new`, name `learning-from-books-system-that-improves-with-your-feedback`, visibility public, no README/gitignore/license (we'll add ours).

- [ ] **Step 2: Clone locally**

```bash
cd ~
gh repo clone learning-from-books-system-that-improves-with-your-feedback learning-from-books
cd learning-from-books
```

This creates `~/learning-from-books/` as the working directory for Phases B–H.

- [ ] **Step 3: Configure Pages source**

```bash
gh repo edit --enable-issues
gh api -X POST /repos/:owner/:repo/pages -f source.branch=main -f source.path=/ 2>/dev/null || true
```

Then in the GitHub web UI: Settings → Pages → Build and deployment → Source → **"GitHub Actions"**.

---

## Phase B — Repository scaffolding

All Phase B–H tasks run from `~/learning-from-books/` unless stated otherwise.

### Task B1: Initialize repo skeleton

**Files:**
- Create: `~/learning-from-books/.gitignore`
- Create: `~/learning-from-books/README.md`
- Create: `~/learning-from-books/requirements.txt`

- [ ] **Step 1: Write .gitignore**

```bash
cd ~/learning-from-books
```

Create `.gitignore` with:

```
# Python
__pycache__/
*.py[cod]
*$py.class
.venv/
venv/
*.egg-info/

# MkDocs build output
site/

# OS
.DS_Store
Thumbs.db

# Editors
.vscode/
.idea/
*.swp

# Secrets (defense in depth — never commit)
.env
.env.*
*.key
secrets.yaml
```

- [ ] **Step 2: Write requirements.txt**

```
mkdocs==1.6.1
mkdocs-material==9.5.49
mkdocs-awesome-pages-plugin==2.9.3
pyyaml==6.0.2
jinja2==3.1.4
pytest==8.3.4
```

- [ ] **Step 3: Write README.md**

```markdown
# Learning From Books

A continuous improvement system for deep reading. Each book gets a hub page with summary, slides, audio overview, infographics, and curated research. Readers send feedback by email and the system improves over time.

## Live site

https://<your-username>.github.io/learning-from-books-system-that-improves-with-your-feedback/

## How to add a book

1. Run `python scripts/new_book.py "Book Title" "Author Name"`
2. Fill in NotebookLM, Drive, and Slides URLs in `docs/books/<slug>/book.yaml`
3. Add chapter files to `docs/books/<slug>/chapters/`
4. Push to `main` — GitHub Action deploys to Pages within ~90 seconds

## How to send feedback

Email `learningfrombooks.feedback+<bookslug>@gmail.com` (e.g. `+lawsofhumannature`). See `feedback-protocol.md` for accepted intents and the manual workflow.

## Tech

MkDocs Material, GitHub Pages, NotebookLM (audio/slides/flashcards), Google Drive (PDFs), Gmail plus-addressing (per-book routing).

## License

Content: CC BY 4.0. Code: MIT.
```

- [ ] **Step 4: Set up Python virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Expected: clean install, no errors. Verify with `mkdocs --version` (should print 1.6.1).

- [ ] **Step 5: Commit**

```bash
git add .gitignore README.md requirements.txt
git commit -m "Initialize repo with gitignore, README, Python requirements"
```

---

## Phase C — MkDocs base configuration

### Task C1: Write mkdocs.yml

**Files:**
- Create: `~/learning-from-books/mkdocs.yml`

- [ ] **Step 1: Write the config**

```yaml
site_name: "Learning From Books"
site_description: "A System That Improves With Your Feedback"
site_url: "https://<your-username>.github.io/learning-from-books-system-that-improves-with-your-feedback/"
repo_url: "https://github.com/<your-username>/learning-from-books-system-that-improves-with-your-feedback"
repo_name: "GitHub"

theme:
  name: material
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
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
  - pymdownx.tabbed:
      alternate_style: true
  - attr_list
  - md_in_html
  - toc:
      permalink: true

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

Replace both occurrences of `<your-username>` with the actual GitHub username.

- [ ] **Step 2: Commit**

```bash
git add mkdocs.yml
git commit -m "Add mkdocs.yml with Material theme, search, awesome-pages, tags"
```

### Task C2: Write extra CSS

**Files:**
- Create: `~/learning-from-books/docs/stylesheets/extra.css`

- [ ] **Step 1: Create the directory**

```bash
mkdir -p docs/stylesheets
```

- [ ] **Step 2: Write extra.css**

```css
/* Book card grid for the master index page */
.book-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1.25rem;
  margin: 2rem 0;
}

.book-card {
  display: block;
  border-radius: 12px;
  overflow: hidden;
  background: var(--md-default-bg-color);
  color: inherit;
  text-decoration: none;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: transform 0.15s, box-shadow 0.15s;
}

.book-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
}

.book-card img {
  width: 100%;
  aspect-ratio: 3 / 4;
  object-fit: cover;
  display: block;
}

.card-meta {
  padding: 0.75rem 1rem 1rem;
}

.card-meta h3 {
  margin: 0 0 0.25rem;
  font-size: 1rem;
}

.author {
  font-size: 0.85rem;
  color: var(--md-default-fg-color--light);
  margin: 0;
}

.tags {
  margin: 0.5rem 0;
  display: flex;
  gap: 0.4rem;
  flex-wrap: wrap;
}

.tags span {
  background: var(--md-accent-fg-color--transparent);
  color: var(--md-accent-fg-color);
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  font-size: 0.75rem;
}

.status {
  font-size: 0.78rem;
  color: var(--md-default-fg-color--lighter);
  margin: 0.5rem 0 0;
}

/* Responsive Google Slides iframe */
.slides-embed {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
  height: 0;
  overflow: hidden;
  margin: 1.5rem 0;
  border-radius: 8px;
}

.slides-embed iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}
```

- [ ] **Step 3: Commit**

```bash
git add docs/stylesheets/extra.css
git commit -m "Add extra.css: book card grid + responsive slides embed"
```

### Task C3: Write placeholder index.md

**Files:**
- Create: `~/learning-from-books/docs/index.md`

- [ ] **Step 1: Write minimal index**

This file is auto-regenerated by `scripts/build_index.py` in Task D2. For now we need a stub so `mkdocs serve` doesn't error.

```markdown
# Learning From Books

A continuous improvement system for deep reading. Send feedback to any book's email — the system improves with your input.

(This page is auto-generated by `scripts/build_index.py` once books are added.)

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

Email [learningfrombooks.feedback+request@gmail.com](mailto:learningfrombooks.feedback+request@gmail.com) with the title and author.
```

- [ ] **Step 2: Verify mkdocs serves locally**

```bash
mkdocs serve
```

Expected: server starts on `http://127.0.0.1:8000`, no errors, index page renders. Press Ctrl-C to stop.

- [ ] **Step 3: Commit**

```bash
git add docs/index.md
git commit -m "Add placeholder index.md (regenerated by build_index.py later)"
```

---

## Phase D — Build script with TDD

### Task D1: Write failing test for build_index.py

**Files:**
- Create: `~/learning-from-books/tests/__init__.py`
- Create: `~/learning-from-books/tests/test_build_index.py`

- [ ] **Step 1: Create tests directory**

```bash
mkdir -p tests
touch tests/__init__.py
```

- [ ] **Step 2: Write test_build_index.py**

```python
"""Tests for scripts/build_index.py."""
from pathlib import Path
import shutil
import subprocess
import sys

import pytest


REPO_ROOT = Path(__file__).resolve().parent.parent
BUILD_INDEX = REPO_ROOT / "scripts" / "build_index.py"


@pytest.fixture
def tmp_docs(tmp_path, monkeypatch):
    """Create a minimal docs/ tree with two books for the script to scan."""
    docs = tmp_path / "docs"
    book_a = docs / "books" / "book-a"
    book_b = docs / "books" / "book-b"
    book_a.mkdir(parents=True)
    book_b.mkdir(parents=True)
    (book_a / "book.yaml").write_text(
        "title: Book A\n"
        "author: Alice\n"
        "year: 2024\n"
        "slug: book-a\n"
        "categories: [psychology]\n"
        "status: active\n"
        "chapters_total: 5\n"
        "cover: infographics/cover.jpg\n"
        "last_updated: '2026-05-25'\n"
    )
    (book_b / "book.yaml").write_text(
        "title: Book B\n"
        "author: Bob\n"
        "year: 2020\n"
        "slug: book-b\n"
        "categories: [economics, strategy]\n"
        "status: active\n"
        "chapters_total: 10\n"
        "cover: infographics/cover.jpg\n"
        "last_updated: '2026-04-01'\n"
    )
    return docs


def test_build_index_generates_index_md(tmp_docs):
    """Running build_index.py against a docs tree writes a non-empty index.md."""
    result = subprocess.run(
        [sys.executable, str(BUILD_INDEX), "--docs", str(tmp_docs)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    index = tmp_docs / "index.md"
    assert index.exists()
    content = index.read_text()
    assert "Learning From Books" in content
    assert "Book A" in content
    assert "Book B" in content


def test_build_index_sorts_by_last_updated_desc(tmp_docs):
    """Newer books appear before older ones in the rendered index."""
    subprocess.run(
        [sys.executable, str(BUILD_INDEX), "--docs", str(tmp_docs)],
        check=True,
    )
    content = (tmp_docs / "index.md").read_text()
    pos_a = content.find("Book A")
    pos_b = content.find("Book B")
    assert 0 < pos_a < pos_b, "Book A (newer) should appear before Book B (older)"


def test_build_index_renders_all_unique_categories(tmp_docs):
    """Categories from all books appear in the Browse by category section."""
    subprocess.run(
        [sys.executable, str(BUILD_INDEX), "--docs", str(tmp_docs)],
        check=True,
    )
    content = (tmp_docs / "index.md").read_text()
    for cat in ("psychology", "economics", "strategy"):
        assert cat.lower() in content.lower(), f"Missing category: {cat}"


def test_build_index_is_idempotent(tmp_docs):
    """Running twice produces identical output."""
    subprocess.run(
        [sys.executable, str(BUILD_INDEX), "--docs", str(tmp_docs)],
        check=True,
    )
    first = (tmp_docs / "index.md").read_text()
    subprocess.run(
        [sys.executable, str(BUILD_INDEX), "--docs", str(tmp_docs)],
        check=True,
    )
    second = (tmp_docs / "index.md").read_text()
    assert first == second
```

- [ ] **Step 3: Run tests, verify they fail**

```bash
pytest tests/test_build_index.py -v
```

Expected: 4 tests FAIL with errors like "No such file or directory: scripts/build_index.py" or non-zero return code.

- [ ] **Step 4: Commit failing tests**

```bash
mkdir -p scripts
git add tests/__init__.py tests/test_build_index.py
git commit -m "Add failing tests for build_index.py"
```

### Task D2: Implement build_index.py to pass tests

**Files:**
- Create: `~/learning-from-books/scripts/__init__.py`
- Create: `~/learning-from-books/scripts/build_index.py`

- [ ] **Step 1: Create scripts package**

```bash
touch scripts/__init__.py
```

- [ ] **Step 2: Write build_index.py**

```python
#!/usr/bin/env python3
"""Generate docs/index.md from docs/books/*/book.yaml metadata files.

The output is a hero header + a grid of book cards + a category browse list +
a request-a-book CTA. Sorted by last_updated descending. Idempotent.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

CATEGORIES_SEED = [
    "Psychology",
    "Systems Thinking",
    "Neuroscience",
    "Economics",
    "Philosophy",
    "History",
    "Strategy",
    "Productivity",
]

HEADER = """# Learning From Books

A continuous improvement system for deep reading. Send feedback to any book's email — the system improves with your input.

"""

FOOTER_TEMPLATE = """## Browse by category

{category_links}

## Request a book

Email [learningfrombooks.feedback+request@gmail.com](mailto:learningfrombooks.feedback+request@gmail.com) with the title and author.
"""


def load_books(docs_dir: Path) -> list[dict]:
    books_dir = docs_dir / "books"
    if not books_dir.exists():
        return []
    out = []
    for book_yaml in sorted(books_dir.glob("*/book.yaml")):
        data = yaml.safe_load(book_yaml.read_text())
        data["_dir"] = book_yaml.parent.name
        out.append(data)
    # newest first
    out.sort(key=lambda b: str(b.get("last_updated", "")), reverse=True)
    return out


def render_card(book: dict) -> str:
    slug = book["_dir"]
    title = book.get("title", "Untitled")
    author = book.get("author", "Unknown")
    year = book.get("year", "")
    cover = book.get("cover", "infographics/cover.jpg")
    chapters = book.get("chapters_total", "?")
    updated = book.get("last_updated", "")
    cats = book.get("categories", [])
    tag_html = "".join(f'<span>{c}</span>' for c in cats)
    return (
        f'<a class="book-card" href="books/{slug}/">\n'
        f'  <img src="books/{slug}/{cover}" alt="">\n'
        f'  <div class="card-meta">\n'
        f'    <h3>{title}</h3>\n'
        f'    <p class="author">{author} · {year}</p>\n'
        f'    <div class="tags">{tag_html}</div>\n'
        f'    <p class="status">{chapters} chapters · updated {updated}</p>\n'
        f'  </div>\n'
        f'</a>\n'
    )


def render_categories(books: list[dict]) -> str:
    seen = set()
    for b in books:
        for c in b.get("categories", []):
            seen.add(c.lower())
    lines = []
    for cat in CATEGORIES_SEED:
        anchor = cat.lower().replace(" ", "-")
        if cat.lower() in seen:
            lines.append(f"- [{cat}](tags.md#{anchor})")
        else:
            lines.append(f"- {cat} *(coming soon)*")
    return "\n".join(lines)


def build(docs_dir: Path) -> str:
    books = load_books(docs_dir)
    if not books:
        body = "(No books yet — run `python scripts/new_book.py` to add one.)\n\n"
    else:
        cards = "".join(render_card(b) for b in books)
        body = f'<div class="book-grid">\n{cards}</div>\n\n'
    footer = FOOTER_TEMPLATE.format(category_links=render_categories(books))
    return HEADER + body + footer


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs", type=Path, default=Path("docs"),
                        help="Path to MkDocs docs directory")
    args = parser.parse_args()
    output = build(args.docs)
    (args.docs / "index.md").write_text(output)
    print(f"Wrote {args.docs / 'index.md'} ({len(output)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 3: Make script executable**

```bash
chmod +x scripts/build_index.py
```

- [ ] **Step 4: Run tests, verify they pass**

```bash
pytest tests/test_build_index.py -v
```

Expected: 4 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add scripts/__init__.py scripts/build_index.py
git commit -m "Implement build_index.py: generates docs/index.md from book.yaml files"
```

### Task D3: Write new_book.py scaffolding helper

**Files:**
- Create: `~/learning-from-books/scripts/new_book.py`

- [ ] **Step 1: Write the script**

```python
#!/usr/bin/env python3
"""Scaffold a new book directory under docs/books/<slug>/.

Usage: python scripts/new_book.py "Book Title" "Author Name" [--year 2024]
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


BOOK_YAML_TEMPLATE = """title: "{title}"
author: "{author}"
year: {year}
slug: "{slug}"
categories: []
status: "draft"
chapters_total: 0
cover: "infographics/cover.jpg"
last_updated: "{today}"

notebooklm_url: ""
notebooklm_flashcards_url: ""
audio_overview_url: ""
slides_condensed_url: ""
slides_detailed_url: ""
drive_pdf_url: ""

feedback_email: "learningfrombooks.feedback+{slug_compact}@gmail.com"

chapters: []
"""

PAGES_TEMPLATE = """title: "{title}"
nav:
  - index.md
  - chapters
  - research
"""

INDEX_MD_TEMPLATE = """# {title}

**{author} · {year}**

## Overview

(Add a 2-3 paragraph synthesized overview here.)

## Audio Overview

(Embed or link to NotebookLM audio overview once `book.yaml` URL is filled.)

## Slide Decks

- [Condensed deck](#)
- [Detailed deck](#)

## Flashcards

(Link to NotebookLM flashcards once `book.yaml` URL is filled.)

## Feedback

Send to `learningfrombooks.feedback+{slug_compact}@gmail.com`. See [feedback protocol](../../../feedback-protocol.md).
"""

LOG_HEADER = """# Feedback log — {title}

Each entry: date, intent, action taken, commit, reply sent.

"""

RESEARCH_STUB = """# {section}

(Curated by Phase 4 agent. Manual entries welcome until then.)
"""


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("title")
    p.add_argument("author")
    p.add_argument("--year", type=int, default=dt.date.today().year)
    p.add_argument("--docs", type=Path, default=Path("docs"))
    args = p.parse_args()

    slug = slugify(args.title)
    slug_compact = slug.replace("-", "")
    today = dt.date.today().isoformat()
    book_dir = args.docs / "books" / slug
    if book_dir.exists():
        print(f"ERROR: {book_dir} already exists", file=sys.stderr)
        return 1
    (book_dir / "chapters").mkdir(parents=True)
    (book_dir / "infographics").mkdir()
    (book_dir / "research").mkdir()
    (book_dir / "feedback").mkdir()

    (book_dir / "book.yaml").write_text(BOOK_YAML_TEMPLATE.format(
        title=args.title, author=args.author, year=args.year,
        slug=slug, slug_compact=slug_compact, today=today))
    (book_dir / ".pages").write_text(PAGES_TEMPLATE.format(title=args.title))
    (book_dir / "index.md").write_text(INDEX_MD_TEMPLATE.format(
        title=args.title, author=args.author, year=args.year,
        slug_compact=slug_compact))
    (book_dir / "feedback" / "log.md").write_text(LOG_HEADER.format(title=args.title))
    for section in ("Author Talks", "Blog Posts", "Academic Commentary"):
        fname = section.lower().replace(" ", "-") + ".md"
        (book_dir / "research" / fname).write_text(RESEARCH_STUB.format(section=section))

    print(f"Created {book_dir}")
    print("Next: fill in book.yaml URLs, add chapter files, regenerate index with build_index.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/new_book.py
```

- [ ] **Step 3: Smoke test**

```bash
python scripts/new_book.py "Smoke Test Book" "Test Author"
ls docs/books/smoke-test-book/
```

Expected output: `book.yaml`, `.pages`, `index.md`, `chapters/`, `infographics/`, `research/`, `feedback/`.

- [ ] **Step 4: Clean up smoke test artifact**

```bash
rm -rf docs/books/smoke-test-book
```

- [ ] **Step 5: Commit**

```bash
git add scripts/new_book.py
git commit -m "Add new_book.py: scaffold per-book directory structure"
```

---

## Phase E — GitHub Actions deployment

### Task E1: Write deploy workflow

**Files:**
- Create: `~/learning-from-books/.github/workflows/deploy.yml`

- [ ] **Step 1: Create workflow directory**

```bash
mkdir -p .github/workflows
```

- [ ] **Step 2: Write deploy.yml**

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
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
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

- [ ] **Step 3: Verify locally that build --strict passes BEFORE pushing**

```bash
python scripts/build_index.py
mkdocs build --strict
```

Expected: completes with no warnings/errors. `site/` directory created. (You can browse `site/index.html` with `python -m http.server 8001 -d site` to confirm.)

- [ ] **Step 4: Clean up build output**

```bash
rm -rf site
```

- [ ] **Step 5: Commit**

```bash
git add .github/workflows/deploy.yml
git commit -m "Add GitHub Actions workflow: build MkDocs and deploy to Pages"
```

### Task E2: Initial push and Pages verification

**Files:** none (push + browser verification)

- [ ] **Step 1: Push to GitHub**

```bash
git push -u origin main
```

- [ ] **Step 2: Watch the Action run**

```bash
gh run watch
```

Expected: workflow `Build and deploy site` runs and turns green within 3 minutes. If `gh` CLI is not configured, open `https://github.com/<your-username>/learning-from-books-system-that-improves-with-your-feedback/actions` in the browser.

- [ ] **Step 3: Verify the Pages URL responds**

```bash
curl -s -o /dev/null -w "HTTP %{http_code}\n" \
  https://<your-username>.github.io/learning-from-books-system-that-improves-with-your-feedback/
```

Expected: `HTTP 200`. Open the URL in a browser; the placeholder index page renders.

- [ ] **Step 4: No commit needed** (deploy is verified, not authored)

---

## Phase F — Migrate Laws of Human Nature with TDD

### Task F1: Write failing test for migration script

**Files:**
- Create: `~/learning-from-books/tests/test_migrate_laws.py`

- [ ] **Step 1: Write the test**

```python
"""Tests for scripts/migrate_laws_of_human_nature.py."""
from pathlib import Path
import shutil
import subprocess
import sys

import pytest
import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
MIGRATE = REPO_ROOT / "scripts" / "migrate_laws_of_human_nature.py"


@pytest.fixture
def fake_source(tmp_path):
    """Mock the dba-site Laws of Human Nature source tree."""
    src = tmp_path / "src"
    (src / "study-guides").mkdir(parents=True)
    (src / "infographics").mkdir()
    (src / "index.md").write_text("---\ntitle: index\n---\nplaceholder\n")
    for n in (1, 2):
        slug = "irrationality" if n == 1 else "narcissism"
        title = "Irrationality" if n == 1 else "Narcissism"
        directive = "Master Your Emotional Self" if n == 1 else "Recognize the Narcissist"
        (src / f"law-{n:02d}-{slug}.md").write_text(
            f"---\n"
            f"title: \"Law {n}: {title} — {directive}\"\n"
            f"category: references\n"
            f"tags: [\"#book/laws-of-human-nature\"]\n"
            f"law_number: {n}\n"
            f"law_name: \"{title}\"\n"
            f"directive: \"{directive}\"\n"
            f"book: \"The Laws of Human Nature\"\n"
            f"author: \"Robert Greene\"\n"
            f"created: 2026-05-16\n"
            f"updated: 2026-05-16\n"
            f"summary: \"Test summary.\"\n"
            f"---\n\n"
            f"# Law {n}: The Law of {title}\n\n"
            f"Body content for law {n}.\n"
        )
        (src / "study-guides" / f"law-{n:02d}-{slug}-study-guide.md").write_text(
            f"---\ntitle: study guide {n}\n---\n\n## Section\n\nStudy guide content {n}.\n"
        )
    (src / "infographics" / "law-01-irrationality-start.png").write_bytes(b"\x89PNG\r\n\x1a\nfake")
    (src / "infographics" / "law-01-irrationality-end.png").write_bytes(b"\x89PNG\r\n\x1a\nfake")
    return src


def test_migrate_creates_book_yaml(fake_source, tmp_path):
    dst = tmp_path / "docs"
    result = subprocess.run(
        [sys.executable, str(MIGRATE), "--source", str(fake_source), "--docs", str(dst)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    book_yaml = dst / "books" / "laws-of-human-nature" / "book.yaml"
    assert book_yaml.exists()
    data = yaml.safe_load(book_yaml.read_text())
    assert data["title"] == "The Laws of Human Nature"
    assert data["author"] == "Robert Greene"
    assert data["slug"] == "laws-of-human-nature"
    assert data["chapters_total"] == 2
    assert "psychology" in [c.lower() for c in data["categories"]]


def test_migrate_writes_chapter_files(fake_source, tmp_path):
    dst = tmp_path / "docs"
    subprocess.run(
        [sys.executable, str(MIGRATE), "--source", str(fake_source), "--docs", str(dst)],
        check=True,
    )
    chapters = dst / "books" / "laws-of-human-nature" / "chapters"
    assert (chapters / "01-irrationality.md").exists()
    assert (chapters / "02-narcissism.md").exists()
    content = (chapters / "01-irrationality.md").read_text()
    assert "chapter: 1" in content
    assert "## Study Guide" in content
    assert "Study guide content 1" in content
    assert "## Slide Deck" in content
    assert "slides-embed" in content
    # original Quartz tags stripped
    assert "#book/laws-of-human-nature" not in content


def test_migrate_renames_infographics(fake_source, tmp_path):
    dst = tmp_path / "docs"
    subprocess.run(
        [sys.executable, str(MIGRATE), "--source", str(fake_source), "--docs", str(dst)],
        check=True,
    )
    infos = dst / "books" / "laws-of-human-nature" / "infographics"
    assert (infos / "01-start.png").exists()
    assert (infos / "01-end.png").exists()


def test_migrate_creates_stubs(fake_source, tmp_path):
    dst = tmp_path / "docs"
    subprocess.run(
        [sys.executable, str(MIGRATE), "--source", str(fake_source), "--docs", str(dst)],
        check=True,
    )
    base = dst / "books" / "laws-of-human-nature"
    assert (base / ".pages").exists()
    assert (base / "feedback" / "log.md").exists()
    assert (base / "research" / "author-talks.md").exists()
    assert (base / "research" / "blog-posts.md").exists()
    assert (base / "research" / "academic-commentary.md").exists()


def test_migrate_idempotent(fake_source, tmp_path):
    dst = tmp_path / "docs"
    subprocess.run(
        [sys.executable, str(MIGRATE), "--source", str(fake_source), "--docs", str(dst)],
        check=True,
    )
    # second run must not error (overwrites OK)
    result = subprocess.run(
        [sys.executable, str(MIGRATE), "--source", str(fake_source), "--docs", str(dst)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
```

- [ ] **Step 2: Run, verify all 5 tests fail**

```bash
pytest tests/test_migrate_laws.py -v
```

Expected: 5 tests FAIL with "No such file" for the migration script.

- [ ] **Step 3: Commit failing tests**

```bash
git add tests/test_migrate_laws.py
git commit -m "Add failing tests for Laws of Human Nature migration"
```

### Task F2: Implement migration script

**Files:**
- Create: `~/learning-from-books/scripts/migrate_laws_of_human_nature.py`

- [ ] **Step 1: Write the script**

```python
#!/usr/bin/env python3
"""Migrate the Laws of Human Nature seed content from dba-site into this repo.

Source layout (dba-site):
  content/references/laws-of-human-nature/
    index.md
    law-NN-slug.md  × 18
    study-guides/law-NN-slug-study-guide.md  × 18
    infographics/law-NN-slug-start.png, *-end.png

Target layout (this repo):
  docs/books/laws-of-human-nature/
    book.yaml, .pages, index.md
    chapters/NN-slug.md  (study guide merged in)
    infographics/NN-start.png, NN-end.png
    research/*.md (stubs)
    feedback/log.md (empty)

Usage:
  python scripts/migrate_laws_of_human_nature.py \\
    --source /home/user/dba-site/content/references/laws-of-human-nature \\
    --docs docs
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

import yaml

BOOK_SLUG = "laws-of-human-nature"
BOOK_TITLE = "The Laws of Human Nature"
BOOK_AUTHOR = "Robert Greene"
BOOK_YEAR = 2018
BOOK_CATEGORIES = ["psychology", "behavior", "leadership"]
TODAY = "2026-05-25"


CHAPTER_LAW_RE = re.compile(r"^law-(\d{2})-(.+)\.md$")
INFOGRAPHIC_RE = re.compile(r"^law-(\d{2})-[^.]+-(start|end)\.png$")
STUDY_GUIDE_RE = re.compile(r"^law-(\d{2})-(.+)-study-guide\.md$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, m.group(2)


def make_chapter_frontmatter(num: int, title: str) -> str:
    return (
        "---\n"
        f"chapter: {num}\n"
        f'title: "{title}"\n'
        'slides_url: ""\n'
        'notebooklm_section_url: ""\n'
        "key_concepts: []\n"
        "---\n\n"
    )


SLIDE_BLOCK = '''## Slide Deck

<div class="slides-embed">
  <iframe src="" frameborder="0" allowfullscreen></iframe>
</div>

*Slide URL pending. Update via `book.yaml` chapter entry.*

'''


def migrate(source: Path, docs: Path) -> int:
    book_dir = docs / "books" / BOOK_SLUG
    chapters_dir = book_dir / "chapters"
    infos_dir = book_dir / "infographics"
    research_dir = book_dir / "research"
    feedback_dir = book_dir / "feedback"
    for d in (chapters_dir, infos_dir, research_dir, feedback_dir):
        d.mkdir(parents=True, exist_ok=True)

    # collect law files
    chapter_entries = []
    for law_file in sorted(source.glob("law-*.md")):
        m = CHAPTER_LAW_RE.match(law_file.name)
        if not m:
            continue
        num = int(m.group(1))
        slug = m.group(2)
        meta, body = parse_frontmatter(law_file.read_text())
        law_name = meta.get("law_name", slug.replace("-", " ").title())
        directive = meta.get("directive", "")
        chapter_title = f"The Law of {law_name}"
        # study guide if it exists
        sg = source / "study-guides" / f"law-{num:02d}-{slug}-study-guide.md"
        sg_body = ""
        if sg.exists():
            _, sg_body = parse_frontmatter(sg.read_text())
            sg_body = sg_body.lstrip()
        # build chapter markdown
        out = make_chapter_frontmatter(num, chapter_title)
        if directive:
            out += f"# Chapter {num} — {chapter_title}\n\n"
            out += f"**Directive: \"{directive}\"**\n\n"
        else:
            out += f"# Chapter {num} — {chapter_title}\n\n"
        out += SLIDE_BLOCK
        out += "## Summary\n\n" + body.strip() + "\n\n"
        if sg_body:
            out += "## Study Guide\n\n" + sg_body.strip() + "\n"
        target = chapters_dir / f"{num:02d}-{slug}.md"
        target.write_text(out)
        chapter_entries.append({
            "num": num,
            "title": chapter_title,
            "slug": f"{num:02d}-{slug}",
            "slides_url": "",
        })

    # copy + rename infographics
    if (source / "infographics").exists():
        for png in (source / "infographics").glob("*.png"):
            m = INFOGRAPHIC_RE.match(png.name)
            if not m:
                continue
            num = m.group(1)
            kind = m.group(2)
            shutil.copy(png, infos_dir / f"{num}-{kind}.png")

    # write book.yaml
    book_yaml = {
        "title": BOOK_TITLE,
        "author": BOOK_AUTHOR,
        "year": BOOK_YEAR,
        "slug": BOOK_SLUG,
        "categories": BOOK_CATEGORIES,
        "status": "active",
        "chapters_total": len(chapter_entries),
        "cover": "infographics/cover.jpg",
        "last_updated": TODAY,
        "notebooklm_url": "",
        "notebooklm_flashcards_url": "",
        "audio_overview_url": "",
        "slides_condensed_url": "",
        "slides_detailed_url": "",
        "drive_pdf_url": "",
        "feedback_email": "learningfrombooks.feedback+lawsofhumannature@gmail.com",
        "chapters": chapter_entries,
    }
    (book_dir / "book.yaml").write_text(yaml.safe_dump(book_yaml, sort_keys=False, allow_unicode=True))

    # .pages
    (book_dir / ".pages").write_text(
        'title: "The Laws of Human Nature"\n'
        'nav:\n'
        '  - index.md\n'
        '  - chapters\n'
        '  - research\n'
    )

    # book index.md
    (book_dir / "index.md").write_text(
        "# The Laws of Human Nature\n\n"
        "**Robert Greene · 2018**\n\n"
        "## Overview\n\n"
        "Robert Greene's 18 laws map the deepest patterns of human behavior — from irrationality and narcissism through aggression and death denial — and show how mastering them gives a decisive advantage in any human endeavor.\n\n"
        "## Audio Overview\n\n"
        "*Link to NotebookLM audio overview pending. See `book.yaml`.*\n\n"
        "## Slide Decks\n\n"
        "- Condensed deck (URL pending)\n"
        "- Detailed deck (URL pending)\n\n"
        "## Flashcards\n\n"
        "*Link to NotebookLM flashcards pending.*\n\n"
        "## Feedback\n\n"
        "Send to `learningfrombooks.feedback+lawsofhumannature@gmail.com`. See [feedback protocol](../../../feedback-protocol.md).\n"
    )

    # feedback log header
    (feedback_dir / "log.md").write_text(
        "# Feedback log — The Laws of Human Nature\n\n"
        "Each entry: date, intent, action taken, commit, reply sent.\n\n"
    )

    # research stubs
    for section_file, section_title in (
        ("author-talks.md", "Author Talks"),
        ("blog-posts.md", "Blog Posts"),
        ("academic-commentary.md", "Academic Commentary"),
    ):
        (research_dir / section_file).write_text(
            f"# {section_title}\n\n(Curated by Phase 4 agent. Manual entries welcome until then.)\n"
        )

    print(f"Migrated {len(chapter_entries)} chapters to {book_dir}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--source", type=Path, required=True,
                   help="Path to content/references/laws-of-human-nature in dba-site")
    p.add_argument("--docs", type=Path, default=Path("docs"))
    args = p.parse_args()
    if not args.source.exists():
        print(f"ERROR: source path does not exist: {args.source}", file=sys.stderr)
        return 1
    return migrate(args.source, args.docs)


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/migrate_laws_of_human_nature.py
```

- [ ] **Step 3: Run tests, verify all 5 pass**

```bash
pytest tests/test_migrate_laws.py -v
```

Expected: 5 tests PASS.

- [ ] **Step 4: Commit**

```bash
git add scripts/migrate_laws_of_human_nature.py
git commit -m "Implement Laws of Human Nature migration script"
```

### Task F3: Run migration against real dba-site content

**Files:** writes into `docs/books/laws-of-human-nature/`

- [ ] **Step 1: Run the migration**

```bash
python scripts/migrate_laws_of_human_nature.py \
  --source /home/sanjayg4/dba-site/content/references/laws-of-human-nature \
  --docs docs
```

Expected output: `Migrated 18 chapters to docs/books/laws-of-human-nature`.

- [ ] **Step 2: Spot-check chapter 1**

```bash
head -30 docs/books/laws-of-human-nature/chapters/01-irrationality.md
```

Expected: frontmatter with `chapter: 1`, slide deck block, summary section. Original Quartz tags absent.

- [ ] **Step 3: Verify all 18 chapters present**

```bash
ls docs/books/laws-of-human-nature/chapters/ | wc -l
```

Expected: `18`.

- [ ] **Step 4: Verify infographics copied**

```bash
ls docs/books/laws-of-human-nature/infographics/
```

Expected: `01-start.png`, `01-end.png` (cover.jpg comes from Task F5).

- [ ] **Step 5: Run mkdocs build --strict to verify**

```bash
python scripts/build_index.py
mkdocs build --strict 2>&1 | tail -20
```

Expected: completes with no warnings/errors. (If a missing-link warning appears for `cover.jpg`, that's expected — fix in Task F5.)

- [ ] **Step 6: Commit migrated content**

```bash
git add docs/books/laws-of-human-nature/
git commit -m "Migrate Laws of Human Nature seed content (18 chapters + 2 infographics)"
```

### Task F4: Fill in NotebookLM and Drive URLs

**Files:**
- Modify: `~/learning-from-books/docs/books/laws-of-human-nature/book.yaml`

- [ ] **Step 1: Open book.yaml**

Open `docs/books/laws-of-human-nature/book.yaml` in your editor.

- [ ] **Step 2: Fill in the top-level URLs from Task A4 notes**

Replace empty strings with the real URLs:

```yaml
notebooklm_url: "https://notebooklm.google.com/notebook/<id>"
notebooklm_flashcards_url: "https://notebooklm.google.com/notebook/<id>/flashcards"
audio_overview_url: "https://notebooklm.google.com/notebook/<id>/audio"
slides_condensed_url: "https://docs.google.com/presentation/d/<id>"
slides_detailed_url: "https://docs.google.com/presentation/d/<id>"
drive_pdf_url: "<drive URL from Task A3>"
```

- [ ] **Step 3: Fill in Chapter 1 slide URL (others can stay empty for Phase 1)**

In the `chapters:` list, update only the first entry:

```yaml
chapters:
  - num: 1
    title: "The Law of Irrationality"
    slug: "01-irrationality"
    slides_url: "https://docs.google.com/presentation/d/<chapter-1-id>"
```

- [ ] **Step 4: Update the matching chapter markdown to use the URL**

Open `docs/books/laws-of-human-nature/chapters/01-irrationality.md`. Replace `slides_url: ""` in the frontmatter with the same URL. Replace the iframe `src=""` with `src="https://docs.google.com/presentation/d/<chapter-1-id>/embed?start=false&loop=false&delayms=3000"`.

- [ ] **Step 5: Commit**

```bash
git add docs/books/laws-of-human-nature/book.yaml docs/books/laws-of-human-nature/chapters/01-irrationality.md
git commit -m "Fill in NotebookLM and Drive URLs in book.yaml; wire chapter 1 slide deck"
```

### Task F5: Generate cover image via Nano Banana

**Files:**
- Create: `~/learning-from-books/docs/books/laws-of-human-nature/infographics/cover.jpg`

- [ ] **Step 1: Generate the image**

In your usual Claude Code session (Max subscription), run the `nano-banana:genimage` skill (or use the plugin's `gemini-image-gen` agent) with prompt:

```
Book cover, "The Laws of Human Nature" by Robert Greene, classical philosophy aesthetic, dark indigo background, gold serif typography, subtle Greek-statue-fragment motif, 3:4 portrait aspect ratio, no text rendering errors.
```

Output target: `/home/sanjayg4/learning-from-books/docs/books/laws-of-human-nature/infographics/cover.jpg`.

- [ ] **Step 2: Verify file exists and is reasonable size**

```bash
ls -la docs/books/laws-of-human-nature/infographics/cover.jpg
```

Expected: file present, 100KB–500KB range.

- [ ] **Step 3: Optimize if needed**

If the file is over 500 KB:

```bash
# Optional: compress with ImageMagick if available
which convert && convert docs/books/laws-of-human-nature/infographics/cover.jpg -quality 82 -resize 600x800^ docs/books/laws-of-human-nature/infographics/cover.jpg
```

- [ ] **Step 4: Commit**

```bash
git add docs/books/laws-of-human-nature/infographics/cover.jpg
git commit -m "Add Laws of Human Nature cover image (Nano Banana generated)"
```

### Task F6: Rebuild and verify local site

- [ ] **Step 1: Regenerate master index**

```bash
python scripts/build_index.py
```

Expected: `Wrote docs/index.md (...bytes)`.

- [ ] **Step 2: Verify index.md contains book card**

```bash
grep -c "Laws of Human Nature" docs/index.md
```

Expected: ≥ 1.

- [ ] **Step 3: Build the full site**

```bash
mkdocs build --strict
```

Expected: completes with no warnings/errors.

- [ ] **Step 4: Serve and browser-test**

```bash
mkdocs serve
```

Open `http://127.0.0.1:8000` in a browser. Verify:
- Master index shows the Laws of Human Nature card with cover
- Click into the book → sidebar shows index → chapters (18 entries) → research
- Open chapter 1 → slide iframe renders and plays
- Study Guide section appears in chapter 1 below the summary
- Dark mode toggle works
- Search "rationality" → returns chapter 1

Stop server with Ctrl-C.

- [ ] **Step 5: Commit regenerated index**

```bash
git add docs/index.md
git commit -m "Regenerate master index with Laws of Human Nature card"
```

---

## Phase G — Manual feedback workflow doc

### Task G1: Write feedback-protocol.md

**Files:**
- Create: `~/learning-from-books/feedback-protocol.md`

- [ ] **Step 1: Write the protocol document**

```markdown
# Feedback Protocol

This site improves with your input. Send an email to the address listed on any book's page; an action is taken and a reply with a link to the new or updated artifact is sent.

## How to send feedback

Each book has its own routing address: `learningfrombooks.feedback+<bookslug>@gmail.com`. The mailto link on every book page pre-fills the correct address.

Two reserved slugs:

- `+request@gmail.com` — request a new book be added (include title + author)
- `+meta@gmail.com` — site-level feedback (not about a specific book)

## Accepted feedback intents

| Intent | Example subject | What happens |
|---|---|---|
| **more-flashcards** | "More flashcards on chapter 3" | NotebookLM regenerates flashcards for that chapter |
| **infographic** | "Infographic for Law 7" | Nano Banana generates a new infographic |
| **summary-rephrase** | "Make chapter 2 summary simpler" | NotebookLM re-prompts with a style hint |
| **audio-language** | "Audio overview in Hindi" | NotebookLM language switch + regenerate |
| **slide-rework** | "Condensed deck too dense" | Slides regenerated with a new outline |
| **research-add** | "Found an author talk: <URL>" | URL appended to `research/author-talks.md` |
| **error** | "Typo in chapter 5, paragraph 4" | Fix in markdown |
| **general** | freeform | Manual judgment |

## Sample reader email

> **To:** learningfrombooks.feedback+lawsofhumannature@gmail.com
> **Subject:** Audio overview in Hindi
>
> Hi! Could you generate the audio overview for The Laws of Human Nature in Hindi as well? Would help me share it with family who don't read English fluently. Thanks.

## Service level (Phase 1, manual)

- Acknowledged within 24 hours
- Fulfilled within 48 hours

Phase 2 will automate this and tighten the SLA to: acknowledged within 1 hour, fulfilled within 4 hours.

## Manual workflow (operator reference)

When email arrives:

1. **Receive** — Gmail notification at `learningfrombooks.feedback+<slug>@gmail.com`
2. **Classify** — read subject + body; tag with one intent above
3. **Act** — open NotebookLM / Nano Banana / chapter file and generate or edit the artifact
4. **Place** — commit the new/changed file under `docs/books/<slug>/`
5. **Log** — append to `docs/books/<slug>/feedback/log.md`:

   ```markdown
   ## 2026-05-26 — chapter-3 flashcards expanded
   - **From**: reader@example.com
   - **Intent**: more-flashcards
   - **Action**: Regenerated NotebookLM flashcards for chapter 3, updated URL in book.yaml
   - **Commit**: <sha>
   - **Reply sent**: yes
   ```
6. **Push** — `git push` → GitHub Action deploys in ~90 seconds
7. **Reply** — respond to the original email with a Pages URL pointing to the new artifact
```

- [ ] **Step 2: Commit**

```bash
git add feedback-protocol.md
git commit -m "Add feedback-protocol.md: 8 intent types, reader templates, operator workflow"
```

---

## Phase H — Push and full Pages verification

### Task H1: Push the seeded content

- [ ] **Step 1: Push**

```bash
git push origin main
```

- [ ] **Step 2: Watch deploy**

```bash
gh run watch
```

Expected: green within 3 minutes.

- [ ] **Step 3: Acceptance browser checks on the live URL**

Open `https://<your-username>.github.io/learning-from-books-system-that-improves-with-your-feedback/` in a real browser. Tick each:

- [ ] Master index displays the Laws of Human Nature card with the cover image
- [ ] Clicking the card lands on book index page
- [ ] Sidebar shows 18 chapter entries plus the research section
- [ ] Search bar finds "rationality" → returns chapter 1
- [ ] Dark mode toggle works and persists across page reloads
- [ ] Chapter 1 slide iframe renders and plays
- [ ] Chapter 1 study guide section appears below summary
- [ ] Audio overview link on book index opens NotebookLM correctly
- [ ] `mailto:` on book index opens with `+lawsofhumannature` pre-filled
- [ ] Mobile viewport (browser dev tools, ≤768px): grid collapses to single column, sidebar collapses to burger menu, chapter pages readable
- [ ] Tags page lists all 8 seeded categories

- [ ] **Step 4: Test feedback email delivery**

From any personal email, send a message to `learningfrombooks.feedback+lawsofhumannature@gmail.com` with subject "Test feedback".

Open the new Gmail inbox. Confirm:
- Message arrived
- `Delivered-To` header reads `learningfrombooks.feedback+lawsofhumannature@gmail.com` (Gmail → ⋮ → Show original)

---

## Phase I — Migrate dba-site wiki copy to a stub

Tasks I1–I2 run in `/home/sanjayg4/dba-site/`, NOT in `~/learning-from-books/`.

### Task I1: Replace wiki content with a stub

**Files:**
- Delete: `/home/sanjayg4/dba-site/content/references/laws-of-human-nature/law-*.md` (18 files)
- Delete: `/home/sanjayg4/dba-site/content/references/laws-of-human-nature/study-guides/` (entire dir)
- Delete: `/home/sanjayg4/dba-site/content/references/laws-of-human-nature/infographics/` (entire dir)
- Modify: `/home/sanjayg4/dba-site/content/references/laws-of-human-nature/index.md` (full rewrite)

- [ ] **Step 1: Switch to dba-site and create a branch**

```bash
cd /home/sanjayg4/dba-site
git checkout main
git pull
git checkout -b lfb-stub-replacement
```

- [ ] **Step 2: Verify nothing else links to this content (safety check)**

```bash
grep -rln "laws-of-human-nature" content/ | grep -v "references/laws-of-human-nature" | head
```

Expected: empty output. If any results appear, STOP — manual handling needed for those files; do not proceed until reviewed.

- [ ] **Step 3: Rewrite the index file**

Replace `content/references/laws-of-human-nature/index.md` with:

```markdown
---
title: "Laws of Human Nature → Moved"
---

# Laws of Human Nature

The full companion (chapters, study guides, slides, audio overview, infographics)
now lives in the **Learning From Books** system:

→ https://<your-username>.github.io/learning-from-books-system-that-improves-with-your-feedback/books/laws-of-human-nature/

Feedback or requests: `learningfrombooks.feedback+lawsofhumannature@gmail.com`
```

Replace `<your-username>` with the actual GitHub username.

- [ ] **Step 4: Delete the migrated content**

```bash
cd /home/sanjayg4/dba-site/content/references/laws-of-human-nature
rm law-*.md
rm -r study-guides infographics
ls
```

Expected: only `index.md` remains.

- [ ] **Step 5: Commit on the branch**

```bash
cd /home/sanjayg4/dba-site
git add content/references/laws-of-human-nature/
git commit -m "Replace Laws of Human Nature wiki copy with stub pointing to Learning From Books site"
```

- [ ] **Step 6: Push and open PR**

```bash
git push -u origin lfb-stub-replacement
gh pr create --title "Move Laws of Human Nature content out to Learning From Books site" \
  --body "All chapter pages, study guides, and infographics now live in the dedicated Learning From Books repo. This wiki page becomes a discoverable stub linking out. Safe revert if needed: \`git revert HEAD\`."
```

Expected: PR URL printed.

- [ ] **Step 7: Merge after self-review**

Open the PR URL, verify the diff, merge.

### Task I2: Confirm Quartz wiki still builds

- [ ] **Step 1: Run Quartz build locally**

```bash
cd /home/sanjayg4/dba-site
npx quartz build
```

Expected: build succeeds, no broken-link errors related to the removed content.

- [ ] **Step 2: No commit needed** (verification only)

---

## Phase J — Final acceptance walkthrough

### Task J1: Run the full acceptance checklist

**Files:** none (checklist execution against the spec)

Open `docs/superpowers/specs/2026-05-25-learning-from-books-phase-1-design.md` in the brainstorm worktree (or the spec file in the new repo if copied over). Walk the **§11 Acceptance criteria** section top to bottom. Each checkbox in the spec must be ticked based on real observation.

- [ ] **Step 1: Run the Infrastructure block** (10 checks) — confirm repo exists, branch state, requirements pinned, `mkdocs serve` works, `mkdocs build --strict` passes, Pages deployment green, URL returns 200.

- [ ] **Step 2: Run the Content block** (9 checks) — confirm `book.yaml` populated, 18 chapters present, chapter 1 slide URL real, study guide merged, infographics displayed, cover renders, log.md exists, research stubs present, feedback-protocol.md committed.

- [ ] **Step 3: Run the Visual & UX block** (11 checks) — open live URL in real browser, click through each item.

- [ ] **Step 4: Run the Operational block** (6 checks) — verify Gmail, AI Studio key (Phase 2 prep), Drive folder, NotebookLM workspace, wiki stub.

- [ ] **Step 5: Run the Documentation block** (3 checks) — README, feedback-protocol, book landing page.

- [ ] **Step 6: Definition of done test**

On a mobile phone (not a desktop browser emulation), open the live Pages URL. Navigate to Laws of Human Nature → chapter 1. Verify the slide deck plays. Send a test feedback email from the phone's mail app. Verify it arrives in the inbox with the correct plus-address header.

- [ ] **Step 7: Final commit (if any unticked items needed last-mile fixes)**

```bash
cd ~/learning-from-books
git status
# resolve any remaining issues, commit, push
```

- [ ] **Step 8: Tag the milestone**

```bash
git tag -a phase-1-complete -m "Phase 1 shipped: Laws of Human Nature seed live on GitHub Pages with manual feedback workflow"
git push origin phase-1-complete
```

---

## Definition of Phase 1 done

All checkboxes in spec §11 pass. User can open the live Pages URL on a phone, find Laws of Human Nature, read chapter 1 with the embedded slides and study guide, and send a feedback email that lands in the Gmail inbox with the correct `+lawsofhumannature` tag.

---

## Self-review notes (plan author)

**Spec coverage check:**

- §6 Repository layout → Tasks B1, C1–C3, D2–D3
- §7 MkDocs config → Tasks C1, C2, C3
- §8 GitHub Actions deployment → Tasks E1, E2
- §9 Phase 1 manual feedback workflow → Task G1 + Operational tasks A1–A4
- §10 Seed migration: Laws of Human Nature → Tasks F1, F2, F3, F4, F5, F6
- §10 Fate of dba-site wiki copy → Tasks I1, I2
- §11 Acceptance criteria → Task J1 walks the spec checklist
- §12 Risks/mitigations → Documented in spec; Phase 1 is manual so the NotebookLM-automation risk doesn't bite yet

**Placeholders:** none. Every step has actual code/commands.

**Type consistency:** the `book.yaml` schema in F2 (migration), D3 (new_book.py template), and D2 (build_index reads) all use the same field names: `title`, `author`, `year`, `slug`, `categories`, `status`, `chapters_total`, `cover`, `last_updated`, plus the URL set.

**Test coverage:** `build_index.py` (D1) and `migrate_laws_of_human_nature.py` (F1) both have failing-test-first cycles. `new_book.py` (D3) uses a smoke-test pattern instead of pytest because it's a scaffolding utility — full TDD here would add complexity without catching real bugs.
