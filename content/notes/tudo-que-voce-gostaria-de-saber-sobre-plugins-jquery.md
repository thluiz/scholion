---
title: "Tudo que você gostaria de saber sobre plugins jQuery e ninguém teve paciência de explicar"
date: '2016-04-11T10:58:02-03:00'
category: webclip
summary: 'O texto explica por que criar plugins jQuery, como usar $.fn, evitar conflitos com $, manter encadeamento, lidar com opções e recorrer a padrões como jQuery Boilerplate e Widget Factory.'
tags: ["jquery", "plugins", "javascript", "boilerplate"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Tudo que você gostaria de saber sobre plugins jQuery e ninguém teve paciência de explicar - Tableless"
    url: "http://tableless.com.br/tudo-que-voce-gostaria-de-saber-sobre-plugins-jquery-e-ninguem-teve-paciencia-de-explicar/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-04/tableless-com-br--tudo-que-voce-gostaria-de-saber-sobre-plugins-jquery.md"
    kind: repo
---

O texto defende que plugins devem ser usados para encapsular e reaproveitar código. A partir daí, explica a base de um plugin jQuery, a diferença entre adicionar métodos em $.meuPlugin e em $.fn.meuPlugin, a necessidade de evitar conflitos com outras bibliotecas e a importância de manter o encadeamento retornando this.

## Fichamento

- Plugins fazem sentido quando o código pode ser reaproveitado em projetos futuros e encapsulam comportamento.
- O ponto de partida é adicionar uma propriedade a $.fn.
- $ é um apelido para jQuery, e o mesmo objeto pode ser acessado por window.jQuery, window.$, jQuery ou $.
- $.fn é equivalente a jQuery.prototype, então métodos colocados ali ficam disponíveis para as instâncias criadas por $().
- Para evitar conflito com outras bibliotecas que também usam $, o plugin pode ser envolvido em uma função anônima.
- Plugins que operam sobre seletores devem retornar this para manter o encadeamento.
- O método each é usado para percorrer a coleção recebida pelo plugin.
- O plugin pode receber parâmetros por meio de options.
- Se parâmetros não forem passados, é preciso definir valores padrão para evitar quebra.
- $.extend é usado para mesclar defaults e options em um novo objeto settings.
- O texto recomenda consultar o guia oficial, o jQuery Boilerplate e o jQuery UI Widget Factory para plugins stateful.
