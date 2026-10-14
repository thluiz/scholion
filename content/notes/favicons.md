---
title: "Favicons"
date: '2013-02-06T16:59:14-03:00'
category: webclip
summary: 'O texto explica o papel dos favicons no branding, compara formatos e tamanhos, e mostra como implementar ícones para browsers, iOS e Windows 8 com fallback adequado.'
tags: ["favicons", "branding", "webdesign", "browser-support"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Favicons"
    url: "https://tableless.com.br/favicons/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2013-02/tableless-com-br--favicons.md"
    kind: repo
---

O texto trata de favicons como parte da identidade de um site, não só como ícones ligados aos favoritos. Ele descreve a evolução do uso desses arquivos em browsers, sistemas operacionais e dispositivos móveis, e relaciona isso com visibilidade, identificação rápida e branding.

## Fichamento

- Favicons são pequenos ícones ao lado da barra de endereços e servem para identificar rapidamente um site.
- O uso do favicon mudou com smartphones, tablets, telas de alta resolução e novos contextos como home screens e áreas de trabalho.
- A função do favicon vai além dos favoritos e faz parte do branding do site.
- Criar ícones exige atenção a semiótica, gestalt, cultura do público e limitações técnicas de tamanhos reduzidos.
- O artigo recomenda evitar conversores automáticos online e repensar o desenho conforme o tamanho final.
- O formato ICO ainda tem amplo suporte e pode conter várias imagens encapsuladas.
- PNG oferece boa qualidade e é uma opção comum nos browsers modernos, com declaração manual de tamanhos.
- JPEG, GIF e APNG não são apresentados como boas escolhas, e SVG ainda tem suporte limitado no texto.
- Favicons animados são desencorajados por serem distrativos e passarem impressão ruim.
- Para compatibilidade, o texto sugere PNG com fallback em ICO para Internet Explorer.
- Os tamanhos citados incluem 16px, 32px, vários tamanhos para iOS, 144px para tiles do Windows 8 e outros casos específicos.
- Para implementar o favicon, o texto mostra a declaração de links no HTML e alerta contra declarar PNG e ICO sem comentários condicionais.
- Apple touch icons devem ser imagens quadradas em PNG, declaradas na ordem da maior para a menor.
- O sufixo precomposed remove efeitos automáticos como cantos arredondados e reflexo no iOS.
- No Windows 8, o tile usa uma imagem PNG de 144px e pode receber cor de fundo pelo HTML.
- O texto também menciona tiles dinâmicos, listas de links e atualizações de conteúdo para sites fixados.
- A conclusão defende que ajustar ícones a cada contexto melhora a integração com o usuário e pode aumentar visitas e reconhecimento da marca.
