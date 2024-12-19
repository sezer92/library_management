from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Member(models.Model):
    name = models.CharField(max_length=100)
    blocked = models.BooleanField(default=False)
    borrow_count = models.PositiveIntegerField(default=0)
    unblock_date = models.DateField(null=True, blank=True)

    def can_borrow(self):
        """
        Vérifie si le membre peut emprunter.
        - Le membre ne peut pas emprunter s'il est bloqué.
        - Le membre ne peut pas emprunter plus de 3 médias.
        """
        if self.blocked or self.borrow_count >= 3:
            return False
        return True

    def __str__(self):
        return self.name



class Media(models.Model):
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=50)  # Exemple : 'Book', 'CD', etc.
    available = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Book(Media):
    author = models.CharField(max_length=100)


class Cd(Media):
    artist = models.CharField(max_length=100)


class Dvd(Media):
    director = models.CharField(max_length=100)

class BoardGame(Media):
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Borrow(models.Model):
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Type de modèle
    object_id = models.PositiveIntegerField()  # ID de l'instance spécifique
    media = GenericForeignKey('content_type', 'object_id')  # Référence générique

    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"Borrowed by {self.member.name} on {self.borrow_date}"