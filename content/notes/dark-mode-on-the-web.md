---
title: "Dark Mode on the Web"
date: '2020-07-05T14:10:32+00:00'
category: webclip
summary: 'The page argues that dark mode is mainly an accessibility feature, then shows how to respect system preference, let users override it, avoid flash of default theme, and adapt media, code blocks, tweets, and embeds.'
tags: ["dark-mode", "accessibility", "css", "react"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Dark Mode on the Web"
    url: "https://fatihkalifa.com/dark-mode-web"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/fatihkalifa-com--dark-mode-on-the-web.md"
    kind: repo
---

The page presents dark mode as an accessibility feature for people who read at night or in dim light. It recommends respecting system preference first, then giving users control to switch between light, dark, and system settings. It also warns against flashes of the default theme and shows how to apply theme changes before rendering.

## Reading notes

- Dark mode is framed less as an aesthetic choice and more as a way to reduce eye strain and improve nighttime reading.
- A site should support dark mode with the `color-scheme` meta tag so the browser can adjust default styling.
- The `prefers-color-scheme` media query can be used to set custom colors, and `window.matchMedia` can detect support in JavaScript.
- System preference should be respected unless the user explicitly selects a theme.
- A theme selector should offer three options: light, dark, and system preference.
- A Flash of Default Theme can happen when theme detection runs after the page renders.
- To avoid that flash, the theme can be read from `localStorage` in blocking JavaScript and written to a `data-theme` attribute before rendering.
- The article replaces React context for theming with CSS variables so most components do not need to re-render when the theme changes.
- Type-safe theme values can be defined in TypeScript and exposed as CSS variables.
- Global styles can combine `:root`, `data-theme`, and `prefers-color-scheme` so default, user, and system settings all work together.
- A hook can share theme state without context by combining persisted state, media-query detection, and a setter.
- Images, GIFs, and videos need separate treatment, including alternate assets, brightness and contrast filters, or inversion for suitable black-and-white images.
- Syntax highlighting can be generated at build time with theme-aware CSS variables.
- Embedded tweets can receive dark styling through `twitter:widgets:theme`, though client-side embeds may flicker.
- GitHub Gist embeds can use filter-based dark mode as a fallback until native support exists.
