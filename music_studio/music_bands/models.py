from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    year_formed = models.IntegerField()
    biography = models.TextField()

    def __str__(self):
        return self.name