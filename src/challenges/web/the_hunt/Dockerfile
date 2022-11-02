FROM node:16

# Create app directory
WORKDIR /usr/src/app

COPY package*.json ./ 
COPY /server/package*.json ./server/
COPY *.txt /

# RUN npm install
RUN cd ./server && npm install

RUN cd ..

# Bundle app source
COPY . .

EXPOSE 7504

CMD [ "npm", "start" ]
