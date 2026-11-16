---
url: "https://dev.to/azure/melhorando-a-produtividade-no-home-office-com-o-vs-code-live-share-no-navegador-175b"
captured_at: "2026-11-16T01:47:05+00:00"
title: "Melhorando a produtividade no Home Office com o VS Code Live Share no navegador"
domain: "dev-to"
---

Nos últimos dias vimos um **enorme** crescimento do trabalho remoto! Porém muitos times remotos tem uma grande dificuldade em unir seus esforços já que suas ferramentas podem ser diferentes. Pensando nisso o [Visual Studio Code](https://code.visualstudio.com/?WT.mc_id=devto-blog-ludossan) aprimorou uma funcionalidade que irá facilitar **muito** o trabalho remoto entre times diferentes dentro da mesma organização e até mesmo pessoas sem nenhum vínculo direto!

## [](#live-share)Live Share

Muitos já conhecem o [VS Code Live Share](https://dev.tolivesharelink/), uma forma sensacional de compartilhar o seu IDE com outras pessoas para fazer _pair_ ou _group programming_.

Com o [Live Share](https://docs.microsoft.com/en-us/visualstudio/liveshare?WT.mc_id=devto-blog-ludossan) podemos não só compartilhar o nosso editor atual e permitir que outras pessoas não só vejam o que estamos fazendo, mas também que comentem, editem ao mesmo tempo, testem, executem e rodem _debugs_ no mesmo código em um mesmo local, em um mesmo IDE. Além disso, podemos também compartilhar nossa sessão no terminal para que todos os participantes possam realizar comandos, ou então apenas um modo _read only_, onde todos podem ver o que está acontecendo.

Com todas essas funcionalidades, o [Live Share](https://docs.microsoft.com/en-us/visualstudio/liveshare?WT.mc_id=devto-blog-ludossan) já é uma ferramenta sensacional que possibilita um trabalho muito mais produtivo e muito mais sincronizado com toda a equipe. Porém o grande problema era que todos precisavam ter o [VS Code](https://code.visualstudio.com/?WT.mc_id=devto-blog-ludossan) instalado na máquina para que isso fosse possível e, muitas vezes, isso era um grande impeditivo quando estávamos tentando fazer tutoriais ou então simplesmente mostrar um código rapidamente.

Esses problemas acabaram!

## [](#live-share-browser-session)Live Share Browser Session

O time do [VS Code](https://code.visualstudio.com/?WT.mc_id=devto-blog-ludossan) incrementou ainda mais a funcionalidade do [Live Share](https://docs.microsoft.com/en-us/visualstudio/liveshare?WT.mc_id=devto-blog-ludossan) permitindo que, agora, todos possam entrar em uma sessão de colaboração diretamente do **browser**! Isso mesmo, sem nenhum tipo de instalação nem nada! Você vai conseguir se juntar a outras pessoas do seu time em um editor _completo_ e tudo isso via seu browser preferido!

Isso é extremamente útil para times de empresas ou organizações diferentes, como terceiros que queiram mostrar algum código específico, mas não paramos apenas nos profissionais, para professores que desejam ensinar seus alunos, que muitas vezes não posuem um client de desktop instalado, esta é uma funcionalidade essencial para incrementar a sala de aula com imersão e interatividade!

## [](#como-entrar-em-uma-sess%C3%A3o-a-partir-do-browser)Como entrar em uma sessão a partir do browser

O caminho é bastante simples.

**1\. O _host_ da sessão inicia uma nova sessão**

Para começar, a pessoa que deseja compartilhar seu editor deve iniciar uma nova sessão do [Live Share](https://docs.microsoft.com/en-us/visualstudio/liveshare?WT.mc_id=devto-blog-ludossan) no seu client do [VS Code](https://code.visualstudio.com/?WT.mc_id=devto-blog-ludossan), da mesma forma que fazemos hoje.

![Iniciando uma sessão do Live Share](https://res.cloudinary.com/practicaldev/image/fetch/s--6d90efQG--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_800/https://user-images.githubusercontent.com/51928518/76938928-b814e300-68b4-11ea-923e-cefabd4688c6.gif)

**2\. Os convidados usam o link compartilhado para entrar pelo browser**

Uma vez iniciada a sessão, o [Live Share](https://docs.microsoft.com/en-us/visualstudio/liveshare?WT.mc_id=devto-blog-ludossan) vai gerar um link para ser compartilhado com possíveis convidados. Estes convidados clicam no link e entram na mesma tela de confirmação que tínhamos anteriormente, porém agora temos uma nova opção! A de entrar na sessão diretamente pelo navegador!

![Entrando em uma sessão pelo navegador](https://res.cloudinary.com/practicaldev/image/fetch/s--UWpHtU_g--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_800/https://user-images.githubusercontent.com/51928518/76941137-b8af7880-68b8-11ea-8228-41fdf4afd3ef.gif)

**3\. Uma experiência completa direto do navegador**

Uma vez dentro da sessão, o(s) convidados(s) podem usufruir de uma experiência completa, como se estivessem dentro do [VS Code](https://code.visualstudio.com/?WT.mc_id=devto-blog-ludossan) instalado em sua própria máquina

![Experiência completa com VS Code](https://res.cloudinary.com/practicaldev/image/fetch/s--Po-WkmIK--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_800/https://user-images.githubusercontent.com/51928518/76942009-40e24d80-68ba-11ea-885c-6eb1069ed550.gif)

## [](#e-como-eu-fa%C3%A7o-para-ter-isso)E como eu faço para ter isso?

Essa atualização é uma atualização imediata da [extensão do VS Code Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack&WT.mc_id=devto-blog-ludossan) então, se você já a está usando, não precisa fazer absolutamente nada! Todos os seus convidados para quaisquer possíveis sessões já vão ver a opção de conexão diretamente pelo browser!

Se você ainda não possui a [extensão](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack&WT.mc_id=devto-blog-ludossan), então basta baixar e instalar em seu editor e sair compartilhando seus códigos!

Saiba mais sobre essa novidade [na documentação oficial](https://docs.microsoft.com/en-us/visualstudio/liveshare/quickstart/browser-join?WT.mc_id=devto-blog-ludossan)

Não deixe de acompanhar mais do meu conteúdo no [meu blog](https://blog.lsantos.dev/?utm_source=devto&utm_medium=article&utm_campaign=live_share) e se [inscreva na newsletter](https://blog.lsantos.dev/signup?utm_source=devto&utm_medium=article&utm_campaign=live_share) para receber notícias semanais!
