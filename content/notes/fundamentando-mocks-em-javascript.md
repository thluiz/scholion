---
title: "Fundamentando Mocks em JavaScript"
date: '2020-07-05T14:10:34+00:00'
category: webclip
summary: 'O texto explica o que são mocks, quando usá-los e como aplicá-los no Jest com dados, funções, módulos e spies, além de limpar os mocks depois dos testes.'
tags: ["javascript", "jest", "mocks", "testing"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Fundamentando Mocks em JavaScript"
    url: "https://gabrieluizramos.com.br/fundamentando-mocks-em-javascript"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/gabrieluizramos-com-br--fundamentando-mocks-em-javascript.md"
    kind: repo
---

O texto defende o uso consciente de mocks para ganhar controle sobre dependências externas e assíncronas nos testes. Ele distingue dados, funções, módulos e spies, mostra como o Jest trata cada caso e reforça que a limpeza dos mocks evita efeitos colaterais entre testes.

## Fichamento

- Mocks substituem trechos de código por algo necessário ao teste, permitindo controlar a implementação.
- Em testes unitários, faz sentido mockar dependências fora do escopo da unidade testada, como requisições e outros efeitos externos.
- O texto usa o Jest como base, mas diz que os conceitos podem ser reaproveitados em outros frameworks.
- Mocks de dados aparecem como a forma mais simples, usando listas e valores criados no próprio teste.
- Para funções comuns, o Jest oferece `jest.fn()`, que pode receber uma implementação ou um valor de retorno pré-definido.
- O texto mostra asserções para verificar chamada, quantidade de chamadas, ausência de chamada e argumentos usados.
- Quando a dependência é passada como parâmetro, o teste pode criar uma função mock e verificar se ela foi executada na quantidade esperada.
- Quando a dependência vem de um módulo externo, o texto usa `jest.mock` para sobrescrever as exportações do módulo.
- Se for preciso inspecionar uma função sem substituir seu comportamento por completo, o texto usa `jest.spyOn`.
- `spyOn` é aplicado ao módulo `logger` para verificar chamadas da função `log` sem reimplementar sua lógica.
- O texto recomenda limpar mocks depois dos testes para evitar problemas em outros casos.
- Para spies, o texto usa `mockRestore`; para `jest.fn()`, menciona `mockClear`, `mockReset` e `mockRestore`.
- Também cita `jest.clearAllMocks()`, `jest.resetAllMocks()` e `jest.restoreAllMocks()` como formas de limpar vários mocks de uma vez.
