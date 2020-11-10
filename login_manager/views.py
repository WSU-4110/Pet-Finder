from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core import serializers
#from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.conf import settings

from .forms import *
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
	return render(request, 'app/loginManager/login_base.html', {'context': context, 'formset': LoginForm(auto_id=False)})

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
	if form:
		return render(request, 'app/loginManager/register_base.html', {'context': context, 'formset': RegisterForm, 'form': form})
	return render(request, 'app/loginManager/register_base.html', {'context': context, 'formset': RegisterForm})

#logins in our user
def login_user(request):
	if request.method == 'POST':
		form = LoginPage(request.POST)
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
	return render(request, 'app/loginManager/forgot_base.html', {'context': context, 'formset': ForgotForm})