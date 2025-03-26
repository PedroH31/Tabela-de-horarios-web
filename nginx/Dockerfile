FROM nginx:1.27.3-alpine-slim

COPY /nginx-setup.conf /usr/share/nginx/html/index.default.conf

CMD ["nginx", "-g", "daemon off;"]