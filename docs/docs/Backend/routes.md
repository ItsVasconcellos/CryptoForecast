---
title: "Rotas"
sidebar_position: 3
---

## Model Router

### Treinar Modelos

- **Endpoint:** `/api/model/train`
- **Método:** `GET`
- **Resposta:**
  - **200 OK:** `"Todos os modelos treinados com sucesso"`
  - **500 Internal Server Error:** Mensagem de erro detalhando o problema.
- **Descrição:** Treina todos os modelos e registra a operação.

:::tip Dica
Essa rota permite o treino de todos os modelos de uma vez só, retirando a necessidade de enviar diversas requisições para treinar os diferentes modelos.
:::

### Fazer Previsões

- **Endpoint:** `/api/model/predict`
- **Método:** `POST`
- **Corpo da Requisição:**
  - Objeto `PredictionRequest` contendo:
    - `crypto`: A criptomoeda para prever.
    - `days`: Número de dias para prever.
    - `timesteps`: Passos de tempo para a previsão.
- **Resposta:**
  - **200 OK:** Lista de objetos `Result` contendo datas e valores de previsão.
  - **500 Internal Server Error:** Mensagem de erro detalhando o problema.
- **Descrição:** Faz previsões com base na requisição fornecida e registra a operação.

## Log Router

### Obter Logs

- **Endpoint:** `/api/logs/`
- **Método:** `GET`
- **Parâmetros de Consulta:**
  - `limit`: O número máximo de logs a serem recuperados (o padrão é 100).
- **Resposta:**
  - **200 OK:** Lista de objetos `LogModel`
- **Descrição:** Recupera uma lista de logs até o limite especificado.

:::success Exemplo de um LogModel

````{
"log_level": self.log_level,
"message": self.message,
"timestamp": self.timestamp.isoformat(),
}```
:::
````
