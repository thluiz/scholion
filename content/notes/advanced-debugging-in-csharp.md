---
title: "Advanced Debugging in C#"
date: '2026-09-24T23:16:26+01:00'
category: webclip
summary: 'O artigo mostra técnicas avançadas de debugging no Visual Studio 2022 para C#: conditional breakpoints, tracepoints, hit count, filtros, edição de código, execution pointer, object IDs e string visualizer.'
tags: ["csharp", "visual-studio", "debugging"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Advanced Debugging in C#"
    url: "https://code-maze.com/csharp-advanced-debugging/?ref=dailydev"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/code-maze-com--advanced-debugging-in-csharp.md"
    kind: repo
---

The article walks through advanced debugging in C# using Visual Studio 2022. It starts with a simple loop-based example and then shows how breakpoints can be made conditional, turned into tracepoints, limited by hit count, filtered by thread or process, moved to a different line, and combined with code edits during a debugging session.

It also covers function breakpoints, dependent breakpoints, object IDs for tracking reference types across scope changes, and the string visualizer for formatted text such as HTML, JSON, or XML.

## Fichamento

- Usa um exemplo simples com uma lista de strings, um loop e o método `PrintPart()` para demonstrar as técnicas de debugging no Visual Studio 2022.
- Mostra como configurar conditional breakpoints para pausar só quando uma expressão é verdadeira, como quando o comprimento de `txt` é menor que 12.
- Explica tracepoints como breakpoints que escrevem mensagens no Output window sem interromper a execução, com suporte a condições e a palavras-chave como `$FUNCTION` e `$CALLER`.
- Apresenta hit count para fazer um breakpoint parar apenas após um número definido de ocorrências, incluindo a opção de agir em múltiplos de um valor.
- Descreve o Filter condition para restringir breakpoints a máquina, thread ou processo, usando campos como `ThreadId`, `ProcessName`, `ProcessId` e `MachineId`.
- Mostra que é possível mudar a localização de um breakpoint durante a depuração alterando o número da linha.
- Diz que o código pode ser editado no meio de uma sessão de debugging e que a execução continua a partir das alterações feitas.
- Explica o execution pointer como a seta amarela que indica a próxima linha a executar e pode ser movida para alterar o fluxo de execução.
- Apresenta function breakpoints para fazer o debugger parar numa função específica.
- Mostra dependent breakpoints, em que um breakpoint só é atingido depois de outro breakpoint já ter sido atingido.
- Explica object IDs como forma de acompanhar um objeto de referência mesmo depois de ele sair de escopo.
- Mostra o string visualizer como ferramenta para ver strings formatadas, incluindo HTML, JSON e XML, usando a Immediate window para atribuir um valor complexo.
