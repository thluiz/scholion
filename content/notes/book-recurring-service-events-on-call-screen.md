---
title: "Book recurring service events on the Call screen"
date: '2026-09-25T09:08:54+01:00'
category: webclip
summary: 'Configura jobs para exigir recurring service events quando houver eventos na service location, e usa a seleção no Call screen para manter deferred revenue em balance.'
tags: ["recurring-service-events", "call-screen", "job-types", "deferred-revenue"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Book recurring service events on the Call screen"
    url: "https://help.servicetitan.com/how-to/recurring-service-call-booking"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/help-servicetitan-com--book-recurring-service-events-on-call-screen.md"
    kind: repo
---

Set up the account so CSRs are prompted to use recurring service events relevant to the service location when booking specified job types on the Call screen. The feature applies to administrators and office employees, primarily for Residential Service and Replacement business types, and requires account configuration.

To use it, recurring services must already be set up through Memberships. Job types associated with recurring services can be marked as required so the booking workflow forces a selection when recurring service events exist for the location. During booking, the CSR can open the Select Recurring Event window, filter and sort the events, and choose one or more that apply to the job. Recurring service events also appear in Follow Ups, and the workflow is described as part of keeping Deferred revenue in balance.

## Fichamento

- A conta precisa estar configurada para que CSRs sejam orientados a usar recurring service events ligados à service location ao reservar job types específicos no Call screen.
- O recurso se aplica a administradores e office employees, beneficia principalmente Residential Service e Replacement e vale para todas as trades.
- É necessário ter recurring services configurados por meio de Memberships antes de usar recurring service events na reserva de jobs.
- Se dismissed recurring service events puderem ser reservados, eles aparecem na lista de recurring service events na Call Booking screen.
- Em Settings > Operations > Job Types, é possível editar um job type e marcar a opção que torna obrigatório selecionar um Recurring Service Event quando houver eventos para a location.
- Depois de ativado, o fluxo de booking passa a notificar quantos recurring service events existem na service location.
- O CSR pode usar Use Recurring Event, abrir a janela Select Recurring Event e filtrar ou ordenar os eventos para achar os que se aplicam ao job.
- Se houver mais de um recurring service event para o mesmo job, é possível selecionar todos os que forem aplicáveis.
- Quando o job type foi configurado como obrigatório, pelo menos um recurring service event precisa ser escolhido para continuar o booking workflow.
- Recurring service events aparecem em Follow Ups e são agendados com base nos frequency details dos recurring services da service location.
- O evento carrega detalhes do recurring service para apoiar a reserva do job.
- Deferred revenue é usada em accrual accounting para registrar receitas de serviços futuros quando eles são entregues, e memberships usam essa lógica para recurring services incluídos no plano.
