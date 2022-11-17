from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

# Create your models here.
class Review(models.Model):
    writer      = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='writed_reviews', on_delete=models.CASCADE)
    rank        = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    movie       = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    movie_title = models.CharField(max_length=100)
    title       = models.CharField(max_length=30)
    content     = models.TextField()
