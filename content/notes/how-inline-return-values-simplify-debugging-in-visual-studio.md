---
title: "How Inline Return Values Simplify Debugging in Visual Studio 2022"
date: '2026-09-25T07:58:57+01:00'
category: webclip
summary: 'Visual Studio 2022 adds Inline Return Values to show function return values directly in the editor, and Copilot can explain them or suggest fixes during debugging.'
tags: ["visual-studio-2022", "debugging", "copilot", "return-values"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How Inline Return Values Simplify Debugging in Visual Studio 2022"
    url: "https://devblogs.microsoft.com/visualstudio/how-inline-return-values-simplify-debugging-in-visual-studio-2022/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/devblogs-microsoft-com--how-inline-return-values-simplify-debugging-in-visual-studio.md"
    kind: repo
---

Visual Studio 2022 adds Inline Return Values so you can see a function’s return value directly in the editor, next to the closing brace. The post says this reduces temporary variables and lets you inspect behavior without leaving your code.

With Copilot integration, you can hover over the inline value and choose Ask Copilot. The debugger sends context to Copilot, which can explain the value and suggest code fixes if needed. The feature also works with native and managed code and is part of broader Copilot-assisted analysis for Locals, Autos, Watch windows, and DataTips.

## Fichamento

- Inline Return Values mostram o valor que será retornado antes da função sair, diretamente no editor.
- A ideia é evitar variáveis temporárias só para inspecionar return values.
- O valor aparece ao lado da chave de fechamento do método quando você chega a um breakpoint ou avança passo a passo.
- Ao passar o mouse sobre o datatip, é possível clicar em Ask Copilot para abrir uma janela de chat.
- O debugger envia contexto relevante para o Copilot, que explica os valores e pode sugerir correções de código.
- O post diz que o recurso funciona tanto para código nativo quanto gerenciado.
- A mesma análise assistida por Copilot também está disponível para Locals, Autos, Watch windows e DataTips.
