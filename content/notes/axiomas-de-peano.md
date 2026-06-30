---
title: "Os axiomas de Peano"
date: 2026-06-16T15:51:39+01:00
summary: "Os cinco axiomas que Peano publicou em 1889, a aritmética que se constrói sobre eles, e o limite que Gödel impôs em 1931."
tags: ["matematica", "logica", "fundamentos-da-matematica", "giuseppe-peano"]
has_commentary: false
sources:
  - title: "Arithmetices principia, nova methodo exposita"
    author: "Giuseppe Peano"
    year: 1889
    publisher: "Fratelli Bocca"
    kind: book
  - title: "Was sind und was sollen die Zahlen?"
    author: "Richard Dedekind"
    year: 1888
    publisher: "Vieweg"
    kind: book
  - title: "Dedekind's Contributions to the Foundations of Mathematics"
    publisher: "Stanford Encyclopedia of Philosophy"
    url: "https://plato.stanford.edu/entries/dedekind-foundations/"
    kind: wiki
  - title: "Peano axioms"
    publisher: "Wikipedia"
    url: "https://en.wikipedia.org/wiki/Peano_axioms"
    kind: wiki
  - title: "Goodstein's theorem"
    publisher: "Wikipedia"
    url: "https://en.wikipedia.org/wiki/Goodstein%27s_theorem"
    kind: wiki
  - title: "Paris–Harrington theorem"
    publisher: "Wikipedia"
    url: "https://en.wikipedia.org/wiki/Paris%E2%80%93Harrington_theorem"
    kind: wiki
---

Giuseppe Peano apresentou seus axiomas em "Arithmetices principia, nova methodo exposita" (Turim, 1889), escrito em latim. As noções primitivas são "número", "um", "sucessor" e "igual a"; sobre elas Peano enuncia nove axiomas, dos quais quatro tratam da igualdade e hoje são contados como parte da lógica subjacente, não da aritmética (Wikipedia, "Peano axioms"). Restam cinco, na forma em que se costuma apresentá-los, modernamente partindo de 0 em vez do 1 original:

1. 0 é um número natural.
2. Todo número natural tem um sucessor, que também é número natural.
3. 0 não é sucessor de nenhum número natural.
4. Se dois números têm o mesmo sucessor, são iguais (o sucessor é injetivo).
5. Se um conjunto contém 0 e contém o sucessor de cada um de seus elementos, então contém todos os números naturais.

O quinto é o princípio de indução: permite provar uma propriedade para infinitos casos sem dar infinitas demonstrações (Wikipedia, "Peano axioms").

A prioridade é de Richard Dedekind, que publicou a mesma caracterização um ano antes em "Was sind und was sollen die Zahlen?" (1888). Peano reconheceu a precedência de Dedekind (Stanford Encyclopedia of Philosophy, "Dedekind's Contributions to the Foundations of Mathematics"), e por isso o sistema também é chamado de axiomas de Dedekind-Peano. Foi Dedekind quem provou que dois sistemas quaisquer satisfazendo os axiomas são isomorfos (a categoricidade) e quem justificou as definições por recursão, o teorema que permite definir adição e multiplicação a partir do sucessor.

A partir do sucessor, a recursão define a soma (a + 0 = a e a + S(b) = S(a + b)), e sobre ela vêm o produto, a ordem e suas propriedades, provadas por indução. A notação e os axiomas de Peano entraram no programa logicista, a tentativa de derivar a matemática da lógica. Russell conheceu o trabalho de Peano em 1900 e adotou sua notação nos Principia Mathematica, escritos com Whitehead entre 1910 e 1913 (Wikipedia, "Giuseppe Peano").

O limite veio depois. Em 1931, Kurt Gödel provou que a aritmética de primeira ordem construída sobre esses axiomas é incompleta: há sentenças verdadeiras no modelo padrão que ela não demonstra (Wikipedia, "Peano axioms"). Pelo segundo teorema de Gödel, ela também não demonstra a própria consistência: a afirmação "estes axiomas não geram contradição", uma vez codificada como sentença aritmética, não é demonstrável a partir deles (ver [incompletude e consistência](/notes/incompletude-e-consistencia-godel/)). Em 1936, Gerhard Gentzen demonstrou a consistência da aritmética de Peano usando indução transfinita até o ordinal ε₀, fora dos próprios recursos do sistema (Wikipedia, "Peano axioms"). Há exemplos concretos de enunciados verdadeiros mas independentes dos axiomas: o teorema de Goodstein (provado por Reuben Goodstein em 1944, mostrado indemonstrável na aritmética de Peano por Kirby e Paris em 1982; Wikipedia, "Goodstein's theorem") e o teorema de Paris-Harrington (1977), apontado como o primeiro enunciado "natural" da matemática verdadeiro nos inteiros mas independente dos axiomas de Peano (Wikipedia, "Paris–Harrington theorem").

Para o sentido formal de "fundamentar", ver [o que significa "fundamentar a aritmética"](/notes/fundamentar-a-aritmetica/).
