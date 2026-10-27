---
url: "http://www.hardware.com.br/comunidade/bios-tutorial/145689/"
captured_at: "2012-11-26T21:48:51-03:00"
title: "Tutorial: Código de erros de todos os BIOS - BIP"
domain: "hardware-com-br"
---

# [Tutorial: Código de erros de todos os BIOS - BIP](http://www.hardware.com.br/comunidade/bios-tutorial/145689/)

## Drivers, BIOS, Firmwares e Manuais

Página 1 de 2
   **1** 
[2](http://www.hardware.com.br/comunidade/bios-tutorial/145689/showthread.php?s=88150659b5bb34116203c32539517cbe&t=145689&page=2)

30-04-2004 por
[**RJR Informática**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=9885)

Tutorial: Código de erros de todos os BIOS - BIP

**Códigos de erro do BIOS**  
  
Durante o boot, o BIOS realiza uma série de testes, visando detectar com exatidão os componentes de hardware instalados no micro. Este teste é chamado de POST (pronuncia-se poust), acrônimo de "Power-On Self Test". Os dados do POST são mostrados durante a inicialização, na forma da tabela que aparece antes do carregamento do sistema operacional, indicando a quantidade de memória instalada, assim como os discos rígidos, drives de disquetes, portas seriais e paralelas e drives de CD-ROM padrão IDE instalados no micro.   
  
Além de detectar o hardware instalado, a função do POST é verificar se tudo está funcionando corretamente. Caso seja detectado algum problema em um componente vital para o funcionamento do sistema, como as memórias, processador ou placa de vídeo, o BIOS emitirá uma certa seqüência de bips sonoros, alertando sobre o problema. Problemas menores, como conflitos de endereços, problemas com o teclado, ou falhas do disco rígido serão mostrados na forma de mensagens na tela.  
  
O código de bips varia de acordo com a marca do BIOS (Award ou AMI por exemplo) podendo também haver pequenas mudanças de uma placa mãe para outra. Geralmente, o manual da placa mãe traz uma tabela com as seqüências de bips usadas. As instruções a seguir lhe servirão como referência caso não tenha em mãos o manual da placa mãe:  
  
**Códigos de erro do BIOS  
Modelo: AMI BIOS Tone POST Codes**   
  
**1 Bip Curto:**  
Post Executado com sucesso: Este é um Bip feliz emitido pelo BIOS quando o POST é executado com sucesso. Caso o seu sistema esteja inicializando normalmente e você não esteja ouvindo este Bip , verifique se o speaker está ligado à placa mãe corretamente.  
  
**1 Bip longo:**  
Falha no Refresh (refresh Failure) : O circuito de refresh da placa mãe está com problemas, isto pode ser causado por danos na placa mãe ou falhas nos módulos de memória RAM  
  
**1 Bip longo e 2 bips curtos:  
1 Bip longo e 3 bips curtos:**  
Falha no Vídeo: Problemas com o BIOS da placa de vídeo. Tente retirar a placa, passar borracha de vinil em seus contatos e recolocá-la, talvez em outro slot. Na maioria das vezes este problema é causado por mau contato.  
  
**2 bips curtos:**  
Falha Geral: Não foi possível iniciar o computador. Este problema é causado por uma falha grave em algum componente, que o BIOS não foi capaz de identificar. Em geral o problema é na placa mãe ou nos módulos de memória  
  
**2 Bips longos:**  
Erro de paridade: Durante o POST, foi detectado um erro de paridade na memória RAM. Este problema pode ser tanto nos módulos de memória quanto nos próprios circuitos de paridade. Para determinar a causa do problema, basta fazer um teste com outros pentes de memória. Caso esteja utilizando pentes de memória sem o Bit de paridade você deve desativar a opção "Parity Check" encontrada no Setup.  
  
**3 Bips longos:**  
Falha nos primeiros 64 KB da memória RAM (Base 64k memory failure) > Foi detectado um problema grave nos primeiros 64 KB da memória RAM. Isto pode ser causado por um defeito nas memórias ou na própria placa mãe. Outra possibilidade é o problema estar sendo causado por um simples mal contato. Experimente antes de mais nada retirar os pentes de memória, limpar seus contatos usando uma borracha de vinil (aquelas borrachas plásticas de escola) e recoloca-los com cuidado.  
  
**4 Bips Longos:**  
Timer não operacional: O Timer 1 não está operacional ou não está conseguindo encontrar a memória RAM. O problema pode estar na placa mãe (mais provável) ou nos módulos de memória.  
  
**5 Bips:**  
Erro no processador: O processador está danificado, ou mal encaixado. Verifique se o processador está bem encaixado, e se por descuido você não esqueceu de baixar a alavanca do soquete Zif (acontece nas melhores famílias :-)  
  
**6 Bips:**  
Falha no Gate 20 (8042 - Gate A20 failure): O gate 20 é um sinal gerado pelo chip 8042, responsável por colocar o processador em modo protegido. Neste caso, o problema poderia ser algum dano no processador ou mesmo problemas relacionados com o chip 8042 localizado na placa mãe  
  
**7 Bips:**  
Processor exception (interrupt error): O processador gerou uma interrupção de exceção. Significa que o processador está apresentando um comportamento errático. Isso acontece às vezes no caso de um overclock mal sucedido. Se o problema for persistente, experimente baixar a freqüência de operação do processador. Caso não dê certo, considere uma troca.  
  
**8 Bips:**  
Erro na memória da placa de vídeo (display memory error) : Problemas com a placa de vídeo, que podem estar sendo causados também por mal contato. Experimente, como no caso das memórias, retirar a placa de vídeo, passar borracha em seus contatos e recolocar cuidadosamente no slot. Caso não resolva, provavelmente a placa de vídeo está danificada.  
  
**9 Bips:**   
Erro na memória ROM (rom checksum error): Problemas com a memória Flash, onde está gravado o BIOS. Isto pode ser causado por um dano físico no chip do BIOS, por um upgrade de BIOS mal sucedido ou mesmo pela ação de um vírus da linhagem do Chernobil.   
  
**10 Bips:**   
Falha no CMOS shutdown register (CMOS shutdown register error): O chamado de shutdown register enviado pelo CMOS apresentou erro. Este problema é causado por algum defeito no CMOS. Nesse caso será um problema físico do chip, não restando outra opção senão trocar a placa mãe.  
  
**11 Bips:**  
Problemas com a memória cache (cache memory bad): Foi detectado um erro na memória cache. Geralmente quando isso acontece, o BIOS consegue inicializar o sistema normalmente, desabilitando a memória cache. Mas, claro, isso não é desejável, pois deteriora muito o desempenho do sistema. Uma coisa a ser tentada é entrar no Setup e aumentar os tempos de espera da memória cache. Muitas vezes com esse "refresco" conseguimos que ela volte a funcionar normalmente.  
  
  
**Códigos de erro do BIOS  
Modelo: AWARD BIOS Tone POST Codes**  
  
Apito \_\_\_\_\_\_\_\_\_\_\_\_\_\_Condição de Erro   
**1 longo, 2 curtos**  
Erro de Display - não é possível mostrar outras informações   
  
Qualquer outro............ (Erro de memória RAM)   
  
  
**Códigos de erro do BIOS  
Modelo: Phoenix BIOS Tone POST Codes**  
  
  
Apito \_\_\_\_\_\_\_\_\_\_\_\_\_Condição   
  
**Nenhum**  
teste de registro de CPU   
teste dos 64K RAM iniciais   
Carregamento do vetor de interrupção   
falha de força CMOS/cálculo do checksum   
Validação de configuração de vídeo   
vídeo funcionando com vídeo ROM   
vídeo funcional   
vídeo Monocromático funcional   
vídeo CGA funcional   
  
**1-1-3**  
CMOS write/read   
**1-1-4**  
ROM BIOS checksum   
**1-2-1**  
Timer do Sistema   
**1-2-2**  
inicialização do DMA   
**1-2-3**  
registro da página de DMA (write/read)   
**1-3-1**  
verificação da atualização da memória RAM   
**1-3-3**  
chip dos 64K RAM iniciais ou linha de dados   
**1-3-4**  
lógica odd/even dos 64K RAM iniciais   
**1-4-1**  
endereço de linha dos 64K RAM iniciais   
**1-4-2**  
falha de paridade nos 64K RAM iniciais   
**2-1-1**  
Bit 0, 64K RAM iniciais   
**2-1-2**  
Bit 1, 64K RAM iniciais   
**2-1-3**  
Bit 2, 64K RAM iniciais   
**2-1-4**  
Bit 3, 64K RAM iniciais   
**2-2-1**  
Bit 4, 64K RAM iniciais   
**2-2-2**  
Bit 5, 64K RAM iniciais   
**2-2-3**  
Bit 6, 64K RAM iniciais   
**2-2-4**  
Bit 7, 64K RAM iniciais   
**2-3-1**  
Bit 8, 64K RAM iniciais   
**2-3-2**  
Bit 9, 64K RAM iniciais   
**2-3-3**  
Bit 10, 64K RAM iniciais   
**2-3-4**  
Bit 11, 64K RAM iniciais   
**2-4-1**  
Bit 12, 64K RAM iniciais   
**2-4-2**  
Bit 13, 64K RAM iniciais   
**2-4-3**  
Bit 14, 64K RAM iniciais   
**2-4-4**  
Bit 15, 64K RAM iniciais   
**3-1-1**  
registro de DMA Slave   
**3-1-2**  
registro de DMA Master   
**3-1-3**  
Registrador da interrupção Master   
**3-1-4**  
Registrador da interrupção Slave   
**3-2-4**  
controlador de teclado   
**3-3-4**  
inicialização do vídeo   
**3-4-1**  
retrace do vídeo   
**3-4-2**  
procura por ROM de vídeo em processamento   
**4-2-1**  
teste da interrupção do Timer   
**4-2-2**  
teste de Shutdown   
**4-2-3**  
falha na porta A20   
**4-2-4**  
interrupção inesperada em modo protegido  
**4-3-1**  
teste de RAM (endereço da falha >FFFFh)   
**4-3-3**  
Intervalo do timer canal 2   
**4-3-4**  
relógio do sistema   
**4-4-1**  
porta Serial   
**4-4-2**  
porta Paralela   
**4-4-3**  
teste do co-processador matemático   
**1-1-2**  
\* seleção da placa de sistema   
**1-1-3**  
\* Extender CMOS RAM  
  
  
**Códigos de erro do BIOS  
Modelo: IBM POST Tone Codes**   
  
  
Apito \_\_\_\_\_\_\_\_\_\_Condição   
**Nenhum**  
placa mãe, fonte   
  
[b]1 curto[b/]  
Sistema passou por todos os testes   
**2 curtos**  
Erro de display   
contínuo ................Placa mãe, fonte   
**1 longo, 1 curto**  
placa mães   
**1 longo, 2 curtos**  
placa de vídeo   
**1 longo, 3 curtos**  
EGA   
**3 longos**  
cartão 3270   
  
  
Referências:   
  
\* AMI BIOS: <http://www.amibios.com>   
\* Phoenix BIOS: <http://www.phoenix.com/index.html>   
\* AWARD BIOS: <http://www.phoenix.com/pcuser/awardbios/Award.html>   
  
Colaboração:   
Usuário: Pink  
  
  
![](http://www.rjrinformatica.ubbi.com.br/indexlogo.jpg)  
Raimundo Junior  
Curitiba-PR  
(41) 9113-1909

29-09-2005 por
[**dimenight**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=35941)

erro na boot!

ola galera! meu problema é que, ao ligar meu PC aparece a mensagem de que o nao foi possivel dar o boot, e que tera que inserir o diskete. E as vezes aparece que nehum HD esta instalado o PC. Tenho dois HD de 40 Gb cada, e meu PC é um AMD Atlhon XP, 512 de RAM. Agradeço a colaboração. Abraços!!!

30-09-2005 por
[**Bug 666**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=3961)

Kra...naum sei aonde você pesquisou nem parei pra confirmar tais informações...porém creio eu que sejam de total veracidade e mereça um local de destaque aki na sala....PARABÉNS!!!

30-09-2005 por
[**soulstaker**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=25311)

Citação:

|  |
| --- |
| Postado Originalmente por **Bug 666**  Kra...naum sei aonde você pesquisou nem parei pra confirmar tais informações...porém creio eu que sejam de total vera... |

assino em baixo..... fico imaginando o trabalho pra reunir todas essas informaçoes....

30-09-2005 por
[**masauski**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=34367)

Ótimo post, merece um pinned!

01-10-2005 por
[**dimenight**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=35941)

então, o q foi q disse de errado. podem me explicar heim?  
abraços!!!

01-10-2005 por
[**Dan Jacques**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=32723)

Mt bom! Taí, gostei msm! Pena que a galera que colocou o DVD-RAM aki no meu micro deixou o speaker desligado :roll: ... Mas vai ajudar muito a galera que estiver com problemas ou quem quiser aprender pra entrar na profissão (como eu, com 14 aninhos). Fui!!!

21-10-2005 por
[**zancanaro**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=11416)

Citação:

|  |
| --- |
| Postado Originalmente por **Larvitar**  Mt bom! Taí, gostei msm! Pena que a galera que colocou o DVD-RAM aki no meu micro deixou o speaker desligado :roll: ... |

E quando a máquina desliga e fica apitando sem parar um barulhinho que parece um alarme ou uma sirene de bombeiro? Uma placa da abit KV7 com um Semprom 2600 e uma memo sansung 512.

21-10-2005 por
[**Robson Pereira**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=11856)

RJR, sempre ajudando a gente. Parabéns mesmo pela iniciativa

22-10-2005 por
[**soulstaker**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=25311)

Citação:

|  |
| --- |
| Postado Originalmente por **zancanaro**  E quando a máquina desliga e fica apitando sem parar um barulhinho que parece um alarme ou uma sirene de bombeiro? Um... |

aki na minha nf7-s acontece isso qdo a temperatura do cpu fica alta demais.......

22-10-2005 por
[**Dan Jacques**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=32723)

Pode ser um aviso aos overclockers de plantão! Dizendo: Ei, teu processador tá pedindo arrego!!! :mrgreen: :twisted:

29-10-2006 por
[**hmatzenbacher**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=86628)

tá... mas e se ele dá um bip curto... só que nada aparece no meu monitor?  
  
é que eu montei um pc novo aqui, e aconteceu isso...  
  
o monitor tá funcionando, que eu já testei noutro lugar...  
  
que será que pode ser?

03-12-2006 por
[**silvacd**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=54411)

Coitado do dimenight...te esqueçeram né  
Bom...Primeiro precisa ver se os cabos dos Hds estão bem conectados.  
É bom dar uma apertada geral nos seus componentes da Placa Mãe;  
Depois, saber qual é seu sistema operacional, depois tenta entrar no modo seguro e ver se reinicia e entra na Recuperação do Sistema e recupera o último antes de dar pau.  
Tem vários esquemas amigo, mas precisa ir vendo passo a passo cada um para resolver.

05-01-2007 por
[**Celipe.com**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=231581)

Solução de problemas de apitos - Bip's no PC

Bom, eu tbm tô com o mesmo problema, tenho 1 PC quando ligo ele, ele dá um bip, pára, dá outro bip, em questão de segundos e não dá nada no monitor. Troquei a placa de vídeo e não adiantou, troquei a memória ram e tbm nada resolveu. O que devo fazer??? ![880982ced09374480e062fef2bbe6089.gif](hardware-com-br--codigo-de-erros-de-todos-os-bios-bip/880982ced09374480e062fef2bbe6089.gif)   
Minha placa é antiga SIS 5595.  
Por favor me ajude a solucionar essa parada. Pois eu preciso muito deste velho computador pra trabalho. Se alguém puder me ajudar, desde já agradeço.![755d1c6ddf28cf6d3784bf89361a1a35.gif](hardware-com-br--codigo-de-erros-de-todos-os-bios-bip/755d1c6ddf28cf6d3784bf89361a1a35.gif)   
  
Celipe.com

02-02-2007 por
[**vovojr**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=65318)

Muito bom, ajuda muito.  
Brigadão.

19-02-2007 por
[**Agneles**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=266639)

Ola amigos gostaria de saber como que eu faco. Coloquei 2 pentes de memorias RAM no meu pc tdos dois PC 2600 166mhz, um de 128 e o outro de 256 mhz , so que meu pc so esta reconhendo 248 mhz dos 2 .  
Minha placa mae pcchips M825G V9.2a.  
Obrigado !

10-03-2007 por
[**sandro ribeiro**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=280236)

tenho um pentium mmx quando ligo ele aparece as seguintes mensagens:  
1962 erro de sequencia de inicializacao.  
8603 erro de dispositivo indicador.  
ele nao inicia o windows 98 que esta no hd.

12-03-2007 por
[**andre9001**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=281038)

mtu bom essa dica da bios

12-03-2007 por
[**andre9001**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=281038)

Citação:

|  |
| --- |
| Postado Originalmente por **sandro ribeiro**  tenho um pentium mmx quando ligo ele aparece as seguintes mensagens:  1962 erro de sequencia de inicializacao.  8603 erro de dispositivo indicador.  ele nao inicia o windows 98 que esta no hd. |

meu amigo verifica se a placa mae ta localizando o hd tenta localizar pela bios.

14-03-2007 por
[**Dú Paulista**](http://www.hardware.com.br/comunidade/bios-tutorial/145689/member.php?s=88150659b5bb34116203c32539517cbe&u=271074)

**Ótimo tópico Amigo**  
**Ajudou bastante no meu trabalho...**  
  
  
**Vlw**
