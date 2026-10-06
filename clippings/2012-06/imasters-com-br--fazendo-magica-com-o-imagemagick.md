---
url: "http://imasters.com.br/artigo/24066/desenvolvimento/fazendo-magica-com-o-imagemagick"
captured_at: "2012-06-04T12:06:16-03:00"
title: "Fazendo mágica com o ImageMagick – iMasters"
domain: "imasters-com-br"
---

# Fazendo mágica com o ImageMagick

Segunda-feira, 09/04/2012 às 10h00, por [developerWorks Brasil](http://imasters.com.br/perfil/developerworks_brasil)

Arthur C. Clarke, escritor britânico de ficção científica, disse que "qualquer tecnologia suficientemente avançada é indistinguível da mágica". Como profissionais que usam a tecnologia avançada atual, fica difícil dizer que as nossas ferramentas não parecem mágicas. Imagine alguém de um passado não muito distante nos vendo usar a tecnologia moderna -, fazendo uma mágica atrás da outra para fotografar, transferir, processar e finalmente imprimir imagens de amigos, parentes, bichos, locais de trabalho e de nós mesmos.

ImageMagick é um nome genérico e chamativo que foi dado a um conjunto de programas que permitem criar, editar, compor e converter imagens digitais em mais de cem formatos diferentes. As ferramentas propriamente ditas consistem em programas e bibliotecas distintas, que oferecem aos seus esforços de manipulação de imagens as opções mais amplas possíveis para realizar essas tarefas, operacional e programaticamente.

Este artigo tem ênfase principalmente no uso dos utilitários de linha de comando convert e display. O ImageMagick é um conjunto variado de ferramentas e, ao final deste artigo, você provavelmente terá uma boa impressão do conjunto.

#### O ImageMagick é um editor

Em termos amplos, um programa de computador chamado de editor se destina a facilitar a criação, modificação e salvamento de certos tipos de dados digitais. Há tantos editores quantos tipos específicos de dados digitais. Há editores de texto para documentos, código do programa e scripts. Vi e Emacs são exemplos bem conhecidos. Para os dados de áudio, há editores como Audacity e Wavosaur. O ImageMagick oferece um editor especializado para a edição de imagens gráficas.

#### Para criar imagens de bitmap

Como muitos outros editores de imagem, o ImageMagick oferece um ambiente interativo de edição de imagem. Entretanto, o ImageMagick oferece interface de programação de aplicativos (APIs) abrangentes e programáveis para que várias linguagens de programação padrão também as usem. A comunidade de programadores do ImageMagick forneceu muitos programas úteis que podem ser escolhidos para editar a funcionalidade imaginada.

Para descrever a funcionalidade de manipulação de imagem, as figuras são melhores que as palavras, e o website do ImageMagick oferece um bom conjunto delas para ilustrar o efeito que cada uma das funções oferece. Consulte "Recursos" para obter um link para mais informações sobre manipulação de imagem.

#### Para editar imagens de bitmap

Existem mais de cem formatos gráficos de imagem que são de uso comum. Dessa forma, para simplificar o processo de edição das imagens já existentes, o ImageMagick oferece o programa convert para converter de um formato a outro e também converter as imagens para uma forma que otimize o editor interativo do próprio ImageMagick.

#### Para incorporar imagens a projetos

Já que um dos pontos fortes do ImageMagick é o recurso de script, é possível escrever scripts customizados para facilitar a incorporação de imagens a projetos especiais. Um exemplo disso é a customização automática de um conjunto de imagens de material de marketing com os dados pessoais de um cliente em perspectiva - nome, endereço, números de telefone, etc.

Para ver esse recurso em ação, observe a imagem simples do gato da minha filha e do meu genro, que coincidentemente se chama Merlin.

![95173f32ab38df6f275f18848d3c1d9a.jpg](imasters-com-br--fazendo-magica-com-o-imagemagick/95173f32ab38df6f275f18848d3c1d9a.jpg)

Para dar um título bonito à imagem, o seguinte comando pode ser usado:

```
$ convert bMerlin.jpg -font Ubuntu-Bold-Italic \
   -pointsize 56 -fill blue -annotate +25+70 \
   'Merlin, the Wizard of Cats' NewMerlin.jpg
 
```

Observação: se o sistema não possui a fonte Ubuntu-Bold-Italic, use o comando a seguir para listar as fontes disponíveis:

```
$ convert -list font
```

Depois do processamento, é obtida a imagem mostrada abaixo:

![9c552c9318d05d377dceceff9a1a16ee.jpg](imasters-com-br--fazendo-magica-com-o-imagemagick/9c552c9318d05d377dceceff9a1a16ee.jpg)

Como é possível ver, não é difícil fazer mágica com o ImageMagick. Basta praticar para saber como usar a ferramenta. Os programadores (ou feiticeiros) que criaram o ImageMagick documentaram muito bem a ferramenta no website. Recomenda-se acessá-lo para aprimorar os conhecimentos obtidos com este artigo (consulte "Recursos").

#### O ImageMagick é uma biblioteca de manipulação de imagens

A biblioteca de opções do programador com essa ferramenta eficiente é mais do que abrangente. Usando linguagens de programação bastante conhecidas, é possível incorporar a eficiência do ImageMagick por meio de APIs simples projetadas para cada linguagem. De scripts simples de bash dos comandos brutos do ImageMagick até a chamada de funções de API de linguagens, como C ou Perl, a programabilidade do ImageMagick o diferencia de muitas outras ferramentas de manipulação gráfica.

É possível optar por usar o editor interativo para fazer ajustes finos em uma imagem ou mudanças gerais em diversas imagens. O valor desse conjunto reside na capacidade de usar suas diversas ferramentas de edição.

#### Conversões entre formatos de imagem bastante difundidos

Existem mais de cem formatos diferentes de arquivos gráficos para imagens digitais. O ImageMagick permite contralar a situação da complexidade, porque pode trabalhar com muitos padrões diferentes.

O ImageMagick é móvel entre sistemas operacionais diferentes. Existem versões funcionais para Windows, UNIX e Linux, Mac OS X e Apple iOS. Este artigo tem ênfase na versão Ubuntu do Linux. Para fazer o download do código de origem ou da versão binária do seu sistema preferencial, consulte o link em Recursos.

#### Binário ou origem?

Como acontece com muitos sistemas de software livre, é necessário fazer uma escolha oficial ao obter o programa: compilar a partir do código de origem ou fazer o download de uma versão binária já compilada especificamente para o sistema. Os dois métodos oferecem vantagens, mas optamos por desenvolver o sistema a partir da origem.

#### Distribuição ou customizado?

Toda distribuição (ou "distro") tem o seu próprio método de incluir binários pré-construídos. Para instalar o ImageMagick nas distribuições que descendem do Debian Linux, como o Ubuntu, usamos um dos gerenciadores de pacote baseados na interface gráfica com o usuário, como o Synaptic Package Manager, ou uma operação de linha de comandos como:

```
$ sudo apt-get install imagemagick
```

Também é possível customizar o ImageMagick de acordo com o seu gosto. Por exemplo, modificar o local onde ele espera que os arquivos de configuração estejam ou alguma configuração específica da criação. Para fazer isso, use os comutadores de opção da linha de comando ao desenvolver o ImageMagick a partir da origem. É possível listar essas opções com o comando configure da seguinte forma:

```
$ ./configure --help
```

Muitas dessas opções são úteis quando há problemas para criá-lo na máquina.

#### Construindo o ImageMagick a partir da origem

A criação da maioria dos programas de software livre para computadores baseados em \*nix envolve três comandos, e o ImageMagick não é uma exceção. Os comandos padrão são:

- $ ./configure - O objetivo do script configure é criar um Makefile customizado para a próxima etapa. Ele executa metodicamente uma série de etapas para determinar a configuração da máquina e, em seguida, informa que alguma coisa crítica está faltando, como uma biblioteca necessária, ou que está tudo bem e o Makefile foi criado com êxito;
- $ make - O Makefile criado na etapa anterior é usado pelo programa make para desenvolver todos os programas que constituem o conjunto ImageMagick, juntamente com a documentação associada;
- $ sudo make install - O comando final copia os programas, a documentação e os arquivos de dados associados para o seu local permanente, onde todos os usuários do sistema esperam que eles estejam. Geralmente, isso significa o diretório /usr/local/bin.

#### Manipulação de imagens para os usuários

O ImageMagick é semelhante aos outros editores de imagem porque fornece um programa interativo para editar imagens. Depois de chamado, é possível acessar as ferramentas de manipulação de imagens acionadas por menu.

#### Criando imagens do zero

O editor interativo ImageMagick é chamado usando o comando display com ou sem um nome de arquivo associado. A interface é semelhante à de muitos outros programas de desenho, fácil de usar e acionada por menus.

Insira o comando display. É exibida a janela da figura a seguir:

![875def4f2ee31f16cb0e992c276fae28.jpg](imasters-com-br--fazendo-magica-com-o-imagemagick/875def4f2ee31f16cb0e992c276fae28.jpg)

Clique na janela e depois em File > New no menu para começar a criar a imagem de bitmap. Será necessário inserir a geometria da imagem e, em seguida, a cor do plano de fundo. Ao inserir a geometria da imagem, também existe a opção de usar uma gradação para as cores do plano de fundo.

Com a tela criada, é possível começar a usar as ferramentas de desenho para decorá-la. Clique em Image Edit > Draw. O modo é alterado, um novo menu é exibido e a funcionalidade do cursor da tela muda. Neste ponto, selecione uma ferramenta de desenho e coloque suas ideias na tela. É possível sair da funcionalidade Draw e das partes de Color da imagem, incluir efeitos especiais e ser criativo.

#### Editando imagens

É possível editar as imagens já existentes de várias formas. Ao inserir o comando display image-name , será possível usar o editor interativo descrito anteriormente, mas é possível usar as outras ferramentas do conjunto para manipular a imagem. O programa convert , por exemplo, oferece a capacidade de converter o arquivo de imagem para outro formato gráfico comum adequado para ambientes diferentes.

Para ver como isso é feito, usaremos um programa para gerar uma sequência de convites para uma "festa de gatos". Esse programa tem a forma de um script de bash, então, inicie um xterm e crie o primeiro arquivo da seguinte forma:

```
$ touch catcards $ chmod a+x catcards
```

Depois de criar o arquivo de script e torná-lo executável, a próxima etapa é abrir o seu editor favorito (por exemplo, Vi, Emacs) e inserir o código do programa do script de bash mostrado na Listagem 1 no arquivo catcards.

```
---
#!/bin/bash
# A "catcard" bash script for demonstrating ImageMagick
# and generating invitations to a "cat party."
# 20111115 by Bill Zimmerly.

# Find the "seq" command, to generate sequence numbers.

SEQ=`which seq`

# Create the guests file. Comment this
# out if "guests" is an external file.
# (Important Note: "cat" in this script
# has nothing to do with cats!)

cat > guests << EOF
Grandma
Aunt Linda
Uncle Dave
Aunt Rachael
Uncle Joe
Uncle Myk
EOF

# Read the guests into an array called "a."
# (Note: IFS is the field separator value,
# which in this case MUST be set for lines.)

old_IFS=$IFS
IFS=$'\n'
a=($(cat guests))

echo "Generating $((${#a[@]})) invitations to:"

# Generate the invitations.

for i in $($SEQ 0 $((${#a[@]} - 1)))
do
  # Use base=1 for human counting and
  # show it on the console.

  j=i
  ((j += 1))
  echo $j. ${a[$i]}

  # Prepare the file name.

  echo "Merlin"$j".jpg" > filename

  # Prepare the invitational text.

  echo ${a[$i]}", I love you and"       > text1
  echo "I want you to come to my"       > text2
  echo "cat party to scratch my belly." > text3
  echo "Sincerely,"                     > text4
  echo "Merlin"                         > text5

  # Use ImageMagick's "convert" command
  # to generate a new card.

  convert bMerlin.jpg \
    -font Ubuntu-Bold-Italic \
    -pointsize 24 -fill blue \
    -annotate +25+40 $(cat text1) \
    -annotate +25+70 $(cat text2) \
    -annotate +25+100 $(cat text3) \
    -annotate +25+130 $(cat text4) \
    -annotate +25+160 $(cat text5) \
    $(cat filename)

done# Restore the field separator value and clean up
# temporary files.

IFS=$old_IFS

rm guests
rm filename
rm text1
rm text2
rm text3
rm text4
rm text5

exit 0
---
```

Clique com o botão direito na figura em branco do gato Merlin - a primeira imagem - e salve-a no diretório onde o script catcards reside. (O script catcards precisa desse arquivo de imagem como dado.)

Finalmente, execute o script e liste os arquivos gerados, como mostra a Listagem 2.

```
$ ./catcards
Generating 6 invitations to:
1. Grandma
2. Aunt Linda
3. Uncle Dave
4. Aunt Rachael
5. Uncle Joe
6. Uncle Myk
$ ls Merlin*
```

Observe que agora há seis imagens novas no diretório. Exiba cada uma das imagens usando o comando display do ImageMagick e observe que são diferentes entre si:

```
$ display Merlin1.jpg
    .
    .
    .
   Etc.
```

Por exemplo, a figura 4 mostra a imagem do convite gerado para a tia Rachael.

![6a61c86af9c76710e115dba6f59a94fa.jpg](imasters-com-br--fazendo-magica-com-o-imagemagick/6a61c86af9c76710e115dba6f59a94fa.jpg)

É possível modificar esse programa facilmente para gerar material de vendas ou gráficos customizados para todos os seus clientes.

#### Manipulação de imagens para programadores

Os programadores podem incorporar a funcionalidade de manipulação de imagens de duas formas: por meio da API MagickWand em C ou da API MagickCore.

#### Usando a API MagickWand em C

Os criadores do ImageMagick criaram um programa de exemplo destinado a aumentar o contraste da imagem do Merlin (consulte Recursos para obter um link para mais detalhes sobre esse programa). A Listagem 3 mostra o código.

```
---
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <wand/MagickWand.h>

int main(int argc,char **argv)
{
#define QuantumScale  ((MagickRealType) 1.0/(MagickRealType) QuantumRange)
#define SigmoidalContrast(x) \
  (QuantumRange*(1.0/(1+exp(10.0*(0.5-QuantumScale*x)))-0.0066928509)*1.0092503)
#define ThrowWandException(wand) \
{ \
  char \
    *description; \
 \
  ExceptionType \
    severity; \
 \
  description=MagickGetException(wand,&severity); \
  (void) fprintf(stderr,"%s %s %lu %s\n",GetMagickModule(),description); \
  description=(char *) MagickRelinquishMemory(description); \
  exit(-1); \
}

  MagickBooleanType
    status;

  MagickPixelPacket
    pixel;

  MagickWand
    *contrast_wand,
    *image_wand;

  PixelIterator
    *contrast_iterator,
    *iterator;

  PixelWand
    **contrast_pixels,
    **pixels;

  register ssize_t
    x;

  size_t
    width;

  ssize_t
    y;

  if (argc != 3)
    {
      (void) fprintf(stdout,"Usage: %s image sigmoidal-image\n",argv[0]);
      exit(0);
    }
  /*
    Read an image.
  */
  MagickWandGenesis();
  image_wand=NewMagickWand();
  status=MagickReadImage(image_wand,argv[1]);
  if (status == MagickFalse)
    ThrowWandException(image_wand);
  contrast_wand=CloneMagickWand(image_wand);
  /*
    Sigmoidal non-linearity contrast control.
  */
  iterator=NewPixelIterator(image_wand);
  contrast_iterator=NewPixelIterator(contrast_wand);
  if ((iterator == (PixelIterator *) NULL) ||
      (contrast_iterator == (PixelIterator *) NULL))
    ThrowWandException(image_wand);
  for (y=0; y < (ssize_t) MagickGetImageHeight(image_wand); y++)
  {
    pixels=PixelGetNextIteratorRow(iterator,&width);
    contrast_pixels=PixelGetNextIteratorRow(contrast_iterator,&width);
    if ((pixels == (PixelWand **) NULL) ||
        (contrast_pixels == (PixelWand **) NULL))
      break;
    for (x=0; x < (ssize_t) width; x++)
    {
      PixelGetMagickColor(pixels[x],&pixel);
      pixel.red=SigmoidalContrast(pixel.red);
      pixel.green=SigmoidalContrast(pixel.green);
      pixel.blue=SigmoidalContrast(pixel.blue);
      pixel.index=SigmoidalContrast(pixel.index);
      PixelSetMagickColor(contrast_pixels[x],&pixel);
    }
    (void) PixelSyncIterator(contrast_iterator);
  }
  if (y < (ssize_t) MagickGetImageHeight(image_wand))
    ThrowWandException(image_wand);
  contrast_iterator=DestroyPixelIterator(contrast_iterator);
  iterator=DestroyPixelIterator(iterator);
  image_wand=DestroyMagickWand(image_wand);
  /*
    Write the image then destroy it.
  */
  status=MagickWriteImages(contrast_wand,argv[2],MagickTrue);
  if (status == MagickFalse)
    ThrowWandException(image_wand);
  contrast_wand=DestroyMagickWand(contrast_wand);
  MagickWandTerminus();
  return(0);
}
---
```

Se esse código de origem for colocado em um arquivo chamado *contrast.c,* será possível usar o comando a seguir para desenvolver o programa contrast :

```
$ cc `MagickWand-config \
     --cflags --cppflags` \
     -O2 -o wand wand.c \
     `MagickWand-config --ldflags --libs`
```

Quando o comando contrast for construído, será possível usá-lo desta forma para aumentar o contraste da foto do Merlin:

```
$ ./contrast bMerlin.jpg MerlinX.jpg
```

Compare a imagem na imagem baixo com as imagens de Merlin acima.

![6970fa491963aa22f3f35adaa1b8e770.jpg](imasters-com-br--fazendo-magica-com-o-imagemagick/6970fa491963aa22f3f35adaa1b8e770.jpg)

#### A API MagickCore

A interface de baixo nível entre as bibliotecas de processamento de imagem e os seus programas é a API MagickCore. Destina-se principalmente a ser usada pelo programador de sistema e fornecer a funcionalidade básica que normalmente não é vista nos níveis mais altos: inicializar o ambiente, criar instâncias de objetos, fazer cálculos de transformação de Fourier, etc.

#### Distribuindo projetos com bibliotecas ImageMagick

O ImageMagick é distribuído sob a licença de software livre do Apache 2.0, que possui alguns requisitos específicos para uso nos seus projetos. Em termos simples, é necessário incluir uma cópia completa da licença na distribuição do seu projeto e atribuí-la claramente a The Apache Software Foundation. Consulte Recursos para obter um link para os detalhes completos da licença Apache 2.0.

#### Conclusão

Na área dos editores de imagem, o conjunto ImageMagick se destaca como um eficiente kit de ferramentas para programadores para a criação e edição de arquivos de imagem. Como foi mostrado pelo script bash anterior e pelos exemplos de código em C, o kit de ferramentas é abrangente e útil para fazer mágica nos seus projetos relacionados a gráficos.

#### Recursos

**Aprender**

- Saiba mais sobre o [ImageMagick](http://www.imagemagick.org/) .
- Saiba mais sobre a manipulação de imagens por meio dos [exemplos de manipulação de imagem do ImageMagick](http://www.imagemagick.org/script/examples.php) .
- Antes de distribuir o seu projeto com o ImageMagick, certifique-se de entender os termos da [licença Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html) .
- A [Zona do developerWorks de software livre](http://www.ibm.com/developerworks/opensource/)  fornece muitas informações sobre ferramentas de software livre e de como utilizar tecnologias de software livre.
- Visite a seção [Safari bookstore](http://www.ibm.com/developerworks/apps/SendTo?bookstore=safari)  da biblioteca de e-reference para encontrar recursos técnicos específicos.
- Siga o [developerWorks no Twitter](http://www.ibm.com/developerworks/opensource/library/os-refactoringphp/twitter.com/developerworks) .

**Obter produtos e tecnologias**

- ImageMagick está disponível para download como [binário](http://www.imagemagick.org/script/binary-releases.php)  ou [origem](http://www.imagemagick.org/script/install-source.php) .
- É possível encontrar o programa contrast.c na página que descreve a [API de C MagickWand](http://www.imagemagick.org/script/magick-wand.php) .
- Inove seu próximo projeto de desenvolvimento de software livre com a [versão de teste do software IBM](http://www.ibm.com/developerworks/downloads/) , disponível para download ou em DVD.
- Saiba mais e [faça o download do Audacity](http://audacity.sourceforge.net/)  a partir da SourceForge.

**Discutir**

**Sobre o autor:** Bill Zimmerly é engenheiro do conhecimento, programador de sistemas de baixo nível com conhecimento de várias versões do UNIX e Microsoft® Windows® e livre-pensador que cultua o altar da Lógica. Suas paixões são criar novas tecnologias e escrever sobre elas. Mora na zona rural de Hillsboro, Missouri, onde o ar é fresco, as paisagens são inspiradoras e há várias vinícolas boas por perto. É possível entrar em contato com ele através do email [bill@zimmerly.com](http://imasters.com.br/artigo/24066/desenvolvimento/bill@zimmerly.com) .
