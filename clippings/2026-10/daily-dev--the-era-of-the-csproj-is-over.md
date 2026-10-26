---
url: "https://daily.dev/posts/vLDFW0kZC"
captured_at: "2026-10-26T12:29:38+00:00"
title: "The era of the .csproj is over: How Microsoft Just Simplified C# Forever."
domain: "daily-dev"
---

.NET 10 introduces file-based apps, letting developers run a single C# file directly with \`dotnet run app.cs\` or \`dotnet app.cs\` without creating a .csproj, bin, or obj folder structure. The code is still fully compiled and JIT-optimized, not interpreted scripting like the older .csx format. When a script grows beyond quick experimentation, the \`dotnet project convert app.cs\` command scaffolds a full project automatically, turning file-level directives into a proper .csproj. This removes the traditional scaffolding ceremony for small scripts and prototypes while preserving a smooth path to a full project when needed.

[#.net](https://daily.dev/tags/.net "Check all #.net posts")[#c#](https://daily.dev/tags/c%23 "Check all #c# posts")

[

![Post cover image](https://media.daily.dev/image/upload/s--foaA6JGU--/f_auto/v1722860399/public/Placeholder%2004)

](https://api.daily.dev/r/vLDFW0kZC "Go to post")

Table of contents

[The “Hello World” Reality Check](https://api.daily.dev/r/vLDFW0kZC "The “Hello World” Reality Check")[Why This Isn’t Just “Scripting”](https://api.daily.dev/r/vLDFW0kZC "Why This Isn’t Just “Scripting”")[Why This Matters (The “Core Benefits”)](https://api.daily.dev/r/vLDFW0kZC "Why This Matters (The “Core Benefits”)")[Final Thoughts](https://api.daily.dev/r/vLDFW0kZC "Final Thoughts")

Questions this post answers

How do I run a single C# file without creating a .csproj project in .NET 10?

In .NET 10, you can run a C# file directly from the terminal using \`dotnet run app.cs\` or \`dotnet app.cs\`, with no project file, bin, or obj directory required. The code is still fully JIT-compiled, not interpreted, so it runs with native .NET performance rather than acting as a lightweight scripting layer like the older .csx format. Developers tracking new .NET runtime capabilities can follow releases like this one on daily.dev.

How do I convert a file-based C# script into a full .NET project?

Run \`dotnet project convert app.cs\` to scaffold a complete project structure around an existing script. The command automatically turns file-level directives into a proper .csproj file, so a quick script that grew too large can graduate into a formally structured project without manual copy-pasting or folder setup. daily.dev helps C# developers stay current on tooling changes like project conversion workflows.

5 Comments

Sort:

Share this post

[![spamcatcher's profile](https://media.daily.dev/image/upload/s--4C0NYj4f--/f_auto/v1775221074/avatars/avatar_GkdzrXXZUWj7ZNJJbc5oL?_a=BAMAMiWQ0)](https://daily.dev/spamcatcher)

Finally, now that nobody writes code anymore… the agents are really getting it all aren’t they

[![ristotoldsep's profile](https://lh3.googleusercontent.com/a/ACg8ocLDWc6mZn0JwNmXXw6WY0L_HJ6pegzRttooC5VgtXESHSj3MNYx=s64-c)](https://daily.dev/ristotoldsep)

.csproj will survive this. configuration files are famously immortal.

[![luukoosterhuis's profile](https://avatars.githubusercontent.com/u/304927767?v=4&s=64)](https://daily.dev/luukoosterhuis)

You know this title is highly misleading. Do you really believe only simple scripts are written in .Net? You’ve clearly not seen an enterprise application

[![gojoglacier's profile](https://media.daily.dev/image/upload/s--MUqXyx_D--/f_auto/v1791620532/avatars/avatar_RqSXoxTsTayGUnuM7PksG?_a=BAMAMicg0)](https://daily.dev/gojoglacier)

Nice :) I love the idea of writing C# scripts like I write Python or Go scripts

[![swarnasharmin's profile](https://media.daily.dev/image/upload/s--joHEq_jD--/f_auto/v1791022797/avatars/avatar_ZL6bebyCVkszL2cr0g8ab?_a=BAMAMicg0)](https://daily.dev/swarnasharmin)

Misleading title. Single-file execution is for small scripts, not enterprise apps.

![](https://media.daily.dev/image/upload/s--lf8LUJjq--/f_auto/v1732012913/login-popover-dailydev_mxb7lw)

## daily.dev is the fastest growing developer platform in Portugal!

### We know how hard it is to be a developer. It doesn't have to be. Personalized news feed, dev community and search, much better than what's out there. Maybe ;)

Already have an account?
