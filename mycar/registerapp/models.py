from django.db import models

class registration(models.Model):
	name = models.CharField(max_length=30)
	district = models.CharField(max_length=30)
	car = models.CharField(max_length=30)
	number = models.CharField(max_length=30)
	licence = models.CharField(max_length=30)


	


# Create your models here.
