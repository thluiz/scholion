---
title: "Assembly Versioning and DLL Hell in C# .NET Framework: Problems and Solutions"
date: '2020-09-19T17:34:14-03:00'
category: webclip
summary: 'The article explains how modern .NET version conflicts happen, why binding redirects are often enough, and when side-by-side loading or repacking assemblies becomes necessary.'
tags: ["dotnet", "assembly-versioning", "binding-redirects", "dll-hell"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Assembly Versioning and DLL Hell in C# .NET Framework: Problems and Solutions - Michael's Coding Spot"
    url: "https://michaelscodingspot.com/dotnet-dll-hell/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-09/michaelscodingspot-com--assembly-versioning-and-dll-hell-in-csharp-dotnet-framework.md"
    kind: repo
---

The article explains that classic DLL Hell has changed in .NET. Applications usually do not share DLLs directly, but modern dependency graphs can still produce version conflicts when different packages require different versions of the same assembly. The text highlights a simple conflict and a diamond dependency conflict, where libraries depend on incompatible versions that the application cannot easily change.

## Reading notes

- DLL Hell in .NET now comes mainly from dependency version conflicts rather than shared DLL files.
- Common packages such as Newtonsoft.Json or Serilog can create conflicts when different projects need different versions.
- A diamond dependency conflict happens when two libraries depend on different versions of the same library and the application cannot easily change those libraries.
- One solution is to align versions so that all projects reference the same major version and the highest compatible version is loaded.
- Binding redirects in app.config can force the runtime to load a chosen version and are described as the easiest and most common fix.
- Binding redirects can still fail if a library calls methods or uses parameters that do not exist in the loaded version.
- If version matching and binding redirects are not enough, assemblies can be loaded side by side.
- Side-by-side loading can be done with AssemblyResolve, different folders for strong-named assemblies, the GAC, or repacking libraries into a new assembly.
- Loading multiple versions in one process can create resource conflicts because a library does not know another version is present.
- Visual Studio can auto-generate binding redirects when NuGet packages are added.
