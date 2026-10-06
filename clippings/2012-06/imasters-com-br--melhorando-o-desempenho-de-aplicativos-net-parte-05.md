---
url: "https://imasters.com.br/dotnet/melhorando-o-desempenho-de-aplicativos-net-parte-05"
captured_at: "2012-06-18T11:18:27-03:00"
title: "Melhorando o desempenho de aplicativos .NET - Parte 05"
domain: "imasters-com-br"
---

Em nosso [último artigo](http://imasters.com.br/artigo/24621/dotnet/melhorando-o-desempenho-do-aplicativo-net-parte-04), discutimos algumas diretrizes para otimizar o coletor de lixo. Ele oferece dois métodos adicionais: Finalize e Dispose. Vamos discutir as diretrizes para esses métodos neste artigo.

  

#### Finalize

  

Alguns objetos requerem limpeza adicional porque utilizam recursos não gerenciados que precisam ser liberados. Isso é tratado por finalização. Um objeto registra por finalização, substituindo o método Object.Finalize.

  

O método Finalize de um objeto é chamado antes que a memória gerenciada do objeto seja recuperada. Isso lhe permite liberar todos os recursos não gerenciados que são mantidos pelo objeto. Implementando o Finalize, você não poderá controlar quando esse método deve ser chamado, pois isso será deixado para o coletor de lixo.

  

O processo de finalização requer um mínimo de dois ciclos de coleta para liberar totalmente a memória do objeto. Durante a primeira coleção, o objeto é marcado para finalização. A finalização é executada em uma thread especializada que é independente do coletor de lixo. Depois que a finalização ocorre, o coletor de lixo pode recuperar a memória do objeto.

  

Tenha em mente de que não há nenhuma garantia em relação ao tempo ou à ordem de coleção de objetos. Além disso, recursos de memória podem consumir uma grande quantidade de tempo antes de serem pegos pelo coletor de lixo.

  

Em C #, implemente Finalize usando a sintaxe destructor.

  

```
 class yourObject {  
   
  // This is a finalizer implementation  
   
  ~yourObject() {  
   
  // Release your unmanaged resources here  
   
  . . .  
   
  }  
   
 }
```

  

A sintaxe anterior faz com que o compilador gere o código a seguir:

  

```
 class yourObject {  
   
  protected override void Finalize() {  
   
  try{  
   
  . . .  
   
  }  
   
  finally {  
   
  base.Finalize();  
   
  }  
   
 }
```

  

#### Dispose

  

Para os tipos que contêm referências para recursos externos que precisam ser explicitamente liberados pelo código de chamada, você usaria o método Dispose. Você pode evitar a finalização ao implementar a interface IDisposable e permitir que os consumidores de sua classe chamem Dispose.

  

Tente evitar a finalização, porque ela é tratada de forma assíncrona e, recursos não gerenciados podem não ser liberados em tempo hábil. Isso é especialmente importante para os recursos grandes e dispendiosos não gerenciados, como bitmaps ou conexões de banco de dados. Com essa abordagem, os recursos são recuperados logo que o Dispose é chamado, e o objeto não tem que estar na fila para a finalização. Você quer ver quase todos os seus objetos finalizáveis sendo eliminados, e não finalizados.

  

Para evitar que o coletor de lixo solicite a finalização, sua implementação Dispose deve chamar GC.SuppressFinalization.

  
  

**Close**

  

Para determinadas classes de objetos, tais como arquivos ou objetos de conexão de banco de dados, um método Close representa melhor a operação lógica que deve ser realizada quando o consumidor do objeto é concluído com o objeto. Como resultado, vários objetos expõem um método Close além de um método Dispose. Em casos bem escritos, ambos são funcionalmente equivalentes.

  
  

**Padrão Dispose**

  

Para implementar o padrão Dispose, faça o seguinte:

  

Crie uma classe que derive de IDisposable.

  

Adicione uma variável de membro privado para controlar se IDisposable.Dispose já foi chamado. Os clientes devem ser autorizados a chamar o método várias vezes sem gerar uma exceção. Se um outro método na classe é chamado depois de uma chamada de Dispose, você deve lançar um ObjectDisposedException.

  

Implemente um override protected void virtual do método Dispose que aceite um único parâmetro booleano. Esse método contém o código de limpeza comum que é chamado também quando o cliente explicitamente chama IDisposable.Dispose ou quando o finalizador é executado. O parâmetro booleano é usado para indicar se a limpeza está sendo realizada como um resultado de uma chamada de cliente para IDisposable.Dispose ou como um resultado de finalização.

  

Implemente o método IDisposable.Dispose que não aceita parâmetros. Esse método é chamado pelos clientes para forçar explicitamente a liberação de recursos. Verifique se Dispose foi chamado antes; caso não tiver sido, chame Dispose(true) e então evite a finalização chamando GC.SuppressFinalize(this). A finalização não é mais necessária porque o cliente forçou explicitamente uma liberação de recursos.

  

Crie um finalizador, usando a sintaxe destruidor. No finalizador, chame Dispose(false).

**Exemplo de Dispose** **em C#**

  

O código deve ser semelhante ao seguinte.

  

```
 public sealed class MyClass: IDisposable  
   
 {  
   
  // Variable to track if Dispose has been called  
   
  private bool disposed = false;  
   
  // Implement the IDisposable.Dispose() method  
   
  public void Dispose(){  
   
  // Check if Dispose has already been called  
   
  if (!disposed)  
   
  {  
   
  // Call the overridden Dispose method that contains common cleanup code  
   
  // Pass true to indicate that it is called from Dispose  
   
  Dispose(true);  
   
  // Prevent subsequent finalization of this object. This is not needed  
   
  // because managed and unmanaged resources have been explicitly released  
   
  GC.SuppressFinalize(this);  
   
  }  
   
  }  
   
   
   
  // Implement a finalizer by using destructor style syntax  
   
  ~MyClass() {  
   
  // Call the overridden Dispose method that contains common cleanup code  
   
  // Pass false to indicate the it is not called from Dispose  
   
  Dispose(false);  
   
  }  
   
   
   
  // Implement the override Dispose method that will contain common  
   
  // cleanup functionality  
   
  protected virtual void Dispose(bool disposing){  
   
  if(disposing){  
   
  // Dispose time code  
   
  . . .  
   
  }  
   
  // Finalize time code  
   
  . . .  
   
  }  
   
  …}
```

  

Passar true ao método Dispose protegido garante que o código específico dispose seja chamado. Passar false pula o código Dispose específico. O método Dispose(bool) pode ser chamado diretamente por sua classe ou indiretamente pelo cliente.

  

Se você fizer referência a quaisquer variáveis estáticas ou métodos em seu código finalize-time Dispose, certifique-se de verificar a propriedade Environment.HasShutdownStarted. Se o objeto estiver seguro, certifique-se de fazer quaisquer bloqueios que forem necessários para a limpeza.

  

Use a propriedade HasShutdownStarted no método Dispose de um objeto para determinar se o CLR está sendo desligado ou se o domínio de aplicativo está descarregando. Se for esse o caso, você não pode acessar com confiança qualquer objeto que tem um método de finalização e for referenciado por um campo estático.

  

```
 protected virtual void Dispose(bool disposing){  
   
  if(disposing){  
   
  // dispose-time code  
   
  . . .  
   
  }  
   
  // finalize-time code  
   
  CloseHandle();  
   
   
   
  if(!Environment.HasShutDownStarted)  
   
  { //Debug.Write or Trace.Write – static methods  
   
  Debug.WriteLine(“Finalizer Called”);  
   
  }  
   
  disposed = true;  
   
 }
```

  

#### Diretrizes de Finalize e Dispose

  

Vamos resumir as recomendações para Finalize e Dispose

  

**Chame Close ou Dispose em classes que os apoiam** - Se a classe gerenciada que você usa implementa Close ou Dispose, chame um desses métodos logo que você terminar com o objeto.

  

**Objetos COM** - Em cenários de servidor em que você cria e destrói objetos em uma base por solicitação, você pode precisar chamar System.Runtime.InteropServices.Marshal.ReleaseComObject. O Runtime Callable Wrapper (RCW) usa uma contagem de referência que é incrementada cada vez que um ponteiro de interface COM é mapeado para ele. O método ReleaseComObject diminui esse contador e, quando ele atinge o zero, o tempo de execução libera todas as suas referências sobre o objeto COM não gerenciado.

  

**Enterprise Services (COM+)** - Não é recomendável compartilhar os componentes de serviço ou objetos COM ou COM+ nos casos em que os objetos são criados em um contexto "não padrão", ou porque o componente é um componente de serviço configurado no COM+, ou porque o componente é um simples componente COM que é colocado em um contexto "não padrão" em virtude do seu cliente. Por exemplo, os clientes tais como páginas em ASP.NET rodando em uma transação ou modo ASPCompat sempre estão localizadas dentro de um contexto COM+. Se o seu cliente for um componente de serviço em si, a mesma regra se aplica.

  

Atravessar uma fronteira de contexto COM + é caro. Esse problema é aumentado se o seu contexto COM+ no lado do cliente tiver afinidade de thread por estar localizado dentro de um STA. Em tese, ative seu componente, trabalhar com ele, e depois libere-o imediatamente. Quando você usa Enterprise Services e classes que derivam de System.EnterpriseServices.ServicedComponent, você precisa chamar Dispose nessas classes.

  

Se o componente que você chamar for um componente COM+ não gerenciado, chame Marshal.ReleaseComObject.

  

**A instrução using em C#** - A instrução using gera automaticamente um try e depois um block no tempo de compilação que chama Dispose no objeto alocado dentro do bloco using. O código a seguir ilustra essa sintaxe.

  

```
 using( StreamReader myFile = new StreamReader(“C:\\ReadMe.Txt”)){  
   
  string contents = myFile.ReadToEnd();  
   
  //… use the contents of the file  
   
   
   
 } // dispose is called and the StreamReader’s resources released  
   
 During compilation, the preceding code is converted into the following equivalent code.  
   
 StreamReader myFile = new StreamReader(“C:\\ReadMe.Txt”);  
   
 try{  
   
  string contents = myFile.ReadToEnd();  
   
  //… use the contents of the file  
   
 }  
   
 finally{  
   
  myFile.Dispose();  
   
 }
```

  

**Não implemente Finalize a não ser que seja exigido** - Evite implementar um finalizador ou um destructor, a menos que a finalização seja necessária. Implementar um finalizador em classes que não o exigem acrescenta carga à thread do finalizador e ao coletor de lixo.

  

**Implemente Finalize somente se você mantiver recursos não gerenciados através de chamadas de clientes** - Use um finalizador apenas em objetos que detêm recursos não gerenciados por meio de chamadas de clientes. Por exemplo, se o objeto possui apenas um método chamado GetData que abre uma conexão, obtém dados de um recurso não gerenciado, fecha a conexão e retorna os dados, não há necessidade de implementar um finalizador. No entanto, se seu objeto também expõe um método Open, no qual uma conexão para um recurso não gerenciado é feita e, em seguida, os dados são obtidos usando um método GetData separado, é possível para a conexão ser mantida para o recurso não gerenciado entre as chamadas. Nesse caso, você deve fornecer um método Finalize para limpar a conexão com o recurso não gerenciado e utilizar o padrão Dispose para dar ao cliente a capacidade de liberar o recurso explicitamente depois de terminado.

  

**Mova a carga de finalização para as folhas de gráficos de objetos** - Se você tem um objeto gráfico com um objeto referenciando outros objetos (folhas) que detêm recursos não gerenciados, você deve implementar os finalizadores nos objetos folha em vez de no objeto raiz. Mover a carga de finalização com os resultados dos objetos folhas  na promoção de apenas os mais relevantes para a fila de finalização, o que ajuda a otimizar o processo de finalização.

  

**Se você implementar Finalize, implemente IDisposable** - Implemente IDisposable se implementar um finalizador. Dessa forma, o código de chamada tem uma forma explícita de recursos livres ao chamar o método Dispose. Você deve ainda implementar um finalizador com Dispose porque você não pode assumir que o código de chamada sempre chama Dispose. Apesar de esse ser um método caro, a implementação do finalizador garante que os recursos sejam liberados.

  

**Se você implementar Finalize e Dispose, use o padrão Dispose** - Se você implementar Finalize e Dispose, use o padrão Dispose, como descrito anteriormente.

  

**Impeça finalização em seu método Dispose** - Se o código de chamada chamar Dispose, você não vai querer que o coletor de lixo chame um finalizador, pois os recursos não gerenciados já terão sido devolvidos ao sistema operacional. Você deve impedir que o coletor de lixo chame o finalizador usando GC.SuppressFinalization em seu método Dispose.

  

```
 public void Dispose()  
   
 {  
   
  // Using the dispose pattern  
   
  Dispose(true);  
   
  // … release unmanaged resources here  
   
  GC.SuppressFinalize(this);  
   
 }
```

  

**Permita que Dispose seja chamado várias vezes** - O código de chamada deve ser capaz de chamar Dispose com segurança várias vezes, sem causar exceções. Após a primeira chamada, outras subsequentes não deverão fazer nada e não lançar uma ObjectDisposedException para chamadas subsequentes.

  

```
 public class BusinessBase : IDisposable{  
   
  public void Dispose() {…}  
   
  protected virtual void Dispose(bool disposing) {}  
   
  ~BusinessBase() {…}  
   
 }  
   
   
   
 public class Customer : BusinessBase, IDisposable{  
   
 private bool disposed = false;  
   
   
   
  protected virtual void Dispose(bool disposing) {  
   
  // Check before calling your Dispose pattern  
   
  if (!disposed){  
   
  if (disposing) {  
   
  // free managed objects  
   
  }  
   
  // free unmanaged objects  
   
  base.Dispose(disposing);  
   
  disposed = true;  
   
  }  
   
  }
```

  

**Mantenha o código do finalizador simples para evitar bloqueio** - O código do finalizador deve ser simples e mínimo. A finalização acontece em uma única thread do finalizador dedicado. Não emita as chamadas que podem bloquear a thread de chamada. Se o finalizador bloqueia, os recursos não são liberados e o aplicativo perde. Além disso, não use o armazenamento local de thread ou qualquer outra técnica que exige afinidade de thread, porque o método do finalizador é chamado por uma thread dedicada, separada da thread principal do aplicativo.

  

**Forneça código de limpeza thread de segurança somente se o seu tipo for thread-safe** - Se seu tipo for thread safe, verifique se o código de limpeza também é thread-safe. Por exemplo, se o seu tipo de thread-safe fornece ambos os métodos Close e Dispose para limpar recursos, garanta que você sincronize threads chamando Close e Dispose simultaneamente.

  

Isso é tudo para as orientações sobre coletor de lixo. No próximo artigo, vamos começar a discutir threading.

  

*⁂*

  

*Texto original da equipe Monitis, liderada por Hovhannes Avoyan, disponível em:* *<http://blog.monitis.com/index.php/2012/04/16/improving-net-application-performance-part-5-finalize-and-dispose/>*

  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](imasters-com-br--melhorando-o-desempenho-de-aplicativos-net-parte-05/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Melhorando+o+desempenho+de+aplicativos+.NET+-+Parte+05&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24695%2Fdotnet%2Fmelhorando-o-desempenho-de-aplicativos-net-parte-05)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](imasters-com-br--melhorando-o-desempenho-de-aplicativos-net-parte-05/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Melhorando+o+desempenho+de+aplicativos+.NET+-+Parte+05&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24695%2Fdotnet%2Fmelhorando-o-desempenho-de-aplicativos-net-parte-05)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/137428621570/u/49/f/546640/c/33212/s/2077c4b7/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
from iMasters - <http://feedproxy.google.com/~r/imasters/~3/qJR15Iy_PDU/story01.htm>
