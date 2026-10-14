---
url: "http://imasters.com.br/tecnologia/seguranca/robots-txt-pode-ser-seu-inimigo-contra-a-seguranca"
captured_at: "2012-12-17T14:55:51-03:00"
title: "Robots.txt pode ser seu inimigo contra a segurança"
domain: "imasters-com-br"
---

O arquivo Robots.txt se trata de um arquivo .txt que Webmasters e SEOs utilizam para informar aos Crawlers (sites de pesquisas) as permissões de acesso a páginas e diretórios e é neste ponto que mora o perigo do Robots.txt.

  

## 1. Sintaxe

  

O Robots.txt possui a seguinte sintaxe:

  

### 1.1. User-agent

  

Responsável por definir qual user-agent (que seria o programa que está fazendo a leitura do seu site) deve ler o arquivo, por exemplo:

  

```
 User-agent: *: qualquer programa pode ler; User-agent: Googlebot; especifico para o google; User-agent: Slurp; especifico para o Yahoo; User-agent: msnbot.; especifico para o MSN
```

  

O site do [user-agents.org](http://www.user-agents.org/) possui uma lista com a relação de user-agents conhecidos, tanto para Crawlers quanto navegadores.

  

### 1.2. Disallow

  

Este comando informa quais diretórios ou paginas o Crawler não deve scannear.

  

### 1.3. Allow

  

Este comando informa quais diretórios ou páginas o Crawler deve scannear. Como por padrão, o Crawler escaneia todos os diretórios, você poderia realizar um bloqueio a um diretório e através do Allow liberar o acesso a um subdiretório.

  

## 2. Exemplo

  

Considere o seguinte exemplo:

  

```
 User-agent: * Disallow: /privado Allow: /privado/excecao Allow: /publico
```

  

Vamos conferir linha a linha:

  

```
 User-agent: * : informados que qualquer Crawler pode acessar o Robots.txt; Disallow: /privado : este diretório não deve ser scanneado; Allow: /privado/excecao : apesar de privado ser proibido, o sub-diretorio “excecao” pode ser scanneado. Allow: /publico : informa que este diretório pode ser scanneado.
```

  

## 3. Entendendo o problema de segurança

  

Até este ponto, estamos apenas configurando a permissão de acesso do Crawler, e aí que está o problema, pois um Cracker precisa conhecer os diretórios e a estrutura de um site, e o Robots pode dar um rumo para ele. Já encontrei Robots com caminhos de banco de dados, arquivos com informações de lista de e-mail, configurações, senhas, backups entre outras coisas.

  

Existem WebSpiders (programa que faz a leitura de sites da Internet de um modo específico, com um objetivo específico) que ficam lendo arquivos de Robots para identificar os diretórios onde a permissão foi negada a procure de arquivos importantes. Por exemplo, poderíamos configurar para que toda vez que encontrar um diretório negado, procurar por arquivos de bando de dados.

  

## 4. Corrigindo o problema de segurança

  

Mas se não podemos utilizar o Robots para informar os diretórios, como podemos fazer isso? Existe uma tag HTML Robots que configura este acesso, porém, como esta fica dentro da página, não informa ao Cracker tão facilmente, e ele deve saber o caminho de alguma outra forma.

  

Segue exemplo da tag:

  

```
 <meta Name=”robots” content=”noindex,nofollow”>
```

  

No parâmetro content, temos duas informações:

  

noindex: opção que solicita para não indexar a página nas pesquisas;

  

nofollow: opção que diz para o *Crawler* dos buscadores não seguir o link.

Também podemos informar em tags de link que o Crawler não deve indexar ele através da propriedade “*rel*”. Segue exemplo:

  

```
 <a href="login " rel="nofollow">Efetuar Login</a>
```

  

Neste exemplo, informamos que o link “login” não deve seguido. Todas essas configurações podem tomar um tempo maior na hora que criamos nossas aplicações, mas com isso temos um site um pouco mais seguro.

  

Vale lembrar que essas configurações não irão proteger os nossos arquivos do site, apenas vamos dificultar o trabalho do Cracker. Jamais deixe um arquivo de banco de dados ou qualquer outro com informações confidenciais em um caminho que pode ser acessado através de uma URL.

  

Alguns servidores e aplicações possuem diretórios protegidos que não podem ser acessados através de URL. Em .NET. por exemplo, quando criamos uma aplicação web, temos a pasta “App\_Data” que não pode ser acessada pela URL, apenas através da própria aplicação.

  

Outra forma seria configurarmos para que alguns diretórios, quando acessados via URL, fossem encaminhados para outras páginas ou retornar como uma página não encontrada.

  

Existem empresas de hospedagem que trabalham com diretórios abaixo do diretório do site. Por exemplo:

  

Temos o site no seguinte diretório: ”D:/SeuSite/Web/” onde fica a sua aplicação web e também tempos o diretório “D:/SeuSite/Dados/” que se trata de um diretório totalmente a parte da sua aplicação web, logo, seus arquivos restritos poderiam ser adicionados neste diretório e estariam “protegidos” neste caso.

  

Com isso, ficamos por aqui. Dúvidas, sugestões e críticas são bem vindas.

  

Obrigado a todos e bons códigos.

  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](imasters-com-br--robots-txt-pode-ser-seu-inimigo-contra-a-seguranca/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Robots.txt+pode+ser+seu+inimigo+contra+a+seguran%C3%A7a&amp;link=http%3A%2F%2Fimasters.com.br%2Ftecnologia%2Fseguranca%2Frobots-txt-pode-ser-seu-inimigo-contra-a-seguranca)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](imasters-com-br--robots-txt-pode-ser-seu-inimigo-contra-a-seguranca/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Robots.txt+pode+ser+seu+inimigo+contra+a+seguran%C3%A7a&amp;link=http%3A%2F%2Fimasters.com.br%2Ftecnologia%2Fseguranca%2Frobots-txt-pode-ser-seu-inimigo-contra-a-seguranca)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/151883677608/u/49/f/546640/c/33212/s/26b06f92/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
from iMasters <http://da.feedsportal.com/c/33212/f/546640/s/26b06f92/l/0Limasters0N0Bbr0Ctecnologia0Cseguranca0Crobots0Etxt0Epode0Eser0Eseu0Einimigo0Econtra0Ea0Eseguranca/ia1.htm>
