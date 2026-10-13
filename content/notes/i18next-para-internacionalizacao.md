---
title: "i18next para Internacionalização"
date: '2014-10-18T07:16:09-03:00'
category: webclip
summary: 'O texto apresenta o i18next como solução para traduzir conteúdo em vários idiomas, usando JSON, data-i18n, detecção de língua e fallback para alternar entre português, inglês e espanhol.'
tags: ["i18next", "internacionalizacao", "javascript", "traducoes"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "i18next para Internacionalização"
    url: "http://tableless.com.br/i18next-para-internacionalizacao/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-10/tableless-com-br--i18next-para-internacionalizacao.md"
    kind: repo
---

O texto conta que a necessidade de atender três idiomas em um projeto levou à busca por uma forma de internacionalização. A proposta é usar o i18next para centralizar traduções em JSON, preencher o HTML por meio de `data-i18n` e deixar o conteúdo mudar conforme a língua do usuário ou a escolha feita no clique.

## Fichamento

- A necessidade de suportar inglês, espanhol e português fez o autor procurar uma solução de internacionalização.
- O i18next é apresentado como a lib que organiza esse fluxo e não se limita a JavaScript.
- As traduções ficam em arquivos `translation.json` dentro de subpastas como `/en-US`, `/es` e `/pt-BR`.
- O HTML pode ficar sem texto fixo, porque o conteúdo é inserido de forma dinâmica conforme a linguagem.
- O atributo `data-i18n` serve para aplicar traduções ao texto e também a atributos como `title` e `alt`.
- A inicialização mostrada usa `fallbackLng`, `debug`, `fixLng` e `load` para definir idioma padrão, exibir informações de desenvolvimento, preservar o cookie de idioma e carregar só a linguagem atual.
- A lib detecta a linguagem do navegador e usa o valor de `fallbackLng` quando a língua detectada não tem tradução.
- Em uma interação do usuário, `i18n.setLng('es', {fixLng: true}, ...)` atualiza a linguagem e reaplica as traduções na página.
- O artigo diz que o resultado é um conteúdo mais acessível em vários idiomas e aponta um repositório com o exemplo e o código comentado.
