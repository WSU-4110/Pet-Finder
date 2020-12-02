from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core import serializers
#from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.conf import settings

from .forms import *
from profileManager.forms import *
from profileManager.models import *
from . import utils

# renders our login page
def login_page(request, error=None, info=None, success=None, warning=None):
	context = {'title':'Login'}
	logout(request)
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	if request.method == 'POST':
		print(request.POST)
		checkLogin = login_user(request)
		if checkLogin:
			context = {'title':'Home'}
			return render(request, 'app/startpage/startpage.html', {'context': context})
	return render(request, 'app/loginManager/login_base.html', {'context': context, 'formset': LoginForm(auto_id=False)}), "login page loaded"
	
#renders our register page
def register_page(request, error=None, info=None, success=None, warning=None, form=None):
	context = {'title':'Register'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	if request.method == 'POST':
		register_user(request)
		return render(request, 'app/startpage/startpage.html', {'context': context})
	return render(request, 'app/loginManager/register_base.html', {'context': context, 'formset': (RegisterForm, updateProfileForm) }), "register_page_loaded"

#logins in our user
def login_user(request):
	if request.method == 'POST':
		data = request.POST
		username = data['username']
		password = data['password']
		checkUser = User.objects.get(username=username, password=password)
		print(checkUser)
		#user = authenticate(request, username=username, password=password)
		#print(user)
		if checkUser:
			login(request, checkUser) #sets it into session data the logged in user
			return True
		else:
			error = "User doesn't exist or invalid password"
			print(error)
			return False

def register_user(request):
	if request.method == 'POST':
		print(request.POST)
		data = request.POST
		username = data['username']
		password = data['password']
		email = data['email']
		phoneNumber = data['phoneNumber']
		about = data['about']
		addressZip = data['zip']
		address = data['address']
		city = data['city']
		state = data['state']
		newUser = User.objects.create(username=username, password=password, email=email)
		newUser.save()
		print(newUser)
		if newUser.id:
			newProfile = Profile.objects.create(user=newUser, phoneNumber=phoneNumber, about=about, zip=addressZip, address=address, city=city, state=state)
			newProfile.save()
			print(newProfile)
			print("success")

	# renders our login page
def forgot_user(request, error=None, info=None, success=None, warning=None, form=None):
	context = {'title':'Login'}
	logout(request)
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	if form:
		return render(request, 'app/loginManager/forgot_base.html', {'context': context, 'formset': ForgotForm, 'form': form})
	return render(request, 'app/loginManager/forgot_base.html', {'context': context, 'formset': ForgotForm}), "success"
