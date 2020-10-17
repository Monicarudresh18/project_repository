from django.db import models

# Create your models here.
class Moviedetails(models.Model):
	moviename = models.CharField(max_length=50)
	hero = models.CharField(max_length=50)
	heroine = models.CharField(max_length=50)
	rating = models.IntegerField()

   
    