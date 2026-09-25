---
title: "Anatomy of the .NET dictionary"
date: '2026-09-25T08:26:24+01:00'
category: webclip
summary: 'Explains how .NET Dictionary stores entries in buckets and arrays, handles collisions with chaining, reuses freed slots, and grows or trims capacity.'
tags: ["csharp", "dotnet", "collections", "anatomy"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Anatomy of the .NET dictionary"
    url: "https://dunnhq.com/posts/2024/anatomy-of-the-dotnet-dictionary/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-09/dunnhq-com--anatomy-of-the-dotnet-dictionary.md"
    kind: repo
---

The post explains that .NET `Dictionary<TKey, TValue>` does not store key/value pairs directly. It uses two arrays, one for buckets and one for entries, and the bucket points into a chain of entries through encoded indices. Collisions are resolved by comparing hash codes and then equality, and removed entries are kept for reuse through a free list.

It also shows that dictionary capacity starts at a prime number, grows by resizing to the next prime when needed, and can be reduced with `TrimExcess`. `KeyValuePair` is described as part of the API rather than the internal storage format. ## Fichamento

- A `.NET Dictionary<TKey, TValue>` usa duas arrays internas, uma de buckets e outra de entries, em vez de guardar os dados como pares chave/valor.
- Os buckets apontam para entries por índices codificados; `0` marca bucket vazio e os valores são 1-based.
- Ao adicionar um item, a chave passa por `GetHashCode`, o bucket é calculado por módulo e a entry é colocada no índice disponível.
- Quando há colisão, a dictionary percorre a cadeia de entries do mesmo bucket e compara hash code e `Equals`.
- Se a chave já existir, a operação de inserção atualiza o valor ou lança exceção, conforme o modo de inserção.
- A cadeia entre entries é mantida pelo campo `next`, que também serve para ligar slots livres.
- Remover um item não apaga fisicamente a entry; ela é marcada como livre, entra na free list e pode ser reutilizada depois.
- `_freeList` aponta para o próximo slot livre e `_freeCount` conta quantos slots livres existem.
- A capacidade inicial usada no exemplo é 3, escolhida a partir de uma lista interna de números primos.
- Quando a capacity estoura, a dictionary resiza para um número primo maior, tipicamente dobrando e arredondando para cima.
- `Count` público é calculado como `_count - _freeCount`, por isso o total externo pode ser menor que o total interno.
- `TrimExcess` é citado como forma de liberar memória numa dictionary grande com muito churn.
- `KeyValuePair` é a interface para entrada e saída de dados, mas não é a forma como a dictionary armazena os valores internamente.
