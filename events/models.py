from __future__ import unicode_literals
from tinymce.models import HTMLField
from django.db import models

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length=254)
	slug = models.SlugField()
	date = models.DateField()
	time = models.TimeField()
	Location = models.TextField()
	Description = HTMLField(blank=True)

	def __str__(self):
		return self.name