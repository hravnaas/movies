from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Actor(models.Model):
    name = models.CharField(max_length = 100)
    movies = models.ManytoManyField(Movies)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)