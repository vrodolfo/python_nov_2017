# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import Users
from django.core.urlresolvers import reverse
from django.contrib import messages
import bcrypt

# Create your views here.


def index(request):
	if request.session.get('first_name')== None:
		request.session['first_name']=""
	if request.session.get('last_name')== None:
		request.session['last_name']=""
	if request.session.get('email_address')== None:
		request.session['email_address']=""
	if request.session.get('status')== None:
		request.session['status']=""
	return render(request, 'first_app/index.html')

def goback(request):
	request.session['first_name']=""
	request.session['last_name']=""
	request.session['email_address']=""
	request.session['status']=""
	return redirect('/')

def result(request):
	return render(request, 'first_app/result.html')

def login(request):
	errors = {}
	user = Users.objects.filter(email_address=request.POST['email_address']).first()

	if user:
		pw= str(request.POST['password'])
		request.session['status']="NotNew"
		if not bcrypt.checkpw(pw.encode(), user.password.encode()):
			errors['password'] = "Password does not match!"
	else:
		errors['email_address'] = "Email not registered!"
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	else:
		return redirect('/result')


def register(request):
	request.session['first_name']=request.POST['first_name']
	request.session['last_name']=request.POST['last_name']
	request.session['email_address']=request.POST['email_address']
	request.session['status']=""

	errors = Users.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
	else:
		pw= str(request.POST['password'])
		hashed_pw = bcrypt.hashpw(pw, bcrypt.gensalt())
		Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'], password=hashed_pw)
		request.session['status']="New"
		return redirect('/result')