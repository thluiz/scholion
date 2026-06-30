---
title: "Incompletude e consistência: os dois teoremas de Gödel"
date: 2026-06-16T15:51:39+01:00
summary: "Por que uma teoria que contém aritmética não pode ser completa nem demonstrar a própria consistência — os dois teoremas que Gödel provou em 1931."
tags: ["logica", "fundamentos-da-matematica", "filosofia-da-matematica", "godel"]
has_commentary: false
sources:
  - title: "Gödel's Incompleteness Theorems"
    publisher: "Stanford Encyclopedia of Philosophy"
    url: "https://plato.stanford.edu/entries/goedel-incompleteness/"
    kind: wiki
  - title: "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I"
    author: "Kurt Gödel"
    year: 1931
    publisher: "Monatshefte für Mathematik und Physik"
    kind: article
  - title: "Peano axioms"
    publisher: "Wikipedia"
    url: "https://en.wikipedia.org/wiki/Peano_axioms"
    kind: wiki
---

Os teoremas de Gödel tratam de duas propriedades de um sistema formal que costumam ser confundidas: consistência e completude. Separá-las é o primeiro passo para entender o que os teoremas afirmam.

Um sistema é **consistente** quando não demonstra nenhuma contradição: não existe sentença tal que ela e sua negação sejam ambas demonstráveis (Stanford Encyclopedia of Philosophy, "Gödel's Incompleteness Theorems"). É o requisito mínimo para o sistema ter qualquer valor. Uma teoria inconsistente demonstra tudo, verdadeiro e falso, e por isso não distingue nada.

Um sistema é **completo** quando decide toda sentença da sua linguagem: para cada afirmação, ou ela ou sua negação é demonstrável (SEP, idem). Uma teoria pode ser consistente e ainda assim incompleta: não se contradizer e mesmo assim deixar perguntas sem resposta. Gödel mostrou que uma teoria consistente capaz de formalizar aritmética suficiente sempre contém uma sentença que ela não prova nem refuta.

Os dois resultados saíram no mesmo artigo, "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I", publicado em janeiro de 1931 (SEP, "Gödel's Incompleteness Theorems"). O título aponta para os Principia Mathematica de Russell e Whitehead, o edifício erguido sobre a notação e os [axiomas de Peano](/notes/axiomas-de-peano/).

### O primeiro teorema

Qualquer sistema consistente, com axiomas efetivamente listáveis e aritmética suficiente, é incompleto: existe uma sentença da sua linguagem que ele não demonstra nem refuta (SEP, "Gödel's Incompleteness Theorems").

A construção usa auto-referência. Por uma técnica chamada diagonalização, Gödel constrói uma sentença G demonstravelmente equivalente, dentro do próprio sistema, à afirmação "G não é demonstrável neste sistema". A auto-referência aqui é apenas formal: pela numeração de Gödel, frases sobre demonstrações viram frases sobre números, e a SEP alerta contra a leitura de que G "fala de si mesma" em sentido substancial (SEP, idem).

Suponha que o sistema demonstrasse G. Então demonstraria algo equivalente a "G não é demonstrável", ou seja, uma falsidade sobre a própria atividade demonstrativa, o que indica inconsistência. O lado simétrico, a demonstração da negação de G, usa na prova original de Gödel uma hipótese um pouco mais forte, a ω-consistência, que Rosser enfraqueceu em 1936 para a consistência simples (SEP, idem). Sendo o sistema consistente, G fica indecidível. Como G é de fato indemonstrável e afirma justamente a própria indemonstrabilidade, G é verdadeira no modelo padrão, e o sistema não a prova (SEP, idem).

### O segundo teorema

O segundo resultado responde à pergunta "por que ela não prova a própria consistência". A afirmação "este sistema é consistente" também pode ser codificada como sentença aritmética, escrita Con(F). A questão é se F demonstra Con(F).

Se F é consistente, então F não demonstra Con(F) (SEP, "Gödel's Incompleteness Theorems"). O raciocínio do primeiro teorema (que "se F é consistente, então G é indemonstrável") pode ele mesmo ser reproduzido dentro de F. Formalizado, isso dá F ⊢ Con(F) → G. Se F demonstrasse Con(F), demonstraria G por simples lógica, contradizendo o primeiro teorema. Logo F não demonstra Con(F).

A intuição informal: pelos próprios axiomas, o sistema não consegue produzir a sentença Con(F) que codifica sua consistência. Há ainda o avesso, que mostra por que essa certificação seria inútil de qualquer modo: se uma teoria demonstrasse a própria Con(F), isso não garantiria nada, porque uma teoria inconsistente demonstra qualquer sentença, Con(F) inclusive.

O resultado depende de Con(F) ser expressa por um predicado de demonstrabilidade "razoável", que satisfaça as três condições de derivabilidade de Hilbert-Bernays-Löb. Com uma codificação artificial da consistência o resultado pode falhar; o segundo teorema vale para a consistência expressa de um modo que efetivamente signifique consistência (SEP, "Gödel's Incompleteness Theorems").

### Provar a consistência de fora

Que F não demonstre a própria consistência deixa em aberto se F é consistente; o resultado diz apenas que a prova, se houver, precisa usar um sistema mais forte que F. Em 1936, Gerhard Gentzen demonstrou a consistência da aritmética de Peano usando indução transfinita até o ordinal ε₀, um princípio que a própria aritmética de Peano não contém; por isso a prova não se formaliza dentro dela (Wikipedia, "Peano axioms").
