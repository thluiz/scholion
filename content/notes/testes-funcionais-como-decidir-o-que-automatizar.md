---
title: "Testes Funcionais - Como decidir o que automatizar?"
date: '2016-07-24T04:16:55+00:00'
category: webclip
summary: 'O texto explica por que automatizar testes, destacando feedback rápido, repetibilidade e economia de tempo, e propõe decidir o que automatizar pela relevância de negócio e pela taxa de erro.'
tags: ["testes-funcionais", "automacao-de-testes", "integracao-continua", "entrega-continuada"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Testes Funcionais - Como decidir o que automatizar?"
    url: "https://thoughtworks.com/pt/insights/blog/functional-tests-how-decide-what-automate"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/thoughtworks-com--testes-funcionais-como-decidir-o-que-automatizar.md"
    kind: repo
---

O texto diz que a automação ajuda a evitar trabalho manual repetido, acelerar o feedback, economizar tempo e manter os testes consistentes. Também observa que isso não elimina a necessidade de testes exploratórios em algum momento da pipeline.

## Fichamento

- Automatizar reduz retrabalho manual, acelera o feedback, economiza tempo e mantém as mesmas precondições e expectativas nos testes.
- Testes manuais repetidos tendem a ser cansativos e inconsistentes, com risco de erro humano, viés de confirmação e passos perdidos.
- O feedback rápido ajuda na integração contínua e na Entrega Contínua, porque permite detectar regressões quando o código é consolidado e corrigir problemas cedo.
- Mesmo com automação, ainda há espaço para testes exploratórios em algum momento da pipeline.
- A decisão sobre o que automatizar deve considerar a Pirâmide de Testes de Mike Cohn, em que há muito mais testes unitários do que testes automatizados de UI, serviço ou integração de alto nível.
- Tentar automatizar tudo o que seria testado manualmente pode gerar suítes grandes demais e regressões demoradas.
- Uma suíte longa de regressão vira gargalo na consolidação de alterações e pode levar a consolidações menos frequentes e maiores.
- O texto propõe focar nas áreas mais importantes para o negócio ou nas funcionalidades mais instáveis, com maior probabilidade de erro.
- Para escolher os testes, o texto sugere combinar relevância de negócios e taxa de erro de cada funcionalidade.
- A matriz de exemplo classifica features como Inbox, New mail, Login e Settings por relevância de negócios, taxa de erro e total.
- Como a relevância de negócios muda com o tempo, os testes devem ser revisados a cada iteração.
