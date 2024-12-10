# Library Management

Projet de gestion de médiathèque développé avec Django. 

## Fonctionnalités
- Gestion des membres.
- Gestion des médias.
- Emprunts et retours.
- Notifications automatiques.

## Installation
## Cloner le Dépôt

1. Assurez-vous que Git est installé sur votre machine.
2. Exécutez la commande suivante pour cloner le dépôt :
   ```bash
   git clone https://github.com/sezer92/library_management.git

## Accédez au dossier du projet :

cd library_management


---

### 2. **Installer les Prérequis**
Expliquez comment installer les dépendances Python :
```markdown
## Installer les Prérequis

1. Assurez-vous que Python (version 3.10 ou supérieure) et pip sont installés.
2. Créez et activez un environnement virtuel :
   - Sous Windows :
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - Sous Linux/macOS :
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
3. Installez les dépendances du projet :
   ```bash
   pip install -r requirements.txt


---

### 3. **Configurer la Base de Données**
Ajoutez des étapes claires pour configurer PostgreSQL ou une base de données alternative :
```markdown
## Configurer la Base de Données

1. Installez PostgreSQL sur votre machine.
2. Créez une base de données nommée `library_management`.
3. Modifiez le fichier `settings.py` pour inclure les détails de connexion à la base de données :
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'library_management',
           'USER': 'postgres',
           'PASSWORD': 'votre_mot_de_passe',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
## Appliquez les migrations :

python manage.py migrate


---

### 4. **Lancer le Serveur**
Ajoutez les étapes pour démarrer le serveur Django :
```markdown
## Lancer le Serveur

1. Lancez le serveur local Django :
   ```bash
   python manage.py runserver

Accédez à l'application dans votre navigateur à l'adresse suivante :

http://127.0.0.1:8000


---

### 5. **Ajouter des Instructions pour Tester**
Mentionnez comment exécuter les tests pour valider le bon fonctionnement :
```markdown
## Exécuter les Tests

1. Exécutez les tests unitaires avec la commande suivante :
   ```bash
   python manage.py test

Les résultats des tests s'afficheront dans le terminal.
YAML

Copier le code

---

### 6. **Fichier README.md**
Ajoutez toutes ces informations dans un fichier `README.md` dans le dossier racine de votre projet. Voici un exemple structuré :

```markdown
# Library Management

Projet de gestion de médiathèque développé avec Django. Ce projet permet de gérer les emprunts, les médias, et les membres.

## Fonctionnalités
- Gestion des membres : ajout, suppression, blocage.
- Gestion des médias : livres, CDs, DVDs, jeux de plateau.
- Emprunts et retours.
- Notifications automatiques pour les retards.

## Prérequis
- Python 3.10 ou supérieur
- PostgreSQL
- Git

## Installation
1. Clonez le projet : `git clone https://github.com/sezer92/library_management.git`
2. Accédez au projet : `cd library_management`
3. Installez les dépendances : `pip install -r requirements.txt`
4. Configurez la base de données selon les instructions ci-dessus.

## Lancement
- Lancez le serveur : `python manage.py runserver`
- Accédez à : `http://127.0.0.1:8000`
