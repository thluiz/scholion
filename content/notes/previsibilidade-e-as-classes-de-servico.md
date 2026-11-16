---
title: "Previsibilidade e as classes de serviço"
date: '2016-06-15T16:56:54+00:00'
category: webclip
summary: 'O texto defende que classes de serviço melhoram a priorização, mas pioram a previsibilidade quando quebram premissas da Lei de Little. Propõe reduzir WIP, tempos de espera e variabilidade para encurtar lead times.'
tags: ["previsibilidade", "classes-de-servico", "lei-de-little", "kanban"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Previsibilidade e as classes de serviço | by Thoughtworks Brasil | Desenvolvimento ágil | Thoughtworks | Medium"
    url: "https://medium.com/desenvolvimento-%C3%A1gil/previsibilidade-e-as-classes-de-servi%C3%A7o-24c20fabacdd"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/medium-com--previsibilidade-e-as-classes-de-servico.md"
    kind: repo
---

O texto relaciona classes de serviço com previsibilidade em fluxo de trabalho. Usa a fila do aeroporto para mostrar como itens urgentes e casos preferenciais alteram a ordem de atendimento e tornam difícil estimar quando um item vai terminar.

## Fichamento

- Classes de serviço são políticas que mudam a ordem de puxar itens depois que eles entram no processo.
- A ideia é tratar alguns itens de forma diferente por valor de negócio ou perfil de risco.
- Em software, isso aparece quando o trabalho normal é interrompido para atender um item regulatório atrasado.
- Classes de serviço não são a mesma coisa que priorização; a priorização acontece antes do item entrar no processo.
- Depois que o item entra no processo, a proposta mais adequada para a previsibilidade é tratar tudo em first in, first served.
- A Lei de Little relaciona lead time médio, WIP médio e vazão média.
- Quanto mais o processo respeita as premissas da Lei de Little, mais previsível e estável ele tende a ficar.
- As premissas citadas incluem entrada e saída em equilíbrio, trabalho que termina, WIP parecido no início e no fim do intervalo, idade média do WIP estável e unidades consistentes.
- Limitar WIP ajuda a manter entrada e saída em equilíbrio.
- Se um item perde valor de negócio, ele pode ser removido do processo, mas isso afeta as métricas e exige tratamento adequado ao contabilizar o trabalho.
- Classes de serviço fazem parte do custo de fazer alguns itens envelhecerem para que outros tenham lead time menor.
- Se houver slack no sistema, ele pode absorver classes de serviço sem tanto impacto na previsibilidade.
- O texto cita a classe de serviço "Intangível" para trabalho importante sem necessidade imediata, como atualizar banco de dados ou pagar dívida técnica.
- Mesmo assim, o autor defende que trabalho técnico deveria ser traduzido em valor para o negócio ou em aumento de capacidade.
- O texto não rejeita classes de serviço, mas afirma que elas reduzem a previsibilidade.
- Um caso em que isso se justifica é uma queda em servidor de produção, quando a espera não é aceitável.
- Quando o valor de negócio não pode ser avaliado de antemão, o autor sugere que a avaliação aconteça depois, com feedback real em produção.
- Para reduzir lead time médio, é preciso reduzir WIP médio, aumentar a vazão média ou ambos.
- O autor considera o controle de WIP uma alavanca melhor do que horas extras ou movimentação de pessoas entre projetos.
- Antes de mudar o processo, é preciso medir os efeitos das mudanças.
- Métricas de fluxo como WIP, lead time, vazão e tempos de espera ajudam a acompanhar as mudanças.
- Diagramas como cumulative flow diagram e lead time scatter plot ajudam a fazer perguntas e verificar o efeito das alterações.
- O texto destaca o tempo de espera como uma fonte comum de aumento de lead time.
- Em muitos processos, itens passam mais tempo esperando do que sendo trabalhados.
- Reduzir WIP e tempos de espera diminui o lead time e pode melhorar a qualidade, porque os problemas aparecem mais cedo.
