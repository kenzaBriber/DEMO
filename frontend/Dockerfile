# Utiliser l'image de base Nginx (version alpine pour la légèreté)
FROM nginx:alpine

# Définir le répertoire de travail dans le conteneur
WORKDIR /usr/share/nginx/html

# Supprimer les fichiers par défaut de Nginx (si nécessaires)
RUN rm -rf ./*

# Copier les fichiers de votre application frontend
COPY . .

# Exposer le port 8080 pour Cloud Run
EXPOSE 8080

# Commande par défaut pour lancer Nginx
CMD ["nginx", "-g", "daemon off;"]
