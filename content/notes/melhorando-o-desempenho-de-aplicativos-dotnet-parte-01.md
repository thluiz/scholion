---
title: "Melhorando o desempenho de aplicativos .NET - Parte 01"
date: '2012-04-29T09:28:09-03:00'
category: webclip
summary: 'A abertura da série define objetivos de desempenho e reúne práticas para projeto, desenvolvimento, acesso a dados, ASP.NET, remoting e interoperabilidade em aplicativos .NET.'
tags: ["dotnet", "desempenho", "aspnet", "acesso-a-dados"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Melhorando o desempenho de aplicativos .NET - Parte 01"
    url: "http://imasters.com.br/artigo/24229/dotnet/melhorando-o-desempenho-de-aplicativos-net-parte-01"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-04/imasters-com-br--melhorando-o-desempenho-de-aplicativos-dotnet-parte-01.md"
    kind: repo
---

A página abre uma série sobre como otimizar aplicativos .NET. O foco é combinar objetivos de desempenho com decisões de projeto, desenvolvimento, acesso a dados, ASP.NET, remoting e interoperabilidade, usando métricas, monitoramento e ajuste ao longo do ciclo de vida do aplicativo.

## Fichamento

- A série quer tratar de como abordar desempenho em aplicativos .NET e como construir para desempenho durante o ciclo de vida.
- Os temas da série são engenharia de aplicação e design, desempenho de aplicativos, medição e ajuste de desempenho.
- Os objetivos de desempenho devem ser definidos antes, incluindo carga de trabalho, tempo de resposta, uso de recursos e throughput.
- Esses objetivos orientam decisões de design e ajudam a avaliar se as metas de desempenho foram cumpridas.
- No design, o desempenho precisa ser equilibrado com segurança e manutenção.
- O desempenho deve ser considerado desde os primeiros estágios do projeto para comparar objetivos e decisões de design.
- Na implementação, é preciso considerar políticas corporativas e a infraestrutura de destino para escolher a arquitetura adequada.
- Em aplicações distribuídas, a página recomenda preferir uma abordagem orientada a serviços em vez de orientada a objeto.
- Entre as práticas para código gerenciado, o texto cita o uso de FxCop.exe para verificar conformidade com diretrizes da Microsoft.
- Também recomenda avaliar propriedades, herança, alocação de memória, criação de threads, chamadas assíncronas que não trazem paralelismo, limpeza de recursos e uso de StringBuilder.
- Para acesso a dados, a página sugere pool de conexões, paginação de grandes resultados, uso de SELECT TOP quando necessário e cuidado ao mover objetos binários grandes.
- O texto orienta usar DataReader quando bastar acesso somente leitura, e DataSet quando for preciso mais flexibilidade ou cache entre pedidos.
- Para consultas longas, a página recomenda profiler e analyzer do SQL.
- Em ASP.NET, a orientação é reduzir o tamanho das páginas, diminuir o número de gráficos, desabilitar view state quando possível e manter o buffer ativado.
- O texto também recomenda usar cache, separar partes estáticas e dinâmicas, desabilitar session state quando não for necessário e usar ReadOnly em páginas que só leem a sessão.
- Para remoting, a página sugere reduzir idas e voltas, serializar apenas o necessário e evitar serializar dados desnecessários em DataSet e DataTable.
- Em interoperabilidade, o texto recomenda reduzir custos de empacotamento, evitar empacotamento desnecessário, limitar fixação de objetos e liberar COM objects em tempo hábil.
