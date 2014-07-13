from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

class UserProfile(models.Model):
	"""Adds a website and profile picture field in addition to the User model which provides basic fields such as Username and password. User built and provided by django""" 	
    # This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	#Need to go down one more level of instances compared to previous unicodes since there is now a User linked to this model and we identify this by, most logically, the username
	def __unicode__(self):
		return self.user.username
