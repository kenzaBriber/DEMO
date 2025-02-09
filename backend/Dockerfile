# Utiliser une image Python légère
FROM python:3.9-slim

# Définir le répertoire de travail


# Copier tous les fichiers dans le conteneur
COPY . .

# Installer les dépendances nécessaires
RUN pip install flask

# Exposer le port 8080 requis par Cloud Run
EXPOSE 8080

# Commande pour démarrer l'application
CMD ["python3", "app.py"]
