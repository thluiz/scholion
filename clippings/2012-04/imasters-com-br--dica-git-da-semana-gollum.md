---
url: "https://imasters.com.br/desenvolvimento/dica-git-da-semana-gollum"
captured_at: "2012-04-20T13:13:16-03:00"
title: "Dica Git da semana: Gollum"
domain: "imasters-com-br"
---

A dica Git desta semana é um pouco fora do assunto, e fala sobre o Gollum, um wiki baseado no Git.

  

#### Wikis

  

Wikis têm estado ao nosso redor por mais de 15 anos, e ser capaz de editar uma página a partir de qualquer localização tem sido um grande poupador de tempo na geração de documentação. A maior parte do [guia do usuário EGit](http://wiki.eclipse.org/EGit) foi criada através da utilização de contribuições wiki.

  

Um problema com a maioria dos wikis é que você precisa estar online para interagir com eles. (Existem alguns clientes que fazem o cache de páginas da Wikipédia para leitura offline, mas eles não são capazes de gerenciar mudanças.) Não seria ótimo se pudéssemos ter um sistema que permitisse editar wikis offline, e incorporasse nossas mudanças de volta quando estivéssemos conectados novamente?

  

#### Gollum

  

Insira o [Gollum](https://github.com/github/gollum) daquelas pessoas finas no [GitHub](https://github.com/). Este é um servidor wiki implementado com ruby que permite a você visualizar, editar e salvar documentos em um wiki em sua máquina local. (Já [faz um tempo](https://github.com/blog/699-making-github-more-open-git-backed-wikis) que está por aí, mas não é amplamente conhecido, por algum motivo.)

  

Como é do GitHub (e este artigo é sobre dicas de Git), então não deve ser nenhuma surpresa que o Gollum é um servidor wiki para páginas wiki apoiadas por um repositório git. Cada gravação corresponde a um commit individual no repositório, e a caixa "escrever uma mensagem de mudança" na parte inferior é traduzida para a mensagem Git commit.

  

Cada página wiki é traduzida para uma página especificada no diretório *--page-file-dir* (ou no repositório raiz, se não estiver definido). Além disso, a marcação é configurável pelo usuário e os padrões com base no tipo de extensão (o padrão para novas páginas é [Markdown](http://daringfireball.net/projects/markdown/)). Alguns formatos wiki, como [MediaWiki](http://www.mediawiki.org/wiki/MediaWiki), também são suportados, enquanto outros, como confluence, não são. Na verdade, o formato multi- é suportado através de [Jekyll](https://github.com/mojombo/jekyll), então quaisquer formatos suportados provavelmente podem ser usados.

  

#### Instalado e funcionando

  

Instalar o Gollum é fácil, desde que você tenha o Ruby instalado (o que você fará, se você tem OSX). Você pode executar:

  

```
 sudo gem install gollum
```

  

...o que irá instalá-lo no caminho do seu sistema automaticamente, ou sem o *sudo* para instalar em um caminho por usuário (que no OSX está em *~/.gem/ruby/1.8/bin*, que você terá que adicionar ao seu caminho, se deseja executar a partir da linha de comando).

  

Uma vez instalado, você pode criar um repositório, iniciar o Gollum, abrir um navegador web, e estará pronto:

  

```
 git init TestWiki gollum --page-file-dir wiki TestWiki openurl http://localhost:4567
```

  

Isso cria um novo wiki (para fins de teste) e dispara o servidor Gollum, apontando para o repositório Git. Nós especificamos *wiki* como subdiretório, de modo que, quando comitamos um arquivo, estamos escrevendo-o em *TestWiki/wiki/PageName.md*.

  

#### Formatos

  

Há muitos tipos diferentes de formatos que são suportados pelo Gollum, mas parsers devem ser instalados separadamente, a fim de ver qualquer conteúdo wiki processado como você espera.

  

Markdown *gem install rdiscount*

  

MediaWiki *gem install wikicloth*

Se você deseja imprimir o código de forma atraente, pode usar Pygments com *sudo easy\_install pygments*. Isso permite que você comece o código com ```java e termine com *```* para imprimir de forma atraente o trecho de código embedded.

  

Então, se você tentar editar uma página e a marcação não estiver sendo processada adequadamente, verifique se você tem um render apropriado para funcionar.

  

#### Identidade

  

Commits do Git no repositório utiliza as credenciais que estão associadas com o usuário que lançou o Gollum. Enquanto isso funciona para projetos abertos, se você quiser ter um usuário gravado de algum tipo de SSO, você precisa integrar isso. O Gollum usa o [Ruby](http://www.sinatrarb.com/) Sinatra para gerar o front-end baseado na web, e isso é usados para determinar se a autenticação é utilizada ou não (veja o [FAQ](http://www.sinatrarb.com/faq.html#auth)).

  

No entanto, ele não suporta passagem da identidade do committer de dentro dos commits ou usando as variáveis *GIT\_AUTHOR\_EMAIL* ou *GIT\_COMMITTER\_EMAIL* (embora isso seja um problema com *Grit*, o Ruby front-end para o repositório Git)). Isso, combinado com a falta de suporte para multi-projeto o limita um pouco para usos produtivos, mas funciona bem para um wiki local (único usuário).

  

#### Resumo

  

O Gollum oferece um mecanismo poderoso baseado na web para editar páginas wiki em um repositório git local, usando as credenciais de commit do usuário local. Isso permite que um wiki distribuído seja editado remotamente (enquanto desconectado), mas gerenciado meio disfarçado pelo Git, incluindo a capacidade de branch, tag e pushing distribuído.

  

Apesar de sua deficiência em alguns importantes casos de uso que fazem um wiki distribuído para equipes de usuários, para um wiki anônimo (ou um em que as credenciais do committer são de menor importância), é um sistema incrivelmente fácil de começar a trabalhar. E para aqueles que escrevem regularmente enquanto desconectados, pode ser uma boa maneira de construir um repositório de informações sem a necessidade de estar conectado, e ainda assim permitir que essas alterações sejam incorporadas a um repositório quando reconectado.

  

*⁂*

  

*Texto original disponível em <http://alblue.bandlem.com/2011/05/git-tip-of-week-gollum.html>*

  
  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](imasters-com-br--dica-git-da-semana-gollum/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Dica+Git+da+semana%3A+Gollum&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24163%2Fdesenvolvimento%2Fdica-git-da-semana-gollum)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](imasters-com-br--dica-git-da-semana-gollum/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Dica+Git+da+semana%3A+Gollum&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24163%2Fdesenvolvimento%2Fdica-git-da-semana-gollum)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/132309390635/u/49/f/546640/c/33212/s/1e92f214/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
  
from iMasters - <http://imasters.com.br/artigo/24163/desenvolvimento/dica-git-da-semana-gollum>
