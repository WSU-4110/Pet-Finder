from django import forms
from django.contrib.auth.models import User


from .models import *


class updateUserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }


class updateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phoneNumber', 'about', 'zip', 'address', 'city', 'state')
        widgets = {
            'phoneNumber': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'about': forms.TextInput(attrs={'placeholder': 'About Me'}),
            'zip': forms.TextInput(attrs={'placeholder': 'Zip Code'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
        }


"""
class LoginPage(forms.Form):
	username = forms.CharField(label='Username', max_length=32, required=True, error_messages={'required': 'Please enter your Username'}, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class' : 'form-control'}))
	password = forms.CharField(label='Password', max_length=32, required=True, error_messages={'required': 'Please enter your Password'}, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class' : 'form-control'}))
	remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())

class ForgetPage(forms.Form):
	forget_email = forms.EmailField(label='forget_email', max_length=64, required=True, error_messages={'required': 'Please enter your email'})
	forget_username = forms.CharField(label='forget_username', max_length=64, required=True, error_messages={'required': 'Please enter your username'})

class ForgotPage(forms.Form):
	forgot_email = forms.EmailField(label='forgot_email', max_length=64, required=True, error_messages={'required': 'Please enter your email'})
	
class RegisterPage(forms.Form):
	reg_email = forms.EmailField(label='Email Address', max_length=32, required=True, error_messages={'required': 'Please enter your Email'}, widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class' : 'form-control'}))
	reg_username = forms.CharField(label='Username', max_length=32, required=True, error_messages={'required': 'Please enter your Username'}, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class' : 'form-control'}))
	reg_password = forms.CharField(label='Password', max_length=32, required=True, error_messages={'required': 'Please enter your Password'}, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class' : 'form-control'}))
	reg_confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class' : 'form-control'}))
	class Meta:
	    model=User
	    fields=('username','email','password')

	def clean(self):
		cleaned_data = super(RegisterPage, self).clean()
		password = cleaned_data.get("reg_password")
		confirm_password = cleaned_data.get("reg_confirm_password")
		if password != confirm_password:
			raise forms.ValidationError(
				"password and confirm_password does not match"
			)
		return cleaned_data
	
class ChangePasswordPage(forms.Form):
	change_currentPassword = forms.CharField(label='change_currentPassword', max_length=32, required=True, error_messages={'required': 'Please enter your Username'})
	change_newPassword = forms.CharField(label='change_newPassword', max_length=32, required=True, error_messages={'required': 'Please enter your Password'})
	change_nnewPassword = forms.CharField(label='change_nnewPassword', max_length=32, required=True, error_messages={'required': 'Please enter your Email'})

"""
