---
title: "Programação funcional e escalabilidade: o que uma coisa tem a ver com a outra?"
date: '2010-10-06T10:42:25-03:00'
category: webclip
summary: 'O texto liga programação funcional à escalabilidade ao destacar a ausência de estado mutável, a facilidade de testar e depurar, e a vantagem para concorrência, paralelismo e passagem de mensagens.'
tags: ["programacao-funcional", "escalabilidade", "paralelismo", "erlang"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Programação funcional x Escalabilidade"
    url: "http://www.google.com/reader/view/#stream/user%2F05215115956327655620%2Flabel%2FBlogs"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2010-10/google-com--programacao-funcional-x-escalabilidade.md"
    kind: repo
---

O texto apresenta a programação funcional como um paradigma que evita estado e dados mutáveis, e afirma que isso ajuda a testar, depurar e escrever programas concorrentes e paralelos. A partir daí, relaciona essa abordagem à escalabilidade, especialmente em sistemas multicore e em contextos distribuídos.

## Fichamento

- A programação funcional trata a computação como avaliação de funções matemáticas e evita estado e dados mutáveis.
- Por depender menos de estado compartilhado, o código tende a ser mais fácil de testar e de depurar.
- A ausência de variáveis compartilhadas facilita a escrita de programas concorrentes e paralelos, porque reduz a necessidade de semáforos, deadlocks e outros efeitos colaterais.
- O texto liga paralelismo à escalabilidade ao comentar a entrada de processadores multicore e a dificuldade de aproveitar todo o processamento disponível.
- Em sistemas distribuídos, o texto diz que a passagem de mensagens é uma alternativa quando não há compartilhamento de variáveis entre máquinas.
- O Erlang é apresentado como uma linguagem funcional e orientada à concorrência, criada na Ericsson para aplicações de telefonia.
- O texto destaca o hot code swapping como recurso que permite alterar o código sem parar o sistema.
- A comunicação entre processos no Erlang é descrita como assíncrona e sem compartilhamento de estado.
- O texto afirma que o Yaws, escrito em Erlang, atingiu cerca de 800 KBps e suportou até 80.000 conexões simultâneas, enquanto o Apache morreu em torno de 4.000 conexões.
- O post se coloca como uma introdução ao tema e diz que pretende abrir discussão e produzir mais textos sobre linguagens de programação e escalabilidade.
