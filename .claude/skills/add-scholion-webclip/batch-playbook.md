# Batch webclip playbook — legacy OneDrive\MD backlog

Processes pre-captured `.md` files (browser-extension clippings: MarkDownload/Obsidian
Web Clipper format, frontmatter `created`/`tags`/`source`/`author`) from
`C:\Users\conta\OneDrive\MD\` into `category: webclip` notes, via the
`scholion-webclipper` API (see `E:\scholion-webclipper\README.md`) — same
backend the interactive `add-scholion-webclip/SKILL.md` uses, different
principal (`add-scholion-webclip-batch`, its own rate-limit window — see
that repo's `.env.example`). Batch mode: **no per-item authorization, no
interactive search-first wait, no per-item commit** — deliberate departures
from the interactive skill for this one backlog-clearing job. Everything
else (ghost-writer voice, source-or-silence, the audit gate, no cross-links
per author request, no Co-Authored-By) still applies in full.

## Your assignment

**Never use the Monitor tool in this job.** A prior batch stalled twice
("waiting for the monitor's completion notification") and ended its turn
without ever reaching the commit step, leaving many staged/untracked files
behind for someone else to clean up. Every call to `scholion-webclipper` is
a synchronous HTTP request you wait on directly — there is nothing here
that needs a background monitor.

Take the next **N files** (N given in your prompt, usually 12–18) from the
**root** of `C:\Users\conta\OneDrive\MD\` (`.md` files only — ignore
subfolders, those are already sorted: `_excluded_sensitive`,
`_excluded_immersao`, `_excluded_work`, `_skip_youtube`,
`_needs_url_review`, `_excluded_duplicate`, `_processed`). Process them one at a time, in order,
**sequentially — never spawn your own subagents or forks for this batch**
(a prior run that self-parallelized produced duplicate slugs and burned
2-3x the tokens of a clean sequential run). Stop after N files (success or
skip both count) and report a summary.

Read the API key once, before the first file:

```powershell
$webclipKey = Get-Content 'C:\Users\conta\.claude\secrets\scholion-webclipper-batch.key' -Raw
```

## Per-file pipeline

1. **Read the file.** Frontmatter has `created` (ISO-ish timestamp), `source`
   (the real URL — already validated real, not `chrome-extension://`, in this
   queue), `title` is the first `# H1`. Strip known junk markers before
   judging content quality: `Navigating to Notifications`, `More for You`,
   `Enjoy the videos and music you love`, `Continuar a ler`,
   `Embedded Content`, `## 0 notifications`, `> ## Excerpt`.

2. **Compose.** Reformat `created` to `capturedAt`. Every file in this
   backlog has `created` as `2026-01-09T13:09:52 (UTC -03:00)` — the
   server validates `capturedAt` and rejects that shape outright, it wants
   `2026-01-09T13:09:52-03:00`: drop the space and the `(UTC `/`)` wrapper,
   concatenate the offset directly onto the timestamp, nothing else
   changes. (`<YYYY-MM>` for both the clipping folder and the note's `date`
   comes from *this* value, not today's date.) No `relatedNotes` —
   cross-link search stays off for this backlog (author's explicit
   request; unlike the interactive skill, don't even run the search).

   **If the cleaned body is ≥ ~400 chars**, compose in text mode — this is
   the common case, the pre-captured content is already good enough:
   ```powershell
   $body = @{ text = '<cleaned body>'; title = '<title>'; url = '<source>'; domain = '<host of source, no www., dots to hyphens>'; capturedAt = '<reformatted created>' } | ConvertTo-Json
   $r = Invoke-RestMethod -Uri 'http://localhost:8080/api/webclip/webclip/compose' -Method Post -Headers @{ 'X-Api-Key' = $webclipKey } -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 300
   ```

   **If the cleaned body is < ~400 chars**, compose in URL mode instead — the
   service does a fresh Playwright+Readability capture server-side (better
   extraction than the old local `fetch-webclip.mjs` this step used to call):
   ```powershell
   $body = @{ url = '<source>'; capturedAt = '<reformatted created>' } | ConvertTo-Json
   $r = Invoke-RestMethod -Uri 'http://localhost:8080/api/webclip/webclip/compose' -Method Post -Headers @{ 'X-Api-Key' = $webclipKey } -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 300
   ```
   If this also errors (`thin_content`, `blocked_domain`, `consent_wall_unresolved`,
   `fetch_timeout`/`fetch_failed` after one retry) — **skip this file**: log
   it (see Logging) as `thin_unrecoverable`, move it to `_needs_url_review`
   (not `_processed` — it still needs a human, or a Chrome-in-the-loop
   fallback, to capture properly), and move on to the next file. No cascade
   of Playwright→WebFetch→curl attempts — one clean try at each mode, then
   skip. `blocked_domain` in particular means don't retry at all, same
   domain will just refuse again.

3. **Audit — read `$r.audit`, don't call anything separately.** Ghost-audit
   already ran inside `compose` (see the interactive skill's own "PORTÃO
   OBRIGATÓRIO" for why there's no standalone HTTP call anymore).

   - `verdict: green` or `yellow` → proceed to step 4. Yellow findings are
     logged, never a reason to loop — this backlog stops at zero `block`
     findings, it does not chase an absolute green (same principle the
     `ghost-audit` skill itself documents).
   - `verdict: red` → **recompose once** (call `compose` again, identical
     input — there's no way to hand feedback into `compose`, so this is a
     second roll, not a fix). Still red → the note is a bust, but the
     `clipping` field is still usable (compose returns it regardless of
     verdict). Write **only** the clipping (step 4b), skip the note, log
     `audit_unresolved`, move the source file to `_processed` anyway (it's
     archived, just missing a polished note).

4. **Write the files.**

   **4a. Note passed (green/yellow):** save in `mode: "return"` — batch
   mode stages its own writes and commits once at the end (step 6), it does
   not want `scholion-webclipper`'s own `vault/` commit:
   ```powershell
   $saveBody = @{ mode = 'return' } | ConvertTo-Json
   $s = Invoke-RestMethod -Uri "http://localhost:8080/api/webclip/webclip/$($r.operationId)/save" -Method Post -Headers @{ 'X-Api-Key' = $webclipKey } -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($saveBody)) -TimeoutSec 60
   ```
   Write `$s.clippingContent` to `E:\scholion\$($s.clippingPath)` and
   `$s.noteContent` to `E:\scholion\$($s.notePath)` verbatim — don't edit
   either (an edit means calling `compose` again, per the interactive
   skill's Decision 8 note).

   **4b. Note skipped (red after recompose):** `save` was never called (it
   refuses red without `webclip.save.force`, which this principal doesn't
   have), so build the clipping file by hand — same shape
   `scholion-webclipper` itself renders. **Use the `$capturedAt`/`$url`/
   `$domain`/`$title` values you already had in step 2, not
   `$r.clipping.*`** — `Invoke-RestMethod` silently parses a JSON string
   that looks like a date into a `[DateTime]` object, which drops the
   original UTC offset (`2026-08-15T09:30:00-03:00` comes back as
   `08/15/2026 13:30:00`, reinterpreted in the local machine's timezone).
   `$r.clipping.markdown` is safe to use as-is (a multi-line string is
   never mistaken for a date):
   ```yaml
   ---
   url: "<$url, from step 2>"
   captured_at: "<$capturedAt, from step 2>"
   title: "<$title, from step 2>"
   domain: "<$domain, from step 2>"
   ---

   <$r.clipping.markdown, verbatim>
   ```
   at `E:\scholion\clippings\<YYYY-MM of $capturedAt>\<domain>--<slug derived from title>.md`.

5. **Commit-gate marker (note only, only when written).** Same reasoning as
   the interactive skill's Decision-10 note: the note text was already
   audited inside `compose`, so pre-empt the `ghost-audit-gate.ps1` hook
   re-auditing it at commit time — write the marker straight from the
   verdict already in hand, right after staging:
   ```powershell
   $o = git -C E:\scholion rev-parse ":$($s.notePath)"
   New-Item -ItemType Directory -Force E:\scholion\.ghost-audit | Out-Null
   Set-Content "E:\scholion\.ghost-audit\$o.ok" $o
   ```

6. **Stage as you go, commit once at the end of your whole batch.** For
   each item: `git add` whatever you wrote (clipping always; note only if
   step 4a happened), build check (`cd /e/scholion && hugo --quiet`, skip
   *this note* — not the clipping — if it fails), write the commit-gate
   marker (step 5) immediately, don't defer it. Keep a running list of
   every path you `git add`ed. When your whole batch is done (all N files
   handled), commit **once**, for exactly your paths, with
   `git commit --only -m "<msg>" -- <path1> <path2> ...` (never a bare
   `git commit` — this repo has other concurrent activity, e.g. a scheduled
   publish task's pre-push hook and possibly other live sessions; `--only`
   with an explicit path list is what stays immune to sweeping in someone
   else's staged file). Message format: `"webclip batch: N items ([list of
   slugs, or file count if long])"`. No `Co-Authored-By` line — ever, this
   machine's rule overrides any session default. **Do not `git push`** —
   the orchestrator pushes between batches, not you.

7. **Move the source file** from `C:\Users\conta\OneDrive\MD\<file>.md` to
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
