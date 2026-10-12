---
title: "Tudo que você precisa saber sobre resoluções, telas retina, devicePixelRatio, DPI, CSS pixels e etc"
date: '2014-07-02T22:50:36-03:00'
category: webclip
summary: 'O texto explica a diferença entre resolução física, DPI, devicePixelRatio, CSS pixels e viewport, e defende que a área útil em CSS pixels importa mais para a usabilidade.'
tags: ["resolucoes", "retina", "devicepixelratio", "viewport"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Tudo que você precisa saber sobre resoluções, telas retina, devicePixelRatio, DPI, CSS pixels e etc - sergiolopes.org"
    url: "http://sergiolopes.org/resolucoes-dpi-pixel-ratio-retina/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-07/sergiolopes-org--resolucoes-telas-retina-devicepixelratio-dpi-css-pixels.md"
    kind: repo
---

O texto distingue resolução física, DPI, CSS pixels e devicePixelRatio. Também mostra que o navegador trabalha com um dpi base de 96 para unidades físicas em CSS, e que telas retina ou equivalentes usam mais de um pixel físico por pixel de conteúdo.

A ideia central é que o viewport, medido em CSS pixels, diz mais sobre a área útil para o usuário do que a resolução física. Por isso o autor critica comparações que olham só para pixels físicos e propõe pensar em um “dpi de conteúdo”, ligado ao tamanho do conteúdo que a tela mostra.

## Fichamento

- A resolução física da tela e o tamanho físico são medidas distintas, e o DPI resulta da divisão entre elas.
- Em JavaScript, é possível ler a resolução com `window.screen.width` e `window.screen.height`, mas não o tamanho físico nem o DPI real da tela.
- Unidades físicas de CSS como `1cm` e `1in` não correspondem ao tamanho físico real; os navegadores usam um dpi base de 96.
- Em telas retina, um pixel de conteúdo é renderizado com mais de um pixel físico, e essa relação é o device pixel ratio.
- No Android, há categorias como xhdpi, hdpi, tvdpi, mdpi e ldpi, cada uma associada a um pixel ratio diferente.
- CSS pixels ou device independent pixels são as medidas usadas no código, enquanto device pixels são os pixels físicos da tela.
- O tamanho do viewport em CSS pixels é o que determina quanto conteúdo cabe na tela.
- O exemplo do Gizmodo sobre iPad mini e Nexus 7 é apontado como errado porque compara resolução física em vez de viewport.
- Alta resolução e alto pixel ratio não são ruins; elas deixam textos, gráficos, fotos e vídeos mais definidos.
- O autor propõe a ideia de “dpi de conteúdo”, baseada em CSS pixels, porque ela se aproxima mais da experiência real do usuário.
- O iPad mini tem a mesma resolução do iPad normal em uma tela fisicamente menor, o que reduz o tamanho aparente do conteúdo.
- A Apple teria escolhido 7.9 polegadas para manter no iPad mini um dpi de conteúdo próximo ao dos iPhones.
- O W3C define o pixel de referência e relaciona o tamanho percebido do pixel à distância de uso da tela.
- A distância ideal de uso varia entre iPhone, iPad e iPad mini, e também entre aparelhos Android como Galaxy S3 e Galaxy Note 2.
- A percepção de pixel depende da visão do usuário, e telas acima de certa densidade deixam de ser distinguíveis pela maioria das pessoas.
