---
title: "Implementing a secure sandbox for local agents"
date: '2026-09-24T23:26:51+01:00'
category: webclip
summary: 'Cursor describes a sandbox for coding agents that cuts approval interruptions, preserves security, and adapts to macOS, Linux, and Windows limits while teaching agents when escalation is needed.'
tags: ["agent-sandboxing", "coding-agents", "security"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Implementing a secure sandbox for local agents"
    url: "https://cursor.com/blog/agent-sandboxing?utm_source=tldrai"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/cursor-com--implementing-a-secure-sandbox-for-local-agents.md"
    kind: repo
---

Cursor says coding agents gain power when they can run terminal commands automatically, but that also raises the risk of deleted databases, broken code, and leaked secrets. Requiring approval for every command leads to approval fatigue, especially when several agents run at once. The team rolled out agent sandboxing on macOS, Linux, and Windows so agents can work inside a controlled environment and ask for approval mainly when they need to go outside it, often for internet access. They report 40% fewer stops than unsandboxed agents.

## Fichamento

- O texto apresenta o sandbox como uma forma de reduzir interrupções sem abrir mão da segurança dos agentes locais.
- Ele descreve o problema das aprovações manuais acumuladas, que fazem os usuários deixarem de revisar cada pedido com cuidado.
- A implementação usa uma API uniforme, mas com mecanismos diferentes em cada sistema operacional.
- No macOS, a equipe avaliou App Sandbox, containers, máquinas virtuais e Seatbelt, e ficou com Seatbelt via sandbox-exec.
- No Linux, a solução combina Landlock e seccomp, com arquivos ignorados ficando inacessíveis ao processo em sandbox.
- No Windows, o Cursor executa o sandbox Linux dentro do WSL2 enquanto trabalha com a Microsoft por primitivas nativas mais adequadas.
- O texto também diz que o harness do agente precisou ser ajustado para explicar as restrições do sandbox e indicar quando a escalada de permissões é necessária.
- Depois dessas mudanças, o comportamento de recuperação melhorou e a avaliação offline também melhorou.
- O rollout gradual em produção confirmou o uso do recurso, e a empresa diz ver um terço das requisições em plataformas suportadas rodando com o sandbox.
