---
url: "https://nandovieira.com.br/redirecionando-uma-porta-local-para-um-servidor-remoto-com-ssh"
captured_at: "2013-01-21T12:09:01-03:00"
title: "Redirecionando uma porta local para um servidor remoto usando SSH"
domain: "nandovieira-com-br"
---

Se você já teve que fazer alguma integração com serviços externos como o PayPal, por exemplo, já deve ter sentido a necessidade de expor algum serviço de sua máquina local na internet. Existem diversos serviços que permitem fazer isso, como o [localtunnel](http://localtunnel.com) e [forward](http://forwardhq.com).

  

Eu costumava usar o localtunnel pelo fato de ser gratuito, mas ele é muito lento. E pagar por um serviço desse tipo, onde só preciso expor serviços exporadicamente não faz muito sentido. Além disso, no caso do localtunnel pelo menos, se sua conexão cai, você receberá um novo endereço ao se reconectar. Isto nem sempre é um problema, mas às vezes é preciso configurar o serviço que está testando com esta nova URL (como é o caso do PagSeguro), o que não é nada prático.

  

Existe uma maneira muito simples de fazer isso usando SSH e um servidor web. E como uso o servidor do Simples Ideias como um playground, vou mostrar como foi simples fazer isso usando [NGINX](http://nginx.org).

  

Depois de ter instalado o NGINX, você só precisa criar um novo arquivo de configuração de host, como no exemplo abaixo.

  

```
 upstream tunnel {  
   server 127.0.0.1:3000;  
   server 127.0.0.1:1234;  
   server 127.0.0.1:9292;  
   server 127.0.0.1:4567;  
 }  
   
 server {  
   listen 80;  
   server_name dev.simplesideias.com.br *.dev.simplesideias.com.br;  
   client_max_body_size  10M;  
   
   location / {  
     proxy_set_header  X-Real-IP  $remote_addr;  
     proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;  
     proxy_set_header Host $http_host;  
     proxy_redirect off;  
   
     proxy_pass http://tunnel;  
   }  
 }
```

  

A primeira coisa que você deve notar é que estou usando um bloco `upstream`, que permite definir os servidores que o NGINX usará para responder à requisição (na prática, você irá configurar o NGINX como um load balancer). Neste caso, adicionei as portas que normalmente uso para Rails, Node.js, Rack e Sinatra.

  

Outra coisa que você deve notar é que este servidor responderá a qualquer requisição no subdomínio `*.dev.simplesideias.com.br`. Isso é muito interessante se você também precisa testar apps que usam subdomínios. Para configurar o seu [servidor de DNS](http://dnsimple.com), basta criar um registro `ALIAS` (registro próprio da DNSimple) como o abaixo.

  

![](http://media.simplesideias.com.br/dnsimple-dev-simplesideias.png)

  

Após reiniciar o servidor, você já poderá redirecionar a porta local de sua máquina para este servidor remoto. Imagine que eu queira redirecionar a porta 3000 do Rails. Neste caso, basta executar o comando abaixo na máquina local:

  

```
 ssh simplesideias.com.br -R 3000:localhost:3000
```

  

Este comando diz que vou redirecionar a porta `localhost:3000` para a porta `3000` do servidor `simplesideias.com.br`. Note que neste caso não é preciso ter nenhuma permissão especial, já que a porta é maior que 1024.

  

Simples, e funciona que é uma maravilha! ;)

  
   
   
 from Simples Ideias <http://simplesideias.com.br/redirecionando-uma-porta-local-para-um-servidor-remoto-com-ssh>
