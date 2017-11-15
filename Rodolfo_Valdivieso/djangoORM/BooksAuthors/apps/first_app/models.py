# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class book(models.Model):
	name          = models.CharField(max_length=255)
	desc          = models.TextField()
	created_at    = models.DateTimeField(auto_now_add = True)
	updated_at    = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "id: " + str(self.id) + "name: " + str(self.name) + ", desc: " + self.desc 


class author(models.Model):
	books         = models.ManyToManyField(book, related_name="authors")
	first_name    = models.CharField(max_length=255)
	last_name     = models.CharField(max_length=255)
	email         = models.CharField(max_length=255)
	created_at    = models.DateTimeField(auto_now_add = True)
	updated_at    = models.DateTimeField(auto_now=True)
	notes         = models.TextField(null=True)

	def __unicode__(self):
		return "id: " + str(self.id) + "first: " + str(self.first_name) + ", last: " + self.last_name + ", email: " + self.email



