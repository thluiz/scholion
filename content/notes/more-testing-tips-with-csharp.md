---
title: "More Testing Tips With C#"
date: '2026-09-25T08:48:53+01:00'
category: webclip
summary: 'The post shares testing tips for C#: generating fake data with Faker.NET or Bogus.NET, using seeds to reproduce randomized tests, comparing output against reference files, and finding free ports or loopback IPs for integration tests.'
tags: ["csharp", "testing", "bogus-net", "faker-net"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "More Testing Tips With C#"
    url: "https://gamlor.info/posts-output/2024-12-11-csharp-testing-stuff/en/?utm_source=newsletter.csharpdigest.net&utm_medium=newsletter&utm_campaign=the-impact-of-locks-and-waits-on-latency&_bhlid=c6a32769d7d59536ee2ffdf5867fbd7fbe6a953b"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/gamlor-info--more-testing-tips-with-csharp.md"
    kind: repo
---

The post gathers a few C# testing tips around test data, reference outputs, and integration-test setup. It says test data generators help when hand-written data gets tedious, seeds make randomized tests reproducible, and reference files work well for stable rendering output.

It also shows how to find a free TCP port with `Socket`, and notes that the whole `127.0.0.0/8` loopback range can be used when a fixed port is required. ## Fichamento

- Em testes, geradores de dados ajudam quando criar exemplos à mão fica trabalhoso e os dados acabam pouco realistas.
- O texto apresenta o `Faker` como uma opção que produz dados em inglês e mais “humanos”, sem foco em casos-limite.
- O `Bogus.NET` é mostrado como uma biblioteca mais ampla, com fábricas de objetos de teste, suporte a vários locais e conjuntos de dados adicionais.
- Ao usar dados aleatórios em testes, o texto recomenda controlar a seed para poder reproduzir uma falha com o mesmo conjunto de dados.
- A seed pode ser definida globalmente no `Bogus.Randomizer.Seed` ou por instância com `UseSeed`.
- Esse estilo de teste é descrito como uma forma simples de property-based testing, porque gera dados aleatórios e verifica se uma propriedade do sistema se mantém.
- Outra técnica é guardar uma referência boa do resultado e comparar com a saída atual, o que funciona bem para código de renderização como HTML, imagens ou SVG.
- Quando o teste falha nesse modelo, o texto sugere inspecionar as diferenças e, se a mudança for esperada, copiar os arquivos de `current` para `reference` e commitar.
- Para testes de integração, o texto mostra como descobrir uma porta TCP livre usando `Socket` com bind em `127.0.0.1:0`.
- Se uma porta fixa for exigida, o texto diz que o intervalo `127.0.0.0/8` pertence à máquina local e permite usar muitos IPs de loopback, como `127.0.0.2` e `127.0.0.3`, na mesma porta.
