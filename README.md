# Gestion de la médiathèque

Ce projet est une application Django pour gérer les ressources d'une médiathèque, incluant des fonctionnalités telles que la gestion des utilisateurs, des médias et des réservations.



## **Prérequis**

Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre machine :

1. **Python** (version 3.10 ou supérieure)
2. **Git**

Aucun prérequis supplémentaire n'est nécessaire grâce à l'utilisation de SQLite comme base de données.



## **Étapes d'installation**

### **1. Cloner le dépôt**
Clonez le dépôt GitHub sur votre machine locale :

git clone <URL_DU_DEPOT>
cd PythonProject


### **2. Créer et activer un environnement virtuel**
Créez un environnement virtuel pour isoler les dépendances du projet :

python -m venv .venv


Activez l'environnement virtuel :
- **Windows** :
 
  .venv\Scripts\activate

- **Mac/Linux** :

  source .venv/bin/activate


### **3. Installer les dépendances**
Installez toutes les dépendances nécessaires à partir du fichier `requirements.txt` :
```bash
pip install -r requirements.txt


### **4. Configurer la base de données**

Le projet utilise une base de données SQLite par défaut. Aucun prérequis supplémentaire n'est nécessaire. Si vous devez réinitialiser la base de données, supprimez le fichier `db.sqlite3` et relancez les migrations (voir étape 5).

---

### **5. Appliquer les migrations**
Exécutez les migrations pour initialiser la base de données :

python manage.py makemigrations
python manage.py migrate


### **6. Charger le jeu d'essais**
Un jeu d'essais est inclus pour tester le projet. Chargez-le avec la commande suivante :

python manage.py loaddata fixtures.json


### **7. Lancer le serveur**
Démarrez le serveur de développement local :

python manage.py runserver


Accédez à l'application dans votre navigateur à l'adresse :

http://127.0.0.1:8000




## **Structure du projet**

Voici la structure des fichiers principaux :
```
PythonProject/
├── library_management/
│   ├── manage.py
│   ├── requirements.txt
│   ├── db.sqlite3
│   ├── fixtures.json
│   ├── ...
├── .venv/
└── README.md
```

---

## **Stratégie de tests**

### **1. Tests unitaires**
Les tests unitaires sont implémentés pour vérifier les fonctionnalités principales du projet. Ils sont localisés dans le fichier `tests.py` et couvrent les cas suivants :
- Création d'un membre.
- Limite des emprunts pour un membre.
- Mise à jour des informations d'un membre.
- Suppression d'un membre.

Pour exécuter les tests unitaires, utilisez la commande suivante :

python manage.py test



### **2. Scénarios de test manuels**
Voici quelques scénarios à vérifier manuellement :
- Créer, modifier, et supprimer un membre via l'interface utilisateur.
- Ajouter et emprunter des médias.
- Vérifier que les membres bloqués ne peuvent pas emprunter.
- Tester les API REST via un outil comme Postman ou cURL.

