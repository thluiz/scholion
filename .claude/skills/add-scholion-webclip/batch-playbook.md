# Batch webclip playbook — unified queue

Processes the unified backlog at `C:\Users\conta\OneDrive\MD\_webclip_manifest.json`
into `category: webclip` notes, via the `scholion-webclipper` API (see
`E:\scholion-webclipper\README.md`) — same backend the interactive
`add-scholion-webclip/SKILL.md` uses, different principal
(`add-scholion-webclip-batch`, its own rate-limit window — see that repo's
`.env.example`). Batch mode: **no per-item authorization, no interactive
search-first wait, no per-item commit** — deliberate departures from the
interactive skill for this one backlog-clearing job. Everything else
(ghost-writer voice, source-or-silence, the audit gate, no cross-links per
author request, no Co-Authored-By) still applies in full.

## The manifest

`_webclip_manifest.json` is the **single source of truth** for what's left,
unifying what used to be two separate queues: pre-captured legacy `.md`
files (from `C:\Users\conta\OneDrive\MD\`, browser-extension exports) and
raw URLs (from the Edge favorites export, never pre-captured — 2026-09-23,
1472 web + 48 YouTube, the YouTube ones deliberately excluded from `items`
entirely, a separate pipeline). Never edit the Edge Bookmarks file itself —
confirmed 2026-09-23 that a local edit doesn't survive Edge's own
sync/restart. The manifest is the only thing that tracks progress now.

Each item:
```json
{ "type": "md_file", "md_path": "<name>.md" (or "_processed/<name>.md"), "url": "<source, or null>", "status": "pending" }
{ "type": "url", "url": "<url>", "status": "pending", "batch": <n>, "source_path": "<original bookmark folder path>" }
```

`status` ∈ `pending | done | failed | skipped`. Whichever this playbook
sets is the record — there's no other bookkeeping to keep in sync.

**The two types get genuinely different treatment, not just a different
compose call:**

- **`md_file`** already has captured content. **Never fetch it fresh, not
  even as a fallback for thin content.** Many of these pages are years old
  and no longer exist as originally captured, or exist differently — a
  refetch attempting to "improve" thin content risks silently composing
  from a different (or dead) version of the page, or just failing outright
  for no gain. Use exactly what was captured, however thin. If it's too
  thin to produce anything honest, that's a `skipped` outcome, not a retry
  trigger.
- **`url`** has no pre-captured content — compose in URL mode is not a
  fallback here, it's the only option there ever was.

## Your assignment

**Never use the Monitor tool in this job.** A prior batch stalled twice
("waiting for the monitor's completion notification") and ended its turn
without ever reaching the commit step, leaving many staged/untracked files
behind for someone else to clean up. Every call to `scholion-webclipper` is
a synchronous HTTP request you wait on directly — there is nothing here
that needs a background monitor.

Read the manifest, take the next **N `pending` items** (N given in your
prompt, usually 12–18), in the order they appear. Process them one at a
time, in order, **sequentially — never spawn your own subagents or forks
for this batch** (a prior run that self-parallelized produced duplicate
slugs and burned 2-3x the tokens of a clean sequential run). Stop after N
items (success or skip both count) and report a summary.

Read the API key once, before the first item:

```powershell
$webclipKey = Get-Content 'C:\Users\conta\.claude\secrets\scholion-webclipper-batch.key' -Raw
$manifestPath = 'C:\Users\conta\OneDrive\MD\_webclip_manifest.json'
$manifest = Get-Content $manifestPath -Raw | ConvertFrom-Json
```

**Update `$manifest` in memory as you go (step 5), write it back to disk
once at the end of your whole batch** (step 7) — not per item. A crash
mid-batch loses at most this one dispatch's progress, which is recoverable
(the items are still `pending`, nothing was destroyed); writing per item
just adds N-1 disk writes for no real safety gain, since nothing else reads
this file concurrently (batches run sequentially, never in parallel — see
above).

## Per-item pipeline

1. **Find the item's `capturedAt`.**
   - `md_file`: read `C:\Users\conta\OneDrive\MD\<md_path>` (already
     relative-pathed to include `_processed/` if applicable, though a
     `pending` item is never there). Frontmatter has `created` as
     `2026-01-09T13:09:52 (UTC -03:00)` — the server validates `capturedAt`
     and rejects that shape outright, it wants
     `2026-01-09T13:09:52-03:00`: drop the space and the `(UTC `/`)`
     wrapper, concatenate the offset directly onto the timestamp, nothing
     else changes. `title` is the first `# H1`; `source`/`author` are also
     in frontmatter. Strip known junk markers from the body before judging
     content quality or composing: `Navigating to Notifications`,
     `More for You`, `Enjoy the videos and music you love`,
     `Continuar a ler`, `Embedded Content`, `## 0 notifications`,
     `> ## Excerpt`.
   - `url`: no `capturedAt` override — omit the field, the server uses now.

2. **Compose.** No `relatedNotes` — cross-link search stays off for this
   backlog (author's explicit request; unlike the interactive skill, don't
   even run the search).

   **`md_file`:**
   ```powershell
   $body = @{ text = '<cleaned body>'; title = '<title>'; url = '<source>'; domain = '<host of source, no www., dots to hyphens>'; capturedAt = '<reformatted created>' } | ConvertTo-Json
   $r = Invoke-RestMethod -Uri 'http://localhost:8080/api/webclip/webclip/compose' -Method Post -Headers @{ 'X-Api-Key' = $webclipKey } -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 300
   ```
   If the cleaned body is under ~400 chars — genuinely too thin to compose
   anything honest from — **don't call `compose` at all**: mark the item
   `status: "skipped"`, `reason: "thin_unrecoverable"` directly (step 5),
   move the source file to `_needs_url_review` (step 6), move on. No
   refetch attempt, per the manifest section above.

   **`url`:**
   ```powershell
   $body = @{ url = '<url>' } | ConvertTo-Json
   $r = Invoke-RestMethod -Uri 'http://localhost:8080/api/webclip/webclip/compose' -Method Post -Headers @{ 'X-Api-Key' = $webclipKey } -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 300
   ```
   Errors here are real, meaningful outcomes, not a signal to try harder —
   this is the one and only attempt at the live page:
   - `thin_content`, `blocked_domain`, `consent_wall_unresolved`: mark
     `status: "failed"`, `reason: "<the error code>"`.
   - `fetch_timeout`, `fetch_failed` (`retryable: true`): one retry, same
     call. Still failing: mark `status: "failed"`, `reason: "<error
     code>"`.

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
     verdict). Write **only** the clipping (step 4b), mark the item
     `status: "skipped"`, `reason: "audit_unresolved"`.

4. **Write the files.**

   **4a. Note passed (green/yellow):** save in `mode: "return"` — batch
   mode stages its own writes and commits once at the end (step 7), it does
   not want `scholion-webclipper`'s own `vault/` commit:
   ```powershell
   $saveBody = @{ mode = 'return' } | ConvertTo-Json
   $s = Invoke-RestMethod -Uri "http://localhost:8080/api/webclip/webclip/$($r.operationId)/save" -Method Post -Headers @{ 'X-Api-Key' = $webclipKey } -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($saveBody)) -TimeoutSec 60
   ```
   A `slug_conflict` here means this exact item was already saved by an
   earlier run whose manifest write never landed (or a different item
   happens to share a title) — mark the item `status: "done"` anyway (the
   note demonstrably exists) and move on; don't treat it as a failure.

   Write `$s.clippingContent` to `E:\scholion\$($s.clippingPath)` and
   `$s.noteContent` to `E:\scholion\$($s.notePath)` verbatim — don't edit
   either (an edit means calling `compose` again, per the interactive
   skill's Decision 8 note). Mark the item `status: "done"`.

   **4b. Note skipped (red after recompose, or thin_unrecoverable from step
   2):** build the clipping file by hand — same shape `scholion-webclipper`
   itself renders. **Use the values you already had before calling
   `compose` (title/url/domain/capturedAt), never `$r.clipping.*`** —
   `Invoke-RestMethod` silently parses a JSON string that looks like a date
   into a `[DateTime]` object, which drops the original UTC offset
   (`2026-08-15T09:30:00-03:00` comes back as `08/15/2026 13:30:00`,
   reinterpreted in the local machine's timezone). `$r.clipping.markdown`
   is safe to use as-is (a multi-line string is never mistaken for a
   date) — skip this whole block for a `thin_unrecoverable` skip, there's
   no `compose` response to draw it from:
   ```yaml
   ---
   url: "<url>"
   captured_at: "<capturedAt>"
   title: "<title>"
   domain: "<domain>"
   ---

   <$r.clipping.markdown, verbatim>
   ```
   at `E:\scholion\clippings\<YYYY-MM of capturedAt>\<domain>--<slug derived from title>.md`.

5. **Update the manifest item in memory** — `Where-Object` returns the same
   object reference from `$manifest.items`, so setting a property on it
   mutates the array in place, no reassignment needed:
   ```powershell
   $item = $manifest.items | Where-Object { $_.type -eq 'url' -and $_.url -eq $url } # or -eq $_.md_path for md_file
   $item.status = 'done' # or 'failed' / 'skipped'
   $item | Add-Member -NotePropertyName reason -NotePropertyValue 'audit_unresolved' -Force # only for non-done
   ```
   Don't write the file yet (see "Your assignment").

6. **`md_file` only — move the source file.** From
   `C:\Users\conta\OneDrive\MD\<md_path>` to `_processed\<name>.md` on
   `done`, or `_needs_url_review\<name>.md` on any skip/failure (it still
   needs a human, or a Chrome-in-the-loop fallback, to sort out — the
   manifest says why). This is belt-and-suspenders on top of the manifest,
   not the source of truth anymore, but keeps the folder visually honest
   about what's left. `type: "url"` items have no file to move.

7. **Stage as you go, commit once at the end of your whole batch, write
   the manifest once at the end too.** For each item: `git add` whatever
   you wrote (clipping always on a `done` or an `audit_unresolved`/
   `thin_unrecoverable` skip; note only on `done`), build check
   (`cd /e/scholion && hugo --quiet`, skip *this note* — not the clipping —
   if it fails), write the commit-gate marker immediately, don't defer it
   (same reasoning as the interactive skill's Decision-10 note — the note
   text was already audited inside `compose`, pre-empt
   `ghost-audit-gate.ps1` re-auditing it):
   ```powershell
   $o = git -C E:\scholion rev-parse ":$($s.notePath)"
   New-Item -ItemType Directory -Force E:\scholion\.ghost-audit | Out-Null
   Set-Content "E:\scholion\.ghost-audit\$o.ok" $o
   ```
   Keep a running list of every path you `git add`ed. When your whole batch
   is done (all N items handled):
   - Commit **once**, for exactly your paths, with `git commit --only -m
     "<msg>" -- <path1> <path2> ...` (never a bare `git commit` — this repo
     has other concurrent activity, e.g. a scheduled publish task's
     pre-push hook and possibly other live sessions; `--only` with an
     explicit path list is what stays immune to sweeping in someone else's
     staged file). Message format: `"webclip batch: N items ([list of
     slugs, or count if long])"`. No `Co-Authored-By` line — ever, this
     machine's rule overrides any session default. **Do not `git push`** —
     the orchestrator pushes between batches, not you.
   - Write `$manifest` back to `$manifestPath`
     (`$manifest | ConvertTo-Json -Depth 10 | Set-Content $manifestPath`).
     This is the actual record of what your batch did — treat it with the
     same care as the commit.

## Logging

Append one line per skip/failure (never for `done`) to
`E:\scholion\clippings\_batch-log.md` (create with a `# Batch skip log`
header if it doesn't exist):

```
- SKIP <url or md_path> — <status: failed | skipped> — <reason> — <one-line detail>
```

## End of batch

Report: how many `done`, how many `failed`/`skipped` (and why, briefly),
and the manifest's remaining `pending` count by type (`md_file` vs `url`)
afterward.
