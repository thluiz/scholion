---
title: "10 Tips for Productive F# Scripting"
date: '2016-04-20T17:06:53-03:00'
category: webclip
summary: 'The post collects practical ways to work productively with F# scripts, from editing .fsx files and using FSI well to loading files, packages, assemblies, and timing code.'
tags: ["fsharp", "fsi", "scripting", "visual-studio"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "10 Tips for Productive F# Scripting ·"
    url: "http://brandewinder.com/2016/02/06/10-fsharp-scripting-tips/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/brandewinder-com--10-tips-for-productive-fsharp-scripting.md"
    kind: repo
---

The post gathers practical tips for working with F# scripts. It favors editing code in .fsx files, running blocks interactively in FSI, and using shortcuts to test and reuse code while keeping scripts clean.

It also covers command-line execution, relative paths, loading assemblies and files, package management with Paket, profiling with #time, and a few extra tricks for working with large datasets and the FSI environment.

## Reading notes

- Use .fsx files for interactive coding because they offer a richer environment and encourage reusable scripts.
- In FSI, evaluated expressions produce values such as it, and you can keep using those values until they are shadowed.
- Scripts can run from the command line with FSI.exe, and behavior can differ between interactive and non-interactive execution.
- Relative paths are safer than absolute paths when a script depends on nearby resources, and __SOURCE_DIRECTORY__ helps locate them.
- Assemblies can be loaded with #r, including packages such as FSharp.Data or .NET assemblies not referenced by default.
- Paket avoids version-numbered package paths, which makes script references less brittle when package versions change.
- #load lets a script include code from another file, as long as any missing dependencies are referenced first.
- #time enables timing and garbage-collection information for code executed in FSI, and can be toggled on or off.
- Turning FSI to 64-bit is suggested for handling large datasets.
- The post also mentions extra tools and tricks such as debugging scripts, FsEye, font-size changes, pretty-printers, and Visual F# Power Tools.
