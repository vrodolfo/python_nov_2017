# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	first_name    = models.CharField(max_length=255)
	last_name     = models.CharField(max_length=255)
	email_address = models.CharField(max_length=255)
	created_at    = models.DateTimeField(auto_now_add = True)
	updated_at    = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return "id: " + str(self.id) + "first: " + str(self.first_name) + ", last: " + self.last_name + ", email: " + self.email_address

class Book(models.Model):
	liked_users   = models.ManyToManyField(User, related_name="liked_books")
	uploaded_by   = models.ForeignKey(User, related_name = "uploaded_books")
	name          = models.CharField(max_length=255)
	desc          = models.CharField(max_length=255)
	created_at    = models.DateTimeField(auto_now_add = True)
	updated_at    = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return "id: " + str(self.id) +"name: " + str(self.name) + ", desc: " + self.desc 


