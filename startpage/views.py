from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core import serializers
#from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.conf import settings

# Create your views here.
def home(request, error=None, info=None, success=None, warning=None):
	context = {'title':'Home'}
	logout(request)
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'app/startpage/startpage.html', {'context': context}), "home page loaded"

def test_home(request):
	assert home(request) == 'home page loaded'

# Create your views here.
def petview(request, error=None, info=None, success=None, warning=None):
	context = {'title':'Home'}
	logout(request)
	if error:
		context['error'] = str(error)
	if info:
		context['info'] = str(info)
	if warning:
		context['warning'] = str(warning)
	if success:
		context['success'] = str(success)
	return render(request, 'app/startpage/petview.html', {'context': context}), 'success'

def test_petview(request):
	assert petview(request) == 'success'