---
url: "http://imasters.com.br/artigo/23877/ruby/como-implementar-uma-aplicacao-cliente-servidor-usando-sockets-em-ruby"
captured_at: "2012-03-19T11:28:34-03:00"
title: "Como implementar uma aplicação cliente-servidor usando Sockets em Ruby"
domain: "imasters-com-br"
---

### Sent to you by Thiago Silva via Google Reader:

## 

[Como implementar uma aplicação cliente-servidor usando Sockets em Ruby](http://feedproxy.google.com/~r/imasters/~3/yA-UTZK4jOA/story01.htm)

via [iMasters -](http://imasters.com.br/) by Samuel Vinicius () on 3/19/12

  

Este é primeiro de vários artigos que irei publicar sobre Sockets em Ruby. Mas antes de qualquer coisa, é conveniente dizer o que são Sockets:

> A grosso modo, são as extremidades de um canal de comunicação bidirecional. Ou seja, você pode utilizar Sockets para fazer comunicação entre processos de uma máquina, entre máquinas diferentes e entre processos de máquinas diferentes.

**O que iremos fazer?**

Como este é o primeiro artigo sobre o tema, pretendo ir direto ao ponto, mostrando, de forma simples, como implementar uma aplicação cliente-servidor. Nela, o cliente envia uma mensagem para o servidor e este responde. Sendo a comunicação entre cliente e servidor realizada via Socket, através do protocolo TCP.

Então, sem mais delongas. Vamos aos códigos:

#### Servidor

```
# file server.rb  
require 'socket'   
  
server = TCPServer.open(3001) # Abre socket em escuta na porta 3001   
loop { # o servidor nunca morre, fica sempre executando  
 client = server.accept # aceita conexão do cliente  
 msg_cliente = client.recvfrom( 10000 ) # recebe mensagem - 10000 bytes - do cliente  
  
 puts "Mensagem do cliente: #{msg_cliente}" # imprime a mensagem do cliente no servidor  
 client.puts "Ola cliente eu, o servidor, recebi sua mensagem" #envia uma mensagem ao cliente   
 client.close # fecha conexão  
}
```

#### Cliente

```
# file client.rb  
require 'socket'  
  
server = TCPSocket.open('localhost', 3001) # conecta ao servidor na porta 3001  
server.puts "Ola servidor eu, o cliente, estou enviando uma mensagem" # envia mensagem para o servidor  
  
resp = server.recvfrom( 10000 ) # recebe a mensagem -10000 bytes - do servidor  
puts resp  
  
server.close # Fecha a conexão com o servidor
```

#### Como rodar a aplicação?

Primeiro, salve o código do servidor em um arquivo .rb - por exemplo server.rb - e execute o arquivo - ruby server.rb. Neste ponto, o servidor está esperando a conexão de um cliente. Agora salve o código do cliente de forma análoga e execute em outro terminal de modo que cliente e servidor sejam rodados ao mesmo tempo. A partir de então, o cliente envia uma mensagem ao servidor e o servidor responde.

Este é um exemplo simples do que pode ser feito com Sockets, espero que te ajude em algo.

\*\*\*

*Referência: <http://www.tutorialspoint.com/ruby/ruby_socket_programming.htm>*

[anexo ausente]

|  |  |
| --- | --- |
| [9bcafcd24ef5e7a319a7e300c0d5b221.gif](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&title=Como+implementar+uma+aplica%C3%A7%C3%A3o+cliente-servidor+usando+Sockets+em+Ruby&link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F23877%2Fruby%2Fcomo-implementar-uma-aplicacao-cliente-servidor-usando-sockets-em-ruby) | [75b9131ce15803402621ad7d693d4dd1.gif](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Como+implementar+uma+aplica%C3%A7%C3%A3o+cliente-servidor+usando+Sockets+em+Ruby&link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F23877%2Fruby%2Fcomo-implementar-uma-aplicacao-cliente-servidor-usando-sockets-em-ruby) |

  
  
[[anexo ausente]](http://da.feedsportal.com/r/129200595819/u/49/f/546640/c/33212/s/1d937fd4/kg/312/a2.htm)[anexo ausente][anexo ausente]

  

### Things you can do from here:

- [Subscribe to iMasters -](http://www.google.com/reader/view/feed%2Fhttp%3A%2F%2Fimasters.uol.com.br%2Ffeed%2F?source=email) using **Google Reader**
- [Get started using Google Reader](http://www.google.com/reader/?source=email) to easily keep up with **all your favorite sites**
