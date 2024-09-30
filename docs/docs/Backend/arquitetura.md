---
title: "Arquitetura da Solução"
sidebar_position: 1
---

## Arquitetura da Solução

Para a solução, optei por utilizar a mesma arquitetura que utilizei no projeto do módulo, devido a sua robustez e fácil mantenabilidade.
Ao iniciar a Sprint, o grupo chegou à conclusão de que seria mais eficiente o uso de um backend único em **fastapi** do que o uso de dois backends, um em **typescript** e outro em **fastapi**. Isso se deve pela necessidade de se utilizar **python** para interagir com o modelo de predição, visto que é uma das ferramentas mais eficientes no mercado. Além disso, a utilização de um único framework facilita lidar com versionamento de bibliotecas, além da interação com o banco de dados se torna mais ágil.

Como é possível ver no diagrama, a nova arquitetura consiste em um frontend em **nuxt** , backend em **Fastapi** e um **Datalake** em **MongoDB**. Para complementar a explicação da arquitetura, é importante destacar as vantagens trazidas por essa unificação do backend. A escolha pelo FastAPI deve-se à sua maior eficiência na integração com o modelo de predição em Python. Além disso, a arquitetura anterior, que separava o backend em duas linguagens distintas (TypeScript e Python), gerava uma maior complexidade, especialmente no que diz respeito à manutenção do código, integração entre diferentes stacks tecnológicas e a necessidade de gerenciar dependências em ambientes separados. Além disso, o overhead de comunicação entre dois servidores distintos poderia resultar em latência adicional, o que poderia impactar diretamente a experiência do usuário.

Essa abordagem mais enxuta também reflete em uma menor complexidade na infraestrutura, visto que há uma diminuição na quantidade de serviços a serem monitorados e gerenciados, o que impacta positivamente na confiabilidade do sistema como um todo.

Com o MongoDB como nosso DataLake, temos acesso a um banco de dados não relacional e a um File System chamado GridFS. Conseguimos salvar todos os dados e logs da aplicação em coleções do banco de dados NoSQL e os modelos gerados no GridFS.

## Estrutura do Backend

### Models

A pasta models representa uma abstração das classes que lidaremos dentro do backend, assim como seus atributos. Há dois arquivos nessa pasta, o `knr.py` e o `models.py`, ambos contendo duas classes dentro deles. O KNR representa um veículo que está percorrendo a linha de produção, tendo as classes `KNR` e `KNRUpdate`. Já o models, representa um modelo de predição, juntamente com sua localização dentro do banco de dados. Assim como o KNR, o models possui uma classe padrão e uma classe de atualização, para permitir que uma instância seja atualizada com novas informações.

### Repositories

Os `repositories` são responsáveis por implementar as funções que os modelos devem possuir. Ou seja, eles são classes que realizam manipulações em objetos dos modelos. Há repositories tanto para o `KNR`, quanto para `Model`. Neles são implementados métodos de maneira idêntica a um `crud` de um site, ou seja, Create, Read one, Read All, Update e Delete.

### Services

Os `Services` realizam a implementação dos métodos do repositório em uma classe, através da instanciação do primeiro em seu construtor. Para ser possível acessar as classes criadas dentro da pasta service em qualquer lugar, cada service possui um singleton, ou seja, uma implementação da classe que terá uma única instância. Assim, garantindo sempre que o Router, o qual é a abstração de nível mais alto, estará lidando com o mesmo service.

### Router

Os `routers` são responsáveis pela implementação das rotas da API, ou seja, utilizam uma instância do Service para realizar operações no banco de dados. Eles são responsáveis por receber as requisições HTTP e direcioná-las para as funções adequadas no Service, que irão manipular os dados no banco de dados conforme necessário. Eles recebem as requisições, extraem os parâmetros necessários e chamam as funções apropriadas no "Service" para manipular os dados no banco de dados conforme necessário. Além disso, eles lidam com a validação dos dados de entrada, garantindo que não haverá exceções no resto do código.
