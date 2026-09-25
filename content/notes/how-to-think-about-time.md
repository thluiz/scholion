---
title: "How to Think About Time"
date: '2026-09-25T08:40:09+01:00'
category: webclip
summary: 'The guide separates physical time from civil time, defines instants, durations, datetimes, periods, and time zones, and warns about ambiguous math, storage, and wall-clock use.'
tags: ["time", "date-time", "time-zones"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "How to Think About Time"
    url: "https://errorprone.info/docs/time"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/errorprone-info--how-to-think-about-time.md"
    kind: repo
---

The guide builds time from two distinct realms. Physical time uses instants and durations on a timeline. Civil time uses datetimes and periods, with calendars and time zones as separate concerns. It argues that code should keep these concepts apart because mixing them creates ambiguity and bugs.

It also warns about several practical pitfalls: negative durations and periods, month-based math, storing values without thinking through time-zone changes, and using wall time to measure elapsed time. UTC is useful as a reference, but zone-independent code should stay in physical time and use types that model instants and durations only.

## Fichamento

- O texto propõe um modelo mental para datas e horas baseado em conceitos separados, em vez de práticas soltas.
- O tempo físico é descrito como uma timeline com instantes e durações, medidos em segundos.
- Durações são diferenças entre instantes; meses e anos não têm significado preciso nesse uso.
- Durações negativas são possíveis, mas o texto recomenda evitá-las por causa de bugs e expectativas implícitas.
- As operações válidas no tempo físico são instant menos instant igual a duração, instant mais ou menos duração igual a instant, duração com duração, e duração vezes ou dividido por número real.
- Um instante particular só pode ser referido com ajuda de uma duração em relação a um instante de referência, chamado epoch.
- O tempo civil é apresentado como um conjunto de conceitos humanos como meses, anos, dias úteis, feriados e calendários.
- No calendário gregoriano, data é ano, mês e dia; hora do dia é hora, minuto e segundo; datetime combina esses seis campos.
- O texto trata o calendário gregoriano prolepticamente para estender o sistema a toda a história.
- Fuso horário não é um sétimo campo do civil datetime; é o conjunto de regras que converte entre instante e datetime.
- Os melhores fusos horários são os da base IANA, como `America/New_York` e `Asia/Kolkata`.
- Códigos de três letras como `PST` são apontados como ruins porque geram ambiguidade e comportamento inconsistente.
- UTC é descrito como o fuso mais simples, com deslocamento fixo zero, usado como ponto de referência.
- Para código independente de fuso, o texto recomenda ficar apenas no tempo físico e usar tipos que modelam instantes e durações.
- Guardar instantes ou datetimes exige pensar em mudanças de fuso do usuário e em alterações nas regras de fuso.
- O texto desaconselha tipos que misturam datetime ou instante com fuso horário, porque eles juntam tempo físico e civil e tornam a serialização ambígua.
- Wall time é aproximado, pode sofrer correções e não deve ser usado para medir tempo decorrido.
- Tempo decorrido deve ser medido com uma ferramenta própria, como Stopwatch.
- Leap seconds são tratados como exceções raras que geralmente podem ser ignoradas, embora afetem leituras de relógio.
- Midnight nem sempre existe em um dia local; às vezes o correto é falar em start of day.
- Recorrências são regras para selecionar datas ou datetimes sucessivos, distintas da aritmética de períodos.
- O texto recomenda escrever datas em formato ISO `YYYY-MM-DD` para evitar ambiguidade cultural.
- A seção final lista APIs por linguagem que representam cada conceito de forma separada.
