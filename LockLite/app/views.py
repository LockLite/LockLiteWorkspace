from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .forms import CredentialForm
from .models import Credential


class CustomLoginView(LoginView):
	authentication_form = LoginForm
	link_page = "register"
	template_name = 'auth.jinja'
	extra_context = {
		'title': "Login",
		'link': {
			'text': "Don't have an account?",
			'name': link_page.capitalize(),
			'page': link_page
		}
	}


def register(request, *args, **kwargs):
	link_page = "login"
	context = {
		'title': "Register",
		'link': {
			'text': "Already has an account?",
			'name': link_page.capitalize(),
			'page': link_page
		}
	}
	if request.method == 'GET':
		context['form'] = RegisterForm()
		return render(request, 'auth.jinja', context)
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
			return render(request, 'auth.jinja', context)


@login_required(login_url="login")
def index(request, *args, **kwargs):
	data = {
		'name': request.user.username,
		'user': request.user.email,
		'credentials': Credential.objects.filter(user_id=request.user.id).values()
	}
	return render(request, 'index.jinja', data)


@login_required(login_url="login")
def createcred(request):
	if request.method == 'POST':
		form = CredentialForm(request.POST)
		if form.is_valid():
			credential = form.save()
			return redirect('index')
	else:
		form = CredentialForm()
		return render(request, 'createcred.jinja', {'form': form})
