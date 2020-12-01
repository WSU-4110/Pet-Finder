
from django import forms
from django.contrib.auth.models import User
from .models import pets

from .models import *


class PetForm(forms.ModelForm):
    class Meta:
        model = pets
        fields = ('animal', 'breed', 'name', 'color')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['animal'].widget.attrs.update({'class': 'textarea', 'placeholder': 'Enter the type of animal.'})
        self.fields['breed'].widget.attrs.update({'class': 'textarea', 'placeholder': 'Enter the breed of the animal.'})
        self.fields['name'].widget.attrs.update({'class': 'textarea', 'placeholder': 'Enter the name of the animal.'})
        self.fields['color'].widget.attrs.update({'class': 'textarea', 'placeholder': 'Enter the Color of the animal.'})

