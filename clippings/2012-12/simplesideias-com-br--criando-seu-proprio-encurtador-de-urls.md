---
url: "http://simplesideias.com.br/criando-seu-proprio-encurtador-de-urls"
captured_at: "2012-12-28T10:44:11-03:00"
title: "Criando seu próprio encurtador de URLs"
domain: "simplesideias-com-br"
---

Um dia desses eu estava dando uma olhada na lista de domínios que eu tenho e vi que o domínio  [<http://fnando.me>](http://fnando.me) estava sem uso. Aí, decidi criar um encurtador de URL usando [Sinatra](http://sinatrarb.com) e [Redis](http://redis.io).

  

Criar encurtadores de URL é uma coisa bastante simples. Normalmente, utilizo o `id` do registro que identifica a URL original em base 36, por exemplo. Com Ruby isso é moleza.

  

```
 id = 12345  
 short = id.to_s(36)  
   
 puts short  
 #=> 9ix  
   
 puts short.to_i(36)  
 #=> 12345
```

  

Uma das vantagens de se usar a base 36 como identificador de URLs é que você tem um limite bastante grande com poucos caracteres. O id 9999999 gera o identificador `5yc1r` com apenas 5 caracteres.

  

Para armazenar estas URLs você pode usar o Redis. Fácil de usar e muito rápido, ele é perfeito para esta tarefa. No Ruby, você pode usar a gem [redis](http://rubygems.org/gems/redis).

  

Primeiro, precisamos definir como iremos armazenar a URL. Você usar uma chave que contenha uma identificação da URL original, além do identificador curto desta URL. Algo como `urls:<url>:<id curto>`.

  

Para saber qual o próximo id disponível para a URL você pode usar o comando `INCR`, que incrementa um número inteiro em uma chave.

  

```
 redis = Redis.new  
 sid = redis.incr("urls._id").to_s(36)
```

  

Para armazenar uma representação da URL, vamos gerar um hash MD5.

  

```
 require "digest/md5"  
   
 url = "http://codeplane.com.br"  
 hash = Digest::MD5.hexdigest(url)
```

  

Agora podemos armazenar a URL no Redis.

  

```
 key = "urls:#{hash}:#{sid}"  
 redis.set(key, url)
```

  

Antes de armazenar a URL você pode verificar se esta URL já foi salva com o comando `KEYS`, passando o hash da URL.

  

```
 unless redis.keys("urls:#{hash}:*").first  
   redis.set(key, url)  
 end
```

  

Para pegar a URL original, você pode fazer uma consulta semelhante, passando apenas o id curto.

  

```
 key = redis.keys("urls:*:#{sid}").first  
 url = redis.get(key) if key
```

  

Agora, como fazer tudo isso rodar em produção? Simples! Eu já peguei tudo isso e empacotei em uma gem ridiculamente simples de usar.

  

## Usando o Dogo

  

A gem [dogo](http://rubygems.org/gems/dogo) faz basicamente tudo isso e ainda disponibiliza um servidor Sinatra que já lida com as requisições.

  

Crie um arquivo `Gemfile` com as dependências de nosso projeto. Em desenvolvimento, gosto de usar o Thin.

  

```
 source :rubygems  
   
 gem "dogo"  
 gem "unicorn"  
   
 group :development do  
   gem "pry"  
   gem "awesome_print"  
   gem "thin"  
 end
```

  

Nós vamos precisar do arquivo `config.ru`, com as informações do Dogo.

  

```
 require "bundler/setup"  
 require "dogo"  
   
 Dogo.host = "http://fnando.me"  
 Dogo.api_key = "abc"  
 Dogo.default_url = "http://nandovieira.com.br"  
   
 run Dogo::Server.new
```

  

Agora é só iniciar o servidor! Em modo de desenvolvimento, basta executar `rackup`.

  

O servidor Sinatra responde a alguns endpoints. O caminho raíz irá redirecionar para a URL definida em `Dogo.default_url`.

  

Para encurtar uma URL, você pode executar o comando `curl 'http://fnando.me/shorten?api_key=abc&url=http://codeplane.com`. Note que estou usando o verbo HTTP `GET` para criar a URL (OMG! REST! OHNOES!). Isso é necessário para funcionar com o [Tweetbot](http://tapbots.com), cliente de Twitter que uso tanto no Mac, quanto no iPhone.

  

Finalmente, a URL original pode ser acessada através do endereço  `http://fnando.me/<id>`.

  

O Dogo faz a contagem de cliques em cada URL. Estes contadores são armazenados em uma chave `clicks.<id curto>`. No futuro, quero adicionar um dashboard que irá exibir isso com alguns gráficos e coisas do tipo, mas tudo vai depender da preguiça (ou da falta dela).

  
   
   
 from Simples Ideias <http://simplesideias.com.br/criando-seu-proprio-encurtador-de-urls>
