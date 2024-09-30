---
title: "Guia de Execução"
sidebar_position: 2
---

## Pré-requisitos

Antes de iniciar, certifique-se de que você tem os seguintes itens instalados:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/)

## Passo a Passo

### 1. Clone o repositório

Abra o terminal e execute o seguinte comando para clonar o repositório do projeto:

```bash
git clone https://github.com/seu-usuario/CryptoForecast.git
```

### 2. Navegue até o diretório do projeto

```bash
cd CryptoForecast/src
```

### 3. Execute o Docker Compose

Certifique-se de que o Docker e o Docker Compose estão instalados. Em seguida, execute o seguinte comando:

```bash
docker-compose up --build
```

### 4. Acesse o projeto

Após a construção e inicialização dos contêineres, acesse o projeto através do endereço fornecido pelo Docker Compose.

:::tip Localização dos serviços
**Backend**: localhost:8000
**Frontend**: localhost:3000
**MongoDB**: localhost:27017
:::

## Conclusão

Agora você deve ver o projeto CryptoForecast em execução, seja localmente ou via Docker. Siga as instruções na tela para continuar.
