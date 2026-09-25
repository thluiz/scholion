---
title: "Local, first, forever"
date: '2026-09-25T21:37:29+01:00'
category: webclip
summary: 'The post argues that local-first apps can use ordinary file-sync services as a durable sync layer, with CRDTs handling conflicts and different file layouts avoiding them.'
tags: ["local-first", "crdt", "file-sync"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Local, first, forever"
    url: "https://tonsky.me/blog/crdt-filesync/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/tonsky-me--local-first-forever.md"
    kind: repo
---

The post says local-first software keeps data on the user’s device but still needs internet sync for things like backing up and syncing across devices. That creates a risk: if the company disappears, the sync service may disappear too.

It proposes using common cloud file-sync tools such as Dropbox, iCloud Drive, OneDrive, Google Drive, or Syncthing as a simple sync layer. With CRDTs, conflicts can be merged automatically, and the article shows several layouts for doing that: one shared state file, one file per client, or append-only operation logs split into chunks.

## Reading notes

- Local-first software keeps data local, but still syncs online from time to time.
- Sync across a user’s own devices depends on some server-like component.
- If the company goes out of business, syncing can stop working.
- File-sync services are common and have multiple implementations.
- File sync is a simple protocol with little API surface.
- With a state-based CRDT, two conflicting state files can be opened, merged, and saved back.
- A file per client avoids Dropbox-level conflicts because each file is only edited on one machine.
- An operations-based CRDT can write operations into append-only files.
- Long operation logs can be split into batches to reduce sync work.
- The demo uses Automerge for text merging.
- The conclusion is that basic file-sync services can be enough for casual local-first sync.
