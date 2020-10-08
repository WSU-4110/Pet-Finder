from django.http import HttpResponse, HttpResponseRedirect, Http404
#from django.core.urlresolvers import reverse
from django.core import serializers
from django.views import generic
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required 
from django.contrib.auth import authenticate, login, logout

import string
import random

def random_strgen(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def check_post(request, str_key):
	if str_key not in request.POST:
		return None
	return request.POST[str_key]
	
	