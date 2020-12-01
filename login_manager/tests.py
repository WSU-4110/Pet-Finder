from django.test import TestCase
from login_manager.views import *

# Create your tests here.
def test_login_page(request):
	assert login_page(request) == 'login page loaded'

def test_register_page(request):
	assert register_page(request) == 'register page loaded'

def test_login_user(request):
	assert login_user(request) == True

def test_register_user(request):
	assert register_user(request) == "success"

def test_forgot_user(request):
	assert forgot_user(request) == "success"	