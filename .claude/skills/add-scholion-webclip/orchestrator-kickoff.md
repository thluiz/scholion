# Como iniciar o processamento do lote de webclips

Comando pronto pra colar como primeira mensagem numa **sessão nova** do
Claude Code (cwd em `E:\scholion`), pra rodar o `batch-playbook.md` contra
a fila unificada (`C:\Users\conta\OneDrive\MD\_webclip_manifest.json`).

Recomendado abrir sessão nova em vez de continuar numa sessão já longa —
o manifesto é a fonte de verdade, retomar é só reler `_webclip_manifest.json`
e seguir dos `pending` restantes.

## Comando

```
Você é o orquestrador do processamento em lote de webclips. Leia
E:\scholion\.claude\skills\add-scholion-webclip\batch-playbook.md — essa é
a fila unificada (C:\Users\conta\OneDrive\MD\_webclip_manifest.json), MDs
legados e URLs do Edge no mesmo manifesto.

Despache agentes general-purpose (Task/Agent tool) SEQUENCIALMENTE, nunca
em paralelo, um de cada vez. Cada dispatch processa os próximos 15 itens
`pending` do manifesto, exatamente como o playbook descreve — inclua o
conteúdo do playbook inteiro no prompt de cada agente, ele precisa dele.

Depois de CADA dispatch: confira o resumo do agente, e a cada poucos lotes
(3-4) rode `git push` em E:\scholion pra não acumular commits locais.

Continue despachando lotes até eu pedir pra parar. Nunca use a ferramenta
Monitor. Se um lote travar ou reportar algo estranho, pare e me avise em
vez de tentar contornar sozinho.

Comece relatando quantos itens `pending` existem por tipo (md_file vs url)
antes do primeiro dispatch.
```

## Detalhes pra ter em mente

- Cada dispatch consome ~15 chamadas de `compose` — com o limite de 500/dia
  na key `add-scholion-webclip-batch`, dá pra rodar uns 30+ lotes por dia
  antes de esbarrar no teto (dificilmente vai bater, já que a latência real
  do `compose` limita o ritmo antes do budget).
- Se a sessão orquestradora ficar muito longa, vale abrir uma sessão nova
  pra continuar — não perde nada, o manifesto é que importa.
- Pra checar progresso a qualquer momento, sem reabrir a fila inteira:
  perguntar "quantos itens pending sobraram no manifesto, por tipo?" em
  qualquer sessão nova com acesso a `E:\scholion`.
- Variar o tamanho do lote (o "15" no comando) se quiser — 12-18 é a faixa
  já testada; maior que isso aumenta o risco de a sessão do agente estourar
  contexto no meio do lote.
