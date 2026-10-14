---
url: "http://imasters.com.br/desenvolvimento/conversando-sobre-vagrant-parte-01/"
captured_at: "2013-01-21T14:21:10-03:00"
title: "Conversando sobre Vagrant – Parte 01"
domain: "imasters-com-br"
---

Neste artigo, vou mostrar um pouco sobre o [Vagrant](http://vagrantup.com/), apresentar um problema comum e a solução para ele. Os requisitos para acompanhar o artigo são familiaridade com o assunto de virtualização, não ter medo do shell e um pouco de paciência! Caso encontre algum erro ou algo não tenha ficado muito claro em algum passo ou explicação, é só postar nos comentários.

  

Muitos desenvolvedores gostam de ter um ambiente de fácil acesso para simular testes da sua aplicação em ambiente parecido ao de produção (OK! Não sei se são muitos, mas deveriam todos ter essa prática).

  

O Vagrant é uma solução para isso junto com o VirtualBox. Algo estranho? Se eu tenho o VirtualBox, por que preciso do Vagrant também? Eu posso fazer tudo com o VirtualBox!

  

Verdade! O VirtualBox já é uma solução para o problema, mas o Vagrant tem recursos que não são fornecidos no VirtualBox, por exemplo, configurações básicas para trabalhar com o Puppet ou Chef, fácil configuração via `Vagrantfile` e o mais interessante para quem é desenvolvedor: um [CLI](http://en.wikipedia.org/wiki/Command-line_interface) amigável!

  

Então, o que eu preciso para começar a usar o Vagrant?

  

[VirtualBox](https://www.virtualbox.org/)

  

Ruby – recomendo instalar a versão mais atual via [RVM](https://rvm.io/rvm/install/)

Tendo os requisitos citados devidamente configurados, recomendo criar uma pasta com o nome da VM que pretende criar e configurar um ambiente ruby para ela, assim:

  

```
 host $ mkdir ubuntu host $ cd ubuntu host $ echo "rvm use 1.9.3" > .rvmrc
```

  

Talvez você precise entrar e sair da pasta do projeto para o RVM carregar o ambiente, caso você use muitas versões do ruby.

  

Feito isso, vamos agora instalar o Vagrant:

  

```
 host $ gem install vagrant
```

  

Agora, temos o Vagrant instalado e precisamos criar nossa VM, mas para isso preciso de uma Box:

  

```
 host $ vagrant box add lucid32 http://files.vagrantup.com/precise32.box
```

  

No exemplo acima, estou adicionando uma Box à minha máquina, no caso, o Ubuntu Pricese 32 bits. Ok! Onde foi parar essa Box agora?

  

No meu caso, foi para `/Users/joaovrmaia/.vagrant.d/boxes/precise32.` Eu uso Mac OS X, mas basicamente o que ele fazer é colocar na home do seu usuário para que você possa reaproveitar o Box para outras VM. O detalhe é que nesse caso estou pegando uma VM padrão do Vagrant, mas nada impede você de criar a sua VM e compartilhar. Outra coisa: isso é comum de acontecer para facilitar todos os desenvolvedores da equipe terem o mesmo ambiente em suas máquinas. Vou deixar essa caso para outro momento.

  

Show! Tenho VirutalBox, tenho Vagrant e tenho minha Box, mas cadê minha VM? Calma, jovem padawan!

  

```
 host $ vagrant init precise32
```

  

Esse comando vai criar o `Vagrantfile`, que tem mais ou menos esta cara:

  

```
 # -*- mode: ruby -*- # vi: set ft=ruby : Vagrant::Config.run do |config| # configurações vão aqui config.vm.box = "precise32" end
```

  

Agora sim já temos tudo para a tão esperada hora, iniciar a VM!

  

```
 host $ vagrant up [default] Attempting graceful shutdown of VM... [default] Clearing any previously set forwarded ports... [default] Forwarding ports... [default] -- 22 => 2222 (adapter 1) [default] Creating shared folders metadata... [default] Clearing any previously set network interfaces... [default] Booting VM... [default] Waiting for VM to boot. This can take a few minutes. [default] VM booted and ready for use! [default] Mounting shared folders... [default] -- v-root: /vagrant
```

  

Yey! VM funcionando, mas como acessar ela agora? Muito fácil: basta dar um `ssh`!

  

```
 host $ vagrant ssh vm $
```

  

Bom, agora sua VM está funcionando e você já está livre para se divertir com ela, mas lembra que citei um problema e que apresentaria sua solução?

  

Provavelmente, os seus primeiros passos serão:

  

```
 vm $ sudo su vm # apt-get update vm # apt-get dist-upgrade
```

  

É claro, aproveitar que a VM está nova e deixá-la atualizada e sem risco de quebrar nada! Ai que você se engana! Em toda atualização de Kernel da VM ou do VirtualBox, o processo a seguir será necessário. Não tive tempo de verificar mais a fundo o problema, mas ele é comum.

  

Ainda não ficou claro qual é o problema? Faça os seguintes passos:

  

```
 vm $ exit host $ vagrant reload [default] Attempting graceful shutdown of VM... [default] Clearing any previously set forwarded ports... [default] Forwarding ports... [default] -- 22 => 2222 (adapter 1) [default] Creating shared folders metadata... [default] Clearing any previously set network interfaces... [default] Booting VM... [default] Waiting for VM to boot. This can take a few minutes. [default] VM booted and ready for use! [default] Mounting shared folders... [default] -- v-root: /vagrant The following SSH command responded with a non-zero exit status. Vagrant assumes that this means the command failed! mount -t vboxsf -o uid=`id -u vagrant`,gid=`id -g vagrant` v-root /vagrant host $
```

  

OH WAIT! Algo de errado não esta certo! Pois é, esse é o problema! =/

  

Fique calmo que eu tenho a solução! =)

  

```
 host $ vagrant ssh # sim, ela ainda funciona mesmo com o erro vm $ sudo apt-get install build-essential -y # compiladores vm $ sudo apt-get install linux-headers-server linux-headers-virtual -y # headers do kernel vm $ sudo apt-get install kernel-package -y # pacotes do kernel vm $ sudo apt-get install dkms -y # para o virtual box vm $ mkdir vbox vm $ wget http://download.virtualbox.org/virtualbox/4.1.12/VBoxGuestAdditions_4.1.12.iso vm $ sudo mount -o loop VBoxGuestAdditions_4.1.12.iso vbox/ vm $ cd vbox vm $ ./VBoxLinuxAdditions.run
```

  

Agora, basta sair da VM e fazer o reload que ela funcionará novamente sem erros! =)

  

O detalhe vai para o `fail` acusado ao rodar o binário `VBoxLinuxAdditions.run` do Xorg, mas caso não tenha ele instalado não é problema!

  

Fica agora aí com a sua VM funcionando de boa para as suas brincadeiras de SysAdmin! =)

  

Abraços!

  
 ![](http://imasters.com.br.feedsportal.com/c/33212/f/546640/s/27bf01e8/mf.gif)  
   

[![](http://res3.feedsportal.com/images/emailthis2_pt.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&title=Conversando+sobre+Vagrant+%E2%80%93+Parte+01&link=http%3A%2F%2Fimasters.com.br%2Fdesenvolvimento%2Fconversando-sobre-vagrant-parte-01%2F)

  

[![](http://rss.feedsportal.com/images/bookmark.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Conversando+sobre+Vagrant+%E2%80%93+Parte+01&link=http%3A%2F%2Fimasters.com.br%2Fdesenvolvimento%2Fconversando-sobre-vagrant-parte-01%2F)

  
   
   
 [![](http://da.feedsportal.com/r/151884680472/u/49/f/546640/c/33212/s/27bf01e8/a2.img)](http://da.feedsportal.com/r/151884680472/u/49/f/546640/c/33212/s/27bf01e8/a2.htm) ![](http://pi.feedsportal.com/r/151884680472/u/49/f/546640/c/33212/s/27bf01e8/a2t.img)  
   
 ![](http://feeds.feedburner.com/~r/imasters/~4/khJBd5xinS8)  
   
   
   
 from iMasters <http://imasters.com.br/desenvolvimento/conversando-sobre-vagrant-parte-01/>
