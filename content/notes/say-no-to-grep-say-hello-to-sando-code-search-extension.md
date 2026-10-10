---
title: "Say no to grep, say hello to \"real\" code searching with Sando Code Search Extension"
date: '2014-09-08T22:12:58-03:00'
category: webclip
summary: 'The post argues that Sando uses Lucene.NET to make code search faster, ranked, and more flexible than grep-like searches, with quick indexing and instant results.'
tags: ["sando", "lucene-net", "code-search", "visual-studio"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Say no to grep, say hello to \"real\" code searching with Sando Code Search Extension"
    url: "http://channel9.msdn.com/coding4fun/blog/Say-no-to-grep-say-hello-to-real-code-searching-with-Sando-Code-Search-Extension"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-09/channel9-msdn-com--say-no-to-grep-say-hello-to-sando-code-search-extension.md"
    kind: repo
---

The post presents Sando as a Visual Studio extension for code search that uses Lucene.NET instead of grep-like matching. It emphasizes ranked results, multi-term search, auto-complete, spelling correction, and fast searches on large codebases.

## Reading notes

- Sando is described as an open source Visual Studio extension that uses Lucene.NET for code indexing and search.
- The post contrasts grep-like regular expression search with Lucene-based search.
- In the Linux kernel demo, FindInFiles searched 47,407 files in about one minute and forty seconds and returned no matches for the sample query.
- The same Linux search with Sando returned results almost instantly.
- Sando pre-indexes source code, which costs about 50 minutes for the Linux source tree, but later updates and branch switches take only a few seconds of indexing.
- For medium-sized projects, initial indexing usually finishes in seconds.
- Sando can index its own source code in less than ten seconds.
- The extension searches C, C++, C#, and XAML.
- Its features include literal searches, symbol searches, google-style searches, preview with highlighted terms, code editor highlighting, auto-completion, auto-correction, auto-recommendation, and a word cloud.
- The post says the project wants help from developers with refactoring, bug fixing, and technical evangelism.
