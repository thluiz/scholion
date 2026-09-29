---
url: "https://carodias.medium.com/entendendo-o-princ%C3%ADpio-da-responsabilidade-%C3%BAnica-4f11cd4a3caa"
captured_at: "2022-04-17T20:44:50-03:00"
title: "Entendendo o Princípio da Responsabilidade Única | by Carolina Dias | Apr, 2022 | Medium"
domain: "carodias-medium-com"
---

# Entendendo o Princípio da Responsabilidade Única

![0*S5a-ojllMXF_JAXm](carodias-medium-com--entendendo-principio-da-responsabilidade-unica/d6062ea164958c4413408918b3239ea7.jpg)

Fonte: [Unsplash](https://unsplash.com/photos/DuHKoV44prg)

Em Engenharia de Software, são bastante difundidos os conceitos de **Princípios de Projetos**. Cinco dos mais conhecidos desses princípios, os chamados **Princípios SOLID**, são a base que diversos desenvolvedores de software seguem para estruturar seus projetos.

Esse acrônimo, introduzido por Robert Martin e Michael Feathers, representa:

- ***S****ingle Responsibility Principle;*
- ***O****pen Closed/Principle;*
- ***L****iskov Substitution Principle;*
- ***I****nterface Segregation Principle;*
- ***D****ependency Inversion Principle.*

Destes princípios, o que considero mais “autoexplicativo” é o **Princípio da Responsabilidade Única**. Conseguimos captar o que ele quer dizer apenas pelo nome. E por isso mesmo ele pode ser um dos princípios mais mal-entendidos ou com divergências no entendimento. Com isso, vamos ver realmente do que ele se trata.

## Tudo começa com um exemplo…

Antes de tudo, vamos mostrar um exemplo de código. Nele queremos representar um menu de um restaurante como uma classe (aqui faremos só o esqueleto da classe, em Python, sem a implementação completa).

Exemplo de classe com várias responsabilidades

Qual seria, então, a principal responsabilidade dessa classe? Pelo nome e pela descrição inicial nós imaginamos que ela seja capaz apenas de realizar operações relacionadas ao menu do restaurante, como listar os itens, checar valores e etc.

Mas não é só isso que ocorre, também temos um método nessa classe para listar e cadastrar funcionários. Opa, mas com isso a classe não está assumindo responsabilidades que não lhe convém? Exatamente, essa classe está quebrando o **Princípio da Responsabilidade Única**.

E o que fazemos para melhorá-la? Uma maneira comum é separar em duas classes diferentes.

Exemplo de classe para o menu

Exemplo de classe para os funcionários

Agora sim cada classe tem sua responsabilidade única. Também dizemos que as classes tem uma **implementação coesa**. Isso se deu pois aplicamos a propriedade da **Separação de Interesses**, na qual cada classe deve ter apenas um interesse. Esses sinônimos revelam bem o que significa esse princípio.

## Agora a definição…

Com esses exemplos simples fica bem mais fácil entender agora a definição, dada a seguir, desse princípio.

Primeiro a definição “oficial” pomposa, aqui encontrada no livro [Engenharia de Software Moderna, cap. 5](https://engsoftmoderna.info/cap5.html#princ%C3%ADpio-da-responsabilidade-%C3%BAnica):

> “toda classe deve ter uma única responsabilidade. Mais ainda, responsabilidade, no contexto do princípio, significa motivo para modificar uma classe. Ou seja, deve existir um único motivo para modificar qualquer classe em um sistema.”

Mas isso não diz exatamente o que nosso simples exemplo representou? De fato. Mas ter uma responsabilidade única não quer dizer que a classe terá apenas um único método, como já vi afirmarem certa vez. A classe pode ter inúmeros métodos e mesmo assim não ferir esse princípio, basta nos atentarmos ao que ela faz e manter sua coesão.

## **Is this the real life…?**

Na prática esse princípio realmente funciona e é aplicado? Geralmente sim, os desenvolvedores de software se atentam bastante ao fato de classes terem uma única responsabilidade. Claro que nem tudo é perfeito e sempre existirão classes fugindo dos “princípios ideais” da engenharia de software, pois no dia-a-dia de desenvolvimento às vezes ocorre o “quantidade >> qualidade”, mas aí já é discussão pra outro dia :D

## Referências

Não só para esse tema, mas para a vida de um desenvolvedor no geral, recomendo o livro essencial **Engenharia de Software Moderna**, do Professor Marco Tulio Valente, disponível para leitura gratuita em <https://engsoftmoderna.info/>

Dúvidas, dicas ou sugestões? Ficarei feliz em recebê-las!
