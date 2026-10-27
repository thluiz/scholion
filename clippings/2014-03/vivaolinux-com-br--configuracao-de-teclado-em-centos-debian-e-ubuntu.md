---
url: "http://www.vivaolinux.com.br/dica/Configuracao-de-teclado-utilizando-as-distribuicoes-CentOS-Debian-e-Ubuntu/"
captured_at: "2014-03-22T20:45:41-03:00"
title: "Linux: Configuração de teclado utilizando as distribuições CentOS, Debian e Ubuntu [Dica]"
domain: "vivaolinux-com-br"
---

# Configuração de teclado utilizando as distribuições CentOS, Debian e Ubuntu

No Brasil, o layout adotado atualmente pela Associação Brasileira de Normas Técnicas (ABNT) é o *QWERTY ABNT2 (br-abnt2)*. Nesta dica mostro como configurar o teclado para o layout ABNT2 nas distribuições *Debian 6*, *CentOS 6* e *Ubuntu 12.04*.
  
  
Para configurar o teclado pode se fazer uso de comandos, mas aqui irei demostrar como fazer esse trabalho editando arquivos do sistema.
  
  
Configurando teclado no Debian e Ubuntu:
  
  
1° - Edite o arquivo */etc/default/keyboard* usando um editor em modo texto e deixe a configuração como mostrada abaixo:

XKBMODEL="pc105"  
XKBLAYOUT="br"  
XKBVARIANT="abnt2"  
XKBOPTIONS=""

2° - Salve as alterações e terá seu teclado configurado com layout ABNT2.
  
  
Configurando teclado no CentOS:
  
  
1° - Edite o arquivo */etc/sysconfig/keyboard* usando um editor em modo texto e deixe a configuração como mostrada abaixo:

KEYTABLE="br-abnt2"  
MODEL="abnt2"  
LAYOUT="br"  
KEYBOARDTYPE="pc"

2° - Salve as alterações e terá seu teclado configurado com o layout ABNT2.
  
  
É uma dica simples, no entanto, muito boa para necessidades básicas.

**Outras dicas deste autor**

**Leitura recomendada**

![3c0f33b84e8622192d04098775adca91.gif](vivaolinux-com-br--configuracao-de-teclado-em-centos-debian-e-ubuntu/3c0f33b84e8622192d04098775adca91.gif) [Istalando RRDTool no Centos 5.6](http://www.vivaolinux.com.br/dica/Istalando-RRDTool-no-Centos-5.6 "Leitura recomendada")   
   ![3c0f33b84e8622192d04098775adca91.gif](vivaolinux-com-br--configuracao-de-teclado-em-centos-debian-e-ubuntu/3c0f33b84e8622192d04098775adca91.gif) [Gravar Slax Linux diretamente no HD e salvar as mudanças](http://www.vivaolinux.com.br/dica/Gravar-Slax-Linux-diretamente-no-HD-e-salvar-as-mudancas "Leitura recomendada")  
   ![3c0f33b84e8622192d04098775adca91.gif](vivaolinux-com-br--configuracao-de-teclado-em-centos-debian-e-ubuntu/3c0f33b84e8622192d04098775adca91.gif) [Configurando Winmodens no Linux](http://www.vivaolinux.com.br/dica/Configurando-Winmodens-no-Linux "Leitura recomendada")  
   ![3c0f33b84e8622192d04098775adca91.gif](vivaolinux-com-br--configuracao-de-teclado-em-centos-debian-e-ubuntu/3c0f33b84e8622192d04098775adca91.gif) [Colocar o syntax highlighting do Vim funcionando corretamente](http://www.vivaolinux.com.br/dica/Colocar-o-syntax-highlighting-do-Vim-funcionando-corretamente "Leitura recomendada")  
   ![3c0f33b84e8622192d04098775adca91.gif](vivaolinux-com-br--configuracao-de-teclado-em-centos-debian-e-ubuntu/3c0f33b84e8622192d04098775adca91.gif) [Painel Lançador do Ubuntu 12.10 - Como adicionar/remover aplicativos manualmente](http://www.vivaolinux.com.br/dica/Painel-Lancador-do-Ubuntu-1210-Como-adicionar-remover-aplicativos-manualmente "Leitura recomendada")

**Comentários**

[1] Comentário enviado por [danfmsouza](http://www.vivaolinux.com.br/perfil/verPerfil.php?login=danfmsouza) em 26/11/2012 - 20:01h:
  
  
E ai galera!  
Uma outra forma menos invasiva de fazer isso no Ubuntu é usar o DPKG para reconfigurar o pacote keyboard-configuration. Podemos usar o seguint comando:  
sudo dpkg-reconfigure keyboard-configuration  
Vai aparecer um Wizard do pacote ai você passa as informações sobre o teclado! É Supimpa! Espero ter ajudado a Galera...

[2] Comentário enviado por [eabreu](http://www.vivaolinux.com.br/perfil/verPerfil.php?login=eabreu) em 26/11/2012 - 21:47h:
  
  
Valeu pela contribuição amigo danfmsouza.

[3] Comentário enviado por [super\_might](http://www.vivaolinux.com.br/perfil/verPerfil.php?login=super_might) em 09/02/2013 - 09:25h:
  
  
valeu a dica.  
Mas no meu caso não funcionou :/  
  
Uso o Ubunto Server 12.10.  
fui la e alterei  
  
XKBMODEL "abnt2"  
XKBLAYOUT "br"  
XKBVARIAT "abnt2"  
XKBOPTIONS ""  
  
O teclado continua desconfigurado.

[4] Comentário enviado por [eabreu](http://www.vivaolinux.com.br/perfil/verPerfil.php?login=eabreu) em 09/02/2013 - 09:38h:
  
  
Primeiramente obrigado pelo comentário !  
  
Segundo a dica e para o debian, centos e ubuntu 12.04 desktop. desculpe se não especifiquei na dica que era para versão de desktop. Mas para a versão servidor, pode tentar configurar usando os seguintes comandos:  
  
# apt-get install console-data  
# dpkg-reconfigure console-data  
  
Dai é só usar o idioma desejado junto com layout do teclado que será usado.

[5] Comentário enviado por [deborahgomess](http://www.vivaolinux.com.br/perfil/verPerfil.php?login=deborahgomess) em 11/11/2013 - 11:07h:
  
  
Como eu salvo as alterações? Pq o pc diz q nao tenho permissão.   
Não há uma forma de fazer isso pelo terminal logado como usuário root? Pq tb nao consegui abrir a pasta do sistema para editar o arquivo por lá.  
Eu sei q tem como mudar essa configuração pelo menu 'system' - 'keyboard', mas nesse caso só muda para o usuário q esta logado. Seria necessário, portanto, fazer isso para cada usuário q fosse criado. Não da tanto trabalho assim mas o interessante é mudar p todos automaticamente.  
Desde já agradeço.

[6] Comentário enviado por [eabreu](http://www.vivaolinux.com.br/perfil/verPerfil.php?login=eabreu) em 11/11/2013 - 11:30h:

[5] Comentário enviado por deborahgomess em 11/11/2013 - 11:07h:  
  
Como eu salvo as alterações? Pq o pc diz q nao tenho permissão.   
Não há uma forma de fazer isso pelo terminal logado como usuário root? Pq tb nao consegui abrir a pasta do sistema para editar o arquivo por lá.  
Eu sei q tem como mudar essa configuração pelo menu 'system' - 'keyboard', mas nesse caso só muda para o usuário q esta logado. Seria necessário, portanto, fazer isso para cada usuário q fosse criado. Não da tanto trabalho assim mas o interessante é mudar p todos automaticamente.  
Desde já agradeço.

Usando o usuário root você tem permissão o suficiente para salvar as alterações feitas.

**Contribuir com comentário**

Para executar esta ação você precisa estar logado no site, caso
contrário, tudo o que for digitado será perdido.
