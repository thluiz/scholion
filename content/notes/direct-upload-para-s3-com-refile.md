---
title: "[Small Bites] Direct Upload para S3: a Solução Definitiva!"
date: '2014-12-18T16:50:10-03:00'
category: webclip
summary: 'O texto defende o upload direto do navegador para o S3 com Refile para evitar sobrecarga do servidor, timeout no Heroku e o custo de fazer a aplicação intermediária no processo.'
tags: ["refile", "s3", "upload-direto", "cloudfront"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "[Small Bites] Direct Upload para S3: a Solução Definitiva! | AkitaOnRails.com - Learn about Ruby, Rails, and all new technologies that are trending right now!"
    url: "http://www.akitaonrails.com/2014/12/18/small-bites-direct-upload-para-s3-a-solucao-definitiva#.VJMv3ivF_OM"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2014-12/akitaonrails-com--direct-upload-para-s3-com-refile.md"
    kind: repo
---

O texto defende o upload direto do navegador para o S3 com Refile para evitar sobrecarga do servidor, timeout no Heroku e o custo de fazer a aplicação intermediária no processo. Também aponta que guardar arquivos no disco local ou em BLOB no banco traz problemas de escala.

Apresenta um passo a passo para Rails com Refile, incluindo gems, configuração do S3 e CORS, campo no model, campo no formulário, whitelist de parâmetros e JavaScript para tratar eventos de upload. No fim, recomenda usar CloudFront na frente do S3 e configurar o host do Refile para servir as imagens pelo CDN.

## Fichamento

- Uploads tradicionais fazem o servidor web receber o arquivo primeiro e isso pesa com arquivos grandes, conexões lentas e timeout fixo do Heroku.
- Salvar arquivos no disco do servidor complica a escala quando a aplicação precisa de múltiplos servidores em balanceamento de carga.
- Guardar binários em campos BLOB no banco é descartado pelo texto.
- Enviar o arquivo para o storage pela aplicação ainda cria duas etapas de upload e deixa tudo mais lento.
- O texto recomenda Refile no lugar de Paperclip, Carrierwave e Dragonfly para esse caso.
- O fluxo proposto faz o upload direto do browser para o S3, sem passar o tráfego pelo servidor da aplicação.
- O Refile usa uma chave em `cache/` antes e depois copia para `store/` quando o formulário é enviado.
- A configuração pedida inclui gems, arquivo de inicialização, credenciais do S3 e CORS no bucket.
- O model recebe `profile_image` e o formulário usa `attachment_field` com `direct: true` e `presigned: true`.
- O controller precisa permitir `profile_image` e `profile_image_cache_id`.
- O JavaScript do Refile entra para tratar eventos de upload e desabilitar o submit durante o envio.
- O texto recomenda CloudFront na frente do S3 e o uso de `Refile.host` apontando para o domínio do CDN.
