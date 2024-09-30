---
title: "Arquitetura da Solução"
sidebar_position: 1
---

## Arquitetura da Solução

Para a solução, optei por utilizar a mesma arquitetura que utilizei no projeto do módulo, devido a sua robustez e fácil mantenabilidade. A escolha pelo `fastapi` se deve pela necessidade de interagir com o modelo de predição, visto que `python` é uma das ferramentas mais eficientes no mercado para isso . Além disso, a utilização de um único framework facilita lidar com versionamento de bibliotecas, além da interação com o banco de dados se torna mais ágil.

## Estrutura do Backend

A arquitetura consiste em quatro componentes principais: **routers**, **repositories**, **models** e **services**. As funcionalidades do serviço estão implementadas em três rotas fundamentais, descritas a seguir.

### Routers

Os **routers** são responsáveis pela implementação das rotas da API. Eles recebem as requisições HTTP, processam os dados de entrada, e encaminham as solicitações para os services adequados para a manipulação dos dados. No projeto, temos duas principais rotas:

1. **/api/logs**: Esta rota lida com as operações relacionadas aos logs gerados pela aplicação, fornecendo funcionalidades como listar logs com limite definido, utilizando o `LogService` para recuperar os registros.

   - Exemplo: `GET /api/logs` recupera uma lista dos logs armazenados.

2. **/api/model**:
   - **/train**: Essa rota treina os modelos de previsão para diferentes criptomoedas. Após o treinamento, logs são gerados para acompanhar o sucesso ou erros no processo.
   - **/predict**: Permite fazer previsões sobre os preços das criptomoedas com base nos modelos treinados. Ela recebe dados como a criptomoeda, dias de previsão e retorna uma lista de previsões.

### Repositories

Os **repositories** são responsáveis pela interação direta com o banco de dados. Eles implementam operações como criar, ler, atualizar e deletar (CRUD), além de outras operações necessárias para gerenciar os modelos de previsão e logs. Cada repository manipula diretamente os objetos dos models, delegando as operações ao MongoDB.

- **GridRepo**: Implementa o sistema de armazenamento de arquivos com GridFS. _(Fora de uso)_
- **ModelRepository**: Armazena e recupera metadados dos modelos de machine learning treinados. _(Fora de uso)_
- **LogRepository**: Gerencia a gravação e leitura dos logs de execução no banco de dados, essenciais para auditoria e acompanhamento das operações.

### Models

Os **models** representam as entidades e os objetos manipulados pelo sistema. No projeto, os principais models incluem:

- **Model**: Representa um modelo de predição de criptomoedas, armazenando atributos como o nome do modelo e a localização no banco de dados.
- **LogModel**: Representa os logs gerados pelo sistema, contendo informações como nível de log, mensagem e data/hora.
- **Result**: Representa o resultado gerado através de uma previsão, formando um modelo para o fastapi ser capaz de lidar.

Esses models são definidos utilizando o Pydantic para garantir a validação de dados e tipos ao longo da aplicação, assegurando que as informações sejam manipuladas de forma segura e consistente.

### Services

Os **services** contêm a lógica de negócios da aplicação. Eles instanciam e utilizam os repositories para realizar as operações necessárias e implementam regras específicas sobre como os dados devem ser manipulados. Cada service é implementado como um **singleton**, garantindo que uma única instância seja compartilhada por toda a aplicação, evitando inconsistências.

- **Create_Model**: Serviço responsável pela implementação da lógica de treinamento de modelos, garantido com que toda a pipeline seja executada na ordem correta.
- **LogService**: Responsável por gerenciar a gravação e leitura dos logs. Todas as operações de log passam por esse service, que garante que as mensagens sejam armazenadas corretamente.
- **GridService**: Gerencia o treinamento e a previsão dos modelos de machine learning. Ele orquestra a execução do treinamento dos modelos com base em dados históricos, e realiza previsões com base nos parâmetros recebidos na rota `/api/model/predict`.


### Utils e DB

A pasta Utils tem como característica a implementação de funções e classes que serão utilizadas múltiplas vezes no projeto, assim contendo um modelo para a requisição de `predições` e as diferentes criptomoedas utilizadas durante o projeto.

Já a pasta DB, contém um único arquivo, o qual permite com que o aplicativo se comunique diretamente com o contâiner do MongoDB.

### Funcionamento Geral

No fluxo da aplicação, uma requisição é recebida por um router, que a valida e chama o service correspondente para processar os dados. O service utiliza o repository para interagir com o banco de dados (MongoDB), seja para buscar logs, armazenar previsões ou manipular modelos de predição. O resultado é então retornado ao cliente através do router.

Essa estrutura modular e bem definida facilita a manutenção, o crescimento e a escalabilidade do projeto, permitindo a adição de novas funcionalidades sem impactar outras partes do sistema.
