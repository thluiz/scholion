---
title: "Executando Testes em Paralelo Com Pytest-Xdist - LuizDeAguiar"
date: '2022-03-28T15:17:09-03:00'
category: webclip
summary: 'Tutorial sobre continuar um projeto Selenium em Python, validar o teste com pytest, usar testes parametrizados e acelerar a execução com o plugin pytest-xdist e a opção -n.'
tags: ["pytest-xdist", "selenium", "testes-paralelos", "pytest"]
has_commentary: false
generated_by: "openai/gpt-5.4-mini"
sources:
  - title: "Executando Testes em Paralelo Com Pytest-Xdist - LuizDeAguiar"
    url: "https://luizdeaguiar.com.br/pt/2022/03/24/executando-testes-em-paralelo/"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2022-03/luizdeaguiar-com-br--executando-testes-em-paralelo.md"
    kind: repo
---

O texto continua um tutorial anterior de Selenium com Python e parte de um repositório já clonado na branch correta. Primeiro ele pede para verificar se o projeto roda com `pipenv run python -m pytest`, depois mostra testes parametrizados com `@pytest.mark.parametrize` e um exemplo de teste para DuckDuckGo.

Em seguida, apresenta `pytest-xdist` como forma de executar testes em paralelo. A página lista cuidados para que os testes sejam independentes, mostra a instalação do plugin com `pipenv install pytest-xdist` e explica a execução com `pipenv run python -m pytest -n 3`, em que `-n` define o número de threads.

## Fichamento

- O tutorial dá sequência a outro material sobre múltiplos navegadores com Selenium e Python.
- Antes de seguir, é preciso clonar a branch `tutorial/multiple-browsers`.
- Para confirmar que o projeto funciona, o texto usa `pipenv run python -m pytest`.
- Testes parametrizados em Python usam `@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])`.
- O exemplo faz o pytest executar a função uma vez para cada valor da lista.
- O teste abre a página do DuckDuckGo, pesquisa a frase e confere o valor do campo e o título do resultado.
- O texto observa que testes de interface web são lentos.
- Para paralelizar no pytest, o tutorial usa o plugin `pytest-xdist`.
- Os testes precisam ser independentes e poder rodar sozinhos e em qualquer ordem.
- O texto alerta para colisões quando testes compartilham estado.
- A instalação do plugin é feita com `pipenv install pytest-xdist`.
- A execução paralela usa `pipenv run python -m pytest -n 3`.
- O número após `-n` indica quantas threads serão usadas.
- O repositório final do tutorial está na branch `tutorial/parallel-tests`.
