---
title: "Estudo de Caso - GridFS e Next"
sidebar_position: 6
---

## GridFS e Salvamento de Modelo

Para esse projeto, a primeira abordagem que tive foi de lidar com o gridfs para o salvamento de modelos. Isso se deve, pois se tornaria muito eficiente poder selecionar diferentes modelos para as diferentes criptomoedas. Além disso, o salvamento de modelos permite que não seja necessário ter o modelo armazenado localmente, diminuindo o armazenamento ocupado pela aplicação.

Todavia, ao seguir nesse direcionamento, enfrentei dificuldades em lidar com o gridfs, especialmente para salvar o arquivo e desserializar o mesmo, tornando um caminho inviável. Ademais, a complexidade da solução aumentou de forma exponencial, fazendo com que não fosse o melhor caminho para a resolução do problema, que foi contornado usando ao salvar os modelos com o artifício do `volume` do Docker

## Uso de Next

Assim como o GridFS, o next é um algo que está sendo utilizado no projeto do grupo, porém na sua versão para `Vue`, o `Nuxt`. Mas diferentemente do GridFS, o `next` simplificou o projeto, provendo uma facilidade na criação de páginas e permitindo lidar facilmente com requests a api.
