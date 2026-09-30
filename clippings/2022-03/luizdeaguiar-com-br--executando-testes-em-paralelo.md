---
url: "https://luizdeaguiar.com.br/pt/2022/03/24/executando-testes-em-paralelo/"
captured_at: "2022-03-28T15:17:09-03:00"
title: "Executando Testes em Paralelo Com Pytest-Xdist - LuizDeAguiar"
domain: "luizdeaguiar-com-br"
---

##   
Índice

1.  [Introdução](#introduction)

2.  [Setup Inicial](#initial-setup)  
    2.1 Clonar o Projeto  
    2.2 Executar o Teste

3.  [Testes Parametrizados](#parameterized-tests)  
    3.1 Implementação  
    3.2 Executar Testes

4.  [Testes em Paralelo](#parallel-tests)  
    4.1 Convenções  
    4.2 Instalando o plugin pytest-xdist  
    4.3 Executando os testes em paralelo

5.  [Repositório](#repository)

6.  [Bibliografia](#bibliography)

##   
1\. [Introdução](#idx-introduction)

Esse tutorial é uma continuação do meu outro tutorial chamado “[Configurando Múltiplos Navegadores com Selenium e Python](https://www.luizdeaguiar.com.br/pt/2022/03/15/configurando-multiplos-navegadores-com-selenium-e-python/)”.  
Por favor, dê uma olhada nele antes de começar esse.

Esse tutorial foi feito com base no curso “[Selenium WebDriver with Python](https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/)”, ministrado por [Andrew Knight](https://www.linkedin.com/in/andrew-leland-knight/).  
Ele também possui um blog, clique no link para acompanhar as novidades: [https://automationpanda.com/](https://automationpanda.com/).

##   
2\. [Setup Inicial](#idx-initial-setup)

Como dito antes, já que esse projeto é uma continuação do tutorial “[Configurando Múltiplos Navegadores com Selenium e Python](https://www.luizdeaguiar.com.br/pt/2022/03/15/configurando-multiplos-navegadores-com-selenium-e-python/)”, será necessário clonar o repositório dele para continuar o seu trabalho.

##   
2.1 Clonar o Projeto

Antes de começar, verifique se você está clonando a branch correta:  
“tutorial/multiple-browsers”.

[![](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/branch-1.png)](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/branch-1.png)

Git Repo:  
[https://github.com/LuizGustavoR/intro-selenium-py/tree/tutorial/multiple-browsers](https://github.com/LuizGustavoR/intro-selenium-py/tree/tutorial/multiple-browsers)

Após clonar, verifique no VSCode se a branch clonada foi a correta:

[![](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/vscode-branch-1.png)](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/vscode-branch-1.png)

##   
2.2 Executar o Teste

Para ter certeza de que o projeto clonado está realmente funcionando,  
abra o “Prompt de Comando” dentro da pasta do projeto.

[![](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/project-folder-2.png)](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/project-folder-2.png)

Execute o comando abaixo:

```
pipenv run python -m pytest
```

Você deveria ver essa mensagem:

[![](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/passed-1-1024x120.png)](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/passed-1.png)

##   
3\. [Testes Parametrizados](#idx-parameterized-tests)

Para parametrizar testes em Python você precisa utilizar o código abaixo antes de uma função de teste:

```
@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
```

O primeiro argumento é uma string com o nome da variável.  
O segundo argumento é uma lista de valores ou tuplas.

##   
3.1 Implementação

O pytest irá executar a função de teste uma vez para cada valor da lista, inserindo cada item da lista na variável “phrase” e executando o teste.

Arquivo “tests/test\_search.py”:

```
"""
These tests cover DuckDuckGo searches.
"""
 
import pytest
 
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
   
    # Given the DuckDuckGo home page is displayed
    search_page.load()
   
    # When the user searches for the phrase variable
    search_page.search(phrase)
 
    # And the search result query is the phrase variable
    assert phrase == result_page.search_input_value()
 
    # And the search result links pertain to the phrase variable
    # for title in result_page.result_link_titles():
    #     assert PHRASE.lower() in title.lower()
 
    # Then the search result title contains the phrase variable
    assert phrase in result_page.title()
```

##   
3.2 Executar Testes

Execute o comando abaixo:

```
pipenv run python -m pytest
```

[![](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/parameterized-tests-1-1024x298.png)](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/parameterized-tests-1.png)

Como você pode ver.  
Testes Web UI são lentos.

Para adicionar um teste em paralelo no pytest use o plugin “pytest-xdist”.  
“pytest-xdist” pode controlar várias threads de teste em uma máquina e também pode distribuí-los através de muitas máquinas.

##   
4.1 Convenções

*   Certifique-se de que todos os testes sejam realmente independentes, evite fazer um teste dependente da configuração ou resultado de outro teste.
*   Deveria poder executar por si só sem outros testes.
*   Deveria poder executar em qualquer ordem.
*   Evite colisão de testes, pode acontecer quando os testes acessam um estado compartilhado, como um teste alterando a senha do usuário enquanto outro teste tenta fazer login com a senha anterior e falha.

##   
4.2 Instalando o plugin pytest-xdist

Para instalar o plugin “pytest-xdist” abra o “Prompt de Comando” dentro da pasta do projeto:

[![](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/project-folder-3.png)](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/project-folder-3.png)

Então execute o comando abaixo:

```
pipenv install pytest-xdist
```

Você deveria ver essa mensagem:

[![](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/xdist-install-1-1024x401.png)](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/xdist-install-1.png)

##   
4.3 Executando os teste em paralelo

Agora execute o comando abaixo:

```
pipenv run python -m pytest -n 3
```

**Obs.:** “-n” significa que você quer executar os teste em paralelo e o número “3” significa o número de threads que você quer.

[![](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/parallel-tests-1-1024x274.png)](https://www.luizdeaguiar.com.br/wp-content/uploads/2022/03/parallel-tests-1.png)

##   
5\. [Repositório](#idx-repository)

Criei uma nova branch para esse tutorial chamada “tutorial/parallel-tests”, clique no link abaixo para visualizar:  
[https://github.com/LuizGustavoR/intro-selenium-py/tree/tutorial/parallel-tests](https://github.com/LuizGustavoR/intro-selenium-py/tree/tutorial/parallel-tests)

Fim.

##   
6\. [Bibliografia](#idx-bibliography)

*   [https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/chapter7.html](https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/chapter9.html)
*   [https://www.launchableinc.com/what-is-parallel-testing](https://www.launchableinc.com/what-is-parallel-testing)
