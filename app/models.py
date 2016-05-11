from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#class User(models.Model):
#	user = models.OneToOneField(User, unique= True)
#	email = models.EmailField()
#	def __unicode__(self):	
#		return self.user.username

class Task(models.Model):
	title = models.CharField(max_length=32)
	comment = models.TextField()
	deadline = models.DateTimeField()
	priority = models.CharField(default="medium",max_length=10)
	def __unicode__(self):
		return self.title
