---
title: "A crash course in memory management"
date: '2026-09-25T09:05:28+01:00'
category: webclip
summary: 'Explains memory as fixed-size boxes with addresses, contrasts JavaScript’s automatic garbage collection with manual allocation and freeing in C, and links that tradeoff to performance and bugs.'
tags: ["memory-management", "javascript", "garbage-collection", "webassembly"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "A crash course in memory management – Mozilla Hacks - the Web developer blog"
    url: "https://hacks.mozilla.org/2017/06/a-crash-course-in-memory-management/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/hacks-mozilla-org--a-crash-course-in-memory-management.md"
    kind: repo
---

The article explains memory as fixed-size boxes with addresses and uses that model to show how JavaScript engines allocate values, track reachability, and reclaim memory through garbage collection. It contrasts that automatic management with C-style manual memory management, where developers use malloc and free and must decide when memory can be released.

It says automatic memory management reduces developer burden but adds overhead and can make performance unpredictable. Manual memory management gives more direct control, but mistakes can cause bugs, security holes, or running out of memory. The article frames this tradeoff as part of the background for ArrayBuffer and SharedArrayBuffer in JavaScript.

## Fichamento

- Apresenta a memória como caixas do mesmo tamanho, cada uma com um endereço, para explicar onde os dados ficam guardados.
- Mostra que números entram diretamente na memória em binário, enquanto letras e outros caracteres precisam de codificação e decodificação.
- Explica que, em JavaScript, a engine faz a alocação de memória e acompanha se um valor ainda pode ser alcançado no programa.
- Define garbage collection como o processo de liberar memória de valores que já não podem ser alcançados.
- Diz que linguagens com esse modelo são memory-managed languages e que isso facilita o trabalho do desenvolvedor, embora adicione overhead.
- Compara com C e WebAssembly, onde a memória é manipulada diretamente e o ambiente de execução inclui código auxiliar para codificação e decodificação de bytes.
- Afirma que, em gerenciamento manual, o runtime pode manter uma free list, e que malloc e free servem para pedir e devolver memória.
- Aponta que decidir quando liberar memória é difícil e que erros nessa decisão podem gerar bugs, falhas de segurança ou falta de memória.
- Conecta esse custo e essa dificuldade ao motivo de muitas linguagens modernas preferirem gerenciamento automático.
