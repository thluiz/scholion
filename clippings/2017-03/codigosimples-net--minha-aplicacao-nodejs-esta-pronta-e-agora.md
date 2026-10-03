---
url: "https://codigosimples.net/2017/03/21/minha-aplicacao-nodejs-esta-pronta-e-agora/"
captured_at: "2017-03-21T17:02:17-03:00"
title: "Minha aplicação NodeJS está pronta! E agora? - Código Simples .NET"
domain: "codigosimples-net"
---

# Minha aplicação NodeJS está pronta! E agora?

 [0](https://codigosimples.net/2017/03/21/minha-aplicacao-nodejs-esta-pronta-e-agora/#respond)

Fala galera, meu primeiro post aqui no codigosimples.net e gostaria de falar com vocês sobre o deploy de aplicações NodeJS. Mais especificamente sites que utilizam esse poderoso framework.

Tudo muito bom, tudo muito bem, mas chegamos num ponto onde precisamos colocar nossa aplicação pra rodar fora de nosso ambiente de desenvolvimento, e hoje vou compartilhar com vocês o que eu tenho feito nesses últimos anos em que me dediquei a tecnologias open source.

Minha intenção não é mostrar o desenvolvimento ou arquitetura de uma aplicação desenvolvida em NodeJS, mas sim demonstrar como disponibilizar uma aplicação dentro de um servidor web. Para isso explicarei algumas tecnologias envolvidas e farei um passo-a-passo para o deploy.

Para isso utilizaremos o seguinte:

- Linux Ubuntu 16
- NGINX como servidor web
- NodeJS
- Forever

### NGINX

Como descrito em seu site ([http://www.nginx.com](http://www.nginx.com/)), o NGINX é um servidor web e proxy reverso, free, open-source e de alta performance. Pode ser usado como servidor de e-mail e é facilmente escalável e configurável. Nos últimos anos ele tem se tornado uma ótima alternativa ao tradicional servidor Apache, que na minha opinião requer muito conhecimento para uma configuração confiável. Veremos o quanto é simples configurar o NGINX para passar a responder requisições, trabalhando muito bem em conjunto com o NodeJS.

Primeiramente teremos que instalá-lo em nosso servidor Linux:

```
1

2

3

apt-get update

apt-get install nginx
```

Após a instalação iniciaremos a configuração do nosso site:

```
1

2

nano /etc/nginx/nginx.conf
```

Não entrarei em todos os detalhes da configuração do NGINX, vou diretamente ao ponto da criação da configuração de nossa aplicação. Localize a seguinte linha no arquivo de configuração:

```
1

2

include /etc/nginx/sites-enabled/*;
```

Insira o seguinte bloco de código imediatamente abaixo da linha acima. Vou detalhar cada linha desse bloco:

```
1

2

3

4

5

6

7

8

9

10

11

12

13

server {

listen 80;

server_name seudominio.com.br;

location / {

proxy_pass http://127.0.0.1:8000;

}

location /static {

root /caminho_para_a_pasta_da_aplicacao/public;

}

}
```

Na linha 1 abrimos o bloco de configuração chamado server.

Na linha 2 informamos a porta a ser utilizada para nossa aplicação.

Na linha 3 definimos o nome do host que será utilizado para identificar nossa aplicação quando solicitada no NGINX.

Na linha 5 configuramos o nosso proxy reverso apontando para o localhost do servidor e a porta onde nossa aplicação NodeJS responderá.

Na linha 9 configuramos o caminho para a pasta de conteúdo estático da aplicação. Essa pasta geralmente coloco os arquivos CSS, JavaScript, Imagens, etc.

Após isso podemos testar a configuração do NGINX para verificar erros que impossibilitarão a execução do mesmo. Para isso digite o seguinte comando:

```
1

2

nginx -t
```

Se estiver tudo certo com o arquivo de confguração, será retornado o seguinte:

```
1

2

3

nginx: the configuration file /etc/nginx/nginx.conf syntax is ok

nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Agora podemos reiniciar o nosso servidor NGINX para que as alterações feitas no arquivo tenham efeito:

```
1

2

service nginx restart
```

### Instalando o NodeJS

Com nosso NGINX configurado e funcionando, vamos instalar o NodeJS

```
1

2

3

4

curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -

sudo apt-get update

sudo apt-get install -y nodejs
```

Para verificarmos a versão do NodeJS instalada executamos o seguinte comando:

```
1

2

node -v
```

Pronto, NodeJS instalado com sucesso!

### Instalando o NPM

O NPM é um gerenciador de pacotes JavaScript, para mais informações visite <https://www.npmjs.com/> . Ele será necessário para obter o pacote Forever que instalaremos mais a frente.

Para instalar o NPM executamos o seguinte comando:

```
1

2

apt-get install -y npm
```

Verificando a versão instalada:

```
1

2

npm -v
```

Feito, NPM instalado!

### Instalando o Forever

O Forever (<https://www.npmjs.com/package/forever>) é uma ferramenta bem simples que permite executar scripts continuamente.

Para instalar:

```
1

2

npm install forever -g
```

O parâmetro -g garante que o Forever ficará disponível globalmente em nosso servidor.

Existem vários parâmetros disponíveis no Forever, vamos focar em apenas quatro deles: start, restart, stop e list.

Com o start iniciamos a execução de um script, que em nosso caso será nossa aplicação. Vejamos como é simples:

```
1

2

forever start /caminho_da_sua_aplicacao/arquivo_inicial.js
```

Onde arquivo\_inicial.js é o arquivo que contém a sua aplicação.

Como retorno desse comando o Forever nos indicará o arquivo de log. Nesse arquivo serão gravados todos logs que sua aplicação emitir durante o ciclo de vida. Isso ajudará muito no caso de exceções ou paradas inesperadas.

Por default o Forever reinicia a aplicação automaticamente no caso de alguma exceção não tratada acontecer. Isso ajuda a manter sua aplicação no ar se algo que você não esperava acontecer. Por isso é sempre importante a revisão do arquivo de log do Forever.

Para listar todas as aplicações que estão rodando através do Forever executamos o seguinte comando:

```
1

2

forever list
```

Veja que temos um retorno de todas as aplicações iniciadas e um id como de um array. Para executar operações de stop e restart utilizaremos esse id.

Reiniciando uma aplicação:

```
1

2

forever restart 0
```

Parando uma aplicação:

```
1

2

forever stop 0
```

### Conclusão

Com a aplicação rodando no Forever podemos acessar o domínio configurado no NGINX e ver a aplicação rodando no browser.

Lembrando que o Forever não aceita somente aplicações web, você pode ter um script que faça qualquer tipo de trabalho rodando continuamente, por exemplo, um robô que trabalhe automatizando alguma tarefa.

É isso, espero que tenham gostado e que seja útil! Até a próxima pessoal!
