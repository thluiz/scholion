---
title: "[Off-Topic] Programadores são péssimos Comunicadores (UDP vs TCP)"
date: '2016-01-11T08:35:39-03:00'
category: webclip
summary: 'Autor argumenta que programadores se comunicam mal, confundem informar com comunicar e usa a metáfora TCP vs UDP para defender uma comunicação com confirmação, ordem e garantia de entendimento.'
tags: ["comunicacao", "carreira", "programacao"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "[Off-Topic] Programadores são péssimos Comunicadores (UDP vs TCP) | AkitaOnRails.com"
    url: "http://www.akitaonrails.com/2013/11/02/off-topic-programadores-sao-pessimos-comunicadores-udp-vs-tcp"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2016-01/akitaonrails-com--programadores-pessimos-comunicadores-udp-vs-tcp.md"
    kind: repo
---

O texto critica a postura comum de programadores que se veem como superiores ao "resto do mundo" e acreditam que código é linguagem universal. O autor afirma que a maior parte dos problemas em projetos não se resolve com código, mas com comunicação. Ele compara o mundo open source, em que contribuições são fragmentadas e muitos projetos fracassam, com o "mundo real", onde tempo, pessoas e riscos são limitados e a comunicação faz diferença entre sucesso e fracasso.

Para explicar, o autor distingue informar de comunicar e descreve comunicação como um processo com emissor, receptor, mensagem e meio. Só existe comunicação quando o receptor recebe e entende a mensagem. Usando a metáfora de redes, ele compara a forma como programadores se comunicam a UDP: enviam fragmentos, não esperam confirmação, não controlam congestionamento, não garantem reenvio ou entrega. Em contraste, defende uma postura "TCP": estabelecer conexão, controlar fluxo, garantir ordem, checar erros e obter confirmação de recebimento e entendimento. Pode parecer mais lento, mas evita retrabalho repetido e falhas acumuladas. A recomendação final é que programadores ajustem seus "protocolos" e passem a se comunicar de forma mais parecida com TCP.

## Fichamento

- Programadores costumam acreditar que entendem tudo melhor do que o restante das pessoas e desvalorizam quem não vive em ambientes como Github, Hacker News e Reddit.
- Nas comunidades de programação prevalece a ideia de que “mostrar o código” basta e que essa seria a linguagem universal suficiente.
- O autor relata já ter respondido que aproximadamente 90% dos problemas em projetos de software não se resolvem com código.
- No open source, a maioria das contribuições é pequena e esporádica, o que torna a experiência fragmentada mesmo para quem participa ativamente.
- Muitos projetos open source não chegam a um resultado concreto, e a maior parte acaba fracassando apesar de alguns sucessos como jQuery.
- Existem bibliotecas tecnicamente boas que não ganham reconhecimento, enquanto projetos com boa coordenação e muitos colaboradores avançam mais.
- Projetos open source que conseguem se estruturar melhor passam a ter datas de lançamento, roadmap e se aproximam de projetos formais.
- Em ambientes fora do open source, não há sobra de tempo ou pessoas, os riscos são maiores e cresce a necessidade de controle sobre resultados.
- Nesse contexto profissional mais restrito, a comunicação se torna fator decisivo para determinar se um projeto vai fracassar ou ter sucesso.
- O autor diferencia: apenas disponibilizar uma informação em um lugar compartilhado não significa ter comunicado algo.
- Comunicação é apresentada como um sistema com quatro elementos: comunicador, recipiente, mensagem e meio de transmissão.
- Programadores tendem a considerar apenas si mesmos e a mensagem, ignorando o receptor e o meio pelos quais a mensagem circula.
- A definição proposta é que só existe comunicação se o destinatário recebe e compreende a mensagem enviada.
- Em linguagem de redes, o autor compara a comunicação a um cliente enviando dados a um servidor por meio de um protocolo específico.
- Se a tentativa de envio falha e retorna erro, considera-se que a comunicação não aconteceu, mesmo que tenha existido uma tentativa.
- No caso de TCP/IP, o autor descreve o processo de handshake com SYN, SYN-ACK e ACK para estabelecer conexão confiável.
- A partir desse handshake, é possível sequenciar pacotes e garantir que todo o conteúdo enviado foi integralmente recebido.
- A maioria dos programadores é comparada a quem pensa em UDP, enviando datagramas sem se importar em verificar se o outro lado recebeu.
- O autor lista comportamentos de “UDP humano”: evitar esperar por handshake, mandar informações fragmentadas com pouco overhead.
- Ele também associa a isso a falta de preocupação com controle de congestionamento, reenvio de pacotes e preferência por broadcast ou multicast.
- Essa postura funciona melhor quando comunicar para grandes grupos basta e não é necessário que todos recebam a mensagem.
- No cenário fragmentado do open source, essa forma de comunicação mais solta pode ser aceitável ou parecer eficiente.
- Em contextos em que é crucial estabelecer conexão e garantir que a mensagem chegue inteira, o autor recomenda agir como TCP.
- TCP é descrito como um mecanismo que mantém um fluxo de dados mesmo em conexões ruins e servidores pouco confiáveis.
- Ele destaca que TCP garante ordem dos pacotes e que 100% dos dados enviados sejam recebidos em sequência correta.
- Em UDP, se o meio ou servidor é ruim e a informação chega corrompida ou se perde, não há reação automática a essas falhas.
- O texto afirma que ambos os protocolos têm seu uso, mas que, quando se precisa de certeza de entrega íntegra, TCP é o caminho.
- No mundo open source, usar um estilo UDP de comunicação pode reduzir latência e aparentar maior eficiência.
- No chamado mundo não-open source, que inclui ambientes fora do software, a exigência é se comunicar com mais características de TCP.
- Entre as vantagens de uma postura tipo TCP, o autor cita garantir conexão estabelecida antes de enviar informações.
- Outra vantagem é manter a ordem das informações, reorganizando “pacotes” se for necessário para facilitar entendimento.
- Ele sugere moderar a velocidade de transmissão de dados para evitar sobrecarregar o interlocutor com excesso de conteúdo.
- Também enfatiza a importância de garantir a entrega da mensagem em si e não apenas o ato de tê-la enviado.
- Inclui-se aí checagem de erros para ter certeza de que a informação não se corrompeu ao longo do processo de comunicação.
- Por fim, defende obter um tipo de “acknowledgment”, confirmando que o outro lado recebeu e compreendeu aquilo que foi dito.
- O autor afirma que, embora pareça que esse modo de comunicação demore mais, ele evita repetição de explicações e retrabalho futuro.
- Ele compara essa situação à ideia de programar sem testes, que aparenta ser mais rápido, mas gera problemas depois.
- O texto termina incentivando que programadores ajustem seus hábitos de comunicação para se aproximarem do comportamento de TCP.
