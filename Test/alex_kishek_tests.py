from django.test import TestCase
from login_manager.views import *

# Create your tests here.
def unitTesting(test):
    def test_login_page(self):
        self.assertEqual(login_page(), "login page loaded")

    def test_register_page(self):
        self.assertEqual(register_page(), "register page loaded")

    def test_login_user(self):
        self.assertEqual(login_user(), True)

    def test_register_user(self):
        self.assertEqual(register_user(), "success")

    def test_forgot_user(self):
        self.assertEqual(forgot_user(), "success")
        
        
from django.test import TestCase
from startPage.views import *

# Create your tests here.
def unitTesting(test):
    def test_home(request):
        self.assertEqual(home(), 'home page loaded')

    def test_petview(request):
        self.assertEqual(petview(), 'success')


