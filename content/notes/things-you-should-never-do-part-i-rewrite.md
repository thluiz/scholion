---
title: "Things You Should Never Do, Part I"
date: '2026-11-20T16:45:21+00:00'
category: webclip
summary: 'Joel Spolsky argues that rewriting large software from scratch discards hard‑won bug fixes and market position, urging careful refactoring of existing code instead.'
tags: ["software-engineering", "legacy-code", "architecture", "management"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "Things You Should Never Do, Part I"
    url: "https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/joelonsoftware-com--things-you-should-never-do-part-i-rewrite.md"
    kind: repo
---

Joel Spolsky uses Netscape’s long gap between versions 4.0 and 6.0 to argue that rewriting a large product from scratch is the worst strategic move a software company can make. Netscape, Borland and others lost time and market share by discarding working code, while Microsoft avoided disaster by keeping its existing Word code base alive alongside a failed rewrite. Programmers are drawn to clean slates because reading existing code feels harder than writing new code, so they label old systems as messy without appreciating the value embedded in them.

He stresses that old code has been exercised in real environments and embodies countless bug fixes, each of which may have taken weeks to discover and diagnose. Throwing it away discards that accumulated knowledge, hands competitors years of advantage, freezes strategic change while the rewrite drags on, and burns money recreating functionality that already exists. Complaints about architecture, performance or ugliness rarely justify a rewrite, since these can be addressed incrementally through refactoring, isolated optimization, and simple tooling. Spolsky warns that a new implementation is not guaranteed to be better than the original, especially with a different team that will likely repeat old mistakes and add new ones, and concludes that limited experimental rewrites of small pieces are acceptable, but full‑scale rewrites of commercial applications are reckless.

## Reading notes

- Netscape 6.0 entered public beta after a three‑year gap since 4.0, with no 5.0 release, during which its browser market share declined sharply.
- Spolsky claims Netscape’s delay was self‑inflicted by choosing to rewrite their browser code base from scratch.
- He notes Borland made similar mistakes with Arago/dBase for Windows and a rewritten Quattro Pro, letting Microsoft products overtake them.
- Microsoft attempted a Word rewrite (Pyramid) but shut it down while continuing to evolve the old code, limiting damage to financial loss.
- He observes that programmers tend to see themselves as architects who prefer bulldozing and rebuilding over incremental renovation.
- Programmers usually think existing code is a mess, largely because reading code is harder than writing it.
- This difficulty in reading code undermines reuse, leading developers to reimplement functions like string splitting instead of learning existing ones.
- As a result, most programmers will describe their current code as a big, tangled mess they would like to replace entirely.
- They often point to long, complex functions and unfamiliar API calls as evidence that the code base is bad.
- Spolsky mocks marketing claims that “all new source code” is inherently better, arguing that code does not “rust” by sitting on disk.
- He argues old code is valuable precisely because it has been used and tested, with many bugs found and fixed over time.
- Using a two‑page window display function as an example, he explains that messy parts often correspond to specific bug fixes.
- These fixes may handle edge cases like missing Internet Explorer, low memory conditions, removed floppy disks, or old Windows 95 versions.
- Each small code change may represent days of debugging and lab work built on weeks of real‑world usage.
- Rewriting from scratch discards all that embedded knowledge and the work invested in diagnosing and fixing those bugs.
- He argues that a full rewrite effectively gives competitors a two‑to‑three‑year head start, a long time in the software market.
- During a rewrite, the company is stuck shipping an aging version, unable to respond to new feature demands due to lack of shippable code.
- He characterizes this state as equivalent to shutting down operations while spending heavily to re‑create existing features.
- Spolsky concedes Netscape’s old code may have been poor, but points out it still worked well on many real systems.
- He identifies three main categories of problems in supposedly messy code: architectural issues, inefficiency, and ugliness.
- Architectural problems, such as networking code triggering UI dialogs directly, can be fixed incrementally through refactoring.
- He describes how, on the Juno project, the team spent months rearchitecting by reorganizing code and interfaces without discarding the base.
- Performance issues, like slow rendering in Netscape, usually affect limited areas and can be optimized or selectively rewritten.
- He claims that in performance work, a small fraction of effort often yields most of the speed improvements.
- Cosmetic issues, like unfortunate type names or inconsistent member variable prefixes, are solvable quickly with editor macros.
- Spolsky warns there is no justification to assume a new code base will be better than the original when starting over.
- He notes that different teams on version two do not necessarily have more relevant experience and will likely repeat past mistakes.
- The rewrite will also introduce new problems that did not exist in the original system.
- He distinguishes between throwing away small experimental functions or refactoring classes and discarding an entire commercial application.
- The slogan “build one to throw away” is described as dangerous when applied to large‑scale, shipping products.
- His final claim is that with experienced leadership, Netscape might have avoided committing to a full rewrite that harmed its position.
