from django.db import models
from django.utils import timezone

class Media(models.Model):
    name = models.CharField(max_length=100)
    borrow_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Book(Media):
    author = models.CharField(max_length=100)

class Dvd(Media):
    director = models.CharField(max_length=100)

class Cd(Media):
    artist = models.CharField(max_length=100)

class BoardGame(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)

class Member(models.Model):
    name = models.CharField(max_length=100)
    blocked = models.BooleanField(default=False)
    borrow_count = models.PositiveIntegerField(default=0)
    unblock_date = models.DateField(null=True, blank=True)

    def check_overdue(self):
        if int(self.borrow_count) > 0 and self.unblock_date and self.unblock_date < timezone.now().date():
            self.blocked = False
            self.save()

    def can_borrow(self):
        return not self.blocked and int(self.borrow_count) < 3


