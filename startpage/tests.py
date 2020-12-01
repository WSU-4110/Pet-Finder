from django.test import TestCase
from startPage.views import *

# Create your tests here.
def test_home(request):
	assert home(request) == 'home page loaded'

def test_petview(request):
	assert petview(request) == 'success'