---
title: "A numeração de Gödel"
date: 2026-06-16T15:16:10+01:00
summary: 'O truque que deixa a matemática falar de si mesma: dar a cada símbolo, fórmula e demonstração um número único e reversível, codificando sequências por potências de primos.'
tags: ["godel", "logica", "incompletude", "matematica"]
has_commentary: false
sources:
  - title: "Gödel numbering — Wikipedia"
    url: "https://en.wikipedia.org/wiki/G%C3%B6del_numbering"
    kind: wiki
  - title: "Gödel's Incompleteness Theorems — Stanford Encyclopedia of Philosophy"
    author: "Panu Raatikainen"
    url: "https://plato.stanford.edu/entries/goedel-incompleteness/"
    kind: article
---

A numeração de Gödel é o truque que deixa a matemática falar de si mesma. A ideia é dar a cada símbolo, cada fórmula e cada demonstração um número próprio, único, de um jeito que sempre permita fazer o caminho de volta.

Primeiro, cada símbolo básico da linguagem (o sinal de igual, o de soma, as variáveis, o zero) ganha um número. Depois, uma fórmula, que é uma sequência de símbolos, é codificada multiplicando os primos em ordem, cada um elevado ao número do símbolo naquela posição. O primeiro símbolo vai no expoente do 2, o segundo no do 3, o terceiro no do 5, e assim por diante: 2^a · 3^b · 5^c · … ([Gödel numbering](https://en.wikipedia.org/wiki/G%C3%B6del_numbering)).

No sistema de Nagel e Newman, a fórmula "0 = 0", de apenas três símbolos, recebe o número 2⁶ × 3⁵ × 5⁶ = 243.000.000 ([Gödel numbering](https://en.wikipedia.org/wiki/G%C3%B6del_numbering)).

O que faz isso funcionar é o teorema fundamental da aritmética: todo número tem uma única fatoração em primos. De posse do número, fatorá-lo recupera exatamente a sequência de símbolos que o gerou, de forma mecânica e efetiva ([SEP](https://plato.stanford.edu/entries/goedel-incompleteness/)).

Há muitas numerações de Gödel possíveis, e o esquema escolhido é arbitrário. O que importa é que alguma escolha seja efetiva e reversível ([Gödel numbering](https://en.wikipedia.org/wiki/G%C3%B6del_numbering)).

Com fórmulas e demonstrações viradas em números, afirmações sobre o que o sistema prova passam a ser afirmações sobre números, dentro do próprio sistema. É esse o mecanismo que permite a Gödel construir uma sentença que fala da própria demonstrabilidade, e a partir dela provar [o teorema da incompletude](/notes/teorema-da-incompletude-de-godel).
