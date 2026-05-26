#!/usr/bin/env python3
"""Render a markdown spec to a standalone HTML file for easy review."""
import sys
from pathlib import Path
import markdown

src = Path(sys.argv[1])
dst = Path(sys.argv[2])
md_text = src.read_text()
title = src.stem.replace("-", " ").title()

html_body = markdown.markdown(
    md_text,
    extensions=[
        "tables",
        "fenced_code",
        "toc",
        "attr_list",
        "def_list",
        "admonition",
        "pymdownx.superfences",
        "pymdownx.tasklist",
        "pymdownx.details",
    ],
    extension_configs={
        "toc": {"permalink": True, "toc_depth": "2-4"},
        "pymdownx.tasklist": {"custom_checkbox": True},
    },
)

css = """
:root {
  --bg: #ffffff;
  --fg: #1a202c;
  --fg-muted: #4a5568;
  --accent: #4f46e5;
  --accent-bg: #eef2ff;
  --border: #e2e8f0;
  --code-bg: #f7fafc;
  --code-fg: #2d3748;
  --table-stripe: #f9fafb;
  --pre-bg: #1a202c;
  --pre-fg: #e2e8f0;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0f172a;
    --fg: #e2e8f0;
    --fg-muted: #94a3b8;
    --accent: #818cf8;
    --accent-bg: #1e1b4b;
    --border: #334155;
    --code-bg: #1e293b;
    --code-fg: #cbd5e1;
    --table-stripe: #1e293b;
    --pre-bg: #020617;
    --pre-fg: #e2e8f0;
  }
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Inter", Roboto, sans-serif;
  background: var(--bg);
  color: var(--fg);
  max-width: 920px;
  margin: 0 auto;
  padding: 2.5rem 1.5rem 6rem;
  line-height: 1.65;
  font-size: 16px;
}
h1 {
  font-size: 2.25rem;
  border-bottom: 3px solid var(--accent);
  padding-bottom: 0.75rem;
  margin-top: 0;
  margin-bottom: 1.5rem;
  letter-spacing: -0.02em;
}
h2 {
  font-size: 1.6rem;
  border-bottom: 1px solid var(--border);
  padding-bottom: 0.4rem;
  margin-top: 3rem;
  margin-bottom: 1rem;
  color: var(--accent);
  letter-spacing: -0.01em;
}
h3 {
  font-size: 1.25rem;
  margin-top: 2rem;
  margin-bottom: 0.6rem;
  color: var(--fg);
}
h4 { font-size: 1.05rem; margin-top: 1.5rem; color: var(--fg-muted); }
.headerlink { opacity: 0; margin-left: 0.5rem; text-decoration: none; color: var(--fg-muted); }
h1:hover .headerlink, h2:hover .headerlink, h3:hover .headerlink, h4:hover .headerlink { opacity: 1; }
p { margin: 0.75rem 0; }
a { color: var(--accent); text-decoration: none; border-bottom: 1px dotted var(--accent); }
a:hover { border-bottom-style: solid; }
code {
  background: var(--code-bg);
  color: var(--code-fg);
  padding: 0.15rem 0.4rem;
  border-radius: 4px;
  font-family: "SF Mono", Menlo, Consolas, monospace;
  font-size: 0.88em;
}
pre {
  background: var(--pre-bg);
  color: var(--pre-fg);
  padding: 1rem 1.25rem;
  border-radius: 8px;
  overflow-x: auto;
  font-size: 0.85em;
  line-height: 1.5;
  margin: 1rem 0;
}
pre code { background: transparent; color: inherit; padding: 0; }
blockquote {
  border-left: 4px solid var(--accent);
  background: var(--accent-bg);
  padding: 0.6rem 1rem;
  margin: 1rem 0;
  border-radius: 0 6px 6px 0;
  color: var(--fg-muted);
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.25rem 0;
  font-size: 0.92em;
}
th, td {
  border: 1px solid var(--border);
  padding: 0.55rem 0.85rem;
  text-align: left;
  vertical-align: top;
}
th {
  background: var(--accent-bg);
  color: var(--accent);
  font-weight: 600;
  font-size: 0.85em;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}
tr:nth-child(even) td { background: var(--table-stripe); }
ul, ol { padding-left: 1.5rem; }
li { margin: 0.35rem 0; }
.task-list-item { list-style-type: none; margin-left: -1.5rem; }
.task-list-item input[type="checkbox"] {
  margin-right: 0.5rem;
  transform: scale(1.15);
  accent-color: var(--accent);
}
hr {
  border: 0;
  border-top: 2px dashed var(--border);
  margin: 2.5rem 0;
}
.toc {
  background: var(--accent-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1rem 1.5rem;
  margin: 1.5rem 0 2.5rem;
}
.toc > ul { padding-left: 1.25rem; }
.toc ul ul { padding-left: 1.25rem; margin: 0.2rem 0; }
.toc a { border-bottom: none; }
.toc a:hover { border-bottom: 1px dotted var(--accent); }
.toctitle {
  font-weight: 600;
  font-size: 1rem;
  margin-bottom: 0.5rem;
  color: var(--accent);
}
.admonition {
  border-left: 4px solid var(--accent);
  background: var(--accent-bg);
  padding: 0.8rem 1.2rem;
  margin: 1rem 0;
  border-radius: 0 6px 6px 0;
}
.admonition-title {
  font-weight: 600;
  margin: 0 0 0.4rem;
  color: var(--accent);
}
@media (max-width: 640px) {
  body { padding: 1.5rem 1rem 4rem; font-size: 15px; }
  h1 { font-size: 1.75rem; }
  h2 { font-size: 1.35rem; }
  pre { font-size: 0.78em; }
  table { font-size: 0.85em; }
  th, td { padding: 0.4rem 0.5rem; }
}
"""

html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
{html_body}
</body>
</html>
"""

dst.write_text(html_doc)
print(f"Wrote {dst} ({len(html_doc):,} bytes)")
