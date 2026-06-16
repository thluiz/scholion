---
title: "O teorema da incompletude de Gödel"
date: 2026-06-16T15:16:10+01:00
summary: 'Em 1931, Gödel provou que todo sistema formal capaz de aritmética é incompleto ou inconsistente: há verdades que ele não alcança a partir das próprias regras. O que isso significa, e onde encosta nos LLMs.'
tags: ["godel", "logica", "incompletude", "llm"]
has_commentary: true
sources:
  - title: "Gödel's Incompleteness Theorems — Stanford Encyclopedia of Philosophy"
    author: "Panu Raatikainen"
    url: "https://plato.stanford.edu/entries/goedel-incompleteness/"
    kind: article
  - title: "Naruhodo #461 - O que é a teoria da Incompletude de Gödel? — Vox"
    url: "https://vox.thluiz.com/2026/03/W11/naruhodo-461-o-que-e-a-teoria-da-incompletude-de-godel"
    kind: podcast
---

No começo do século XX, a aposta era que a matemática podia ser fechada. Bastaria achar o conjunto certo de axiomas, as regras de partida, e dele se deduziria toda verdade matemática, sem contradição. Esse era o programa de David Hilbert: um sistema ao mesmo tempo completo (prova tudo o que é verdadeiro) e consistente (nunca prova uma coisa e o seu contrário).

Em 1931, com 25 anos, Kurt Gödel mostrou que isso é impossível ([Naruhodo #461](https://vox.thluiz.com/2026/03/W11/naruhodo-461-o-que-e-a-teoria-da-incompletude-de-godel)).

O **primeiro teorema da incompletude**, na formulação da Stanford Encyclopedia of Philosophy, diz que "qualquer sistema formal consistente F dentro do qual se possa realizar uma certa quantidade de aritmética elementar é incompleto; isto é, há afirmações da linguagem de F que não podem ser nem provadas nem refutadas em F" ([SEP](https://plato.stanford.edu/entries/goedel-incompleteness/)). Existem verdades que o sistema não alcança a partir das próprias regras.

O **segundo teorema** diz que um sistema desses não consegue provar a própria consistência. Para garantir que ele nunca vai se contradizer, é preciso apoiar-se em algo de fora dele ([SEP](https://plato.stanford.edu/entries/goedel-incompleteness/)).

### Como ele provou

Gödel faz o sistema dar uma volta sobre si mesmo. Inventou um jeito de traduzir cada fórmula da matemática num número, de forma mecânica e reversível (a [numeração de Gödel](/notes/numeracao-de-godel)). Com isso, a matemática passa a poder falar de si própria: afirmações sobre números viram afirmações sobre afirmações ([SEP](https://plato.stanford.edu/entries/goedel-incompleteness/)).

Aí ele constrói uma sentença que, lida por fora, equivale a "esta afirmação não pode ser provada neste sistema". Se o sistema provasse essa sentença, estaria provando algo falso e perderia a consistência; se não a prova, a sentença é verdadeira e o sistema não a alcança, ficando incompleto. A própria SEP avisa que essa leitura em português é uma simplificação: o teorema entrega uma equivalência formal, não uma frase que literalmente "diz" algo sobre si mesma ([SEP](https://plato.stanford.edu/entries/goedel-incompleteness/)).

### O que o teorema não diz

Uma leitura errada acha que Gödel provou existirem verdades absolutas, impossíveis de provar em qualquer lugar. A incompletude é sempre relativa a um sistema formal dado: o que é inalcançável dentro de um sistema pode virar teorema dentro de outro, mais forte ([SEP](https://plato.stanford.edu/entries/goedel-incompleteness/)).

Outra leitura supõe que todo sistema matemático é incompleto. Há sistemas completos e decidíveis, desde que não cheguem a expressar a aritmética inteira. A aritmética só com soma, sem multiplicação (a aritmética de Presburger), é um desses casos ([SEP](https://plato.stanford.edu/entries/goedel-incompleteness/)). A incompletude só aparece quando o sistema é rico o bastante para falar de aritmética.

### Onde isso encosta nos LLMs

No [Naruhodo #461](https://vox.thluiz.com/2026/03/W11/naruhodo-461-o-que-e-a-teoria-da-incompletude-de-godel), Altair de Souza leva o teorema para a inteligência artificial. A linguagem é um sistema formal: vocabulário finito, regras, e aritmética elementar possível com letras e sílabas. Um modelo de linguagem aproxima esse sistema, e é justamente por essa aproximação ser possível que, na leitura de Altair via Gödel, ela já nasce incompleta.

A imagem que Altair usa para a incompletude é a de uma função injetora, uma ida sem volta. Dá para associar uma pessoa a um número (a idade, por exemplo), mas do número não se reconstrói a pessoa. O modelo recebe tudo o que você disse, escreveu e fez, e ainda assim "não volta em você". Por isso ele enquadra a ideia de uma inteligência artificial geral como construção ideológica, sem estatuto de resultado científico ([Naruhodo #461](https://vox.thluiz.com/2026/03/W11/naruhodo-461-o-que-e-a-teoria-da-incompletude-de-godel)).

O autor já tinha anotado isso em [systems to describe for everything](/notes/systems-to-describe-for-everything-is-it-possible): usar máquinas finitas para mapear o real inteiro é confundir o mapa com o território, e exigir o mapa completo é improdutivo. Em [epistemological limitation defines the thing](/notes/epistemological-limitation-defines-the-thing), Žižek desloca a tese, e a incompletude passa a ser traço do próprio real.

Na pesquisa [Leibniz e os vetores](/research/leibniz-characteristica-vetores), isso entra como o ponto em que o projeto de uma língua-cálculo esbarra na incompletude, por dentro da própria lógica.
