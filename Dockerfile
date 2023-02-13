# Partir de l'image Python 3.9-slim-bullseye
FROM python:3.9-slim-bullseye

# Définir le répertoire de travail
WORKDIR /usr/src/app

# Copier les fichiers de requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances requises en utilisant pip
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier le code source de votre application dans le conteneur
COPY project .

# Définir le port sur lequel votre application Django écoutera
EXPOSE 8000

# Démarrer l'application en exécutant la commande suivante
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]