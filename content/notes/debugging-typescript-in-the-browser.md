---
title: "Debugging TypeScript in the browser"
date: '2020-02-22T12:12:00+00:00'
category: webclip
summary: 'The article explains that TypeScript must be transpiled to JavaScript, then shows how source maps restore the original .ts file in browser devtools so you can set breakpoints and inspect runtime values.'
tags: ["typescript", "source-maps", "browser-debugging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Debugging TypeScript in the browser"
    url: "https://web.archive.org/web/20191014111157id_/https://blog.fullstacktraining.com/debugging-typescript-in-the-browser/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--debugging-typescript-in-the-browser.md"
    kind: repo
---

TypeScript has to be transpiled to JavaScript before it can run in the browser, which means the browser normally shows the generated JavaScript instead of the original source. The article presents source maps as the way to connect the modified file back to the TypeScript file and make browser debugging practical.

## Reading notes

- Source maps are special files created for JavaScript or CSS that map minified or transformed output back to its source.
- With a source map, the browser can show the original source code instead of only the generated file.
- Source maps also make it easier to add breakpoints while debugging.
- The example uses `tsc --sourceMaps true` to generate both the JavaScript output and a `.map` file.
- The generated JavaScript includes `//# sourceMappingURL=app.js.map` at the end.
- The source map JSON includes `version`, `file`, `sourceRoot`, `sources`, `names`, and `mappings`.
- The mappings use Base 64 VLQ encoding to relate positions in the generated file to positions in the original source.
- A source map visualization tool can be used to inspect how `app.ts` maps to `app.js`.
- In browser developer tools, the original `.ts` file appears under the Sources tab in Chrome or the Debug panel in Firefox and Safari.
- With the map loaded, breakpoints and runtime variable values are visible in the original TypeScript source.
