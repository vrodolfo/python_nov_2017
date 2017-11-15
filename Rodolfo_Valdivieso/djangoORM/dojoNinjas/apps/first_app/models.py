# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class dojo(models.Model):
	name  = models.CharField(max_length=255)
	city  = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	desc  = models.TextField(null=True)
	def __unicode__(self):
		return "id: " + str(self.id) + ", name: " +  str(self.name) + ", city: " +  str(self.city) + ", state: " +  str(self.state) + ", desc: " +  str(self.desc)

class ninja(models.Model):
	dojo_id     = models.ForeignKey(dojo, related_name = "ninjas")
	first_name  = models.CharField(max_length=255)
	last_name   = models.CharField(max_length=255)
	def __unicode__(self):
		return "id: " + str(self.id) + ", dojo_id: " +  str(self.dojo_id) + ", first_name: " +  str(self.first_name) + ", last_name: " +  str(self.last_name) 