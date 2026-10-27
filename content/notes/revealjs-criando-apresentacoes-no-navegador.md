---
title: "Reveal.js: criando apresentações no navegador"
date: '2013-02-15T16:42:27-03:00'
category: webclip
summary: 'O texto mostra como montar uma apresentação básica com reveal.js, definir a estrutura HTML exigida, ativar opções de exibição, usar fragmentos, trocar temas e carregar plugins.'
tags: ["revealjs", "html5", "javascript", "apresentacoes"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Reveal.js: criando apresentações no navegador"
    url: "https://tableless.com.br/reveal-js-criando-apresentacoes-no-navegador/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-02/tableless-com-br--revealjs-criando-apresentacoes-no-navegador.md"
    kind: repo
---

O texto apresenta o reveal.js como uma biblioteca JavaScript que permite criar apresentações no navegador usando HTML5, CSS3 e JavaScript. Ele explica a estrutura mínima da página, mostra como iniciar a apresentação e indica opções para personalizar a navegação, a transição e os recursos dos slides.

## Fichamento

- O reveal.js permite criar apresentações no navegador com HTML5, CSS3 e JavaScript.
- A estrutura básica exige um `div.reveal` com outro `div.slides` dentro.
- Os slides são criados como elementos `section` dentro de `div.slides`.
- A apresentação é iniciada com `Reveal.initialize()`.
- O método `initialize` aceita opções para auto slide, centralização, controles, navegação pelo mouse e transição.
- Fragmentos são criados adicionando a classe `fragment` a conteúdos dentro do slide.
- A biblioteca oferece temas como `beige`, `night`, `serif`, `simple` e `sky`.
- Plugins podem ser ativados pela opção `dependencies`, como o plugin de zoom.
- O texto menciona que a biblioteca também permite temas próprios, uso da API JavaScript e eventos de slides e fragmentos.
- O artigo cita o serviço rvl.io como uma forma de criar apresentações sem código.
