from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)

    description = models.TextField(null=True, blank=True)

    year = models.PositiveIntegerField()

    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])

    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return self.comment
