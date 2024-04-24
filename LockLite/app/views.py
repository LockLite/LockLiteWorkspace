from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from cryptography.fernet import Fernet

from .forms import RegisterForm, LoginForm, AddCredentialForm, UpdateCredentialForm, DeleteCredentialForm
from .models import Credential

f = Fernet(settings.ENCRYPT_KEY)


class CustomLoginView(LoginView):
	authentication_form = LoginForm
	link_page = "register"
	template_name = 'form.jinja'
	extra_context = {
		'form_title': "Login",
		'form_link': {
			'text': "Don't have an account?",
			'name': link_page.capitalize(),
			'page': link_page
		},
		'form_button_color': 'blue'
	}


def register(request, *args, **kwargs):
	link_page = "login"
	context = {
		'form_title': "Register",
		'form_link': {
			'text': "Already has an account?",
			'name': link_page.capitalize(),
			'page': link_page
		},
		'form_button_color': 'blue'
	}
	if request.method == 'GET':
		context['form'] = RegisterForm()
		return render(request, 'form.jinja', context)
	if request.method == 'POST':
		context['form'] = RegisterForm(request.POST)
		if context['form'].is_valid():
			user = context['form'].save(commit=False)
			user.username = user.username.lower()
			user.save()
			messages.success(request, 'You have signed up successfully.')
			login(request, user)
			return redirect(link_page)
		else:
			return render(request, 'form.jinja', context)


@login_required(login_url="login")
def index(request, *args, **kwargs):
	context = {
		# Dashboard
		'dashboard_username': request.user.username,

		# Datatable
		'datatable_title': 'Credentials',
		'datatable_data': Credential.objects.filter(user_id=request.user.id),
		'datatable_actions': {
			'create': 'createcred',
			'edit': 'updatecred',
			'delete': 'deletecred'
		},
		'datatable_columns': [
			{
				'name': 'Company',
				'key': 'label'
			},
			{
				'name': 'Email',
				'key': 'credentials_email'
			},
			{
				'name': 'Password',
				'key': 'credentials_password'
			}
		]
	}
	return render(request, 'index.jinja', context)


@login_required(login_url="login")
def createcred(request):
	link_page = "index"
	context = {
		'form_title': "Create credential",
		'form_link': {
			'text': "Show credentials",
			'name': "here",
			'page': link_page
		},
		'form_button_color': 'blue'
	}
	if request.method == 'GET':
		context['form'] = AddCredentialForm()
		return render(request, 'form.jinja', context)
	if request.method == 'POST':
		context['form'] = AddCredentialForm(request.POST)
		if not context['form'].is_valid():
			return render(request, 'form.jinja', context)
		credential = context['form'].save(commit=False)

		# Encrypt credential password
		credential_original = context['form'].cleaned_data['credentials_password']
		credential_bytes = credential_original.encode('utf-8')
		credential_encrypted = f.encrypt(credential_bytes)
		credential_decoded = credential_encrypted.decode('utf-8')
		credential.credentials_password = credential_decoded

		credential.user = request.user
		credential.save()
		return redirect('index')


@login_required(login_url="login")
def updatecred(request, pk):
	credential = Credential.objects.get(pk=pk)
	link_page = "index"
	context = {
		'form_title': "Update credential",
		'form_link': {
			'text': "Show credentials",
			'name': "here",
			'page': link_page
		},
		'form_credential': credential,
		'form_button_color': 'blue'
	}
	if request.method == 'GET':
		context['form'] = UpdateCredentialForm(instance=credential)
		return render(request, 'form.jinja', context)
	if request.method == 'POST':
		context['form'] = UpdateCredentialForm(request.POST, instance=credential)
		if not context['form'].is_valid():
			return render(request, 'form.jinja', context)
		credential = context['form'].save(commit=False)

		# Encrypt credential password
		credential_original = context['form'].cleaned_data['credentials_password']
		credential_bytes = credential_original.encode('utf-8')
		credential_encrypted = f.encrypt(credential_bytes)
		credential_decoded = credential_encrypted.decode('utf-8')
		credential.credentials_password = credential_decoded

		credential.user = request.user
		credential.save()
		return redirect('index')


@login_required(login_url="login")
def deletecred(request, pk):
	credential = Credential.objects.get(pk=pk)
	link_page = 'index'
	context = {
		'form_title': 'Delete credential',
		'form_link': {
			'text': '',
			'name': 'Cancel',
			'page': link_page
		},
		'form_credential': credential,
		'form_button_color': 'red'
	}
	if request.method == 'GET':
		context['form'] = DeleteCredentialForm(instance=credential)
		return render(request, 'form.jinja', context)
	if request.method == 'POST':
		context['form'] = DeleteCredentialForm(request.POST, instance=credential)
		if not context['form'].is_valid():
			return render(request, 'form.jinja', context)
		credential.delete()
		return redirect('index')


