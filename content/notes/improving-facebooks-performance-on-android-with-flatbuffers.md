---
title: "Improving Facebook's performance on Android with FlatBuffers"
date: '2015-08-03T16:43:48-03:00'
category: webclip
summary: 'Facebook explains how FlatBuffers replaced JSON for Android storage and UI data flow, reducing parsing cost, memory churn, startup time, and disk-cache story load latency.'
tags: ["flatbuffers", "android-performance", "json", "storage-format"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Improving Facebook's performance on Android with FlatBuffers"
    url: "https://code.facebook.com/posts/872547912839369/improving-facebook-s-performance-on-android-with-flatbuffers/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2015-08/code-facebook-com--improving-facebooks-performance-on-android-with-flatbuffers.md"
    kind: repo
---

Facebook describes how it stores social graph data on Android as a tree structure rather than normalizing it into tables. JSON was too slow to parse, too costly to initialize, and too allocation-heavy, so the app needed a better storage format.

## Reading notes

- FlatBuffers lets the app read individual subcomponents of a tree directly, without deserializing the whole object first.
- Data can be stored directly in a file and mmap-ed into memory, which lowers memory footprint and avoids intermediate object creation.
- Because FlatBuffers are immutable, the team tracks mutations alongside the base buffer so small updates can be applied without redownloading an entire story.
- The mutation buffer keeps an index from absolute positions in the base buffer to new data, plus the replacement data in FlatBuffer format.
- FlatBuffers are used for storage, networking, and the in-memory app format, which removes transformation steps between server response and UI display.
- The Flat Models approach moves application and networking logic below storage, leaving the UI to read from storage through standard Android cursors.
- The article reports reductions in story load time from 35 ms to 4 ms, transient memory allocations by 75 percent, cold start time by 10 to 15 percent, and storage size by 15 percent.
