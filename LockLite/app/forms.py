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


class AddCredentialForm(forms.ModelForm):
	label = forms.CharField(
		label="Name",
		strip=False,
		widget=forms.TextInput(attrs={
			"placeholder": "Insert a name"
		})
	)
	credentials_email = forms.EmailField(
		label="Email",
		widget=forms.EmailInput(attrs={
			"placeholder": "Insert your credential email",
			"autofocus": True
		})
	)
	credentials_password = forms.CharField(
		label="Password",
		strip=False,
		widget=forms.PasswordInput(attrs={
			"placeholder": "Insert your credential password"
		})
	)

	class Meta:
		model = Credential
		fields = ['label', 'credentials_email', 'credentials_password']
		exclude = ['user']


class UpdateCredentialForm(forms.ModelForm):
	label = forms.CharField(
		label="Name",
		strip=False,
		widget=forms.TextInput(attrs={
			"placeholder": "Insert a name"
		})
	)
	credentials_email = forms.EmailField(
		label="Email",
		widget=forms.EmailInput(attrs={
			"placeholder": "Insert your credential email",
		})
	)
	credentials_password = forms.CharField(
		label="Password",
		strip=False,
		widget=forms.PasswordInput(attrs={
			"placeholder": "Insert your credential password"
		})
	)

	class Meta:
		model = Credential
		fields = ['label', 'credentials_email', 'credentials_password']
		exclude = ['user']


class DeleteCredentialForm(forms.ModelForm):
	class Meta:
		model = Credential
		fields = []
