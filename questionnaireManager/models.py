from django.db import models
from django import forms

from django.contrib.auth.models import User

class Questions(models.Model):
    zip = models.CharField(max_length=10, blank=True)
    animal = models.CharField(max_length=3, blank=True)
    rooms = models.CharField(max_length=2, blank=True)
    trait = models.CharField(max_length=10, blank=True)






