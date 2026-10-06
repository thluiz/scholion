---
title: "Identificando os IEs"
date: '2012-07-10T13:48:19-03:00'
category: webclip
summary: 'A página mostra como identificar versões antigas do Internet Explorer e adicionar uma classe específica na tag HTML para tratar erros com JavaScript, jQuery ou comentários condicionais.'
tags: ["internet-explorer", "javascript", "jquery", "comentarios-condicionais"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Identificando os IEs"
    url: "https://tableless.com.br/identificando-os-ies/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-07/tableless-com-br--identificando-os-ies.md"
    kind: repo
---

A página propõe adicionar uma classe específica na tag HTML para identificar o navegador quando for preciso corrigir bugs em versões antigas do Internet Explorer. Mostra exemplos em JavaScript e em jQuery para marcar IE6, IE7 e IE8.

Também compara essa abordagem com CSS hacks e com comentários condicionais. O texto diz que prefere comentários condicionais para separar arquivos de CSS por versão do navegador.

## Fichamento

- Adiciona-se uma classe no elemento HTML para identificar o navegador e direcionar código específico.
- Em JavaScript, o texto usa a verificação de MSIE no user agent e acrescenta ie8, ie7 ou ie6 conforme a versão.
- Em jQuery, o exemplo verifica se o navegador é IE e usa a versão para adicionar a classe correspondente.
- O autor diz preferir esse método a CSS hacks e a comentários condicionais usados apenas para inserir a classe na tag HTML.
- O texto mostra comentários condicionais para IE6, IE7, IE8 e para navegadores que não são IE.
- O texto também mostra comentários condicionais para separar arquivos CSS por versão do Internet Explorer.
- A página menciona um PDF para ajudar a convencer clientes e chefes a suportar navegadores antigos.
