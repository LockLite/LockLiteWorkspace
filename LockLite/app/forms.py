from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Credential
from django import forms

class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CredentialForm(forms.ModelForm):
   class Meta:
     model = Credential
     fields = '__all__'
