---
title: "What the Team Behind Cursor Knows About the Future of Code"
date: '2026-09-25T08:41:20+01:00'
category: webclip
summary: 'Cursor’s team argues that code work is shifting from typing in an IDE to directing and reviewing AI agents, with planning, model choice, and long-running workflows becoming central.'
tags: ["cursor", "ai-coding", "software-development", "ai-agents"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "What the Team Behind Cursor Knows About the Future of Code"
    url: "https://every.to/source-code/what-the-team-behind-cursor-knows-about-the-future-of-code?utm_source=substack&utm_medium=email"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/every-to--what-team-behind-cursor-knows-about-future-of-code.md"
    kind: repo
---

Cursor’s team describes a post-IDE workflow where developers spend less time typing code by hand and more time planning work, directing agents, and reviewing what they produce. They also say cloud and local agents are starting to blend, and that choosing the right model matters more than prompt tricks.

## Fichamento

- O IDE continua existindo, mas o centro do trabalho está se deslocando para a interface de agente, onde a conversa com a IA vira a parte principal do processo.
- Em alguns casos, escrever código à mão pode representar só uma pequena parte do tempo de trabalho, enquanto o restante vai para orientar a IA e revisar o resultado.
- O modelo e o harness importam juntos, porque a infraestrutura em torno do modelo define como ele recebe contexto, lida com erros e executa tarefas longas.
- A equipe testou esse limite com um navegador web feito do zero por agentes, em uma tarefa que rodou por semanas, gerou 3 milhões de linhas de código e custou cerca de 80 mil dólares em tokens.
- O grupo trabalha para permitir que um agente comece no computador local, continue na nuvem e depois retome no computador do usuário sem perder contexto.
- Antes de codificar, Sam passa tempo em plan mode para detalhar o que quer construir, usando designs e capturas de tela quando o projeto é mais complexo.
- Para projetos maiores, ela divide o trabalho entre vários agentes em paralelo; para correções simples, às vezes pula o planejamento.
- Sam escolhe modelos por heurísticas próprias: Claude Opus para brainstorming e problemas mal especificados, GPT 5.2 Codex High para bug-finding e tarefas muito literais.
- Quando necessário, ela roda vários modelos ao mesmo tempo, compara as respostas e pede que um justifique a abordagem diante de outro.
- Cursor inclui ferramentas de revisão, como find issues e Bugbot, e a equipe interna não faz merge antes de tratar todos os comentários do Bugbot.
- Sam prefere uma abordagem de retrieval first, com pointers para conversas e documentos de plano, em vez de depender só de resumos comprimidos.
- A promessa dos agentes fica mais forte em tarefas complexas e multi-step; para tradução direta de Figma para código, os ganhos ainda são limitados.
