---
title: "FrontEnd"
sidebar_position: 5
---

O frontend foi desenvolvido utilizando **Next.js** e **Chart.js** para fornecer uma interface interativa e intuitiva que permite aos usuários fazer previsões sobre o valor futuro de criptomoedas. O frontend consome a API do backend para obter previsões e exibir os dados de maneira gráfica. A seguir, estão as principais funcionalidades e estrutura da página.

### Funcionalidades Principais

1. **Seleção de Criptomoeda e Período de Previsão**:

   - A página permite ao usuário selecionar uma criptomoeda dentre várias opções (Bitcoin, Ethereum, Solana, entre outras) e o período de previsão (1 dia, 1 semana, 1 mês, etc.).

2. **Previsão de Preços**:

   - Ao clicar no botão "Predict", o frontend envia uma requisição **POST** para o endpoint `/api/model/predict` com os dados da criptomoeda e o período de previsão selecionados.
   - A resposta do servidor contém os dados preditivos que são então exibidos em um gráfico de linha interativo, utilizando o **Chart.js**.

3. **Treinamento de Modelos**:

   - A interface também inclui um botão que chama a rota de treinamento do backend, permitindo o treino de novos modelos de previsão com base em dados atualizados.

4. **Gráfico Interativo**:

   - As previsões geradas são visualizadas por meio de um gráfico de linha, que exibe as datas no eixo X e os valores preditivos no eixo Y. O gráfico é construído utilizando o **Chart.js**, que foi configurado para ser responsivo e incluir legendas, títulos e tooltips.
