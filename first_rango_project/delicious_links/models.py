from django.db import models

from tagging.fields import TagField
from tagging.models import Tag

class Link(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	url=models.CharField(max_length=400)
	date=models.DateTimeField('Date publsihed')
	
	class Meta:
		ordering = ('-date',)
	
	def get_absolute_url(self:
		return "/link/%s/"$self.id
	def __unicode__(self):
		return self.title
	def get_tags(self):
		return Tag.objects.get_for_object(self)
