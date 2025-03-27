FROM nginx:1.27.3-alpine-slim

COPY --from=build /app/frontend/dist /usr/share/nginx/html

COPY /nginx-setup.conf /usr/share/nginx/html/index.default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]