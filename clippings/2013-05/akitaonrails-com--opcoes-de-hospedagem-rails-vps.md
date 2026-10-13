---
url: "http://www.akitaonrails.com/2013/05/03/opcoes-de-hospedagem-rails-vps#.UYotarXV_zw"
captured_at: "2013-05-08T08:06:02-03:00"
title: "AkitaOnRails.com - Opções de hospedagem Rails: VPS"
domain: "akitaonrails-com"
---

# **O**pções de hospedagem Rails: VPS

[Tutorials](http://www.akitaonrails.com/Tutorials)  [Ruby](http://www.akitaonrails.com/Ruby)  [Dicas e Tutoriais](http://www.akitaonrails.com/Dicas e Tutoriais)  [Iniciante](http://www.akitaonrails.com/Iniciante)

![afc96026101bc2a1d15dbd597fb68c65.jpg](akitaonrails-com--opcoes-de-hospedagem-rails-vps/afc96026101bc2a1d15dbd597fb68c65.jpg)

![1cf5bcb3bbb29ad8bb94d40718c0efca.png](akitaonrails-com--opcoes-de-hospedagem-rails-vps/1cf5bcb3bbb29ad8bb94d40718c0efca.png)

![2519279b85f7e42f181b4dd1d03c4acd.png](akitaonrails-com--opcoes-de-hospedagem-rails-vps/2519279b85f7e42f181b4dd1d03c4acd.png)

A opção mais antiga, antes de existirem os Platform as a Service (PaaS) como Heroku, AppFog, OpenShift e outros são os Virtual Private Servers ou VPS**.** Os termos confundem pois costumamos chamar de "cloud" as soluções que caem nas categorias SaaS (serviços), PaaS (plataforma), IaaS (infraestrutura) e muitos tendem a deixar VPS numa categoria à parte**.**

VPS são máquinas virtuais, assim como um VirtualBox, Parallels, VMWare na sua máquina local, só que hospedado no data center de alguém**.** Eu particularmente acho que VPS está na mesma categoria que IaaS**.**

[Check out all related links](#links)

Seguindo o modelo Amazon AWS a diferença entre seus [EC2](http://aws.amazon.com/ec2/)  e os VPS é que um VPS tende a se comportar mais como um servidor físico**.** Você controla ações que seriam de hardware como reboot, shutdown**.** Uma vez que uma VPS é criada e ligada, ela permanece ligada**.**

Um EC2, ou um dyno Heroku, são máquinas "voláteis"**.** Elas podem ser "recicladas" sem que você precise saber disso**.** Ou seja, elas podem ser desligadas, clonadas, movidas para outro servidor físico**.** O tipo de controle de um IaaS é ser "elástico". A melhor forma de ser elástico é não depender da máquina ou do armazenamento e tornar simples recriar máquinas a partir de receitas (como de Chef) ou de imagens (AMI, VMI)**.** Para recriação, os arquivos que compõe a aplicação não deveriam mudar**.**

Por isso mesmo, seja colocando uma aplicação no AWS EC2 ou num Heroku, a prática está em fazer coisas como uploads serem enviadas a um serviço de armazenamento permanente externo, como o [Amazon AWS S3](http://aws.amazon.com/s3/) **.** Ou então montar um disco separado que é uma das opções com o [Amazon AWS EBS](http://aws.amazon.com/ebs/)  (Elastic Block Store), de forma que novas instâncias possam montar esse disco separado (bom para bancos de dados)**.**

A arquitetura da Amazon oferece os meios também para cenários em múltiplas zonas geográficas (multi AZ - multi-availability zones), o que em muito aumenta a disponibilidade do seu serviço, obviamente por um bom preço**.** A parte boa da solução da AWS é que os serviços que ela monta sobre sua infraestrutura usufruem dos mesmos benefícios**.** Por exemplo, o [Amazon RDS](http://aws.amazon.com/rds/)  (Relational Database Service) é o serviço de banco de dados MySQL, Oracle ou Microsoft SQL Server gerenciado pela Amazon**.** Uma das vantagem é que se você escolher, seu banco de dados pode estar distribuído no esquema multi AZ, espalhado em múltiplos data centers fisicamente diferentes, geograficamente separados, para a máxima disponibilidade em casos de serviços de missão crítica**.**

Enfim, deve estar claro que para a máxima flexibilidade a melhor solução é usar um IaaS robusto como a Amazon AWS**.** Concorrentes incluem o mais recente [Microsoft Azure](http://www.windowsazure.com/en-us/) **.** O [Rackspace Open Cloud](http://www.rackspace.com/open-cloud/)  quer ir nessa direção também, mas ele oferece bem menos**.** Não é necessário ter tudo que a Amazon para ser um "IaaS", ao pé da letra, se for uma "infraestrutura oferecida e gerenciada como serviço", é um IaaS, por isso eu disse que considero muitos do serviços de "VPS" também como IaaS**.** Se olha a [lista na Wikipedia](http://en.wikipedia.org/wiki/Cloud_computing#Infrastructure_as_a_service_.28IaaS.29) verá que ele lista muitos deles juntos**.**

## Virtual Private Server

Vou considerar como VPS a funcionalidade de manter uma máquina permanente (não-volátil) com armazenamento de bloco permanente (não-S3), com rede privada entre as máquinas virtuais, como "VPS"**.**

O termo VPS existe há muito mais tempo que o termo IaaS**.** Historicamente falando, o conceito de dividir os recursos da máquina física entre múltiplos usos existe desde o tempo dos mainframes**.** Qualquer OS que você esteja usando hoje, seja Windows, Linux ou OS X, é capaz de criar múltiplos usuários, executar processos em paralelo**.** Depois surgiu o formato onde é possível "virtualizar" o OS inteiro, onde cada usuário ou processo "sente" como se estivesse numa máquina física isolada**.**

Para controlar as máquinas virtuais (criar, desligar, etc) existem os "hypervisors", os monitores que existem diretamente sobre o hardware (XenServer, KVM, Hyper-V) ou dentro do OS que boota primeiro (VirtualBox)**.**

Sobre ele são criadas máquinas virtuais que podem ser totalmente virtuais ou o que chamamos de para-virtuais**.** No primeiro tipo, o OS na máquina virtual realmente "acha" que está sozinha no hardware, é a mais lenta das opções**.** No segundo tipo, o OS sabe que existe o hypersor e se comunica com ela, o que a torna bem mais performática**.** Exemplos de opções de paravirtualização são Xen, OpenVZ**.**

Existe um terceiro tipo que eu diria, é um passo anterior à total máquina virtual, que é onde o kernel do OS tem a capacidade de dividir espaços virtuais sem precisar um segundo OS sobre um hardware totalmente virtual**.** Nesse caso dizemos que o kernel é capaz de criar uma "prisão", literalmente um "jail", onde os programas que rodam nesse espaço não deveriam saber sobre os outros jails ao seu redor**.** É uma opção de menor overhead (pois não precisa de um hardware virtual inteiro e outro OS instalado) mas não é 100% isolado (na prática o comportamento é como se fosse)**.** Um exemplo é se existir algum exploit do programa num jail que consiga dar crash no kernel, todos os outros jails caem**.** Num sistema virtualizado, o programa com exploit conseguirá no máximo derrubar a máquina virtual onde está mas não as outras no mesmo hypersor**.** Nessa categoria de jails temos alguns conhecidos como [chroot](http://en.wikipedia.org/wiki/Chroot)  ou o mais recente [LXC](http://lxc.sourceforge.net) **.**

Alguns VPS usam soluções de paravirtualização, outros que preferem economizar recursos de hardware usam jails**.** Uma das vantagens da leveza do jail é poder, dentro de uma máquina virtual já paravirtualizada, ainda dividir uma segunda vez usando LXC sem grandes perdas**.** É praticamente uma [Inception](http://www.imdb.com/title/tt1375666/) .

![8457fb0e3eda32215285740ce0257157.jpg](akitaonrails-com--opcoes-de-hospedagem-rails-vps/8457fb0e3eda32215285740ce0257157.jpg)

Os que eu mais usei até o momento na categoria VPS paravirtualizado são o [Linode](http://www.linode.com) , [Rackspace Cloud](http://www.rackspace.com)  e [WebbyNode](http://webbynode.com) **.** Se não me engano, todos eles utilizam máquinas Xen com [XenServer](http://www.citrix.com/products/xenserver/overview.html) **.**

Todos eles oferecem os mesmos serviços básicos, dentre eles:

- criação e gerenciamento de máquinas virtuais paravirtualizadas em Xen com acesso a root
- upgrade vertical facilitado (mais CPU, mais RAM)
- diversos sistemas operacionais (32-bits, 64-bits, Linux, Windows)
- serviços de fácil configuração de load balancer, DNS (IPs públicos, IPs privados de rede reservada interna)
- coisas essenciais como snapshots, procedimentos de backup agendados, monitoramento dos recursos
- suporte 24x7 (todos tem um tempo de resposta bom para tickets de problemas e dúvidas, nunca fiquei sem resposta)

No fundo é esse o essencial que se espera de qualquer bom VPS que se preze**.** Os preços só dos servidores variam mas precisa adicionar os diferentes serviços, facilidades, etc**.** Então não se atenha somente ao preço unitário de servidor:

- Linode: 1GB RAM, 8 CPU (1x priority), 24GB HD - USD 20**.**00/mês
- WebbyNode: 1GB RAM, 45GB HD - USD39**.**90/mês
- Rackspace: 1GB RAM, 1 CPU, 40GB HD - USD 43**.**80/mês

Pra dar uma noção, vejamos uma configuração mais com cara de "produção":

- Linode: 4GB, 8 CPU (4x priority), 96GB - USD 80**.**00/mês
- WebbyNode: 4GB, 180GB HD - USD 159**.**99/mês
- Rackspace: 4GB, 2 CPU, 160GB - USD 175**.**20/mês

Notem que quando se diz "CPU" estamos dizendo "vCPU" ou "CPU virtual"**.** Ou seja, dentro da máquina virtual você vai enxergar a quantidade de CPUs, mas elas estão na prática competindo recursos do CPU de verdade com outras máquinas virtual**.** É isso que quer dizer o fator de "prioridade" da Linode**.** Apesar do número de vCPU ser mesmo entre os dois planos do exemplo, o segundo plano dá mais prioridade do CPU real para o tipo mais caro do que para o mais barato, obviamente**.** No caso da WebbyNode não havia denominação de CPUs na tabela de planos**.**

O valor de USD 20/mês por uma máquina de 1GB de RAM é o que muitos consideram mais "barato" do que um Heroku ou AppFog**.** Mas como disse, no caso da AppFog você tem 2GB pelos mesmos USD 20/mês**.** No caso do Heroku inicia em USD 36/mês por 1 dyno. Portanto, não é tão mais "caro"**.** Começa a ficar mais caro quando se adiciona outros serviços como um banco de dados mais parrudo como um [Heroku Postgres Crane](https://postgres.heroku.com/pricing)  que é USD 50/mês, ou o [Amazon AWS MySQL instância pequena](http://aws.amazon.com/pt/rds/pricing/)  que pode chegar a USD 64/mês, ou com serviços como [Websolr Cobalt](http://websolr.com/plans)  que é USD 20/mês**.**

No exemplo, uma aplicação que precise acima da versão "free" no Heroku pode custar: USD 36 (dyno) + USD 50 (postgres) + USD 20 (websolr) = USD 106/mês; no AppFog custaria: USD 20 (já com banco de dados) + USD 20 (websolr) = USD 40/mês**.**

Digamos que você configure tudo na mão na Linode com uma máquina de USD 20/mês**.** No cenário mais "caro", você vai gastar USD 80/mês**.** Se você precisar dedicar 4 horas por mês dando alguma manutenção, significa que você está vendendo sua taxa horária a USD 20/hora**.** No caso da AppFog sua taxa horária seria de USD 5/hora**.** A justificativa é clara: você deveria estar não consumindo horas nisso e pensando em como fazer sua hora valer o triplo, quádruplo disso**.** Existe uma frase popular que diz o seguinte:

> "Penny wise, Pound Foolish"

Traduzindo pra português seria algo como:

> "Quem economiza centavos perde dólares"

Agora cuidado com a interpretação**!** Do jeito que eu disse parece que estou dizendo para só usar coisas caras em vez de economizar com o mais barato**.** De jeito nenhum! A única coisa que estou dizendo é que não existe uma única medida, a única coisa que faz sentido é [custo/benefício](http://pt.wikipedia.org/wiki/Rela%C3%A7%C3%A3o_de_custo-benef%C3%ADcio) , é a resposta à pergunta: *"Vou ter o valor sobre o que estou pagando**?**"*

![4e8d47c341b475a3bb0449e18bcb4216.jpg](akitaonrails-com--opcoes-de-hospedagem-rails-vps/4e8d47c341b475a3bb0449e18bcb4216.jpg)

Seu carro é um chevet 1981 caindo aos pedaços que male-male liga**?** Se te oferecerem um seguro barato de R$ 10/mês, ele vale a pena**?**

A resposta - caso esse cenário absurdo pudesse acontecer - poderia ser: *"óbvio que não, é um pau velho**!**"* Eu diria: *"depende!"* Digamos que o dono desse carro o use pra trabalhar e, com ele, consiga tirar R$ 100/mês**.** Só que o carro pode falhar a qualquer momento e se parar, não leva menos de 2 semanas pra reparar**.** Significa que ele vai perder no mínimo R$ 50/mês**.** Fora que a taxa de frequência é de pelo menos 3 vezes por semestre**.** Se num sementre ele gastaria R$ 60 num hipotético seguro e se parar as 3 vezes ele vai perder R$ 150, o seguro mais do que faz sentido**.**

Mesma coisa com servidores. Se seu cliente vale USD 20, coloque-o num servidor de USD 20**.** Se sua hora vale USD 5 e você não tem nada a fazer pra ganhar mais por hora, gerencie você mesmo**.**

Ou outro cenário mais comum: você está trabalhando num projeto pessoal, não tem compromissos com ninguém, está usando a oportunidade para estudar e aprender**.** USD 20/mês é hiper barato para se capacidar num categoria de trabalho que pode lhe render USD 40 ou mais por hora no futuro**.** Nesse caso não estamos falando [nem de custo, nem de despesa, nem de gasto, mas de investimento](http://www.academiaeconomica.com/2008/05/custo-despesa-gasto-e-investimento.html) **.**

## Qual VPS?

Na prática, a WebbyNode é a menor das 3 ofertas, mas tamanho não é documento e nunca tive problemas com eles**.** Porém eles não possuem uma coisa importante para quem pretende escalar horizontalmente: load balancer**.** Porém, como eles tem a oferta de IP privado entre servidores da mesma conta, você mesmo pode instalar uma máquina de HAProxy e balancear entre os servidores web**.** Não é o ideal mas dá para fazer.

O Linode implementou o [NodeBalancer](http://www.linode.com/nodebalancers/)  a USD 20 extras por mês**.** Parece uma boa opção para balancear seus serviços rapidamente**.**

Da mesma forma a Rackspace o [Cloud Load Balancer On-Demand](http://www.rackspace.com/cloud/load-balancing/) , iniciando a USD 10**.**95 extras por mês. Ambos os balancers da Linode e Rackspace funcionam de forma similar**.**

Não sei se eles usam um load balancer via software simples como [HAProxy](http://haproxy.1wt.eu/)  ou algo mais robusto e sofisticado como o bom e velho [F5 BIG-IP](http://www.f5.com/products/hardware/big-ip-hardware/overview/) **.** Se tivesse que chutar eu diria que a Linode usa o HAProxy e a Rackspace usa o F5 ou Barracuda ou Cisco ou todos :-)

O Rackspace é o mais caro, mas por investir e usar a plataforma de IaaS [OpenStack](http://www.openstack.org/)  ele é bem mais sofisticado e oferece bem mais opções**.** É quase um Amazon AWS simplificado ao principal. Uma das coisas que ele tem que mais me interessa é o [Cloud Database](http://www.rackspace.com/cloud/databases/)  que - segundo eles - é melhor do que o Amazon RDS**.** Como já devem ter lido nos meus artigos anteriores sobre Heroku, AppFog, já devem ter entendido o quão importante é um bom serviço gerenciado, robusto, seguro e escalável de banco de dados**.**

Por causa disso minha escolha - caso precise garantir um bom serviço específico de banco de dados - seria colocar na Rackspace Cloud**.**

Para produtos menores, que tem 1 ou 2 servidores (recomendado, mínimo de 1 web, 1 banco) tanto o WebbyNode quanto Linode oferecem bom valor pelo preço**.**

## Começando a pensar como um Sysadmin

![8bba3b7ff309d4ec18b8bfa2b8da964a.jpg](akitaonrails-com--opcoes-de-hospedagem-rails-vps/8bba3b7ff309d4ec18b8bfa2b8da964a.jpg)

Como já disse diversas vezes, a menos que você tenha uma boa experiência e conhecimento tendo trabalhado como sysadmin em um grande data center, não se responsabilize pela saúde de infraestrutura com um cliente pagante**.** Delegue o serviço e repasse os custos.

Ser um sysadmin é muito mais do que saber dar um apt-get install em pacotes**.** Para uma breve introdução a instalar um ambiente Rails completo do zero, leia meu artigo [Ruby e Rails no Ubuntu 12**.**04 LTS Precise Pangolin](http://www.akitaonrails.com/2012/08/13/ruby-e-rails-no-ubuntu-12-04-lts-precise-pangolin#.UYQoFJUSM_s)**.**

Fora isso você precisa no mínimo:

- Firewall - o básico de [iptables](https://help.ubuntu.com/community/IptablesHowTo)  é essencial e não, deixar porta de MySQL aberta na internet pública é uma **péssima** prática**.** Já vi isso e é um desastre esperando para acontecer**.** E novamente, não faça "copy e paste" de uma configuração que já existe**.** É o mesmo que colocar um cadeado que todo mundo tem uma cópia da chave, ou usar um cadeado que um estranho que te deu**.** Você pode estar deixando coisas abertas sem saber.
- Tuning de Banco de dados - todo banco de dados, na configuração padrão, é horrível**.** E todos sem prática basicamente fazem um apt-get install mysql-server e dão por encerrado**.** No mínimo - no mínimo! - comece a estudar o site da Percona e a uma configuração um pouco melhorzinha pelo [wizard](https://tools.percona.com/wizard)  deles**.** Mas mesmo só isso não é suficiente, você precisa saber monitorar os serviços, avaliar a utilização dos recursos, processamento e customizar os parâmetros de acordo com seu servidor e sua aplicação**.** Não é algo que se faz uma vez e esquece. PostgreSQL também precisa de tuning**.** Tem aplicações que falham porque não conexões suficientes disponíveis no banco**.** Ou estouram a máquina porque tem demais e consome todos os recursos**.** São múltiplos fatores a se preocupar.
- Daemons - tem gente que inicia uma aplicação Rails com Unicorn executando unicorn config/unicorn**.**rb & e larga assim! Ou seja, quando o servidor precisar reiniciar por alguma razão o Unicorn não vai subir**.** Você obrigatoriamente precisa e um init script (/etc/init**.**d/) ou se estiver no Ubuntu um script de Upstart (/etc/init/) para que o OS saiba como subir sua aplicação**.** Um exemplo para Resque que uso é assim:

|  |
| --- |
| ``` description "Resque worker configuration. Run with ID"  start on (local-filesystems and net-device-up IFACE=eth0) stop on shutdown  respawn respawn limit 5 20  instance $ID  script   HOME_DIR=/home/minha_app   APP_ROOT=$HOME_DIR/apps/minha_app/current   PIDFILE=$HOME_DIR/apps/minha_app/shared/pids/resque-$ID.pid   LOGFILE=$HOME_DIR/apps/minha_app/shared/log/resque-$ID.log   echo $$ > $PIDFILE   chown meu_user:meu_grupo $PIDFILE   chown meu_user:meu_grupo $LOGFILE   exec su -c "export PATH=$HOME_DIR/.rbenv/shims:$HOME_DIR/.rbenv/bin:$PATH; cd $APP_ROOT; bundle exec rake environment resque:work QUEUE=* RAILS_ENV=production PIDFILE=$PIDFILE >> $LOGFILE 2>&1" minha_app end script ``` |

Esse é um exemplo rústico (obviamente mude minha\_app e outros parâmetros de acordo com o que você usa)**.**

- Monitoramento - daemons podem morrer, o Upstart cuida de vários aspectos disso mas não de tudo, e em muitos casos você pode precisar de uma ajuda extra**.** Nesse caso recomendo o [Monit](http://mmonit.com/monit/) **.** Não recomendo usar God ou semelhantes pois fica minha pergunta: *"God monitora seus daemons, e quem monitora God**?**"* Monit é escrito em C, leve, robusto, bem testado, raramente dá problema**.** Um exemplo de um trecho de configuração de Monit é assim:

|  |
| --- |
| ``` check process memcached with pidfile /var/run/memcached.pid     start program = "/etc/init.d/memcached start"     stop program = "/etc/init.d/memcached stop"  check process postfix with pidfile /var/spool/postfix/pid/master.pid     start program = "/etc/init.d/postfix start"     stop program  = "/etc/init.d/postfix stop"  check process resque-0 with pidfile /home/meu_user/apps/minha_app/shared/pids/resque-0.pid     group resque     start program = "/sbin/start resque ID=0"     stop program = "/sbin/stop resque ID=0"     if changed pid 6 times within 6 cycles then stop ``` |

Se por acaso um serviço cair e ele não se recompor, você pode tentar subir**.** Se ele não subir em algumas tentativas pare de tentar subir e avise alguém**.** Enfim, várias estratégias que podem ser configuradas dependendo do serviço**.** Novamente, você precisa compreender muito bem o comportamento de cada serviço antes de criar essas estratégias**.**

E não deixe só por isso. Coloque sistemas de monitoramento para ficar constantemente avaliando a saúde do seu sistema**.** Recursos como CPU, RAM, disco, tráfego (in e out), daemons rodando, etc**.** Você precisa saber o comportamento do seu sistema em condições normais e em condições extraordinárias**.** Coisas simples como não saber configurar um mero [logrotate](http://linux.die.net/man/8/logrotate)  e deixar seus logs consumirem todo o espaço em disco**.**

- Backup - todo bom sistema tem como agendar tanto imagem/snapshot completo da máquina quanto especificamente de serviços como banco de dados**.** Você precisa dos dois. Precisa inclusive testar procedimentos de restauração - erro mais comum é agendar backup e quando precisa descobrir que ele não restaura como esperava, ou que você esqueceu de selecionar tudo que precisava colocar no backup**.** Cuidado que tem algumas opções onde o backup é guardado na mesma máquina que você está "backapeando"**.** Obviamente nem preciso dizer que é uma péssima idéia: se sua máquina der problema, seu backup vai ficar inacessível**.** Sempre jogue o backup em algum lugar externo. Mantenha backups rotacionados, diários, semanais, mensais para fins de auditoria se precisar**.** Nunca, jamais, guarde dados sensíveis como número de cartão de crédito ou senhas como texto**!****!**!
- Disaster Recovery - seu sistema caiu**.** O que aconteceu? Você precisa ter os meios de realizar diagnósticos rápidos (sistemas de monitoramento), avaliar o que deu errado na raíz (condição do erro), criar novos procedimentos para que o mesmo erro não se repita**.** Mais do que isso, já ter pronto procedimentos a serem seguidos para cada tipo de situação**.** Um exemplo: jamais fazer uma atualização do binário de banco de dados sem antes fazer um backup completo dos dados**.**

Existem muitos outros fatores a se considerar, mas esse é o mínimo**.** Eu não sou um sysadmin experiente, mas o básico que sei é o suficiente para entender que infraestrutura é algo que deve ser levado a sério**.** O famoso *"está rodando"* é totalmente insuficiente**.** "Rodar" é muito simples, qualquer idiota consegue. Manter de pé e, principalmente, recuperar rapidamente e com integridade se algo der errado, é que diferencia os adultos das crianças**.**

Finalmente, existem várias opções**.** Avalie bem o que cada serviço oferece de acordo com os requerimentos funcionais da sua aplicação e do seu cliente e escolha**.** A vantagem é que hoje existem opções para todos os gostos e tamanhos**.**
