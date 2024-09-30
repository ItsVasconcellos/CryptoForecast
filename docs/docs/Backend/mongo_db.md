---
title: "Database"
sidebar_position: 2
---

## Opção do MongoDB

A escolha do MongoDB para o projeto CryptoForecast se justifica por sua flexibilidade no armazenamento de dados não estruturados, como os logs de previsões e os modelos de machine learning. O MongoDB, sendo um banco de dados NoSQL, é ideal para armazenar documentos com diferentes formatos e estruturas, o que facilita a criação de coleções adaptáveis ao crescimento e à evolução dos dados ao longo do tempo, sem a rigidez de esquemas fixos.

Além disso, o MongoDB oferece suporte ao GridFS, uma funcionalidade que permite armazenar grandes arquivos, como modelos treinados de machine learning, que podem ultrapassar o limite de tamanho de documentos tradicionais do MongoDB. Apesar de a tentativa inicial de usar o GridFS para o salvamento de modelos ter gerado dificuldades na serialização e recuperação dos arquivos, o MongoDB ainda foi mantido como banco de dados e permite a futura implementação do processo de salvamentos de modelos.

## Coleções

### Models

Essa coleção inicialmente foi projetada para armazenar informações sobre os modelos de machine learning, como o nome do modelo e o caminho de onde ele seria salvo no GridFS. No entanto, o salvamento dos modelos foi reestruturado para o volume do Docker, mantendo a simplicidade e evitando as complexidades encontradas com o GridFS. Além disso, a coleção models permite adicionar os campos de métrica, garantindo a implementação de uma feature de escolha de modelos baseada em uma determinada pipeline.

```py
{
    "model_name": "BitcoinPriceModel_v1",
    "gridfs_path": "/path/to/model/in/gridfs",
    "last_trained": "2024-09-10T12:00:00",
}
```

### Logs

A coleção de logs armazena informações sobre eventos e mensagens importantes relacionados à execução e ao treinamento dos modelos. Essa coleção é crucial para o monitoramento e a auditoria do processo de previsão.

```py
{
    "log_level": self.log_level,
    "message": self.message,
    "timestamp": self.timestamp.isoformat(),
}
```

## Conclusão

Essas coleções são projetadas para manter a flexibilidade no gerenciamento dos dados, com o MongoDB facilitando a escalabilidade do projeto conforme novos tipos de dados ou modelos forem adicionados ao sistema.
