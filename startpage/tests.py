from django.test import TestCase
from startPage.views import *

# Create your tests here.
def unitTesting(test):
    def test_home(request):
        self.assertEqual(home(), 'home page loaded')

    def test_petview(request):
        self.assertEqual(petview(), 'success')
