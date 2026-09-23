# Batch webclip playbook — legacy OneDrive\MD backlog

Processes pre-captured `.md` files (browser-extension clippings: MarkDownload/Obsidian
Web Clipper format, frontmatter `created`/`tags`/`source`/`author`) from
`C:\Users\conta\OneDrive\MD\` into `category: webclip` notes. Batch mode: **no
per-item authorization, no interactive search-first wait** — this deliberately
departs from the interactive `add-scholion-webclip` SKILL.md for this one
backlog-clearing job (that skill's own one-commit-per-artefact rule is also
relaxed here — see step 9, batch mode commits once per batch run, not per
artefact). Everything else from that skill (ghost-writer voice,
source-or-silence, style-test + ghost-audit gate, no cross-links per author
request, no Co-Authored-By) still applies in full.

## Your assignment

**Never use the Monitor tool in this job.** A prior batch stalled twice
("waiting for the monitor's completion notification") and ended its turn
without ever reaching the commit step, leaving many staged/untracked files
behind for someone else to clean up. Ghost-audit and style-test are both
synchronous HTTP/CLI calls you wait on directly — there is nothing here that
needs a background monitor.

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

3. **No cross-link search.** Do not `Grep` the vault for related notes and do
   not add cross-links to other Scholion notes in the fichamento (i.e. call
   the endpoint below with no `relatedNotes`). This backlog is high-volume,
   low-context-per-item; cross-linking was cut by the author's explicit
   request partway through the run. Earlier notes in this batch job do have
   links — leave those as they are, just don't add more.

4. **Compose via the `webclip-summary` endpoint** (server-side, same call as
   `add-scholion-webclip/SKILL.md` step 5 — read that file once at the start
   of your batch too). POST `{text, title, url, domain}` (no `relatedNotes`,
   per item 3 above) to
   `http://localhost:8080/api/vox-intelligence/presets/scholion/webclip-summary`.
   Language, PT-BR-vs-structural voice rules, and PT-EU avoidance are all
   handled by the endpoint's prompt — do NOT read the full body into your own
   context or compose by hand; that defeats the point of moving this
   server-side. Use `$r.slug`, `$r.title`, `$r.summary`, `$r.tags`, `$r.body`
   directly. `has_commentary: false`. `sources`: two entries — the original
   url (`kind` inferred from domain) and the GitHub archived copy:
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

5. **Real timestamp** for the note's own `date`: run `date
   +"%Y-%m-%dT%H:%M:%S%:z"` fresh — never reuse a timestamp from a previous
   file in your batch, never invent one.

6. **Save the clipping** at
   `E:\scholion\clippings\<YYYY-MM>\<domain>--<slug>.md` (domain = host of
   `source`, no `www.`, dots → `-`; slug from the title). Frontmatter: `url`
   (= `source`), `captured_at` (= `created`, reformatted to
   `YYYY-MM-DDTHH:MM:SS±HH:MM` if needed), `title`, `domain`. Body = the
   captured text (refetched version if step 2 refetched, otherwise the
   original).

7. **Write the note** to `E:\scholion\content\notes\<slug>.md`.

8. **Audit — mandatory, same gate as everywhere else in this repo:**
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
     clipping from step 6 still gets committed (matéria-prima has value on
     its own). Move the source file to `_processed` anyway (it's archived,
     just missing a polished note) and continue to the next file.

9. **Stage as you go, commit once at the end of your whole batch.** This
    replaces the earlier "two commits per item" rule — changed at the
    author's request to cut commit volume. For each item: `git add
    clippings/<YYYY-MM>/<file>.md`, and if the note passed the gate, build
    check (`cd /e/scholion && hugo --quiet`, skip *this note* if it fails)
    → `git add content/notes/<slug>.md` → write its commit-gate marker
    immediately (don't defer this part):
    ```powershell
    $o = git -C E:\scholion rev-parse ":content/notes/<slug>.md"
    New-Item -ItemType Directory -Force E:\scholion\.ghost-audit | Out-Null
    Set-Content "E:\scholion\.ghost-audit\$o.ok" $o
    ```
    Keep a running list of every path you `git add`ed. When your whole batch
    is done (all N files handled), commit **once**, for exactly your paths,
    with `git commit --only -m "<msg>" -- <path1> <path2> ...` (never a bare
    `git commit` — this repo has other concurrent activity, e.g. a scheduled
    publish task's pre-push hook and possibly other live sessions; `--only`
    with an explicit path list is what stays immune to sweeping in someone
    else's staged file). Message format: `"webclip batch: N items ([list of
    slugs, or file count if long])"`. No `Co-Authored-By` line — ever, this
    machine's rule overrides any session default. **Do not `git push`** —
    the orchestrator pushes between batches, not you.

10. **Move the source file** from `C:\Users\conta\OneDrive\MD\<file>.md` to
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
