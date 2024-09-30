---
title: "Docker"
sidebar_position: 4
---

Esse arquivo `docker-compose.yml` é utilizado para orquestrar múltiplos serviços de um aplicativo. Há três containers: um para o **backend** (FastAPI), um para o **frontend** (Next.js + TailwindCSS), e outro para o banco de dados **MongoDB**.

### Estrutura Geral

- **services**: Define os diferentes serviços que compõem o aplicativo. Aqui temos três serviços: `backend`, `frontend`, e `db` (banco de dados).
- **volumes**: Dois volumes persistentes são definidos, um para o MongoDB e outro para o BackEnd. Isso garante com que os dados do banco sejam preservados mesmo que o container seja removido, além de permitir o salvamento de modelos localmente, retirando a necessidade de treinar toda vez que o projeto é inciciado.
- **networks**: Define uma rede para facilitar a comunicação entre os containers.

### 1. **Backend (FastAPI)**

- **build**: Indica onde encontrar os arquivos necessários para construir a imagem do backend. O contexto (`context: ./backend`) é o diretório onde está localizado o `Dockerfile`.
- **container_name**: Nome dado ao container do backend (neste caso, `backend`).
- **ports**: Define o mapeamento de portas entre o container e a máquina local. Aqui, a porta 8000 da máquina local está mapeada para a porta 8000 no container, que é onde o FastAPI vai rodar.
- **environment**: Variáveis de ambiente definidas para o container. Elas configuram a URI de conexão ao banco de dados MongoDB e o nome do banco de dados (`cryptoForecast`).
- **depends_on**: Indica que o backend depende do serviço `db` (MongoDB), ou seja, o MongoDB precisa estar rodando antes do backend ser inicializado.

### 2. **Frontend (Next.js + TailwindCSS)**

- **build**: Similar ao backend, isso especifica o diretório e o Dockerfile usado para construir o frontend.
- **container_name**: Nome do container do frontend (neste caso, `frontend`).
- **ports**: Mapeia a porta 3000 da máquina local para a porta 3000 do container, onde o Next.js vai rodar.
- **depends_on**: Indica que o frontend depende do backend, ou seja, o backend precisa estar ativo antes do frontend.
- **networks**: Configura o serviço para participar da rede chamada `network`, permitindo a comunicação com outros serviços, como o backend.

### 3. **MongoDB**

- **image**: Utiliza a última imagem oficial do MongoDB (`mongo:latest`).
- **container_name**: Nome do container do MongoDB (`mongodb`).
- **ports**: Mapeia a porta 27017 da máquina local para a porta 27017 no container, que é onde o MongoDB escuta.
- **volumes**: Define que o MongoDB usará um volume persistente (`mongo_data`) para armazenar seus dados no diretório `/data/db` dentro do container.

### 4. **Volumes**

- **mongo_data**: Volume persistente para armazenar os dados do MongoDB, garantindo que os dados não sejam perdidos ao reiniciar ou recriar o container.

### 5. **Redes**

- **network**: Cria uma rede Docker onde os serviços `frontend` e `backend` podem se comunicar de forma eficiente.

---

Essa configuração é útil para isolar e gerenciar cada parte do sistema, desde o frontend até o banco de dados, com cada serviço rodando em seu próprio container. Além disso, o Docker Compose facilita o gerenciamento do ambiente de desenvolvimento, permitindo inicializar todos os serviços com um único comando (`docker-compose up`).
