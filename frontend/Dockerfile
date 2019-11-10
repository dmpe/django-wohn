FROM node:latest as node_cache
WORKDIR /app/
COPY *.json ./
# COPY yarn.lock ./
RUN ls -al && yarn install
COPY . ./
RUN ls -la && yarn run build

# here we switch from nodejs container to
# having proper, scalable web server: Nginx
# FROM nginx:latest
# RUN (set -e; \
#      apt update; \
#      apt install -y software-properties-common brotli gpg; \
# #     apt-add-repository --yes --update ppa:hda-me/nginx-stable; \
#      apt install nginx-module-brotli;\
#     )
# COPY --from=node_cache /app/dist /usr/share/nginx/html
# EXPOSE 2746
# CMD ["nginx", "-g", "daemon off;"]
