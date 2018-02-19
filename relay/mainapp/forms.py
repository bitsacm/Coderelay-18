from django import forms
import re
from django.core import validators

class registerform(forms.Form):
	teamname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TeamName'}))

	name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))

	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),max_length=20)
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),max_length=20)
	id = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'BITS ID'}), validators=[\
		validators.RegexValidator(re.compile('^201[0-9]{1}[0-9A-Z]{4}[0-9]{4}P'),message='BITS ID is invalid',code='invalid!')])


class loginform(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),max_length=20)
	id = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'BITS ID'}),validators=[\
		validators.RegexValidator(re.compile('^201[0-9]{1}[0-9A-Z]{4}[0-9]{4}P'),message='BITS ID of teammate 1 is empty or invalid',code='invalid!')])
