FROM node:current as node_cache
WORKDIR /cache/
COPY package.json ./
COPY yarn.lock ./
RUN yarn add install


FROM node:current
WORKDIR /app
COPY --from=node_cache /cache/ .
COPY . /app
RUN yarn global add local-web-server && yarn run build
EXPOSE 2746
CMD ["ws", "--port=2746", "--directory=dist/"]
