FROM node:current as node_cache
WORKDIR /cache/
COPY package.json ./
COPY yarn.lock ./
RUN yarn add install --production


FROM node:current
WORKDIR /app
COPY --from=node_cache /cache/ .
COPY . /app
RUN yarn global add http-server && yarn run build
EXPOSE 2746
CMD ["http-server", "dist"]
