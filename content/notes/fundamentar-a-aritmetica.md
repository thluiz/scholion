---
title: "O que significa \"fundamentar a aritmética\""
date: 2026-06-16T15:51:39+01:00
summary: "Categoricidade, modelos não-padrão e a leitura estrutural: o que está em jogo quando se diz que cinco axiomas fundamentam os números."
tags: ["filosofia-da-matematica", "logica", "fundamentos-da-matematica", "formalismo"]
has_commentary: false
sources:
  - title: "Peano axioms"
    publisher: "Wikipedia"
    url: "https://en.wikipedia.org/wiki/Peano_axioms"
    kind: wiki
  - title: "Dedekind's Contributions to the Foundations of Mathematics"
    publisher: "Stanford Encyclopedia of Philosophy"
    url: "https://plato.stanford.edu/entries/dedekind-foundations/"
    kind: wiki
  - title: "Recent Work on the Principles of Mathematics"
    author: "Bertrand Russell"
    year: 1901
    publisher: "International Monthly, Vol. 4"
    kind: article
---

Dizer que cinco axiomas "fundamentam a aritmética" é dizer algo preciso: que toda verdade sobre os números naturais deveria seguir desses axiomas mais a lógica, e que os axiomas determinam de que objeto se está falando. Os [axiomas de Peano](/notes/axiomas-de-peano/) fixam o papel de um elemento inicial e de uma operação de sucessor; não dizem o que o 0, o 1, o 2 são. Qualquer estrutura que satisfaça essas regras conta como um modelo.

Na versão de segunda ordem dos axiomas, quando a indução quantifica sobre todos os subconjuntos, o sistema é categórico: Dedekind provou em 1888 que dois modelos quaisquer são isomorfos (Stanford Encyclopedia of Philosophy, "Dedekind's Contributions to the Foundations of Mathematics"). A menos de isomorfismo, há um único modelo. É o sentido forte de "fundamentar": os axiomas fixam a estrutura dos naturais por inteiro.

Em primeira ordem o quadro muda. A aritmética de primeira ordem não é categórica. Pelo teorema de Löwenheim-Skolem (Wikipedia, "Peano axioms") existem modelos não-padrão, de todas as cardinalidades infinitas, que satisfazem os mesmos axiomas sem ser os números naturais usuais; Skolem construiu um explicitamente em 1933 (idem). E por Gödel (1931), nenhum sistema consistente desse tipo demonstra todas as verdades aritméticas, nem a própria consistência ([incompletude e consistência](/notes/incompletude-e-consistencia-godel/)).

Na leitura estrutural, a aritmética trata de relações entre posições numa sequência gerada pelo sucessor. É a tese que Russell formulou em "Recent Work on the Principles of Mathematics" (1901), ao escrever que na matemática "nunca sabemos do que estamos falando, nem se o que dizemos é verdadeiro" ([nota](/notes/mathematics-never-know-what-talking-about/)). A verdade está na estrutura das relações, não nos referentes que elas poderiam ter. Os axiomas de Peano caracterizam essa estrutura por meio do 0, do sucessor e da indução, e objetos diferentes podem satisfazê-la.
