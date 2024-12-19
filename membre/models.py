from django.db import models

class Media(models.Model):
    title = models.CharField(max_length=200)
    available = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Book(Media):
    author = models.CharField(max_length=100)


class Cd(Media):
    artist = models.CharField(max_length=100)


class Dvd(Media):
    director = models.CharField(max_length=100)

class BoardGame(Media):
    creator = models.CharField(max_length=100)
