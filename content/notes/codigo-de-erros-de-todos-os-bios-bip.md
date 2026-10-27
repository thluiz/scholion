---
title: "Tutorial: Código de erros de todos os BIOS - BIP"
date: '2012-11-26T21:48:51-03:00'
category: webclip
summary: 'A página explica como o POST do BIOS identifica hardware na inicialização e lista códigos de bips de AMI, Award, Phoenix e IBM, com causas prováveis e orientações básicas de teste.'
tags: ["bios", "post", "bips", "hardware"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Tutorial: Código de erros de todos os BIOS - BIP"
    url: "http://www.hardware.com.br/comunidade/bios-tutorial/145689/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-11/hardware-com-br--codigo-de-erros-de-todos-os-bios-bip.md"
    kind: repo
---

A página explica que o BIOS executa o POST na inicialização para detectar o hardware instalado e verificar se os componentes principais estão funcionando. Quando encontra falhas graves, o BIOS pode sinalizar com sequências de bips, e o código varia conforme a marca do BIOS e, às vezes, a placa-mãe.

## Fichamento

- O POST verifica o hardware detectado no boot, como memória, processador, vídeo, discos, portas seriais e paralelas e drives de CD-ROM.
- Falhas graves em memória, processador ou vídeo podem gerar bips, enquanto problemas menores aparecem como mensagens na tela.
- Nos códigos da AMI, a tabela vai de 1 bip curto a 11 bips, com causas como falha de refresh, falha de vídeo, erro de paridade, falha nos 64 KB iniciais da RAM, timer não operacional, erro no processador, falha no Gate 20, exceção do processador, erro na memória de vídeo, erro na ROM, erro no registro de shutdown do CMOS e problema na memória cache.
- Nos códigos da Award, 1 longo e 2 curtos indicam erro de display, e outros padrões apontam para erro de memória RAM.
- Nos códigos da Phoenix, os bips são organizados em sequências numéricas ligadas a testes como registradores da CPU, leitura e escrita do CMOS, checksum da ROM BIOS, timer do sistema, inicialização do DMA, controlador de teclado, vídeo, falha na porta A20, portas serial e paralela e coprocessador matemático.
- Nos códigos da IBM, os padrões cobrem falhas da placa-mãe, fonte, display, placa de vídeo, EGA e placa 3270.
- O texto recomenda verificar encaixe de memória e placa de vídeo, limpar contatos, conferir o speaker, baixar a frequência do processador após overclock malsucedido e trocar o componente quando a falha persistir.
