---
title: "Melhorando o desempenho de aplicativos .NET - Parte 07"
date: '2012-07-09T11:03:46-03:00'
category: webclip
summary: 'O texto reúne práticas para usar chamadas assíncronas em .NET, destacando quando elas ajudam na responsividade do cliente ou no paralelismo no servidor, e quando só acrescentam bloqueio e complexidade.'
tags: ["dotnet", "async", "performance"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Melhorando o desempenho de aplicativos .NET - Parte 07"
    url: "http://imasters.com.br/artigo/24960/dotnet/melhorando-o-desempenho-de-aplicativos-net-parte-07"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-07/imasters-com-br--melhorando-o-desempenho-de-aplicativos-net-parte-07.md"
    kind: repo
---

O texto apresenta melhores práticas para chamadas assíncronas em aplicativos .NET. Ele diz que esse tipo de execução retorna imediatamente, pode melhorar a responsividade da interface do cliente e pode reduzir o tempo total quando duas operações independentes rodam ao mesmo tempo.

Também alerta para usos que não trazem ganho real. Se a chamada assíncrona só ocupa threads sem permitir trabalho paralelo, ela bloqueia recursos e, em servidores como ASP.NET ou serviços web, pode atrasar o processamento de outras requisições.

## Fichamento

- Chamadas assíncronas retornam imediatamente e deixam a execução do método atual continuar.
- No cliente, elas podem aumentar a responsividade da interface, mas adicionam complexidade de programação e de sincronização.
- Um loop pode verificar a conclusão da chamada assíncrona e, se necessário, o código pode usar retorno de chamada ou aguardar o término.
- No servidor, chamadas assíncronas ajudam quando há duas operações independentes que podem rodar ao mesmo tempo.
- O exemplo com dois serviços web mostra que iniciar uma chamada assíncrona e executar a outra operação em paralelo reduz a duração total.
- Deve-se evitar chamadas assíncronas que não criam paralelismo, porque elas bloqueiam threads sem trazer benefício.
- Em aplicativos de servidor, esse padrão usa dois threads para uma tarefa e pode atrasar outras requisições.
