---
url: "http://blog.caelum.com.br/um-exemplo-bacana-de-coercao-em-ruby/"
captured_at: "2014-10-29T12:11:20-03:00"
title: "Um exemplo bacana de coerção em Ruby"
domain: "blog-caelum-com-br"
---

Ruby é cheio de características interessantes. Uma delas, muito importante, é a flexibilidade.

Por exemplo, as operações aritméticas em ruby (+, -, \*, /) não são definidas por operadores reservados da linguagem. São definidas como métodos. Veja; quando executamos o código a seguir:

```
2 + 2
```

O que o interpretador entende é análogo a

```
2.+(2)
```

A primeira versão do código é apenas uma maneira mais limpa de representar a segunda.

Ok, fica mais limpo. Mas onde está a flexibilidade?

Como + é um método como outro qualquer, é possível que ele seja definido ou redefinido por um código nosso. Neste caso, o método + está definido na classe Fixnum, que define o comportamento do números inteiros. Nesse caso específico do objeto ‘2’. Sim, o literal ‘2’ é uma instância de Fixnum.

Para exemplificar esse tipo de flexibilidade, vamos só por diversão criar uma classe que represente um intervalo de tempo em minutos. Quero usá-la da seguinte forma:

```
intervalo = Intervalo.new(90)
puts "#{intervalo.horas}:#{intervalo.minutos}" # => 1:30
```

Para que isso seja possível, a classe Intervalo deve ter um construtor, um método chamado horas e outro chamado minutos.

```
class Intervalo
  def initialize(minutos)
    @minutos = minutos
  end

  def horas
    @minutos / 60
  end

  def minutos 
    @minutos % 60
  end
end
```

O método horas retorna o resultado inteiro da divisão do total de minutos por 60. E o método minutos retorna o resto inteiro dessa divisão.

Legal! Mas é meio cansativo ficar digitando “#{intervalo.horas}:#{intervalo.minutos}” em todo lugar que quisermos exibir um intervalo. Seria mais interessante poder digitar apenas intervalo.to\_s. Ou seja, invocar a representação String do nosso objeto intervalo e ter o mesmo efeito.

No entanto, se executarmos o intervalo.to\_s, vamos perceber que o retorno é algo como “#”, e não o desejado 1:30.

Isso acontece porque o interpretador simplesmente não foi ensinado a representar como String um objeto da classe Intervalo. Ele simplesmente utiliza a definição presente na classe Object, ou seja, ele utiliza a implementação herdada do método to\_s definida para qualquer Object. Precisamos, portanto, redefinir o método to\_s para ter um comportamento específico na classe Intervalo. Simples:

```
class Intervalo
  # ...

  def to_s
    "#{horas}:#{minutos}"
  end
end
```

A bem da verdade, ainda existe um probleminha.

```
intervalo = Intervalo.new(61)
puts intervalo.to_s # => 1:1
```

É mais interessante que os minutos sempre tenham duas casas. Para que isso aconteça, podemos usar sprintf que aceita uma máscara para definir a formatação. Logo, nosso método to\_s fica melhor assim:

```
class Intervalo
  # ...

  def to_s
    sprintf("%.1i:%.2i", horas, minutos)
  end
end
```

Ok. Mas e a história da soma? O que aconteceria se eu tentasse somar 30 minutos a um intervalo de 90 minutos? Teríamos um intervalo de 2 horas?

```
intervalo = Intervalo.new(90)
novo_intervalo = intervalo + 30
```

Isso falha. E a mensagem de erro nos avisa que o objeto intervalo (que é uma instância da classe Intervalo) não tem o método +. Lembre-se que

```
intervalo + 30
```

Equivale a

```
intervalo.+(30)
```

Para chegar ao resultado desejado, não é necessário nada de especial. Basta definir o método + dentro da classe Intervalo.

```
class Intervalo
  # ...

  def +(outros_minutos)
    Intervalo.new(@minutos + outros_minutos)
  end
end
```

Lindo! Agora é possível somar um intervalo a um número inteiro que representa os minutos que devem ser acrescentados.

```
intervalo = Intervalo.new(90)
novo_intervalo = intervalo + 30
puts novo_intervalo.to_s # => 2:00
```

Perceba que nosso objeto intervalo é imutável. A operação de adição retorna um novo objeto em vez de alterar o objeto original. Essa é uma prática que visa [reduzir a complexidade do código](http://www.caelum.com.br/apostila-java-testes-xml-design-patterns/o-modelo-da-bolsa-de-valores-datas-e-objetos-imutaveis/#2-7-imutabilidade-de-objetos "reduzir a complexidade do código").

Dá para ir mais longe. O que aconteceria se tentássemos somar dois intervalos?

```
uma_hora_e_meia = Intervalo.new(90)
uma_hora = Intervalo.new(60)

soma = uma_hora_e_meia + uma_hora
```

Temos uma mensagem de erro que a príncipio parece meio críptica: “Intervalo can’t be coerced into Fixnum”. No entanto, ela revela que o interpretador está tentando ‘coerce’ ou seja forçar nosso objeto Intervalo a ser tratado como um objeto do tipo Fixnum (numérico). Por que isso acontece? Vamos olhar para dentro do método Intervalo#+. Para simplificar o entendimento, vamos expandir o método pra realizar seu trabalho em duas linhas.

```
class Intervalo
  # ...

  def +(outros_minutos)
    novo_valor = @minutos + outros_minutos
    Intervalo.new(novo_valor)
  end
end
```

No último exemplo, perceba que dentro do método Intervalo#+ quando fazemos a soma

```
novo_valor = @minutos + outros_minutos
```

Temos @minutos como sendo um objeto da classe Fixnum, ou seja, um número inteiro. E outros\_minutos como sendo um objeto da classe Intervalo. Logo nosso problema, para simplificar, deriva da seguinte situação: Já é possível fazer a soma Intervalo + Fixnum; porém não é possível fazer a soma Fixnum + Intervalo. Veja:

```
intervalo = Intervalo.new(90)
soma_intervalo_mais_inteiro = intervalo + 30 # => 2:00

soma_inteiro_mais_intervalo = 30 + intervalo # => "Intervalo can't be coerced into Fixnum"
```

Lembrando que a última soma é traduzida para

```
30.+(intervalo)
```

Ou seja, é chamado o método + definido na classe Fixnum. Esse método está definido no core da linguagem e não faz nenhuma idéia do que possa ser um Intervalo.

No entanto, os idealizadores do Ruby pensaram numa maneira bem interessante de flexibilizar o comportamento do método Fixnum#+. Como a classe Fixnum não sabe somar Intervalos, ela delega esta responsabilidade de volta para a classe Intervalo. Ou seja, quando um Fixnum está sendo somado a algo que o Ruby não reconhece como número, ele solicita ao objeto desconhecido que devolva dois objetos compativeis. Isso é realizado por um método chamado coerce. A responsabilidade desse método é devolver dois objetos que possam ser somados. Por exemplo.

```
class Intervalo
  # ...
  def coerce(numero_inteiro)
    [numero_inteiro, @minutos]
  end
end
```

Perceba que agora quando executar

```
30 + intervalo
```

Internamente, o objeto 30 vai chamar o método coerce do objeto intervalo para ter como retorno um par de objetos compatíveis com a operação de soma. Algo como

```
intervalo.coerce(30) # => [30, 90]
```

Perceba agora que a operação de soma prosseguirá dentro do método Fixnum#+ usando estes dois objetos, que são perfeitamente ‘somáveis’.

30.+(90) # => 120

Assim sendo a operação toda se resolve e temos como resultado da soma Fixnum + Intervalo um número inteiro, ou seja, um Fixnum.

```
intervalo = Intervalo.new(90)
soma = 30 + intervalo 
# ocorre uma chamada para intervalo.coerce(30) cujo retorno é [30, 90] e em seguida 30.+(90) retornando 120
puts soma # => 120
```

Ótimo! A classe Fixnum está disposta a ser interoperável com qualquer outra classe. Desde que lhe seja dada uma maneira de entender como os objetos dessa nova classe querem ser somados a um Fixnum.

Bacana! Mas dá pra ficar melhor. A situação que temos agora é:

Intervalo + Fixnum => Intervalo  
 Fixnum + Intervalo => Fixnum

Meio esquisito. Seria mais interessante que indepententemente da ordem dos operadores o resultado fosse sempre um Intervalo. E é aí que está o pulo do gato.

Perceba que podemos controlar completamente como vai ser a operação de soma realizada pelo Fixnum. Basta que nosso método coerce retorne um par de objetos apropriado.

Neste momento nosso método Intervalo#coerce retorna [30, 90], ou seja, [Fixnum, Fixnum]. O que aconteceria se retornássemos [Intervalo, Fixnum]? Ou seja

```
class Intervalo
  def coerce(numero_inteiro)
    [Intervanlo.new(numero_inteiro), @minutos]
  end
end
```

Invertemos a soma!

```
30 + Intervalo.new(90)
```

Para algo como

```
Intervalo.new(30) + 90
```

Isso é lindo e genial! Pois o controle da operação de soma do Fixnum volta para o método + da classe Intervalo! E nesse método a operação de soma já está corretamente definida e retorna um objeto do tipo Intervalo :]

Assim temos

Intervalo + Fixnum => Intervalo  
 Fixnum + Intervalo => Intervalo

E facilmente conseguiremos chegar a

Intervalo + Intervalo => Intervalo

Para que isso seja possível, precisamos olhar para nossa implementação do método Intervalo#+

```
class Intervalo
  # ...
  def +(outros_minutos)
    novo_valor = @minutos + outros_minutos
    Intervalo.new(novo_valor)
  end
end
```

Agora, novo\_valor pode ser Fixnum (quando estamos somando Intervalo + Fixnum) ou Intervalo (quando estamos somando Fixnum + Intervalo e usando coerção). Neste segundo caso, quando novo\_valor é do tipo Intervalo, vamos ter um problema ao fazer Intervalo.new(novo\_valor), pois o método Intervalo#initialize

```
class Intervalo
  def initialize(minutos)
    @minutos = minutos
  end
end
```

Guardaria a representação interna @minutos como sendo um Intervalo. E @minutos deve ser sempre um Fixnum. Como resolver isso?

Para garantir que @minutos seja sempre do tipo Fixnum, basta forçar que o parâmetro minutos seja convertido para Fixnum indepententemente de sua natureza. Garantimos isso chamando minutos.to\_i

```
class Intervalo
  def initialize(minutos)
    @minutos = minutos.to_i
  end
end
```

Portanto, quando um objeto do tipo Intervalo precisar ser representado como um inteiro, podemos fazer que ele devolva o número absoluto de minutos que o compõe. A convenção em Ruby para que um objeto seja convertido para número inteiro é que sua classe exponha um método chamado to\_i. Logo

```
class Intervalo
  # ...
  def to_int
    @minutos
  end
end
```

Como estamos seguindo a conveção de definir um método chamado to\_i, não precisamos nos preocupar quando o parâmetro minutos do construtor é do tipo Fixnum, pois nesta classe o método to\_i já está definido e retorna o próprio objeto em que foi chamado. Bonito, não?

Referências:

http://www.mutuallyhuman.com/blog/2011/01/25/class-coercion-in-ruby/

https://pragprog.com/book/ruby/programming-ruby
