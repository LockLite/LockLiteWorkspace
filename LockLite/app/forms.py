from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import Credential


class LoginForm(AuthenticationForm):
	username = UsernameField(
		widget=forms.TextInput(attrs={
			"autofocus": True,
			"placeholder": "Insert your username"
		}),
	)
	password = forms.CharField(
		label="Password",
		strip=False,
		widget=forms.PasswordInput(attrs={
			"autocomplete": "current-password",
			"placeholder": "Insert your password"
		})
	)


class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class CredentialForm(forms.ModelForm):
	class Meta:
		model = Credential
		fields = '__all__'
