---
url: "https://imasters.com.br/banco-de-dados/codificar-video-com-filas-de-trabalho-mongodb"
captured_at: "2012-05-17T11:28:37-03:00"
title: "Codificar vídeo com filas de trabalho MongoDB"
domain: "imasters-com-br"
---

A arquitetura da web está crescendo constantemente e cada vez mais complexa. Por um lado, os websites normalmente consistiam em arquivos estáticos em um servidor da web. Agora, até mesmo websites simples, com pouca ou nenhuma interatividade, normalmente são dinâmicos, executados em um sistema de gerenciamento de conteúdo suportado por um banco de dados.

  

Ainda assim, os aplicativos da web alcançaram um certo nível de padronização - eles começam com uma arquitetura semelhante. Talvez imagine um site com um único servidor da web e um único servidor de banco de dados, eles podem até ser a mesma máquina. Quando uma solicitação chega, o servidor da web se comunica com o servidor de banco de dados. Com base na solicitação, o servidor da web normalmente consulta o servidor de banco de dados e pode inserir, excluir e assim por diante. O servidor da web então responde ao usuário com uma resposta adequadamente formatada. Conforme o aplicativo é escalado, mais servidores da web e servidores de banco de dados envolvem-se.

  

Conforme a arquitetura cresce, o padrão básico permanece: uma solicitação chega, os dados são processados e uma resposta é enviada de volta. Entretanto, eventualmente isso não é bom o bastante. Algumas solicitações demoram muito e requerem que o usuário espere. É necessário mover essas solicitações para fora do ciclo de solicitação-resposta. Para resolver este problema, você requer uma fila de trabalho.

  

#### O que é uma fila de trabalho?

  

Uma fila de trabalho é uma fila simples - o trabalho é inserido por produtores e extraído por trabalhadores. As filas de trabalho separam a descoberta ou criação de uma tarefa a partir da execução real da tarefa. Isto é útil, pois a execução da tarefa geralmente é mais intensiva em recursos que a programação da tarefa. Quando a tarefa é programada, é possível relatar sucesso imediatamente ao usuário final, depois, a execução real de sua tarefa ocorre. Isto é importante para aplicativos da web, pois leva tarefas de longa execução para fora do ciclo solicitação-resposta, dando aos usuários um feedback imediato. Os usuários normalmente são muito mais tolerantes a latência que não é imediatamente exposta na interface do usuário, por isso o processamento off-line por meio de filas de trabalho é tão importante.

  

Há muitas abordagens para criar filas de trabalho. Uma opção, embora ingênua, é usar um sistema de gerenciamento de banco de dados relacional (RDBMS). Isto é simples de implementar, pois muitas arquiteturas já têm um sistema de banco de dados como o MySQL. Entretanto, o desempenho é menor que o ideal comparado a outras abordagens. A conformidade com a atomicidade, consistência, isolação e durabilidade (ACID) necessária para RDBMS não é necessária para este cenário e impacta negativamente o desempenho. Um sistema mais simples pode executar melhor.

  

Um sistema que ganhou popularidade por este uso é o Redis. É um armazenamento de dados de valor chave, como o memcached altamente popular, mas com mais recursos. Por exemplo, o Redis possui suporte para push e aparecimento de elementos em listas de uma forma altamente escalável e eficiente. O Resque, geralmente usado com Ruby on Rails, é um sistema desenvolvido sobre o Redis (consulte "Recursos" para obter detalhes adicionais). Entretanto, o Redis suporta apenas primitivas simples. Não é possível inserir objetos complexos nas listas e há suporte relativamente limitado para gerenciar itens nessas listas.

  

Como alternativa, muitos sistemas usam um intermediário de mensagem, como o Apache ActiveMQ ou o RabbitMQ. Embora esses sistemas sejam rápidos e escaláveis, eles estão designados para mensagens simples. Se desejar executar relatório incomum em suas filas de trabalho ou modificar itens nas filas, estará preso, porque os intermediários de mensagens raramente oferecem esses recursos. Felizmente, uma solução eficiente e escalável está disponível: MongoDB.

  

O MongoDB permite criar filas que contêm dados aninhados complexos. Sua semântica bloqueadora garante que não passará por problemas com simultaneidade e sua escalabilidade garante que é possível executar grandes sistemas. Como o MongoDB é um banco de dados relacional eficiente, é possível executar relatório sólido em sua fila e priorizar por critérios complexos. Entretanto, o MongoDB não é um RDBMS tradicional. Por exemplo, ele não suporta consultas Structured Query Language (SQL).

  

O MongoDB possui muitos recursos atraentes além do desempenho excelente para filas de trabalho, como a abordagem flexível e sem esquema. Ele suporta estruturas de dados aninhados, o que significa que pode até armazenar subdocumentos. Como é um armazenamento de dados de recursos mais completos que o Redis, ele fornece um conjunto mais rico de funções de gerenciamento para que seja possível visualizar, consultar, atualizar e excluir tarefas facilmente com critérios arbitrários.

  

#### Um exemplo de codificação de vídeo com filas de trabalho do MongoDB

  

Este tipo de abordagem é útil em uma ampla variedade de situações. Por exemplo, suponha que há vários sites remotos, cada um com um número de câmeras de segurança. Devido ao grande número de locais e o fato de que a alta segurança seria um exagero, essas câmeras de segurança tiram fotos a cada cinco segundos. Você é incumbido de coletar essas fotos e codificá-las em vídeos que são armazenados em um local central. Seu colega de trabalho já gravou um programa para fazer upload de arquivos compactados (.zip) que contêm fotos em um servidor remoto. Para este exemplo, você coleta e codifica as fotos usando uma fila de trabalho MongoDB acoplada ao FFmpeg, que é um codificador de vídeo aberto. Você codifica o vídeo no Theora, um codec de vídeo aberto.

  

A Listagem 1 mostra um pouco do código que monitora um diretório para uploads e depois enfileira todos os arquivos que encontrar.

  

```
 require 'lib/init'  
   
 require 'rb-inotify'  
   
   
 notifier = INotify::Notifier.new  
   
   
 watch_path = ARGV[1] || @app_config[:watch_path]  
   
   
 puts "watching #{watch_path}..."  
   
   
 # Use rb-inotify to watch the directory for changes:  
   
   
 notifier.watch(watch_path, :moved_to, :create) do |event|  
   
   
  filename = "#{watch_path}/#{event.name}"  
   
  file_size = File.size(filename)   
   
  file_type = `file -b #{Escape.shell_command(filename)}`.strip   
   
   
  new_record = { :path=>filename,   
   
  :file_size=>file_size,   
   
  :file_type=>file_type,   
   
  :in_progress=>false,   
   
  :encoded=>false }  
   
   
  @queue_collection.insert(new_record) # enqueue the record  
   
   
 endnotifier.run
```

  

*Lista 1. O arquivo monitor.rb*

  

Observe que a Listagem 1 inclui uma referência ao arquivo lib/init.rb. O código para esse arquivo é mostrado na Listagem 2.

  

```
 require 'rubygems'  
   
 require 'yaml'  
   
 require 'escape'  
   
 require 'mongo'  
   
   
 default_app_settings = {:watch_path=>'./incoming',   
   
  :encoded_path=>'./encoded',  
   
  :frames_per_second=>0.25}  
   
   
 @app_config = default_app_settings  
   
   
 if File.exists?('config/app.yml')  
   
  @app_config.merge!(YAML.load(File.open('config/app.yml')) || {})   
   
 end  
   
   
 Dir.mkdir(@app_config[:watch_path]) unless File.exists?(@app_config[:watch_path])  
   
 Dir.mkdir(@app_config[:encoded_path]) unless File.exists?(@app_config[:encoded_path])  
   
   
 default_mongo_settings = {:hostname=>'127.0.0.1',   
   
  :port=>27017,   
   
  :database=>'sample_db',   
   
  :collection=>'encode_queue'}   
   
   
 mongo_config = default_mongo_settings  
   
   
 if File.exists?('config/mongo.yml')  
   
  mongo_config.merge!(YAML.load(File.open('config/mongo.yml')) || {})   
   
   
 end@conn = Mongo::Connection.new(mongo_config[:hostname], mongo_config[:port])  
   
 @db = @conn[mongo_config[:database]]  
   
 @queue_collection = @db[mongo_config[:collection]]
```

  

*Lista 2. O arquivo lib/init.rb*

  

O código na Listagem 1 usa o gem rb-inotify para monitorar o diretório em que os arquivos de entrada estão armazenados. Por padrão, esse arquivo é chamado simplesmente de entrada. Instale rb-inotify com vários outros gems necessários, como mostrado na Listagem 3.

  

```
  sudo gem install rb-inotify mongo
```

  

*Lista 3. Instalando Gems*

  

O script inicializador na Listagem 2 contém configurações padrão para o aplicativo e sua conexão ao MongoDB. É possível substituir essas configurações criando um diretório chamado config e incluindo dois arquivos YAML, app.yml e mongo.yml, nesse diretório. A Listagem 1 usa essas configurações para monitorar os arquivos de entrada. O gem rb-inotify usa o recurso inotify do Linux® para executar uma parte do código sempre que um arquivo for movido ou criado no diretório de entrada. O gem rb-inotify suporta outros tipos de eventos, como exclusões e modificações, mas não são importantes para este exemplo.

  

Quando ele detecta um novo arquivo, o script do monitor insere um registro na coleção do MongoDB que inclui o caminho, tamanho de arquivo e tipo de arquivo do arquivo. O script do monitor usa o comando file do Linux para recuperar o tipo de arquivo, que pode ser útil para diagnosticar rapidamente problemas, pois é possível considerar registros de banco de dados para ver se o tipo de arquivo parece ser correto. Se um tipo de arquivo for obviamente incorreto (por exemplo, é uma planilha LibreOffice e está esperando um arquivo compactado), então será possível determinar rapidamente que a falha é uma entrada inválida em vez de um erro de script.

  

#### Processando a fila

  

Agora que você possui tarefas presentes na fila, é necessário processar essas tarefas. Felizmente, como você pode ver na Listagem 4, isto é fácil.

  

```
 require 'lib/init'  
   
   
 puts "running queue with PID #{Process.pid}"  
   
   
 time_between_checks = 5 # in seconds   
   
 encoder_information = {:hostname=>`hostname`, :process_id=>Process.pid}  
   
   
 while true  
   
  # Search through the queue; if nothing is present,   
   
  # then the MongoDB API throws an exception.   
   
  # We trap that exception, and retry until something is found.  
   
   
  row = @queue_collection.find_and_modify(  
   
  :query=>{:in_progress=>false,   
   
  :encoded=>false},   
   
  :update=>{:$set=>{:in_progress=>true}}  
   
  ) rescue (sleep(time_between_checks); retry )  
   
  if row   
   
  # If something is found,   
   
  # then we use the encode_zip_file script to encode it:  
   
   
  # Create a filename for output video:  
   
  timestamp = Time.now.strftime("%d_%m_%Y_%H%M%p")  
   
  outfile = File.join(@app_config[:encoded_path],   
   
  "video_" <<  
   
  "#{row['_id'].to_s}.ogv")  
   
   
  infile = row['path']  
   
  cmd = "ruby encode_zip_file.rb " <<   
   
  Escape.shell_command(infile) << " " <<  
   
  Escape.shell_command(outfile)  
   
   
  output = `#{cmd} 2>&1` # Redirect STDERR to STDOUT,   
   
  # so that we get all of the output  
   
   
  @queue_collection.update({:_id=>row["_id"]},   
   
  {:$set=>{:encoder=>encoder_information,   
   
  :encoded_video=>outfile,  
   
  :output=>output,   
   
  :encoded=>true,   
   
  :in_progress=>false}})   
   
   
  end  
   
 end
```

  

*Lista 4. O arquivo queue\_runner.rb*

  

Este código é executado em uma verificação de loop constante para novo trabalho. Ele usa o comando do MongoDB find\_and\_modify , que possui um efeito duplo. Como o nome implica, o primeiro comando encontra um registro e depois atualiza esse registro em uma segunda operação atômica. Esse comando afeta somente um registro por vez, então você só recebe uma tarefa por vez. A cláusula de consulta do comando find\_and\_modify garante que não trabalhe em tarefas que já estejam processadas ou estejam sendo codificadas por outros processos. A cláusula de atualização do comando find\_and\_modify configura o sinalizador in\_progress para que outros processos não comecem a funcionar na tarefa. Quando nenhum registro é encontrado, o MongoDB lança uma exceção. O código resgata essa exceção, fica em espera em um intervalo de pesquisa e depois tenta novamente a operação.

  

Quando o código encontra um registro, ele o processa. Ele cria um nome para o nome de arquivo baseado no ID do Mongo, que é garantido como exclusivo. Então, ele chama o script encode\_zip\_file.rb, que é discutido na próxima seção. O código atualiza o registro. O registro não está mais em andamento porque está codificado. O código também atualiza o registro para incluir o caminho de saída. Então, se desejar fazer trabalho adicional com o arquivo de vídeo, como exibi-lo ao usuário, é possível. Por fim, ele inclui as informações (nome do host, ID do processo e assim por diante) no processo de codificador atual.

  

Observe que, para simplicidade, este script somente acessa arquivos armazenados localmente. Entretanto, é possível estendê-lo facilmente de modo que faça download de arquivos usando File Transfer Protocol (FTP), Hypertext Transfer Protocol (HTTP) ou um mecanismo semelhante.

  

#### Codificando o Filme

  

Como é possível ver na Listagem 5, o script encode\_zip\_file.rb usa FFmpeg para codificar o vídeo.

  

```
 require 'lib/init'  
   
 require 'ftools'  
   
 require 'tmpdir'  
   
 require 'pathname'  
   
   
 (puts "usage: #{$0} INPUT_FILE OUTPUT_FILE"; exit) unless ARGV.length == 2  
   
   
 input_file_raw = ARGV.first  
   
 output_file = ARGV.last  
   
   
 input = Pathname.new(input_file_raw).realpath.to_s  
   
 puts "processing #{input}"  
   
   
 temporary_directory = Dir.mktmpdir  
   
 temporary_image_directory = File.join(temporary_directory, 'images')  
   
   
 # Create directory to store images  
   
 Dir.mkdir(temporary_image_directory)  
   
   
 # Unzip zip file into temporary image directory:  
   
 cmd = "cd #{temporary_image_directory}; unzip #{Escape.shell_command(input)}"  
   
   
 `#{cmd}`  
   
   
 input_frames = Dir.glob("#{temporary_image_directory}/*")  
   
   
 index = 0  
   
   
 target_file_extension = File.extname(input_frames.first).downcase  
   
   
 # Sort input images by creation time,  
   
 # then copy them to the root of the temporary directory:  
   
   
 input_frames.sort_by { |f| File.ctime(f) }.each do |f|  
   
   
  # ffmpeg needs a consistent file format, so we'll reformat the filenames:  
   
  target_file = File.join(temporary_directory,  
   
  "frame_#{'%03i' % index}#{target_file_extension}")  
   
  index = index + 1  
   
  File.copy(f, target_file)  
   
 end  
   
   
 frames_per_second = @app_config[:frames_per_second]  
   
   
 # Encode the video:  
   
 cmd = "ffmpeg -r #{frames_per_second} " <<  
   
  "-i #{temporary_directory}/frame_%03d#{target_file_extension} " <<  
   
  "-vcodec libtheora #{output_file}"  
   
   
 puts `#{cmd}`
```

  

*Lista 5. O script encode\_zip\_file.rb*

  

Este script pega um arquivo de entrada e um de saída da linha de comando, descompacta-os em um diretório de memória e depois renomeia-os, pois FFmpeg espera uma convenção de nomenclatura consistente para seus quadros. Ao classificar os arquivos e, depois, renomeá-los, o script permite que as imagens de arquivo compactadas tenham nomenclatura arbitrária enquanto ainda permitem que o FFmpeg processe os quadros.

  

O FFmpeg possui um conjunto direto de opções. A opção -r configura o número de quadros por segundo. A opção -i configura o arquivo de entrada, que pode ser outro arquivo de vídeo se, por exemplo, desejar fazer a transcodificação. Neste caso, no entanto, você está trabalhando a partir de um conjunto de arquivos de entrada. A parte frame\_%03d significa que o FFmpeg espera que os arquivos sejam chamados de frame\_000, frame\_001 e assim por diante. O script usa qualquer extensão que o primeiro arquivo no archive de arquivo compactado tenha, presumindo que todos os arquivos tenham um formato de arquivo semelhante. Por fim, a opção -vcodec libtheora instrui o FFmpeg a usar o codec Theora. O script então simplesmente executa o comando e publica os resultados.

  

Agora, você tem um sistema em funcionamento para codificar vídeos. É possível verificar isto iniciando o MongoDB e usando os comandos mostrados na Listagem 6 em duas janelas diferentes.

  

```
  ruby monitor.rb  
   
  ruby queue_runner.rb
```

  

*Lista 6. Iniciando o Sistema*

  

Agora é possível ver dois diretórios pelo script do inicializador: de entrada e codificado. Simplesmente crie um arquivo compactado que contenha várias imagens Joint Photographic Experts Group (JPEG) e copie-o no diretório de entrada. Você deve ver um arquivo .ogv aparecer no diretório codificado que pode ser aberto no Firefox para visualizar um vídeo de suas imagens.

  

#### Conclusão

  

Como pode ver, usar o MongoDB é simples e fácil. É possível estender as abordagens mencionadas neste artigo para que funcionem com uma grande variedade de sistemas. O MongoDB possui um rico conjunto de recursos para modelar dados aninhados e você pode usar isso facilmente para lidar com dados de tarefas mais complexas. Em suma, as filas de trabalho orientadas a MongoDB são uma abordagem eficiente e flexível que pode ser escalada para grandes filas. Você não vai se arrepender de usá-las em seu aplicativo.

  

#### Recursos

  

**Aprender**

  

A documentação do MongoDB explica todos os detalhes sobre as[operações atômicas do MongoDB](http://www.mongodb.org/display/DOCS/Atomic+Operations), como o comando find\_and\_modify usado neste artigo.

  

A documentação do gem [rb-inotify abrange](http://rubydoc.info/github/nex3/rb-inotify/master/file/README.md) o uso das ligações libinotify usadas neste artigo.

  

As instruções [A documentação da interface da linha de comando do FFmpeg](http://ffmpeg.org/ffmpeg.html) mostra como usar argumentos da linha de comando do ffmpeg .

  

Encontre muitas informações sobre instruções, ferramentas e atualizações de projetos para ajudá-lo a desenvolver com tecnologias de software livre e usá-las com produtos IBM na [Zona de software livre do developerWorks](http://www.ibm.com/developerworks/opensource/).

  

Fique por dentro dos[eventos técnicos e webcasts do developerWorks](http://www.ibm.com/developerworks/offers/techbriefings/events.html) com ênfase em uma série de produtos IBM e assuntos relacionados ao segmento de mercado de TI.

  

Participe de um [briefing gratuito do developerWorks Live!](http://www.ibm.com/developerworks/offers/techbriefings/) para se atualizar rapidamente sobre produtos e ferramentas IBM e tendências do segmento de mercado de TI.

  

Siga o [DeveloperWorks no Twitter](http://www.twitter.com/developerworks/).

  

Acompanhe as [demos do developerWorks](http://www.ibm.com/developerworks/offers/lp/demos/) que abrangem desde demos de instalação e configuração de produtos para iniciantes até funcionalidade avançada para desenvolvedores experientes.

**Obter produtos e tecnologias**

  

[MongoDB](http://www.mongodb.org/) é um banco de dados rápido, aberto e orientado a documentos.

  

[Apache ActiveMQ](http://activemq.apache.org/) é um sistema de mensagens aberto, que é outra boa forma para enfileirar trabalho.

  

[Resque](https://github.com/defunkt/resque) é um sistema para enfileirar tarefas usando o Redis.

  

Como você é interessado em aplicativos de banco de dados, talvez também se interesse no [DB2 Express-C](http://www.ibm.com/developerworks/downloads/im/udbexp/index.html)livre, disponível na [página de download de Avaliação do developerWorks](http://www.ibm.com/developerworks/downloads/index.html).

**Discutir**

  

Participe da [comunidade do developerWorks](http://www.ibm.com/developerworks/community/). Entre em contato com outros usuários do developerWorks, enquanto explora os blogs, fóruns, grupos e wikis orientados ao desenvolvedor.

**Sobre o autor:** David Berube é consultor, palestrante e autor de *Practical Rails Plugins, Practical Reporting with Ruby and Rails,* e *Practical Ruby Gems.* É possível entrar em contato com ele através do email [info@berubeconsulting.com](http://www.ibm.com/developerworks/br/library/os-mongodb-work-queues/info@berubeconsulting.com).

  
[anexo ausente]  
  

[![9bcafcd24ef5e7a319a7e300c0d5b221.gif](imasters-com-br--codificar-video-com-filas-de-trabalho-mongodb/9bcafcd24ef5e7a319a7e300c0d5b221.gif)](http://share.feedsportal.com/viral/sendEmail.cfm?lang=pt&amp;title=Codificar+v%C3%ADdeo+com+filas+de+trabalho+MongoDB&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24454%2Fmongodb%2Fcodificar-video-com-filas-de-trabalho-mongodb)

  

[![75b9131ce15803402621ad7d693d4dd1.gif](imasters-com-br--codificar-video-com-filas-de-trabalho-mongodb/75b9131ce15803402621ad7d693d4dd1.gif)](http://res.feedsportal.com/viral/bookmark_pt.cfm?title=Codificar+v%C3%ADdeo+com+filas+de+trabalho+MongoDB&amp;link=http%3A%2F%2Fimasters.com.br%2Fartigo%2F24454%2Fmongodb%2Fcodificar-video-com-filas-de-trabalho-mongodb)

  
  
  
[[anexo ausente]](http://da.feedsportal.com/r/134204340216/u/49/f/546640/c/33212/s/1f7234d2/a2.htm) [anexo ausente]  
  
[anexo ausente]  
  
  
  
  
from iMasters - <http://feedproxy.google.com/~r/imasters/~3/-Knf5TbMmOw/story01.htm>
