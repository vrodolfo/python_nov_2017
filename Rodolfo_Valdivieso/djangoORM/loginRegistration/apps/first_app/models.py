# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.
class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(str(postData['first_name'])) < 2:
			errors['first_name'] = "First name should be more than 2 characters"
		if any(map(str.isdigit, str(postData['first_name']))):
			errors['first_name'] = "First name should be letters only"

		if len(str(postData['last_name'])) < 2:
			errors['last_name'] = "Last name should be more than 2 characters"
		if any(map(str.isdigit, str(postData['last_name']))):
			errors['last_name'] = "Last name should be letters only"

		if not EMAIL_REGEX.match(str(postData['email_address'])):
			errors['email_address'] = "Invalid Email Format"

		duplicate = Users.objects.filter(email_address=postData['email_address']).first()
		if duplicate:
			errors['email_address'] = "Email already exist!"

		if len(str(postData['password'])) < 8:
			errors['password'] = "Password should be more than 8 characters"
		elif not any(map(str.isupper, str(postData['password']))):
			errors['password'] = "Password should contain at least 1 Capital Letter"

		#validations for birthdate
		
		return errors


class Users(models.Model):
	first_name    = models.CharField(max_length=255)
	last_name     = models.CharField(max_length=255)
	email_address = models.CharField(max_length=255)
	birthDate     = models.DateTimeField(null=True)
	password      = models.CharField(max_length=255)
	created_at    = models.DateTimeField(auto_now_add = True)
	updated_at    = models.DateTimeField(auto_now=True)
	# *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
	objects = UserManager()
	# *************************
	def __unicode__(self):
		return "id: " + str(self.id) + "first_name: " + str(self.first_name) + ", last_name: " + str(self.last_name) +  "email_address: " + str(self.email_address) +  "password: " + str(self.password)


"""
models come with a hidden key:
      objects = models.Manager()
we are going to overwrite this!
"""