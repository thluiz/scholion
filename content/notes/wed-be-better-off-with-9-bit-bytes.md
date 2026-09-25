---
title: "We'd be Better Off with 9-bit Bytes"
date: '2025-08-08T01:04:20+01:00'
category: webclip
summary: 'The post argues that if 9-bit bytes had become standard, many later limits would have been less painful: IPv4, UNIX time, Unicode, pointers, and other encodings would have had more room before exhausting.'
tags: ["9-bit-bytes", "computer-history", "address-space", "unicode"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "We'd be Better Off with 9-bit Bytes"
    url: "https://pavpanchekha.com/blog/9bit.html?utm_source=tldrnewsletter"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2025-08/pavpanchekha-com--wed-be-better-off-with-9-bit-bytes.md"
    kind: repo
---

The post argues that 9-bit bytes would have made the computing world easier in several places. With 36-bit IPv4 addresses, 36-bit UNIX timestamps, and 18-bit Unicode characters, many of the exhaustion problems we live with now would have arrived much later or not at all.

## Reading notes

- 70s systems such as the PDP-10 used nine-bit bytes, and the post treats that as a plausible base for a different standard.
- A 9-bit byte world would give IPv4 36-bit addresses, enough for far more devices and users before exhaustion.
- 32-bit UNIX timestamps would become 36-bit timestamps and would not run out in 2038.
- Unicode would have more room, with 18-bit characters instead of 16-bit ones, making the available repertoire much larger.
- Pointer sizes and memory limits would shift too, with 32-bit operating systems allowing larger per-process address spaces.
- Other effects mentioned include roomier AS numbers, ports, process IDs, and user IDs, along with changes to instruction encodings and character sets.
- The main cost discussed is TCP sequence numbers, where 18-bit space might be too small for high-bandwidth connections and could force an earlier protocol upgrade.
- The post ends by suggesting that many early computing limits were shaped by numerological choices rather than hard necessity.
