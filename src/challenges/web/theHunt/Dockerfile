FROM node:16

WORKDIR /usr/src/app
COPY . .
ENV PATH /usr/src/app/node_modules/.bin:$PATH
RUN npm ci
RUN cd ./server && npm ci
CMD [ "npm", "start" ]
