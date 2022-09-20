from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('Manager', 'Manager'),
    ('Viewer', 'Viewer'),
)
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(choices=CATEGORY_CHOICES, max_length=8)

class Movies(models.Model):
    movie = models.CharField(max_length=100)
    release_date = models.DateField()
    durations = models.IntegerField()

class Cinema(models.Model):
    cinema_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    number_of_screen = models.IntegerField()

class Screen(models.Model):
    screen= models.CharField(max_length=100)
    cinema= models.ForeignKey(Cinema, on_delete=models.CASCADE)

class Movie_Run(models.Model):
    start_time = models.TimeField()
    end_time=models.TimeField()
    screen= models.ForeignKey(Screen, on_delete=models.CASCADE)
    movies= models.ForeignKey(Movies, on_delete=models.CASCADE)

class Actor(models.Model):
    actor_name=models.CharField(max_length=100)

class Movie_Cast(models.Model):
    character_name=models.CharField(max_length=100)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE) 
    movies= models.ForeignKey(Movies, on_delete=models.CASCADE)