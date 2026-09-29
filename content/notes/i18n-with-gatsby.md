---
title: "i18n with Gatsby"
date: '2020-03-02T07:29:13-03:00'
category: webclip
summary: 'The article proposes duplicating each Gatsby page per locale and passing locale through page context, then shows two ways to render localized content statically: React-Intl or JSON files queried with Gatsby data layer.'
tags: ["gatsby", "internationalisation", "react-intl", "graphql"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "i18n with Gatsby"
    url: "https://medium.com/significa/i18n-with-gatsby-528607b4da81"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2020-03/medium-com--i18n-with-gatsby.md"
    kind: repo
---

The article argues that Gatsby i18n works best when each locale gets its own page copy, so content is rendered statically instead of waiting for JavaScript. It then shows how to pass the locale through page context and use that value in layouts, links, and content loading.

## Reading notes

- Create one page per locale, keeping the default language out of the URL path and duplicating pages for other languages
- Store the locale in page context so page components can read it during rendering
- With React-Intl, use a Layout component to provide the locale and feed the provider with locale-specific strings
- Wrap Gatsby Link so navigation keeps the current locale instead of always falling back to the default language
- Without external dependencies, load locale JSON files and map them by locale in the page component
- Use Gatsby source and transformer plugins to query localized JSON content through GraphQL
- Page context can be used as a GraphQL query variable to filter results per locale
- Gatsby data layer can also support different images per language with gatsby-image
- A localized link can be built with React Context and a consumer in the layout setup
