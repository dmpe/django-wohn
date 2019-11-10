FROM node:latest as node_cache
WORKDIR /cache/
COPY *.json ./
COPY yarn.lock ./
RUN yarn install
COPY . /app
RUN yarn run build

# here we switch from nodejs container to
# having proper, scalable web server: Nginx
FROM nginx:latest
COPY --from=node_cache /app/dist /usr/share/nginx/html
EXPOSE 2746
CMD ["nginx", "-g", "daemon off;"]
