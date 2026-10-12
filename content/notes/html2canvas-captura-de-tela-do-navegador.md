---
title: "html2canvas: captura de tela do navegador"
date: '2012-05-24T18:22:41-03:00'
category: webclip
summary: 'O texto explica como o canvas do HTML5 permite capturar telas com javascript usando html2canvas, mostra o fluxo Preload/Parse/Render e um exemplo com proxy para um site externo.'
tags: ["html5", "canvas", "javascript", "html2canvas"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "html2canvas: captura de tela do navegador"
    url: "https://imasters.com.br/apis-microsservicos/screenshot-com-canvas-e-javascript"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/imasters-com-br--html2canvas-captura-de-tela-do-navegador.md"
    kind: repo
---

O texto diz que, antes do HTML5, fazer print-screen de telas do browser com javascript era inviável. Com o canvas, passam a existir recursos para isso, e o html2canvas é apresentado como uma API para renderizar a página.

## Fichamento

- O canvas do HTML5 é apontado como a base que tornou possível capturar telas do navegador com javascript.
- O html2canvas é apresentado como uma API usada para esse tipo de renderização.
- O método inicial citado é Preload, que recebe Element, Options, Complete, Logging, Proxy e Timeout.
- O fluxo descrito pela script é Preload, depois Parse dos elementos e depois Render do objeto.
- O código mostrado usa $(window).ready, html2canvas.Preload, html2canvas.Parse e html2canvas.Renderer para gerar uma imagem em data URL.
- A função openConsole abre uma janela e escreve nela o conteúdo com a imagem gerada.
- O exemplo mais avançado usa um proxy para recuperar o conteúdo de um site externo e colocá-lo dentro de um iframe.
- Depois do carregamento do iframe, o texto mostra a captura do body com html2canvas e a exibição do resultado no console.
- O texto afirma que os browsers que aceitam canvas são Chrome, FF, Opera e IE7.
- Também menciona o site Can I Use como referência de compatibilidade entre navegadores.
