import datetime

from django.db import models
from django.utils import timezone


class FilmGenres(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Film(models.Model):
    filmGenres_id = models.ForeignKey(FilmGenres, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name