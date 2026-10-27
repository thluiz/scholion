---
url: "https://nandovieira.com.br/openstruct-no-ruby-dois-ponto-zero"
captured_at: "2013-01-21T10:12:50-03:00"
title: "OpenStruct no Ruby 2.0"
domain: "nandovieira-com-br"
---

Recentemente foi [lançada a versão RC1 do Ruby 2.0.0](http://blade.nagaokaut.ac.jp/cgi-bin/scat.rb/ruby/ruby-core/51301). Dando uma olhada no [changelog](https://github.com/ruby/ruby/blob/v2_0_0_rc1/NEWS), algumas mudanças relacionadas à classe OpenStruct chamaram minha atenção.

  

A classe [OpenStruct](http://ruby-doc.org/stdlib-1.9.3/libdoc/ostruct/rdoc/OpenStruct.html) permite criar uma estrutura de dados com atributos que podem ser definidos de forma arbitrária. Além disso, se você passar um Hash durante a instanciação, cada uma das chaves irá gerar um atributo equivalente.

  

```
 require "ostruct"  
   
 user = OpenStruct.new({  
   :name => "John Doe",  
   :email => "john@example.org"  
 })  
   
 puts user.name  
 #=> John Doe  
   
 puts user.email  
 #=> john@example.org
```

  

Você também pode atributir valores livremente, como o exemplo abaixo.

  

```
 user.age = 42  
 puts user.age  
 #=> 42
```

  

Em versões anteriores, você só podia acessar os atributos de uma instância da OpenStruct através dos métodos *readers*. No entanto, o Ruby 2.0 introduziu alguns métodos muito úteis.

  

```
 puts user[:name]  
 #=> John Doe  
   
 puts user["name"]  
 #=> John Doe
```

  

Você também pode usar o método `OpenStruct#[]=` para definir atributos.

  

```
 user["name"] = "John D."  
 puts user.name  
 #=> John D.
```

  

Um outro método que foi adicionado permite retornar uma representação da OpenStruct como Hash. Trata-se do método `OpenStruct#to_h`. No Ruby 1.9 este método retornava `nil`.

  

```
 p user.to_h  
 #=> {:name=>"John Doe", :email=>"john@example.org", :age=>42}
```

  

E, finalmente, uma mudança muito útil está relacionada ao método `OpenStruct.new`, que agora aceita instâncias das classes OpenStruct e Struct.

  

```
 another_user = OpenStruct.new(user)  
   
 p another_user.to_h  
 #=> {:name=>"John Doe", :email=>"john@example.org", :age=>42}
```

  

Para quem gosta muito da classe [HashWithIndifferentAccess](https://github.com/rails/rails/blob/master/activesupport/lib/active_support/hash_with_indifferent_access.rb), disponível na biblioteca [ActiveSupport](https://rubygems.org/gems/activesupport), esta mudança é particularmente empolgante.

  
   
   
 from Simples Ideias <http://simplesideias.com.br/openstruct-no-ruby-dois-ponto-zero>
