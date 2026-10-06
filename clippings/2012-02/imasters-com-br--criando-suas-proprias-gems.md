---
url: "http://imasters.com.br/artigo/23464/ruby-on-rails/criando-suas-proprias-gems"
captured_at: "2012-02-01T12:23:49-03:00"
title: "Criando suas próprias gems"
domain: "imasters-com-br"
---

### Sent to you by Thiago Silva via Google Reader:

## 

[Criando suas próprias gems](http://feedproxy.google.com/~r/imasters/~3/JA-PBHhUYtU/story01.htm)

via [iMasters -](http://imasters.com.br/) by Uriel Juliatti () on 2/1/12

  

Mesmo com pouco tempo de desenvolvimento, pude concluir que continuamente escrevia aplicações amarradas e extremamente acopladas. À medida que fui adquirindo experiência e a oportunidade de desenvolver aplicações mais robustas aqui na Giran ([@giran\_br](http://www.h-online.com/open/news/item/Debian-7-0-will-use-3-2-kernel-1425560.html)), notei a urgência de aprender a desenvolver aplicações mais flexíveis e modulares, isto é, “plugáveis”. Essa visão torna o sistema mais coeso e com o risco de acoplamento bem menor – como aconselham as boas práticas sobre a arquitetura de um projeto de sistema e a “real” Orientação a Objetos (polêmicos).

Contudo, com esse objetivo em vista, resolvi utilizar os recursos do ruby para ir de encontro às melhores soluções. E embarcando nessa jornada comecei a dar uma pincelada sobre as solução já existentes no ruby, quando então me deparei com o mais óbvio: as gems - Você já fez um gem install -algumagembonitaecharmosaquevaifazertudopragente-, não é? É por aí...

Mas antes da prática, um pouco de teoria para fixar:

#### **RubyGems**

A descrição do site oficial diz:

> RubyGems is a package manager for the Ruby programming language that provides a standard format for distributing Ruby programs and libraries (in a self-contained format called a “gem”), a tool designed to easily manage the installation of gems, and a server for distributing them.

Utilizando a referência, o RubyGems é um gerenciador de pacotes para ruby que facilita a instalação de gems. Alguns se confundem com a definição e até mesmo com a aplicação dos termos, confundindo um com o outro, mas o RubyGem é, como havia dito, o gerenciador, ou seja, a ferramenta necessária para versionar, instalar, desinstalar, listar , procurar, construir as gems etc.

#### **E o que são gems?**

Bibliotecas, pacotes e até mesmo aplicações em ruby, se assim posso dizer – uma gem é basicamente isso. Porém, a maneira que você vai utilizar essa gem é uma questão de decisão de cada programador de acordo com a decisão de cada projeto.

#### **Teoria, teoria, bla bla bla**

O principal objetivo deste artigo é ensinar como funciona a construção de uma gem simples e como ela pode ser construída. Portanto, não haverá nenhum tipo de implementação por agora. Vamos começar com o já subestimado *HelloWorld* para o mundo da criação de gems. Depois dessa chuva teórica – e radioativa – abra o seu terminal e crie o ambiente ruby para esta gem:

```
1 rvm gemset create hello_word  
  
1 rvm gemset use hello_word
```

Se você não sabe ou nunca utilizou o RVM, pode começar lendo [aqui](https://rvm.beginrescueend.com/gemsets/basics/) e [aqui](https://rvm.beginrescueend.com/rvm/install/). O RVM irá ajudar bastante na organização dos rubies dos seus projetos.

#### **Criando a estrutura**

A partir daí, passamos para a construção do esqueleto das nossas gems: alguns preferem via shellzinho [trollface].

```
1 mkdir -p hello_world/{lib/hello_world,test}
```

, outros preferem usar o [Jeweler](https://github.com/technicalpickles/jeweler) – tanto para estrutura como para o manipulamento – mas eu escolhi o [Bundler](http://gembundler.com/) - a mesma biblioteca que utilizamos no rails para instalar as dependências do Gemfile.

Portanto, caso não tiver instalado – verifique com um rvm gem list - utilize o comando *gem install bundler* e, com a gem já instalada, vamos criar a nossa estrutura assim: *$ bundle gem hello\_world*:

```
create hello_world/Gemfile  
create hello_world/Rakefile  
create hello_world /.gitignore  
create hello_world/hello_world.gemspec  
create hello_world/lib/hello_world.rb  
create hello_world/lib/hello_world/version.rb  
Initializating git repo in /Users/urieljuliatti/git/hello_world
```

#### **Modificando o gemspec**

O bundler criou um arquivo .gemspec que possui diversos dados sobre a sua gem recém-criada. Algumas partes você precisa modificar, mas falarei em alguns instantes. Obtivemos o seguinte dentro do .gemspec:

```
# -*- encoding: utf-8 -*-  
$:.push File.expand_path("../lib", __FILE__)  
require "hello_world/version"  
   
Gem::Specification.new do |s|  
s.name = "hello_world"  
s.version = HelloWorld::VERSION  
s.platform = Gem::Platform::RUBY  
s.authors = ["Seu nome"]  
s.email = ["Seu email"]  
s.homepage = "Seu Website"  
s.summary = %q{Um resumo.}  
s.description = %q{A descrição da sua gem}  
   
s.rubyforge_project = "hello_world"  
   
s.files = `git ls-files`.split("\n")  
s.test_files = `git ls-files -- {test,spec,features}/*`.split("\n")  
s.executables = `git ls-files -- bin/*`.split("\n").map{ |f| File.basename(f) }  
s.require_paths = ["lib"]  
end
```

*\* Utilizaremos as configurações logo adiante na hora que formos publicar nossas gem.*

#### **Versionamento**

Observe que o Bundler criou um /version além de uma constante chamada HelloWorld::VERSION – gerada pelo version.rb dentro de lib/hello\_world – para a nossa gem, isso significa que você pode versioná-la através dele. Inclusive, esse é um dos bons recursos adquiridos ao tomar uma decisão de criar uma gem. O ideal é você seguir algumas recomendações [Semantic Versioning](http://semver.org/), mas, caso deseje uma mais simples, seguiremos com algumas considerações que fiz:

```
# dir: /lib/hello_world/version.rb  
   
module HelloWorld  
   
VERSION = "0.0.1"  
   
end
```

Quando sua gem tiver outros ou novos recursos, é só modificar o número da versão e publicar novamente com o gem build.

Agora vejamos o que foi gerado no diretório lib/, temos um arquivo chamado *hello\_world*, que é o cara que chamamos quando alguém requerer nossa gem. Você pode criar outros arquivos no diretório e chamá-los nessa classe, mas no nosso caso vai ser só o método hello, para demonstração.

```
# dir: lib/hello_world.rb  
   
module HelloWorl  
   
def self.hello  
   
"Olá mundo!"  
   
end  
   
end
```

#### **Publicando nossa gem**

Bem, agora que você já gerou a estrutura, criou seu arquivo ruby e definiu algum comportamento (método), vamos então editar nosso gemspec para publicar nossa gem:

```
# -*- encoding: utf-8 -*-  
$:.push File.expand_path("../lib", __FILE__)  
require "hello_world/version"  
   
Gem::Specification.new do |s|  
s.name = "hello_world"  
s.version = HelloWorld::VERSION  
s.platform = Gem::Platform::RUBY  
s.authors = ["Uriel Juliatti"]  
s.email = ["uriel.juliatti@giran.com.br"]  
s.homepage = ""  
s.summary = %q{Primeira gemzinha para aprender como criar a sua própria gem.}  
s.description = %q{Essa gem é um demonstrativo do blog do Uriel Juliatti, desenvolvedor web na Giran Soluções e E-commerce.}  
   
s.rubyforge_project = "hello_world"  
   
s.files = `git ls-files`.split("\n")  
s.test_files = `git ls-files -- {test,spec,features}/*`.split("\n")  
s.executables = `git ls-files -- bin/*`.split("\n").map{ |f| File.basename(f) }  
s.require_paths = ["lib"]  
end
```

Agora buildamos a nossa gem:

```
$ gem build hello_world.gemspec  
WARNING: no homepage specified  
Successfully built RubyGem  
Name: hello_world  
Version: 0.0.1  
File: hello_world-0.0.1.gem
```

Esse comando é responsável por gerar um .gem. Inclusive, omiti a homepage, caso contrário, ele iria subir o arquivo para o repositório Rubygems.org e deixaria disponível ao público essa gem teste.

#### **Gemfile**

Um detalhe para  o arquivo de Gemspec – como já mostrado anteriormente –  é que podemos carregar dependências através do bundler – sem nos preocuparmos em gerenciar esse arquivo diretamente. É a melhor forma para gerenciar dependências de uma gem. Por exemplo, digamos que escolhêssemos usar o RSpec para testar a nossa gem: em vez de referenciar o *RSpec* diretamente no Gemfile, vamos adicioná-lo como uma dependência em *hello\_word.gemspec*.

Obs: Se você não estiver familiarizado com o gerenciamento de um arquivo Gemspec, dê uma conferida na [documentação](http://docs.rubygems.org/read/chapter/20#dependencies).

```
# -*- encoding: utf-8 -*-  
$:.push File.expand_path("../lib", __FILE__)  
require "hello_world/version"  
   
Gem::Specification.new do |s|  
s.add_development_dependency "rspec"  
end
```

Só para garantir, já que o arquivo é referenciado através do Gemfile, vamos executar o bundle e averiguar se temos todas as dependências instaladas:

```
$ bundle  
Fetching source index for http://rubygems.org/  
Using diff-lcs (1.1.2)  
Using hello_world (0.0.1) from source at /Users/urieljuliatti/Projects/ruby/hello_world  
Installing rspec-core (2.3.1)  
Installing rspec-expectations (2.3.0)  
Installing rspec-mocks (2.3.0)  
Installing rspec (2.3.0)  
Using bundler (1.0.7)  
Your bundle is complete! It was installed into /Users/urieljuliatti/.rvm/gems/ruby-1.9.2-p290
```

Dessa forma, ao publicarmos uma gem que tenha vários contribuidores envolvidos, você pode instruí-los a usar o bundle, ajudando-os a configurar o ambiente e instalando todas as suas dependências de uma só vez. Como boa prática, adicione essas informações sempre no README da sua gem.

#### **Gerenciando tarefas**

Outro bom detalhe é se atentar ao Rakefile gerado pelo Bundler e as suas tarefas:

```
#dir /Rakefile  
   
require 'bundler'  
   
$ rake -T  
   
(in /Users/urieljuliatti/ruby/hello_world)  
   
rake build # Constrói a gem dentro de um diretório , empacotando-a.  
   
rake install # Constrói e instala a gem no sistema de gems  
   
rake release # Cria uma tag para a versão, constrói a gem e publica lá em Rubygems
```

Esse código é responsável por instalar uma gem configurada do nosso jeito, portanto podemos instalá-la e testá-la por completo localmente. Aí, então, chamar o rake release para tagear aquela versão e publicá-la no RubyGems. Praticamente, é uma forma de “automatizar” certos processos referentes à produção das nossas gems.

[anexo ausente]

|  |  |
| --- | --- |
| [9bcafcd24ef5e7a319a7e300c0d5b221.gif](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&title=Criando+suas+pr%C3%B3prias+gems&link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F23464%2Fruby-on-rails%2Fcriando-suas-proprias-gems) | [75b9131ce15803402621ad7d693d4dd1.gif](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Criando+suas+pr%C3%B3prias+gems&link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F23464%2Fruby-on-rails%2Fcriando-suas-proprias-gems) |

  
  
[[anexo ausente]](http://da.feedsportal.com/r/123995923767/u/49/f/546640/c/33212/s/1c5171ab/a2.htm)[anexo ausente]

  

### Things you can do from here:

- [Subscribe to iMasters -](http://www.google.com/reader/view/feed%2Fhttp%3A%2F%2Fimasters.uol.com.br%2Ffeed%2F?source=email) using **Google Reader**
- [Get started using Google Reader](http://www.google.com/reader/?source=email) to easily keep up with **all your favorite sites**
