---
title: "Performance Improvements in .NET 9"
date: '2026-09-25T07:57:45+01:00'
category: webclip
summary: 'A release tour of .NET 9 performance work across the JIT, GC, runtime, libraries, and tooling, with benchmarked gains in casts, loops, bounds checks, vectorization, LINQ, regex, JSON, networking, and more.'
tags: ["dotnet", "performance", "jit", "runtime"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Performance Improvements in .NET 9"
    url: "https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-9/?_bhlid=19677f8720c25fb16cce66e0ac29aa1f1cb4c9af"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/devblogs-microsoft-com--performance-improvements-in-net-9.md"
    kind: repo
---

The post surveys performance work in .NET 9 across the stack. It highlights JIT changes such as dynamic PGO for casts and lengths, tier 0 boxing fixes, loop and bounds-check optimizations, stronger branch reasoning, and new AVX512, Arm64, and SVE code generation. It also covers GC, threading, reflection, Native AOT, and many library updates that reduce allocation, remove unnecessary work, and improve throughput.

## Fichamento

- O texto diz que .NET 9 reúne mais de 350 pull requests focados em desempenho, com melhorias em JIT, GC, VM, Mono, Native AOT, reflection, numerics, strings, LINQ, compression, cryptography, networking, JSON e diagnostics.
- No JIT, o post destaca dynamic PGO para otimizar casts e tamanhos comuns, além de mudanças que reduzem boxing em tier 0 e melhoram loops, bounds checks, branches, inlining e operações com `Nullable<T>`.
- Em código vetorial e intrínsecos, o texto aponta suporte a SVE e AVX10.1, melhorias em AVX512, novas instruções e mudanças que aceleram `SearchValues`, `TensorPrimitives`, `BigInteger`, `Base64`, `Hex`, `BitArray`, `Quaternion` e outras rotinas numéricas.
- O post relata que o GC em modo server passou a usar DATAS por padrão, que há menos custo em write barriers, e que houve mudanças para reduzir alocações em várias rotinas do runtime e da biblioteca base.
- Em reflexão e metaprogramação, o texto mostra ganhos em `Delegate.EnumerateInvocationList`, `ActivatorUtilities.CreateInstance`, `FieldInfo`, `UnsafeAccessor`, `Type.GetType`, `Enum.Parse` e `JsonSerializer` com enumeração e caches mais baratos.
- Em LINQ, o texto descreve uma grande reorganização interna dos iteradores, com menos dispatch de interface, novos atalhos para arrays e listas, melhorias em `ToArray`, `ToList`, `ToDictionary`, `OrderBy`, `GroupBy`, `Distinct`, `Union`, `Any`, `First`, `Single`, `SequenceEqual`, `Chunk` e `DefaultIfEmpty`.
- Em strings, spans e regex, o post destaca `SearchValues<string>`, `IndexOfAny`, `ContainsAny`, `EndsWith`, `Split` sobre spans, `Regex.EnumerateSplits`, e uso mais amplo de vetorização para buscas e comparações.
- Em networking, o texto menciona ganhos em `SslStream`, handshake TLS, resumption, HTTP/1.1 connection pooling, `HttpClient`, `WebUtility`, `HttpUtility`, `WebSocket` e `Uri`, além de novas APIs para `JsonSerializer` sobre `PipeWriter`.
- No fim, o autor explica que escreve esses posts para aprender, testar, agradecer contribuições, divulgar ganhos gratuitos de desempenho e mostrar técnicas que leitores podem aplicar no próprio código.
