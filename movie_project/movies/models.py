from sys import maxsize
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class movies(models.Model):
    name = models.CharField(max_length=200)
    imdb_score = models.FloatField()
    premiered_on = models.DateField()
    language = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


