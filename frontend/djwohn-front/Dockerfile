FROM node:current

WORKDIR /app

# install and cache app dependencies
COPY package.json /app/package.json
RUN yarn install

COPY . /app

EXPOSE 8080
CMD ["yarn", "run", "serve"]
