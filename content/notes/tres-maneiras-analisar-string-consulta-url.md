---
title: "Três maneiras para analisar uma string de consulta em uma URL"
date: '2012-07-16T13:36:59-03:00'
category: webclip
summary: 'O texto mostra três maneiras de obter a query string de uma URL em JavaScript e depois apresenta uma função simples para dividir pares chave-valor em um objeto, com uso em um plugin jQuery.'
tags: ["javascript", "url", "query-string"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Três maneiras para analisar uma string de consulta em uma URL"
    url: "https://web.archive.org/web/20150827064713/http://imasters.com.br:80/artigo/24967/desenvolvimento/tres-maneiras-para-analisar-uma-string-de-consulta-em-uma-url/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-07/web-archive-org--tres-maneiras-analisar-string-consulta-url.md"
    kind: repo
---

O texto apresenta três formas de recuperar a query string de uma URL em JavaScript. Depois disso, mostra uma função que recebe a string de consulta, separa os pares por "&" e monta um objeto com chave e valor.

## Fichamento

- A abertura diz que analisar string de consulta com JavaScript não é comum, mas pode ser necessário no front end.
- As três técnicas listadas servem para obter a query string a partir da URL, não para convertê-la em objeto.
- Uma forma usa substring junto com indexOf quando a URL está disponível como string.
- Outra forma usa window.location.search quando a URL é a da página atual, com remoção do "?" inicial.
- A terceira forma usa um elemento âncora para ler a URL e acessar a propriedade search.
- A função parseQueryString divide a string por "&" e depois separa cada par por "=", guardando o resultado em um objeto.
- O autor diz que o processo é simples e que cada par vira uma propriedade do objeto.
- No uso em projetos, ele menciona uma biblioteca ou plugin jQuery que já analisa URLs.
- Essa biblioteca inclui a query string analisada como propriedade e corrige dois bugs do Internet Explorer ligados à técnica.
