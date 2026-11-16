---
url: "https://medium.com/desenvolvimento-%C3%A1gil/previsibilidade-e-as-classes-de-servi%C3%A7o-24c20fabacdd"
captured_at: "2026-11-16T06:00:48+00:00"
title: "Previsibilidade e as classes de serviço | by Thoughtworks Brasil | Desenvolvimento ágil | Thoughtworks | Medium"
domain: "medium-com"
---

Design
Brazil
Software Development
Previsibilidade e as classes de serviço
Thoughtworks Brasil
10 min read
·
May 30, 2016

por Leonardo Campos

Imagine que você está em uma fila no aeroporto, aguardando para passar pela imigração. A fila que ainda falta é enorme e só tem um agente (não muito feliz) servindo essa fila. Você está suando, pois o ar-condicionado está sendo reparado e parece não ter como o calor ficar pior.

Depois de alguns minutos, você já tem uma boa ideia de quanto tempo mais você deve ficar nessa fila. Seu raciocínio é mais ou menos o seguinte “Demorou quinze minutos para cinco pessoas passarem, como ainda tem vinte na minha frente, acho que deve levar mais uma hora.”

Pouco depois de você ter feito o cálculo, você começa a tentar se convencer de que dá para tolerar, não é tão ruim assim. Mas não demora muito para você perceber que faltou um pequeno detalhe no seu cálculo: você não considerou os passageiros “urgentes” que logo chegariam.

Um avião pousa com quarenta e cinco minutos de atraso e, infelizmente, alguns passageiros não têm tempo suficiente para ficar na fila, caso contrário, perderiam suas conexões. Para que isso não acontecesse, eles receberam “passes livres” para poder furar a fila.

“Ok, são só mais quinze minutos”, você pensa com resignação.

Mais tarde, quando esses passageiros já foram atendidos, alguns idosos começam a chegar de forma aleatória, às vezes individualmente, às vezes em grupos. Eles também são atendidos preferencialmente, antes de quaisquer outros. É nesse ponto que você simplesmente desiste de tentar fazer alguma projeção sobre quando você estará fora dessa fila e livre para curtir sua viagem.

Bom, se essa fosse uma história real, o que você sentiu foram os efeitos do que se conhece como ‘Classes de Serviço’.

Classe de Serviço

Crédito da imagem: larskflem via Compfight cc

De acordo com Daniel S. Vacanti, “Uma classe de serviço é uma política ou um conjunto de políticas em relação à ordem pela qual os itens de trabalho são puxados em um processo após o comprometimento em relação ao item” Em outras palavras, uma “Classe de Serviço”, que vou chamar apenas de CdS daqui para frente, significa que você trata alguns itens de forma diferente uma vez que eles já estejam em seu processo. Pode ser que o motivo seja diferentes perfis de risco ou tipos de trabalho ou qualquer outra coisa. No exemplo do aeroporto, havia três tipos de CdS (Passageiros atrasados, Idosos e Padrão) e você, meu amigo, teve o azar de estar na de menor prioridade.

A ideia por trás das CdS é que você deveria privilegiar items de acordo com o valor de negócio ou de acordo com o perfil de risco associado. Um exemplo pode ser encontrado no desenvolvimento de software, quando se para o trabalho normal com o objetivo de dar espaço a algum item regulatório que esteja atrasado. Isso acontece devido ao Lead Time esperado ser mais longo que o permitido pela data limite do item. Tudo lindo e maravilhoso, mas essa abordagem cobra seu preço sobre a previsibilidade.

Priorização

Não confunda as CdS com priorização. Se você der uma olhada mais atenta à definição de CdS do Daniel Vacanti, tem uma sutileza: “após o comprometimento em relação ao item”. Em outras palavras, as CdS acontecem depois que o item entrou no processo, portanto depois da priorização. Muitas equipes enfrentam dificuldades relacionadas à priorização, mas isso é tópico para um outro post.

Quando você for puxar trabalho para dentro do seu processo, você deveria, de todas as formas possíveis, puxar o item de trabalho mais valioso por quaisquer critérios que você esteja utilizando na priorização. Acontece que, uma vez dentro do processo, é isso. Depois que entrar no processo, a melhor abordagem para a previsibilidade deveria ser tratar todos os itens com a política de o Primeiro dentro / o Primeiro servido (First in/First served — FIFS).

Pressupostos da Lei de Little

Ok, vamos ser um pouco mais técnicos aqui.O Dr. John Little, um professor do MIT (Massachussetts Institute of Technology), descobriu uma relação entre algumas variáveis de processo. A fórmula dele relaciona o Lead Time médio, o Trabalho em Progresso (WIP — do inglês, Work In Progress) médio e a Vazão média.

O que é importante, contudo, não é a fórmula em si, mas o fato de que essa relação deve seguir algumas premissas para se manter válida. A melhor parte é que quanto mais seu processo seguir essas premissas, mais previsível e estável ele se tornará.

“Não é que você é ou não previsível. É que você ‘faz’ previsibilidade. A previsibilidade é proativa, não reativa. As ações que você realiza hoje têm o maior impacto em sua previsibilidade amanhã.” — Daniel S. Vacanti (tradução livre)

Vamos explorar um pouco mais as premissas por trás da Lei de Little:

As taxas de entrada e saída deveriam ser iguais. Isso significa que a taxa na qual os itens entram em seu sistema deveria ser igual à taxa na qual eles saem dele.
Todo trabalho que é começado deveria em algum momento ser terminado e, por fim, abandonar o sistema.
A quantidade de WIP deveria ser aproximadamente a mesma no começo e no fim do intervalo de tempo escolhido para o cálculo.
A idade média do WIP não deveria estar nem crescendo, nem diminuindo.
Tanto o Lead Time, quanto o WIP e a Vazão devem ser medidos com unidades consistentes.

Se você limita o WIP adequadamente, então as premissas um e três não deveriam ser um problema muito grande. Limitar o WIP garante que qualquer trabalho novo entre no sistema apenas quando exista espaço para acomodá-lo. Em outras palavras, limitar o WIP deveria manter a taxa de entrada em equilíbrio com a taxa de saída.

A segunda premissa diz que não importa o que aconteça, um item que entra no sistema vai até o fim, até que esteja pronto. O que acontece de forma razoavelmente frequente é que algo que perde valor de negócio é removido do processo (não flui até o fim). As métricas ficam prejudicadas. No exemplo do aeroporto, seria equivalente a alguém simplesmente decidir abandonar a fila de vez. Não me entenda mal, seria estúpido trabalhar em algo que não tem mais valor de negócio. O que quero dizer é que você moverá tal item para “pronto” e tratará esse trabalho adequadamente em suas métricas.

É a quarta premissa que “apanha como mala velha” das CdS. Algum WIP irá envelhecer mais do que deveria para obter Lead Times menores para as CdS de maior prioridade. No caso da fila do aeroporto, você teve que “envelhecer” na fila para que os passageiros atrasados, assim como os idosos, fossem atendidos antes.

A questão é que toda vez que seu processo viola uma premissa da Lei de Little, haverá um impacto negativo na previsibilidade.

Slack

Se você tem alguma capacidade ociosa (slack) em seu sistema, você pode ser capaz de lidar com diferentes CdS sem impactar sua previsibilidade. Em seu livro, “Kanban: Mudança Evolucionária de Sucesso para seu Negócio de Tecnologia”, David J. Andersonpropõe uma CdS chamada “Intangível”, que engloba trabalho importante, mas não necessário no futuro imediato, como, por exemplo, atualizar a versão do banco de dados ou pagar dívidas técnicas (Já falei que prefiro esse termo a débito técnico?). Para essa CdS, não há expectativa de Lead Time associada. Assim, a ideia é que um percentual dos itens fluindo pelo seu sistema sejam itens Intangíveis, o que significa que uma parte da capacidade estará sendo utilizada para trabalhar neles. É exatamente essa a capacidade que será realocada para trabalhar em itens de maior prioridade quando eventualmente aparecerem. Esse é o slack no seu sistema. É quase como manter uma pessoa desenvolvedora de lado, mas pelo menos ela faz algum trabalho de valor.

Parece-me ser uma boa solução se você tiver condições de adotá-la, especialmente porque trata o problema de que esse é o tipo de trabalho que dificilmente seria priorizado pelo negócio. Contudo, em minha opinião, todo trabalho técnico deveria ser traduzido ou em valor direto para o negócio ou em aumento de capacidade para entregar valor de negócio. O que quero dizer é que as coisas técnicas deveriam ter seus valores avaliados para serem priorizadas como quaisquer outros tipos de trabalho.

Você não deveria utilizar CdS, então?

Será que estou falando que as CdS são do mal e que você não deveria mais lançar mão delas? De jeito nenhum. O que estou falando é que você deveria estar ciente do impacto negativo que elas têm na previsibilidade do seu processo. Uma queda em um servidor de produção é um exemplo de trabalho que normalmente não pode esperar. O que se quer é apenas limitar o número de vezes que você tem que infringir as premissas da Lei de Little.

E trabalho super valioso para o negócio (lembre-se, até coisas técnicas deveriam ser vistas pelas lentes do negócio)? Não deveria ter um tratamento diferente? A resposta curta é: depende. Se você for capaz de avaliar o valor de negócio, vá em frente. Mas quando se fala de trabalho do conhecimento, considero que é pouco frequente as vezes que é possível descobrir o valor de negócio de antemão. O valor de negócio relacionado ao item deveria ser avaliado posteriormente, quando você o puser em produção e puder ter feedback de verdade. Então, mais uma vez, todos os itens deveriam ser priorizados por quaisquer critérios possíveis. O caso é que eles não deveriam ser tratados de forma diferente depois que estiverem dentro do seu sistema, pelo menos se você se preocupa com a previsibilidade (do tipo que o ajudaria a responder à pergunta: Quando esse trabalho estará pronto).

Como falei, ter slack é um solução possível, mas cara. Por que desenvolver algo que não é prioridade agora apenas para poder lidar com o impacto da variabilidade causado pelas CdS?

O que fazer então?

Deveríamos nos perguntar qual a razão de usarmos as CdS para começo de conversa. Falei um pouco sobre valor de negócio e perfil de risco. Contudo, na maioria das vezes, a razão de utilizar as CdS é uma de duas. Ou as coisas estão levando muito tempo para atravessar seu processo, ou o Lead Time está imprevisível demais e o negócio precisa de previsibilidade, pelo menos para alguns itens.

Se você puder encurtar os Lead Times e deixar seu processo previsível, você provavelmente não precisaria das CdS. Bem, pelo menos não tão frequentemente. E quanto menos você violar as premissas da Lei de Little, mas previsível você será.

Então, como tornar seu processo mais previsível e, ao mesmo tempo, encurtar os Lead Times?Se ainda não mostrei a fórmula da Lei de Little, aqui vai (uma versão dela):

Lead Time médio = WIP médio / Vazão média

Ela mostra claramente que para diminuir o Lead Time médio, é preciso reduzir o WIP médio ou aumentar a vazão média, ou ambos. Normalmente a gestão prefere influenciar o lado da vazão, utilizando “ferramentas” como horas extras, movimentação de pessoas de um projeto para outro etc. Não acredito que essa seja a melhor abordagem, contudo. O WIP é uma alavanca muito melhor para se utilizar.

Um problema comum é ter uma taxa de entrada maior que a de saída, o que quer dizer que o WIP está descontrolado. Lembre-se da premissa nº 1. Como a fórmula mostra, mudanças no WIP médio impactam no Lead Time médio.

Assim, o primeiro passo importante é que você controle o WIP. Mas antes que você faça qualquer alteração no seu processo, você deveria se certificar de que pode medir os efeitos dessa mudança. Uma das maneiras de conseguir isso é coletar métricas de fluxo (WIP, Lead Time, Vazão, Tempos de espera etc). Uma vez coletadas, ferramentas visuais tais como o Diagrama de fluxo cumulativo (Cumulative Flow Diagram) e o diagrama de dispersão de Lead Time podem ajudar você a fazer as perguntas certas e mais tarde checar os efeitos das mudanças. Depois de ter as métricas, você pode começar a mexer nas políticas do seu processo e então monitorar os efeitos das mudanças sobre as métricas.

Vamos dar mais um pulo no nosso exemplo da fila do aeroporto. Quanto tempo foi gasto em atendimento pelo agente da imigração e quanto tempo foi gasto simplesmente esperando? Tempo de espera é outro problema comum que causa aumento no Lead Time. Na maioria dos processos, os itens passam mais tempo esperando para serem trabalhados do que de fato sendo trabalhados. Seu quadro Kanban e suas métricas deveriam refletir isso, como colunas/estágios representando itens prontos para serem puxados por um estágio mais para frente no fluxo. O problema é que não há adição de valor durante a espera. Assim, uma vez medido, você deveria mudar a forma como sua equipe trabalha para tentar eliminar ou diminuir esses tempos de espera. A simples remoção das colunas não resolve o problema, apenas o joga para baixo do tapete, certo?

A redução tanto do WIP quanto dos tempos de espera impactam positivamente o Lead Time do seu processo. Lead Times menores têm um efeito secundário positivo: as métricas de qualidade mostram uma melhoria, pois os problemas são descobertos mais rápido e as pessoas ainda se lembram do trabalho que fizeram. A propósito, software de melhor qualidade também produz menos efeitos inesperados, de forma que mais previsibilidade pode ser obtida.

Espero que essas ideias possam ajudar você a melhorar a previsibilidade do seu processo e deixar seus clientes (mais) felizes.

Referências:

Actionable Agile Metrics for Predictability — Daniel S. Vacanti
Kanban: Mudança Evolucionária de Sucesso para seu Negócio de Tecnologia — David J. Anderson
Kanban em 10 passos — Jesper Boeg

Post publicado originalmente em https://www.thoughtworks.com
