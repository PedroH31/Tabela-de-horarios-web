FROM node:18-alpine
WORKDIR /frontend
COPY package.json package-lock.json ./
RUN npm install

COPY . . 

ENV VITE_PORT=8080

RUN npm run build

CMD ["npm", "run", "build", "dev", "--", "--host"]