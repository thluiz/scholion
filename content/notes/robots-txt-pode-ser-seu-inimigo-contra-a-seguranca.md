---
title: "Robots.txt pode ser seu inimigo contra a segurança"
date: '2012-12-17T14:55:51-03:00'
category: webclip
summary: 'O texto explica a sintaxe do robots.txt e mostra por que ele pode expor diretórios e caminhos sensíveis. Sugere usar meta robots, rel="nofollow" e proteção fora da URL.'
tags: ["robots-txt", "seguranca-web", "crawler", "nofollow"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Robots.txt pode ser seu inimigo contra a segurança"
    url: "http://imasters.com.br/tecnologia/seguranca/robots-txt-pode-ser-seu-inimigo-contra-a-seguranca"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2012-12/imasters-com-br--robots-txt-pode-ser-seu-inimigo-contra-a-seguranca.md"
    kind: repo
---

O texto descreve como o robots.txt é usado para indicar a crawlers quais páginas e diretórios podem ou não ser acessados. Em seguida, mostra que essa mesma informação pode revelar a estrutura do site e facilitar a descoberta de caminhos sensíveis.

## Fichamento

- O robots.txt serve para informar permissões de acesso a páginas e diretórios para crawlers.
- A sintaxe básica apresentada inclui user-agent, disallow e allow.
- Disallow bloqueia diretórios ou páginas para o crawler.
- Allow libera o acesso a diretórios ou subdiretórios que estavam bloqueados.
- O risco de segurança aparece porque o arquivo pode expor a estrutura interna do site.
- O texto cita exemplos de caminhos de banco de dados, listas de e-mail, configurações, senhas e backups que podem aparecer em robots.txt.
- WebSpiders podem ler robots.txt para localizar diretórios negados e procurar arquivos importantes neles.
- Como alternativa, o texto cita a meta tag robots com noindex e nofollow.
- O texto também cita rel="nofollow" em links para impedir que o crawler siga o link.
- Essas medidas não protegem os arquivos em si; apenas dificultam o trabalho do cracker.
- O texto recomenda não deixar arquivos confidenciais em caminhos acessíveis por URL.
- Em aplicações .NET, a pasta App_Data é citada como exemplo de diretório inacessível pela URL.
- Outra opção citada é redirecionar ou retornar página não encontrada quando certos diretórios forem acessados pela URL.
- O texto menciona ainda hospedar arquivos restritos fora do diretório principal do site.
