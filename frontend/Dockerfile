FROM node:latest as node_cache
RUN (set -e; \
    apt update; \
    apt install -y tree;\
  )
WORKDIR /app/
COPY *.json ./
# COPY yarn.lock ./
RUN ls -al
RUN npm install --verbose
COPY . ./
RUN tree src/ && npm run build

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
