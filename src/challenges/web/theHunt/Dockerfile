FROM node:16

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./ 
COPY /server/package*.json ./server/
COPY *.txt /

RUN npm install --omit=dev
RUN cd ./server && npm install --omit=dev

# Bundle app source
COPY . .

# Note: You cannot run a react app in dev mode without
# an interactive terminal. So above we use `npm install --omit=dev`
# and instead of `npm start` we run `npm index.js`
CMD [ "npm", "index.js" ]
