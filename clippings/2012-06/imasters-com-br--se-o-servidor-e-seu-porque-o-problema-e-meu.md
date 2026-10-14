---
url: "http://imasters.com.br/artigo/24862/java/se-o-servidor-e-seu-porque-o-problema-e-meu"
captured_at: "2012-06-29T12:06:59-03:00"
title: "Se o servidor é seu, porque o problema é meu?"
domain: "imasters-com-br"
---

Vamos falar um pouco sobre administração em aplicativos e servidores Java, que serve também no geral para outros serviços. Desde que assumi a gerência da Integrator na parte de hospedagem, vejo e-mails que são direcionados ao suporte e recebo, também, muitos pedidos que, sinceramente, não deveriam vir de um desenvolvedor Java.

  

A crítica que faço aqui é construtiva e, de certa forma, um puxão de orelha para que os profissionais que trabalham com desenvolvimento comecem a se preocupar mais com o que criaram e assumam o problema.

  

#### Criei meu aplicativo e agora?

  

Tudo começa com a sua criação. Você, profissional desenvolvedor, recebeu a árdua tarefa de criar aquele sistema “maravilhoso“ que alguém idealizou ou, por motivos pessoais, quis aprender algo ou desenvolver o sistema de seus sonhos.

  

Depois de muita luta, você desenvolveu e foi aprovado pelo seu cliente, pela diretoria da empresa onde trabalha ou por você. Mas e agora? Como executar isto fora de minha máquina de desenvolvimento?

  

#### Do desenvolvimento até a produção

  

Muitos desenvolvedores se acostumaram com a automação das ferramentas de desenvolvimento e, claro, com tanta facilidade. Parar e iniciar o serviço Java ali é simples.  Entretanto, o desenvolvedor Java não pode apenas saber como operar uma ferramenta de desenvolvimento.

  

O profissional de Java precisa - na realidade necessita - conhecer o servidor Java que executa seus aplicativos. Não é apenas o básico de instalar, configurar, iniciar e parar. Também não vale dizer que sabe ler logs. Vai além... O profissional Java precisa saber como o servidor Java escolhido opera. Isso vai desde as suas características básicas de configuração, até como ele pode ser modificado e otimizado para melhorar o desempenho do que desenvolveu.

  

Está bem, você vai dizer que não é administrador, mas sim é um desenvolvedor, certo? Errado! Isto é comum no governo, onde um carimba e outro coloca a folha. Se olhar para fora, verá que muitos fazem várias tarefas diferentes. E no seu caso, o servidor Java é a extensão do seu aplicativo.

  

#### O aplicativo precisa funcionar em qualquer lugar

  

Se você é o desenvolvedor, logo, é importante saber como fazer para que o seu aplicativo funcione em qualquer lugar, não somente em sua máquina. Usar o framework XYZ não é a etapa final do que criou. É no momento que ele vai para produção, que é onde aparecerão os problemas.

  

O que mais vejo e escuto é a frase: na minha máquina funciona. Ora, se você desenvolve corretamente, sem nenhum problema oculto, nada personalizado especificamente para sua máquina, o que causaria erros online, também funciona em qualquer lugar.

  

Estes são os problemas mais comuns do desenvolvimento para a produção:

  

1. Nome do banco de dados – criar a conexão usando um nome local, onde na produção se modifica, bate o recorde em erros de acesso pelo usuário;

     

   Nome do usuário do banco de dados – no segundo problema mais comum, o usuário é diferente e gera erro de acesso negado;

     

   Permissões de acesso em arquivos – é o terceiro mais comum. Quem usa o Windows está muito acostumado a ter permissão para tudo, mas online, servidores seguros tem permissões para escrita e execução, que precisam ser dadas em arquivos e diretórios;

     

   Erro no local onde está o banco de dados – conhecer a regra de como acessar o banco de dados no servidor de produção é o mínimo; vai desde do host até a porta. Não vá colocando o que “acha” ser o correto. Na dúvida, sempre pergunte a quem administra o sistema operacional para evitar erros e mudar, principalmente, no código que foi compilado para colocar em produção;

     

   Problemas de memória – usar o framework XYZ porque ele foi indicado na comunidade é ótimo. Mas saber o que ele consome de sua máquina é melhor ainda. Não adianta achar que sabe como usar o Tomcat, que localmente tudo funciona, que online não vai dar problemas, se você nem sabe localmente o quanto o Tomcat necessita de memória para executar seu aplicativo. Máquina de desenvolvimento possuem vários GIGAS de memória RAM e muitas vezes o desenvolvedor nem se preocupou em limitar o serviço em um X de memória. Online, você terá configurado uma limitação no servidor Java. É importante saber se, dentro desta limitação, seu aplicativo executa com conforto;

     

   Envio de email – o SMTP tem regras em qualquer lugar. Saber a porta correta e os parâmetros básicos mínimos necessários é importante para que, em produção, o envio seja feito sem erros.

     

   Erro 404 – o deploy não funcionou, logo, tem algo de errado. É preciso ver nos logs o que está ocorrendo;

     

   Bibliotecas – as bibliotecas usadas no desenvolvimento precisam estar em produção. Se exportou o WAR file, EAR file, e nenhum está com as bibliotecas, ou falta alguma (porque foram colocadas diretamente no servidor Java), precisa-se fazer o mesmo em produção. Algumas bibliotecas também costumam dar problema quando existem duas do mesmo tipo, mas com versões diferentes;

     

   Localização – não deveria estar nesta lista, mas infelizmente, é um erro também comum. É possível configurar o Locale em seu aplicativo ou diretamente no servidor Java. Não é porque na sua máquina o Locale é em pt-br que online vai ser também. Saber modificar isso no servidor Java que seja não é difícil e lhe salva de dores de cabeça com uma configuração muito simples;

     

   Erro na descompactação do arquivo WAR – probleminha comum quando você sobe por FTP o aplicativo com o Tomcat ligado, por exemplo, causando um hot deploy sem o arquivo ter finalizado totalmente o seu envio. Alternativamente, ocorreu alguma queda de pacote no envio e ocorreu uma falha, deixando o arquivo impossibilitado de ser operado e, consequentemente, o servidor Java lançará um erro na descompactação;

     

   Assumir o problema – é, eu sei, isto não se trata de erro de produção. Mas pensar é um ato importante para resolver problemas. Sair culpando o outro, sendo que o problema é seu, não faz parte do meio que escolheu como profissão. Se assumiu um cargo como desenvolvedor, assuma também que o que fizer pode ter falhas e que elas são corrigíveis. Assumir o problema é o primeiro passo em direção à solução.

#### Os logs são a chave para a solução dos problemas

  

Todos os problemas que relatei acima sempre lançam exceções. Claro que, muitas vezes, o desenvolvedor sai reclamando antes de pensar - que é sua maior tarefa - no porquê essas exceções estão sendo lançadas. A grande vantagem do Java é que ele aponta o dedo para o problema. E com o número de usuários no mundo, é muito fácil descobrir uma resposta para o problema. Mas fica mais difícil se quiser que resolvam o SEU problema para você, acredite.

  

#### Indo além dos servidores Java

  

Em produção, não basta apenas saber como operar um servidor Java. Você desenvolveu o aplicativo e, como conhecedor do que fez, deve também saber que o seu uso pode crescer. Mas, muitas vezes, se esquece de que o comportamento com dez pessoas testando é um e com centenas online, é outro.

  

Um belo dia, seu servidor Java caiu - se não caiu, deu um erro estranho em seu aplicativo ou aconteceu algo que não havia previsto. Mas a culpa não é sua, certo? Funcionava antes e não mexi em nada. Errado! Totalmente sua culpa. Só de dar a resposta de que não mexeu em nada já implica que não está cuidando do que fez. Se não observar por um tempo o que desenvolveu e a sua evolução, não vai ter correções e, como consequência, erros. Saiba estes princípios básicos no desenvolvimento:

  

1. Bibliotecas e frameworks mudam – se mudam de versão, é porque a anterior não era perfeita. Erros são reportados e precisam ser atualizados para evitar que no seu, uma hora ocorra o que o outro já teve;

     

   Servidores Java mudam – mesma situação que citei acima. Se mudou a versão do servidor Java, pode ser que algum possível bug pode causar problemas em seu aplicativo;

     

   Profiler – usar um profiler vai lhe orientar em como seu aplicativo se comporta e ver possíveis picos de memória/CPU que possam lhe causar problemas, mais adiante, com muitos usuários acessando.

#### Atacando o problema de frente

  

Evidentemente, muitas são as situações que ocorrem em aplicativos. Nem todos os problemas são simples de serem solucionados, mas alguns são.

  

1. Otimize o banco de dados – conhecer queries lindas com subqueries é muito bom. Mas saber o que elas causam, ao serem chamadas em bancos de dados, com muitos dados, é melhor ainda. Otimizar queries é importante para melhorar o desempenho. Claro que, em meio a isto, entram também saber otimizar a estrutura das tabelas, criar índices corretos e até mesmo criar caches de queries de pesquisas para melhorar o seu desempenho no acesso ao aplicativo;

     

   Modificar o comportamento falho do aplicativo – sim, sei que você não quer mexer no que estava funcionando bem nos primeiros 10.000 registros/acessos. Mas agora não está mais. Muita gente acessando, muitos erros sendo lançados, memória, velocidade. Precisa modificar o comportamento, voltar para a “prancheta” do desenvolvimento e replanejar. Se não fizer isto, seu projeto vai falhar, mais dia ou menos dia;

     

   Mude de servidor Java – sei que você aprendeu agora, e muito bem, aquele servidor chamado Apache Tomcat. Mas ele pode não estar dando conta do recado como outro daria. É hora de conhecer novos servidores Java e testar, seja o Jetty, JBoss ou GlassFish. Algumas pequenas mudanças, como a troca de servidor Java, podem trazer benefícios ao que desenvolveu, mesmo que isto lhe traga de volta ao “be a bá” de como tudo funciona;

     

   Buscar alternativas – sempre, em algum lugar deste planeta imenso do desenvolvimento, alguém arrumou alguma solução que  fez melhorar o desempenho do aplicativo com aquela tecnologia XYZ que escolheu e deu a dica. Busque alternativas e dicas.

#### Empurrão ou puxão de orelha?

  

Minha intenção é dar a vocês, leitores, um empurrão no sentido certo. Existem várias etapas no desenvolvimento e todas envolvem o que criou. Vai desde o sistema operacional que irá trabalhar em produção, até o que é acessado pelo seu aplicativo. Estes detalhes precisam ser todos analisados, mesmo que você diga que é apenas um mero desenvolvedor Java.

  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](imasters-com-br--se-o-servidor-e-seu-porque-o-problema-e-meu/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Se+o+servidor+%C3%A9+seu%2C+porque+o+problema+%C3%A9+meu%3F&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24862%2Fjava%2Fse-o-servidor-e-seu-porque-o-problema-e-meu)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](imasters-com-br--se-o-servidor-e-seu-porque-o-problema-e-meu/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Se+o+servidor+%C3%A9+seu%2C+porque+o+problema+%C3%A9+meu%3F&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24862%2Fjava%2Fse-o-servidor-e-seu-porque-o-problema-e-meu)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/138509694804/u/49/f/546640/c/33212/s/20d8c2ae/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
from iMasters - <http://feedproxy.google.com/~r/imasters/~3/FoLUG6qWqq8/story01.htm>
