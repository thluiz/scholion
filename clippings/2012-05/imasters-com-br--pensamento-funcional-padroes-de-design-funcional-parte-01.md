---
url: "https://imasters.com.br/back-end/pensamento-funcional-padroes-de-design-funcional-parte-01"
captured_at: "2012-05-08T10:27:59-03:00"
title: "Pensamento funcional: padrões de design funcional - Parte 01"
domain: "imasters-com-br"
---

Algumas pessoas no mundo funcional afirmam que o conceito de padrão de design é defeituoso e que ele não é necessário na programação funcional. É possível defender essa visão com uma definição estreita de *padrão* - mas isso é mais uma questão de semântica que de uso. A *conceito* de padrão de design - uma solução nomeada e catalogada para um problema comum - está bem vivo. No entanto, os padrões às vezes têm aparências diferentes dependendo do paradigma. Como os blocos de criação e as abordagens aos problemas são diferentes no mundo funcional, alguns dos padrões Gang of Four tradicionais (consulte "Recursos") desaparecem, enquanto outros preservam o problema mas o resolvem de forma radicalmente diferente. Esta edição e a próxima investigam os padrões de design tradicionais e os repensam de uma maneira funcional.

  

No mundo da programação funcional, os padrões de design tradicionais se manifestam geralmente em uma destas três maneiras:

  

O padrão é absorvido pela linguagem;

  

A solução do padrão ainda existe no paradigma funcional, mas os detalhes da implementação são diferentes;

  

A solução é implementada usando recursos que outras linguagens ou paradigmas não possuem. Por exemplo, muitas soluções que usam metaprogramação são limpas e elegantes - e não são possíveis em Java.

Eu investigarei esses três casos um por vez, começando nesta edição com alguns padrões familiares, a maioria dos quais são incluídos total ou parcialmente pelas linguagens modernas.

  

#### Factories e currying

  

Currying é um recurso de muitas linguagens funcionais. O currying, que recebeu seu nome em homenagem ao matemático Haskell Curry (a linguagem de programação Haskell também recebeu seu nome em homenagem a ele), transforma uma função multiargumentos para que possa ser chamada como uma cadeia de funções de argumento único. Intimamente relacionada é a técnica de aplicação parcial, que designa um valor fixo a um ou mais argumentos de uma função, produzindo assim outra função de aridade (aridade é o número de parâmetros para a função).

  

No contexto dos padrões de design, currying funciona como um factory para funções. Um recurso comum nas linguagens de programação funcionais são funções de primeira classe (ou de ordem superior), que possibilita que as funções ajam como qualquer outra estrutura de dados. Graças a esse recurso, é possível criar facilmente funções que retornam outras funções com base em algum critério, o que é a essência de um factory. Por exemplo, se temos uma função geral que adiciona dois números, é possível usar currying como um factory para criar uma função que sempre adiciona um a seu parâmetro - um incrementador, como mostrado na Listagem 1, implementado em Groovy:

  

```
 def adder = { x, y -> return x + y }  
   
 def incrementer = adder.curry(1)  
   
   
 println "increment 7: ${incrementer(7)}" // prints "increment 7: 8"
```

  

*Listagem 1. Currying como um factory de função*.

  

Nessa Listagem 1, eu realizei currying do primeiro parâmetro como 1, retornando uma função que aceita um único parâmetro. Basicamente eu criei um factory de função.

  

Quando a linguagem suporta esse tipo de comportamento de forma nativa, isso tende a ser usado como um bloco de criação para outras coisas, grandes e pequenas. Por exemplo, considere o exemplo de Scala mostrado na Listagem 2:

  

```
 object CurryTest extends Application {  
   
   
  def filter(xs: List[Int], p: Int => Boolean): List[Int] =  
   
  if (xs.isEmpty) xs  
   
  else if (p(xs.head)) xs.head :: filter(xs.tail, p)  
   
  else filter(xs.tail, p)  
   
   
  def dividesBy(n: Int)(x: Int) = ((x % n) == 0)  
   
   
  val nums = List(1, 2, 3, 4, 5, 6, 7, 8)  
   
  println(filter(nums, dividesBy(2)))  
   
  println(filter(nums, dividesBy(3)))  
   
 }
```

  

*Listagem 2. O uso "casual" de currying pelo Scala*.

  

O código na Listagem 2 é um dos exemplos de recursão e de currying na documentação do Scala (consulte "Recursos"). O método filter() filtra recursivamente uma lista de números inteiros por meio do parâmetro p. p é *uma função de predicado,* - termo comum no mundo funcional para uma função booleana. O método filter() verifica se a lista está vazia e, caso ela esteja, ele simplesmente a devolve; caso contrário, verifica o primeiro elemento na lista (xs.head) por meio do predicado para ver se deve ser incluído na lista filtrada. Se passar pelo predicado, o método retorna uma nova lista com o início na frente e o final filtrado como resto. Se o primeiro elemento falhar no teste de predicação, o retorno se torna apenas o resto filtrado da lista.

  

O que há de interessante na Listagem 2 do ponto de vista dos padrões é o uso "casual" de currying no método dividesBy(). Observe que dividesBy() aceita dois parâmetros e devolve true ou false, dependendo se o segundo parâmetro divide o primeiro sem resto. Entretanto, quando esse método é chamado como parte da chamada do método filter(), ele é chamado somente com um parâmetro, - sendo seu resultado uma função com currying usada como o predicado no método filter().

  

Esse exemplo ilustra uma de duas maneiras pelas quais os padrões se manifestam na programação funciona, como eu listei no começo deste artigo. Primeiro, o currying está integrado na linguagem ou no tempo de execução, portanto o conceito de um factory de função está entranhado e não precisa de uma estrutura extra. Segundo, isso ilustra meu argumento sobre implementações diferentes. Usar currying como na Listagem 2 provavelmente nunca ocorreria a um programador Java típico; nunca tivemos realmente código móvel e certamente nunca pensamos em construir funções específicas a partir de funções gerais. De fato, é possível que a maioria dos desenvolvedores autoritários não pensaria em usar um padrão de design aqui, pois a criação de um método dividesBy() específico a partir de um método geral parece ser um problema pequeno, considerando que os padrões de design - que contam principalmente com a estrutura para solucionar problemas e, portanto, exigem um grande gasto adicional para implementar - parecem ser soluções para problemas maiores. Usar currying da maneira para o qual foi criado não justifica a formalidade de um nome especial além do que ele já tem.

  

#### Funções de primeira classe e padrões de design

  

Usar funções de primeira classe simplifica enormemente muitos padrões de design frequentes. O padrão de design Command até desaparece, pois não é mais necessário um wrapper de objeto para funcionalidade móvel.

  

**Método Template**

  

As funções de primeira classe tornam o padrão de design do Método Template (consulte "Recursos") mais simples de implementar, pois removem a estrutura possivelmente desnecessária. O Método Template define o esqueleto de um algoritmo em um método, delegando algumas etapas a subclasses e forçando-as a definir essas etapas sem alterar a estrutura do algoritmo. Uma implementação típica do Método Template pode ser vista na Listagem 3, em Groovy:

  

```
 abstract class Customer {  
   
  def plan  
   
   
  def Customer() {  
   
  plan = []  
   
  }  
   
   
  def abstract checkCredit()  
   
  def abstract checkInventory()  
   
  def abstract ship()  
   
   
  def process() {  
   
  checkCredit()  
   
  checkInventory()  
   
  ship()  
   
  }  
   
 }
```

  

*Listagem 3. Implementação "padrão" do Método Template.*

  

Na Listagem 3, o método process() conta com os métodos checkCredit(), checkInventory()e ship(), cujas definições devem ser fornecidas por subclasses, pois são métodos abstratos.

  

Como as funções de primeira classe podem agir como qualquer outra estrutura de dados, é possível redefinir o exemplo na a Listagem 3 usando blocos de código, como mostra a Listagem 4:

  

```
 class CustomerBlocks {  
   
  def plan, checkCredit, checkInventory, ship  
   
   
  def CustomerBlocks() {  
   
  plan = []  
   
  }  
   
   
  def process() {  
   
  checkCredit()  
   
  checkInventory()  
   
  ship()  
   
  }  
   
 }  
   
   
 class UsCustomerBlocks extends CustomerBlocks{  
   
  def UsCustomerBlocks() {  
   
  checkCredit = { plan.add "checking US customer credit" }  
   
  checkInventory = { plan.add "checking US warehouses" }  
   
  ship = { plan.add "Shipping to US address" }  
   
  }  
   
 }
```

  

*Listagem 4. Template Method com funções de primeira classe.*

  

Nessa Listagem 4, as etapas no algoritmo são apenas as propriedades da classe, que podem ser atribuídas como qualquer outra propriedade. Esse é um exemplo no qual o recurso da linguagem absorve na maior parte os detalhes da implementação. Ainda é útil falar desse padrão como uma solução para um problema (delegar etapas a manipuladores posteriores), mas a implementação é mais simples.

  

As duas soluções não são equivalentes. No exemplo "tradicional" de Método Template na Listagem 3, a classe abstrata requer subclasses para implementar os métodos dependentes. Claro, a subclasse pode simplesmente criar um corpo de método vazio, mas a definição de método e classe abstrata é um tipo de documentação, um lembrete aos criadores de subclasses. Por outro lado, a rigidez de declarações de método pode não ser adequada em situações nas quais mais flexibilidade seja necessária. Por exemplo, seria possível criar uma versão da classe do meu Cliente, que aceita qualquer lista de métodos para processamento.

  

O suporte profundo a recursos como blocos de código torna as linguagens mais fáceis para os desenvolvedores. Imagine que queiramos permitir que os criadores de subclasses ignorem algumas etapas. O Groovy tem um operador especial de acesso protegido (?.) que garante que o objeto não é nulo antes de chamar um método com ele. Considere a definição process() na Listagem 5:

  

```
 def process() {  
   
  checkCredit?.call()  
   
  checkInventory?.call()   
   
  ship?.call()  
   
 }
```

  

*Listagem 5. Incluindo proteção na chamada de bloco de códigos.*

  

Na Listagem 5, o usuário que implementar a subclasse pode escolher a qual dos métodos-filho atribuir o código, deixando os demais em branco.

  

**Strategy**

  

Outro padrão de design popular que é simplificado por funções de primeira classe é o padrão Strategy, que define uma família de algoritmos, contendo cada um e tornando-os intercambiáveis. O padrão permite que o algoritmo varie de forma independente dos clientes que o usam. Funções de primeira classe tornam simples o desenvolvimento e manipulação de estratégias.

  

Uma implementação tradicional do padrão de design Strategy, para calcular os produtos de números, encontra-se na Listagem 6:

  

```
 interface Calc {  
   
  def product(n, m)  
   
 }  
   
   
 class CalcMult implements Calc {  
   
  def product(n, m) { n * m }  
   
 }  
   
   
 class CalcAdds implements Calc {  
   
   
  def product(n, m) {  
   
  def result = 0  
   
  n.times {  
   
  result += m  
   
  }  
   
  result  
   
  }  
   
 }
```

  

*Listagem 6. Usando o padrão de design Strategy para o produto de dois números.*

  

Na Listagem 6, definimos uma interface para o produto de dois números. Implementamos a interface com duas classes concretas diferentes (estratégias): uma usando multiplicação e a outra, adição. Para testar essas estratégias, criamos um caso de teste, mostrado na Listagem 7:

  

```
 class StrategyTest {  
   
  def listOfStrategies = [new CalcMult(), new CalcAdds()]  
   
   
  @Test  
   
  public void product_verifier() {  
   
  listOfStrategies.each { s ->  
   
  assertEquals(10, s.product(5, 2))  
   
  }  
   
  }  
   
 }
```

  

*Listagem 7. Estratégias de produto de tese.*

  

Como seria de se esperar na na Listagem 7, ambas as estratégias retornam o mesmo valor. Usando blocos de códigos como funções de primeira classe, é possível reduzir muito da cerimônia do exemplo anterior. Considere o caso das estratégias de exponenciação, mostradas na Listagem 8:

  

```
 @Test  
   
 public void exp_verifier() {  
   
  def listOfExp = [  
   
  {i, j -> Math.pow(i, j)},  
   
  {i, j ->  
   
  def result = i  
   
  (j-1).times { result *= i }  
   
  result  
   
  }]  
   
   
  listOfExp.each { e ->  
   
  assertEquals(32, e(2, 5))  
   
  assertEquals(100, e(10, 2))  
   
  assertEquals(1000, e(10, 3))  
   
  }  
   
 }
```

  

*Listagem 8. Testando a exponenciação com menos cerimônia.*

  

Na Listagem 8, definimos duas estratégias para exponenciação sequencial direta, usando blocos de códigos do Groovy. Assim como no exemplo de Template Method, trocamos formalidade por conveniência. A abordagem tradicional força nome e estrutura em torno de cada estratégia, o que pode ser útil às vezes. No entanto, observe que existe a opção de incluir proteções mais rígidas no código na Listagem 8, mas não é possível ignorar facilmente as restrições impostas pela abordagem mais tradicional - o que é mais uma discussão dinâmico contra estático em vez de uma discussão de programação funcional contra padrões de design.

  

Os padrões afetados pela presença de funções de primeira classe são, na maioria, exemplos de padrões sendo absorvidos pela linguagem. Em seguida, mostrarei um exemplo que mantém a semântica, mas muda a implementação.

  

#### Flyweight e memoização

  

O padrão Flyweight é uma técnica de otimização que usa compartilhamento para suportar um grande número de referências de objetos de baixa granularidade. O programador mantém um conjunto de objetos disponíveis, criando referências no conjunto para visualizações particulares. Flyweight usa a ideia de um objeto canônico - um objeto único que representa todos os outros objetos daquele tipo. Por exemplo, para um produto de consumidor em particular, uma versão canônica desse produto representaria todos os produtos do mesmo tipo. Em um aplicativo, em vez de criar uma lista de produtos para cada usuário, o programador cria uma lista de produtos canônicos e cada usuário tem uma referência dessa lista para seu produto.

  

Considere as classes na Listagem 9, que modelam tipos de computador:

  

```
 class Computer {  
   
  def type  
   
  def cpu  
   
  def memory  
   
  def hardDrive  
   
  def cd  
   
 }  
   
   
 class Desktop extends Computer {  
   
  def driveBays  
   
  def fanWattage  
   
  def videoCard  
   
 }  
   
   
 class Laptop extends Computer {  
   
  def usbPorts  
   
  def dockingBay  
   
 }  
   
   
 class AssignedComputer {  
   
  def computerType  
   
  def userId  
   
   
  public AssignedComputer(computerType, userId) {  
   
  this.computerType = computerType  
   
  this.userId = userId  
   
  }  
   
 }
```

  

*Listagem 9. Classes simples que modelam tipos de computador.*

  

Nessas classes, suponhamos que seja ineficiente criar uma nova instância Computer para cada usuário, supondo que todos os computadores tenham as mesmas especificações. Uma transação no estilo AssignedComputer associa um computador com um usuário.

  

Uma maneira comum de tornar esse código mais eficiente é combinar os padrões Factory e Flyweight. Considere o factory singleton para gerar tipos canônicos de computador, mostrado na Listagem 10:

  

```
 class ComputerFactory {  
   
  def types = [:]  
   
  static def instance;  
   
   
  private ComputerFactory() {  
   
  def laptop = new Laptop()  
   
  def tower = new Desktop()  
   
  types.put("MacBookPro6_2", laptop)  
   
  types.put("SunTower", tower)  
   
  }  
   
   
  static def getInstance() {  
   
  if (instance == null)  
   
  instance = new ComputerFactory()  
   
  instance  
   
  }  
   
   
  def ofType(computer) {  
   
  types[computer]  
   
  }   
   
 }
```

  

*Lista 10. Factory singleton para instâncias de computador em flyweight.*

  

A classe ComputerFactory desenvolve um cache de possíveis tipos de computadores e, em seguida, fornece a instância adequada por meio do método ofType(). Esse é um factory singleton da forma como seria escrito em Java.

  

No entanto, Singleton também é um padrão de design (consulte "Recursos")) e é outro bom exemplo de um padrão absorvido pelo tempo de execução. Considere ComputerFactory simplificado, usando a anotação @Singleton fornecida por Groovy, mostrada na Listagem 11:

  

```
 @Singleton class ComputerFactory {  
   
  def types = [:]  
   
   
  private ComputerFactory() {  
   
  def laptop = new Laptop()  
   
  def tower = new Desktop()  
   
  types.put("MacBookPro6_2", laptop)  
   
  types.put("SunTower", tower)  
   
  }  
   
   
  def ofType(computer) {  
   
  types[computer]  
   
  }  
   
 }
```

  

*Listagem 11. Factory singleton simplificado.*

  

Para testar se o factory retorna instâncias canônicas, criamos um teste de unidade, mostrado na Listagem 12:

  

```
 @Test  
   
 public void flyweight_computers() {  
   
  def bob = new AssignedComputer(ComputerFactory.instance.ofType("MacBookPro6_2"), "Bob")  
   
  def steve = new AssignedComputer(ComputerFactory.instance.ofType("MacBookPro6_2"),   
   
  "Steve") assertTrue(bob.computerType == steve.computerType)
```

  

*Lista 12. Testando tipos canônicos.*

  

Salvar informações comuns entre instâncias é uma boa ideia, uma ideia que eu quero preservar quando passar para a programação funcional. No entanto, os detalhes da implementação são bem diferentes. Esse é um exemplo de como preservar a *semântica* de um padrão e mudar (preferencialmente, simplificar) a implementação.

  

Em último artigo, eu falei sobre *memoização*, um recurso integrado em uma linguagem de programação que permite armazenamento em cache automático de valores de retorno de função recorrentes. Em outras palavras, uma função memoizada permite que o tempo de execução armazene os valores em cache para o programador. As versões recentes do Groovy suportam memoização (consulte "Recursos")). Considere as funções definidas na Listagem 13:

  

```
 def computerOf = {type ->  
   
  def of = [MacBookPro6_2: new Laptop(), SunTower: new Desktop()]  
   
  return of[type]  
   
 }  
   
   
 def computerOfType = computerOf.memoize()
```

  

*Lista 13. Memoização de flyweights.*

  

Na Listagem 13, os tipos canônicos são definidos na função computerOf. Para criar uma instância memoizada da função, simplesmente chamamos o método memoize(), definido pelo tempo de execução do Groovy.

  

A Listagem 14 mostra um teste de unidade comparando a chamada das duas abordagens:

  

```
 @Test  
   
 public void flyweight_computers() {  
   
  def bob = new AssignedComputer(ComputerFactory.instance.ofType("MacBookPro6_2"), "Bob")  
   
  def steve = new AssignedComputer(ComputerFactory.instance.ofType("MacBookPro6_2"),   
   
  "Steve") assertTrue bob.computerType == steve.computerType  
   
   
  def sally = new AssignedComputer(computerOfType("MacBookPro6_2"), "Sally")  
   
  def betty = new AssignedComputer(computerOfType("MacBookPro6_2"), "Betty")  
   
  assertTrue sally.computerType == betty.computerType  
   
 }
```

  

*Listagem 14. Comparando abordagens*.

  

O resultado final é o mesmo, mas observe a enorme diferença nos detalhes da implementação. Para o padrão de design "tradicional", criamos uma nova classe para agir como um factory, implementando dois padrões. Para a versão funciona, implementados um único método e retornamos uma versão memoizada. A transferência de detalhes como o armazenamento em cache para o tempo de execução traz menos oportunidades para falhas das implementações escritas à mão. Nesse caso, preservamos a semântica do padrão Flyweight, mas com uma implementação muito simples.

  

#### Conclusão

  

Neste artigo, eu apresentei as três maneiras como a semântica dos padrões de design se manifesta na programação funcional. Em primeiro lugar, eles podem ser absorvidos pela linguagem ou tempo de execução. Mostrei exemplos disso usando os padrões Factory, Strategy, Singleton e Template Method. Em segundo lugar, os padrões podem preservar sua semântica, mas ter implementações completamente diferentes: mostrei um exemplo do padrão Flyweight usando classes e usando memoização. Em terceiro, linguagens e tempos de execução funcionais podem ter recursos totalmente diferentes, o que lhes permite solucionar problemas de maneiras completamente diferentes.

  

No próximo artigo, continuarei essa investigação da intersecção entre padrões de design e programação funcional e mostrarei exemplos da terceira abordagem.

  

#### Recursos

  

**Aprender**

  

[*The Productive Programmer*](http://oreilly.com/catalog/9780596519780/) (Neal Ford, O'Reilly Media, 2008): O livro mais recente de Neal Ford trata de ferramentas e práticas que ajudam a melhorar sua eficiência em codificação.

  

[*Design Patterns: Elements of Reusable Object-Oriented Software*](http://www.amazon.com/Design-Patterns-Object-Oriented-Addison-Wesley-Professional/dp/0201633612/ref%3Dsr_1_1%3Fie%3DUTF8%26amp;s%3Dbooks%26amp;qid%3D1236221690%26amp;sr%3D1-1) (Erich Gamma et al., Addison-Wesley, 1994): o trabalho clássico da Gang of Four sobre padrões de design.

  

[Padrões de Design em Linguagens Dinâmicas](http://norvig.com/design-patterns/ppframe.htm): A apresentação de Peter Norvig argumenta que linguagens eficientes (como linguagens funcionais) precisam menos de padrões de design.

  

[Groovy](http://groovy.codehaus.org/): Groovy é uma linguagem de JVM multiparadigma com sintaxe muito semelhante à do Java. Seus vários recursos avançados incluem muitos aumentos de programação funcional.

  

[Scala](http://scala-lang.org/): Scala é uma linguagem funcional moderna no JVM.

  

[*Guia do Scala para desenvolvedores de Java atarefados*](http://www.ibm.com/developerworks/views/java/libraryview.jsp?search_by=scala+neward): aprofunde-se em Scala nessa série do developerWorks escrita por Ted Neward.

  

[Padrão Template method](http://en.wikipedia.org/wiki/Template_method_pattern): Template Method é um conhecido padrão de design de Gang of Four.

  

[Padrão Singleton](http://en.wikipedia.org/wiki/Singleton_pattern): Singleton é outro conhecido padrão de Gang of Four.

  

[Memoização do encerramento](http://groovy.codehaus.org/Groovy+1.8+release+notes#Groovy18releasenotes-Closurememoization): confira as notas sobre o release do recurso de memoização incluído no Groovy 1.8.

  

Navegue pela [livraria de tecnologia](http://www.ibm.com/developerworks/apps/SendTo?bookstore=safari) para ver livros sobre este e outros tópicos técnicos.

  

[Zona de tecnologia Java do developerWorks](http://www.ibm.com/developerworks/java): Encontre centenas de artigos sobre cada aspecto da programação Java.

**Obter produtos e tecnologias**

  

[Avalie produtos IBM](http://www.ibm.com/developerworks/downloads/) da maneira que for melhor para você: faça download da versão de teste de um produto, avalie um produto on-line, use-o em um ambiente de nuvem ou passe algumas horas na [no Ambiente de Simulação da SOA](http://www.ibm.com/developerworks/downloads/soasandbox/index.html) aprendendo a implementar Arquitetura Orientada a Serviços de modo eficiente.

**Discutir**

  

Participe dos [comunidade do developerWorks](http://www.ibm.com/developerworks/community/). Entre em contato com outros usuários do developerWorks e explore os blogs, fóruns, grupos e wikis voltados para desenvolvedores.

\*\*\*

  

**Sobre o autor:** Neal Ford é arquiteto de software e Meme Wrangler na ThoughtWorks, uma consultoria global de TI. Ele também desenvolve aplicativos, materiais de instrução, artigos para revistas, treinamentos e apresentações em vídeo/DVD e é autor ou editor de livros que abordam várias tecnologias, incluindo o mais recente, [*The Productive Programmer*](http://oreilly.com/catalog/9780596519780/). Sua especialidade é o desenvolvimento de aplicativos corporativos de grande porte. Também é palestrante admirado em conferências de desenvolvedores no mundo todo. Conheça seu [website](http://www.nealford.com/).

  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](imasters-com-br--pensamento-funcional-padroes-de-design-funcional-parte-01/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Pensamento+funcional%3A+padr%C3%B5es+de+design+funcional+-+Parte+01&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24360%2Fdesign%2Fpensamento-funcional-padroes-de-design-funcional-parte-01)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](imasters-com-br--pensamento-funcional-padroes-de-design-funcional-parte-01/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Pensamento+funcional%3A+padr%C3%B5es+de+design+funcional+-+Parte+01&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24360%2Fdesign%2Fpensamento-funcional-padroes-de-design-funcional-parte-01)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/133515345842/u/49/f/546640/c/33212/s/1f1fa7f2/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
  
from iMasters - <http://imasters.com.br/artigo/24360/design/pensamento-funcional-padroes-de-design-funcional-parte-01>
