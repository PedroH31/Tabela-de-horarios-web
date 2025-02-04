FROM node:18-alpine
WORKDIR /frontend
COPY package.json package-lock.json ./
RUN npm install

COPY . . 

RUN mkdir -p /frontend/build

RUN npm run build


RUN chmod -R 755 /frontend/build

CMD ["npm", "run", "dev", "--", "--host"]