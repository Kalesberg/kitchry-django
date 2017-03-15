from django.db import models

# Create your models here.
class Client(models.Model):
	name = models.CharField(max_length=50)
	slug = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	email = models.CharField(max_length=50)
	profile_img = models.CharField(max_length=50)
	weight = models.FloatField(default=70.0)
	stats = models.CharField(max_length=200)
	
	def __str__(self):
		return self.stats