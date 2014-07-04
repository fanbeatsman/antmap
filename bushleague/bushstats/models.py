from django.db import models


class Player(models.Model):
	name = models.CharField(max_length=128, unique=True)
	wins = models.IntegerField(default=0)
	loses = models.IntegerField(default=0)
	kills = models.IntegerField(default=0)
	deaths = models.IntegerField(default=0)
	gpm = models.IntegerField(default=0)
	bkbtiming = models.TimeField(auto_now=False, auto_now_add=False, default="00:00")
	
	def __unicode__(self):
		return self.name
