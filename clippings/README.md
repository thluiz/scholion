# Clippings

Web pages captured as raw material for [Scholion](https://github.com/thluiz/scholion)
research and notes. Private and versioned, but never published directly —
the public site only references the original URL when something here
becomes a citation or a `webclip` note.

This lives at the repo's top level (not under `content/`), so Hugo
never builds it into the public site — it has no `contentDir` override,
so it only reads `content/` by default.

## Structure

```
clippings/<YYYY-MM>/<domain>--<title-slug>.md
```

- `<YYYY-MM>`: month of capture (not of the original page's publication).
- `<domain>`: site domain without `www.` (e.g. `nytimes-com`, `wikipedia-org`).
- `<title-slug>`: slug of the page title.

Example: `clippings/2026-09/nytimes-com--article-title.md`

## Frontmatter

```yaml
---
url: "https://example.com/original-page"
captured_at: "2026-09-23T14:32:00-03:00"
title: "Page title as captured"
domain: "example-com"
---
```

`captured_at` is the real capture timestamp (not the page's own
publication date) — it's what backs the citation if the original page
later changes or goes offline.

## Usage

This material is a starting point, not a finished product. The skill
`add-scholion-webclip` captures a page (via Playwright, or Claude in
Chrome as a fallback for sites needing a logged-in session) into this
folder, then generates a `category: webclip` note in `content/notes/`
with a summary and a structured fichamento — and, on request, separate
`category: quote` notes for specific phrases from the same page. Raw
clippings are never pasted directly into a note; the note is always
composed prose that goes through the normal ghost-writer/ghost-audit
pipeline.
