---
url: "http://imasters.com.br/artigo/24960/dotnet/melhorando-o-desempenho-de-aplicativos-net-parte-07"
captured_at: "2012-07-09T11:03:46-03:00"
title: "Melhorando o desempenho de aplicativos .NET - Parte 07"
domain: "imasters-com-br"
---

Em nosso [último artigo](http://imasters.com.br/artigo/24817/dotnet/melhorando-o-desempenho-de-aplicativos-net-parte-06), nós discutimos diretrizes para a otimização de threads. Neste artigo veremos as melhores práticas para a utilização de chamadas assíncronas. Quando você chama um método de forma assíncrona, eles não interrompem a execução. A chamada de threads retorna imediatamente e continua a execução do método atual.

  

#### Melhores práticas assíncronas

  

Esta seção resume as melhores práticas para otimizar o desempenho ao utilizar execução assíncrona:

  

Considere chamadas assíncronas do lado do cliente para receptividade UI

Você pode usar chamadas assíncronas para aumentar a capacidade de resposta dos aplicativos do cliente. No entanto, pense nisso com cuidado, pois chamadas assíncronas introduzem uma complexidade adicional de programação e lógica de sincronização e requer cuidado para ser adicionada ao seu código de interface gráfica.

  

O código a seguir mostra uma chamada assíncrona seguida por um loop que pesquisa para a conclusão da chamada assíncrona. Você pode adicionar um critério de saída para a condição "while", no caso de você precisar sair da função antes que a chamada seja concluída. Você pode usar o mecanismo de retorno de chamada ou aguardar a conclusão se não precisar atualizar o cliente.

  

```
 IAsyncResult CallResult = SlowCall.BeginInvoke(slow,null,null);  
 while ( CallResult.IsCompleted == false)  
 {   
  … // provide user feedback   
 }  
 SlowCall.EndInvoke(CallResult);
```

  

Use métodos assíncronos no servidor de E/S nas operações vinculadas

Você pode aumentar o desempenho do seu aplicativo executando várias operações ao mesmo tempo. As duas operações não são dependentes uma da outra. Por exemplo, o código a seguir chama dois serviços da web. A duração do código é a soma de ambos os métodos.

  

```
 // get a reference to the proxy  
 EmployeeService employeeProxy = new EmployeeService();  
   
 // execute first and block until complete  
 employeeProxy.CalculateFederalTaxes(employee, null, null);  
   
 // execute second and block until complete  
 employeeProxy.CalculateStateTaxes(employee);
```

  

Você pode refatorar o código da seguinte maneira para reduzir a duração total da operação. No seguinte código, ambos os métodos executam simultaneamente, o que reduz a duração global da operação. Note que o exemplo a seguir usa o método BeginCalculateFederalTaxes, uma versão assíncrona do CalculateFederalTaxes; ambos os métodos são gerados automaticamente quando você faz referência a um serviço web a partir do aplicativo do seu cliente na Visual Studio .NET.

  

```
 // get a reference to the proxy  
 EmployeeService employeeProxy = new EmployeeService();  
   
 // start async call, BeginCalculateFederalTaxes  
 // call returns immediately allowing local execution to continue  
 IAsyncResult ar = employeeProxy.BeginCalculateFederalTaxes(employee, null, null);  
   
 // execute CalculateStateTaxes synchronously  
 employeeProxy.CalculateStateTaxes(employee);  
   
 // wait for the CalculateFederalTaxes call to finish  
 employeeProxy.EndCalculateFederalTaxes(ar);
```

  

Evite chamadas assíncronas que não agregam paralelismo

Evite chamadas assíncronas que irão bloquear vários threads para a mesma operação. O código a seguir mostra uma chamada assíncrona para um serviço web. A chamada do código bloqueia enquanto espera que a chamada de serviço web para ser concluída. Observe que o código de chamada não executa nenhum trabalho adicional enquanto a chamada assíncrona está em execução.

  

```
 // get a proxy to the Web service  
 customerService serviceProxy = new customerService ();  
   
 //start async call to CustomerUpdate   
 IAsyncResult result = serviceProxy.BeginCustomerUpdate(null,null);   
   
 // Tasks that can be done in parallel should appear here but is absent here  
   
 // wait for the asynchronous operation to complete  
 // Client is blocked until call is done  
 result.AsyncWaitHandle.WaitOne();  
 serviceProxy.EndCustomerUpdate(result);
```

  

Quando um código como este é executado em um aplicativo de servidor - como um aplicativo ASP.NET ou serviço web, que utiliza dois threads para fazer uma tarefa e não oferece nenhum benefício -, na verdade, atrasa outros pedidos a serem processados. Você deve evitar esta prática.

  

No próximo artigo da série .NET iremos discutir melhores práticas e diretrizes de bloqueio.

  

 \*\*\*

  

Artigo original disponível em: <http://blog.monitis.com/index.php/2012/04/20/improving-net-application-performance-part-7-asynchronous-calls/>

  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](imasters-com-br--melhorando-o-desempenho-de-aplicativos-net-parte-07/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Melhorando+o+desempenho+de+aplicativos+.NET+-+Parte+07&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24960%2Fdotnet%2Fmelhorando-o-desempenho-de-aplicativos-net-parte-07)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](imasters-com-br--melhorando-o-desempenho-de-aplicativos-net-parte-07/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Melhorando+o+desempenho+de+aplicativos+.NET+-+Parte+07&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24960%2Fdotnet%2Fmelhorando-o-desempenho-de-aplicativos-net-parte-07)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/139261997465/u/49/f/546640/c/33212/s/21294522/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
from iMasters - <http://da.feedsportal.com/c/33212/f/546640/s/21294522/l/0Limasters0N0Bbr0Cartigo0C24960A0Cdotnet0Cmelhorando0Eo0Edesempenho0Ede0Eaplicativos0Enet0Eparte0E0A7/ia1.htm>
