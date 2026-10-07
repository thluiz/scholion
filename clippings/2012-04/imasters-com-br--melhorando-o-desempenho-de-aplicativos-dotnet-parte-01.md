---
url: "http://imasters.com.br/artigo/24229/dotnet/melhorando-o-desempenho-de-aplicativos-net-parte-01"
captured_at: "2012-04-29T09:28:09-03:00"
title: "Melhorando o desempenho de aplicativos .NET - Parte 01"
domain: "imasters-com-br"
---

Estamos começando uma nova série de artigos que vai ser principalmente voltada para o desenvolvimento da mente dos nossos leitores. Esta nova série fornecerá detalhes de como otimizar e melhorar o desempenho de seus aplicativos do .NET. Nela, vamos discutir como abordar o desempenho em seu aplicativo, explicar as considerações de desempenho, e como construir para o desempenho durante o ciclo de vida dele.

  

Vamos organizar esta série nas seguintes seções:

  

Engenharia de aplicação e considerações de design

  

Desempenho dos aplicativos

  

Medição e ajuste de desempenho

As informações que vamos fornecer nesta série ajudarão você a desenvolver aplicativos que funcionem bem e cumpram os diversos objetivos de desempenho, tais como: tempo de resposta, throughput, utilização de CPU, utilização de memória, disco e rede de I/O. Vamos fornecer informações sobre como medir, monitorar e ajustar seu aplicativo usando a configuração adequada. Também forneceremos uma série de princípios e melhores práticas que ajudam a melhorar o desempenho.

  

#### Estabelecendo objetivos

  

É importante que você defina antecipadamente os objetivos de desempenho que incluem carga de trabalho, tempo de resposta, utilização de recursos e de throughput. Estabelecer esses objetivos iniciais ajuda no processo de tomada de decisão na fase de design do seu aplicativo, além de ajudar você a avaliar o desempenho dele.

  

Se você definir seus objetivos bem, isso te dará uma direção sobre onde se concentrar durante as fases de design e de desenvolvimento. As métricas de desempenho são usadas para medir os vários cenários do seu aplicativo e quando compará-los aos seus objetivos para determinar se as metas de desempenho são cumpridas.

  

#### Uma rápida visão de melhores práticas para desempenho em .NET

  

Vamos começar discutindo as melhores práticas para dar uma ideia dos temas que vamos discutir nesta série.

  
  

**Melhores práticas** **em design**

  

Quando você leva em consideração o desempenho, equilibre suas necessidades com atributos de outros serviços do seu aplicativo, tais como segurança e manutenção.

  

Desempenho do modelo a partir dos primeiros estágios do processo de projeto para avaliar os objetivos em relação às suas decisões de design. Isso pode economizar tempo e recursos no caminho.

  

Quando se trata de implementação do seu aplicativo, leve em consideração as políticas e os procedimentos corporativos, bem como a infraestrutura em que o aplicativo está sendo implantado. Identificar esses requisitos ajuda a selecionar a arquitetura adequada e a resolver possíveis conflitos entre seu aplicativo e a arquitetura de infraestrutura desde o início.

  

Priorize o desempenho, a manutenção e a facilidade de desenvolvimento ao selecionar uma abordagem de desenvolvimento em particular. Por exemplo, você pode usar estruturas que eliminam a necessidade de implementar sua própria serialização.O XML é ótimo para interoperabilidade e flexibilidade, no entanto, é bastante detalhado e pode exigir um esforço enorme de análise. Além disso, o XML pode ser usado para transportar grandes quantidades de dados, então use um DataReader para renderizar os dados rapidamente, mas não passe um objeto DataReader entre as camadas de aplicação.

  

Se você está projetando aplicações distribuídas, prefira uma abordagem orientada a serviços acima de uma abordagem orientada a objeto.

  

**Melhores práticas de desenvolvimento em .NET**

  

Os itens a seguir listam como melhorar o desempenho do código gerenciado.

  

Use FxCop.exe para analisar os conjuntos binários e verifique se estão em conformidade com as diretrizes de design do .NET recomendadas pela Microsoft.

  

Avalie o design das classes do seu objeto e olhe para os problemas de desempenho associados a propriedades de classe e as implicações de herança de classe.

  

Gerencie a memória de forma otimizada escrevendo código que ajude o coletor de lixo a funcionar eficientemente. Você pode fazer isso minimizando alocações ocultas, e evite a promoção de objetos de vida curta, a pré-alocação de memória, segmentação de memória, e forçando as coletas de lixo.

  

Tente evitar a criação de threads em uma base por solicitação, ou usando Thread.Abort ou Thread.Suspend.

  

Evite fazer chamadas assíncronas, se elas não adicionarem paralelismo e que bloqueiam a thread logo após iniciar a chamada. Nessas situações, não há nenhuma vantagem de usar chamadas assíncronas.

  

Limpe seus recursos assim que você terminar de usá-los. Por exemplo, use blocos de finalização em tratamento de exceções, ou use Dispose em quaisquer objetos descartáveis.

  

Tente usar StringBuilder ao criar manipulações de strings complexas e ao concatenar strings várias vezes.

Essas são algumas das melhores práticas de desenvolvimento. Vamos discuti-las em detalhes em um próximo artigo. Listaremos algumas das melhores práticas para desempenho de dados de acesso.

  
  

**Desempenho** **de dados de acesso**

  

Use o pool de conexão do banco de dados para compartilhar conexões entre diferentes solicitações.

  

Permita que o usuário navegue através dos grandes conjuntos de resultados até o último usuário, uma página por vez. DataAdapter e DataGrid são apropriados para pequenas quantidades de dados. Para um grande conjunto de resultados, use o argumento SQL SELECT TOP com o intuito de restringir o tamanho de um conjunto de resultados.

  

Tente não mover dados de grandes objetos binários repetidas vezes, mas considere armazenar indicadores nos bancos de dados para arquivar as localizações em vez dos próprios objetos binários.

  

Caso possa utilizar um objeto DataReader em vez de um objeto DataSet, faça isso, mas use DataReader apenas se precisar de acesso de somente leitura dos dados e não tiver uma solicitação para armazená-los. Use DataSet quando você precisar de mais flexibilidade ou desejar armazenar em cache dados entre diferentes pedidos.

  

Otimize consultas de longa execução utilizando o profiler do SQL e, para identificar a causa da consulta de longa duração, use o analyzer do SQL.

  

**Melhorando o desempenho do ASP.NET**

  

Otimize suas páginas da web aparando o tamanho de cada página e reduzindo o número de gráficos. Desabilite o estado de exibição para páginas que não requerem isso. Certifique-se de que o buffer está ativado para reduzir a comunicação entre cliente e servidor.

  

Sintonize o seu thread pool do ASP.NET. Iremos fornecer detalhes sobre isso em um próximo artigo.

  

Utilize a API Cache para armazenar seus dados, tanto usando o cache de saída ou por cache de fragmento de página. Para fazer isso de forma eficaz, separe as áreas estática e dinâmica de suas páginas e controles de usuário.

  

Desabilite o estado da sessão caso não precise dele. Se precisar, escolha o método apropriado na in-process store, os out-of-process state servers, ou um servidor SQL Analyzer. Geralmente, a in-process store oferece o melhor desempenho. Use o atributo ReadOnly em páginas que só leem o estado da sessão.

  

**Melhorando o desempenho remoto do .NET**

  

Se você usar o remoto, reduza o número de ida e volta da comunicação usando a interface volumosa.

  

Serialize apenas os dados de que você precisa para melhorar o desempenho de serialização usando o atributo NonSerialized, impedindo que campos desnecessários sejam serializados.

Use os métodos a seguir para melhorar a eficiência de serialização: use um aliase de nome de coluna para reduzir o tamanho dos nomes das colunas; evite serializar os valores originais e novos para o campo DataSet se não for necessário; e apenas serialize as instâncias DataTable que você precisa.

  

**Melhorando o desempenho de interoperabilidade**

  

Para reduzir os custos de empacotamento, considere a quantidade o tipo de dado que você transmite para e a partir de código não gerenciado.

  

Evite empacotamento desnecessário utilizando os atributos explícitos de entrada e saída.

  

Você pode minimizar a fragmentação da pilha não fixando objetos mais do que a duração de uma chamada P/Invoke. Se você tiver um aplicativo de servidor bastante sobrecarregado, considere chamar a função Marshal.ReleaseComObject para certificar-se de que os objetos COM sejam liberados em tempo hábil.

Como você pode ver, há uma série de itens a serem levados em consideração se você quer melhorar o desempenho do seu aplicativo. NET. Ao longo das próximas semanas, iremos aprofundar os temas que abordamos nesta introdução.

  

⁂  
*Texto original da equipe Monitis, liderada por Hovhannes Avoyan, disponível em <http://blog.monitis.com/index.php/2012/02/22/improving-net-application-performance/>*

  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](imasters-com-br--melhorando-o-desempenho-de-aplicativos-dotnet-parte-01/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Melhorando+o+desempenho+de+aplicativos+.NET+-+Parte+01&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24229%2Fdotnet%2Fmelhorando-o-desempenho-de-aplicativos-net-parte-01)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](imasters-com-br--melhorando-o-desempenho-de-aplicativos-dotnet-parte-01/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Melhorando+o+desempenho+de+aplicativos+.NET+-+Parte+01&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24229%2Fdotnet%2Fmelhorando-o-desempenho-de-aplicativos-net-parte-01)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/132733359394/u/49/f/546640/c/33212/s/1ed60daa/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
  
from iMasters - <http://feedproxy.google.com/~r/imasters/~3/Vh0a_ttu-_0/story01.htm>
