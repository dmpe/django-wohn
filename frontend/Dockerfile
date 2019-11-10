FROM node:latest as node_cache
ENV NODE_ENV development
RUN (set -e; \
    apt update; \
    apt install -y tree;\
  )
WORKDIR /app/
COPY *.json ./
RUN ls -al
RUN yarn install
COPY . ./
RUN tree src/ && yarn run build

# here we switch from nodejs container to
# having proper, scalable web server: Nginx
FROM nginx:latest
RUN (set -e; \
  apt update; \
  apt install -y software-properties-common brotli gpg; \
# apt-add-repository --yes --update ppa:hda-me/nginx-stable; \
  apt install nginx-module-brotli;\
)
COPY --from=node_cache /app/dist /usr/share/nginx/html
EXPOSE 2746
CMD ["nginx", "-g", "daemon off;"]
