---
url: "https://gabrieluizramos.com.br/fundamentando-mocks-em-javascript"
captured_at: "2026-11-16T03:42:02+00:00"
title: "Fundamentando Mocks em JavaScript"
domain: "gabrieluizramos-com-br"
---

Parte importante de criação de [confiança com o software que você escreve](https://gabrieluizramos.com.br/voce-confia-em-si/) é a consciência e a fundamentação sobre como utilizar corretamente alguma estrutura de _mocks_ no seu código.

Um _mock_ nada mais é do que a substituição de um determinado trecho de código por algo necessário ao seu teste. Como se fosse um dublê, em um filme, sabe? Da mesma forma como dublês se passam por outras pessoas em cenas de ação, no nosso teste, os _mocks_ vão interpretar trechos de código permitindo que a gente tenha controle sobre sua implementação.

Vamos imaginar o seguinte cenário:

> Você está desenvolvendo um e-commerce e, na tela de pagamento, ao clicar no botão "finalizar compra" a sua compra é efetuada e você recebe uma confirmação em uma modal com uma mensagem de sucesso

Muito provavelmente você não vai querer ficar simulando uma compra real a todo momento que executar seus testes unitários. Se você fosse realizar algo dessa forma, teriam algumas variáveis que são meio complicadas de serem previstas (conexão com internet, estabilidade e velocidade da conexão, tempo de resposta da API consumida) que poderiam impactar seus testes e que não necessariamente entregariam algum valor pra você ou para seu teste. Sem contar que existem outros tipos de teste que podem assegurar esse cenário.

É justamente nesse cenário que os _mocks_ caem como uma luva. Nesse exemplo você consegue substituir esses trechos de código responsáveis por retornar o sucesso ou falha da requisição de sua API (ou qualquer necessidade externa e assíncrona) por um outro trecho específico. Assim consegue de fato trabalhar e moldar as asserções do seu teste com o que você espera em cada um dos casos de teste.

* * *

**Vale avisar que**: utilizarei _mock_ como um termo geral para facilitar a comunicação. Mesmo que existam outras nomenclaturas (como _fake_ para dados, _spies_ para verificação de funções e _stubs_ para sobrescrever comportamento), é bem comum que chamemos tudo de _mock_ no dia-a-dia.

Lembrando que os exemplos citados aqui levam em consideração a utilização do [Jest](https://jestjs.io/) como ferramenta de teste, mas os conceitos podem ser reaproveitados para o framework que você estiver usando.

* * *

### [#](#antes-de-tudo-tenha-em-mente-a-unidade-que-voce-quer-testar)Antes de tudo, tenha em mente a unidade que você quer testar

Por desespero de fazer seus testes passarem é muito comum "sair _mockando_ tudo", mas isso pode ser muito pior do que você imagina. Você deve utilizar estruturas de _mock_ quando sua unidade (função ou trecho de código) possui dependência de algo que não está no escopo do seu teste.

Voltando ao cenário que mencionamos: o responsável por disparar a real requisição para finalizar a compra é o navegador ou dispositivo que está sendo utilizado.

Portanto, qualquer ação que envolva algo que não seja específico do botão "finalizar compra" é um possível candidato a receber um _mock_ durante o teste desse exemplo que imaginamos.

### [#](#criando-mocks)Criando _mocks_

Existem duas formas principais de escrever um _mock_ no Jest: criando um _mock_ no teste que estiver sendo executado ou utilizando criando uma pasta `__mocks__` ao lado do arquivo que você estiver testando.

Focaremos na primeira opção (de criar os _mocks_ em nossos testes) que é o mais importante para o momento. O que muda para o segundo caso é apenas a estrutura de pasta.

No entanto, se quiser, você pode [ler a documentação](https://jestjs.io/docs/pt-BR/manual-mocks) também.

### [#](#tipos-de-mock)Tipos de _mock_

Vamos dividir nossos _mocks_ nas seguintes categorias:

*   dados;
*   funções.

* * *

#### [#](#dados)Dados

Provavelmente o cenário mais simples de _mock_ que existe, mas muito fundamental.

Vamos imaginar que nós temos uma função que recebe uma lista de personagens e um nome a ser filtrado.

Algo como:

```
const filterCharacter = (characters, name) => {
  return characters.filter(char => char && char.name.includes(name));
}
```

Para conseguirmos testar essa função, precisaremos utilizar uma lista de personagens (um _mock_ no nosso teste) e algum parâmetro de nome.

Escrevendo nosso _mock_, para esse teste, podemos ter algo como:

```
const mockCharacters = [
  { name: 'anakin skywalker', nickname: 'darth vader' },
  { name: 'leia organa' },
  { name: 'luke skywalker' },
  { name: 'r2-d2' },
  { name: 'c3po' },
];
```

E podemos escrever um teste para verificar todos os personagens com sobrenome `skywalker`, por exemplo:

```
import { filterCharacter } from './filter-character';

const mockCharacters = [
  { name: 'anakin skywalker', nickname: 'darth vader' },
  { name: 'leia organa' },
  { name: 'luke skywalker' },
  { name: 'r2-d2' },
  { name: 'c3po' },
];

describe('filterCharacter', () => {
  it('filtra uma lista de personagens por um determinado nome', () => {
    const resultado = filterCharacter(mockCharacters, 'skywalker');
    const esperado = 2;

    expect(resultado.length).toEqual(esperado);
  });
});
```

* * *

#### [#](#funcoes)Funções

O Jest nos permite utilizar algumas [funções específicas](https://jestjs.io/docs/pt-BR/jest-object#mock-functions) dependendo da necessidade do nosso teste e, para facilitar, vale a pena dividirmos esse tópico em outros 3:

*   funções comuns;
*   módulos;
*   espiões.

##### [#](#funcoes-comuns)Funções comuns

Vamos imaginar que nossa função de filtrar personagens, recebe um terceiro parâmetro. Esse novo parâmetro é uma função que verifica se o personagem está vivo, baseado em um campo `alive`.

Nossa função será algo como:

```
const filterCharacter = (characters, name, isAlive) => {
  return characters.filter(char => char && char.name.includes(name) && isAlive(char));
}
```

Essa função não está mais no escopo do nosso teste unitário então podemos fazer um _mock_ dela.

Para realizar o _mock_ de uma função, utilizamos o seguinte método do Jest:

```
const mock = jest.fn();
```

O trecho `jest.fn()` retorna uma função de _mock_ para ser utilizada.

Caso você precise simular o comportamento dessa função com algum resultado pré-definido, você pode passar uma implementação de uma função como parâmetro ou utilizar alguns outros métodos e inclusive receber qualquer parâmetro.

Vamos imaginar que nossa função sempre retorna `true`, por exemplo.

```
const mockFn = jest.fn(() => true);
// ou utilizando .mockImplementation passando uma nova implementação
const mockFn = jest.fn().mockImplementation(() => true);
// ou utilizando .mockReturnedValue passando o valor de retorno diretamente
const mockFn = jest.fn().mockReturnedValue(true);
```

A lista completa dos métodos (vamos ver alguns a seguir) está [na documentação](https://jestjs.io/docs/pt-BR/mock-function-api#m%C3%A9todos).

Dessa maneira, conseguimos verificar se a função `isAlive` foi chamada ou não corretamente com as asserções:

```
// verifica se a função foi chamada
expect(mockFn).toHaveBeenCalled();
// verifica quantas vezes a função foi chamada (exemplo: 2)
expect(mockFn).toHaveBeenCalledTimes(2);
// verifica que a função não foi chamada
expect(mockFn).not.toHaveBeenCalled();
// verifica que a função não foi chamada com algum parâmetro (exemplo: 'false')
expect(mockFn).toHaveBeenCalledWith(false);
```

Vamos ao nosso teste:

```
import { filterCharacter } from './filter-character';

// mock atualizado com os valores de "alive"
const mockCharacters = [
  { name: 'anakin skywalker', nickname: 'darth vader', alive: true },
  { name: 'leia organa', alive: false },
  { name: 'luke skywalker', alive: false },
  { name: 'r2-d2', alive: true },
  { name: 'c3po', alive: true },
];

describe('filterCharacter', () => {
  it('filtra uma lista de personagens por um determinado nome e verifica se o personagem está vivo', () => {
    const mockIsAlive = jest.fn(() => true)
    const resultado = filterCharacter(mockCharacters, 'skywalker', mockIsAlive);
    const esperado = 2;

    expect(resultado.length).toEqual(esperado);


    // como a função isAlive é executada quando o personagem
    // possui o nome passado como parâmetro
    // podemos verificar se foi executada a mesma quantidade de vezes
    // que nosso resultado
    expect(mockIsAlive).toHaveBeenCalledTimes(resultado.length)
  });
});
```

Se quiser fazer um exercício, crie um novo caso de teste onde o `mock` da função `isAlive` retornar `false`. ✏️

##### [#](#modulos)Módulos

Vamos imaginar que agora a função `isAlive` não é mais recebida como parâmetro, mas é uma dependência externa (módulo) da função `filterCharacter`. Ou seja, agora temos algo como:

```
import { isAlive } from './is-alive';

const filterCharacter = (characters, name) => {
  return characters.filter(char => char && char.name.includes(name) && isAlive(char));
}
```

Para conseguir cobrir esse cenário, utilizaremos a função `jest.mock`. Essa função, recebe como parâmetro o caminho do módulo que será sobrescrito com o _mock_ (no nosso caso `is-alive`) e pode receber como segundo parâmetro (opcionalmente) uma função que pode retornar manualmente os valores que o módulo exporta. Caso esse segundo parâmetro não seja passado, por padrão, o Jest fará um _automocking_ das funções e fará _mock_ de todos os valores exportados.

Ou seja, para realizar o _mock_ desse módulo, agora podemos seguir da seguinte maneira:

```
jest.mock('./is-alive');
// ou
jest.mock('./is-alive', () => {
  return {
    isAlive: jest.fn();
  }
});
```

A diferença da primeira pra segunda utilização é que a segunda nos permite customizar os valores exportados pelo módulo, caso precisemos. Caso você opte por utilizar a primeira, todos as funções exportadas pelo módulo já serão sobrescritas por uma função de _mock_ igual ao retorno do `jest.fn` por padrão.

Com isso, podemos manter nosso teste exatamente igual! A única diferença é que não precisaremos mais passar essa função como parâmetro e agora, após realizar o _mock_ de `is-alive`, iremos importar essa função para verificar se ela foi de fato executada.

```
import { filterCharacter } from './filter-character';
// importamos o modulo
import { isAlive } from './is-alive';

jest.mock('./is-alive', () => ({ isAlive: jest.fn(() => true) }));

const mockCharacters = [
  { name: 'anakin skywalker', nickname: 'darth vader', alive: true },
  { name: 'leia organa', alive: false },
  { name: 'luke skywalker', alive: false },
  { name: 'r2-d2', alive: true },
  { name: 'c3po', alive: true },
];

describe('filterCharacter', () => {
  it('filtra uma lista de personagens por um determinado nome e verifica se o personagem está vivo', () => {
    const resultado = filterCharacter(mockCharacters, 'skywalker');
    const esperado = 2;

    expect(resultado.length).toEqual(esperado);

    // modificamos para usar o import
    expect(isAlive).toHaveBeenCalledTimes(mockCharacters.length)
  });
});
```

##### [#](#espioes)Espiões

Até agora só vimos como realizar _mock_ das funções mas, se quiséssemos manter a execução de alguma função, sem sobrescrever seu comportamento?

Vamos imaginar que, agora, teremos um novo módulo chamado `logger`. Esse módulo exporta uma função `log` que será executado junto com o filtro. Da seguinte maneira:

```
import { isAlive } from './is-alive';
import { log } from './logger';

const filterCharacter = (characters, name) => {
  return characters.filter(char => {
    log(char);
    return char && char.name.includes(name) && isAlive(char);
  });
}
```

Não precisamos implementar essa nova função, mas vamos imaginar que agora vamos apenas verificar se ela foi chamada corretamente, sem precisar nos preocupar com a forma que ela é implementada.

Para nos ajudar dessa vez, utilizaremos o método [`spyOn`](https://jestjs.io/docs/pt-BR/jest-object#jestspyonobject-methodname) do jest. Esse método recebe como parâmetro o objeto a ser "espionado" e a função a ser verificada, da seguinte maneira:

```
// importamos tudo para que possamos verificar a função `log`
import * as logger from './logger';

const spy = jest.spyOn(logger, 'log');
```

Dessa forma, seguimos nossos testes normalmente com o que já tínhamos e validamos se nosso _mock_ da função `log` foi chamado corretamente.

```
import { filterCharacter } from './filter-character';
import { isAlive } from './is-alive';
import * as logger from './logger';

jest.mock('./is-alive', () => ({ isAlive: jest.fn(() => true) }));

const mockCharacters = [
  { name: 'anakin skywalker', nickname: 'darth vader', alive: true },
  { name: 'leia organa', alive: false },
  { name: 'luke skywalker', alive: false },
  { name: 'r2-d2', alive: true },
  { name: 'c3po', alive: true },
];

describe('filterCharacter', () => {
  it('filtra uma lista de personagens por um determinado nome e verifica se o personagem está vivo', () => {
    const espiao = jest.spyOn(logger, 'log');
    const resultado = filterCharacter(mockCharacters, 'skywalker');
    const esperado = 2;

    expect(resultado.length).toEqual(esperado);

    expect(isAlive).toHaveBeenCalledTimes(resultado.length)

    // como a função log é executada sempre
    // que os personagens são filtrado
    // podemos verificar se a quantidade de vezes
    // é igual à quantidade de personagens no mock
    expect(espiao).toHaveBeenCalledTimes(mockCharacters.length);
  });
});
```

* * *

### [#](#-nao-esqueca-de-limpar-seus-mocks-)🚨 Não esqueça de "limpar" seus _mocks_ 🚨

Se tem uma coisa mais importante do que saber como utilizar um _mock_ de forma consciente é saber limpar um _mock_ após seus testes. Com certeza isso vai poupar uma dor de cabeça e evitar que você possa ter problemas futuros em outros testes que tentem acessar seus módulos.

Para funções de `spy`, basta executar o método `mockRestore`, da seguinte forma:

```
const espiao = jest.spyOn(logger, 'log');

// após o teste
espiao.mockRestore();
```

Para funções que manipulamos com `jest.fn()`, podemos utilizar outros métodos como:

```
const mockFn = jest.fn();

// após o teste

// limpa as execuções
// mas mantém as implementações
mockFn.mockClear();

// limpa as execuções
// e as implementações
mockFn.mockReset();

// limpa as execuções
// e as implementações
// e também faz com que a função retorne ao seu valor original
// antes do mock
mockFn.mockRestore();
```

E, caso queiramos limpar todos os mocks do teste, sem ficar manipulando um por um, podemos usar também:

```
// similar ao `mockClear`, mas para todas as funções de mock
jest.clearAllMocks();

// similar ao `mockReset`, mas para todas as funções de mock
jest.resetAllMocks();

// similar ao `mockRestore`, mas para todas as funções de mock
jest.restoreAllMocks();
```

Muito provavelmente você vai querer automatizar essas limpezas em algum hook dos seus testes, como [vimos anteriormente](https://gabrieluizramos.com.br/anatomia-de-um-teste-em-javascript).

* * *

### [#](#ja-utilizava-mock-nos-seus-testes)Já utilizava _mock_ nos seus testes?

Já teve experiência (ou até mesmo dores de cabeça) com alguma estrutura de _mock_?

Espero que possa ter ajudado e que, de agora em diante, você possa utilizar essas ferramentas a favor dos testes que você estiver escrevendo!
