---
url: "https://web.archive.org/web/20140705174939/http://imasters.com.br/linguagens/php/facilitando-a-consistencia-do-ambiente-de-desenvolvimento/"
captured_at: "2013-01-31T20:58:29-03:00"
title: "Facilitando a consistência do ambiente de desenvolvimento"
domain: "web-archive-org"
---

Cada desenvolvedor é diferente, mas o ambiente da sua equipe de desenvolvimento não tem que ser. Um web app moderno usa muitas tecnologias diferentes. As dependências comuns para um ambiente de desenvolvimento web em funcionamento incluem PHP e suas extensões necessárias, um servidor web, um banco de dados, frameworks de teste, e outros aplicativos e serviços. A abordagem clássica para auxiliar uma equipe de desenvolvedores é implementar um servidor e instalar todos os pacotes necessários para o desenvolvimento. Essa metodologia fornece um ambiente consistente para todos os desenvolvedores da equipe, garantindo que todos os colaboradores recebam a mesma experiência em todo o ciclo de desenvolvimento. No entanto, por mais consistente e homogêneo que um desenvolvimento remoto possa ser, desenvolver remotamente traz uma série de problemas, incluindo sacrifícios de velocidade e uma dependência desagradável de uma conexão confiável à Internet. É igualmente difícil de mexer com pacotes experimentais quando você sabe que eles poderiam afetar o ambiente de todos em sua equipe.

  

Navegar em um sistema de arquivo remoto para encontrar o arquivo que você deseja editar pode ser complicado. Muitos editores de texto e IDEs possuem características que tentam minimizar isso, mas eu nunca encontrei uma que funcionasse de forma confiável e comparável à velocidade do desenvolvimento local. Salvar um arquivo em uma rede pode apresentar atraso que se soma a uma quantidade significativa de perda de produtividade ao longo do tempo. Arquivo de navegação à parte, nada supera a velocidade de trabalhar localmente. Para trabalhar em sua máquina local, você tem que instalar todos os pacotes que a equipe está usando, e cada membro tem de fazer isso também. Essa abordagem apresenta inconsistência. Como desenvolvedores, nós buscamos consistência, velocidade, e, mesmo amando a Internet, gostaríamos de ser capazes de trabalhar sem ela às vezes. Então, o que vamos fazer? Nós construímos uma máquina dentro de uma máquina que funciona em todas as plataformas e garante a homogeneidade entre os ambientes de desenvolvimento.

  

Graças aos avanços na tecnologia de virtualização e da comunidade open source, existe uma série de ferramentas gratuitas para que qualquer um possa aproveitar as máquinas virtuais para a sua equipe.

  

## VirtualBox, Vagrant, e Puppet

  

Para começar, existem alguns aplicativos que são necessários. O [VirtualBox](https://www.virtualbox.org/) é um software de virtualização de hardware que permite que você execute outro sistema operacional em sua máquina local. Já o [Vagrant](http://www.vagrantup.com/) é um conjunto de scripts que permitem que você manipule facilmente essas máquinas virtuais a partir da linha de comando. E, por fim, o [Puppet](http://puppetlabs.com/) permite definir quais alterações de configuração devem ser feitas para que a máquina funcione da maneira que você deseja.

  

### Instale o VirtualBox

  

[Baixe](https://www.virtualbox.org/wiki/Downloads) e instale o VirtualBox. Agora você está pronto para instalar qualquer sistema operacional e executá-lo localmente.

  

### Instale oVagrant

  

O Vagrant é uma ferramenta de linha de comando para construir e distribuir ambientes de desenvolvimento virtualizados com VirtualBox. Executando apenas alguns comandos, você pode baixar e provisionar uma máquina virtual que combina com a de sua equipe.

  

Ruby e seu gerenciador de pacotes RubyGems são necessários para dar início ao Vagrant. Existem [instruções detalhadas](http://www.vagrantup.com/docs/getting-started/index.html) para ajudar.

  

Uma vez que Ruby e RubyGems estiverem instalados, execute o seguinte comando na sua máquina local para garantir que seus pacotes estejam atualizados.

  

```
 gem update --system
```

  

Para instalar o Vagrant, execute o seguinte comando em sua máquina local:

  

```
 gem install vagrant
```

  

### Configure o Vagrant

  

Supondo que tudo deu certo, a configuração do Vagrant deve ser fácil. Eu criei uma amostra *Vagrantfile* e uma uma configuração base em Puppet, a fim de provisionar uma máquina com Apache, MySQL, PHP, MySQL, Xdebug, PEAR, CodeSniffer PHP, e PHPUnit. Você pode clonar [meu repositório](https://github.com/phishy/lamp-stack).

  

Depois de ter clonado o repositório de exemplo, é hora de instalar a imagem de base do Vagrant. O seguinte comando fará o download da box via Internet e armazená-la em cache. É um download 300 MB, mas você só deve ter que fazer isso uma vez.

  

`vagrant box add base http://files.vagrantup.com/lucid32.box`

  

O próximo passo é modificar o seu Vagrantfile. Sua configuração vai encaminhar as portas de sua máquina local para a máquina virtual. Monte uma pasta local de sua escolha dentro de sua VM e inicialize o Puppet como seu provisioner padrão. Eu já fiz isso por você.

  

Há algumas diretrizes de configuração importantes no Vagrantfile. Vamos dar uma olhada.

  

```
 # This enables Puppet as the default provisioner config.vm.provision :puppet # For verbose output, and you wish to do a dry run, substitute this line config.vm.provision :puppet, [anexo ausente]  
   
  ptions => "--verbose --debug"
```

  

Uma vez que o provisionamento estiver completo, você irá acessar o ambiente LAMP do seu navegador por meio de <http://localhost:8080/.> A linha a seguir é a mágica que faz isso:

  

`config.vm.forward_port "http", 80, 8080`

  

Todo este exercício existe para trabalhar com arquivos locais que são servidos pela VM, e vamos precisar compartilhar um diretório local com a máquina. A linha a seguir monta a pasta chamada *www* no seu diretório home para DocumentRoot/var/www) do Apache na máquina virtual.

  

```
 config.vm.share_folder "www", "/var/www", "~/www"
```

  

Se optou por deixar essa configuração como está ou modificá-la, você pode inicializar a máquina virtual e começar provisionando-a com o seguinte comando em sua máquina local. Certifique-se de que você está no diretório que contém o Vagrantfile.

  

```
 vagrant up
```

  

(Se você receber uma stack dump e um erro de permissão, uma [explicação](https://github.com/mitchellh/vagrant/issues/580) está disponível.)

  

Vagrant inicializa a imagem base com o VirtualBox, e aí executa Puppet com a configuração localizada em *manifests/base.pp*. Comentei as linhas no arquivo *base.pp* para você entender melhor a sua função. Além disso, mantive a configuração bem simples. A configuração mais avançada vai exigir que você crie módulos que possam ser herdados, inclusive, parâmetrizados etc.

  

Para referência, aqui tem [mais documentação sobre as diretivas do Puppet](http://projects.puppetlabs.com/projects/puppet/wiki/Core_Types_Cheat_Sheet).

  

Muitos desenvolvedores também escreveram e compartilharam scripts do Puppet com o mundo. Aqui está uma [configuração LAMP mais complicada](https://github.com/saz/puppet-php).

  

Uma vez que a máquina estiver funcionando, se quiser fazer SSH para a máquina, você pode fazer assim:

  

```
 vagrant ssh
```

  

A fim de fazer SSH para a máquina sem o uso de Vagrant (por exemplo, ao criar um túnel para usar o cliente GUI MySQL), use a maior sintaxe:

  

```
 ssh vagrant@localhost -p 2222 (password: vagrant)
```

  

Existem poucas razões que você configurar a máquina virtual de dentro dela mesma. Conectar-se à máquina dessa forma deve ser limitada à execução de ambientes dependentes de ferramentas de linha de comando, como PHPUnit e MySQL.

  

## Distribuindo e provisionando com Puppet

  

O Puppet é o verdadeiro herói aqui. Uma vez que uma máquina virtual é distribuída, ele torna fácil manter a configuração das máquinas sincronizadas. Pense em sua máquina virtual como descartável. Você deve ser capaz de destruí-la e recriá-la sem perder funcionalidade. Quaisquer alterações de configuração devem ser feitas para que a máquina possa ser propagada para o arquivo de configuração do Puppet e distribuída através de um repositório Git ou um servidor do Puppet (puppetmaster). Lembre-se: a chave é que todos tenham o mesmo ambiente e, para fazer isso, nenhuma modificação personalizada deve ser feita para a máquina virtual sem compartilhar suas alterações na configuração através do arquivo Puppet.

  

Se você tiver modificado *base.pp*, você pode facilmente reconfigurar a máquina da seguinte forma:

  

```
 vagrant reload
```

  

Você também pode destruir completamente a máquina e começar de novo:

  

```
 vagrant destroy vagrant up
```

  

Se você quiser apenas suspender a máquina virtual para mais tarde:

  

```
 vagrant suspend vagrant resume
```

  

Depois de ter configurado uma box, você também pode empacotá-la e distribuir uma versão binária usando o comando de pacote do Vagrant. Eu prefiro criar um repositório Git com muitas pastas contendo configurações diferentes. Por exemplo, você pode ter um ambiente LAMP estável em uma pasta, e outra contendo um script para instalar o release candidate do PHP 5.4. No entanto, outra pode conter um ambiente Ruby ou Python. Alternar entre elas é tão simples como suspender uma máquina e reinicializar outra.

  

## Desenvolvendo com um ambiente local consistente

  

Neste ponto, você já deve ser capaz de modificar arquivos facilmente  dentro do seu diretório *www* em sua máquina local, recarregar seu navegador em <http://localhost:8080/> e ver os resultados.

  

Essa configuração serve como um ótimo ambiente de desenvolvimento com o qual começar. Cada aplicativo terá seu próprio conjunto de dependências. Você pode até mesmo distribuir a configuração da máquina virtual dentro do repositório do aplicativo para servir como uma definição explícita das dependências que ela tem. Com isso, você pode configurar o servidor de integração contínuo para implementar uma máquina, provisioná-la, instalar o aplicativo, executar seus testes e reportar de volta para você.

  

Existe um último nível de configuração e flexibilidade com uma configuração como essa. Acima de tudo, porém, sua equipe será capaz de trabalhar mais rápido e de forma mais eficiente, e você não vai acabar em uma situação em que algo funciona de forma diferente em um ambiente em relação a outro. Espero que você encontre uma maneira de usar essas ferramentas para sua própria saúde mental.

  

\*\*\*

  

*Texto original disponível em <http://webadvent.org/2011/facilitating-development-environment-consistency-by-jeff-loiselle>*

  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](web-archive-org--facilitando-a-consistencia-do-ambiente-de-desenvolvimento/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Facilitando+a+consist%C3%AAncia+do+ambiente+de+desenvolvimento&amp;link=http%3A%2F%2Fimasters.com.br%2Flinguagens%2Fphp%2Ffacilitando-a-consistencia-do-ambiente-de-desenvolvimento%2F)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](web-archive-org--facilitando-a-consistencia-do-ambiente-de-desenvolvimento/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Facilitando+a+consist%C3%AAncia+do+ambiente+de+desenvolvimento&amp;link=http%3A%2F%2Fimasters.com.br%2Flinguagens%2Fphp%2Ffacilitando-a-consistencia-do-ambiente-de-desenvolvimento%2F)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/151885044650/u/49/f/546640/c/33212/s/281b1154/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
from iMasters <http://imasters.com.br/linguagens/php/facilitando-a-consistencia-do-ambiente-de-desenvolvimento/>
