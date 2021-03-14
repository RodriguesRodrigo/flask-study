# Requisitos

 - Python 3.6 (versão mínima)

# Rodar o projeto

## Instalando as dependências

> Obs: É de boa prática utilizar o virtualenv para melhor organização dos pacotes.

1) Existem duas formas para instalar as dependências do projeto:

> Obs: Caso você não consiga utilizar o make por causa do seu sistema operacional, basta abrir o arquivo e executar o comando manualmente.

1.1) Instalando as dependências básicas parar rodar o projeto:

```
$ make install
```

1.2) Para instalar todas as dependências do projeto, incluindo as de desenvolvimento, rode o comando abaixo:

```
$ make install-dev
```

2) Faça uma cópia do arquivo .env.example com o nome .env e insira os valores de cada variavel de ambiente.

## Rode o projeto

Basta rodar o comando abaixo:

```
$ make run-dev
```

# Rodar os testes

Instale todas as dependências de desenvolvimento e depois execute os testes:

```
$ make install-dev
$ make test
```
