from django.db import models
from django import forms

from django.contrib.auth.models import User

# Create your models here.

ANIMAL_CHOICES = [
    ('cat', 'Cat'),
    ('dog', 'Dog')
]

INTEGER_CHOICES= [tuple([x,x]) for x in range(1,9)]


class Questions(models.Model):
    animal = forms.CharField(label='What is the ype of animal you are choosing?',
                             widget=forms.Select(choices=ANIMAL_CHOICES))
    energy = forms.IntegerField(label="What is the animal's energy level", widget=forms.Select(choices=INTEGER_CHOICES))
    fur = forms.IntegerField(label="How much should it shed?", widget=forms.Select(choices=INTEGER_CHOICES))
    outside = forms.IntegerField(label="What outside space is available?", widget=forms.Select(choices=INTEGER_CHOICES))
    inside = forms.IntegerField(label="What outside space is available?", widget=forms.Select(choices=INTEGER_CHOICES))






