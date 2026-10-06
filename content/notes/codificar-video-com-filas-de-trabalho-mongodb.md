---
title: "Codificar vídeo com filas de trabalho MongoDB"
date: '2012-05-17T11:28:37-03:00'
category: webclip
summary: 'O texto explica filas de trabalho para tirar tarefas longas do ciclo solicitação-resposta e mostra um exemplo em Ruby que usa MongoDB, rb-inotify e FFmpeg para converter imagens em vídeo.'
tags: ["mongodb", "job-queues", "ffmpeg", "ruby"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Codificar vídeo com filas de trabalho MongoDB"
    url: "https://imasters.com.br/banco-de-dados/codificar-video-com-filas-de-trabalho-mongodb"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-05/imasters-com-br--codificar-video-com-filas-de-trabalho-mongodb.md"
    kind: repo
---

O texto apresenta filas de trabalho como forma de separar a criação da tarefa da sua execução, para que aplicações web respondam ao usuário sem esperar por processos longos. Compara essa abordagem com RDBMS, Redis e intermediários de mensagem, e destaca o MongoDB pela capacidade de guardar dados aninhados e gerenciar tarefas com critérios arbitrários.

## Fichamento

- Filas de trabalho separam a descoberta ou criação de uma tarefa da execução real da tarefa.
- Essa separação é útil porque tarefas longas saem do ciclo solicitação-resposta e o usuário recebe feedback imediato.
- O texto diz que um RDBMS pode ser uma opção simples, mas tende a ter desempenho inferior nesse cenário.
- O Redis é apresentado como uma alternativa popular, mas com suporte limitado a primitivas simples e pouca flexibilidade para gerenciar itens na fila.
- Sistemas de mensagens como Apache ActiveMQ e RabbitMQ são citados como rápidos e escaláveis, mas voltados a mensagens simples.
- O MongoDB é descrito como adequado para filas com dados aninhados complexos, sem esquema e com recursos de consulta, atualização e exclusão mais ricos.
- O exemplo usa várias câmeras de segurança em sites remotos, coleta fotos em arquivos compactados e as codifica em vídeo em um local central.
- O monitor.rb usa rb-inotify para observar o diretório de entrada e inserir na coleção do MongoDB registros com caminho, tamanho, tipo de arquivo e estado da tarefa.
- O queue_runner.rb usa find_and_modify para pegar uma tarefa por vez, marcar in_progress e evitar que outros processos trabalhem no mesmo item.
- Quando encontra um registro, o processo chama encode_zip_file.rb, salva o caminho do vídeo gerado e registra informações do codificador no documento.
- O script encode_zip_file.rb descompacta as imagens, reorganiza os nomes dos arquivos para o padrão esperado pelo FFmpeg e então codifica o vídeo com libtheora.
- O texto conclui que filas de trabalho orientadas a MongoDB são uma abordagem eficiente, flexível e escalável para filas grandes.
