# Gestion de la médiathèque

Ce projet est une application Django pour gérer les ressources d'une médiathèque, incluant des fonctionnalités telles que la gestion des utilisateurs, des médias et des réservations.

---

## **Prérequis**

Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre machine :

1. **Python** (version 3.10 ou supérieure)
2. **Git**
3. **PostgreSQL** (avec `pg_config` configuré pour fonctionner avec `psycopg2`)
4. **Microsoft Visual C++ Build Tools** (pour compiler certaines dépendances Python sous Windows)

---

## **Étapes d'installation**

### **1. Cloner le dépôt**
Clonez le dépôt GitHub sur votre machine locale :

git clone <URL_DU_DEPOT>
cd PycharmProjects/PythonProject


---

### **2. Créer et activer un environnement virtuel**
Créez un environnement virtuel pour isoler les dépendances du projet :

python -m venv .venv

Activez l'environnement virtuel :
- **Windows** :

  .venv\Scripts\activate

- **Mac/Linux** :
 
  source .venv/bin/activate
  ```

---

### **3. Installer les dépendances**
Installez toutes les dépendances nécessaires à partir du fichier `requirements.txt` :

cd library_management
pip install -r requirements.txt

pour lancer le projet 
cd library_management
python manage.py runserver


---

### **4. Configurer la base de données**

Assurez-vous que PostgreSQL est installé et configuré. Créez une nouvelle base de données pour le projet :
```sql
CREATE DATABASE library_management;
```

Mettez à jour le fichier `settings.py` pour y inclure les informations de connexion à la base de données :
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library_management',
        'USER': 'postgres',
        'PASSWORD': 'MyS3cureP@ssw0rd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### **5. Appliquer les migrations**
Exécutez les migrations pour initialiser la base de données :
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **6. Lancer le serveur**
Démarrez le serveur de développement local :

python manage.py runserver


Accédez à l'application dans votre navigateur à l'adresse :
```
http://127.0.0.1:8000
```

---

## **Résolution des problèmes courants**

### **Erreur : `pg_config` introuvable**
Installez PostgreSQL et ajoutez le chemin vers `pg_config` dans votre variable d'environnement `PATH`.

### **Erreur : `Microsoft Visual C++ 14.0` requis**
Installez les [Microsoft Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

