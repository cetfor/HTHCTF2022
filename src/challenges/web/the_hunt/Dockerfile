FROM node:16

# Create app directory
WORKDIR /usr/src/app

COPY /server/package*.json ./server/
COPY *.txt /

RUN cd ./server && npm install

COPY . .

EXPOSE 7504

CMD [ "npm", "start" ]
