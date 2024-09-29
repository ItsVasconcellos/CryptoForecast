ARG NODE_VERSION=lts

FROM node:${NODE_VERSION}-slim as base

WORKDIR /app

FROM base as build

COPY package.json package-lock.json ./
RUN npm install 

COPY . .

RUN npm run build

FROM base

ENV NODE_ENV=production
ENV PORT=3000

COPY --from=build /app/node_modules /app/node_modules
COPY --from=build /app/package.json /app/package.json

COPY --from=build /app/.next /app/.next

EXPOSE 3000

CMD ["npm", "start"]
