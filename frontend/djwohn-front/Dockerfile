# base image
FROM node:current

# set working directory
WORKDIR /app

# install and cache app dependencies
COPY package.json /app/package.json
RUN yarn install

COPY . /app

# start app
CMD ["yarn", "run", "serve"]
EXPOSE 8080
