---
title: "A love letter to React"
date: '2026-09-25T08:46:40+01:00'
category: webclip
summary: 'O texto diz que React influenciou o LiveView e o Phoenix ao mostrar um modelo de componentes reativos, a colocation entre markup e código, componentes HTML-aware e otimizações de diffs no servidor e no cliente.'
tags: ["react", "phoenix", "liveview", "frontend"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A love letter to React"
    url: "https://fly.io/blog/love-letter-react/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/fly-io--a-love-letter-to-react.md"
    kind: repo
---

React é apresentado como a base de várias escolhas do Phoenix e do LiveView. O texto destaca o modelo de componente reativo, a colocação conjunta de markup e código, e a adoção de componentes HTML-aware e slots para montar interfaces mais extensíveis.

## Fichamento

- React mostrou um modelo de componentes simples de entender, com estado e renderização que se refaz quando o estado muda.
- O LiveView levou esse modelo para um processo com estado no servidor.
- A colocação de HTML junto com o código da aplicação é descrita como uma decisão correta porque reúne partes fortemente acopladas.
- O texto defende que, se duas partes do código mudam juntas, elas devem viver juntas.
- Componentes HTML-aware e JSX são apresentados como uma forma de manter a estrutura do markup legível e de permitir composição natural entre tags estáticas e componentes dinâmicos.
- Slots e componentes funcionais no Phoenix são usados como uma resposta ao problema de criar componentes reutilizáveis e extensíveis sem esconder a estrutura HTML.
- O texto afirma que o Phoenix adota diffs eficientes no servidor, enviando só as partes dinâmicas que mudaram.
- No cliente, o texto menciona o uso de morphdom para aplicar apenas os patches mínimos no DOM.
- A influência de React aparece também no backend, com frameworks como o Blade sendo citados como exemplos de engines HTML-aware.
- O texto encerra defendendo que, em 2022, frameworks de backend deveriam seguir essa direção.
