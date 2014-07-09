from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Accessing Django built in User authentication tools and importing the User model. 
"""class User(models.Model):
	username
	password
	email
	first_name
	last_name
"""
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	role = models.CharField(max_length=20)
	about_you = models.CharField(max_length=500)
	address = models.CharField(max_length = 100)
	city = models.CharField(max_length = 100)
	state = models.CharField(max_length = 20)

	def __unicode__(self):
		return self.user
