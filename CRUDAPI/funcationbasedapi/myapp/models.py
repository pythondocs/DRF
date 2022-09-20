from django.db import models

# Create your models here.
class StudentUser(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    city = models.CharField(max_length=70)