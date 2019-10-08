# base image
FROM node:current

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/package.json
RUN yarn install

COPY . /app

# start app
CMD ["yarn", "run", "serve"]
EXPOSE 8080
