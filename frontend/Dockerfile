# Usamos la imagen oficial de Nginx
FROM nginx:alpine

LABEL maintainer="Subgrupo 4 - FitCol"
LABEL description="Frontend FitCol - Interfaz web para gestión de usuarios y rutinas"

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/

# Copiamos los archivos HTML, CSS y JS al directorio de Nginx
COPY html/ /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]