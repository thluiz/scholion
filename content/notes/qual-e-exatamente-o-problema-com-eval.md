---
title: "Qual é exatamente o problema com eval()"
date: '2012-06-12T13:31:38-03:00'
category: webclip
summary: 'O texto questiona os argumentos comuns contra eval() em JavaScript, dizendo que performance e segurança costumam ser exageradas e que o problema mais sério está na qualidade do código e na dificuldade de debugar.'
tags: ["javascript", "eval", "quality-of-code"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Qual é exatamente o problema com eval()?"
    url: "http://elcio.com.br/qual-e-exatamente-o-problema-com-eval/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/elcio-com-br--qual-e-exatamente-o-problema-com-eval.md"
    kind: repo
---

O texto diz que a reserva contra `eval()` vem mais de uma sensação de gambiarra e de falta de elegância do que de um problema técnico claro. Ele contesta os argumentos de performance e segurança, e trata como mais relevante a dificuldade de depuração quando algo dá errado.

## Fichamento

- O autor diz que seu incômodo com `eval()` é sobretudo uma questão de elegância e de aparência de improviso.
- Ele afirma que os argumentos de performance e segurança, na forma como costumam ser usados contra `eval()`, não o convenceram.
- Sobre performance, ele diz que o custo de interpretar código via `eval()` raramente importa nas situações em que a função seria útil.
- Ele observa que navegadores como V8, Nitro e SpiderMonkey já fazem cache do código passado a `eval()` em várias circunstâncias.
- Ele usa o caso de fallback para JSON como exemplo e diz que, depois de uma espera de dois segundos por Ajax, alguns milissegundos a mais não fazem diferença.
- Ele argumenta que trocar `eval()` por uma biblioteca de JSON com validações pode adicionar 17Kb de código sem trazer ganho real para esse caso.
- Sobre segurança, ele diz que não viu um caso real em que `eval()` por si só fosse a origem do problema.
- Ele sustenta que, quando o código vem de JSON gerado no servidor, o conteúdo já foi produzido pela própria aplicação e não por uma fonte externa aleatória.
- Ele afirma que, se um agressor já tem acesso ao servidor para injetar dados maliciosos, há problemas mais graves do que o uso de `eval()`.
- Ele diz que usar `eval()` com entrada do usuário no client significa, no máximo, que a pessoa executa código na própria máquina.
- Ele separa o problema de `eval()` do problema de não validar no servidor os dados produzidos por esse código.
- Ele também questiona a diferença entre executar código vindo por `eval()` e incluir scripts de serviços como Google Analytics, Twitter, Facebook e AddThis.
- O ponto que ele considera mais forte é o da qualidade do código, porque erros em código avaliado ficam mais difíceis de debugar.
- Ele diz que, no uso que faz de JSON, costuma confiar em bibliotecas ou módulos padrão de PHP e Python.
- Ele mostra um exemplo ruim de uso de `eval()` para acessar uma propriedade e diz que pode ser substituído diretamente por `document[obj].className='selected'`.
- O texto esclarece que criticar esses argumentos contra `eval()` não significa defender seu uso indiscriminado.
