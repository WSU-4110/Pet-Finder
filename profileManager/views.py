from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core import serializers
#from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.conf import settings

from .forms import *

# Profile Page Views.
def profile(request, error=None, info=None, success=None, warning=None):
	context = {'title':'Home'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'app/profileManager/profile.html', {'context': context})

# Update Profile Page Views.
def updateProfile(request, error=None, info=None, success=None, warning=None):
	context = {'title':'Home'}
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'app/profileManager/updateProfile.html', {'context': context, 'formset': updateProfileForm(auto_id=False)})

# Saves Profile - ToDo
def saveProfile(request):
	if request.method == 'POST':
		form = Profile(request.POST)              # Validate the request.post
		if form.is_valid(): 
			error = "valid"
			username = form.cleaned_data['username'].lower() #protects against sql injection and converts to lowercase
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password) #Check if username and pass are correct
			if user:
				login(request, user) #sets it into session data the logged in user
				if form.cleaned_data['remember_me']:
					settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
				return HttpResponseRedirect(reverse('dashboard_kpi:kpi_page'))
			else:
				error = "User doesn't exist or invalid password"
				return login_page(request, error)
		else:
			error = "Form isn't valid"
			return login_page(request, error)
	return HttpResponseRedirect(reverse('dashboard_kpi:kpi_page'))
