from django import forms
from django.contrib.auth import password_validation
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
	username = UsernameField(
		widget=forms.TextInput(attrs={
			"autofocus": True,
			"placeholder": "Insert your username"
		}),
	)
	email = forms.EmailField(
		label="Email",
		widget=forms.EmailInput(attrs={
			"placeholder": "Insert your email address"
		})
	)
	password1 = forms.CharField(
		label="Password",
		strip=False,
		widget=forms.PasswordInput(attrs={
			"autocomplete": "new-password",
			"placeholder": "Insert your password"
		}),
		help_text=password_validation.password_validators_help_text_html(),
	)
	password2 = forms.CharField(
		label="Confirm",
		widget=forms.PasswordInput(attrs={
			"autocomplete": "new-password",
			"placeholder": "Confirm your password"
		}),
		strip=False,
		help_text="Enter the same password as before, for verification.",
	)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class CredentialForm(forms.ModelForm):
	class Meta:
		model = Credential
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		super(CredentialForm, self).__init__(*args, **kwargs)
		if user:
			self.fields['user'].queryset = User.objects.filter(username=user.username)
