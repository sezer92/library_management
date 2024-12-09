from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Définit le module de configuration de Django pour Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_management.settings')

# Crée une instance de Celery
app = Celery('library_management')

# Charge la configuration depuis les settings de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-découverte des tâches de toutes les applications installées
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
