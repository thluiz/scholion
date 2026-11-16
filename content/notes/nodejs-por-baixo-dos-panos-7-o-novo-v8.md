---
title: "Node.js Por Baixo dos Panos #7 - O Novo V8"
date: '2020-04-20T21:22:44+00:00'
category: webclip
summary: 'O texto explica a troca do pipeline antigo do V8 por Ignition e TurboFan, mostrando como bytecode, uso de memória e otimização passaram a organizar a execução do JavaScript.'
tags: ["v8", "ignition", "turbofan", "javascript"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Node.js Por Baixo dos Panos #7 - O Novo V8"
    url: "https://dev.to/khaosdoctor/node-js-por-baixo-dos-panos-6-o-novo-v8-9h5"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/dev-to--nodejs-por-baixo-dos-panos-7-o-novo-v8.md"
    kind: repo
---

O texto descreve a mudança do V8, que saiu do pipeline com Full-Codegen e Crankshaft e passou a usar Ignition e TurboFan. A ideia central é que o AST continua sendo analisado, mas agora o Ignition gera bytecode para reduzir memória e acelerar a compilação, enquanto o TurboFan assume a otimização.

## Fichamento

- Após a versão V8.5.9, o V8 trocou o pipeline antigo por outro com Ignition e TurboFan, e esse novo arranjo é apontado como um dos motivos da velocidade atual do JavaScript.
- As etapas iniciais continuaram as mesmas, com geração de AST e análise do código, mas o Full-Codegen foi substituído pelo Ignition e o Crankshaft pelo TurboFan.
- O Ignition é um interpretador de bytecode criado principalmente para reduzir uso de memória, já que o modelo antigo podia prender até 20% da memória do heap do V8.
- O texto afirma que o Ignition não é um parser; ele lê o código em bytecode e o emite em bytecode, gerando um bytecode menor e removendo código não usado.
- Em vez de compilar JavaScript em tempo real com lazy load, o Ignition analisa e compila o script inteiro de uma vez, o que reduz o tempo de compilação e o tamanho do bytecode.
- No novo fluxo, o AST alimenta o Ignition, que percorre os nós e produz bytecodes usados como nova fonte para os compiladores.
- O bytecode é descrito como baseado em registradores, com registros para variáveis locais, argumentos da função e um accumulator implícito para entradas, saídas e resultados.
- O texto exemplifica instruções de bytecode como carregar constantes, subtrair argumentos, armazenar em registrador, multiplicar, somar e retornar.
- Antes da interpretação, o parser aplica otimizações como otimização de registros, peephole e remoção de código morto, permitindo bytecodes menores e mais otimizados.
- O Ignition não foi escrito em C++ nem em assembly manual; o texto diz que ele usa o back-end do TurboFan, um macroassembler de gravação única, para funcionar em várias arquiteturas.
- O TurboFan substituiu o Crankshaft como compilador JIT de otimização do JavaScript e foi pensado primeiro como um bom compilador para WebAssembly.
- O TurboFan usa a representação Sea-of-Nodes e foi criado para lidar melhor com JavaScript geral e com código ES6, que o Crankshaft não sabia tratar bem.
- Houve um período em que o TurboFan servia como compilador secundário para ES6, mas o pipeline foi depois simplificado, com o Ignition fornecendo bytecode como nova fonte comum para os compiladores.
- A separação em front-end, otimização e back-end permitiu reduzir código específico de máquina, e o texto cita uma queda de 29% nesse tipo de código.
- O texto chama de picos de má-otimização os casos em que um código rápido caía em uma situação que o Crankshaft não conseguia tratar, ficando até 100 vezes mais lento.
- Também menciona que, por causa dessa execução imprevisível, os desenvolvedores precisavam escrever um "CrankScript" para agradar o Crankshaft.
- As otimizações prematuras são descritas como um problema porque o interpretador era mais importante para o V8, e o Ignition ajudou ao reduzir a AST, o bytecode e o uso de memória, adiando otimizações mais pesadas para depois.
