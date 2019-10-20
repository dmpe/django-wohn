FROM node:current as node_cache
WORKDIR /cache/
COPY package.json .
RUN yarn install



FROM node:current

WORKDIR /app

COPY --from=node_cache /cache/ .

COPY . /app

EXPOSE 2746
CMD ["yarn", "run", "serve"]
