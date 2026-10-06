---
title: "Melhorando o desempenho de aplicativos .NET - Parte 05"
date: '2012-06-18T11:18:27-03:00'
category: webclip
summary: 'O artigo explica quando usar Finalize e Dispose, como aplicar o padrão Dispose em C#, e quais cuidados evitam finalização desnecessária, bloqueios e liberação tardia de recursos.'
tags: ["dotnet", "csharp", "dispose", "garbage-collector"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Melhorando o desempenho de aplicativos .NET - Parte 05"
    url: "https://imasters.com.br/dotnet/melhorando-o-desempenho-de-aplicativos-net-parte-05"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-06/imasters-com-br--melhorando-o-desempenho-de-aplicativos-net-parte-05.md"
    kind: repo
---

O texto diferencia finalização e liberação explícita de recursos em .NET. Finalize fica a cargo do coletor de lixo e serve para limpar recursos não gerenciados; Dispose é usado quando o código chamador deve liberar recursos imediatamente. O artigo também apresenta o padrão Dispose e resume cuidados para evitar finalizadores desnecessários e reduzir custo de coleta.

## Fichamento

- Finalize é usado para liberar recursos não gerenciados quando o objeto vai ser coletado, sem controle direto do momento da chamada.
- A finalização costuma exigir ao menos dois ciclos de coleta para liberar totalmente a memória do objeto.
- Em C#, o finalizador é escrito com a sintaxe de destructor.
- Dispose é indicado quando o código chamador precisa liberar explicitamente recursos externos.
- A implementação de Dispose pode evitar a finalização com GC.SuppressFinalization.
- Classes como arquivos e conexões de banco de dados podem expor Close além de Dispose, com comportamento equivalente em casos bem escritos.
- O padrão Dispose usa um campo para impedir chamadas repetidas, um Dispose(bool) para a limpeza comum e um finalizador que chama Dispose(false).
- Se houver código dependente de variáveis estáticas ou métodos estáticos no momento da finalização, o texto orienta verificar Environment.HasShutdownStarted.
- A instrução using em C# gera, na compilação, um bloco try/finally que chama Dispose ao sair do escopo.
- O artigo recomenda não implementar Finalize sem necessidade, para não aumentar a carga da thread de finalização e do coletor de lixo.
- Finalize faz sentido quando o objeto mantém recursos não gerenciados entre chamadas do cliente e precisa de limpeza caso Dispose não seja chamado.
- Em gráficos de objetos, a carga de finalização deve ficar nas folhas que detêm os recursos não gerenciados.
- Quem implementa Finalize também deve implementar IDisposable, e se implementar ambos deve seguir o padrão Dispose.
- O código do finalizador deve ser simples, sem chamadas que possam bloquear a thread dedicada ao finalizador.
- Se o tipo for thread-safe, o código de limpeza também precisa ser thread-safe.
