# Batch webclip playbook — legacy OneDrive\MD backlog

Processes pre-captured `.md` files (browser-extension clippings: MarkDownload/Obsidian
Web Clipper format, frontmatter `created`/`tags`/`source`/`author`) from
`C:\Users\conta\OneDrive\MD\` into `category: webclip` notes. Batch mode: **no
per-item authorization, no interactive search-first wait** — this deliberately
departs from the interactive `add-scholion-webclip` SKILL.md for this one
backlog-clearing job. Everything else from that skill (ghost-writer voice,
source-or-silence, style-test + ghost-audit gate, one commit per artefact, no
Co-Authored-By) still applies in full.

## Your assignment

Take the next **N files** (N given in your prompt, usually 12–18) from the
**root** of `C:\Users\conta\OneDrive\MD\` (`.md` files only — ignore
subfolders, those are already sorted: `_excluded_sensitive`,
`_excluded_immersao`, `_skip_youtube`, `_needs_url_review`,
`_excluded_duplicate`, `_processed`). Process them one at a time, in order.
Stop after N files (success or skip both count) and report a summary.

## Per-file pipeline

1. **Read the file.** Frontmatter has `created` (ISO-ish timestamp), `source`
   (the real URL — already validated real, not `chrome-extension://`, in this
   queue), `title` is the first `# H1`. Strip known junk markers before
   judging content quality: `Navigating to Notifications`, `More for You`,
   `Enjoy the videos and music you love`, `Continuar a ler`,
   `Embedded Content`, `## 0 notifications`, `> ## Excerpt`.

2. **Quality check.** If cleaned body < ~400 chars: try
   `node E:\scholion\.claude\skills\add-scholion-webclip\fetch-webclip.mjs "<source url>"`
   for a fresh Playwright capture. If that also comes back thin/empty/error:
   use whatever text exists if it's enough to support at least 2–3 honest
   fichamento bullets; if truly nothing (just nav junk), **skip this file** —
   log it (see Logging) and move it to `_needs_url_review` (not `_processed` —
   it still needs a human, or a Chrome-in-the-loop fallback, to capture
   properly), and move on to the next file.

3. **Detect language** of the body (Portuguese vs English vs other). The note
   you compose — resumo, fichamento, `summary`, `tags` — is written in **that**
   language, not forced PT-BR. This is a deliberate exception to the
   Scholion-wide PT-BR rule (see `add-scholion-webclip/SKILL.md` step 6). If
   the body is Portuguese, apply `ghost-writer`'s full PT-BR lexical rules
   (banned vocabulary table). If English (or other), apply only the
   **structural** anti-AI rules from `ghost-writer` (no mechanical
   parallelism, no three-beat setup/twist/punch, no em-dash pause-punch, no
   aphoristic mini-closes, no meta-narration, no indirect-negative
   constructions, vary sentence openings) — read
   `C:\Users\conta\.claude\skills\ghost-writer\SKILL.md` once at the start of
   your batch and keep it active while composing every note in your batch.

4. **Cross-links (batch mode, no waiting)**: `Grep` `E:\scholion\content\notes\`
   and `E:\scholion\content\research\` for the page's central theme/keyword.
   Link in the fichamento **only** on a strong, obviously-on-topic match (a
   note whose title/theme is essentially the same subject — not a loose
   thematic echo). No match, or only a loose one: don't force a link. Don't
   ask — decide and move on.

5. **Compose the note** (resumo 1–2 paragraphs + `## Fichamento` with
   paraphrased bullets, per `add-scholion-webclip/SKILL.md` steps 6–12 —
   read that file once at the start of your batch too). `has_commentary:
   false`. Tags 2–4 kebab-case in the note's language. `sources`: two entries
   — the original url (`kind` inferred from domain) and the GitHub archived
   copy:
   ```yaml
   sources:
     - title: "<title>"
       url: "<source>"
       kind: article   # or video/wiki/repo/etc per domain
     - title: "Raw clipping (archived copy)"
       url: "https://github.com/thluiz/scholion/blob/main/clippings/<YYYY-MM>/<file>.md"
       kind: repo
   ```
   `<YYYY-MM>` is derived from the file's own `created` field, not today's date.

6. **Real timestamp** for the note's own `date`: run `date
   +"%Y-%m-%dT%H:%M:%S%:z"` fresh — never reuse a timestamp from a previous
   file in your batch, never invent one.

7. **Save the clipping** at
   `E:\scholion\clippings\<YYYY-MM>\<domain>--<slug>.md` (domain = host of
   `source`, no `www.`, dots → `-`; slug from the title). Frontmatter: `url`
   (= `source`), `captured_at` (= `created`, reformatted to
   `YYYY-MM-DDTHH:MM:SS±HH:MM` if needed), `title`, `domain`. Body = the
   captured text (refetched version if step 2 refetched, otherwise the
   original).

8. **Write the note** to `E:\scholion\content\notes\<slug>.md`.

9. **Audit — mandatory, same gate as everywhere else in this repo:**
   - `cd /e/scholion && STYLE_TEST_FILTER=<slug> python -m pytest tests/style/ --tb=short`
   - Ghost-audit HTTP (PowerShell, see `add-scholion-webclip/SKILL.md` top
     section for the exact call). Read `$r.'x-parsed'`.
   - `verdict: green` → proceed.
   - `verdict: yellow` or `red`: apply the tool's own `suggestion` per
     finding (same discipline as the worked example in this session's
     `i-dont-like-llms` note — direct fixes, no reactive rewriting beyond
     what the finding actually names) and **re-run ghost-audit**. Up to
     **2 fix attempts total** per note.
   - Still not green after 2 attempts → **skip this note**: delete the
     draft `content/notes/<slug>.md`, log it (see Logging), but the
     clipping from step 7 still gets committed (matéria-prima has value on
     its own). Move the source file to `_processed` anyway (it's archived,
     just missing a polished note) and continue to the next file.

10. **Commits** (repo `E:\scholion`, no `Co-Authored-By` line — ever, this
    machine's rule overrides any session default). **Two separate commits,
    never bundled** — stage and commit the clipping FIRST, on its own, before
    writing the note file at all. Confirm with `git status` that the clipping
    commit is clean (nothing else staged) before moving to step 8. A prior
    batch bundled clip+note into one commit by mistake; don't repeat that.
    - `git add clippings/<YYYY-MM>/<file>.md && git commit -m "clip: <title>"`
    - If the note passed the gate: build check
      (`cd /e/scholion && hugo --quiet`, abort *this note's* commit if
      exit ≠ 0, log+skip same as a failed audit) → `git add
      content/notes/<slug>.md` → commit-gate marker:
      ```powershell
      $o = git -C E:\scholion rev-parse ":content/notes/<slug>.md"
      New-Item -ItemType Directory -Force E:\scholion\.ghost-audit | Out-Null
      Set-Content "E:\scholion\.ghost-audit\$o.ok" $o
      ```
      → `git commit -m "note: <title>"`. **Do not `git push`** — the
      orchestrator pushes once per batch, not per note (keeps push volume
      sane and lets it check in between batches).

11. **Move the source file** from `C:\Users\conta\OneDrive\MD\<file>.md` to
    `C:\Users\conta\OneDrive\MD\_processed\<file>.md` — this is what makes
    the batch resumable after an interruption: whatever is still sitting in
    the root of `OneDrive\MD\` is what's left to do.

## Logging

Append one line per skip (never for successes) to
`E:\scholion\clippings\_batch-log.md` (create with a `# Batch skip log`
header if it doesn't exist):

```
- SKIP <original filename> — <reason: thin_unrecoverable | audit_unresolved | build_failed> — <one-line detail>
```

## End of batch

Report: how many processed clean, how many skipped (and why, briefly), and
the count of `.md` files still left in `OneDrive\MD\` root afterward.
