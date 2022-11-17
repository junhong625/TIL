from django.db import models

# Create your models here.
class Movie(models.Model):
    poster_path       = models.CharField(max_length=100)
    backdrop_path     = models.CharField(max_length=100)
    original_title    = models.CharField(max_length=100)
    title             = models.CharField(max_length=30)
    original_language = models.CharField(max_length=20)
    runtime           = models.IntegerField()
    revenue           = models.IntegerField()
    budget            = models.IntegerField()
    vote_count        = models.IntegerField()
    adult             = models.IntegerField()
    movie_id          = models.IntegerField()
    vote_average      = models.FloatField()
    popularity        = models.FloatField()
    release_date      = models.DateField()
    overview          = models.TextField()


    