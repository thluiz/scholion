---
title: "Mikko Ohtamaa: Javascript autocompletions and having one for Sublime Text 2"
date: '2013-03-04T13:24:29-03:00'
category: webclip
summary: 'The article explains why JavaScript autocompletion is difficult, then surveys ways to add type information and build completions in Sublime Text 2 with JsDoc, TypeScript, CodeIntel, CTags, or custom scripts.'
tags: ["javascript", "autocompletion", "sublime-text-2", "typescript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Mikko Ohtamaa: Javascript autocompletions and having one for Sublime Text 2"
    url: "http://opensourcehacker.com/2013/03/04/javascript-autocompletions-and-having-one-for-sublime-text-2/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-03/opensourcehacker-com--javascript-autocompletions-sublime-text-2.md"
    kind: repo
---

The article says JavaScript autocompletion is hard because the language does not expose static type information while code is being written, and because frameworks use incompatible ways to define classes, modules, and namespaces. It then reviews several ways to add type hints and feed them into editor completion systems.

## Reading notes

- JavaScript lacks static typing, so an editor cannot know the type of values such as `this`, `$`, or `jQuery` before the code runs.
- The absence of native classes and modules means each framework invents its own conventions, which makes automatic type extraction harder.
- Editors can use generated or manually maintained type files, such as `.sublime-completions` files.
- JsDoc comments can carry class and namespace information, especially for code organized with RequireJS.
- TypeScript can provide type information either through external `.d.ts` files or by writing code in TypeScript itself.
- Sublime Text 2 has a TypeScript plug-in for autocompletions.
- SublimeCodeIntel uses OpenKomodo CodeIntel, which is open source and written in Python, but the author says he could not get its JsDoc support working.
- CTags is another backend Sublime Text 2 can use, though the author did not test it with JavaScript completion.
- A Three.js script shows a simpler route: scan the codebase with regexes and generate Sublime Text 2 completion files.
- The same idea can apply to other dynamically typed languages when the project controls its namespace conventions.
