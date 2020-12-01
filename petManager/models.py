from django.db import models
from django import forms

from django.contrib.auth.models import User


# Create your models here.


class pets(models.Model):
    animal = models.TextField()
    breed = models.TextField()
    name = models.TextField()
    color = models.TextField()

    def __str__(self):
        return 'pets #{}'.format(self.id)
