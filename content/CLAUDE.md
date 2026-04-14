# DBA Knowledge Base — Agent Context

This is a personal knowledge base for a Doctorate in Business Administration (DBA) in AI, structured as a Karpathy-style LLM Wiki. Raw sources (course PDFs, worksheets, arXiv papers, lecture transcripts) are compiled by an LLM into dense, cross-linked markdown pages. No embeddings, no vector DB — the LLM reads markdown directly.

The framework skills live at `/home/sanjayg4/src/obsidian-wiki/.skills/`. The canonical agent contract is at that repo's `AGENTS.md`. Follow those skill routing rules when the user says things like "ingest this", "what do I know about X", "lint the wiki", etc.

## Vault Layout

```
/home/sanjayg4/dba-kb/
├── index.md           # master catalog, kept current after every op
├── log.md             # chronological ledger, append-only
├── .manifest.json     # per-source tracking (created on first ingest)
├── _meta/
│   └── taxonomy.md    # controlled tag vocabulary (edit before adding new tags)
├── _raw/              # staging area — drop rough notes, ingest promotes them
├── _archives/         # snapshots from /wiki-rebuild
├── concepts/          # atomic abstract ideas
├── entities/          # people, orgs, models, datasets, tools
├── skills/            # how-to knowledge
├── references/        # factual specs, APIs, configs
├── synthesis/         # cross-cutting analysis
├── journal/           # time-bound entries
└── projects/          # per-project summaries from /wiki-update
```

## DBA-specific conventions

- **Course content**: filename pattern `course/<course-code>-<slug>.pdf` in the source drop directory (to be configured in `.env` → `OBSIDIAN_SOURCES_DIR`). Summaries go to `references/<course-code>-<slug>.md` with frontmatter `category: references`, tag `#src/course`.
- **Worksheets**: the user's own assignments. Summaries go to `synthesis/worksheet-<YYYY-MM-DD>-<slug>.md`, tag `#dba/worksheet`. These represent your own thinking, so link them densely to `concepts/` pages.
- **arXiv papers**: `references/arxiv-<id>-<slug>.md`, tag `#src/paper`. Always extract entities (authors, model names, datasets) into `entities/` and abstract ideas into `concepts/`.
- **Lecture transcripts**: `journal/lecture-<YYYY-MM-DD>-<slug>.md`, tag `#src/transcript`. Extract concepts into `concepts/` as usual.
- **Citations**: use `[[wikilinks]]` within the wiki. When citing raw sources, include the raw filename and page anchor if applicable (e.g. `_raw/papers/attention.pdf#page=5`).

## Frontmatter (required on every wiki page)

```yaml
---
title: <human-readable title>
category: <concepts|entities|skills|references|synthesis|journal|projects>
tags: [<from _meta/taxonomy.md>]
sources: [<paths to raw files or other wiki pages>]
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---
```

## Core principles

- **Compile, don't retrieve** — when ingesting a new source, update existing related pages rather than duplicating content.
- **Track everything** — after any op, update `.manifest.json` (for ingests), `index.md`, and `log.md`.
- **Connect densely** — every page should link to its neighbors with `[[wikilinks]]`. That's what makes this a graph, not a folder.
- **Atomic pages** — one concept per file. Long combined pages defeat the graph.
- **Human vs LLM** — you (the human) own sourcing and questions. The LLM owns summarizing, cross-linking, and bookkeeping.

## Reference

Framework spec: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
Framework repo: https://github.com/Ar9av/obsidian-wiki
