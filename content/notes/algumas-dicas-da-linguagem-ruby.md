---
title: "Algumas Dicas da Linguagem Ruby"
date: '2012-06-29T19:12:56-03:00'
category: webclip
summary: 'A página reúne truques de Ruby para troca de variáveis, interpolação de strings, condicionais que retornam valor, ranges, hashes, splat, joins e conversão entre bases.'
tags: ["ruby", "idiomas", "strings", "arrays"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Algumas Dicas da Linguagem Ruby"
    url: "https://akitaonrails.com/2012/06/29/algumas-dicas-da-linguagem-ruby/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/akitaonrails-com--algumas-dicas-da-linguagem-ruby.md"
    kind: repo
---

A página reúne truques de Ruby para deixar tarefas comuns mais curtas ou mais legíveis. Mostra troca de variáveis, interpolação de strings, condicionais que retornam valor, ranges, hashes, arrays, splat, join e conversão de números entre bases.

## Fichamento

- Ruby permite escrever a mesma coisa de jeitos diferentes, e parte disso é associada ao Principle of Least Surprise.
- A troca de duas variáveis pode ser feita com atribuição paralela, sem usar variável temporária.
- Em Ruby, a interpolação de strings é preferida para montar textos com valores de variáveis.
- Strings formatadas com `%` também são usadas, e a interpolação pede aspas duplas.
- `%(...)` facilita strings multilinha com interpolação, evitando muitas barras de escape.
- `%w(...)` é uma forma alternativa de declarar arrays de strings.
- Números podem usar `_` como separador de milhar.
- `if` e `case` devolvem o valor da última expressão executada, então o bloco inteiro pode ser atribuído a uma variável.
- `case` usa `===`, e com `Range` isso testa se o valor pertence ao intervalo.
- `Range` pode ser iterado com `for`, `upto` ou `each`, e também pode virar array.
- A soma de um `Range` pode ser feita com `reduce`, inclusive na forma curta `reduce(:+)`.
- Hash pode ser criado com sintaxe de símbolo em Ruby 1.9+ e também a partir de um array com chaves e valores alternados usando `Hash[*array]`.
- `zip` serve para montar um hash a partir de arrays separados de chaves e valores.
- `*hash` transforma o hash em pares chave-valor, e `flatten` achata essa estrutura.
- Arrays podem ser inicializados de várias formas equivalentes, inclusive com `%w`, `Array.new` e repetição com `*`.
- O splat permite capturar o resto de um array durante a atribuição.
- O splat também expande um array em argumentos de método.
- `[ *args ]` serve para tratar um único valor ou um array do mesmo jeito na iteração.
- `join` e a multiplicação do array por uma string fazem a junção dos elementos com separador.
- `rand` gera um inteiro aleatório, e `to_s(base)` / `to_i(base)` convertem números entre bases.
