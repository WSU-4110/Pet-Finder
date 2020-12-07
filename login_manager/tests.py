from django.test import TestCase
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from profileManager.models import *

# Create your tests here.
class LoginTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="usertestcase1", password="usertestcase1")
        User.objects.create(username="usertestcase2", password="usertestcase2")

    def test_pass_case_1(self):
        usertestcase1 = User.objects.get(username="usertestcase1")
        self.assertEqual(usertestcase1.password, 'usertestcase1')

    def test_pass_case_2(self):
        usertestcase2 = User.objects.get(username="usertestcase2")
        self.assertEqual(usertestcase2.password, 'usertestcase2')

    def test_fail_case_1(self):
        usertestcase1 = User.objects.get(username="usertestcase1")
        self.assertEqual(usertestcase1.password, 'usertestcase2')

    def test_fail_case_2(self):
        usertestcase2 = User.objects.get(username="usertestcase2")
        self.assertEqual(usertestcase2.password, 'usertestcase1')

    def test_fail_case_3(self):
        self.assertEqual(User.objects.get(username="usertestcase3").username, 'usertestcase3')

class RegisterTestCase(TestCase):
	def setUp(self):
		usertestcase1 = User.objects.create(username="usertestcase1", password="usertestcase1")
		usertestcase2 = User.objects.create(username="usertestcase2", password="usertestcase2")
		Profile.objects.create(user=usertestcase1, phoneNumber='5555555555', about='fake_data', zip='12345', address='123 fake address', city='fakeCity', state='MI')
		Profile.objects.create(user=usertestcase2, phoneNumber='5555555555', about='fake_data_2', zip='12345', address='123 fake address', city='fakeCity', state='MI')

	def test_pass_case_1(self):
		usertestcase1 = User.objects.get(username="usertestcase1")
		self.assertEqual(Profile.objects.get(user=usertestcase1).about, 'fake_data')

	def test_fail_case_1(self):
		usertestcase2 = User.objects.get(username="usertestcase2")
		self.assertEqual(Profile.objects.get(user=usertestcase2).about, 'fake_data')

